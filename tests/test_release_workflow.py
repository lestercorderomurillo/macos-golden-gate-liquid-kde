"""Execute the archive gate used by the release workflow, without network access."""
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import textwrap

import pytest


@pytest.mark.parametrize('damage', [None, 'tag', 'checksum', 'version'])
def test_pinned_release_checker_is_taken_only_from_verified_archive(tmp_path, monkeypatch, damage):
    workflow = Path(__file__).resolve().parents[1] / '.github/workflows/release.yml'
    script = textwrap.dedent(workflow.read_text().split("          python3 - <<'PYCODE'\n", 1)[1].split('          PYCODE', 1)[0])
    commit = 'a' * 40
    payload = io.BytesIO()
    with tarfile.open(fileobj=payload, mode='w:gz') as archive:
        for name, contents in [('VERSION', b'wrong' if damage == 'version' else b'1.2.3\n'),
                               ('.github/scripts/release_evidence.py', b'# verified checker\n')]:
            info = tarfile.TarInfo('macos-tahoe-liquid-kde-' + commit + '/' + name)
            info.size = len(contents)
            archive.addfile(info, io.BytesIO(contents))
    data = payload.getvalue()
    pin = {'repository': 'lestercorderomurillo/macos-tahoe-liquid-kde', 'commit': commit,
           'version': '1.2.3', 'sha256': '0' * 64 if damage == 'checksum' else hashlib.sha256(data).hexdigest()}
    (tmp_path / 'upstream.json').write_text(json.dumps(pin))
    (tmp_path / 'VERSION').write_text('1.2.3\n')
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv('RUNNER_TEMP', str(tmp_path))
    monkeypatch.setattr(subprocess, 'check_output', lambda args, **k:
                        data if args[0] == 'curl' else ('b' * 40 if damage == 'tag' else commit) + '\trefs/tags/v1.2.3\n')
    if damage:
        with pytest.raises(AssertionError):
            exec(compile(script, str(workflow), 'exec'), {})
        assert not (tmp_path / 'tahoe-release-evidence.py').exists()
    else:
        exec(compile(script, str(workflow), 'exec'), {})
        assert (tmp_path / 'tahoe-release-evidence.py').read_bytes() == b'# verified checker\n'
