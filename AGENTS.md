# Golden Gate

## Required skills

Read and follow these skills on every task in this repository:

- [communication-autonomy](skills/lester-skills/communication-autonomy/SKILL.md) — work silently, interrupt only for real decisions or blockers, and close with a one-line "Done." report.
- [Skill organization](skills/lester-skills/other-skills.md) — keep Lester and other skill collections under `skills/`.

## Clean install-ready delivery

After every fix or release, leave the user's actual VS Code checkout clean and
ready to install, in both Tahoe and Golden Gate. Publishing from an isolated
worktree does not complete delivery while the checkout the user opens remains
behind or contains leftover edits. Synchronize that checkout to the delivered
commit, including VERSION, the upstream pin and component hashes as applicable.

Commit and deliver all task-owned changes, including AGENTS.md. Keep generated
logs, temporary captures, build output and machine-specific .vscode settings out
of tracked changes. Never hide dirt with assume-unchanged or skip-worktree, or
ignore files that belong in version control.

Coordinate with other agents before reconciling a shared checkout. Preserve
uncommitted work that is not part of the delivery in a named, recoverable local
backup before moving the checkout; never discard it with reset --hard or git
clean. Do not reapply obsolete release edits over the delivered version. If
active work prevents a clean checkout, resolve ownership or report that specific
blocker instead of claiming the repository is ready.

Check local git status once after the final checkout update and resolve any
remaining task-owned changes. This is a local delivery check, not permission to
repeat remote publication queries, rerun passed tests or wait for full CI.
Documentation-only policy changes need no new version or release.

## Paired repository delivery

Tahoe and Golden Gate are one connected delivery. Work requested in either
checkout covers the corresponding changes in both repositories unless the user
explicitly excludes an edition. A repository name, working directory or
edition-specific README heading alone does not limit that scope.

For shared documentation subjects such as About This Computer and Finder,
update the matching README images in both editions and both appearance modes.
Capture each edition with its own defaults, wallpaper and controls; never
reuse one edition's photograph as the other. Refresh only the requested
subjects and preserve unrelated photographs and their original provenance.
Reuse a counterpart update already completed in the same task.

Keep shared implementation exclusively in Tahoe and deliver Golden Gate's
matching version and verified pin for implementation releases. Publish paired
releases and deliver to dev and main in both repositories. Documentation,
photography and agent-policy updates also require paired delivery, but do not
bump versions, move release tags or publish releases for those changes alone.
Apply shared policy corrections to both AGENTS.md files. Do not report the
work complete after delivering only one repository; finish the counterpart or
report its specific blocker. Leave both actual checkouts clean and ready.

## Efficient scope and repository graph

Select tests by the behavior they prove. When one executable scenario covers
A, B, C and D, keep that scenario and remove duplicate source-text assertions.
Keep independent failure cases, security checks and distinct SDK coverage;
"probably covered" is not evidence of equivalent coverage. Do not add tests
that merely assert workflow wording, test names, file lists or this policy.
Test executable CI helpers through their behavior when they can lose coverage.

Use the offline graph before broad repository reads:
`python3 tools/repo_graph.py --repo <checkout> <changed-path> ...` from Golden
Gate. Omit paths for the working diff; use `--limit 10` for compact output,
`--limit 0` for every impact or `--all` for the adjacency graph. The tool works
on either checkout without network, packages or an AI service. Follow its
caller links and read only affected functions first. Dynamic imports, generated
paths and native/SDK dependencies need manual scope review; this navigation aid
must never silently exclude tests from CI. No suggested tests is a coverage
question, not a pass. Agent tooling in `tools/` is permitted in Golden Gate;
shared desktop/installer implementation still belongs exclusively in Tahoe.

CI cancels superseded runs on the same ref. Preserve all distro legs and the
disjoint primary shards. Reuse weekly distro SDK layers and compiler results;
retain compiler-content checking and never enable unsafe cache sloppiness.
Selected qualification precedes merge; the full remote matrix stays async.

## Review and merge qualification

