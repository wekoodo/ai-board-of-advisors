# `_inbox/` Pre-Meeting Document Intake Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a persistent, local-only `_inbox/` drop zone for pre-meeting documents, and wire the chair to surface and assign those documents at meeting start.

**Architecture:** Pure-markdown ICM project — no code, no build, no test framework. The work is one new tracked file (`_inbox/README.md`), one `.gitignore` rule that keeps dropped documents local-only, and three instruction-file edits so the meeting chair checks the inbox at meeting start and moves relevant documents into `meetings/<meeting>/inputs/`. Each task's "test cycle" is a verification command (`git status`, `git check-ignore`, `grep`) rather than a unit test.

**Tech Stack:** Markdown, git. No runtime.

## Global Constraints

- This is an ICM project: every file answers exactly one question; the folder hierarchy is the architecture. Keep edits minimal and in the voice of the surrounding files.
- Dropped documents are sensitive personal/financial data and MUST stay local-only (gitignored) — only `_inbox/README.md` is tracked. This deliberately overrides the original handoff's "track everything" instruction.
- Documents are **moved** (not copied) into `meetings/<meeting>/inputs/` when assigned; the rest stay in `_inbox/`.
- Do NOT touch any advisor `CONTEXT.md` files. Do NOT create an `inputs/` folder at the repo root.
- Date inside any new content is 2026-06-30 where a date is needed; folder/record naming conventions are unchanged.

---

### Task 1: Create the inbox folder with its tracked README

**Files:**
- Create: `_inbox/README.md`

**Interfaces:**
- Consumes: nothing.
- Produces: the `_inbox/` folder (kept in git by `README.md`, which doubles as the keep-file — no `.gitkeep`).

- [ ] **Step 1: Write `_inbox/README.md`**

Create `_inbox/README.md` with exactly this content:

```markdown
# `_inbox/` — Pre-Meeting Document Intake

Drop documents here that the board should have on hand for a meeting — entity
structures, contracts, spreadsheets, statements, anything an advisor may need to
read. Add them any time, between sessions.

**These documents are local-only.** Everything in this folder except this README
is gitignored and never committed — the same privacy posture as your profile and
your meeting records. Only this `README.md` is tracked, so the folder always
exists on a fresh clone.

**What happens to them.** At the start of a meeting the board chair lists whatever
is waiting here, asks which files are relevant to that meeting, and **moves** the
ones you confirm into `meetings/<meeting>/inputs/`. Anything you don't pick stays
here for a future meeting.
```

- [ ] **Step 2: Verify the file exists**

Run: `git status --short _inbox/`
Expected: shows `?? _inbox/README.md` (untracked, not yet ignored — the ignore rule lands in Task 2).

- [ ] **Step 3: Commit**

```bash
git add _inbox/README.md
git commit -m "feat: add _inbox/ drop zone with intake README"
```

---

### Task 2: Make dropped documents local-only in `.gitignore`

**Files:**
- Modify: `.gitignore`

**Interfaces:**
- Consumes: `_inbox/README.md` from Task 1 (the negation rule must keep it tracked).
- Produces: a gitignore state where any file dropped in `_inbox/` is ignored except `README.md`.

- [ ] **Step 1: Add the inbox rule**

In `.gitignore`, immediately after the existing meetings block (the lines ending with `!meetings/example-*/`, currently at lines 8–10), insert a blank line then:

```
# Pre-meeting document intake — folder + README tracked, dropped docs local-only
_inbox/*
!_inbox/README.md
```

- [ ] **Step 2: Verify a dropped document is ignored but README is not**

Run:
```bash
printf 'test\n' > _inbox/_probe.txt && git check-ignore _inbox/_probe.txt _inbox/README.md; rm _inbox/_probe.txt
```
Expected: prints `_inbox/_probe.txt` only (README is NOT listed, i.e. it stays tracked). `git check-ignore` exits 0 because at least one path matched.

