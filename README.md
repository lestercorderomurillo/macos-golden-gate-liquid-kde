# macOS Golden Gate Theme for Plasma 6.6/6.7+

Introducing Golden Gate, reimagined for Linux.

The complete macOS Golden Gate experience, from its liquid glass to its finest details, brought natively to KDE Plasma 6.6 and 6.7+.

> [!CAUTION]
> This project is experimental and still under heavy development, so things will break from time to time. Don't use it on a production system. If something goes wrong, please [open an issue](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new).

<br>

![Roadmap](https://img.shields.io/badge/project-roadmap-6B4B8A?style=for-the-badge&logo=github&logoColor=white)

| Component | Description | Status |
|-----------|-------------|--------|
| **Color Schemes** | Carefully matched light and dark palettes for the whole desktop | Planned |
| **Wallpapers** | Golden Gate wallpapers that follow the day, from morning to night | Planned |
| **Fonts** | The full San Francisco family for that crisp, Mac-like reading feel | Planned |
| **Cursors** | The familiar Mac pointer, faithfully recreated | Planned |
| **Plasma Theme** | Translucent panels and glass surfaces across the whole shell | Planned |
| **Kvantum Theme** | Mac styling that feels native in every Qt app | Planned |
| **GTK Theme** | The same look carried into your GTK apps | Planned |
| **Acrylic Glass** | Deep liquid-glass blur where the wallpaper shines through every surface | Planned |
| **KDE Rounded Corners** | Softly rounded corners on every window, just like macOS | Planned |
| **Auto Theme Switcher** | Light by day, dark by night, switching the whole desktop for you | Planned |
| **OLED Care** | Gentle pixel shifting that protects OLED panels from burn-in | Planned |
| **Installer UI** | A beautiful glass installer that sets everything up in a few clicks | Planned |
| **Aurorae Decorations** | Mac-style title bars with traffic-light window controls | Planned |
| **Global Menu Plasmoid** | A unified menu bar up top, with app menus right where you expect them | Planned |
| **Dock Task Manager** | An icons-only Dock with red Mac-style notification badges | Planned |
| **Nautilus** | A Finder-style file manager with a clean macOS sidebar | Planned |
| **Icons** | A complete icon set in light and dark, drawn in the macOS style | Planned |
| **Multi-Distro Support** | One experience that feels at home on Arch, Fedora, openSUSE and Gentoo | Planned |
| **Launcher Plasmoid** | A Launchpad-style app grid with quick search and favorites | Planned |
| **Trashcan Plasmoid** | A Trash that lives in the Dock, just like on a Mac | Planned |
| **Sounds** | Subtle system sounds for notifications and events | Planned |
| **Firefox Theme** | Firefox dressed to match the rest of the desktop | Planned |
| **Konsole Theme** | A terminal that looks straight out of macOS | Planned |
| **Kate Theme** | Matching colors and chrome for the Kate editor | Planned |
| **SDDM Theme** | A macOS-style login and lock screen | Planned |
| **Glass Plasmoids** | Bundled open source KDE plasmoids reworked with the glass look | Planned |
| **Control Center Plasmoid** | A Control Center panel for quick settings | Planned |
| **System Preferences Plasmoid** | System Settings, presented the Mac way | Planned |
| **OS Selector** | A gorgeous boot picker for dual-boot setups | Planned |
| **Boot Screen** | An Apple-style boot splash, crisp from 1080p to 4K | Planned |
| **Shutdown Screen** | A styled shutdown sequence to match the boot experience | Planned |

<br>

![Harness](https://img.shields.io/badge/testing-harness-8A4B5B?style=for-the-badge&logo=qemu&logoColor=white)

Every supported distro can be test-driven in a disposable VM. `./vm <distro>` boots a graphical KDE Plasma machine with this repo mounted, the `tester` user auto-logged in, and the installer UI already open, while `./vm all` runs every distro at once, each in its own window:

```bash
./vm cachyos
./vm all
```

Supported distros: `cachyos`, `arch`, `manjaro`, `endeavouros`, `garuda`, `fedora`, `nobara`, `opensuse`, `gentoo`, `gentoo-openrc`.

<br>

![Getting started](https://img.shields.io/badge/getting-started-3B7B5B?style=for-the-badge&logo=gnubash&logoColor=white)

Everything goes through the **graphical installer**: a glass window that drives install / uninstall with a per-feature picker:

```bash
./installer
```

It checks for a newer release on launch, lets you toggle exactly which parts of the theme get applied, and shows live progress while it runs.

<br>

![Contributing](https://img.shields.io/badge/contributing-A04B4B?style=for-the-badge&logo=github&logoColor=white)

Bug reports are the most valuable contribution right now: **[open an issue](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new)**, or use **Apple menu → About This Computer → Report a Bug…** straight from the desktop. Please include:

- Your Plasma version (`plasmashell --version`) and distro (`grep PRETTY_NAME /etc/os-release`)
- The theme version (`cat VERSION`, or the version shown in *About This Computer*)
- A screenshot or recording if it's a visual regression

Pull requests are welcome too: keep them small and focused, and test with the `./vm` harness before submitting.

<br>

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
