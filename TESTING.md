# Installer testing

Golden Gate **v0.62.0** includes the verified Acrylic fixes for Nautilus blur,
KWin scene damage and competing blur effects, with Glass opacity retired.
The prepared edition passed 69 affected preset, conflict and wizard tests;
its light/dark desktop and all sixteen installer pages were captured in the
pinned disposable VM and individually reviewed. See the
[Acrylic validation report](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/v0.62.0/tests/native/acrylic_glass_062.md)
for the actual Wayland/X11 rendering matrix, upstream audit and coverage limits.

The photographs below use the pinned disposable VM capture recipe and retain
reviewed, content-hashed provenance. Exact release commits require passing
push CI on both main and dev in both repositories.

## Installation steps

Scroll horizontally through the installation steps.

<table>
<tr>
  <td align="center"><img src="src/screenshots/installer-welcome_v1-7294d58e0ca7.png" alt="Welcome" width="500"><br>Welcome</td>
  <td align="center"><img src="src/screenshots/installer-appearance_v1-6cab7f9b8e38.png" alt="Appearance" width="500"><br>Appearance</td>
  <td align="center"><img src="src/screenshots/installer-icons_v1-f1584dc9997d.png" alt="Icons and color" width="500"><br>Icons and color</td>
  <td align="center"><img src="src/screenshots/installer-wallpaper_v1-e61fd4253869.png" alt="Wallpaper" width="500"><br>Wallpaper</td>
  <td align="center"><img src="src/screenshots/installer-launcher_v1-073fc714664d.png" alt="Launcher" width="500"><br>Launcher</td>
  <td align="center"><img src="src/screenshots/installer-layout_v1-0c48e8115be6.png" alt="Top bar and Dock" width="500"><br>Top bar and Dock</td>
  <td align="center"><img src="src/screenshots/installer-effects_v1-6b6932c793a1.png" alt="Effects" width="500"><br>Effects</td>
  <td align="center"><img src="src/screenshots/installer-window_controls_v1-d952f24786d0.png" alt="Flat or Glassy window controls" width="500"><br>Window controls</td>
  <td align="center"><img src="src/screenshots/installer-shadows_v1-e5ab0e67b78f.png" alt="Window shadow comparison" width="500"><br>Window shadows</td>
  <td align="center"><img src="src/screenshots/installer-fonts_v1-80a3c70b4b60.png" alt="Fonts" width="500"><br>Fonts</td>
  <td align="center"><img src="src/screenshots/installer-firefox_v1-184a37d6d5a4.png" alt="Firefox" width="500"><br>Firefox</td>
  <td align="center"><img src="src/screenshots/installer-files_v1-4ac161f733ea.png" alt="File manager" width="500"><br>File manager</td>
  <td align="center"><img src="src/screenshots/installer-glass_style_v1-df5b35f44370.png" alt="Window glass" width="500"><br>Window glass</td>
  <td align="center"><img src="src/screenshots/installer-boot_v1-edf5e1ecc87c.png" alt="Boot animation" width="500"><br>Boot animation</td>
  <td align="center"><img src="src/screenshots/installer-oled_v1-126a7ebd1b96.png" alt="OLED protection" width="500"><br>OLED protection</td>
  <td align="center"><img src="src/screenshots/installer-summary_v1-c303975678d9.png" alt="Summary" width="500"><br>Summary</td>
</tr>
</table>