- [ ] **Step 3: Confirm README is still tracked and clean**

Run: `git status --short _inbox/`
Expected: no output for `_inbox/README.md` (already committed in Task 1, the probe file was removed).

- [ ] **Step 4: Commit**

```bash
git add .gitignore
git commit -m "chore: keep _inbox/ documents local-only, track only the README"
```

---

### Task 3: Wire the inbox check into the chair's meeting loop (root `CONTEXT.md`)

**Files:**
- Modify: `CONTEXT.md` (the "Hosting a Meeting" numbered loop)

**Interfaces:**
- Consumes: the `_inbox/` convention from Tasks 1–2.
- Produces: a meeting-start instruction the chair reads on every meeting — referenced by `meeting-process.md` (Task 4) and the directory map (Task 5).

- [ ] **Step 1: Insert the inbox-check step**

In `CONTEXT.md`, inside the "Hosting a Meeting" list, the current step `1.` reads:

```
1. **Read** the user's message.
```

Insert a new step immediately before it and leave the rest of the list as prose-numbered (the existing items already read 1–8; add the inbox step as a new first item and renumber is NOT required because the list uses explicit numbers — instead insert it as an un-numbered lead-in line). Replace:

```
1. **Read** the user's message.
```

with:

```
1. **Check `_inbox/`** at the start of a meeting — list any documents waiting there,
   surface them to the user, and ask which are relevant to this meeting. **Move** the
   confirmed files into `meetings/<meeting>/inputs/` (creating that directory), and
   leave the rest in `_inbox/` for future meetings. `_inbox/` documents are local-only.
2. **Read** the user's message.
```

Then renumber the remaining steps in that list so they run 3–9 (the old `2.`–`8.` each increase by one). Specifically:
- `2. **Convene**` → `3. **Convene**`
- `3. **Let them respond in character**` → `4. **Let them respond in character**`
- `4. **Synthesize**` → `5. **Synthesize**`
- `5. **Produce an artifact**` → `6. **Produce an artifact**`
- `6. **Let the user review** ...` → `7. **Let the user review** ...`
- `7. **Continue** turn by turn.` → `8. **Continue** turn by turn.`
- `8. **Capture the record.**` → `9. **Capture the record.**`

- [ ] **Step 2: Verify the step is present and the list is sequential**

Run: `grep -nE "Check \`_inbox/\`|^[0-9]\. \*\*" CONTEXT.md`
Expected: the inbox-check line appears as item `1.`, and the printed step numbers run `1.`–`9.` with no duplicates or gaps in the "Hosting a Meeting" list.

- [ ] **Step 3: Commit**

```bash
git add CONTEXT.md
git commit -m "feat: chair checks _inbox/ at meeting start"
```

---

### Task 4: Add the full inbox step and `inputs/` record entry to `meeting-process.md`

**Files:**
- Modify: `_config/shared/meeting-process.md`

**Interfaces:**
- Consumes: the meeting-loop step from Task 3 (this is its full-protocol expansion).
- Produces: the authoritative description of the inbox check and the `inputs/` subfolder in the meeting record.

- [ ] **Step 1: Add the inbox step to "The Meeting Loop"**

In `_config/shared/meeting-process.md`, the section "## The Meeting Loop" opens with:

```
A meeting unfolds turn by turn. Each cycle:

1. **The user asks** — a question, a topic, a decision they're weighing, a problem they want a fresh
   look at.
```

Insert a meeting-start paragraph between the "Each cycle:" line and step `1.`:

```
At the **start of the meeting**, before the first cycle, the chair checks the `_inbox/` drop zone:
list any documents waiting there, surface them to the user, and ask which are relevant to this
meeting. **Move** the confirmed files into `meetings/<meeting>/inputs/` (creating that directory),
and leave the rest in `_inbox/` for future meetings. `_inbox/` documents are local-only (gitignored);
they become part of the meeting record once assigned. If `_inbox/` is empty, skip silently.

A meeting unfolds turn by turn. Each cycle:
```

