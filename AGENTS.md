# Golden Gate

## Repository write boundary

Write only inside the active repository. Filesystem access is not permission
to write elsewhere. An exception requires the user's explicit instruction to
change a specific external location (for example, a host configuration).
A request to test, debug, build, capture, or release does not grant that permission.

Keep all agent-created temporary files in the repository's existing
`build/<task>/`. If the repository uses `temporal/` instead, use that.
Ensure Git ignores the directory before writing. Put test homes, temporary
directories, caches, logs, downloads, VM overlays, worktrees, and previews
there. Configure tool output paths, including `TMPDIR` and tool-specific
cache paths, before running tools. Resolve paths and symlinks before writing.
External prepared images and tools may be read in place. If a tool needs an
external write, choose a repository-local method or stop and identify the
required location. Never move scratch work to another disk for extra space.
If `build` is an existing executable, use the ignored `temporal/` directory.
Give each run an isolated directory and clean it automatically on exit,
including errors and cancellation (for example, a context manager or shell
trap). Remove task-owned Git worktrees with `git worktree remove`. Keep only
requested deliverables and necessary recovery evidence. Never stage scratch files.

## No lazy mode

When the user reports a problem or corrects an earlier answer, take the next
authorized action that advances the fix. Every problem report must produce
a concrete, verifiable output greater than zero bytes, such as a patch, a
working artifact, or a diagnostic record with the observed failure and its
cause when known. An apology, promise, or repeated explanation is insufficient.
If blocked, finish independent work and identify the exact remaining blocker.
Ask only for a decision or permission the user has not already given.

### Mistake dictionary

Whenever an agent makes a mistake, correct the user's deliverable first. Then
update this dictionary in both editions during the same task. Record what
happened, the assumption or decision that caused it, and an observable check
that prevents recurrence. Extend an existing entry when the mistake repeats.

