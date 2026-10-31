"""The wrapper delegates maintenance to Tahoe without updating sources."""

import subprocess
import sys

import pytest
import bootstrap


@pytest.mark.parametrize("entry", ["install", "installer"])
def test_explicit_cleanup_uses_shared_code_and_both_checkouts(tmp_path, monkeypatch, entry):
    root = tmp_path / "golden"
    root.mkdir()
    sibling = tmp_path / "tahoe"
    sibling.mkdir()
    prepared = tmp_path / "prepared"
    scripts = prepared / "src/scripts"
    scripts.mkdir(parents=True)
    shared = scripts / "repository_maintenance.py"
    shared.write_text("# shared code")
    monkeypatch.setattr(bootstrap, "ROOT", root)
    monkeypatch.setattr(bootstrap, "local_source", lambda: sibling)
    monkeypatch.setattr(bootstrap, "prepare", lambda **kw: prepared)
    monkeypatch.setattr(bootstrap, "latest_release", lambda *a: pytest.fail("update query"))
    monkeypatch.setenv("MAC_TAHOE_NO_UPDATE_CHECK", "false")
    calls = []
    monkeypatch.setattr(bootstrap.os, "execv", lambda binary, args: calls.append((binary, args)))
    assert bootstrap.main(entry, ["--free-space"]) == 0
    assert calls == [(sys.executable, [sys.executable, str(shared),
                                      "--repository", str(root), "--repository", str(sibling)])]
    assert bootstrap.os.environ["MAC_TAHOE_NO_UPDATE_CHECK"] == "true"


def test_old_local_source_reports_unsupported_maintenance(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(bootstrap, "prepare", lambda **kw: tmp_path)
    monkeypatch.setattr(bootstrap, "local_source", lambda: None)
    monkeypatch.setenv("MAC_TAHOE_NO_UPDATE_CHECK", "true")
    assert bootstrap.main("installer", ["--free-space"]) == 1
    assert "does not support --free-space" in capsys.readouterr().err


@pytest.mark.parametrize("entry", ["uninstall", "test", "vm"])
def test_non_installer_entries_do_not_run_maintenance(tmp_path, monkeypatch, entry):
    monkeypatch.setattr(bootstrap, "prepare", lambda **kw: tmp_path)
    monkeypatch.setattr(bootstrap, "local_source", lambda: None)
    monkeypatch.setattr(bootstrap.os, "chdir", lambda *a: None)
    launches = []
    monkeypatch.setattr(bootstrap.os, "execv", lambda *a: launches.append(a))
    monkeypatch.setenv("MAC_TAHOE_NO_UPDATE_CHECK", "true")
    assert bootstrap.main(entry, ["--free-space"]) == 0
    assert launches[0][1] == [sys.executable, str(tmp_path / entry), "--free-space"]


@pytest.mark.parametrize("failure", ["returncode", "timeout", "missing"])
def test_auto_maintenance_failure_does_not_stop_updated_installer(tmp_path, monkeypatch, failure):
    scripts = tmp_path / "src/scripts"
    scripts.mkdir(parents=True)
    (scripts / "repository_maintenance.py").write_text("# shared code")
    monkeypatch.setattr(bootstrap, "prepare", lambda **kw: tmp_path)
    monkeypatch.setattr(bootstrap, "local_source", lambda: None)
    monkeypatch.setattr(bootstrap, "update_wrapper", lambda *a: None)
    monkeypatch.setattr(bootstrap, "update_local_source", lambda *a: True)
    monkeypatch.delenv("GOLDEN_GATE_TAHOE_SOURCE", raising=False)
    monkeypatch.setenv("MAC_TAHOE_NO_UPDATE_CHECK", "false")
    def run(command, **kw):
        assert "--auto" in command
        if failure == "timeout":
            raise subprocess.TimeoutExpired(command, 660)
        if failure == "missing":
            raise FileNotFoundError(command[0])
        return subprocess.CompletedProcess(command, 1)
    monkeypatch.setattr(bootstrap.subprocess, "run", run)
    monkeypatch.setattr(bootstrap.os, "chdir", lambda *a: None)
    launches = []
    monkeypatch.setattr(bootstrap.os, "execv", lambda *a: launches.append(a))
    assert bootstrap.main("installer", []) == 0
    assert launches[0][1] == [sys.executable, str(tmp_path / "installer")]