(Keep the existing "A meeting unfolds turn by turn. Each cycle:" line that follows — the insertion goes above it, so that line now appears once, right before step `1.`. Remove the now-duplicate original occurrence.)

- [ ] **Step 2: Add `inputs/` to "The Meeting Record" file list**

In the "## The Meeting Record" section, the bullet list currently ends with the `transcript.md` bullet:

```
- **`transcript.md`** — the full, turn-by-turn conversation. Written **only when the user asks to
  keep it** ("save the full transcript" / "keep the record"). It exists for digging deeper into how a
  conclusion or an artifact came about — not as the default record.
```

Insert a new bullet immediately before the `transcript.md` bullet:

```
- **`inputs/`** — present whenever the user supplied pre-meeting documents. Holds the source files
  moved from `_inbox/` when the meeting started (contracts, statements, spreadsheets). Local-only,
  like the rest of a real meeting record.
```

- [ ] **Step 3: Verify both edits and check for an accidental duplicate line**

Run: `grep -nc "A meeting unfolds turn by turn. Each cycle:" _config/shared/meeting-process.md`
Expected: `1` (exactly one occurrence — confirms the duplicate from Step 1 was removed).

Run: `grep -nE "_inbox/|\*\*\`inputs/\`\*\*" _config/shared/meeting-process.md`
Expected: shows the new meeting-start paragraph mentioning `_inbox/` and the new `inputs/` bullet.

- [ ] **Step 4: Commit**

```bash
git add _config/shared/meeting-process.md
git commit -m "docs: full _inbox/ intake step and inputs/ record entry in meeting-process"
```

---

### Task 5: Add the `_inbox/` directory-map entry to `_config/CONTEXT.md`

**Files:**
- Modify: `_config/CONTEXT.md`

**Interfaces:**
- Consumes: the convention defined in Tasks 1–4.
- Produces: the routing-layer pointer so the directory map is aware of `_inbox/`.

- [ ] **Step 1: Add a note under the directory's intro**

`_config/CONTEXT.md` describes `_config/` itself; `_inbox/` is a sibling at the repo root, so it does not belong in the `_config/` contents table. Add a one-line pointer instead. After the contents table (after the table's last row, before the "## When to Load" heading), insert:

```

> **Related — repo root:** `_inbox/` is the intake point for pre-meeting documents. The chair checks
> it at meeting start and moves relevant files into `meetings/<meeting>/inputs/`; full detail is in
> `shared/meeting-process.md`.
```

- [ ] **Step 2: Verify the pointer is present**

Run: `grep -n "_inbox/" _config/CONTEXT.md`
Expected: one line referencing `_inbox/` as the intake point for pre-meeting documents.

- [ ] **Step 3: Commit**

```bash
git add _config/CONTEXT.md
git commit -m "docs: note _inbox/ intake point in _config directory map"
```

---

### Task 6: Final verification against the spec

**Files:** none (verification only).

- [ ] **Step 1: Run the full spec checklist**

```bash
git status --short _inbox/README.md
git check-ignore _inbox/README.md; echo "exit=$?"
grep -n "_inbox/" CONTEXT.md _config/shared/meeting-process.md _config/CONTEXT.md
git diff --name-only HEAD~5
```

Expected:
- `_inbox/README.md` is tracked (no `??`, and `git check-ignore` prints nothing with `exit=1`).
- All three instruction files reference `_inbox/`.
- The changed-files list is exactly: `_inbox/README.md`, `.gitignore`, `CONTEXT.md`, `_config/shared/meeting-process.md`, `_config/CONTEXT.md` — and **no advisor `CONTEXT.md`** and **no root `inputs/` folder**.

- [ ] **Step 2: Confirm no out-of-scope files changed**

Run: `git diff --name-only HEAD~5 | grep -E "advisors|advisors-extended" || echo "clean"`
Expected: `clean`.