| Mistake | What went wrong | Check before closing |
| --- | --- | --- |
| Overstating the Adaptive Contrast sampling limit | The backdrop grid interval was described as a limit on all sampling. The per-glyph sampler uses a separate timer. | Identify each GPU readback path and report the measured cadence for the path changed. |
| Maximizing the completion window | Bringing the ready page forward was mistakenly implemented as maximizing the wizard. | Minimize the wizard during installation and verify completion restores its original window size. |
| Treating a local installer as a published fix | After v0.84.32 restored the older installer, the agent provided a local fullscreen launcher and repeatedly explained the rollback. It treated the working candidate as the endpoint even though the user wanted the ordinary published installer. | Follow the release request through both publication workflows once the applicable approval is in hand. Verify each published tag contains or pins the fix and synchronize the ordinary checkouts. Give the user both release links. |
| Validating a fresh package instead of an upgrade | A calendar copied into a test guest showed the new glass, while an ordinary reinstall skipped the existing desktop packages and still reported success. | Seed the previous installed packages, including valid packages without ownership records, and run the normal reinstall. Compare installed contents against the staged candidate and verify that stored settings and personal recovery copies survive. |
| Documenting before repairing | When the user asked why the release was missing, the agent prioritized writing a rule while the requested deliverable was still missing. | Take the next authorized repair or delivery action first. If a decision genuinely blocks it, show the exact result and ask for that decision once. Record the lesson after advancing the repair. For contributor fixes, use the reviewed patch as a starting point, correct remaining defects and demonstrate the issue is resolved before closing the task. A list of requested changes left PR #173 unfinished. |
| Linking outside the user's VS Code workspace | The installer video was linked from a scratch disk. The agent mistakenly assumed that its own filesystem access meant the user could open the same link in VS Code. | For every local deliverable, place a usable copy in the actual repository open in VS Code. Resolve the link target, verify it is a readable, nonempty file inside that checkout, and give the user the clickable link and repository-relative path. Keep temporary previews out of release assets. |
| Leaving scratch directories on other disks | Test worktrees, VM overlays and captures accumulated outside the checkout because free space was treated as authorization. An ambiguous directory glob also sent a diagnostic log to the parent directory after a failed directory change. | Resolve every output path under the active repository’s ignored build directory before starting the tool. Stop on a failed directory change before opening a redirected output file. Golden Gate writes prepared sources under the wrapper checkout. For isolated staging, copy the wrapper into the test directory and verify its returned path is inside that copy. |
| Losing a freshly installed test guest at shutdown | The media launcher cleaned the first EndeavourOS disk before the installed-session test could open it. Native installation had to be repeated. | Before shutting down the installer media, verify the next launcher can open the entire disk backing chain and firmware from its own repository-local recovery directory. |
| Shipping a stale desktop probe fixture | The Dock probe began reading the panel ID and saved visibility, but its old negative fixture omitted the ID. Release CI found the missing ID and a package recovery message missing from every translated catalog. The Launchpad change also left the native wizard test expecting a third launcher choice. | When changing a qualification probe, run its failure-control tests and verify accepted and rejected real panel states. When adding installer recovery text, also run the catalog completeness check across every locale. For launcher choice changes, exercise keyboard selection, artwork and Settings navigation through the native wizard in both editions. |
| Using a test grid as a README photograph | The Adaptive Contrast gallery used checkerboard test frames because they documented rendering. They obscured how the feature looks on the desktop. The standalone System Information preview also showed a black outline absent from the installed Plasma dialog. | Check the requested component, framing and background at README size. When a new photograph is requested, open the component in the disposable guest, take a new exposure and verify the visible content at README size. For an adaptive effect, compare the same scene with the setting off and on and confirm a visible change before labeling it. For the System Information README photograph, open About This Computer from the installed system menu, verify that KWin reports the active window as plasmashell, and show the capture at its logical desktop width. |
| Animating mismatched desktop states | Golden Gate’s Quickbar and Finder GIFs paired approved screenshots without checking the surrounding desktop. The Dock appeared only in the dark frame. | Capture each mode with the same window geometry, crop and visible controls. Check both endpoints and the midpoint, then decode each gallery GIF to compare its frame delays with the others. Keep the Multicolor Dock on its own timing. |
| Missing overlap pixels in a recycled Apps grid | Matching isolated tile captures missed three pixels where the descender of a two-line label overlapped the next icon. A recycled Qt Quick item kept its earlier sibling paint order. | Scroll the complete Apps grid forward and backward with long names. Compare the settled crop byte-for-byte against the unpooled grid, including row boundaries. |
| Opening a graphics benchmark on the host | A graphics demo ignored an assumed help flag and opened on the host display. The process was stopped. | Inspect installed manuals or source for supported flags. Clear host display and session-bus variables before invoking any graphical benchmark, including for option discovery. |
| Misreading qualification harness failures | Passing the staging source override into updater tests disabled the mocked update. A long test directory also exceeded the Unix socket path limit. A Nobara post-reboot probe read the pristine source mount, which had no installed build identity header. | Limit staging overrides to source preparation. Give D-Bus tests a short path backed by the ignored qualification directory (count the full generated socket filename before running pytest), and run file ownership checks as the intended user. Run post-reboot probes from the same writable guest checkout used for installation and verify the generated build identity there. For generated widget QML, stage twice and compare against the first install. A native menu can enter a nested Qt event loop, so verify that timer-driven probes advance each phase exactly once. |
| Losing Control Center refraction during integration | The lens shader and its settings shipped while a half-pixel offset on Edit Controls prevented KWin from recognizing the separate tiles. | Open the installed popup and compare the same wallpaper with edge lens depth enabled and disabled. Verify a visible change on the rounded tile edges in both editions. When restoring a preset, also run the native settings module’s save and reopen test. The v0.85.15 installer checks passed while the module test still expected the superseded saturation value. When changing shared menu dependencies or panel fill defaults, run the isolated launcher popup and desktop controls pixel probes before tagging. The v0.85.22 probes staged an incomplete menu and expected the previous fill. |
| Blurring the desktop between Control Center tiles | The backdrop pass applied blur across the transparent gaps. Checking refraction inside the tiles missed the sharp-exterior requirement in issue #134. | Compare fine desktop detail in the gaps and around the popup with the popup closed and open, and verify the lens independently inside a control. |
| Giving the launcher menu a heavy black or white fill | The launcher used its own popup tint and compositor preset even though the surface already had the notification card shape. | Open Launchpad options and Notification Center in each edition and appearance. Check that their interiors use the same live material and compare actual captures over desktop content. |

