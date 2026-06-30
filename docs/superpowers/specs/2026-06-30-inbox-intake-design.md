# Design: `_inbox/` Pre-Meeting Document Intake

**Date:** 2026-06-30
**Branch:** main
**Source:** refines `docs/superpowers/handoffs/2026-06-30-inbox-intake-pattern.md` after a brainstorming pass

---

## Purpose

The Board of Advisors system has no designated place for user-provided input documents
(entity structures, spreadsheets, contracts) that need to be available *before* or *during* a
meeting. Meeting folders don't exist until a meeting starts, and chat attachments are in-context
only — nothing is persisted to disk.

This adds a persistent **`_inbox/`** drop zone at the repo root. Users drop documents in between
sessions; when a meeting starts, the chair surfaces them, asks which are relevant, and moves the
confirmed ones into the meeting.

## Privacy Model (revised from the handoff)

The handoff specified that `_inbox/` be tracked and shared in git. Brainstorming surfaced that this
contradicts the rest of the system's privacy posture: `_config/profile/*` and all real meetings
(`meetings/*/`) are deliberately gitignored as sensitive personal/financial data. Dropped documents
(contracts, entity structures, financial spreadsheets) are at least as sensitive. The handoff's own
design is also internally inconsistent — documents move into `meetings/<meeting>/inputs/`, which is
already gitignored, so they leave tracking the moment a meeting starts anyway.

**Decision:** dropped documents are **local-only**. Only the folder's `README.md` is tracked so the
folder is always committed; everything else dropped in is gitignored. This matches the profile and
meetings posture and is consistent with where the documents end up.

## Files to Create or Edit

### 1. Create `_inbox/README.md` (tracked)

Short human-facing note covering:
- What the folder is for (drop pre-meeting documents here).
- That dropped documents are **local-only** (gitignored) — only this README is committed.
- That at meeting start the chair surfaces these files and, on confirmation, moves the relevant ones
  into `meetings/<meeting>/inputs/`.

This file doubles as the keep-file, so **no separate `.gitkeep`** is created.

### 2. Edit `.gitignore`

Add, near the existing profile/meetings privacy block:

```
# Pre-meeting document intake — folder + README tracked, dropped docs local-only
_inbox/*
!_inbox/README.md
```

### 3. Edit root `CONTEXT.md`

The chair's meeting loop under "Hosting a Meeting" is where a meeting actually starts — this is where
the inbox check must live to reliably fire (not only in `_config/CONTEXT.md`, which is a directory
map). Add an inbox-check step: at meeting start, list any files in `_inbox/`, surface them to the
user, ask which are relevant to this meeting, then **move** confirmed files into
`meetings/<meeting>/inputs/` (creating that directory), leaving the rest in `_inbox/` for future
meetings.

### 4. Edit `_config/shared/meeting-process.md`

Add the full version of the same inbox-check step to the meeting-start sequence, and note `inputs/`
as a meeting-record subfolder alongside `brief.md` / `minutes.md` / `artifacts/` / `transcript.md`
(holds the input documents assigned to the meeting).

### 5. Edit `_config/CONTEXT.md`

Add a one-line directory-map entry noting `_inbox/` is the intake point for pre-meeting documents;
detail lives in `meeting-process.md`.

## Behavior

- **Move, not copy.** Assigning a document relocates it to `meetings/<meeting>/inputs/` and removes it
  from `_inbox/`. Keeps the inbox a clean drop zone; each document lives with the meeting it belongs
  to. Both locations are gitignored, so nothing is lost from tracking either way.
- **Lazy, like the rest of the record.** The `inputs/` directory is created only when a document is
  actually assigned to a meeting — consistent with how meeting folders are created lazily.

## Deliberate Deviations from the Handoff

1. **Contents gitignored, not tracked** — for privacy consistency with profile/meetings.
2. **Wired into root `CONTEXT.md`, not only `_config/CONTEXT.md`** — so the check actually fires at
   meeting start.
3. **`README.md` instead of `.gitkeep`** — keeps the folder committed and documents the convention to
   a human in the same file.

## What NOT to Change

- Do not touch any advisor `CONTEXT.md` files — intake is a meeting-process concern, not an advisor
  concern.
- Do not create an `inputs/` folder at the repo root — inputs are always meeting-scoped once assigned.

## Verification

- [ ] `_inbox/README.md` exists and `git status` shows it tracked.
- [ ] `.gitignore` ignores `_inbox/*` except `README.md`; a test file dropped in `_inbox/` shows as
      ignored.
- [ ] Root `CONTEXT.md` "Hosting a Meeting" loop includes the inbox-check step.
- [ ] `_config/shared/meeting-process.md` describes the inbox-check step and lists `inputs/` as a
      meeting-record subfolder.
- [ ] `_config/CONTEXT.md` mentions `_inbox/` as the document intake point.
