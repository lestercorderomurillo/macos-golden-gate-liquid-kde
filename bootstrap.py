"""Use local Tahoe sources when available, otherwise fetch a published release."""

import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import pwd
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parent
ENTRY_POINTS = {"install", "uninstall", "installer", "test", "vm"}
# Entry points that fast-forward this checkout before running.
UPDATE_ENTRY_POINTS = {"install", "installer"}
TAHOE_REPOSITORY = "lestercorderomurillo/macos-tahoe-liquid-kde"
GOLDEN_GATE_REPOSITORY = "lestercorderomurillo/macos-golden-gate-liquid-kde"
RELEASES_URL = f"https://github.com/{GOLDEN_GATE_REPOSITORY}/releases/latest"


def active_prepared(cache: Path) -> set[Path] | None:
    """Older wrappers have no lease; their entry points still run in the source."""
    active = set()
    try:
        processes = list(Path("/proc").iterdir())
    except OSError:
        return None  # Cannot establish whether legacy snapshots are in use.
    for process in processes:
        if not process.name.isdecimal():
            continue
        try:
            relative = Path(os.readlink(process / "cwd")).relative_to(cache)
        except (OSError, ValueError):
            continue
        if relative.parts:
            active.add(cache / relative.parts[0])
    return active


def prune_prepared(cache: Path, current: Path) -> None:
    """Retire only wrapper snapshots, after their replacement is ready.

    A running entry point holds a shared lock on its ready marker. Never
    unlink a locked snapshot: the wizard and its backend still import it.
    """
    active = active_prepared(cache)
    for previous in cache.iterdir():
        # The caller owns .prepare.lock; no extraction can still be using
        # these TemporaryDirectory names left behind by an interrupted run.
        if (not previous.is_symlink() and previous.is_dir()
                and re.fullmatch(r"\.prepare-[a-z0-9_]{8}", previous.name)):
            try:
                shutil.rmtree(previous)
            except OSError as exc:
                print(f"Golden Gate: could not remove interrupted download {previous}: {exc}", file=sys.stderr)
            continue
        if (active is None or previous in active
                or previous == current or previous.is_symlink()
                or not previous.is_dir()
                or not re.fullmatch(r"[0-9a-f]{20}", previous.name)):
            continue
        marker = previous / ".golden-gate-ready"
        try:
            fd = os.open(marker, os.O_RDONLY | os.O_NOFOLLOW)
            with os.fdopen(fd) as lease:
                if not re.fullmatch(r"(?:local-development|[0-9a-f]{40})\n", lease.read()):
                    continue
                try:
                    fcntl.flock(lease, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    continue
                shutil.rmtree(previous)
        except FileNotFoundError:
            continue
        except OSError as exc:
            print(f"Golden Gate: could not remove old cache {previous}: {exc}", file=sys.stderr)


def lease_prepared(target: Path) -> int:
    """Keep the snapshot alive across exec until the entry point exits."""
    fd = os.open(target / ".golden-gate-ready", os.O_RDONLY | os.O_NOFOLLOW)
    try:
        fcntl.flock(fd, fcntl.LOCK_SH)
        os.set_inheritable(fd, True)
    except BaseException:
        os.close(fd)
        raise
    return fd


def extract_archive(archive: Path, destination: Path) -> Path:
    """Extract regular files first, then contained relative symbolic links."""
    with tarfile.open(archive, "r:gz") as tar:
        members = tar.getmembers()
        roots = set()
        seen = set()
        for member in members:
            path = PurePosixPath(member.name)
            if path.is_absolute() or ".." in path.parts or not path.parts:
                raise ValueError("Unsafe archive path")
            if path in seen:
                raise ValueError("Duplicate archive path")
            seen.add(path)
            roots.add(path.parts[0])
            if member.issym():
                target = PurePosixPath(posixpath.normpath(str(path.parent / member.linkname)))
                if (PurePosixPath(member.linkname).is_absolute()
                        or not target.parts or target.parts[0] != path.parts[0]
                        or ".." in target.parts):
                    raise ValueError("Archive link escapes the source tree")
            elif not (member.isfile() or member.isdir()):
                raise ValueError("Unsupported archive member")
        if len(roots) != 1:
            raise ValueError("Expected one archive root")
        for member in members:
            path = destination / member.name
            if member.isdir():
                path.mkdir(parents=True, exist_ok=True)
            elif member.isfile():
                path.parent.mkdir(parents=True, exist_ok=True)
                with tar.extractfile(member) as source, path.open("xb") as output:
                    shutil.copyfileobj(source, output)
                path.chmod(0o755 if member.mode & 0o111 else 0o644)
        for member in members:
            if member.issym():
                path = destination / member.name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.symlink_to(member.linkname)
    return destination / roots.pop()


def _version(text: str) -> tuple[int, ...]:
    return tuple(int(part) for part in re.findall(r"\d+", text)[:3])


def _github(path: str, accept: str = "application/vnd.github+json") -> bytes | None:
    request = urllib.request.Request(f"https://api.github.com/repos/{path}",
                                     headers={"Accept": accept, "User-Agent": "GoldenGate-KDE"})
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            return response.read()
    except (OSError, ValueError):
        return None


def latest_release(repository: str) -> str | None:
    """The newest published release tag, or None when GitHub can't answer."""
    data = _github(f"{repository}/releases/latest")
    try:
        tag = json.loads(data)["tag_name"] if data else None
    except (ValueError, KeyError, TypeError):
        return None
    return tag if isinstance(tag, str) and re.fullmatch(r"v\d+\.\d+\.\d+", tag) else None


def latest_tahoe() -> dict | None:
    """The newest published Tahoe release and its commit."""
    tag = latest_release(TAHOE_REPOSITORY)
    sha = _github(f"{TAHOE_REPOSITORY}/commits/{tag}", "application/vnd.github.sha") if tag else None
    commit = sha.decode(errors="replace").strip() if sha else ""
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        return None
    return {"repository": TAHOE_REPOSITORY, "commit": commit, "version": tag[1:]}


def download(pin: dict, destination: Path) -> None:
    commit = pin["commit"]
    if not isinstance(commit, str) or len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit):
        raise ValueError("Publish and pin Tahoe's edition support first, or set "
                         "GOLDEN_GATE_TAHOE_SOURCE to a local Tahoe checkout")
    url = ("https://codeload.github.com/lestercorderomurillo/"
           f"macos-tahoe-liquid-kde/tar.gz/{commit}")
    print("Downloading shared Tahoe implementation…", flush=True)
    request = urllib.request.Request(url, headers={"User-Agent": "GoldenGate-KDE"})
    digest = hashlib.sha256()
    with urllib.request.urlopen(request, timeout=60) as response, destination.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            digest.update(chunk)
            output.write(chunk)
    # A release is checked against its VERSION after extraction; the
    # offline fallback pin carries its own archive digest.
    if "version" not in pin and digest.hexdigest() != pin.get("sha256"):
        raise ValueError("Tahoe archive checksum mismatch; refusing to run it")


