# Changelog

Notable changes to the **Board of Advisors product** (system/factory content). Personal boards
pick these up via the product `upstream` remote — see `_config/shared/updates.md` and the README
section *Keeping your board up to date*.

[Keep a Changelog](https://keepachangelog.com/)-style sections; [SemVer](https://semver.org/)-inspired versions.

## [Unreleased]

### Added

- Add an optional entity registry (`_config/profile/entities/`) with a tracked `_template/`,
  basic `overview.md` during general onboarding, and an in-depth interview that runs only
  when the user asks.
- Add an optional living-trust profile (`trust.md`) and a focused `trust-onboarding.md`
  route. Neither is required to complete general onboarding.
- Add meeting **Profile write-back** so standing facts land in `_config/profile/` in the same
  session, plus a **Profile updates** line on the advisor Handoff block.
- Nest meeting records under `meetings/<scope>/<topic>/` (`personal`, `trust`, or an entity
  slug) only when `entities/index.md` exists. Boards with no entity registry keep
  `meetings/<topic>/`.

### Changed

- Expand output conventions with an **Evidence and calculation** protocol: sourced,
  user-reported, assumed, and illustrative figures; verify current rules when retrieval
  exists; trace arithmetic; carry material evidence on the Handoff block.
- Load `_config/profile/CONTEXT.md` and follow scoped rules instead of bulk-loading every
  profile file (including entity folders).
- Ignore all real profile content in `.gitignore` while tracking `profile/CONTEXT.md`,
  `profile/entities/CONTEXT.md`, and `profile/entities/_template/`.

## [0.3.0] — 2026-09-05

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
  not CFA; 05 holds a CFA charter and does not claim Series 65; 08 drops CIC). Replace
  elite / world-class openers with a short nameplate and a will-not-do line.
- Make `collaboration.md` the source of truth for roster credentials and cross-referrals
  under one-way containment: every pair an advisor lists must appear there; the file may
  list extra pairs. Asset location is 05 ↔ 02; contribution sequencing stays 01 ↔ 02; 01
  flags a Roth window and 02 owns conversion math.
- Move custom-advisor instructions to `advisors-extended/` only.
- State the US default in `ethics.md`, the chair convening map, and 02 (the seat that
  dropped an international-tax claim).
- Remove named brands from the corporate attorney seat (keep the asset-protection ideas).
- Point estate-tax exposure at an illustrative federal exclusion in 07 frameworks
  (about $15M per person, indexed annually) instead of a year-vantage sunset sentence.

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
