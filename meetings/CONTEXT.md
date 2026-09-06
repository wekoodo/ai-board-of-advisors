# Meeting History Router

## Purpose

Use this router when prior meeting context may matter, or when creating a new meeting folder.
Locate one relevant meeting first, then load only the record files needed for the current question.

## Folder layout

New meeting records use a **local date-time prefix plus a topic slug**. The prefix is the
host's local calendar date and 24-hour clock at the lazy-creation threshold, formatted
`YYYY-MM-DD-HHMM` (zero-padded hour and minute; no colons, `T`, or timezone). The topic slug
is a short kebab-case label for the question. The same calendar date also lives inside
`brief.md` and `minutes.md`.

Example: `2026-09-06-1430-property-review`.

**No entity index** (`_config/profile/entities/index.md` is absent):

```text
meetings/<YYYY-MM-DD-HHMM>-<topic-slug>/
```

**Entity index exists:**

```text
meetings/<scope>/<YYYY-MM-DD-HHMM>-<topic-slug>/
```

| Scope folder | Use when |
| --- | --- |
| `personal` | Household or personal work, or portfolio-wide / multi-entity work with no single primary entity |
| `trust` | A living trust (or similar estate vehicle in `_config/profile/trust.md`) is the primary subject |
| `<entity-slug>` | One registered entity is the primary subject. Use the slug from `_config/profile/entities/index.md` (that slug must already have passed `_config/profile/entities/CONTEXT.md` **Slugs**) |

Do not pre-create empty scope folders. Create `meetings/<scope>/` lazily with the first meeting in
that scope, and only when that path is not already a meeting record. A path is a meeting record
when it contains `brief.md` or `minutes.md`. Never invent a new logical scope slug. Reserved
non-entity scopes are only `personal` and `trust`. Use `trust` only when `trust.md` exists.

Shipped `example-*` meetings stay at `meetings/example-*/` as factory references. Never add them
to the private index. Never move them under a scope folder.

Do not put meeting records inside `_config/profile/`. Profile folders hold durable facts; meetings
hold working records. When a meeting changes standing facts, write those facts back to the owning
profile files in the same session. Follow `_config/shared/meeting-process.md` **Profile write-back**.

### Choose the scope (only when the entity index exists)

1. If the question is about one entity's operations, coverage, contracts, tax, or governance, that
   entity's slug is the scope even if related entities are mentioned. List related entities in the
   brief's `Scope:` line.
2. If a living trust is the primary subject (funding, trustees, instruments), use `trust`.
3. If the work is household, personal, or a true cross-entity calendar or portfolio action, use
   `personal`. Ranking existing action registers is conversation, not a meeting, unless the user
   asks to save that ranking.

### Existing records stay put

If a later session creates `entities/index.md` after meetings already sit at
`meetings/<YYYY-MM-DD-HHMM>-<topic-slug>/` (or an older unstamped `meetings/<topic-slug>/`),
leave those folders where they are. Do not move them into
`meetings/<scope>/<YYYY-MM-DD-HHMM>-<topic-slug>/`. New meetings after the index exists use
the scoped layout. The private index may list both layouts; the `Folder:` path is the
meeting's identity.

Resume an existing record at its current path — stamped or unstamped. Do not relocate it to
repair layout, to match a new entity index, to add a stamp, or because the topic is touched
again. Do not create a new stamped folder for work that is still that record. Leaving it in
place keeps inbound profile provenance links and outbound relative links valid.

A matching topic slug is not the same meeting. `meetings/2026-09-06-1430-property-review/` and
`meetings/personal/2026-09-06-1430-property-review/` are distinct records, as are an unstamped
`meetings/property-review/` and a later stamped folder with the same slug. Never merge them,
overwrite one with the other, or nest a flat folder under a scope because the names match.

Before creating `meetings/<scope>/<YYYY-MM-DD-HHMM>-<topic-slug>/`, check occupancy at two
levels:

1. If `meetings/<scope>/` itself contains `brief.md` or `minutes.md`, it is a meeting record, not
   a scope folder. Do not write a child topic into it. Resume that record only when it is the
   same work. For other new work in that logical scope, create
   `meetings/<scope>-<YYYY-MM-DD-HHMM>-<topic-slug>/` and set the index `Scope:` field to the
   logical scope (`personal`, `trust`, or the entity slug). Do not nest.
2. If `meetings/<scope>/<YYYY-MM-DD-HHMM>-<topic-slug>/` already exists, resume that record only
   when it is the same work; otherwise append `-2` (then `-3`, …) to the topic slug. A later
   meeting on the same topic is a new stamped folder, not a rename of the earlier one.

Never move or create a meeting onto a shipped `example-*` path. Never add a date-time prefix
to a shipped `example-*` folder.

## Private Index

`index.md` is local-only routing metadata, not authoritative meeting history. If it does not exist,
continue with the scoped fallback below. Never add shipped `example-*` meetings to this private
index.

Each substantive user meeting has exactly one entry, keyed by its folder path from `meetings/`:

```markdown
### <Meeting title>
- Folder: `<YYYY-MM-DD-HHMM>-<topic-slug>/` or `<scope>/<YYYY-MM-DD-HHMM>-<topic-slug>/` (older unstamped paths stay as stored)
- Date: `YYYY-MM-DD`
- Status: `active` | `completed` | `paused`
- Scope: `personal` | `trust` | one or more entity slugs | `none` (flat layout)
- Purpose: <one sentence>
- Advisors: <advisor names or numbers>
- Tags: <search tags, or `none`>
- Brief: [`brief.md`](<path>/brief.md)
- Minutes: [`minutes.md`](<path>/minutes.md) | `pending`
```

## Find a Prior Meeting

1. Read `index.md` if it exists.
2. Select one relevant entry by title, scope folder, purpose, advisors, tags, date, or status.
3. Load that meeting's `brief.md` first.
4. Load `minutes.md` only for decisions, recommendations, status, profile updates, or next steps.
5. Load individual artifacts only when the current question requires them.
6. Do not preload transcripts, complete artifact directories, or all meeting records.

## Scoped Fallback and Repair

When the index is missing, has no useful match, or points to a missing file:

1. Search both layouts: existing `meetings/<YYYY-MM-DD-HHMM>-<topic-slug>/` folders (and older
   unstamped `meetings/<topic-slug>/` folders) and, when present,
   `meetings/<scope>/<YYYY-MM-DD-HHMM>-<topic-slug>/` folders (and older unstamped scoped
   folders). Do not treat a matching topic slug as one meeting.
2. If needed, search only `brief.md` and `minutes.md` files for relevant terms.
3. Do not search transcripts or bulk-load artifacts by default.
4. Trust meeting record files over conflicting index metadata.
5. Create or repair the single entry keyed by folder path after locating a substantive user meeting.
6. Consolidate duplicate entries for the same folder path.

## Maintain the Index

Create or update the entry when the meeting folder is created under the existing lazy-creation rule:
when the question is clear enough for `brief.md`, the first artifact is produced, or the user asks to
save, whichever comes first. Use `pending` for minutes until `minutes.md` exists. Update the same
entry when minutes are created, material routing metadata changes, or status changes. Do not create
empty minutes solely for the index.

`agenda.md`, if present, tracks deferred questions and possible future work. `index.md` catalogs
meetings with actual records.

## Shipped Fictional Examples

- `example-emergency-fund/` — simple single-advisor meeting; start with its `brief.md`.
- `example-rental-property/` — multi-advisor meeting with artifacts; start with its `brief.md`, then
  use `minutes.md` to select an artifact.
