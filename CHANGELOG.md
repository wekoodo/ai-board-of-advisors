# Changelog

Notable changes to the **Board of Advisors product** (system/factory content). Personal boards
pick these up via the product `upstream` remote — see `_config/shared/updates.md` and the README
section *Keeping your board up to date*.

[Keep a Changelog](https://keepachangelog.com/)-style sections; [SemVer](https://semver.org/)-inspired versions.

## [Unreleased]

### Added

- Add a chair convening map (`_config/shared/convening.md`) so the host can pick the fewest
  seats that own a question (01 vs 05, legal form vs tax treatment, 09/10 only when the
  topic is actually energy or storage).
- Add Scope (in / out / convene-only) to every advisor contract and to the add-your-own
  template.
- Add operator frameworks to the business strategist (unit economics, pricing, bottleneck,
  hiring vs contractor, 90-day cadence) without replacing SWOT / Porter / BMC / OKR /
  growth levers.
- List typical artifacts in each advisor `references/CONTEXT.md` so the chair knows what to
  commission. Lists only — no sample files.

### Changed

- Tighten seat identity: drop prestige padding and credentials that blur jobs (01 is CFP,
  not CFA; 05 reasons like a CFA and does not claim Series 65; 08 drops CIC). Replace
  elite / world-class openers with a short nameplate and a will-not-do line.
- Make `collaboration.md` the single source for roster credentials and cross-referrals.
  Asset location is 05 ↔ 02; contribution sequencing stays 01 ↔ 02; 01 flags a Roth
  window and 02 owns conversion math.
- Move custom-advisor instructions to `advisors-extended/` only.
- State the US default in one line (chair convening map, US-law seats, ethics).
- Remove named brands from the corporate attorney seat (keep the asset-protection ideas).
- Point estate-tax exposure at an illustrative current-year exclusion in 07 frameworks
  instead of a 2025-vantage sunset sentence in the contract.

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
