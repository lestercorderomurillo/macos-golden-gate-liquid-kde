#!/usr/bin/env python3
"""Small, offline dependency index for agent navigation, not a CI coverage gate."""
import argparse
import ast
from collections import defaultdict, deque
import json
from pathlib import Path
import re
import subprocess


def tracked(root):
    return subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')[:-1]


def graph(root):
    files = set(tracked(root))
    edges = defaultdict(set)
    modules = defaultdict(set)
    suffixes = defaultdict(set)
    for name in files:
        path = Path(name)
        for offset in range(len(path.parts)):
            suffixes['/'.join(path.parts[offset:])].add(name)
        if path.suffix in {'.py', '.qml', '.js'}:
            modules[path.stem].add(name)
    for name in sorted(files):
        path = root / name
        if path.suffix not in {'', '.py', '.qml', '.js', '.sh', '.bash', '.cmake', '.yml', '.yaml', '.cpp', '.c', '.h', '.hpp', '.cc', '.cxx'} and path.name != 'CMakeLists.txt':
            continue
        if path.is_symlink() or not path.is_file() or path.stat().st_size > 262144:
            continue
        try:
            text = path.read_text()
        except (UnicodeError, OSError):
            continue
        if '\0' in text:
            continue
        refs = set()
        if path.suffix == '.py':
            try:
                for node in ast.walk(ast.parse(text)):
                    if isinstance(node, ast.Import):
                        refs.update(a.name.split('.')[-1] for a in node.names)
                    elif isinstance(node, ast.ImportFrom):
                        refs.add((node.module or '').split('.')[-1])
                        refs.update(a.name for a in node.names)
            except SyntaxError:
                pass
        if path.suffix == '.qml':
            refs.update(re.findall(r'\b([A-Z]\w*)\s*\{', text))
        for ref in refs:
            candidates = modules.get(ref, ())
            local = {candidate for candidate in candidates
                     if Path(candidate).parent == Path(name).parent}
            # QML component names are scoped to their directory, not global.
            edges[name].update(local if path.suffix == '.qml' else local or candidates)
        # Literal paths and script names cover shell entry points and fixtures.
        literals = re.findall(r'''["']([^"'\n]+)["']''', text)
        if path.name == 'CMakeLists.txt' or path.suffix == '.cmake':
            literals += re.findall(r'[\w./+-]+\.(?:cpp|c|h|hpp|qml|py|js|cmake)\b', text)
        for ref in literals:
            candidates = {ref, (Path(name).parent / ref).as_posix()}
            edges[name].update(candidates & files)
            if Path(ref).suffix and not any(c.isspace() for c in ref):
                edges[name].update(suffixes.get(ref, ()))
        edges[name].discard(name)
    return files, edges


def impact(files, edges, changed):
    reverse = defaultdict(set)
    for caller, dependencies in edges.items():
        for dependency in dependencies:
            reverse[dependency].add(caller)
    reasons = {name: None for name in changed}
    queue = deque(sorted(changed))
    while queue:
        dependency = queue.popleft()
        for caller in sorted(reverse[dependency]):
            if caller not in reasons:
                reasons[caller] = dependency
                queue.append(caller)
    return {'changed': sorted(changed),
            'affected': reasons,
            'tests': [name for name in reasons if name.startswith('tests/') and Path(name).name.startswith('test_')],
            'unindexed': sorted(set(changed) - files),
            'limits': 'Navigation hints only: dynamic imports, generated paths, C++/SDK dependencies and runtime QML connections may be absent. No tests found does not mean no tests needed.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--limit', type=int, default=40, help='maximum affected paths displayed; 0 means all')
    parser.add_argument('--all', action='store_true', help='emit adjacency graph instead of impact')
    parser.add_argument('paths', nargs='*', help='changed paths relative to --repo; default: working diff against HEAD')
    args = parser.parse_args()
    root = args.repo.resolve()
    files, edges = graph(root)
    changed = args.paths or subprocess.check_output(
        ['git', 'diff', '--name-only', '-z', 'HEAD'], cwd=root).decode().split('\0')[:-1]
    result = {name: sorted(edges[name]) for name in sorted(edges) if edges[name]} if args.all else impact(files, edges, changed)
    if not args.all and args.limit > 0:
        result['affected_count'] = len(result['affected'])
        result['test_count'] = len(result['tests'])
        result['affected'] = dict(list(result['affected'].items())[:args.limit])
        result['tests'] = result['tests'][:args.limit]
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
