# Installer testing

Native installer screens for Golden Gate 0.61.8, captured in a disposable KDE Plasma VM.
The gallery is captured from the release source and reviewed before publication.
Release checks cover both editions, theme switching, installation, reboot and removal.

Run `./installer` from this checkout to review the wizard. For shared test commands and the capture workflow, see [Tahoe CONTRIBUTING.md](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md).

## v0.61.8 focused validation

On 2026-10-27, 171 focused checks passed on the shared Tahoe source and the
same 171 passed on prepared Golden Gate content `9d2e8e8532812762e034`.
The checks used Python 3.14 with offscreen Qt on the maintainer's Linux host:
window controls, shadows, GTK upgrade/geometry, wizard navigation and summary,
installer supervision, CLI choices and Nix staging. No native ABI changed.
Existing component and VM evidence below remains applicable to unchanged code.
All 45 wrapper checks also passed, covering source staging, release selection,
archive checksums and version handling. The required full CI runs on the exact
release commits; no duplicate local container matrix is used.

## v0.61.8 window controls and shadows

The installer offers Flat and Glassy controls with reviewed Nautilus close-ups,
rim highlights matched to the maintainer's reference and a separate Window
shadows page with four screenshot cards. Golden Gate starts with Glassy;
explicit choices survive navigation, summary edits and later light/dark switches.

The release uses a fresh complete 90-frame capture from the pinned disposable
VM, a matching immutable Tahoe pin and successful exact-commit CI on both
branches. Shared validation is recorded in [Tahoe TESTING.md](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/TESTING.md).

## v0.61.5 reset default validation

The shared installer starts with **Reset Dock and panel customization** checked.
Uncheck it to preserve the current layout. Golden Gate prepared content
`f4438e729918882ada4b` passed 160 wizard, CLI, UI and layout component checks,
including the checked default and retaining an unchecked choice during navigation.
The release uses a new complete capture from the pinned disposable KDE neon VM;
its gallery and immutable Tahoe pin are verified before publication.

## v0.61.4 validation

The wrapper suite passed 45 checks, including published-tag update selection,
version verification and dirty/diverged checkout protection. Preparing the local Tahoe candidate with
`GOLDEN_GATE_TAHOE_SOURCE` and `./installer --prepare` passed 38 affected
wizard/GTK checks, followed by nine final shadow regressions. After the Arch
login-defaults and GTK session fixes, the prepared source passed 112 affected
updater, wizard, KConfig, session-environment and shadow checks. Arch testing
matched the reporter's Plasma/KWin, Mesa and Firefox versions and covered
reinstall preservation/reset, skipping Nautilus, reboot, light/dark switching
and all four shadow levels. The VM GPU was VirGL rather than an RX 9060 XT.
The shared
implementation and disposable-VM evidence are described in
[Tahoe TESTING.md](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/TESTING.md).
The release workflow also requires successful push CI for both repositories'
exact `main` and `dev` release commits and verifies this edition's fresh,
reviewed screenshot bundle against the immutable Tahoe pin.

## Installation steps

Scroll horizontally through the installation steps.

<table>
<tr>
  <td align="center"><img src="src/screenshots/installer-welcome_v1-7d2d14822ff3.png" alt="Welcome" width="500"><br>Welcome</td>
  <td align="center"><img src="src/screenshots/installer-appearance_v1-5983201d6502.png" alt="Appearance" width="500"><br>Appearance</td>
  <td align="center"><img src="src/screenshots/installer-icons_v1-821a7b881aab.png" alt="Icons and color" width="500"><br>Icons and color</td>
  <td align="center"><img src="src/screenshots/installer-wallpaper_v1-b0d495268582.png" alt="Wallpaper" width="500"><br>Wallpaper</td>
  <td align="center"><img src="src/screenshots/installer-launcher_v1-793f94230455.png" alt="Launcher" width="500"><br>Launcher</td>
  <td align="center"><img src="src/screenshots/installer-layout_v1-1bc63d9527fd.png" alt="Top bar and Dock" width="500"><br>Top bar and Dock</td>
  <td align="center"><img src="src/screenshots/installer-effects_v1-977e5114cde9.png" alt="Effects" width="500"><br>Effects</td>
  <td align="center"><img src="src/screenshots/installer-window_controls_v1-916a128ce301.png" alt="Flat or Glassy window controls" width="500"><br>Window controls</td>
  <td align="center"><img src="src/screenshots/installer-shadows_v1-c63dd8869965.png" alt="Window shadow comparison" width="500"><br>Window shadows</td>
  <td align="center"><img src="src/screenshots/installer-fonts_v1-47275156cd9d.png" alt="Fonts" width="500"><br>Fonts</td>
  <td align="center"><img src="src/screenshots/installer-firefox_v1-08f83dcd26d9.png" alt="Firefox" width="500"><br>Firefox</td>
  <td align="center"><img src="src/screenshots/installer-files_v1-f87b06ae8bd9.png" alt="File manager" width="500"><br>File manager</td>
  <td align="center"><img src="src/screenshots/installer-boot_v1-ca46dbc266fb.png" alt="Boot animation" width="500"><br>Boot animation</td>
  <td align="center"><img src="src/screenshots/installer-oled_v1-31b79c5ca4db.png" alt="OLED protection" width="500"><br>OLED protection</td>
  <td align="center"><img src="src/screenshots/installer-summary_v1-404db506bc87.png" alt="Summary" width="500"><br>Summary</td>
</tr>
</table>
