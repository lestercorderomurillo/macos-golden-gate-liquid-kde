"""Exercise update decisions against real disposable git histories, without GitHub."""
import json
from pathlib import Path
import subprocess

import pytest
import bootstrap


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


def commit(root, message):
    git(root, 'add', '.')
    git(root, '-c', 'user.name=Update test', '-c', 'user.email=update@example.invalid',
        'commit', '-qm', message)
    return git(root, 'rev-parse', 'HEAD')


@pytest.fixture
def release_pair(tmp_path, monkeypatch):
    for key in ('MAC_TAHOE_NO_UPDATE_CHECK', 'GOLDEN_GATE_UPDATED', 'GOLDEN_GATE_TAHOE_SOURCE'):
        monkeypatch.delenv(key, raising=False)
    remote = tmp_path / 'published'
    remote.mkdir()
    git(remote, 'init', '-q')
    files = {'VERSION': '0.61.9\n', 'installer': '# installer\n',
             'bootstrap.py': '# wrapper\n', '.gitignore': 'build/\n',
             'defaults.json': '{"wallpaper":"MacGoldenGate"}',
             'upstream.json': json.dumps({'commit': 'a' * 40, 'sha256': '0' * 64}),
             'src/installer/installer_ui.py': '# UI\n',
             'src/scripts/defaults.json': '{"wallpaper":"MacTahoe"}',
             'src/scripts/launcher_defaults.py': '# defaults\n',
             'src/offline/wallpapers/MacGoldenGate/metadata.json': '{}'}
    for name, value in files.items():
        path = remote / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value)
    old = commit(remote, 'old release')
    wrapper = tmp_path / 'golden-gate'
    sibling = tmp_path / 'macos-tahoe-liquid-kde'
    for root in (wrapper, sibling):
        subprocess.run(['git', 'clone', '-q', str(remote), str(root)], check=True)
    (remote / 'VERSION').write_text('0.61.10\n')
    new = commit(remote, 'new release')
    git(remote, 'tag', 'v0.61.10')
    monkeypatch.setattr(bootstrap, 'ROOT', wrapper)
    monkeypatch.setattr(bootstrap, 'latest_release', lambda repo: 'v0.61.10')
    monkeypatch.setattr(bootstrap.os, 'geteuid', lambda: 1000)
    real_git = bootstrap._git
    fetches = []

    def local_git(*args, root=None):
        if args[0] == 'fetch':
            fetches.append(root or wrapper)
            args = ('fetch', '--no-tags', str(remote), args[-1])
        return real_git(*args, root=root)

    monkeypatch.setattr(bootstrap, '_git', local_git)
    restarts = []
    monkeypatch.setattr(bootstrap.os, 'execv', lambda *args: restarts.append(args))
    return wrapper, sibling, remote, old, new, fetches, restarts


@pytest.mark.parametrize('target', ['wrapper', 'sibling'])
@pytest.mark.parametrize('state', ['clean', 'modified', 'staged', 'untracked', 'deleted',
                                  'local-commit', 'equal', 'newer', 'offline', 'mismatch', 'fetch-failed'])
def test_update_preserves_testing_and_only_advances_verified_versions(release_pair, monkeypatch,
                                                                    target, state, capsys):
    wrapper, sibling, remote, old, new, fetches, restarts = release_pair
    root = wrapper if target == 'wrapper' else sibling
    if state in ('modified', 'staged'):
        (root / 'installer').write_text('# local test\n')
        if state == 'staged':
            git(root, 'add', 'installer')
    elif state == 'untracked':
        (root / 'experiment.py').write_text('# local test\n')
        git(root, 'config', 'status.showUntrackedFiles', 'no')
    elif state == 'deleted':
        (root / 'src/scripts/launcher_defaults.py').unlink()
    elif state == 'local-commit':
        (root / 'experiment.py').write_text('# committed test\n')
        commit(root, 'local experiment')
    elif state in ('equal', 'newer'):
        (root / 'VERSION').write_text('0.61.10\n' if state == 'equal' else '0.62.0\n')
        commit(root, 'testing version')
    elif state == 'offline':
        monkeypatch.setattr(bootstrap, 'latest_release', lambda repo: None)
    elif state == 'mismatch':
        git(remote, 'tag', '-f', 'v0.61.10', old)
    elif state == 'fetch-failed':
        git(remote, 'tag', '-d', 'v0.61.10')
    before = git(root, 'rev-parse', 'HEAD')
    status = git(root, 'status', '--porcelain', '--untracked-files=all')
    files = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*')
             if p.is_file() and '.git' not in p.relative_to(root).parts}
    if target == 'wrapper':
        bootstrap.update_wrapper('installer', [])
    else:
        # Deleting a required file makes a sibling incomplete: exercise the
        # update decision directly to prove deletions cannot be overwritten.
        monkeypatch.setattr(bootstrap, 'local_source', lambda: sibling)
        bootstrap.update_local_source('installer', [])
    if state == 'clean':
        assert git(root, 'rev-parse', 'HEAD') == new
        assert (root / 'VERSION').read_text().strip() == '0.61.10'
        assert bool(restarts) == (target == 'wrapper')
        assert fetches == [root]
    else:
        assert git(root, 'rev-parse', 'HEAD') == before
        assert git(root, 'status', '--porcelain', '--untracked-files=all') == status
        assert all((root / name).read_bytes() == value for name, value in files.items())
        assert not restarts
        if state not in ('equal', 'newer', 'offline'):
            assert 'Keeping local' in capsys.readouterr().out or state in ('mismatch', 'fetch-failed')
    other = sibling if target == 'wrapper' else wrapper
    assert git(other, 'rev-parse', 'HEAD') == old


