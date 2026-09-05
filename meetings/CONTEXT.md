# Meeting History Router

## Purpose

Use this router when prior meeting context may matter, or when creating a new meeting folder.
Locate one relevant meeting first, then load only the record files needed for the current question.

## Folder layout

Meeting records use a **topic-only** folder name. The date lives inside `brief.md` and
`minutes.md`, not in the folder name.

**No entity index** (`_config/profile/entities/index.md` is absent):

```text
meetings/<topic-slug>/
```

**Entity index exists:**

```text
meetings/<scope>/<topic-slug>/
```

| Scope folder | Use when |
| --- | --- |
| `personal` | Household or personal work, or portfolio-wide / multi-entity work with no single primary entity |
| `trust` | A living trust (or similar estate vehicle in `_config/profile/trust.md`) is the primary subject |
| `<entity-slug>` | One registered entity is the primary subject. Use the slug from `_config/profile/entities/index.md` |

Do not pre-create empty scope folders. Create `meetings/<scope>/` lazily with the first meeting in
that scope. Never invent a new scope slug. Reserved non-entity scopes are only `personal` and
`trust`. Use `trust` only when `trust.md` exists.

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

If a later session creates `entities/index.md` after some meetings already sit at
`meetings/<topic-slug>/`, leave those folders until that meeting is next touched, then move the
record to `meetings/personal/<topic-slug>/` (or the matching entity/trust scope) and update the
index entry. Do not leave a second copy at the old path.

## Private Index

`index.md` is local-only routing metadata, not authoritative meeting history. If it does not exist,
continue with the scoped fallback below. Never add shipped `example-*` meetings to this private
index.

Each substantive user meeting has exactly one entry, keyed by its folder path from `meetings/`:

```markdown
### <Meeting title>
- Folder: `<topic-slug>/` or `<scope>/<topic-slug>/`
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

1. Search scope-folder names (when present), then topic folder names.
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
