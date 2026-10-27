# Installer testing

Native installer screens for Golden Gate 0.61.8, captured in a disposable KDE Plasma VM.
The gallery is captured from the release source and reviewed before publication.
Release checks cover both editions, theme switching, installation, reboot and removal.

Run `./installer` from this checkout to review the wizard. For shared test commands and the capture workflow, see [Tahoe CONTRIBUTING.md](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md).

## v0.61.8 battery icon contrast

The shared Tahoe icon staging now makes neutral battery fills and charging
bolts follow KDE's light/dark foreground colors in both editions. Battery
geometry, warning colors and saved percentage-display choices are preserved.
Generated Regular, Glass and offline appearance themes opt into KDE palette
recoloring for inherited icons. The implementation also covers Nix packaging.

Golden Gate's wrapper suite passed all 45 tests. Tahoe's 54 focused checks
include native KDE icon rendering at four sizes and four scaling factors,
light/dark/light transitions, symbolic aliases and install/reinstall/uninstall.
The complete shared suite was exercised on prepared Golden Gate content;
18 initially blocked checks passed after allowing private D-Bus/Xvfb sessions
and incorporating the upstream README badge correction. Four optional cases
remain skipped, not passed. Both editions' battery previews were reviewed in
a disposable KDE neon VM (Plasma 6.8.1, Qt 6.11.1), with synthetic charge levels.
See [Tahoe TESTING.md](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/TESTING.md)
for commands, content identifiers and coverage limits. The release gallery is
a separate fresh complete bundle from the pinned capture profile.

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
  <td align="center"><img src="src/screenshots/installer-welcome_v1-ba93cf0062b4.png" alt="Welcome" width="500"><br>Welcome</td>
  <td align="center"><img src="src/screenshots/installer-appearance_v1-5983201d6502.png" alt="Appearance" width="500"><br>Appearance</td>
  <td align="center"><img src="src/screenshots/installer-icons_v1-821a7b881aab.png" alt="Icons and color" width="500"><br>Icons and color</td>
  <td align="center"><img src="src/screenshots/installer-wallpaper_v1-b0d495268582.png" alt="Wallpaper" width="500"><br>Wallpaper</td>
  <td align="center"><img src="src/screenshots/installer-launcher_v1-793f94230455.png" alt="Launcher" width="500"><br>Launcher</td>
  <td align="center"><img src="src/screenshots/installer-layout_v1-1bc63d9527fd.png" alt="Top bar and Dock" width="500"><br>Top bar and Dock</td>
  <td align="center"><img src="src/screenshots/installer-effects_v1-cecefb4a1b6b.png" alt="Effects" width="500"><br>Effects</td>
  <td align="center"><img src="src/screenshots/installer-fonts_v1-fb3bae8c3394.png" alt="Fonts" width="500"><br>Fonts</td>
  <td align="center"><img src="src/screenshots/installer-firefox_v1-014565ebb9bb.png" alt="Firefox" width="500"><br>Firefox</td>
  <td align="center"><img src="src/screenshots/installer-files_v1-31e0561836be.png" alt="File manager" width="500"><br>File manager</td>
  <td align="center"><img src="src/screenshots/installer-boot_v1-2cb322a78a40.png" alt="Boot animation" width="500"><br>Boot animation</td>
  <td align="center"><img src="src/screenshots/installer-oled_v1-06ea94242cf0.png" alt="OLED protection" width="500"><br>OLED protection</td>
  <td align="center"><img src="src/screenshots/installer-summary_v1-02b4861793b0.png" alt="Summary" width="500"><br>Summary</td>
</tr>
</table>
