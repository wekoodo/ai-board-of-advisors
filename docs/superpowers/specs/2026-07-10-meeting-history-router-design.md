# Meeting History Router Design

## Goal

Add a compact, private meeting-history index so an agent can locate one prior meeting and load only
the files needed for the current question, without scanning or preloading the complete meeting tree.

## Architecture

The `meetings/` Layer-4 working area gains a tracked recursive router at `meetings/CONTEXT.md` and a
local-only catalog at `meetings/index.md`. The router is stable product guidance that ships with the
template. The index is private, evolving routing metadata and is explicitly ignored by Git.

The index is a cache, not the source of truth. Each meeting's `brief.md`, `minutes.md`, and artifacts
remain authoritative. If an entry is absent or stale, the chair performs a scoped filename/text
search, selects the relevant meeting, and repairs or creates that meeting's single index entry.

## Routing Flow

When prior meeting context may matter, the chair:

1. Reads `meetings/CONTEXT.md`.
2. Reads the compact local `meetings/index.md` if it exists.
3. Selects one relevant meeting.
4. Loads that meeting's `brief.md` first.
5. Loads `minutes.md` only when decisions, recommendations, status, or next steps are needed.
6. Loads individual artifacts only when the current question requires them.
7. Does not preload transcripts, complete artifact directories, or all meeting records.
8. Falls back to a scoped search only when the index has no useful match, then repairs the index.

Shipped fictional examples remain discoverable in a separate tracked section of
`meetings/CONTEXT.md`. They are never copied into the user's private index automatically.

## Index Contract

`meetings/index.md` contains exactly one compact entry per substantive user meeting. Each entry has:

- Meeting title
- Folder path
- Date
- Status: `active`, `completed`, or `paused`
- One-sentence purpose
- Relevant advisors
- Search tags and any related agenda IDs
- A link to `brief.md`
- A link to `minutes.md`, or the literal value `pending` until that file exists

The chair identifies an existing entry by its folder path and updates it in place. Continuing a
meeting must not append a duplicate entry.

## Lifecycle

The index uses the existing meeting-record threshold rather than introducing a new definition of
"substantive." The chair creates or updates the entry when the meeting folder is created lazily:
when the question is clear enough to write `brief.md`, when the first artifact is produced, or when
the user asks to save, whichever comes first.

At initial creation, `minutes.md` may not exist; its index field is `pending`. As the meeting
progresses, the chair updates the same entry when minutes are created, material routing metadata
changes, or the status changes. The meeting files always override conflicting index metadata.

`meetings/agenda.md` remains separate if present: it tracks deferred questions and possible future
work, while `meetings/index.md` catalogs meetings that have actual records.

## Files

- Create `meetings/CONTEXT.md`: routing flow, index schema, examples, fallback and repair behavior.
- Modify `.gitignore`: explicitly ignore `/meetings/index.md` while preserving the tracked router
  and shipped example directories.
- Modify `CONTEXT.md`: route prior-meeting lookup through `meetings/CONTEXT.md` and require index
  maintenance at the existing record-creation threshold.
- Modify `_config/shared/meeting-process.md`: define lifecycle updates, pending minutes, in-place
  deduplication, and the authority boundary.
- Modify `_config/shared/icm-conventions.md` only as needed to record the recursive Layer-4 router
  and private index classification.

No sample private `meetings/index.md` will be committed. Existing meeting folders require no
migration; indexing them is optional and can happen when they are next used.

## Error Handling

- Missing index: continue with a scoped search and create the index only when a substantive user
  meeting is found or created.
- No useful match: search meeting folder names, then `brief.md` and `minutes.md`; do not search
  transcripts or bulk-load artifacts by default.
- Stale entry or broken link: trust the meeting files, correct the existing entry, and continue.
- Duplicate entries: consolidate them by folder path into one current entry.
- Missing minutes: retain `pending`; do not create empty minutes solely to satisfy the index.

## Verification

1. Run the repository ICM audit against the project root.
2. Run `git diff --check`.
3. Confirm `meetings/index.md` is ignored with `git check-ignore -v meetings/index.md`.
4. Confirm `meetings/CONTEXT.md` is not ignored.
5. Search the changed contracts for consistent lifecycle, `pending`, authority, example-separation,
   and scoped-fallback language.
6. Confirm no private index file or meeting data was added to Git.

## Acceptance Criteria

- A fresh installation contains generic tracked routing instructions and no private meeting entries.
- Starting a substantive meeting creates or updates exactly one local index entry keyed by folder
  path.
- An agent can locate a prior meeting through the index and load only its selected record files.
- A missing or stale index degrades safely to scoped search and repair.
- Agenda items, recorded meeting history, and shipped fictional examples retain distinct purposes.
- Topic-only meeting folder names and all existing meeting records remain compatible.
- The implementation remains pure Markdown and harness-agnostic.
