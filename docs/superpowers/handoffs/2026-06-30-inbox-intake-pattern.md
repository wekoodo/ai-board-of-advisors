# Handoff: `_inbox/` Intake Pattern for Pre-Meeting Documents

**Date:** 2026-06-30  
**Branch:** main  
**For:** Fresh agent session to implement

---

## Context

The Board of Advisors system currently has no designated place for user-provided input documents (entity structures, spreadsheets, contracts, etc.) that need to be available *before* or *during* a meeting. Meeting folders don't exist until a meeting starts, and chat attachments are in-context only — nothing is persisted to disk automatically.

---

## What to Build

Add a **`_inbox/` folder** at the repo root as a persistent, tracked drop zone for input documents. This is a small, targeted addition — one new folder plus updates to two existing files.

### The Convention

- Users (and collaborators on a shared repo) drop documents into `_inbox/` at any time, between sessions.
- When a meeting kicks off, the model checks `_inbox/`, moves any relevant files into the new meeting's `inputs/` subfolder (creating `meetings/<meeting-name>/inputs/` as part of that step), and leaves unrelated files in `_inbox/` for future meetings.
- `_inbox/` is tracked in git so both partners in a shared repo can add documents and see each other's additions.
- Empty `_inbox/` gets a `.gitkeep` so the folder is committed even when nothing is waiting.

---

## Files to Create or Edit

### 1. Create `_inbox/.gitkeep`
Empty file. Ensures the folder is tracked when no documents are present.

### 2. Edit `_config/shared/meeting-process.md`
Add a step to the meeting-start sequence directing the model to:
1. List files in `_inbox/` and surface them to the user.
2. Ask which (if any) are relevant to this meeting.
3. Move confirmed files to `meetings/<meeting-name>/inputs/` (creating the `inputs/` directory in the process).
4. Leave unselected files in `_inbox/` for future meetings.

The exact placement: insert as a new step between "load the brief" and "convene advisors" in whatever sequencing the file currently describes.

### 3. Edit `_config/CONTEXT.md`
Add a single reference line noting that `_inbox/` is the intake point for pre-meeting documents, so the routing layer is aware of it. This is a one-liner — the detail lives in `meeting-process.md`.

---

## What NOT to Change

- Do not touch any advisor `CONTEXT.md` files — intake is a meeting-process concern, not an advisor concern.
- Do not add `_inbox/` to `.gitignore` — it must be tracked and shared.
- Do not create an `inputs/` folder at the repo root — inputs are always meeting-scoped once assigned.

---

## Verification

After implementing, confirm:
- [ ] `_inbox/.gitkeep` exists and `git status` shows it tracked.
- [ ] `_config/shared/meeting-process.md` describes the inbox-check step clearly enough that a cold agent reading it would know to check `_inbox/` at meeting start.
- [ ] `_config/CONTEXT.md` mentions `_inbox/` as the document intake point.
- [ ] No other files were modified.
