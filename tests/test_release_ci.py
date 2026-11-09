"""Publication verifies the immutable source without waiting for full remote CI."""
from pathlib import Path


def test_release_checks_local_evidence_and_published_tahoe_pin():
    repo = Path(__file__).resolve().parents[1]
    text = (repo / '.github/workflows/release.yml').read_text()
    assert 'require-ci.yml' not in text
    assert '  source:' not in text and 'needs:' not in text
    assert 'gh release view' not in text and 'time.sleep' not in text
    assert 'for attempt in range' not in text
    assert not (repo / '.github/workflows/require-ci.yml').exists()
    assert 'ref: ${{ steps.pin.outputs.commit }}' in text
    assert 'repository: lestercorderomurillo/macos-tahoe-liquid-kde' in text
    assert "assert tagged == pin['commit']" in text
    assert "assert digest.hexdigest() == pin['sha256']" in text
    assert 'python3 tahoe/.github/scripts/release_evidence.py --repo .' in text
    assert '--verify-tag --title' in text
    workflow = (repo / '.github/workflows/test.yml').read_text()
    push, remainder = workflow.split('  push:\n', 1)[1].split('  pull_request:\n', 1)
    assert 'branches: [dev]' in push
    assert 'branches: [main, dev]' in remainder
    assert 'workflow_dispatch:' in workflow
    assert "paths-ignore: ['**/*.md', 'src/screenshots/**']" in push
    assert 'promotion:' not in workflow
    assert 'python3 -m pytest tests -q' in workflow
