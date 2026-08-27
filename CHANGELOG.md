# Changelog

Notable changes to the **Board of Advisors product** (system/factory content). Personal boards
pick these up via the product `upstream` remote — see `_config/shared/updates.md` and the README
section *Keeping your board up to date*.

[Keep a Changelog](https://keepachangelog.com/)-style sections; [SemVer](https://semver.org/)-inspired versions.

## [Unreleased]

_Notes for the next release after v0.2.0 go here._

## [0.2.0] — 2026-08-27

### Added

- Add an index-first, local-only meeting-history router so the board can find prior meetings
  without preloading the complete history.
- Pin `google-doc-style` from `wekoodo/skills` in `skills-lock.json`.

### Changed

- Throttle opportunistic product-update checks to once per calendar day and keep routine checks
  separate from the deeper update protocol.
- Harden the update flow's routing and privacy boundaries.
- Separate the `google-doc-style` board overlay from Always-load protocol and load it only for
  reader-facing writing.
- Load the shared ethics rules consistently in every advisor contract.
- Replace the in-repo `maintaining-icm` skill with the published `icm` skill from
  `wekoodo/skills`, pinned in `skills-lock.json`.
- Drop the `obra/superpowers` skill set from the project lockfile.
- Refresh the `google-doc-style` pin in `skills-lock.json` (skill v1.1).

### Fixed

- Require the complete profile schema before onboarding can pass its completion gate.

### Removed

- Tracked `.agents/skills/maintaining-icm/` (now restored from the lockfile like other skills).
- Factory authoring plans, specs, and handoffs under `docs/superpowers/` so they do not ship with
  the product or propagate into personal boards.

After updating to v0.2.0, restore project skills with `npx skills experimental_install`. If
leftover Superpowers copies remain on disk, run `npx skills remove --all` and then restore.

## [0.1.0] — 2026-07-08

Initial release.