## Non-negotiable execution discipline

If an operation is likely to take 20 minutes or more, treat that as a sign
that its scope may exceed the request or its method may be inefficient. First
look for a smaller sufficient check or an existing prepared environment.
Before starting or retrying a run that still needs 20 minutes or more, tell
the user the expected time and what makes it necessary.
If a run exceeds its estimate or attempts for the same objective total
20 minutes, stop that approach and report the result so far. Reuse verified
work or choose a faster approach. Continue the long run only when the user
explicitly authorizes it. Count base provisioning, retries and storage
allocation when estimating VM work.

**Top priority: Do not make changes the user did not request.** Treat
everything outside the requested change as a constraint to preserve. When
editing or recapturing an approved result, use that result and its provenance
as the baseline. Compare the candidate against it and correct any unrelated
difference before presenting or publishing the work. If a necessary deviation
cannot be avoided, explain it and get approval before making it.

Work quickly on the requested change. Choose the smallest executable checks
from the diff and its direct risks; expand only for an observed failure or a
specific affected dependency. Reuse passing evidence while code, inputs and
environment remain unchanged. Do not repeat tests for release bookkeeping.

For a visible change, use a capture of the affected component on the candidate.
If it clearly shows the requested behavior, that capture is the complete
focused validation. “Retest and fix” does not require a separate test run.
Reuse a matching capture or take the needed frame with the existing capture
tools in a prepared isolated environment. Do not build a custom harness, add
a test suite or provision a new VM for a question the capture answers.

If the capture shows a defect, keep it out of the gallery, fix the defect
and recapture the same view. Use another check only for a specific behavior
the image cannot establish. Show the passing visual change for approval
before publication. Keep this workflow in maintainer files, outside product
UI and README feature copy.

Keep one prepared KDE neon base for routine capture checks and README previews
in both editions. Install the current candidate in a disposable overlay and
use the edition's defaults. Keep release qualification independent and select
its checks from the affected behavior and existing coverage. A successful
capture answers the visual claim it exercised.

Brief nonvisual fixes proceed to paired release after focused checks. Changes
to colors, icons, materials, layout or other appearance require the user's
explicit approval of the actual preview before merge or publication. Passing
VM/CI checks or the agent's own visual review does not replace that approval.
The approval boundary below takes precedence over every delivery rule here.

Full CI and the distro matrix remain enabled and asynchronous. Do not run a
second matrix on main, wait for unrelated CI or expand a narrow change into a
redesign. Honor deadlines, stop optional work and report genuine blockers.
For CI optimization, preserve coverage and measure before/after under stated
cache conditions; an unmet requested speedup is not a completed optimization.

## Required skills

Read and follow these skills on every task in this repository:

- [communication-autonomy](skills/lester-skills/communication-autonomy/SKILL.md) — work silently, interrupt only for real decisions or blockers, and close with a one-line "Done." report.
- [Skill organization](skills/lester-skills/other-skills.md) — keep Lester and other skill collections under `skills/`.

For visible desktop changes, use [macos-visual-identity](skills/lester-skills/macos-visual-identity/SKILL.md)
to identify the matching approved component and reference before implementation.

Task-specific development skills are indexed in [skills/catalog.md](skills/catalog.md).
Load only the relevant skill; `.agents/skills/` holds discovery links to the
canonical collections under `skills/`. Project policy and current user
instructions govern authorization and qualification.

## Clean install-ready delivery

