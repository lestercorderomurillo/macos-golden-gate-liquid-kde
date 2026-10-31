# Contributing

Golden Gate stages the shared Tahoe implementation with this edition's
defaults. See [Tahoe's contributor documentation](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md)
for development and installer lifecycle details.

## Installer storage maintenance

After a verified update, the installer requests threshold-based Git maintenance
for its wrapper and automatically selected Tahoe sibling. Run
`./installer --free-space` or `./install --free-space` to compact their Git
storage explicitly and report actual recovered space without installing or
checking for newer releases. The shared maintenance implementation lives in
Tahoe; the wrapper uses its local source or verified fallback pin.

Unused prepared sources and interrupted downloads are retired after a valid
replacement is ready. Running installers retain their snapshots. Git maintenance
preserves `.git`, commits, branches, tags, stashes, reflogs and local files; it
skips linked worktrees and shared object stores. It never deletes desktop assets,
settings or uninstall backups. Referenced historical assets remain in Git, so
an already packed clone may recover little space. Repacking also needs temporary
disk space. Source overrides and read-only entry points never trigger automatic
maintenance.
