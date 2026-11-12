# Installer testing

Golden Gate **v0.69.0** uses original Apple glyph outlines for the system-menu symbols.
Tahoe shows an icon on every action; Golden Gate shows only About, System Settings
and App Store. The active theme selects this preset across light/dark transitions,
independently of the Launcher preset. The existing App Store drawing is retained.

The native renderer, live cached-menu preset changes and shortcut interactions
pass in an isolated Arch SDK/X11 environment. Both editions passed installation
and reinstallation in disposable KDE neon Plasma/KWin 6.8.1 Wayland VMs, with
four reviewed menu captures. The full remote matrix remains asynchronous.
See [release evidence](release-evidence.json) and the
[original-font glyph provenance](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/6f515f188b86db6ee6f997eedee0c669c4c02a36/src/offline/plasmoids/org.kde.mac.tahoe.liquid.globalmenu/systemmenusymbols.json).

[Light menu](src/screenshots/menu_v1-4ccac1191586.webp) · [Dark menu](src/screenshots/menu_dark_v1-e6cda19d04cd.webp) · [Capture provenance](src/screenshots/previews/system-menu-golden-gate-069-provenance-a2ffe6af504b.json)

The README About, Finder and top bar photographs retain their v0.67.0 source from a
disposable VM. Other desktop images and the installer gallery retain their original
reviewed provenance ([capture records](src/screenshots/release-capture.json)). The retained v0.66.2 About previews show the corrected labels
in both modes ([provenance](src/screenshots/previews/about-buttons-provenance.json)).

[Light preview](src/screenshots/previews/about-buttons-light-23dd8b3e3837.png) · [Dark preview](src/screenshots/previews/about-buttons-dark-2e4c5cf8099c.png)

## Installation steps

Scroll horizontally through the installation steps.

<table>
<tr>
  <td align="center"><img src="src/screenshots/installer-welcome_v1-2eef653f309d.webp" alt="Welcome" width="500"><br>Welcome</td>
  <td align="center"><img src="src/screenshots/installer-appearance_v1-5e73ea5769b1.webp" alt="Appearance" width="500"><br>Appearance</td>
  <td align="center"><img src="src/screenshots/installer-icons_v1-5c39efb79c75.webp" alt="Icons and color" width="500"><br>Icons and color</td>
  <td align="center"><img src="src/screenshots/installer-wallpaper_v1-304d0c6147a3.webp" alt="Wallpaper" width="500"><br>Wallpaper</td>
  <td align="center"><img src="src/screenshots/installer-launcher_v1-977963829b7e.webp" alt="Launcher" width="500"><br>Launcher</td>
  <td align="center"><img src="src/screenshots/installer-layout_v1-cf121a13991a.webp" alt="Top bar and Dock" width="500"><br>Top bar and Dock</td>
  <td align="center"><img src="src/screenshots/installer-effects_v1-a9a6e8f18a5d.webp" alt="Effects" width="500"><br>Effects</td>
  <td align="center"><img src="src/screenshots/installer-window_controls_v1-d70c5487f84f.webp" alt="Flat or Glassy window controls" width="500"><br>Window controls</td>
  <td align="center"><img src="src/screenshots/previews/button-position-golden-gate-dark-wizard-a50b95609e38.webp" alt="Window buttons" width="500"><br>Window buttons</td>
  <td align="center"><img src="src/screenshots/installer-shadows_v1-18b5866f33f3.webp" alt="Window shadow comparison" width="500"><br>Window shadows</td>
  <td align="center"><img src="src/screenshots/installer-fonts_v1-8e2cbdfba9cf.webp" alt="Fonts" width="500"><br>Fonts</td>
  <td align="center"><img src="src/screenshots/installer-firefox_v1-cf6e0028e6b4.webp" alt="Firefox" width="500"><br>Firefox</td>
  <td align="center"><img src="src/screenshots/installer-files_v1-2d08654ee384.webp" alt="File manager" width="500"><br>File manager</td>
  <td align="center"><img src="src/screenshots/installer-glass_style_v1-185745c76452.webp" alt="Window glass" width="500"><br>Window glass</td>
  <td align="center"><img src="src/screenshots/installer-boot_v1-125daf2a30c9.webp" alt="Boot animation" width="500"><br>Boot animation</td>
  <td align="center"><img src="src/screenshots/installer-oled_v1-28ace0a58506.webp" alt="OLED protection" width="500"><br>OLED protection</td>
  <td align="center"><img src="src/screenshots/installer-summary_v1-628b8b82aa07.webp" alt="Summary" width="500"><br>Summary</td>
</tr>
</table>

Window buttons, captured in a disposable VM: [Light wizard](src/screenshots/previews/button-position-golden-gate-light-wizard-36aca73ad37c.webp) · [Light comparison](src/screenshots/previews/button-position-golden-gate-light-comparison-2252a75d62e9.png) · [Dark wizard](src/screenshots/previews/button-position-golden-gate-dark-wizard-a50b95609e38.webp) · [Dark comparison](src/screenshots/previews/button-position-golden-gate-dark-comparison-d3035dd038c4.png) · [Provenance](src/screenshots/previews/button-position-golden-gate-provenance-3524c01456df.json)