After an approved delivery, synchronize both actual VS Code checkouts to the
delivered commits, including versions, pins and component hashes. Commit all
task-owned changes, including policy; keep logs, builds and machine settings
out of tracked changes. Check local status once after the final update.

Coordinate ownership before moving a shared checkout. Preserve unrelated work
in a named recoverable backup; never discard it, hide it with index flags or
reapply obsolete release edits. Pending visual work belongs on an isolated
candidate branch/worktree and must not replace the approved installation.

## Paired repository delivery

Tahoe and Golden Gate are one delivery unless the user explicitly excludes an
edition. Shared implementation and assets stay in Tahoe; Golden Gate receives
the matching version and immutable pin. Deliver approved work to dev/main in
both repositories. Shared policy corrections belong in both AGENTS.md files.

Documentation/policy-only edits need diff review and `git diff --check`, then
paired commits/pushes; no runtime tests, version bump, tags, release or CI wait.
For visual documentation, obtain approval of the new photographs first.
Capture each edition with its own defaults and preserve unrelated photographs
and their actual provenance. Never reuse one edition's capture as the other.

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

## Standing authorization for fixes and releases

There are two delivery paths:

- **Brief nonvisual fix:** focused checks, then commit, fast-forward dev/main,
  tag and publish the paired release without another permission question.
- **Visual or judgment-dependent change:** research, implement and test the
  candidate, show the actual result beside its reference where applicable,
  then wait for the user's explicit visual approval. Before approval, do not
  merge/promote the candidate, bump versions, move the released pin, push a
  release tag or publish. A request to continue working is not approval.

Approval covers the shown result. Material changes after approval need a new
preview and approval. Once approved, complete paired delivery autonomously;
never ask again for individual commits, pushes or release operations.
A request to test harder adds focused validation, not permission to skip the
visual decision. Later corrective fixes follow the same two delivery paths.

Use fail-fast release commands. Verify versions, immutable pin, archive checksum
and evidence before tagging. Publish through the release workflows, Tahoe first.
Report observed publication results and the known CI status; submitted is not
published, and pending or failed is not passed. Repair relevant failures when
observed; do not silently withdraw or revert a release without cause.
After publication, check the tag's release workflow and the tests for the
released commit on dev in both repositories. Follow pending runs to completion,
investigate failures, and report each final result with its run link.

## Appearance synchronization qualification

Every shipped plasmoid, glass surface and menu must follow the effective system
appearance in both editions. Qualify light, dark and automatic mode, including
an actual automatic boundary crossing; choosing auto without observing its
transition is not a pass. Keep Qt/Kvantum and GTK 3/4 applications open while
switching through native KDE settings, the standalone switcher and supported
GTK preferences. Exercise rapid successive and overlapping selections and prove
that the latest selection wins without stale surfaces, palettes or controls.
A manual selection supersedes the project schedule; native KDE automatic mode
keeps KDE's scheduler authoritative. Preserve saved material optics, window
controls, user wallpapers and unrelated preferences. Never test on the host.
Record installed source fingerprints, application continuity, rendered evidence
and the exact VM/SDK coverage; configuration readback alone is insufficient.

## Review and merge qualification

Changes to installer lifecycle require a focused install/reinstall check in a
disposable Plasma VM before publication. Other changes require only the checks
that prove their affected behavior. Record the actual source, commands and results. Captures alone do not replace installer qualification or
resolve known CI failures. Dependency changes require the exhaustive package
mapping checks; translated messages require catalog checks; native rendering
tests must pass with their declared dependencies in a clean CI environment.

A request to review, fix, test and merge means review the diff and existing CI
results first, repair relevant failures, qualify the candidate and obtain any
required visual approval before merging. A successful compile, plugin load or workflow submission does not
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
the selected checks pass and required visual approval is granted, publication
does not wait for every distro or a second run on main. Investigate later failures with a focused reproduction and
repair; do not automatically revert an entire delivery for every CI failure.
Revert when the user requests it or the failure warrants withdrawing the change.
Never describe pending or unrun checks as passed.

