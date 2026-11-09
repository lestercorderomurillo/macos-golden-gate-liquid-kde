"""Exercise navigation through imports, literal paths, cycles and QML types."""
import importlib.util
from pathlib import Path
import subprocess

SPEC = importlib.util.spec_from_file_location('repo_graph', Path(__file__).resolve().parents[1] / 'tools/repo_graph.py')
graph = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(graph)


def test_transitive_impact_with_cycles_and_unindexed_files(tmp_path):
    subprocess.run(['git', 'init', '-q', str(tmp_path)], check=True)
    sources = {'core.py': 'import facade\n', 'facade.py': 'from core import run\n',
               'tests/test_feature.py': 'import facade\n', 'Other.qml': 'Item {}',
               'View.qml': 'Other {}', 'tests/test_view.py': 'fixture = "View.qml"',
               'CMakeLists.txt': 'add_executable(probe core.cpp)',
               'core.cpp': '#include "api.h"', 'api.h': '#pragma once',
               'tests/test_native.py': 'fixture = "CMakeLists.txt"',
               'unrelated.py': 'value = 3', 'binary.bin': '\0binary'}
    for name, source in sources.items():
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text(source)
    subprocess.run(['git', 'add', '.'], cwd=tmp_path, check=True)
    files, edges = graph.graph(tmp_path)
    result = graph.impact(files, edges, ['core.py', 'Other.qml', 'unknown.py', 'api.h'])
    assert sorted(result['tests']) == ['tests/test_feature.py', 'tests/test_native.py', 'tests/test_view.py']
    assert result['affected']['tests/test_feature.py'] == 'facade.py'
    assert result['affected']['tests/test_view.py'] == 'View.qml'
    assert result['unindexed'] == ['unknown.py']
    assert 'unrelated.py' not in result['affected']
