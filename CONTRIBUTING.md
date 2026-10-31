# Contributing

Golden Gate stages the shared Tahoe implementation with this edition's
defaults. See [Tahoe's contributor documentation](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md)
for development and installer lifecycle details.

## Installer storage maintenance

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