Release commands must stop on failed prerequisites. Verify the version, immutable
pin, archive checksum and evidence before committing or pushing a release tag;
use fail-fast scripts or separate dependent commands. Never continue publication
after a failed validation command. Policy-only edits need no new release.

All icon variants must preserve the original layers, paths, silhouette, cutouts and existing borders of every icon. Change layer colors and opacity only; never add a tile, rim, bevel, shadow or replacement artwork. Qualify default light/dark, clear light/dark and tinted light/dark against macOS references, using red and blue for tint calibration.

Dock icon qualification includes Apps, every pinned application, and both empty/full Trash. Use the bundled original artwork and its aliases; tint/material changes must not substitute newly invented symbols. Check application aliases separately from reserved menu symbols. Review facial details and lettering at actual Dock size over light and dark backgrounds. Generate icons deterministically from original artwork and explicit material parameters, never an image model. For performance-only changes, compare output hashes and benchmark the same fixture; reuse reviewed photographs when pixels are unchanged. State examples such as full Trash do not belong in color tables.

## Respect for the user's time

Before allocating qualification or capture disks, use the
[Plasma VM qualification skill](skills/lester-skills/plasma-vm-qualification/SKILL.md)
to check available space under the active checkout’s ignored build directory and plan per-guest cleanup.

Disposable development VM overlays, capture working copies and source archives
must be removed once the requested qualification is complete and its reviewed
images and evidence are preserved. Do not retain whole VM disks as release
evidence. Preserve unique scripts, logs and recovery data in a named compact
backup before cleanup; never delete active work or user-owned files. Report
before/after allocated sizes for storage cleanup tasks. Installer cleanup only
removes recognized successful-build intermediates, including older cached builds;
failed-run diagnostics, final binaries, compiler caches and user recovery data
remain available.

Keep routine work silent; explain only decisions, material findings or blockers.
Use successful push/publication output as evidence without repeat lookups. Do
not poll unrelated CI, rerun passed checks, refresh unrelated photographs or
keep working after delivery. When corrected, change the next action.

Finish with the result, a useful link and any material limitation. For a visual
candidate, show the preview and ask for approval; do not claim release delivery.
Ask only for missing input that changes the outcome.

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

### README presentation

Show Dock photographs as one visible vertical list, with a short label for each appearance or tint. Do not use tables or collapsed galleries for the Dock.

Use concise, factual English descriptions without marketing slogans or em dashes.
Use a colon for label and title separators in project documentation.
Follow the punctuation conventions of each translation. Preserve the punctuation of
compound words, Markdown list markers, version ranges and technical syntax.
Use the repository's edition name in feature headings: Finder, Launchpad, Dock,
Shell, Control Center, Clipboard History, System Information, Plasma Theme and
Boot Splash. Mark Shell, Control Center and Clipboard History as Alpha; do not
add Alpha to System Information. Place the small centered distro-status caption
above the distro icons.

Show each feature once. Keep Finder and About/System Information photographs in
their own sections, with no duplicate Finder or About gallery. Use only the
startup photograph in Boot Splash. Keep implementation/reference links and
capture-provenance commentary out of feature descriptions; retain the underlying
provenance records and all required attribution and license notices. Credits
should identify references and actual third-party components without promotional
appeals. Use green text badges for available, supported or verified states,
yellow for Alpha, planned, in-progress or pending states, and red for unsupported
states. Preserve explicit coverage limits when summarizing testing.

Keep the contribution guide linked and include verified contributors and issue
reporters from both repositories, with working local avatars and profile links.
Apply shared README edits to both editions using their respective names, defaults
and photographs. Do not restore removed explanatory sections or duplicate
screenshots during release bookkeeping. Batch requested editorial changes until
the user finishes; commit and deliver both repositories when asked to publish.
An explicit request for fresh photographs covers the requested README features,
not the installer gallery or unrelated artwork.

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

