# Meeting History Router

## Purpose

Use this router when prior meeting context may matter. Locate one relevant meeting first, then load
only the record files needed for the current question.

## Private Index

`index.md` is local-only routing metadata, not authoritative meeting history. If it does not exist,
continue with the scoped fallback below. Never add shipped `example-*` meetings to this private
index.

Each substantive user meeting has exactly one entry, keyed by its folder path:

```markdown
### <Meeting title>
- Folder: `<topic-slug>/`
- Date: `YYYY-MM-DD`
- Status: `active` | `completed` | `paused`
- Purpose: <one sentence>
- Advisors: <advisor names or numbers>
- Tags: <search tags and any related agenda IDs, or `none`>
- Brief: [`brief.md`](<topic-slug>/brief.md)
- Minutes: [`minutes.md`](<topic-slug>/minutes.md) | `pending`
```

## Find a Prior Meeting

1. Read `index.md` if it exists.
2. Select one relevant entry by title, purpose, advisors, tags, agenda ID, date, or status.
3. Load that meeting's `brief.md` first.
4. Load `minutes.md` only for decisions, recommendations, status, or next steps.
5. Load individual artifacts only when the current question requires them.
6. Do not preload transcripts, complete artifact directories, or all meeting records.

## Scoped Fallback and Repair

When the index is missing, has no useful match, or points to a missing file:

1. Search topic folder names.
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
