# macOS Golden Gate Liquid Theme for KDE Plasma 6.6/6.7+

A full macOS Golden Gate-style desktop experience for KDE Plasma 6.6 and 6.7+.

> [!WARNING]
> **Alpha / active development.** Things break as KDE, KWin and friends update; the installer pulls upstream changes on launch and may behave differently between runs. If a Plasma / KDE / Kvantum upgrade breaks the look, run `sudo ./install` again — it reapplies every override and recompiles the native components against the updated libraries, restoring everything. Expect rough edges, hold off on production desktops, and please [report any issue](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new) you hit.

![Features](https://img.shields.io/badge/features-4B6B8A?style=for-the-badge&logo=kde&logoColor=white)

### Acrylic Glass Golden Gate Launcher

Closer to the real design. Quick search, a favorites capsule, and two view modes.

### Acrylic Glass Golden Gate Dock

Real liquid-glass depth. The wallpaper bends through the surface, with red macOS-style notification badges.
The dock's glass opacity is re-applied after every theme change so switching a
Global Theme in System Settings cannot leave an opaque panel behind.

### Acrylic Glass Golden Gate Finder

Nautilus reshaped into Finder, with a macOS-style sidebar and clean chrome. Light and dark.

### Acrylic Glass Golden Gate Menu

Unified menu bar with native dropdowns. System menu, app name, and window controls in the top panel.

### System Information

Glass system information window.

### Plasma Theme

Desktop right-click with translucent glass blur.

### Boot Splash

Plymouth boot screen with centered Apple-style logo on every monitor, scaled dynamically from 1080p to 4K. Boot mode shows a progress bar; shutdown / reboot share the same layout without the bar. On LUKS2-encrypted installs the passphrase prompt renders under the logo with a masked field.

---

![Roadmap](https://img.shields.io/badge/project-roadmap-6B4B8A?style=for-the-badge&logo=github&logoColor=white)

| Component | Description | Status |
|-----------|-------------|--------|

---

![Requirements and dependencies](https://img.shields.io/badge/requirements-%26%20dependencies-4B6B8A?style=for-the-badge&logo=linux&logoColor=white)

<details>
<summary><b>Hard requirements</b> — installer refuses to start without these</summary>

- **KDE Plasma 6.6+** (`plasmashell`, `kwriteconfig6`, `kreadconfig6`, `plasma-apply-lookandfeel`, `plasma-apply-cursortheme`, `plasma-apply-wallpaperimage`, `kpackagetool6`, `kbuildsycoca6`, `qdbus6` *or* `qdbus`)
- **Python 3.10+**
- **`sudo`** (for both `./install` and `./uninstall` — root needed to write the compiled plasmoids + KWin effect under the system Qt6 libdir)
- **Qt6 path discovery** — one of: `qmake6`, `qtpaths6`, or `pkg-config` + `Qt6Core.pc`. The installer asks Qt where its plugin / QML directories live; it refuses to guess. If none of those tools are installed, the installer falls back to the known libdir convention for your distro **only when that directory actually exists on disk**.
- **`dbus-send`** — session bus messaging, present on every supported distro.
- **`systemctl`** (systemd hosts) or **`crontab`** (OpenRC hosts) — schedules the OLED-care and timed light/dark features. The installer detects the init system and uses whichever fits; `crontab` is pulled in automatically on OpenRC when a scheduled feature is enabled.

</details>

<details>
<summary><b>Build toolchain</b> — needed for the compiled plasmoids and KWin effect</summary>

Skipped automatically when every compiled feature is disabled, including
`--no-plasmoids --no-globalmenu --no-acrylic-glass --no-rounded-corners`.

- **`cmake`**
- **`g++`** (GCC C++ compiler)
- **`pkg-config`**

</details>

<details>
<summary><b>KDE / Qt6 development SDK</b> — required by find_package() in the compiled units</summary>

Your distro's KDE Plasma 6 dev meta-package usually pulls these in one shot.

- **Extra CMake Modules** (`ECM`)
- **KF6**: `KCoreAddons`, `KConfig`, `KI18n`, `KWindowSystem`, `KDBusAddons`, `KCMUtils`, `KIconThemes`
- **KDecoration3**, **KWin** headers (`KWinDBusInterface`, `KWinX11DBusInterface`)
- **libplasma**, **libtaskmanager**, **libnotificationmanager**, **KSysGuard**
- **PlasmaActivities**, **PlasmaActivitiesStats**
- **Qt6 Base** + **Qt6 Declarative** + **Qt6 Wayland**
- **libepoxy**, **X11**, **XCB**

</details>

<details>
<summary><b>Bundled assets and one online integration</b></summary>

Fonts, icons, cursors, wallpapers, plasmoids, and Acrylic Glass all ship in the
repo under `src/offline/`. **KDE Rounded Corners is the sole online feature:**
the installer downloads the pinned v0.9.0 source archive, verifies its SHA-256,
then compiles it against the installed KWin. A failed or unavailable download
only skips Rounded Corners; the bundled theme continues installing. Verified
archives are cached under `build/online/`. A successful build installs and
enables the effect with its active and inactive window radii set to 28 px;
the setting remains independent from GTK, Plasma SVG, Aurorae, and Acrylic
geometry. The release update check on
launch may also access GitHub and pull a newer project release on a clean
checkout.

</details>

<details>
<summary><b>Optional integrations</b> — probed and used if present, never required</summary>

- **Kvantum** (`kvantummanager`) — Qt widget theme. Without it, Qt apps fall back to plain Breeze widgets while keeping the rest of the theme.
- **Nautilus** — Golden Gate Finder. Only relevant if you install with `--nautilus`.
- **`gsettings`** + **`gtk-update-icon-cache`** — GTK app integration (color-scheme hint, GTK 3/4 theme load).
- **`dolphin`**, **`spectacle`** — used by the "Report a Bug" → screenshot helper.

</details>

<details>
<summary><b>Quick install hints</b> — if preflight tells you a tool is missing</summary>

| Distro | Qt6 tools | KDE Plasma 6 dev |
|--------|-----------|------------------|
| Arch / CachyOS / Manjaro / EndeavourOS / Garuda | `pacman -S qt6-tools` | `pacman -S extra-cmake-modules plasma-workspace kdecoration libplasma libnotificationmanager libksysguard plasma-activities-stats` |
| Gentoo | `emerge dev-qt/qttools:6` | `emerge kde-frameworks/extra-cmake-modules kde-plasma/plasma-workspace kde-plasma/kdecoration kde-plasma/libplasma kde-plasma/libnotificationmanager kde-plasma/libksysguard kde-plasma/plasma-activities-stats` |
| Fedora / Nobara / RHEL | `dnf install qt6-qttools-devel` | `dnf install extra-cmake-modules plasma-workspace-devel kdecoration-devel libplasma-devel knotifications-devel libksysguard-devel kf6-plasma-activities-devel` |
| openSUSE Tumbleweed | `zypper install qt6-tools-devel` | `zypper install extra-cmake-modules plasma6-workspace-devel kdecoration-devel libKF6Plasma-devel libnotificationmanager6-devel libksysguard6-devel libKF6PlasmaActivitiesStats6-devel` |

</details>

---

![Usage](https://img.shields.io/badge/getting-started-3B7B5B?style=for-the-badge&logo=gnubash&logoColor=white)

The easiest way to install is the **graphical installer** — a glass window that drives install / uninstall and a per-feature picker:

```bash
./installer   # graphical: install / uninstall + feature picker
```

It opens a glass launcher to install, uninstall, or open the feature picker — toggle which parts of the theme get applied (wallpapers, fonts, Plasma theme, Kvantum, Plymouth, …), checks for a newer release on launch, and shows live progress while it runs. It wraps the same `./install` / `./uninstall` commands, so the CLI stays the source of truth.

### Command line

Prefer the terminal? A bare `sudo ./install` opens an interactive wizard right in your terminal: pick components, theme mode and OLED care, review the summary, confirm, then watch a live progress screen with a step list, progress bar and install log. `sudo ./uninstall` does the same for removal. Arrow keys move, space toggles (on a group title it toggles the whole group), Enter continues, q quits.

```bash
sudo ./install     # terminal wizard: pick components, then install
sudo ./uninstall   # terminal wizard: pick components, then remove
```

Any flag skips the wizard, so scripted installs behave exactly as before. `./legacy-install` and `./legacy-uninstall` never show the wizard at all, only the classic `[Y/n]` prompt:

```bash
sudo ./install --help            # show all options
sudo ./install --preflight       # run only the safety checks
sudo ./install --no-apply-theme  # stage files, don't switch Plasma yet
sudo ./legacy-install            # classic prompt, install everything
sudo ./legacy-uninstall          # classic prompt, reset to Breeze
```

### Try it in a VM, per OS

`./vm <distro>` boots a graphical KDE Plasma VM with this repo mounted, the `tester` user auto-logged in, and the installer UI opened automatically. Or run `cd /home/tester/repo && sudo ./install` in a terminal and review by eye.

```bash
./vm cachyos
./vm arch
./vm manjaro
./vm endeavouros
./vm garuda
./vm fedora
./vm nobara
./vm opensuse
./vm gentoo
./vm gentoo-openrc
./vm all      # every distro at once, each in its own window
```

`./vm all` trims each VM to 2 vCPU / 4 GiB so the fleet fits in RAM; override with `VM_CPUS` / `VM_MEM_MIB`. Ctrl-C in the launching terminal stops every VM.

The first `./vm gentoo-openrc` pass installs Gentoo onto its persistent test
disk. Boot that installed OpenRC system afterward with
`VM_BOOT_TARGET=1 ./vm gentoo-openrc`.

Update check on launch is on by default; when a newer release exists and the checkout is a clean git tree, the installer pulls it and re-runs itself. To bypass: `sudo MAC_GOLDEN_GATE_NO_UPDATE_CHECK=true ./install`. To only check: `sudo ./install --check-update`.

### Picking what to install

Skip components with `--no-<name>`, or restrict to a few with `--only`:

```bash
sudo ./install --no-gtk --no-sddm             # skip GTK and SDDM
sudo ./install --only --fonts --icons         # only fonts and icons
sudo ./uninstall --only --cursors             # uninstall just cursors
```

Available names:

`wallpapers`, `fonts`, `cursors`, `plasma-theme`, `window-decorations`, `kvantum`, `color-schemes`, `icons`, `plasmoids`, `globalmenu`, `acrylic-glass`, `rounded-corners`, `global-theme`, `layout`, `sounds`, `gtk`, `sddm`, `apps`, `nautilus`, `portals`, `oled-care`, `plymouth`.

Upgrade and boot-splash knobs:

- `--no-grub-modify` — don't touch `/etc/default/grub`. (By default the Plymouth step appends `splash` and re-runs `grub-mkconfig` so the boot splash renders; with this flag you get a warning + the manual command instead.)
- `--reset-wallpapers` — forget the saved light/dark wallpaper choices and apply the bundled wallpaper once.

Normal upgrades preserve deliberate wallpaper choices and pinned taskbar apps.
The Mac panel layout is rebuilt on every install; uninstall always removes its
top bar, Dock, Launcher, and Trash while restoring the user's pinned apps.
`--reset-wallpapers` is a one-shot action and is not saved to `features.json`.

### Light, dark, or auto

```bash
sudo ./install            # auto (default)
sudo ./install --dark
sudo ./install --light
```

Auto is light 06:00–18:00, dark otherwise, via a systemd user timer (or a crontab line on OpenRC). `--light` / `--dark` pin the mode and skip the schedule.

Switch by hand anytime:

```bash
mac-golden-gate-theme-switch light
mac-golden-gate-theme-switch dark
mac-golden-gate-theme-switch auto
```

### For OLED screens

The top bar never moves, and OLED panels burn static content in. The opt-in **OLED care** service nudges panel geometry on a timer — the top bar's height by a few px (its menu, clock, and tray shift with it) and the dock's position by a few px sideways — so no pixel renders the same content for hours. Off by default; enable it from the graphical installer's feature picker (`./installer` → **OLED care pixel shift**) or on the CLI:

```bash
sudo ./install --oled-care          # enable (every 5 min, up to 8 px)
sudo ./install --oled-care --save   # enable and remember it
sudo ./install --no-oled-care       # back off

# custom cadence + distance
sudo ./install --oled-care --oled-interval=3 --oled-max-shift=4
```

`--oled-interval=N` sets minutes between shifts (1–59, default 5); `--oled-max-shift=N` sets the maximum shift distance in px (1–16, default 8). Panels move one 2 px step per fire (the 32 px top bar walks 32 → 34 → … → 40 → 38 → … and back), matching manufacturer pixel-shift practice. Manual control anytime: `mac-golden-gate-oled-care shift` steps once (`--max-px N` to override the distance), `restore` puts the panels back, `status` shows the stored geometry.

### Remembering your choices

```bash
sudo ./install --no-gtk --dark --save   # write to features.json
sudo ./install                          # next run reuses features.json
sudo ./install --reset                  # back to defaults
```

---

![Report a bug](https://img.shields.io/badge/report-a%20bug-A04B4B?style=for-the-badge&logo=github&logoColor=white)

Found something broken? Please open a GitHub issue:

**👉 [Report a bug](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new)**

You can also reach the issue tracker straight from the desktop:

- **Apple menu → About This Computer → Report a Bug…** opens the same form in your browser.
- After every `./install` or `./uninstall` run, the final line of the output prints the issues URL.

When filing, please include:

- Your Plasma version (`plasmashell --version`) and distro (`cat /etc/os-release | grep PRETTY_NAME`)
- The MacGoldenGate Liquid KDE version (`cat VERSION` in the repo, or the version shown in *About This Computer*)
- A screenshot or recording if it's a visual regression

---

![Disclaimer](https://img.shields.io/badge/disclaimer-not%20affiliated%20with%20apple-6B6B6B?style=for-the-badge&logo=apple&logoColor=white)

Built using AI tools.

Independent reimplementation inspired by the macOS aesthetic. All code and theme assets are original or derived from compatibly licensed open-source work. The bundled wallpapers and the SF Pro / SF Mono fonts remain Apple's property, are redistributed from public archives, and are not covered by this project's license. "macOS" and "Apple" are trademarks of Apple Inc.; this project is not affiliated with or endorsed by Apple.

If you like Apple, buy an Apple product.

Licensed GPL-3.0.

---

![Credits and inspiration](https://img.shields.io/badge/credits-%26%20inspiration-8A6B4B?style=for-the-badge&logo=apple&logoColor=white)

Thanks to the open-source projects that inspired this one or fed assets into it. Everything here is maintained independently:

- **[EliverLara](https://github.com/EliverLara/TahoeLauncher)**: `TahoeLauncher`, the inspiration for the Launcher plasmoid.
- **[vinceliuice](https://github.com/vinceliuice)**: `MacTahoe-icon-theme`, the basis for the icons and cursors, and inspiration for the GTK look.
- **[taj-ny](https://github.com/taj-ny/kwin-effects-forceblur)** and **[4v3ngR](https://github.com/4v3ngR/kwin-effects-glass)**: Better Blur and its glass fork, the starting point of the Acrylic Glass effect (the KWin blur authors stay credited in the source headers).
- **[luisbocanegra](https://github.com/luisbocanegra/plasma-panel-colorizer)**: `plasma-panel-colorizer` v7.3.0, bundled offline and installed by the layout step to tint the panels (GPL-3.0, license shipped alongside).
- **[Matin Lotfaliei / KDE-Rounded-Corners](https://github.com/matinlotfali/KDE-Rounded-Corners)**: the GPL-3.0 KWin rounded-window effect, fetched from the pinned v0.9.0 release and built online against the host KWin SDK (license installed alongside).
- **[ful1e5](https://github.com/ful1e5)**: `apple_cursor`, inspiration for an alternate macOS-style cursor.
- **[sahibjotsaggu](https://github.com/sahibjotsaggu)**: `San-Francisco-Pro-Fonts`, where the SF Pro / SF Mono bundle comes from.
- **[Lucide](https://github.com/lucide-icons/lucide)**: copy icons bundled in the global menu (ISC, © Lucide Contributors).
- **[512pixels.net](https://512pixels.net/projects/default-mac-wallpapers-in-5k/)**: high-resolution macOS wallpaper archive.

Please support their efforts too: star their repos, report bugs upstream, and contribute back when you can.

If a credit is missing, please [open an issue](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new).