@pytest.mark.parametrize('entry,args,env', [
    ('installer', [], {'GOLDEN_GATE_TAHOE_SOURCE': 'explicit'}),
    ('installer', [], {'MAC_TAHOE_NO_UPDATE_CHECK': 'true'}),
    ('installer', ['--prepare'], {}), ('installer', ['--check-update'], {}),
    ('installer', ['--help'], {}), ('installer', ['--uninstall'], {}),
    ('uninstall', [], {}), ('test', [], {}), ('vm', [], {}),
])
def test_explicit_testing_and_read_only_entries_never_update(release_pair, monkeypatch, entry, args, env):
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr(bootstrap, 'latest_release', lambda *a: pytest.fail('network check'))
    bootstrap.update_wrapper(entry, args)
    bootstrap.update_local_source(entry, args)
    assert not release_pair[-2] and not release_pair[-1]


def test_changes_arriving_during_fetch_are_preserved(release_pair, monkeypatch):
    wrapper, sibling, remote, old, new, fetches, restarts = release_pair
    previous = bootstrap._git
    def edit_during_fetch(*args, **kwargs):
        result = previous(*args, **kwargs)
        if args[0] == 'fetch':
            (sibling / 'installer').write_text('# editing while update checks\n')
        return result
    monkeypatch.setattr(bootstrap, '_git', edit_during_fetch)
    bootstrap.update_local_source('installer', [])
    assert git(sibling, 'rev-parse', 'HEAD') == old
    assert (sibling / 'installer').read_text() == '# editing while update checks\n'


def test_installer_launch_updates_both_then_stages_new_source(release_pair, monkeypatch):
    wrapper, sibling, remote, old, new, fetches, restarts = release_pair
    monkeypatch.setattr(bootstrap.os, 'chdir', lambda path: None)
    assert bootstrap.main('installer', []) == 0
    assert git(wrapper, 'rev-parse', 'HEAD') == new
    assert git(sibling, 'rev-parse', 'HEAD') == new
    assert fetches == [wrapper, sibling]
    staged = Path(restarts[-1][1][-1]).parent
    assert staged != sibling
    assert (staged / 'VERSION').read_text().strip() == '0.61.10'
    assert json.loads((staged / 'src/scripts/defaults.json').read_text())['wallpaper'] == 'MacGoldenGate'
    assert json.loads((sibling / 'src/scripts/defaults.json').read_text())['wallpaper'] == 'MacTahoe'


def test_incomplete_development_sibling_is_not_silently_replaced(release_pair):
    sibling = release_pair[1]
    (sibling / 'src/scripts/launcher_defaults.py').unlink()
    with pytest.raises(ValueError, match='unfinished changes'):
        bootstrap.local_source()
    assert not (sibling / 'src/scripts/launcher_defaults.py').exists()
    assert not release_pair[-2]


def test_developer_launch_stages_local_work_instead_of_new_release(release_pair, monkeypatch):
    wrapper, sibling, remote, old, new, fetches, restarts = release_pair
    (wrapper / 'bootstrap.py').write_text('# wrapper experiment\n')
    (sibling / 'experiment.py').write_text('# theme experiment\n')
    monkeypatch.setattr(bootstrap.os, 'chdir', lambda path: None)
    assert bootstrap.main('installer', []) == 0
    assert not fetches
    assert git(wrapper, 'rev-parse', 'HEAD') == old
    assert git(sibling, 'rev-parse', 'HEAD') == old
    staged = Path(restarts[-1][1][-1]).parent
    assert (staged / 'VERSION').read_text().strip() == '0.61.9'
    assert (staged / 'experiment.py').read_text() == '# theme experiment\n'
    assert (wrapper / 'bootstrap.py').read_text() == '# wrapper experiment\n'
