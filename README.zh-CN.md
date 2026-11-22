<p align="center">
  <!-- Adapted with ImageGen from artwork by Apple: https://developer.apple.com/macos/ -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/artwork/kde-27-dark-bc048fb145ee.png">
    <img src="docs/artwork/kde-27-4808d8789e9c.png" alt="27 · KDE" width="180" height="180">
  </picture>
</p>

<h1 align="center">适用于 Linux KDE 桌面的 macOS Golden Gate 外观与操作体验</h1>

<p align="center">
  <a href="README.md" lang="en" hreflang="en">🇺🇸 English</a> ·
  <a href="README.es.md" lang="es" hreflang="es">🇪🇸 Español</a> ·
  <a href="README.zh-CN.md" lang="zh-CN" hreflang="zh-CN" aria-current="page">🇨🇳 简体中文</a> ·
  <a href="README.pt-BR.md" lang="pt-BR" hreflang="pt-BR">🇧🇷 Português (Brasil)</a> ·
  <a href="README.de.md" lang="de" hreflang="de">🇩🇪 Deutsch</a> ·
  <a href="README.fr.md" lang="fr" hreflang="fr">🇫🇷 Français</a>
</p>

<p align="center">
  <a href="https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/releases"><img src="https://img.shields.io/github/v/release/lestercorderomurillo/macos-golden-gate-liquid-kde?label=release&amp;color=blue" alt="release"></a>
  <a href="https://kde.org/plasma-desktop/"><img src="https://img.shields.io/badge/Plasma-6.6%2B-1d99f3?logo=kde" alt="plasma"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0-blue" alt="license"></a>
  <a href="https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new"><img src="https://img.shields.io/badge/report-a%20bug-red?logo=github" alt="report a bug"></a>
</p>


<p align="center">
  macOS Golden Gate 风格，适用于 KDE Plasma 6.6、6.7 和 6.8+。
</p>

<p align="center">
  <sub>选择发行版以查看其测试状态。</sub>
</p>

<p align="center">
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#cachyos" title="CachyOS"><img src="src/screenshots/distros/cachyos.svg" alt="CachyOS" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#arch" title="Arch Linux"><img src="src/screenshots/distros/archlinux.svg" alt="Arch Linux" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#endeavouros" title="EndeavourOS"><img src="src/screenshots/distros/endeavouros.svg" alt="EndeavourOS" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#fedora" title="Fedora"><img src="src/screenshots/distros/fedora.svg" alt="Fedora" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#manjaro" title="Manjaro"><img src="src/screenshots/distros/manjaro.svg" alt="Manjaro" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#artix" title="Artix Linux (OpenRC)"><img src="src/screenshots/distros/artixlinux.svg" alt="Artix Linux" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#garuda" title="Garuda Linux"><img src="src/screenshots/distros/garudalinux.svg" alt="Garuda Linux" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#nobara" title="Nobara Linux"><img src="src/screenshots/distros/nobaralinux.svg" alt="Nobara Linux" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#opensuse" title="openSUSE Tumbleweed"><img src="src/screenshots/distros/opensuse.svg" alt="openSUSE" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#neon" title="KDE neon"><img src="src/screenshots/distros/kdeneon.svg" alt="KDE neon" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#debian" title="Debian testing / sid (Plasma 6.6+)"><img src="src/screenshots/distros/debian.svg" alt="Debian" width="32" height="32"></a>
  <a href="https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#nixos" title="NixOS (experimental)"><img src="src/screenshots/distros/nixos.svg" alt="NixOS" width="32" height="32"></a>
</p>

