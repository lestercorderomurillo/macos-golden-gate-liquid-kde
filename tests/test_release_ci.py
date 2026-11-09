"""Publication verifies the immutable source without waiting for full remote CI."""
from pathlib import Path


def test_release_checks_local_evidence_and_published_tahoe_pin():
    repo = Path(__file__).resolve().parents[1]
    text = (repo / '.github/workflows/release.yml').read_text()
    assert 'require-ci.yml' not in text
    assert 'needs: source' in text.split('  publish:', 1)[1]
    assert 'ref: ${{ needs.source.outputs.commit }}' in text
    assert 'repository: lestercorderomurillo/macos-tahoe-liquid-kde' in text
    assert "assert tagged == pin['commit']" in text
    assert "assert digest.hexdigest() == pin['sha256']" in text
    assert 'python3 tahoe/.github/scripts/release_evidence.py --repo .' in text
    assert '--verify-tag --title' in text
    workflow = (repo / '.github/workflows/test.yml').read_text()
    assert 'branches: [main, dev]' in workflow
    assert 'python3 -m pytest tests -q' in workflow
