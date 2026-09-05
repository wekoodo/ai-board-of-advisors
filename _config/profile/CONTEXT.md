# Profile

Persistent personal, financial, and optional entity and trust facts live in this directory.
Real profile content is stored here and excluded from Git by default. Cloning the repository
does not restore it. Content sent to a cloud model follows that provider's policies. This file
routes advisors to the smallest relevant profile set; it does not authorize loading every
entity folder.

## Profile Files

| File | Contains | Requirement |
|------|----------|-------------|
| `personal.md` | Name, location, family structure, health | Required |
| `financial.md` | Income, assets, liabilities, cash flow, insurance coverage | Required |
| `businesses.md` | High-level holdings map, or confirmation that none are owned | Required |
| `investments.md` | Portfolio allocation, accounts, risk tolerance, time horizon | Required |
| `goals.md` | Short, medium, and long-term goals; current concerns | Required |
| `trust.md` | Living trust or similar estate vehicle (optional; may shim to `trust/`) | Optional |
| `entities/index.md` | Known entities, relationships, onboarding status, and profile paths | Optional |

`entities/index.md` and `trust.md` appear only when onboarding records them. Tracked
`entities/CONTEXT.md` and `entities/_template/` are not evidence that the user owns entities.
General onboarding is complete without `index.md` or `trust.md`.

## Scoped load rules

1. For every consultation, load this router and the core files relevant to the question from
   `personal.md`, `financial.md`, `businesses.md`, `investments.md`, and `goals.md`. If a named
   file is a shim, follow `../shared/icm-conventions.md` **Resolve a named profile path** and
   load only the resolved sections this question needs. Do not recursively load the directory.
2. If `trust.md` exists and the question is about that estate vehicle, ownership, succession,
   titling, or family governance, also load `trust.md`. Resolve a shim the same way. Do not load
   the complete `trust/` folder unless the user asked for a full trust review.
3. For explicit trust onboarding, load `../setup/trust-onboarding.md` only when the user asked
   to begin or resume it. Do not start that interview from a meeting mention.
4. If `entities/index.md` exists and the matter is entity-scoped, load `entities/CONTEXT.md`,
   `entities/index.md`, and only the named entity folder or folders. Entity-scoped meeting
   records live at `meetings/<entity-slug>/<topic-slug>/`, not inside the profile folder.
   Follow `../../meetings/CONTEXT.md`.
5. For a cross-entity matter, load the smallest set of entity profiles needed to understand the
   relationship. Do not preload every entity.
6. When an entity has only `overview.md`, use the known facts and identify missing detail. Offer
   in-depth onboarding when the missing facts affect the work. Do not start it unless the user
   asks.
7. If `entities/index.md` is absent, there is no entity layer. Keep meetings at
   `meetings/<topic-slug>/`. If that index is created later, leave existing flat meeting
   folders in place; follow `../../meetings/CONTEXT.md` **Existing records stay put**.

## Agent Instructions

1. Follow the scoped load rules; do not bulk-load `entities/`.
2. If a loaded file's "Last Updated" date is more than 12 months ago, note it at the start of the
   session and offer to update. For a shim, use the resolved owning section's date, not the shim
   stamp alone.
3. `businesses.md` is required as an onboarding-completion signal. If it says "no businesses
   owned," no further action is needed. When entities exist, treat `businesses.md` as the
   high-level map and `entities/index.md` as the authoritative entity router.
4. General onboarding requires only a basic overview for each known entity. It must not force
   in-depth onboarding for every entity, and it must not require a living trust.
5. If no required profile files exist yet, stop and direct the user to run onboarding: load
   `_config/setup/CONTEXT.md` to begin.

## Updating Profile Files

Edit any file directly, or ask an advisor to update a section. When writing or updating a profile
file, include a "Last Updated: YYYY-MM-DD" line at the top of the file you edited so the staleness
check works. If the named path is a shim, edit the resolved owning section; do not duplicate
facts in the shim. Follow `entities/CONTEXT.md` for entity status and file ownership when
`entities/index.md` exists. Follow `../shared/icm-conventions.md` **Keep files load-scoped** and **Resolve
a named profile path**: if a write would mix independently loadable concerns into a file that is
loaded as a whole, split into a folder with a `CONTEXT.md` router now. Keep a thin shim when a
completeness gate or existing load path names the old file.

A board meeting that changes standing facts must write those facts here in the same session. Do
not leave standing state only in `meetings/`. Follow `../shared/meeting-process.md`
**Profile write-back**. That check is required when minutes are written; it does not wait for the
user to ask. Write only the owning files for the scopes in the meeting. Do not bulk-load or
bulk-edit every entity folder.