def local_files(source: Path) -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(source), "ls-files", "--cached", "--others",
         "--exclude-standard", "-z"], check=True, capture_output=True)
    # ls-files includes tracked deletions in an in-progress rewrite.
    return sorted(name for name in set(result.stdout.decode().split("\0"))
                  if name and ((source / name).is_file() or (source / name).is_symlink()))


def local_source() -> Path | None:
    """An explicit checkout wins, then the sibling repository; never modify it."""
    explicit = os.environ.get("GOLDEN_GATE_TAHOE_SOURCE")
    source = (Path(explicit).expanduser() if explicit else
              ROOT.parent / "macos-tahoe-liquid-kde").resolve()
    required = ("VERSION", "installer", "src/installer/installer_ui.py",
                "src/scripts/defaults.json", "src/scripts/launcher_defaults.py",
                "src/offline/wallpapers/MacGoldenGate/metadata.json")
    if all((source / name).is_file() for name in required):
        return source
    if explicit:
        raise ValueError(f"Incomplete local Tahoe source: {source}")
    if (source / ".git").exists():
        status = _git("status", "--porcelain", "--untracked-files=all", root=source)
        if status is not None and status.returncode == 0 and status.stdout.strip():
            raise ValueError(f"Local Tahoe source has unfinished changes and missing required files: "
                             f"{source}. Restore the missing files to test this checkout.")
    return None


def apply_defaults(source: Path, defaults: dict) -> None:
    package = defaults.get("wallpaper")
    if package not in ("MacTahoe", "MacGoldenGate"):
        raise ValueError("Unsupported wallpaper default")
    config = source / "src/scripts/defaults.json"
    wallpaper = source / "src/offline/wallpapers" / package
    if not config.is_file() or not (wallpaper / "metadata.json").is_file():
        raise ValueError("Pinned Tahoe source lacks edition support or wallpapers")
    preset = defaults.get("launcher_preset", 1)
    if type(preset) is not int or preset not in (1, 2):
        raise ValueError("Unsupported launcher preset default")
    if "launcher_preset" in defaults and not (source / "src/scripts/launcher_defaults.py").is_file():
        raise ValueError("Pinned Tahoe source lacks launcher presets; publish and pin "
                         "the shared update, or set GOLDEN_GATE_TAHOE_SOURCE to "
                         "the updated local Tahoe checkout")
    config.write_text(json.dumps(defaults, indent=2) + "\n")


