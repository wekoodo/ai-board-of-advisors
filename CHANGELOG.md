# Changelog

Notable changes to the **Board of Advisors product** (system/factory content). Personal boards
pick these up via the product `upstream` remote — see `_config/shared/updates.md` and the README
section *Keeping your board up to date*.

[Keep a Changelog](https://keepachangelog.com/)-style sections; [SemVer](https://semver.org/)-inspired versions.

## [Unreleased]

### Changed

- Replace the in-repo `maintaining-icm` skill with the published `icm` skill from
  `wekoodo/skills`, pinned in `skills-lock.json`.
- Drop the `obra/superpowers` skill set from the project lockfile.
- Refresh the `google-doc-style` pin in `skills-lock.json` (skill v1.1).

### Added

- Pin `google-doc-style` from `wekoodo/skills` in `skills-lock.json`.

### Removed

- Tracked `.agents/skills/maintaining-icm/` (now restored from the lockfile like other skills).

After merging this change, restore project skills with `npx skills experimental_install`. If
leftover Superpowers copies remain on disk, run `npx skills remove --all` and then restore.

## [0.1.0] — TBD

Initial release.
