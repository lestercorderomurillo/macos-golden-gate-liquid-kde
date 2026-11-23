# Third-party notices and license scope

Golden Gate contains its downloader, defaults, documentation, and preview
assets. Its shared implementation is fetched from the Tahoe commit and archive
hash recorded in [upstream.json](upstream.json). The copyright and license
notices of that exact source remain applicable; this wrapper does not replace
them or claim ownership of the upstream components.

- Preserve the downloaded source's `LICENSE`, component license files, and
  copyright/SPDX headers. The [Tahoe notice index](https://github.com/lestercorderomurillo/macos-tahoe-liquid-kde/blob/main/THIRD_PARTY_NOTICES.md)
  is a navigation aid; check the actual pinned source when redistributing.
- [Distribution logo provenance](src/screenshots/distros/sources.json) records
  per-logo sources, licenses, modifications, and hashes. The included
  [Simple Icons CC0 text](LICENSES/CC0-Simple-Icons.txt) does not override
  underlying brand rights or the per-logo license information.
- The emblems adapted from Apple artwork, Apple wallpapers, SF fonts, and system sounds are
  outside this project's GPL grant. Including them in a bundle or screenshot
  does not create a redistribution license or transfer their ownership.
- Screenshots, contributor portraits, and the existing banner can contain
  third-party artwork or likenesses. Do not treat those elements as exclusively
  owned by this project or erase their applicable attribution.

[NOTICE](NOTICE) identifies original project contributions. [LICENSING.md](LICENSING.md)
explains redistribution obligations and distinguishes official releases from
independent versions. [License text sources](LICENSES/sources.json)
record the included supplemental text's immutable source and hash.

This index is not a complete chain-of-title certification. Missing provenance
must be investigated, not filled with an assumed license or copyright owner.
The README Credits section remains separately maintained.

## Development skills

The optional development resources under `skills/qt-skills`,
`skills/wshobson-skills`, `skills/openai-skills` and
`skills/superpowers-skills` retain their upstream licenses and notices.
Their collection `upstream.json` records source commits, original hashes and
project adaptations. See [the skill catalog](skills/catalog.md). These
resources are separate development aids; their original authors retain their
rights. Project entry points and independently written helpers do not imply
upstream endorsement.