def prepare(*, lease: bool = False) -> Path:
    # Resolve local development sources before making any network request.
    pin = json.loads((ROOT / "upstream.json").read_text())
    defaults = json.loads((ROOT / "defaults.json").read_text())
    source = local_source()
    if source is None and os.environ.get("MAC_TAHOE_NO_UPDATE_CHECK", "").lower() != "true":
        pin = latest_tahoe() or pin
    digest = hashlib.sha256((ROOT / "bootstrap.py").read_bytes())
    digest.update(json.dumps([pin, defaults], sort_keys=True).encode())
    files = local_files(source) if source else []
    for name in files:
        path = source / name
        digest.update(name.encode())
        digest.update(str(path.lstat().st_mode).encode())
        digest.update(os.readlink(path).encode() if path.is_symlink() else path.read_bytes())
    cache = ROOT / "build"
    cache.mkdir(exist_ok=True)
    target = cache / digest.hexdigest()[:20]
    with (cache / ".prepare.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if target.is_symlink():
            raise ValueError("Prepared source must not be a symbolic link")
        if (target / ".golden-gate-ready").is_symlink():
            raise ValueError("Prepared source marker must not be a symbolic link")
        if (target / ".golden-gate-ready").is_file():
            if lease:
                lease_prepared(target)
            prune_prepared(cache, target)
            return target
        with tempfile.TemporaryDirectory(prefix=".prepare-", dir=cache) as temporary:
            staging = Path(temporary)
            if source:
                checkout = staging / "source"
                for name in files:
                    destination = checkout / name
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source / name, destination, follow_symlinks=False)
            else:
                archive = staging / "tahoe.tar.gz"
                download(pin, archive)
                checkout = extract_archive(archive, staging / "unpacked")
                if "version" in pin and (checkout / "VERSION").read_text().strip() != pin["version"]:
                    raise ValueError("Tahoe release archive does not match its version")
            apply_defaults(checkout, defaults)
            (checkout / ".golden-gate-ready").write_text(
                ("local-development" if source else pin["commit"]) + "\n")
            checkout.rename(target)
        if lease:
            lease_prepared(target)
        prune_prepared(cache, target)
    return target


def _git(*args: str, root: Path | None = None) -> subprocess.CompletedProcess | None:
    """Run git in this checkout as the invoking user; pulling as root would
    leave root-owned objects."""
    env = dict(os.environ)
    drop = None
    if os.geteuid() == 0 and os.environ.get("SUDO_UID") and os.environ.get("SUDO_GID"):
        uid, gid = int(os.environ["SUDO_UID"]), int(os.environ["SUDO_GID"])
        user = pwd.getpwuid(uid)
        env["HOME"] = user.pw_dir

        def drop():
            os.initgroups(user.pw_name, gid)
            os.setresgid(gid, gid, gid)
            os.setresuid(uid, uid, uid)
    try:
        return subprocess.run(["git", "-C", str(root or ROOT), *args], capture_output=True, text=True,
                              timeout=120, env=env, preexec_fn=drop, check=False)
    except (OSError, subprocess.SubprocessError):
        return None


def _clean_checkout(root: Path | None = None) -> bool:
    root = root or ROOT
    if not (root / ".git").exists():
        return False
    git = _git if root == ROOT else lambda *args: _git(*args, root=root)
    top = git("rev-parse", "--show-toplevel")
    if top is None or top.returncode != 0 or Path(top.stdout.strip()).resolve() != root:
        return False
    status = git("status", "--porcelain", "--untracked-files=all")
    return status is not None and status.returncode == 0 and not status.stdout.strip()


def _update_checkout(root: Path, repository: str, label: str) -> bool:
    """Only a newer published VERSION and a clean fast-forward may change files."""
    try:
        current = (root / "VERSION").read_text().strip()
    except OSError:
        return False
    if not re.fullmatch(r"\d+\.\d+\.\d+", current):
        return False
    latest = latest_release(repository)
    if not latest or _version(latest) <= _version(current):
        return False
    available = f"{label} {latest} is available (local v{current})."
    release_url = f"https://github.com/{repository}/releases/tag/{latest}"
    if not _clean_checkout(root):
        print(f"{available} Keeping local source: changes present or not a clean git checkout. "
              f"{release_url}", flush=True)
        return False

    git = _git if root == ROOT else lambda *args: _git(*args, root=root)

    def git_ok(*args):
        result = git(*args)
        return result if result is not None and result.returncode == 0 else None

    fetched = git_ok("fetch", "--no-tags", f"https://github.com/{repository}.git",
                     "refs/tags/" + latest)
    target = git_ok("rev-parse", "FETCH_HEAD^{commit}") if fetched is not None else None
    commit = target.stdout.strip() if target is not None else ""
    version = git_ok("show", commit + ":VERSION") if re.fullmatch(r"[0-9a-f]{40}", commit) else None
    if version is None or version.stdout.strip() != latest.removeprefix("v"):
        print(f"{available} Could not verify the published update; keeping local source. "
              f"{release_url}", flush=True)
        return False
    if git_ok("merge-base", "--is-ancestor", "HEAD", commit) is None:
        print(f"{available} Keeping local commits: the release is not a fast-forward. "
              f"{release_url}", flush=True)
        return False
    if not _clean_checkout(root) or git_ok("merge", "--ff-only", commit) is None:
        print(f"{available} Could not safely update; keeping local source. "
              f"{release_url}", flush=True)
        return False
    print(f"Updated {label}: v{current} → {latest}", flush=True)
    return True


