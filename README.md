# macOS Golden Gate Theme for Plasma 6.6/6.7+

Introducing Golden Gate, reimagined for Linux.

The complete macOS Golden Gate experience, from its liquid glass to its finest details, brought natively to KDE Plasma 6.6 and 6.7+.

> [!CAUTION]
> This project is experimental and still under heavy development, so things will break from time to time. Don't use it on a production system. If something goes wrong, please [open an issue](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new).

---

![Roadmap](https://img.shields.io/badge/project-roadmap-6B4B8A?style=for-the-badge&logo=github&logoColor=white)

| Component | Description | Status |
|-----------|-------------|--------|
| **Color Schemes** | Light and Dark color palettes | Planned |
| **Wallpapers** | Golden Gate Iridescence + Landscape (Morning/Evening/Night) | Planned |
| **Fonts** | SF Pro Display, Text, Rounded, Mono | Planned |
| **Cursors** | Golden Gate style cursors | Planned |
| **Plasma Theme** | Translucent panels + close/min/max buttons | Planned |
| **Kvantum Theme** | Kvantum theme | Planned |
| **GTK Theme** | GTK2/3/4 window chrome and controls | Planned |
| **Acrylic Glass** | KWin blur, per-surface rounded corners, persistent Dock glass and third-party effect safety | Planned |
| **KDE Rounded Corners** | Verified online source build, enabled with a 28 px active/inactive window radius | Planned |
| **Auto Theme Switcher** | 06:00 / 18:00 schedule plus an event-driven System Settings bridge for Plasma, Kvantum, GTK, icons, cursors, decorations and wallpaper | Planned |
| **OLED Care** | Opt-in pixel-shift timer for the top bar and dock | Planned |
| **Installer UI** | Glass window with an animated hello greeting; drives install / uninstall and a per-feature picker | Planned |
| **Aurorae Decorations** | Window title bar and borders | Planned |
| **Global Menu Plasmoid** | Unified menu bar: system menu, app name, window controls, app menus | Planned |
| **Dock Task Manager** | Icons-only dock applet with macOS-style notification badges | Planned |
| **Nautilus** | Install Nautilus and set as default file manager on KDE | Planned |
| **Icons** | Full icon set (light & dark) | Planned |
| **Multi-Distro Support** | KDE Plasma 6.6+ on the Arch, Fedora, openSUSE and Gentoo families | Planned |
| **Launcher Plasmoid** | App grid launcher | Planned |
| **Trashcan Plasmoid** | Trash widget with configurable icons | Planned |
| **Sounds** | Notification and event sounds | Planned |
| **Firefox Theme** | Firefox browser theme | Planned |
| **Konsole Theme** | Terminal profile | Planned |
| **Kate Theme** | Text editor theme | Planned |
| **SDDM Theme** | Login and lock screen | Planned |
| **Calendar Plasmoid** | Calendar dropdown | Planned |
| **Control Center Plasmoid** | Quick settings panel | Planned |
| **System Preferences Plasmoid** | Settings launcher | Planned |
| **OS Selector** | Boot manager / OS picker screen | Planned |
| **Boot Screen** | Plymouth splash for startup (1080p–4K) | Planned |
| **Shutdown Screen** | Styled logout / shutdown sequence | Planned |

---

![Harness](https://img.shields.io/badge/testing-harness-8A4B5B?style=for-the-badge&logo=qemu&logoColor=white)

Every supported distro can be test-driven in a disposable VM. `./vm <distro>` boots a graphical KDE Plasma machine with this repo mounted, the `tester` user auto-logged in, and the installer UI already open, while `./vm all` runs every distro at once, each in its own window:

```bash
./vm cachyos
./vm all
```

Supported distros: `cachyos`, `arch`, `manjaro`, `endeavouros`, `garuda`, `fedora`, `nobara`, `opensuse`, `gentoo`, `gentoo-openrc`.

---

![Getting started](https://img.shields.io/badge/getting-started-3B7B5B?style=for-the-badge&logo=gnubash&logoColor=white)

Everything goes through the **graphical installer**: a glass window that drives install / uninstall with a per-feature picker:

```bash
./installer
```

It checks for a newer release on launch, lets you toggle exactly which parts of the theme get applied, and shows live progress while it runs.

---

![Contributing](https://img.shields.io/badge/contributing-A04B4B?style=for-the-badge&logo=github&logoColor=white)

Bug reports are the most valuable contribution right now: **[open an issue](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new)**, or use **Apple menu → About This Computer → Report a Bug…** straight from the desktop. Please include:

- Your Plasma version (`plasmashell --version`) and distro (`grep PRETTY_NAME /etc/os-release`)
- The theme version (`cat VERSION`, or the version shown in *About This Computer*)
- A screenshot or recording if it's a visual regression

Pull requests are welcome too: keep them small and focused, and test with the `./vm` harness before submitting.

---

![Credits](https://img.shields.io/badge/credits-%26%20inspiration-8A6B4B?style=for-the-badge&logo=apple&logoColor=white)

Everything here is maintained independently. Thanks to the open source projects that gave inspiration for this project:

- **[EliverLara](https://github.com/EliverLara/TahoeLauncher)**: `TahoeLauncher`, the inspiration for the Launcher plasmoid.
- **[vinceliuice](https://github.com/vinceliuice)**: `MacTahoe-icon-theme`, the basis for the icons and cursors, and inspiration for the GTK look.
- **[taj-ny](https://github.com/taj-ny/kwin-effects-forceblur)** and **[4v3ngR](https://github.com/4v3ngR/kwin-effects-glass)**: Better Blur and its glass fork, the starting point of the Acrylic Glass effect.
- **[luisbocanegra](https://github.com/luisbocanegra/plasma-panel-colorizer)**: `plasma-panel-colorizer`, bundled offline to tint the panels.
- **[Matin Lotfaliei](https://github.com/matinlotfali/KDE-Rounded-Corners)**: `KDE-Rounded-Corners`, the KWin rounded-window effect built against the host KWin SDK.
- **[ful1e5](https://github.com/ful1e5)**: `apple_cursor`, inspiration for an alternate macOS-style cursor.
- **[sahibjotsaggu](https://github.com/sahibjotsaggu)**: `San-Francisco-Pro-Fonts`, where the SF Pro / SF Mono bundle comes from.
- **[Lucide](https://github.com/lucide-icons/lucide)**: copy icons bundled in the global menu.
- **[512pixels.net](https://512pixels.net/projects/default-mac-wallpapers-in-5k/)**: high-resolution macOS wallpaper archive.

Independent reimplementation inspired by the macOS aesthetic, not affiliated with or endorsed by Apple. "macOS" and "Apple" are trademarks of Apple Inc.; the bundled wallpapers and SF fonts remain Apple's property. Licensed GPL-3.0.
