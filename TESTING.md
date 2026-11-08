# Installer testing

Golden Gate **v0.63.2** uses fixed Dock spacing: a 56 px center pitch on the
default 68 px panel, preserving approximately 42 px visible icons. The old
spacing selector and its saved overrides no longer affect the Dock.

The shared implementation passed 20 Dock regressions and 7 task-manager/install
regressions in a disposable KDE neon VM, with light/dark/light visual checks.
See [detailed evidence](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/v0.63.2/tests/dock_spacing_validation.json)
for commands and coverage limits. Release publication requires passing CI
for the exact commits on main and dev in both repositories.

## Installation steps

Scroll horizontally through the installation steps.

<table>
<tr>
  <td align="center"><img src="src/screenshots/installer-welcome_v1-d7ca113e7443.webp" alt="Welcome" width="500"><br>Welcome</td>
  <td align="center"><img src="src/screenshots/installer-appearance_v1-5e73ea5769b1.webp" alt="Appearance" width="500"><br>Appearance</td>
  <td align="center"><img src="src/screenshots/installer-icons_v1-5c39efb79c75.webp" alt="Icons and color" width="500"><br>Icons and color</td>
  <td align="center"><img src="src/screenshots/installer-wallpaper_v1-304d0c6147a3.webp" alt="Wallpaper" width="500"><br>Wallpaper</td>
  <td align="center"><img src="src/screenshots/installer-launcher_v1-977963829b7e.webp" alt="Launcher" width="500"><br>Launcher</td>
  <td align="center"><img src="src/screenshots/installer-layout_v1-bbb0b4fa570f.webp" alt="Top bar and Dock" width="500"><br>Top bar and Dock</td>
  <td align="center"><img src="src/screenshots/installer-effects_v1-a9a6e8f18a5d.webp" alt="Effects" width="500"><br>Effects</td>
  <td align="center"><img src="src/screenshots/installer-window_controls_v1-d70c5487f84f.webp" alt="Flat or Glassy window controls" width="500"><br>Window controls</td>
  <td align="center"><img src="src/screenshots/installer-shadows_v1-18b5866f33f3.webp" alt="Window shadow comparison" width="500"><br>Window shadows</td>
  <td align="center"><img src="src/screenshots/installer-fonts_v1-8e2cbdfba9cf.webp" alt="Fonts" width="500"><br>Fonts</td>
  <td align="center"><img src="src/screenshots/installer-firefox_v1-cf6e0028e6b4.webp" alt="Firefox" width="500"><br>Firefox</td>
  <td align="center"><img src="src/screenshots/installer-files_v1-78741c27bb81.webp" alt="File manager" width="500"><br>File manager</td>
  <td align="center"><img src="src/screenshots/installer-glass_style_v1-185745c76452.webp" alt="Window glass" width="500"><br>Window glass</td>
  <td align="center"><img src="src/screenshots/installer-boot_v1-125daf2a30c9.webp" alt="Boot animation" width="500"><br>Boot animation</td>
  <td align="center"><img src="src/screenshots/installer-oled_v1-28ace0a58506.webp" alt="OLED protection" width="500"><br>OLED protection</td>
  <td align="center"><img src="src/screenshots/installer-summary_v1-ad9c473b2eee.webp" alt="Summary" width="500"><br>Summary</td>
</tr>
</table>
