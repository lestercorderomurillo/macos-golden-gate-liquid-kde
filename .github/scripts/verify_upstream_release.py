"""Extract Golden Gate's evidence checker from its verified Tahoe release."""
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile


def verify_upstream_release(repo: Path, output: Path) -> None:
    pin = json.loads((repo / 'upstream.json').read_text())
    version = (repo / 'VERSION').read_text().strip()
    repository = pin['repository']
    commit = pin['commit']
    if repository != 'lestercorderomurillo/macos-tahoe-liquid-kde':
        raise ValueError('Unexpected Tahoe repository')
    if not re.fullmatch('[a-f0-9]{40}', commit):
        raise ValueError('Tahoe pin must be an immutable commit')
    if not re.fullmatch(r'\d+\.\d+(?:\.\d+|rc[1-9]\d*)', version) or pin['version'] != version:
        raise ValueError('Golden Gate version differs from the Tahoe pin or is invalid')

    tag = 'refs/tags/v' + version
    result = subprocess.check_output(
        ['git', 'ls-remote', 'https://github.com/' + repository + '.git', tag, tag + '^{}'],
        text=True,
    )
    refs = {ref: sha for sha, ref in (line.split() for line in result.splitlines())}
    if refs.get(tag + '^{}', refs.get(tag)) != commit:
        raise ValueError('Tahoe tag differs from pin')

    archive = subprocess.check_output([
        'curl', '--fail', '--location', '--silent', '--show-error', '--max-time', '120',
        'https://codeload.github.com/' + repository + '/tar.gz/' + commit,
    ])
    if hashlib.sha256(archive).hexdigest() != pin['sha256']:
        raise ValueError('Tahoe archive checksum mismatch')
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as source:
        root = 'macos-tahoe-liquid-kde-' + commit + '/'
        if source.extractfile(root + 'VERSION').read().decode().strip() != version:
            raise ValueError('Tahoe archive version differs from pin')
        checker = source.extractfile(root + '.github/scripts/release_evidence.py').read()
    output.write_bytes(checker)


if __name__ == '__main__':
    verify_upstream_release(Path.cwd(), Path(os.environ['RUNNER_TEMP']) / 'tahoe-release-evidence.py')
