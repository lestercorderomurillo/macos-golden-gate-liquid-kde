# Golden Gate

Golden Gate is a parameterized distribution of macos-tahoe-liquid-kde.
All implementation and wallpaper assets live in Tahoe. Keep this repository
limited to the downloader, its tests, `defaults.json`, the audited upstream
pin, release version, documentation, screenshots and the existing banner. Do not vendor Tahoe here.

The shared offline `icon-toolset` also lives only in Tahoe. It generates icon
appearances from the bundled base with arbitrary RGB glass tints; Golden Gate
documents that tool without copying its implementation or generated assets.

Every entry point stages `GOLDEN_GATE_TAHOE_SOURCE` or a complete sibling
`../macos-tahoe-liquid-kde` checkout when present. An explicit source override
is development mode: do not query releases or update either checkout.
For ordinary `install` and `installer` launches, compare each checkout's
`VERSION` to its latest published release independently. Update only a clean
checkout whose HEAD is an ancestor of the verified release commit, then
restart the wrapper when it changed. A sibling alone never disables updates.
Preserve local edits, untracked files, deletions and divergent commits; report
newer releases without replacing that development source. Never downgrade an
equal or newer local version. An incomplete dirty sibling must fail clearly
instead of silently switching away from the developer's source.
Stage a content-addressed copy with Golden Gate defaults; never apply those
defaults to the Tahoe checkout. Include untracked source files and omit tracked
deletions when staging local work. `--prepare`, uninstall, test and VM entry
points never update checkouts. `MAC_TAHOE_NO_UPDATE_CHECK=true` disables all
update queries. Without local sources, select the latest published Tahoe
release, checked against that release's `VERSION`.
`upstream.json` is
the verified fallback when GitHub's API is unreachable or
`MAC_TAHOE_NO_UPDATE_CHECK=true`, and the reference for release checks.
Update it with both a published immutable commit and its archive SHA-256.
The selected commit must contain edition support and MacGoldenGate.
Validate the wrapper and prepared Tahoe source according to the testing scope
below; this does not require repeating the full shared suite for every edit.
`GOLDEN_GATE_TAHOE_SOURCE` allows testing a local Tahoe checkout before publishing.

## Documentation style

Keep TESTING.md as a concise snapshot of the latest verified release, stated
once, followed by the installer photographs. Replace the previous summary;
never append a changelog, superseded candidates or unreleased development logs.
Keep one short validation summary with a link to detailed evidence and coverage
limits. When consolidating accumulated history, reduce the document by at least
half. Preserve reviewed photographs, content-hashed filenames and original
provenance; do not recapture or relabel unchanged images. Keep README concise
and put installer photographs only in TESTING.md.

Limit README installation/update notes to two short lines of user actions.
Omit updater internals and repeated explanations; keep technical details in
CONTRIBUTING.md or linked developer documentation.

## Testing scope and evidence

Cover all affected behavior and preserve complete CI coverage. Separate focused
development checks, final integration checks, distro compatibility, and release
evidence; they answer different questions and are not interchangeable.

Before testing, briefly identify the changed behavior, its callers and shared
dependencies, affected editions/backends/SDKs, and the checks that prove each
claim. Use the actual diff, not just the issue title, to choose scope. Expand
that scope when a failure or shared dependency reveals another affected path.

| Change | Required focused validation |
| --- | --- |
| Wrapper, downloader or source selection | Wrapper suite, including local-source staging, release fallback and checksum/version handling where affected. |
| Tahoe implementation | Component regressions and affected installer lifecycle paths in Tahoe; exercise the prepared Golden Gate source when edition staging can change the result. |
| Defaults, materials or appearance | Affected editions, light/dark transitions, saved choices and relevant visual checks in a disposable VM. |
| Native backend, ABI or distro packages | Build against the affected SDKs and test the changed backend on representative distros with distinct relevant SDK/package layouts. Record build, load and behavior results separately. |
| Documentation or agent instructions only | Review consistency, references and `git diff --check`; no manual pytest, native builds or VM runs. |

For an X11-only fix, test the affected component on at least two supported
distros with X11 available, covering the relevant KWin ABI differences. Verify
the intended module loads and the reported behavior is fixed in an isolated
session. Include install/reinstall/uninstall regressions when those paths
changed, and a Wayland regression check when shared code changed. A successful
compile or plugin load alone does not prove rendering is correct. Missing X11
support is a coverage gap, not a pass. Do not repeat unrelated desktop lifecycle
qualification on every distro for this fix.

