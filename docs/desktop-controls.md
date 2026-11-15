# Desktop controls

Golden Gate uses the original shared [Tahoe desktop controls](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/v0.72.0/docs/desktop-controls.md), with its own Liquid Glass materials and effective system appearance. The visual references are actual macOS Tahoe and Golden Gate; no implementation is copied from MacShell or the reviewed forks.

Control Center provides floating glass controls, native system models and saved Edit Controls choices. Wi-Fi, Battery and Notifications are also available as individual panel widgets. New or reset layouts include them; customized panels remain intact. Calendar remains last and the existing clock/calendar is preserved.

See [release evidence](../release-evidence.json) for the exact validation and hardware limits. Existing desktop photographs keep their original provenance.

[Light preview](../src/screenshots/previews/control-center-golden-gate-light-cc2bdfc937e8.png) · [Dark preview](../src/screenshots/previews/control-center-golden-gate-dark-bd924a582ef2.png) · [Capture provenance](../src/screenshots/previews/control-center-golden-gate-provenance.json)

Typography uses the bundled SF Pro Text face: 13 logical pixels for labels and
11 for secondary captions. Original monochrome symbols use consistent 18-pixel
panel, 22-pixel inline and 26-pixel circular-control sizing, independent of the
user's icon theme. Battery state remains live. The glass edge follows the Dock's
opposing light rims; the existing compositor blur and edition material remain
active. This does not replace the saved Acrylic Glass optics or introduce a new
refraction shader.