Every implementation release requires a focused install/reinstall check in at
least one disposable Plasma VM before publication. Record the actual source,
commands and results. Captures alone do not replace installer qualification or
resolve known CI failures. Dependency changes require the exhaustive package
mapping checks; translated messages require catalog checks; native rendering
tests must pass with their declared dependencies in a clean CI environment.

A request to review, fix, test and merge means review the diff and existing CI
results first, repair relevant failures, then qualify the candidate before
merging. A successful compile, plugin load or workflow submission does not
prove rendering behavior. Do not merge first and leave required validation
for the user to discover afterward.

Choose a small representative set by the behavior and compatibility boundaries
actually changed, not every distro by default. For shared KWin effect, shader
or ABI changes, cover the supported 6.6, 6.7 and 6.8 SDK/API branches using
selected distro environments, and exercise at least one real isolated X11
rendering case plus Wayland when shared code affects it. One environment may
prove multiple claims; another distro is needed only for a distinct relevant
SDK, package layout or observed failure. Record build, load and visible behavior
separately. Include existing executable shader/pixel regressions when shader
inputs or coordinate conventions change; source-text checks are not substitutes.

The selected qualification checks must pass on the final implementation before
merge. Inspect existing CI failures and resolve those relevant to the change;
do not choose a passing subset to avoid an observed regression. Reuse matching
passing evidence and running CI jobs rather than launching duplicate matrices.
The complete distro matrix stays enabled and may finish asynchronously. Once
the selected checks pass, publication does not wait for every distro or a
second run on main. Investigate later failures with a focused reproduction and
repair; do not automatically revert an entire delivery for every CI failure.
Revert when the user requests it or the failure warrants withdrawing the change.
Never describe pending or unrun checks as passed.

Release commands must stop on failed prerequisites. Verify the version, immutable
pin, archive checksum and evidence before committing or pushing a release tag;
use fail-fast scripts or separate dependent commands. Never continue publication
after a failed validation command. Policy-only edits need no new release.

## Respect for the user's time