Run focused checks while implementing; reserve broad integration runs for a
stable candidate. Required CI supplies the complete suite and configured distro
matrix on the final implementation commit. Do not also run the entire matrix
locally unless CI cannot exercise the needed case or a failure needs local
reproduction. Run the shared suite against the prepared source when staging
changes executable behavior; a pin-only update to an already validated Tahoe
commit needs wrapper/pin checks and affected staged regressions, not another
identical full Tahoe run.

Record commands or CI links, source commit/content, environment, results and
coverage limits. Reuse passing development evidence while its code, inputs and
environment remain unchanged. After a further edit, rerun the affected checks;
broaden only for a concrete dependency, failure or coverage gap. New test
dependencies must work in every affected CI image. Never duplicate a running
matrix just to obtain the same evidence sooner. Once the planned checks pass
and coverage gaps are resolved, stop testing unless new changes invalidate
that evidence.

For implementation delivery, inspect required CI results for the exact commits
on both branches. Earlier-commit evidence never substitutes for the exact-SHA
release gate: publication requires successful `test.yml` push runs on `main`
and `dev` for each repository's exact release commit. Never weaken workflows,
skip required checks or treat missing,
cancelled or failed checks as success to shorten a task. Screenshot provenance verification remains mandatory; new visual tests and
captures are conditional on a clear visual change, as specified below.

Documentation-only delivery does not require a version bump, pin update,
release or new screenshots. Automatic push CI may still run; report its status
accurately without launching duplicate checks or waiting for unrelated runtime
jobs as proof of a prose edit. Honor explicit user testing constraints and
report any resulting coverage gaps; never describe unrun checks as passed.

## Delivery and project requirements

Publish matching `v<version>` releases in both repositories. Deliver completed
changes to both `dev` and `main` in both repositories, and verify both remote
branches include them before reporting completion. Release titles must
be exactly `v<version>`, with no subtitles, descriptions or other extra text.
This repository's
`VERSION` must equal the pinned Tahoe source's `VERSION`; `upstream.json` must
reference the commit tagged for that Tahoe release. Publish Tahoe first,
verify the archive checksum, then publish Golden Gate. Each README must show
the preset and wallpaper its edition installs by default.

`defaults.json` selects `launcher_preset: 2` alongside the Golden Gate wallpaper.
The pinned Tahoe source must include `launcher_defaults.py`. Both launcher
presets stay selectable from the options menu and General settings; do not
force the edition default over an explicit saved choice.
Both presets keep every category pill vertically aligned, including categories
created while scrolling. The shared Tahoe implementation centers pills inside
full-height ListView delegate cells; do not position the delegates themselves.

Preserve the README Credits section and existing local banner artwork.
Preserve existing copyright and component license notices. Follow `NOTICE`,
`LICENSING.md`, and `THIRD_PARTY_NOTICES.md`; keep GPL intact,
without copying, rebranding, or commercial-use bans or claims to third-party marks.
Never run the live installer as a test or change the user's desktop.

Capture documentation screenshots only inside a disposable VM. Never switch
the host theme, move its windows, or inject host input for screenshots. Run
captures sequentially, verify labels and window identity, and review each image
before publishing it.

Run visual tests and capture documentation screenshots only when the actual
change clearly affects visible output: layout, colors, materials, typography,
icons, wallpaper, controls or rendered UI content. A release, version bump,
updater fix, translation of console-only messages, documentation edit or CI
change alone does not justify visual tests or new captures. State the concrete
visual impact before starting a VM. Reuse reviewed screenshots and their
original provenance when visual inputs are unchanged; never relabel old images
as newly captured. Run focused visual checks only for affected components,
editions and modes, and do not repeat an unchanged passing check. A failed or
rejected new frame cannot be filled with an older image.

When new documentation captures are needed, use Tahoe's `./release-screenshots`
with the pinned VM and capture profile. Stage this edition's reviewed images
with `stage --edition golden-gate --destination <this-checkout>`. After pinning
the published Tahoe release, verify committed screenshots with
`--repo <this-checkout> verify --tahoe-repo <tahoe-checkout>`, including when
existing reviewed images are retained. Publish through
`.github/workflows/release.yml` against the immutable Tahoe pin.
The release workflow requires successful `test.yml` push runs on both `main`
and `dev` for the exact Golden Gate commit and the exact pinned Tahoe commit. Its shared CI gate is itself pinned
to an immutable Tahoe commit. Never bypass failed, cancelled, skipped or missing CI. Never bypass it with direct `gh release create`.
The capture implementation belongs only in Tahoe; do not vendor it here.