本项目用于自定义 Linux 上 KDE 桌面的外观，不包含任何 Apple 服务，也不会连接到这些服务。如需 Apple 服务，请[直接前往 Apple 官方商店选购](https://www.apple.com/store)。

> [!CAUTION]
> **滚动发布理念**
> 实验性项目。每天接收更新。更新可能破坏兼容性。请避免用于生产系统；[在此报告问题](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new)。

> [!WARNING]
> **谨防收费的重新打包版本：本主题免费。**
>
> 如果你通过第三方渠道发现本主题，无需付费获取：直接从本仓库下载即可。我们保持项目免费，让所有人都能使用，无需付费。无需购买或订阅。

<br>

![贡献](https://img.shields.io/badge/contributing-A04B4B?style=for-the-badge&logo=github&logoColor=white)

错误报告、修复、测试和文档：参阅[贡献指南](CONTRIBUTING.md)。

Tahoe 和 Golden Gate 的代码贡献者及问题报告者：

<p>
  <a href="https://github.com/lestercorderomurillo"><img src="src/screenshots/contributors/lestercorderomurillo.svg" width="40" height="40" alt="@lestercorderomurillo" title="@lestercorderomurillo"></a>
  <a href="https://github.com/yanhenrique-dev"><img src="src/screenshots/contributors/yanhenrique-dev.svg" width="40" height="40" alt="@yanhenrique-dev" title="@yanhenrique-dev"></a>
  <a href="https://github.com/naevui"><img src="src/screenshots/contributors/naevui.svg" width="40" height="40" alt="@naevui" title="@naevui"></a>
  <a href="https://github.com/caioniehues"><img src="src/screenshots/contributors/caioniehues.svg" width="40" height="40" alt="@caioniehues" title="@caioniehues"></a>
  <a href="https://github.com/404-not-found129"><img src="src/screenshots/contributors/404-not-found129.svg" width="40" height="40" alt="@404-not-found129" title="@404-not-found129"></a>
  <a href="https://github.com/myakupozluk"><img src="src/screenshots/contributors/myakupozluk.svg" width="40" height="40" alt="@myakupozluk" title="@myakupozluk"></a>
  <a href="https://github.com/EMS1998"><img src="src/screenshots/contributors/EMS1998.svg" width="40" height="40" alt="@EMS1998" title="@EMS1998"></a>
  <a href="https://github.com/allfritz"><img src="src/screenshots/contributors/allfritz.svg" width="40" height="40" alt="@allfritz" title="@allfritz"></a>
  <a href="https://github.com/elegos"><img src="src/screenshots/contributors/elegos.svg" width="40" height="40" alt="@elegos" title="@elegos"></a>
  <a href="https://github.com/kozeki-uii"><img src="src/screenshots/contributors/kozeki-uii.svg" width="40" height="40" alt="@kozeki-uii" title="@kozeki-uii"></a>
  <a href="https://github.com/imightbelosthere"><img src="src/screenshots/contributors/imightbelosthere.svg" width="40" height="40" alt="@imightbelosthere" title="@imightbelosthere"></a>
  <a href="https://github.com/evaildev"><img src="src/screenshots/contributors/evaildev.svg" width="40" height="40" alt="@evaildev" title="@evaildev"></a>
  <a href="https://github.com/xarblu"><img src="src/screenshots/contributors/xarblu.svg" width="40" height="40" alt="@xarblu" title="@xarblu"></a>
  <a href="https://github.com/PKMNPlatin"><img src="src/screenshots/contributors/PKMNPlatin.svg" width="40" height="40" alt="@PKMNPlatin" title="@PKMNPlatin"></a>
  <a href="https://github.com/matinlotfali"><img src="src/screenshots/contributors/matinlotfali.svg" width="40" height="40" alt="@matinlotfali" title="@matinlotfali"></a>
  <a href="https://github.com/luisbocanegra"><img src="src/screenshots/contributors/luisbocanegra.svg" width="40" height="40" alt="@luisbocanegra" title="@luisbocanegra"></a>
  <a href="https://github.com/OliverChase2003"><img src="src/screenshots/contributors/OliverChase2003.svg" width="40" height="40" alt="@OliverChase2003" title="@OliverChase2003"></a>
  <a href="https://github.com/RoxasYTB"><img src="src/screenshots/contributors/RoxasYTB.svg" width="40" height="40" alt="@RoxasYTB" title="@RoxasYTB"></a>
  <a href="https://github.com/Flagwill"><img src="src/screenshots/contributors/Flagwill.svg" width="40" height="40" alt="@Flagwill" title="@Flagwill"></a>
  <a href="https://github.com/4l3j0Ok"><img src="src/screenshots/contributors/4l3j0Ok.svg" width="40" height="40" alt="@4l3j0Ok" title="@4l3j0Ok"></a>
  <a href="https://github.com/0xrushi"><img src="src/screenshots/contributors/0xrushi-88d08627bc35.svg" width="40" height="40" alt="@0xrushi" title="@0xrushi"></a>
  <a href="https://github.com/aenriii"><img src="src/screenshots/contributors/aenriii-b3ff7f30e5bb.svg" width="40" height="40" alt="@aenriii" title="@aenriii"></a>
  <a href="https://github.com/andreas399"><img src="src/screenshots/contributors/andreas399-00993524b291.svg" width="40" height="40" alt="@andreas399" title="@andreas399"></a>
  <a href="https://github.com/Andrew-Sor"><img src="src/screenshots/contributors/Andrew-Sor-94949c08022e.svg" width="40" height="40" alt="@Andrew-Sor" title="@Andrew-Sor"></a>
  <a href="https://github.com/ardashir77"><img src="src/screenshots/contributors/ardashir77-40723979caf5.svg" width="40" height="40" alt="@ardashir77" title="@ardashir77"></a>
  <a href="https://github.com/azizaktas"><img src="src/screenshots/contributors/azizaktas-3e26627b326b.svg" width="40" height="40" alt="@azizaktas" title="@azizaktas"></a>
  <a href="https://github.com/binary-pleb"><img src="src/screenshots/contributors/binary-pleb-f740b0b97491.svg" width="40" height="40" alt="@binary-pleb" title="@binary-pleb"></a>
  <a href="https://github.com/bneils"><img src="src/screenshots/contributors/bneils-fb7ae850b1d9.svg" width="40" height="40" alt="@bneils" title="@bneils"></a>
  <a href="https://github.com/FAYZER77"><img src="src/screenshots/contributors/FAYZER77-d2d7b1894be9.svg" width="40" height="40" alt="@FAYZER77" title="@FAYZER77"></a>
  <a href="https://github.com/fxrncyyisingithub"><img src="src/screenshots/contributors/fxrncyyisingithub-318dada63e53.svg" width="40" height="40" alt="@fxrncyyisingithub" title="@fxrncyyisingithub"></a>
  <a href="https://github.com/germanbagutteorsomething"><img src="src/screenshots/contributors/germanbagutteorsomething-ab237be9d3ca.svg" width="40" height="40" alt="@germanbagutteorsomething" title="@germanbagutteorsomething"></a>
  <a href="https://github.com/iNarrow12"><img src="src/screenshots/contributors/iNarrow12-89d67a613995.svg" width="40" height="40" alt="@iNarrow12" title="@iNarrow12"></a>
  <a href="https://github.com/IsaiahSHanson"><img src="src/screenshots/contributors/IsaiahSHanson-c91886c82a21.svg" width="40" height="40" alt="@IsaiahSHanson" title="@IsaiahSHanson"></a>
  <a href="https://github.com/kuau"><img src="src/screenshots/contributors/kuau-f7a628210421.svg" width="40" height="40" alt="@kuau" title="@kuau"></a>
  <a href="https://github.com/Lando0007"><img src="src/screenshots/contributors/Lando0007-055a69c9d9ec.svg" width="40" height="40" alt="@Lando0007" title="@Lando0007"></a>
  <a href="https://github.com/LilT59"><img src="src/screenshots/contributors/LilT59-71e54221db69.svg" width="40" height="40" alt="@LilT59" title="@LilT59"></a>
  <a href="https://github.com/marcosfantonio"><img src="src/screenshots/contributors/marcosfantonio-7cf4769037d2.svg" width="40" height="40" alt="@marcosfantonio" title="@marcosfantonio"></a>
  <a href="https://github.com/moulikanand12345-lang"><img src="src/screenshots/contributors/moulikanand12345-lang-10436c88ec5b.svg" width="40" height="40" alt="@moulikanand12345-lang" title="@moulikanand12345-lang"></a>
  <a href="https://github.com/nanechi"><img src="src/screenshots/contributors/nanechi-6ee8bdc66808.svg" width="40" height="40" alt="@nanechi" title="@nanechi"></a>
  <a href="https://github.com/nousernameget"><img src="src/screenshots/contributors/nousernameget-867f5abf1c6b.svg" width="40" height="40" alt="@nousernameget" title="@nousernameget"></a>
  <a href="https://github.com/OpalSand"><img src="src/screenshots/contributors/OpalSand-e851921f53a7.svg" width="40" height="40" alt="@OpalSand" title="@OpalSand"></a>
  <a href="https://github.com/P0sixSplo1t-2"><img src="src/screenshots/contributors/P0sixSplo1t-2-d399b40eaff7.svg" width="40" height="40" alt="@P0sixSplo1t-2" title="@P0sixSplo1t-2"></a>
  <a href="https://github.com/rokan00"><img src="src/screenshots/contributors/rokan00-7f822820142e.svg" width="40" height="40" alt="@rokan00" title="@rokan00"></a>
  <a href="https://github.com/RussH"><img src="src/screenshots/contributors/RussH-c209ade9c4c8.svg" width="40" height="40" alt="@RussH" title="@RussH"></a>
  <a href="https://github.com/Salkio"><img src="src/screenshots/contributors/Salkio-d253feaa8c23.svg" width="40" height="40" alt="@Salkio" title="@Salkio"></a>
  <a href="https://github.com/Shivamingale3"><img src="src/screenshots/contributors/Shivamingale3-7fd280070657.svg" width="40" height="40" alt="@Shivamingale3" title="@Shivamingale3"></a>
  <a href="https://github.com/shoko3756"><img src="src/screenshots/contributors/shoko3756-71094b9b49ef.svg" width="40" height="40" alt="@shoko3756" title="@shoko3756"></a>
  <a href="https://github.com/Sonicx9876"><img src="src/screenshots/contributors/Sonicx9876-68707df90a4e.svg" width="40" height="40" alt="@Sonicx9876" title="@Sonicx9876"></a>
  <a href="https://github.com/Tias-dev"><img src="src/screenshots/contributors/Tias-dev-73b7671b1fa4.svg" width="40" height="40" alt="@Tias-dev" title="@Tias-dev"></a>
  <a href="https://github.com/txhammer68"><img src="src/screenshots/contributors/txhammer68-5ba01c461020.svg" width="40" height="40" alt="@txhammer68" title="@txhammer68"></a>
  <a href="https://github.com/vanshdev0101"><img src="src/screenshots/contributors/vanshdev0101-c4d78aedabcb.svg" width="40" height="40" alt="@vanshdev0101" title="@vanshdev0101"></a>
  <a href="https://github.com/vialolis"><img src="src/screenshots/contributors/vialolis-53aa505d17ae.svg" width="40" height="40" alt="@vialolis" title="@vialolis"></a>
  <a href="https://github.com/Whiddu"><img src="src/screenshots/contributors/Whiddu-e0cacbd52acd.svg" width="40" height="40" alt="@Whiddu" title="@Whiddu"></a>
  <a href="https://github.com/yingmanwumen"><img src="src/screenshots/contributors/yingmanwumen-17ac0de05287.svg" width="40" height="40" alt="@yingmanwumen" title="@yingmanwumen"></a>
  <a href="https://github.com/yofriendfromschool1"><img src="src/screenshots/contributors/yofriendfromschool1-0438de7dda5b.svg" width="40" height="40" alt="@yofriendfromschool1" title="@yofriendfromschool1"></a>
  <a href="https://github.com/zhaokelei"><img src="src/screenshots/contributors/zhaokelei-c371e37c16fb.svg" width="40" height="40" alt="@zhaokelei" title="@zhaokelei"></a>
</p>

<br>

![功能与截图](https://img.shields.io/badge/features-%26%20screenshots-4B6B8A?style=for-the-badge&logo=kde&logoColor=white)

### Golden Gate Finder (Alpha)

采用 Golden Gate 玻璃效果的 Finder 风格文件浏览。

<p align="center">
  <a href="src/screenshots/previews/readme-golden-gate-light-finder-362858f81e2b.webp"><img src="src/screenshots/previews/readme-golden-gate-light-finder-362858f81e2b.webp" alt="Golden Gate light desktop with Files focused" width="415"></a>
  <a href="src/screenshots/previews/readme-golden-gate-dark-finder-b835bc92a197.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-finder-b835bc92a197.webp" alt="Golden Gate dark desktop with Files focused" width="415"></a>
</p>

<details>
<summary><strong>浅色和深色模式下的红色与蓝色强调色</strong></summary>

<table>
<tr><th>强调色</th><th>浅色</th><th>深色</th></tr>
<tr><td>蓝色</td><td><a href="src/screenshots/previews/readme-golden-gate-light-finder-blue-362858f81e2b.webp"><img src="src/screenshots/previews/readme-golden-gate-light-finder-blue-362858f81e2b.webp" alt="Finder 在浅色模式下以蓝色突出显示侧边栏所选项" width="415"></a></td><td><a href="src/screenshots/previews/readme-golden-gate-dark-finder-blue-b835bc92a197.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-finder-blue-b835bc92a197.webp" alt="Finder 在深色模式下以蓝色突出显示侧边栏所选项" width="415"></a></td></tr>
<tr><td>红色</td><td><a href="src/screenshots/previews/readme-golden-gate-light-finder-red-64f13f0002bb.webp"><img src="src/screenshots/previews/readme-golden-gate-light-finder-red-64f13f0002bb.webp" alt="Finder 在浅色模式下以红色突出显示侧边栏所选项" width="415"></a></td><td><a href="src/screenshots/previews/readme-golden-gate-dark-finder-red-928d44f325a4.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-finder-red-928d44f325a4.webp" alt="Finder 在深色模式下以红色突出显示侧边栏所选项" width="415"></a></td></tr>
</table>

</details>

<br>

### Golden Gate Launchpad (Alpha)

查找应用、浏览分类，让收藏触手可及。应用网格在浅色和深色模式下分别使用半透明的白色和黑色磨砂玻璃。两种模式的搜索框均使用相同的黑金渐变。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-launcher-7313220bc2be.webp" alt="Default Golden Gate preset 2 in light mode, with detached search and Golden Gate wallpaper" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-dark-launcher-1e3a163fc520.webp" alt="Default Golden Gate preset 2 in dark mode, with detached search and Golden Gate wallpaper" width="415">
</p>

<br>

### Golden Gate Dock (Alpha)

玻璃折射、悬停放大、红色通知计数气泡和自动隐藏。

<p align="center">
  <strong>Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-regular-ab3f15dc4638.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-regular-ab3f15dc4638.webp" alt="Golden Gate Dock icon appearance preview: Light" width="830"></a>
</p>

<p align="center">
  <strong>Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-regular-10bd3f5e3f7a.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-regular-10bd3f5e3f7a.webp" alt="Golden Gate Dock icon appearance preview: Dark" width="830"></a>
</p>

<p align="center">
  <strong>Clear Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-clear-90ade834a80a.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-clear-90ade834a80a.webp" alt="Golden Gate Dock icon appearance preview: Clear Light" width="830"></a>
</p>

<p align="center">
  <strong>Clear Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-clear-168be084ef75.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-clear-168be084ef75.webp" alt="Golden Gate Dock icon appearance preview: Clear Dark" width="830"></a>
</p>

<p align="center">
  <strong>Blue Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-blue-66f49f74fb75.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-blue-66f49f74fb75.webp" alt="Golden Gate Dock icon appearance preview: Blue Light" width="830"></a>
</p>

<p align="center">
  <strong>Blue Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-blue-42692e6defe8.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-blue-42692e6defe8.webp" alt="Golden Gate Dock icon appearance preview: Blue Dark" width="830"></a>
</p>

<p align="center">
  <strong>Purple Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-purple-f505c90f757a.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-purple-f505c90f757a.webp" alt="Golden Gate Dock icon appearance preview: Purple Light" width="830"></a>
</p>

<p align="center">
  <strong>Purple Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-purple-de2ddd0fdac7.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-purple-de2ddd0fdac7.webp" alt="Golden Gate Dock icon appearance preview: Purple Dark" width="830"></a>
</p>

<p align="center">
  <strong>Pink Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-pink-8a5dddb388f5.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-pink-8a5dddb388f5.webp" alt="Golden Gate Dock icon appearance preview: Pink Light" width="830"></a>
</p>

<p align="center">
  <strong>Pink Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-pink-35b9f3ee83b9.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-pink-35b9f3ee83b9.webp" alt="Golden Gate Dock icon appearance preview: Pink Dark" width="830"></a>
</p>

<p align="center">
  <strong>Red Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-red-4f92758a9626.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-red-4f92758a9626.webp" alt="Golden Gate Dock icon appearance preview: Red Light" width="830"></a>
</p>

<p align="center">
  <strong>Red Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-red-95f297477353.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-red-95f297477353.webp" alt="Golden Gate Dock icon appearance preview: Red Dark" width="830"></a>
</p>

<p align="center">
  <strong>Orange Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-orange-9a56e2ebccdf.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-orange-9a56e2ebccdf.webp" alt="Golden Gate Dock icon appearance preview: Orange Light" width="830"></a>
</p>

<p align="center">
  <strong>Orange Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-orange-cf8fa5dc1f63.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-orange-cf8fa5dc1f63.webp" alt="Golden Gate Dock icon appearance preview: Orange Dark" width="830"></a>
</p>

<p align="center">
  <strong>Yellow Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-yellow-2acdddb4feb4.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-yellow-2acdddb4feb4.webp" alt="Golden Gate Dock icon appearance preview: Yellow Light" width="830"></a>
</p>

<p align="center">
  <strong>Yellow Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-yellow-9dcd8b6de570.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-yellow-9dcd8b6de570.webp" alt="Golden Gate Dock icon appearance preview: Yellow Dark" width="830"></a>
</p>

<p align="center">
  <strong>Green Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-green-0feca8496131.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-green-0feca8496131.webp" alt="Golden Gate Dock icon appearance preview: Green Light" width="830"></a>
</p>

<p align="center">
  <strong>Green Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-green-524aa37bd27b.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-green-524aa37bd27b.webp" alt="Golden Gate Dock icon appearance preview: Green Dark" width="830"></a>
</p>

<p align="center">
  <strong>Gray Light</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-light-dock-gray-fed59e6cbc46.webp"><img src="src/screenshots/previews/readme-golden-gate-light-dock-gray-fed59e6cbc46.webp" alt="Golden Gate Dock icon appearance preview: Gray Light" width="830"></a>
</p>

<p align="center">
  <strong>Gray Dark</strong><br>
  <a href="src/screenshots/previews/readme-golden-gate-dark-dock-gray-0e1e1330d670.webp"><img src="src/screenshots/previews/readme-golden-gate-dark-dock-gray-0e1e1330d670.webp" alt="Golden Gate Dock icon appearance preview: Gray Dark" width="830"></a>
</p>

<br>

### Golden Gate Shell (Alpha)

文件、编辑等菜单随当前窗口切换。系统菜单可打开设置和会话控制。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-menu-9b7732bf8f54.webp" alt="Kate 打开文档时的文件菜单" width="830">
  <img src="src/screenshots/previews/readme-golden-gate-dark-menu-187b654fc97f.webp" alt="Kate 打开文档时的文件菜单" width="830">
</p>

<br>

### Golden Gate 日历 (Alpha)

点击面板时钟即可打开玻璃背景的月历。滚动鼠标滚轮或使用方向键切换月份，按 Home 键返回本月。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-calendar-a57f0c15b7e4.webp" alt="日历 · 浅色" width="328">
  <img src="src/screenshots/previews/readme-golden-gate-dark-calendar-3f6fce9327f4.webp" alt="日历 · 深色" width="328">
</p>

<br>

### Golden Gate 控制中心 (Alpha)

Wi-Fi、声音、亮度和通知集中在一个玻璃菜单中。外观按钮用太阳表示浅色模式，用月亮表示深色模式，用双色圆形表示自动模式。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-control-b2f97f2b1d01.webp" alt="Control Center in light mode" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-dark-control-4381ce71a5ec.webp" alt="Control Center in dark mode" width="415">
</p>

<p align="center">
  <strong>Wi-Fi</strong><br>
  <img src="src/screenshots/previews/readme-golden-gate-light-wifi-da9772cd7a44.webp" alt="Wi-Fi · 浅色" width="328">
  <img src="src/screenshots/previews/readme-golden-gate-dark-wifi-d0681f7df173.webp" alt="Wi-Fi · 深色" width="328">
</p>

<p align="center">
  <strong>电池</strong><br>
  <img src="src/screenshots/previews/readme-golden-gate-light-battery-a210d9bfc206.webp" alt="电池 · 浅色" width="328">
  <img src="src/screenshots/previews/readme-golden-gate-dark-battery-f4c19532b2b6.webp" alt="电池 · 深色" width="328">
</p>

<br>

### Golden Gate 通知 (Alpha)

玻璃质感的通知横幅和分组历史记录，支持应用操作和直接回复。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-notification-history-73984031c763.webp" alt="通知 （浅色模式）" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-light-notifications-a04d36feef81.webp" alt="通知 （浅色模式）" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-dark-notifications-f25aa49ee123.webp" alt="通知 （深色模式）" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-dark-notification-history-0e0da3b5fead.webp" alt="通知 （深色模式）" width="415">
</p>

<br>

### Golden Gate 剪贴板历史 (Alpha)

直接在 Launchpad 中查找并复用复制的文字和图片。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-clipboard-201f48d695ba.webp" alt="Clipboard history in the golden-gate launcher in light mode" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-dark-clipboard-a33e0f449807.webp" alt="Clipboard history in the golden-gate launcher in dark mode" width="415">
</p>

<br>

### Golden Gate 系统信息 (Alpha)

硬件、软件和主题信息，文字颜色随背景调整。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-about-297e9c7ea212.webp" alt="浅色模式的系统信息窗口，控制按钮位于左侧" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-dark-about-00f124f6732c.webp" alt="深色模式的系统信息窗口，控制按钮位于右侧" width="415">
</p>

<br>

### Golden Gate Plasma 主题 (Alpha)

采用协调浅色和深色配色的半透明菜单与弹出窗口。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-context-f1061c4f2d17.webp" alt="Desktop context menu in light mode" width="415">
  <img src="src/screenshots/previews/readme-golden-gate-dark-context-4d8aba01c050.webp" alt="Desktop context menu in dark mode" width="415">
</p>

<br>

### Golden Gate 启动画面 (Alpha)

从启动到关机保持一致外观，内置 LUKS2 加密磁盘解锁功能。

<p align="center">
  <img src="src/screenshots/previews/readme-golden-gate-light-boot-6d6f3b7d649e.webp" alt="Plymouth startup splash with a progress bar" width="415">
</p>

<br>

![功能](https://img.shields.io/badge/features-6B4B8A?style=for-the-badge&logo=github&logoColor=white)

- **语言：**安装程序支持英语、西班牙语、简体中文、巴西葡萄牙语、德语和法语；Plasma 组件已翻译。
- **安装程序：**图形化组件选择、随附主题资源和更新支持。
- **发行版：**为基于 Arch、基于 Fedora、openSUSE、Debian 和 KDE neon 的系统安装依赖。
- **调度：**通过 systemd 用户定时器或 OpenRC 上的 cron 自动切换主题并提供 OLED 保护。
- **玻璃特效：**浅色和深色模式下可调节的模糊、折射和三色渐变。
- **兼容性：**Plasma 6.6–6.8，原生特效根据已安装的 Qt 和 KWin 版本编译。
- **Launchpad：**两种布局、内嵌或独立搜索、收藏和可滚动应用分类。
- **Dock：**悬停放大、通知徽章、自动隐藏，重新安装时保留固定项。 多屏时，指针需在另一屏幕底边停留 2 秒 Dock 才会移过去，避免点击窗口底部时 Dock 挡住窗口。 Dock 始终显示时保持悬浮和圆角：在其屏幕上最大化的窗口会停在 Dock 正上方，Dock 则贴紧屏幕底边，与 macOS 一致。
- **菜单栏** 多屏时所有菜单栏保持一致：显示或隐藏托盘图标、更改小组件设置（时钟、苹果菜单、控制中心）会应用到每个屏幕的菜单栏。添加、移除或移动小组件仍只作用于单个菜单栏。
- **外观：**桌面、应用、图标和窗口装饰的浅色/深色风格同步；每个显示器独立壁纸。
- **应用集成：**全局菜单、GTK 菜单修复、Finder 风格 Nautilus，以及带配置备份的 Firefox 主题。
- **恢复：**要求检查、设置备份和卸载还原。
- **可选功能：**OLED 面板位移，以及实验性 NixOS 和 Home Manager 模块。
- **测试：**回归测试、发行版容器和 Plasma 虚拟机。

<br>

![入门](https://img.shields.io/badge/getting-started-3B7B5B?style=for-the-badge&logo=gnubash&logoColor=white)

下载并打开安装程序：

```bash
git clone --filter=blob:none https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde.git
cd macos-golden-gate-liquid-kde
./installer
```

选择 **Express** 进行安装。再次打开 `./installer` 即可更新或卸载。

释放磁盘空间并保留 Git 工作副本和本地工作：

```bash
./installer --free-space
```

| 安装程序语言 | 状态 |
| --- | --- |
| 🇺🇸 英语 | ![可用](https://img.shields.io/badge/Available-1A7F37) |
| 🇪🇸 西班牙语 | ![可用](https://img.shields.io/badge/Available-1A7F37) |
| 🇨🇳 简体中文 | ![可用](https://img.shields.io/badge/Available-1A7F37) |
| 🇧🇷 巴西葡萄牙语 | ![可用](https://img.shields.io/badge/Available-1A7F37) |
| 🇩🇪 德语 | ![可用](https://img.shields.io/badge/Available-1A7F37) |
| 🇫🇷 法语 | ![可用](https://img.shields.io/badge/Available-1A7F37) |
| 🇮🇹 意大利语 | ![可用](https://img.shields.io/badge/Available-1A7F37) |
| 🇯🇵 日语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 🇰🇷 韩语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 🇷🇺 俄语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 🇸🇦 阿拉伯语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 🇮🇳 印地语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 🇳🇱 荷兰语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 🇵🇱 波兰语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 🇹🇷 土耳其语 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |

<details>
<summary><b>系统要求</b></summary>

所需的桌面环境、构建工具和系统软件包。

- KDE Plasma 6.6+
- Python 3.10+ 和 PyQt6
- `sudo`
- Qt 6 开发工具
- 用于编译型 Plasma 组件和 KWin 特效的 KDE 与 Qt 6 开发包
- `cmake`, `g++`，以及 `pkg-config`（选择编译功能时）
- `dbus-send`
- `systemctl` 或 `crontab`（用于计划功能）

下载文件、缺失依赖和可选的 KDE Rounded Corners 需要网络连接。

| 发行版 | Qt 6 工具 | KDE Plasma 6 开发包 |
|--------|------------|-----------------------------------|
| Arch 系列 | `pacman -S qt6-tools` | `pacman -S extra-cmake-modules plasma-workspace kdecoration libplasma libnotificationmanager libksysguard plasma-activities-stats` |
| Fedora 系列 | `dnf install qt6-qttools-devel` | `dnf install extra-cmake-modules plasma-workspace-devel kdecoration-devel libplasma-devel knotifications-devel libksysguard-devel kf6-plasma-activities-devel` |
| openSUSE Tumbleweed | `zypper install qt6-tools-devel` | `zypper install extra-cmake-modules plasma6-workspace-devel kdecoration-devel libKF6Plasma-devel libnotificationmanager6-devel libksysguard6-devel libKF6PlasmaActivitiesStats6-devel` |

</details>

<details>
<summary><b>OLED 保护</b></summary>

可选的面板位移；默认关闭。

在 **OLED 保护** 页面启用。在此选择位移间隔和最大像素位移；默认关闭。

**手动控制**

```bash
mac-tahoe-oled-care shift
mac-tahoe-oled-care restore
mac-tahoe-oled-care status
```

</details>

<details>
<summary><b>在虚拟机中测试</b></summary>

在隔离的 Plasma 桌面中试用主题。

```bash
./vm <os>
```

**OS:** `cachyos` · `arch` · `manjaro` · `endeavouros` · `garuda` · `fedora` · `nobara` · `opensuse` · `neon` · `debian` · `artix` · `kubuntu`

`all` 启动所有发行版。[虚拟机设置与验证指南](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/README.md)。

`./vm kubuntu` 启动以 SHA-256 固定的 Kubuntu 26.04.1 LTS ISO；配置来宾后使用回环 SSH 端口 `2234`。此启动器回归测试目标尚待完整的实际运行验证。

</details>


<br>

![兼容性](https://img.shields.io/badge/compatibility-system%20support-4B6B8A?style=for-the-badge&logo=linux&logoColor=white)

检查你的发行版、初始化系统和 Plasma 版本的支持情况。

<details>
<summary><b>发行版</b></summary>

此表中的全部 11 个发行版均通过实际虚拟机验证。选择状态徽章以查看已审阅截图和测试结果。

| | 名称 | 状态 |
|:--:|------|---------|
| <img src="https://cdn.simpleicons.org/cachyos" alt="CachyOS" width="22"> | CachyOS | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#cachyos) |
| <img src="https://cdn.simpleicons.org/archlinux" alt="Arch Linux" width="22"> | Arch Linux | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#arch) |
| <img src="https://cdn.simpleicons.org/endeavouros" alt="EndeavourOS" width="22"> | EndeavourOS | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#endeavouros) |
| <img src="https://cdn.simpleicons.org/fedora" alt="Fedora" width="22"> | Fedora | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#fedora) |
| <img src="https://cdn.simpleicons.org/manjaro" alt="Manjaro" width="22"> | Manjaro | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#manjaro) |
| <img src="https://cdn.simpleicons.org/linux" alt="Linux" width="22"> | Artix Linux (OpenRC) | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#artix) |
| <img src="https://cdn.simpleicons.org/linux" alt="Linux" width="22"> | Garuda Linux | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#garuda) |
| <img src="https://cdn.simpleicons.org/nobaralinux" alt="Nobara" width="22"> | Nobara | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#nobara) |
| <img src="https://cdn.simpleicons.org/opensuse" alt="openSUSE" width="22"> | openSUSE Tumbleweed | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#opensuse) |
| <img src="https://cdn.simpleicons.org/kde" alt="KDE" width="22"> | KDE neon | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#neon) |
| <img src="https://cdn.simpleicons.org/debian" alt="Debian" width="22"> | Debian testing / sid (Plasma 6.6+) | [![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37)](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md#debian) |

</details>

<details>
<summary><b>初始化系统</b></summary>

自动主题切换和 OLED 保护使用以下调度后端：

| 初始化系统 | 调度 | 已记录测试 |
| --- | --- | --- |
| systemd | 用户定时器 | ![桌面虚拟机已验证](https://img.shields.io/badge/Desktop%20VM%20verified-1A7F37) |
| OpenRC | 用户 cron | ![Artix 桌面虚拟机已验证](https://img.shields.io/badge/Artix%20desktop%20VM%20verified-1A7F37) |
| dinit | 用户 cron | ![调度已验证](https://img.shields.io/badge/Scheduling%20verified-1A7F37) ![桌面虚拟机测试待完成](https://img.shields.io/badge/Desktop%20VM%20testing%20pending-D4A017) |

OpenRC 和 dinit 需要运行中的 cron 守护进程。
[桌面测试结果](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/tests/vm/PROOF.md) · [dinit 调度检查](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md#setup)。

</details>

<details>
<summary><b>Plasma 版本</b></summary>

支持 Plasma 6.6–6.8；编译特效使用宿主 SDK。

| Plasma | 支持 | 起始版本 |
|--------|---------|-------|
| 6.5 及更早版本 | ![不支持](https://img.shields.io/badge/Not%20supported-D1242F) | 不适用 |
| 6.6 | ![支持](https://img.shields.io/badge/Supported-1A7F37) | v0.1.0 |
| 6.7 | ![支持](https://img.shields.io/badge/Supported-1A7F37) | v0.19.0 |
| 6.8 | ![支持](https://img.shields.io/badge/Supported-1A7F37) | v0.54.1 |

</details>

<br>

![路线图](https://img.shields.io/badge/project-roadmap-6B4B8A?style=for-the-badge&logo=github&logoColor=white)

目前可用的功能和计划添加的内容。

<details>
<summary><b>组件状态</b></summary>

各组件的当前状态。

| 组件 | 状态 |
|-----------|--------|
| 配色方案 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 壁纸 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 字体 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 光标 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Plasma 主题 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Kvantum 主题 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| GTK 主题 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Acrylic Glass | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| KDE Rounded Corners | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 自动主题切换器 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| OLED 保护 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 安装程序界面 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 本地化 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Aurorae 装饰 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 全局菜单 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Dock | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Finder 风格 Nautilus | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Launchpad | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Shell | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 剪贴板历史 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 系统信息 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 回收站 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 声音 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 启动画面 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 关机画面 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| Firefox 主题 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 图标 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 多发行版支持 | ![支持](https://img.shields.io/badge/Supported-1A7F37) |
| OpenRC 测试 | ![虚拟机已验证](https://img.shields.io/badge/VM%20verified-1A7F37) |
| Konsole 主题 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| Kate 主题 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| SDDM 主题 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 日历 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 控制中心、Wi-Fi、电池和通知 | ![Alpha](https://img.shields.io/badge/Alpha-D4A017) |
| 系统偏好设置 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |
| 操作系统选择器 | ![计划中](https://img.shields.io/badge/Planned-D4A017) |

</details>

<br>

**[报告错误](https://github.com/lestercorderomurillo/macos-golden-gate-liquid-kde/issues/new)**，或使用 **Apple 菜单 → 关于本机 → 报告错误…**。

请提供：

- 你的 Plasma 版本： `plasmashell --version`
- 你的发行版： `grep PRETTY_NAME /etc/os-release`
- **关于本机**中显示的主题版本
- 显示问题的截图或录屏

请保持拉取请求范围集中，并使用 `./vm` 验证。参阅 [CONTRIBUTING.md](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md)。

共享的[图标生成工具集](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/CONTRIBUTING.md#icon-generation-toolset)基于 Tahoe 随附图标创建浅色、深色、单色和半透明玻璃外观，支持任意 RGB 色调。从 Tahoe 工作副本运行 `./icon-toolset`，可为任一版本离线生成、预览、验证和打包图标。所有图标实现和资源均保留在 Tahoe 中。

<br>

![免责声明](https://img.shields.io/badge/disclaimer-not%20affiliated%20with%20apple-6B6B6B?style=for-the-badge&logo=apple&logoColor=white)

这是受 macOS 美学启发的独立重新实现。与 Apple 或 KDE 无关联，也未获其背书。“macOS”和“Apple”是 Apple Inc. 的商标。

macOS 27 徽标、随附壁纸、系统声音及 SF Pro / SF Mono 字体仍属于 Apple，不受本项目许可证覆盖。其他组件保留各自许可证和版权声明；有关范围及已知来源缺口，请参阅下方第三方声明索引。

整体以 [GPL-3.0](LICENSE) 授权；各组件许可证和第三方权利仍适用。请参阅[版权声明](NOTICE)、[许可与项目身份](LICENSING.md)及[第三方声明](THIRD_PARTY_NOTICES.md)。

<br>

![致谢](https://img.shields.io/badge/credits-%26%20inspiration-8A6B4B?style=for-the-badge&logo=apple&logoColor=white)

项目参考与第三方组件：

- **[EliverLara](https://github.com/EliverLara/TahoeLauncher)**: `TahoeLauncher`: Launchpad 设计参考。
- **[vinceliuice](https://github.com/vinceliuice)**: `MacTahoe-icon-theme`: 基础图标和光标；GTK 设计参考。
- **[taj-ny](https://github.com/taj-ny/kwin-effects-forceblur)** 和 **[4v3ngR](https://github.com/4v3ngR/kwin-effects-glass)**: Better Blur 及其玻璃分支：Acrylic Glass 使用的上游代码。
- **[luisbocanegra](https://github.com/luisbocanegra/plasma-panel-colorizer)**: `plasma-panel-colorizer`, 离线随附，用于为面板着色。
- **[Matin Lotfaliei](https://github.com/matinlotfali/KDE-Rounded-Corners)**: `KDE-Rounded-Corners`, 基于宿主 KWin SDK 构建的 KWin 窗口圆角特效。
- **[ful1e5](https://github.com/ful1e5)**: `apple_cursor`: 替代光标设计参考。
- **[sahibjotsaggu](https://github.com/sahibjotsaggu)**: `San-Francisco-Pro-Fonts`: SF Pro / SF Mono 包的来源。
- **[Lucide](https://github.com/lucide-icons/lucide)**: 全局菜单随附的复制图标。
- **[512pixels.net](https://512pixels.net/projects/default-mac-wallpapers-in-5k/)**: 高分辨率 macOS 壁纸档案。

受 macOS 美学启发的独立重新实现，与 Apple 无关联，也未获其背书。“macOS”和“Apple”是 Apple Inc. 的商标；随附壁纸和 SF 字体仍属于 Apple。以 GPL-3.0 授权。


[安装程序截图与测试](TESTING.md)。