def _updates_enabled(entry: str, args: list[str]) -> bool:
    return (entry in UPDATE_ENTRY_POINTS
            and not any(arg in args for arg in
                        ("--prepare", "--check-update", "--free-space", "--help", "-h", "--uninstall", "--supervise"))
            and not os.environ.get("GOLDEN_GATE_TAHOE_SOURCE")
            and os.environ.get("MAC_TAHOE_NO_UPDATE_CHECK", "").lower() != "true")


def update_wrapper(entry: str, args: list[str]) -> None:
    """Update the wrapper independently of an automatically discovered sibling."""
    if not _updates_enabled(entry, args) or os.environ.get("GOLDEN_GATE_UPDATED") == "1":
        return
    if not _update_checkout(ROOT, GOLDEN_GATE_REPOSITORY, "Golden Gate"):
        return
    os.environ["GOLDEN_GATE_UPDATED"] = "1"
    try:
        os.execv(sys.executable, [sys.executable, str(ROOT / entry), *args])
    except OSError:
        os.environ.pop("GOLDEN_GATE_UPDATED", None)


def update_local_source(entry: str, args: list[str]) -> bool:
    """An implicit sibling follows releases unless it contains local test work."""
    if not _updates_enabled(entry, args):
        return False
    source = local_source()
    if source is not None:
        return _update_checkout(source, TAHOE_REPOSITORY, "Tahoe")
    return False


def main(entry: str = "installer", args: list[str] | None = None) -> int:
    if entry not in ENTRY_POINTS:
        raise ValueError("Unknown entry point")
    args = sys.argv[1:] if args is None else args
    original_uid, original_gid = os.geteuid(), os.getegid()
    try:
        if args == ["--free-space"]:
            # Maintenance uses the local source or verified offline pin, never
            # queries or installs a newer release as a side effect.
            os.environ["MAC_TAHOE_NO_UPDATE_CHECK"] = "true"
        update_wrapper(entry, args)
        source_updated = update_local_source(entry, args)
        # sudo entry points retain their root hop for Tahoe's own privilege
        # handling; downloads and extraction belong to the invoking user.
        if original_uid == 0 and os.environ.get("SUDO_UID"):
            os.setegid(int(os.environ["SUDO_GID"]))
            os.seteuid(int(os.environ["SUDO_UID"]))
        source = prepare(lease=args != ["--prepare"])
        maintenance = source / "src/scripts/repository_maintenance.py"
        roots = [ROOT]
        sibling = local_source()
        if sibling is not None:
            roots.append(sibling)
        maintenance_args = [arg for root in roots for arg in ("--repository", str(root))]
        if (_updates_enabled(entry, args) and maintenance.is_file()
                and (source_updated or os.environ.get("GOLDEN_GATE_UPDATED") == "1")):
            try:
                result = subprocess.run([sys.executable, str(maintenance), "--auto", *maintenance_args],
                                        check=False, timeout=660)
                if result.returncode:
                    print("Golden Gate: Git maintenance did not finish; continuing with the update.", file=sys.stderr)
            except (OSError, subprocess.SubprocessError) as exc:
                print(f"Golden Gate: Git maintenance did not finish: {exc}", file=sys.stderr)
    except (OSError, ValueError, tarfile.TarError, subprocess.SubprocessError) as exc:
        print(f"Golden Gate: {exc}", file=sys.stderr)
        return 1
    finally:
        if os.geteuid() != original_uid:
            os.seteuid(original_uid)
            os.setegid(original_gid)
    # Keep the selected local snapshot or release throughout this invocation.
    os.environ["MAC_TAHOE_NO_UPDATE_CHECK"] = "true"
    if args == ["--prepare"]:
        print(source)
        return 0
    if args == ["--free-space"]:
        if not maintenance.is_file():
            print("Golden Gate: this Tahoe source does not support --free-space yet.", file=sys.stderr)
            return 1
        os.execv(sys.executable, [sys.executable, str(maintenance), *maintenance_args])
        return 0
    os.chdir(source)
    os.execv(sys.executable, [sys.executable, str(source / entry), *args])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
