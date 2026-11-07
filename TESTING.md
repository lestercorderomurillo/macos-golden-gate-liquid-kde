# Installer testing

Golden Gate **v0.63rc2** uses Golden Gate (Official), with a three-stop
gradient and separate light/dark colors. Tahoe (Clear) and Tahoe (Frosted)
remain available in Acrylic Glass settings. The Dock retains fixed v0.62.0
optics independently of window presets and fine tuning; existing blur fixes
and retired controls remain preserved.

The wrapper suite passed **97 tests**. Tahoe's focused screenshot-provenance
and glass-step checks passed **54 tests**, covering selective recapture, original
image provenance and light/dark/automatic previews. Popup fill checks passed
for the more transparent light fill and stronger black dark fill. Shader and
gradient values are unchanged. Seven targeted regression checks also passed for
RC version reading, update ordering, candidate-to-candidate and candidate-to-stable
automatic updates, the installed About version and selective version-frame capture. See the [preset gallery](GLASS_PRESETS.md) for all surface
and fine-tuning values with light/dark photographs. Captures use the pinned
Plasma 6.8.1 VM and do not establish new live qualification on other versions.
The [v0.62 rendering report](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/v0.62.0/tests/native/acrylic_glass_062.md)
retains its original version-specific Wayland/X11 evidence.

The photographs below use the pinned disposable VM capture recipe and retain
reviewed, content-hashed provenance. Exact release commits require passing
push CI on both main and dev in both repositories.

## Installation steps

Scroll horizontally through the installation steps.

<table>
<tr>
  <td align="center"><img src="src/screenshots/installer-welcome_v1-ecb13f95075d.png" alt="Welcome" width="500"><br>Welcome</td>
  <td align="center"><img src="src/screenshots/installer-appearance_v1-52a0e27afb4d.png" alt="Appearance" width="500"><br>Appearance</td>
  <td align="center"><img src="src/screenshots/installer-icons_v1-911c87201812.png" alt="Icons and color" width="500"><br>Icons and color</td>
  <td align="center"><img src="src/screenshots/installer-wallpaper_v1-ddf94b5e2060.png" alt="Wallpaper" width="500"><br>Wallpaper</td>
  <td align="center"><img src="src/screenshots/installer-launcher_v1-940e3d7dfa0f.png" alt="Launcher" width="500"><br>Launcher</td>
  <td align="center"><img src="src/screenshots/installer-layout_v1-3f9af58417ba.png" alt="Top bar and Dock" width="500"><br>Top bar and Dock</td>
  <td align="center"><img src="src/screenshots/installer-effects_v1-1faf0c3900d3.png" alt="Effects" width="500"><br>Effects</td>
  <td align="center"><img src="src/screenshots/installer-window_controls_v1-0acd92a8c492.png" alt="Flat or Glassy window controls" width="500"><br>Window controls</td>
  <td align="center"><img src="src/screenshots/installer-shadows_v1-e074d3c0e821.png" alt="Window shadow comparison" width="500"><br>Window shadows</td>
  <td align="center"><img src="src/screenshots/installer-fonts_v1-9f686b69a638.png" alt="Fonts" width="500"><br>Fonts</td>
  <td align="center"><img src="src/screenshots/installer-firefox_v1-4c3ed2bde6a6.png" alt="Firefox" width="500"><br>Firefox</td>
  <td align="center"><img src="src/screenshots/installer-files_v1-e2e81c4d3623.png" alt="File manager" width="500"><br>File manager</td>
  <td align="center"><img src="src/screenshots/installer-glass_style_v1-52175672a91d.png" alt="Window glass" width="500"><br>Window glass</td>
  <td align="center"><img src="src/screenshots/installer-boot_v1-bf2f81dcf7be.png" alt="Boot animation" width="500"><br>Boot animation</td>
  <td align="center"><img src="src/screenshots/installer-oled_v1-3b9ec426baba.png" alt="OLED protection" width="500"><br>OLED protection</td>
  <td align="center"><img src="src/screenshots/installer-summary_v1-838c84e7b4fa.png" alt="Summary" width="500"><br>Summary</td>
</tr>
</table>