Use the least costly environment that can prove each claim. Reuse applicable
evidence and existing CI environments. Run focused executable checks in an
existing distro container or isolated graphical session when it provides the
required SDK, render stack and backend. For a rendering claim, exercise the
actual renderer and check visible output. A build or a configuration check
alone is insufficient.

Use a disposable desktop VM when the claim depends on an installed Plasma
session, system lifecycle or hardware integration, or when a desktop preview
is required. Check the local inventory first and reuse a prepared image with
the required dependencies through a disposable overlay. A listed distro, a
downloaded ISO and a raw cloud image are provisioning inputs. Provision or
rebuild a guest only when a required check has no suitable prepared base.
Existing scope, approval and backend requirements still apply.

| Change | Required focused validation |
| --- | --- |
| Wrapper, downloader or source selection | Wrapper suite, including local-source staging, release fallback and checksum/version handling where affected. |
| Tahoe implementation | Component regressions and affected installer lifecycle paths in Tahoe; exercise the prepared Golden Gate source when edition staging can change the result. |
| Defaults, materials or appearance | Target the changed behavior, affected editions and saved choices. Use isolated rendering checks when they can exercise the affected stack. Use a prepared desktop VM for desktop-dependent behavior and required previews. |
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
above and resolve relevant known CI failures, then publish the installable fix after any required visual approval. Full remote CI remains enabled and runs asynchronously on
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

After the applicable approval gate, publish matching `v<version>` releases in both repositories. Deliver completed
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
that gallery. Share focused previews separately for user review, with source hashes;
public documentation changes require approval. Retain unchanged galleries with original provenance and identify them as
historical where appearance changed; do not relabel them as current captures.
After any required visual approval, publish through `.github/workflows/release.yml` after fast local-evidence and
immutable pin/archive checks. Full remote CI runs asynchronously; it does not
block publication or the user's installation. Never represent pending or failed
CI as passed. Do not create releases outside the workflow.
The capture implementation belongs only in Tahoe; do not vendor it here.

The shared installer must record a verified uninstall wallpaper reset as
project-applied state. Reinstallation replaces that unchanged background while
preserving a background selected afterward by the user. A Breeze/Next filename
alone is not proof of ownership; legacy misclassified states require an
explicit reset. Keep this implementation in Tahoe.

The shared Acrylic Glass KCM offers Tahoe Clear (blur 5), Tahoe Frosted
(blur 12) and Golden Gate Official (blur 4), with stable saved material IDs 1 and 2. Retired Clear ID 0 falls
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
the Dock defaults to no gradient while retaining blur and refraction; its component controls may override that default.
Launcher labels use the system foreground shifted 40% toward black or white.
Use the sampled background and client fill to select readable grid and list
text. Light-mode category pills retain their translucent white backing.
Golden Gate light mode uses full-opacity search text. Category fills use 68% white when selected and 52%
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
Do not use a Tahoe photograph as Golden Gate evidence or vice versa. Both editions
install the Tahoe launcher preset and honor “Use my launcher”. Native
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

Dock and Control Center gradients default off in every material and appearance mode; explicit component overrides may enable them. Preserve blur and refraction. Recover separate rounded blur islands and let shader coverage antialias their edges; integer region clipping must not cut off fractional coverage. Keep transparent gaps and custom cutouts intact.

Acrylic Glass stores an independent component map for each stable material/variant ID. The KCM selector covers general windows, Finder, menus, other Plasma popups, Apps + Clipboard, search, Control Center, About, Dock and menu bar, with the same optical controls. Preserve existing defaults and legacy saved optics when migrating. Dock and Control Center gradients default off in all three presets but may be enabled explicitly for that component. Switching presets retains their edits; Restore resets only the selected preset. Background transparency edits Plasma/Kvantum SVG fills and About/Control Center QML fills, never whole-window opacity. Apply must patch owned assets transactionally and reload live surfaces; Cancel must not write assets. Preserve mode-specific values, unrelated app mappings and externally edited files. Keep implementations and preset definitions exclusively in Tahoe.