Apply these rules in both Tahoe and Golden Gate. They supersede older delivery
or communication wording below. In the user's sense, *necio* means persisting
stubbornly after a correction, not useful diligence ([Diccionario del español
de México](https://dem.colmex.mx/ver/necio)). The following are concrete failure
patterns to stop, not reasons to remove necessary correctness checks.

1. Rechecking publication after a successful publishing command: use that result; do not issue a second release lookup.
2. Polling a release repeatedly: submit the authorized operation and report the known outcome; do not invent an obligation to wait.
3. Rechecking remote branches after a successful push: use the push result unless it reports an error or ambiguity.
4. Narrating plans, tool calls or implementation details: omit routine process narration; explain only when asked or when needed for user input.
5. Repeating unchanged status messages: no stream of “still waiting”, “verifying” or “almost done”.
6. Announcing that you will be concise or respectful: demonstrate it in the response instead.
7. Delaying publication for the entire remote matrix: pass the selected qualification before merge, then publish without waiting for every distro; keep full CI asynchronous.
8. Waiting for main to repeat dev's result: promote the same commit without a polling job.
9. Running the full matrix twice for the same delivered change: run it on dev and on PRs; main promotion does not launch a duplicate.
10. Running runtime CI for Markdown-only edits: use documentation/path filters; do not build native components for prose.
11. Repeating passing local tests after bookkeeping: reuse evidence while tested code, inputs and environment are unchanged.
12. Running the whole suite for a narrow fix: choose affected behavior and expand only for a concrete failure or dependency.
13. Taking every screenshot for one changed component: capture only the needed views in a disposable VM.
14. Revalidating the entire historical gallery at every release: retain original provenance and check changed artifacts; do not repeat historical audits without cause.
15. Replacing reviewed images because the version changed: preserve them and their actual capture identity.
16. Expanding a bug fix into an unsolicited redesign or framework: make the smallest complete repair.
17. Asking again for permission already granted: act within the existing authorization.
18. Asking questions already answered by the repository or session: consult existing context first.
19. Treating old AGENTS wording as stronger than a new user instruction: apply the user's correction and reconcile the conflicting rule.
20. Reciting internal checklists to the user: keep operational records in files and return the useful result.
21. Printing long logs when one error explains the failure: inspect quietly and surface only the decision-relevant issue.
22. Sending coordination acknowledgment loops: message peers for ownership conflicts or actionable handoffs, not ceremonial updates.
23. Bumping versions or publishing releases for instruction-only edits: commit and push the documentation without release churn.
24. Continuing after the requested result is complete: stop; do not add a new verification phase.

Default final response: the result, its usable link/path when relevant, and a
material unresolved limitation if one exists. Do not describe how it was done
unless requested. Ask only for missing input that changes the outcome. Never
claim an unobserved success: “submitted” is sufficient when an asynchronous
operation has only been submitted. A failed operation still needs correction;
removing redundant confirmation is not permission to hide failure.


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
release, checked against that release's `VERSION`. Never replace a newer pinned
release candidate with an older stable release. Compact RC tags such as
`0.63rc1` sort after `0.62.0` and before `0.63.0`.
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
| Defaults, materials or appearance | Target the changed behavior, affected editions and saved choices. Use a disposable VM only for rendering or transition claims that need visual evidence; scope it to the changed component. Documentation photography follows the optional capture policy. |
| Native backend, ABI or distro packages | Build against the affected SDKs and test the changed backend on representative distros with distinct relevant SDK/package layouts. Record build, load and behavior results separately. |
| Documentation or agent instructions only | Review consistency, references and `git diff --check`; no manual pytest, native builds or VM runs. |

For an X11 fix, run at least one representative isolated X11 session and
verify both module loading and the reported behavior. Cover affected KWin
6.6, 6.7 and 6.8 SDK/API branches with selected distro environments; add another
runtime distro only for a distinct relevant compatibility difference or failure.
Include install/reinstall/uninstall regressions only when those paths changed,
and a Wayland regression when shared code changed. Compilation or plugin loading
alone does not prove rendering. Missing X11 support is a coverage gap, not a pass.
Do not repeat unrelated desktop lifecycle qualification across distros.

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

For implementation delivery, run focused local checks for the affected behavior,
review component-scoped VM captures when needed, and record their exact source
fingerprint in `release-evidence.json`. Complete the selected merge qualification
above and resolve relevant known CI failures, then publish the installable fix. Full remote CI remains enabled and runs asynchronously on
`dev`; `main` promotion does not run a polling or duplicate test job.
Do not wait for the full matrix or repeat the historical screenshot audit before
telling the user the release can be installed. Clearly distinguish local checks,
reviewed captures, published release and pending/passed/failed remote CI. Never
call pending, cancelled, skipped or failed checks successful. Investigate later
CI failures and deliver a corrective release when necessary. Preserve complete
CI coverage; this policy changes publication ordering, not the test matrix.

Documentation-only delivery does not require a version bump, pin update,
release or new screenshots. Automatic push CI may still run; report its status
accurately without launching duplicate checks or waiting for unrelated runtime
jobs as proof of a prose edit. Honor explicit user testing constraints and
report any resulting coverage gaps; never describe unrun checks as passed.

## Delivery and project requirements

Publish matching `v<version>` releases in both repositories. Deliver completed
changes to both `dev` and `main` in both repositories, and use successful push output as delivery evidence; do not re-query refs. Release titles must
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

Visual validation and documentation photography are separate tasks. A visible
change may justify a focused visual check; it does not require refreshing the
documentation gallery. New documentation captures are optional unless the user
requests them or an affected published image would otherwise misrepresent the
changed behavior. A request to "show me" authorizes a focused preview of the
changed component, not a full release capture run.

Before starting a VM, name the changed component, the visible difference and
the exact frames needed. For a Dock application-list or icon-alias change,
check the affected Dock in the relevant editions and appearance modes. Do not
recapture installer pages, window materials, Files, About This Computer, boot
or shutdown unless the diff changes their behavior or the user requests a
gallery refresh. The Dock appearing incidentally in another screenshot does
not by itself require replacing that screenshot.

Reuse reviewed images with their original source commit, hashes and provenance;
never relabel them as newly captured. A new version, source commit, VM checksum,
profile change or capture-tool limitation is not evidence that every component
changed. Do not modify the global capture profile or rebuild the full gallery
merely to obtain a focused preview. If the publication tooling cannot preserve
unaffected images, report that limitation and keep the preview separate; do not
expand the capture scope to satisfy the tool. A rejected new frame must not be
replaced by an older image presented as fresh evidence.

Once the planned affected checks pass, stop. Do not repeat them for documentation,
version or release bookkeeping. A user instruction to stop testing cancels
further test, VM, capture and manual CI launches; preserve completed evidence
and report any remaining publication gate without trying to satisfy it through
another test route.

When new documentation captures are needed, use Tahoe's `./release-screenshots`
with the pinned VM and capture profile. Stage this edition's reviewed images
with `stage --edition golden-gate --destination <this-checkout>` when refreshing
that gallery. Focused previews may be published separately with reviewed source
hashes. Retain unchanged galleries with original provenance and identify them as
historical where appearance changed; do not relabel them as current captures.
Publish through `.github/workflows/release.yml` after fast local-evidence and
immutable pin/archive checks. Full remote CI runs asynchronously; it does not
block publication or the user's installation. Never represent pending or failed
CI as passed. Do not create releases outside the workflow.
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

Express uses automatic Dock appearance. The first update to 0.64 applies Dock
preset revision 3 even without layout reset; later reinstalls preserve removed
pins and icon choices unless reset is selected. Keep existing pins in order,
append only installed equivalents, and retain Firefox/browser names and artwork.
The shared implementation and migration evidence belong in Tahoe.

Maintain Tahoe's `component-hashes.json` with each component change using
`python src/scripts/component_manifest.py --write`. Commit the ledger with the
implementation; CI checks it against the sources. Hash components and individual
plasmoids independently, including their installation recipe dependencies.
Never use VERSION or a repository commit as a global reinstall key. Runtime
reuse must compare actual staged content and relevant choices, detect missing
or changed installed files, and record success only after completion. Keep
explicit configuration changes and resets outside payload reuse. The shared
implementation and ledger belong only in Tahoe.

Installer Nautilus and Dolphin previews must show one focused application per
frame. Check window identity, focus and settled geometry immediately before and
after each photograph inside a disposable VM; reject interrupted captures.
Use Tahoe's `release-screenshots file-previews` for these four light/dark frames.

Menu appearance comparisons use real screenshots of the corresponding macOS
edition, aligned at the same display scale and blended at 50/50 opacity.
Do not use a Tahoe photograph as Golden Gate evidence or vice versa. Installer
source defaults remain Tahoe with launcher preset 1 and Golden Gate with
preset 2; explicit per-step choices still override their own setting. Native
menu selections use the measured 8px corners, while edition materials remain
independent of the launcher preset. Record any remaining geometry differences
instead of claiming a pixel-identical match.

Native menu outer borders use continuous corners independently of the 5px
content inset. Keep the blue selection at its measured 8px corners. The
MacTahoe Qt style delegates ordinary widgets and edition materials to Kvantum;
install its sidecar in both editions and retain it through light/dark switches.

System-menu symbols follow the active edition's real macOS reference. Tahoe
shows symbols on every action; Golden Gate shows only About, System Settings
and App Store, without reserved icon columns on other rows. Keep Recent Items
absent. `kdeglobals`'s `MacTahoeLiquidKde/SystemMenuPreset` follows the active
edition through light/dark transitions, independently of the Launcher preset;
read it again whenever the cached menu opens. System Settings uses the
reference 18-tooth wheel with three spokes and a hollow hub. Preserve the
existing App Store symbol and refresh each README's own light/dark menu frames.

Use the original Apple glyph outlines from the bundled font for system-menu
symbols, not hand-drawn approximations. Regenerate the committed paths with
`src/scripts/build_menu_symbols.py`; keep the font hash, glyph identities and
uniform transforms in `systemmenusymbols.json`. The plugin must not require
a host Apple font or an SVG loader at runtime. App Store remains unchanged.
