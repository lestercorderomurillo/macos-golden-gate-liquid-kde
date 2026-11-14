# Contributing

Golden Gate stages the shared Tahoe implementation with this edition's
defaults. See [Tahoe's contributor documentation](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md)
for development and installer lifecycle details.

## Installer storage maintenance

The recommended `--filter=blob:none` clone keeps full ancestry and downloads
historical files on demand. Audited clean published shallow clones created by
older instructions migrate through a filtered ancestry fetch; development
checkouts retain their history settings.

Ordinary installer launches maintain both the wrapper and an automatically
selected Tahoe sibling, including after manual `git pull`. Use
`./installer --free-space` (or `./install --free-space`) for an explicit run
with actual recovered-byte reporting. This verifies public cache ownership
without installing or updating. `MAC_TAHOE_NO_UPDATE_CHECK=true` forbids online
verification. The shared implementation lives only in Tahoe.

Clean canonical clones at an exactly verified published release keep `.git`,
full commit ancestry, canonical tags, main/dev positions and current branch
snapshots. Obsolete published large files become an origin-backed `blob:none`
cache; old file lookups download them as needed. Older-version merged branches
can retire with reference IDs/reflogs saved in
`.git/tahoe-maintenance-journal.json`. Dirty, divergent, unpublished or private
work is preserved; linked worktrees and shared stores are skipped. VERSION
alone never authorizes deletion. Explicit development overrides and read-only
entry points do not trigger automatic maintenance.

Unused prepared sources and interrupted downloads retire after a valid
replacement is ready; leases protect active installers. Settings, desktop
assets, recovery backups, arbitrary developer files, VMs and capture evidence
remain. See [Tahoe's maintenance policy](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md#installer-storage-maintenance)
for recovery, offline behavior and local opt-outs (`tahoe.maintenance compact`
or `off`). Repacking needs temporary space; savings depend on retained history.

## Optional Dock applications

The shared custom installer offers **Dock apps** in the Desktop step. It reuses
installed equivalents and installs only explicitly selected missing categories.
Native packages come from existing distro repositories; per-user Flatpak is an
explicit alternative, with separate consent to add Flathub. A failed optional
app leaves its category pending and does not abort the theme installation.
Removing the theme keeps these applications. The implementation and catalog
live exclusively in Tahoe; both editions use the same transaction choices.


## Dock icon appearance

In the custom installer, open **Desktop → Dock apps… → Dock appearance** and
choose **macOS-style Dock icons**. This is separate from optional app installation:
it uses installed Linux applications with consistent icons for Files, Browser,
Mail, Calendar, Notes, Photos, Music, Video, App Store and System Settings.
The tooltip retains the real application name. Other applications keep their
normal icons; launchers and running windows retain the same application identity.

**Keep current Dock icons** is the installer default and preserves each Dock's
choice, including during a layout reset. **Application icons** turns the option
off. It can also be toggled in the Dock widget's Appearance settings. Pins, their
order and the global icon theme are preserved. The bundled artwork has light and
dark variants and does not require changing the desktop icon theme.


### Dock migration in 0.64

Express uses automatic Dock appearance. Each Dock records `dockPresetRevision=3`
after applying the preset, installed application equivalents and macOS-style
role icons. Revisions 0, 1 and 2 migrate once, regardless of the release they
came from (including 0.61.0). The migration retains existing launchers in order
and appends missing installed roles; it never installs applications. Firefox
and other browsers retain their real application artwork and name.

An explicit layout reset reapplies the preset. Without reset, revision 3 keeps
removed pins and icon choices; explicit optional app requests can still add
the requested roles. `keep`, `native` and `macos` are explicit icon overrides;
`auto` applies the pictured icons only on initial migration or reset. Rebuilding
retains the revision per screen. Failed script execution can retry.

## Incremental installation

Tahoe maintains independent content fingerprints for payloads and individual
plasmoids, plus a receipt that avoids regenerating unchanged icons. Changes to
source recipes, relevant choices or installed files invalidate the affected
work. Configuration application and explicit resets still run as requested.
Maintain the shared ledger with `python src/scripts/component_manifest.py --write`
in Tahoe and commit it with component changes; Golden Gate stages that code
without copying the implementation here. See [the shared evidence and coverage
limits](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/v0.66.1/CONTRIBUTING.md#0661-validation-evidence).

## Publishing fixes

Run focused local checks and review component-scoped VM captures. Record their
source fingerprint, results and coverage limits in `release-evidence.json`, then
publish through `release.yml`. It checks that evidence and the published immutable
Tahoe pin/archive without waiting for full remote CI. Keep the complete remote
suite enabled and report pending or failed results honestly; a published fix is
available to install before full qualification finishes. Preserve historical
gallery provenance and link new focused previews separately.

Runtime CI runs on `dev`, pull requests and manual dispatch. Promote the same
commit to `main` without a second suite or a polling job; send runtime changes
through `dev` first. Markdown and documentation-image-only changes do not start
the runtime matrix. Use command results as delivery evidence instead of repeated
publication or branch lookups. Golden Gate validates the immutable Tahoe tag and
archive once, without waiting for or querying the GitHub release page.

## Agent navigation

`python3 tools/repo_graph.py bootstrap.py --limit 10` lists inferred callers
and relevant tests. Use `--repo ../macos-tahoe-liquid-kde` for shared code.
The index reads tracked source locally and never changes files or contacts an
AI service. Output is bounded by default; `--all` emits the full graph. Dynamic
imports and native dependencies still require review. This is a navigation
tool, not an automatic test-skipping gate.

## Appearance synchronization

Both editions share Tahoe's system appearance follower. Native KDE and GTK
selections synchronize the installed components; `mac-tahoe-theme-switch auto`
selects the 06:00/18:00 schedule, and a later manual selection supersedes it.
See the [implementation and qualification scope](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/docs/appearance-sync.md).