The shared installer must record a verified uninstall wallpaper reset as
project-applied state. Reinstallation replaces that unchanged background while
preserving a background selected afterward by the user. A Breeze/Next filename
alone is not proof of ownership; legacy misclassified states require an
explicit reset. Keep this implementation in Tahoe.

The shared Acrylic Glass KCM offers Tahoe and Golden Gate materials, both
with blur strength 5 and stable saved IDs 1 and 2. Retired Clear ID 0 falls
back to Tahoe without resetting saved optics when opening the KCM.
Installing or reinstalling Acrylic Glass selects the complete Golden Gate
material, replacing saved material selections and optical overrides while
preserving radius controls and window rules. Preset data and rendering
live only in Tahoe, including Plasma/Kvantum popup surfaces. Golden Gate stages
light Plasma popups, tooltips, the detached search capsule and native Qt menus
with 60% white fill so dark text stays readable. Dark surfaces retain 1% white
fill. About This Computer must use those same mode-dependent Golden Gate
fills. Its `hint-clear-surface` marker identifies the edition; it must never
force 1% white in light mode. Keep light/dark/light transition and
secondary-label contrast tests in Tahoe so this regression cannot be approved
as expected behavior.
Preserve the saved gradient, blur and refraction in both modes; apply
these surfaces in both the installer and Nix staging.
Tahoe retains 55% white light fills and slightly clearer 48% black dark fills.
Golden Gate menus retain their black upper gradient in light and dark mode:
85% black at the top, fading to zero at 55% of the surface height;
the Dock is exempt from the gradient while retaining blur and refraction.
Launcher text uses a soft, low-opacity halo of the opposite luminance, without
a hard outline. Light-mode category pills have a translucent white backing
for readable dark labels. Keep this shared implementation in Tahoe.
In Golden Gate light mode, the Apps input uses full-opacity text and a
stronger diffuse halo. Category fills use 68% white when selected and 52%
otherwise. These changes follow the staged edition independently of the
selected launcher preset; preserve Tahoe and dark-mode styling.
There is no Reduced Transparency preference or generated opaque variant.

Published screenshots must include the first 12 hexadecimal characters of their
content SHA-256 in the filename (for example, `launcher_preset_1_light-abc123def456.png`).
Update README links and provenance together, remove replaced image files and
obsolete aliases, and preserve unrelated artwork. Apply this in both repositories
every time images are published; never overwrite a changed image at its old URL.

Main README desktop screenshots must show Files and About This Computer in
separate images in each appearance mode. Each frame must contain only its
featured application with that window focused; reject combined or unfocused
frames. Enforce this in capture and release validation. This requirement is
for the main README gallery, not distro qualification/OS screenshots.

The shared v0.61 installer is a single native PyQt6 wizard. `install` and
`uninstall` are aliases for the graphical UI, with no legacy or terminal wizard.
Keep the native implementation in Tahoe. Source-edition defaults are first and
selected on every new wizard launch; user choices are scoped to one transaction.

Keep installer screenshots in TESTING.md, linked from the README. Desktop and Dock
photographs remain in the README; stage and verify both documentation files.

Golden Gate window controls are generated offline by Tahoe's
`window_controls.py` for Aurorae and GTK 3/4. Preserve Tahoe buttons, shared frame geometry
and shadow controls. Install both Aurorae families and select the edition in
the switcher, global-theme defaults and verifier. GTK < 4.20 needs explicit
mode selection for literal button URLs in its adaptive legacy stylesheet;
keep ownership detection and screenshot verification consistent with it.

The native wizard has a Window controls step with Flat and Glassy choices and
reviewed, high-resolution Nautilus title-bar crops from a disposable VM.
Window shadows has its own page with None, Soft, Medium and Hard comparison
crops in light and dark mode; keep shadows out of the Effects page.
Defaults remain edition-specific (Tahoe Flat, Golden Gate Glassy), but an explicit transaction
choice overrides the edition for Aurorae, GTK, global-theme defaults and the
standalone switcher. Preserve the choice through light/dark transitions; new
wizard launches still start from source-edition defaults.
