# Meeting-Mode Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
>
> **This is a pure-markdown product — there is no code, no build, and no automated test suite.** Wherever a code plan would say "write the failing test / run it," this plan substitutes an explicit **Verify** step: a concrete check (grep for stale references, path resolution, content presence, gitignore behavior) the implementer performs and confirms before committing. Treat Verify steps as the test cycle.
>
> **Post-build refinement (commit `ee0e35d`).** After the initial build, the meeting **record shape** was refined for ICM clarity, and this plan is updated to match. A meeting now leaves small, routed files: **`brief.md`** (question + context + date) and **`minutes.md`** (decisions, each artifact and how to use it, next steps) as the standard record, **`artifacts/`** for deliverables, and **`transcript.md`** only on request (for digging deeper). Meeting folders are **topic-only** (the date lives inside the files), and `.gitignore` uses `meetings/*/` + `!meetings/example-*/`. Where earlier drafts referenced transcript-on-save, date-stamped folders, or `example-2026-*` names, the form below is authoritative.

**Goal:** Convert the Board of Advisors from a staged file-pipeline ("copy a template, run Round 1→2→3, read the output files") into a **conversational live meeting** where the board chair hosts, routes each message to the relevant advisor(s), and artifacts are living files the user co-edits mid-meeting — absorbing the staged pipeline entirely.

**Architecture:** The root `CONTEXT.md` becomes the meeting **host**. A new `_config/shared/meeting-process.md` defines the conversational loop and how convening degrades by harness capability (isolated sub-agent where supported; inline role-play otherwise — both file-based). Each meeting leaves a small routed record under `meetings/<topic-slug>/` — a `brief.md` + `minutes.md` (+ `artifacts/`), with `transcript.md` only on request. The `sessions/` tree is renamed `meetings/`, the staged `_template/` and per-advisor `output/` folders are retired, and the two examples are regenerated as meeting records.

**Tech Stack:** Plain Markdown. No code, no build tools, no runtime dependencies. `git` and a PowerShell runner are tooling, not product. Targets agentic harnesses that read project files (Claude Code, Codex, OpenCode, Hermes, …) — **not** plain web chat.

**Source-of-truth spec:** `docs/superpowers/specs/2026-06-22-meeting-mode-design.md`.

## Global Constraints

These apply to **every** iteration. Each task's requirements implicitly include this section.

- **Pure markdown.** No runtime code, APIs, or dependencies in the product. The PowerShell runner and `git` are tooling only.
- **Target = agentic harnesses only.** No web-chat / canvas / Project-Gem-GPT anything. A filesystem is always assumed; artifacts are always real files.
- **One artifact home.** All meeting artifacts live under `meetings/<meeting>/artifacts/`. The per-advisor `output/` folders are retired.
- **Routed record.** A substantive meeting leaves small, single-purpose files — `brief.md` (question + context + date) and `minutes.md` (decisions, each artifact and how to use it, next steps) as the standard record, plus any `artifacts/`. The full `transcript.md` is written only on request. Folders are topic-only (the date lives inside the files).
- **Chair routing.** The host convenes only the advisor(s) a message touches — one or several — not the whole board by default.
- **Convening degrades gracefully.** Sub-agent per advisor where the harness supports it (preferred); inline role-play otherwise. Both write artifact files and produce identical records.
- **Relative paths only.** Core advisors (`advisors/NN-name/`) and extended advisors (`advisors-extended/NN-name/`) sit at **equal depth**, so both use `../../_config/...` and `../../meetings/...`.
- **`AGENTS.md` is canonical.** `CLAUDE.md`/`GEMINI.md` carry zero duplicated content (native import + plain-text fallback line + platform notes).
- **Durable-figures rule** (from `conventions.md`): any concrete year-specific figure is labeled **"illustrative — verify current-year value."** Never present a stale dollar amount as current fact. Regenerated example artifacts must comply.
- **Examples are 100% fictional** — invented persona, company, and figures; never seeded from the user's real life. (See memory: keep-generated-examples-fictional.)
- **No stale references.** After this plan, no shipped file (everything **except** `docs/superpowers/**` and `tmp/**`, which are historical/build scaffolding) may reference `sessions/`, `board-process`, `output/` as an artifact home, or the staged stage names `01-initial-meeting` / `02-artifacts` / `03-reconvene`.
- **No placeholder text** ("TBD", "TODO", "[fill in]") in any shipped file **except** the intentional bracket placeholders in `advisors/_template/`.

---

## File Map

What this plan touches, by iteration. (R)=rename, (M)=modify, (D)=delete, (C)=create.

```
board-of-advisors/
├── .gitignore                                   (M) Iter 01 (glob), Iter 06 (drop output rules)
├── AGENTS.md                                    (M) Iter 05
├── CONTEXT.md                                   (M) Iter 03   ← becomes meeting host
├── CLAUDE.md / GEMINI.md                        (M) Iter 05   ← wording only (note section)
├── README.md                                    (M) Iter 05 (narrative) + Iter 07 (examples)
│
├── _config/
│   ├── CONTEXT.md                               (M) Iter 01   ← sessions→meetings refs
│   ├── profile/CONTEXT.md                       (M) Iter 01   ← if it references sessions
│   └── shared/
│       ├── board-process.md → meeting-process.md (R) Iter 01, (M) Iter 02  ← rewritten
│       ├── collaboration.md                     (M) Iter 01   ← if it references sessions
│       └── conventions.md                       (M) Iter 04   ← Handoff repositioned
│
├── advisors/
│   ├── _template/CONTEXT.md                      (M) Iter 04   ← Inputs rewritten
│   ├── 01..08/CONTEXT.md                         (M) Iter 04   ← Inputs rewritten (×8)
│   └── **/output/                                (D) Iter 06
│
├── advisors-extended/
│   ├── 09..10/CONTEXT.md                         (M) Iter 04   ← Inputs rewritten (×2)
│   └── **/output/                                (D) Iter 06
│
└── sessions/ → meetings/                         (R) Iter 01
    ├── _template/                                (D) Iter 06   ← staged template retired
    ├── example-emergency-fund/                   (M) Iter 07   ← regenerated as brief + minutes
    └── example-rental-property/                  (M) Iter 07   ← brief + minutes + artifacts + transcript
```

**Iteration 08** creates no new files — it is the integration review.

**Build scaffolding (gitignored, local-only):** `tmp/meeting-mode/kickoff-iteration-01..08.md` and `tmp/meeting-mode/run-iterations.ps1` drive the build, mirroring the original `tmp/kickoff-iteration-NN.md` + `run-iterations.ps1` pattern.

---

## Iteration 01: Rename & Reference Sweep

Purely mechanical: rename the folder and the process file, repoint every reference. No semantic content changes yet.

**Files:**
- Rename: `sessions/` → `meetings/`
- Rename: `_config/shared/board-process.md` → `_config/shared/meeting-process.md`
- Modify: every shipped file that references `sessions/` or `board-process` — at minimum `CONTEXT.md` (root), `AGENTS.md`, `README.md`, `_config/CONTEXT.md`, `_config/shared/collaboration.md`, `_config/profile/CONTEXT.md`, all advisor `CONTEXT.md` (10 + `_template`), and `.gitignore`.

**Interfaces:**
- Produces: a repo where every path reference points at `meetings/` and `meeting-process.md`. Later iterations rewrite the *content* of those files.

- [ ] **Step 1: Rename the folder and process file (preserve history)**

  ```bash
  git mv sessions meetings
  git mv _config/shared/board-process.md _config/shared/meeting-process.md
  ```

- [ ] **Step 2: Find every stale reference**

  Run (ripgrep), excluding historical/scaffolding dirs:
  ```bash
  rg -n --glob '!docs/superpowers/**' --glob '!tmp/**' -e 'sessions/' -e 'board-process' .
  ```
  This is the worklist for Step 3. Expect hits in the root `CONTEXT.md`, `AGENTS.md`, `README.md`, `_config/CONTEXT.md`, `collaboration.md`, `profile/CONTEXT.md`, and all advisor `CONTEXT.md` files.

- [ ] **Step 3: Repoint every hit**

  In each file from Step 2, replace `sessions/` → `meetings/` and `board-process.md` → `meeting-process.md` (and prose "board-process" → "meeting-process"). Advisor `CONTEXT.md` board-session input lines change e.g. `../../sessions/[session-name]/00-brief.md` → `../../meetings/[meeting-name]/...` (the semantics of those lines are rewritten in Iter 04; here only the path token changes). Do **not** touch `docs/superpowers/**` or `tmp/**`.

- [ ] **Step 4: Update `.gitignore` glob**

  Change the user-meetings ignore rule. Because meeting folders are topic-only (no date prefix to glob), use the example-prefix form:
  ```gitignore
  # User meetings — local-only (the shipped example-* meetings are NOT excluded)
  meetings/*/
  !meetings/example-*/
  ```
  (Leave the `advisors/**/output/*` rules for now — they're removed in Iter 06.)

- [ ] **Step 5: Verify**

  ```bash
  rg -n --glob '!docs/superpowers/**' --glob '!tmp/**' -e 'sessions/' -e 'board-process' .
  ```
  Expected: **no matches.** Also confirm `meetings/` exists, `_config/shared/meeting-process.md` exists, and `.gitignore` has `meetings/*/` + `!meetings/example-*/`.

- [ ] **Step 6: Commit**

  ```bash
  git add -A
  git commit -m "refactor: rename sessions/ -> meetings/ and board-process -> meeting-process (reference sweep)"
  ```

---

## Iteration 02: Write `meeting-process.md` (the protocol)

Replace the renamed file's content entirely with the conversational protocol.

**Files:**
- Modify (full rewrite): `_config/shared/meeting-process.md`

**Interfaces:**
- Consumes: nothing.
- Produces: the canonical description of the live-meeting loop that the root `CONTEXT.md` (Iter 03) and advisor Inputs (Iter 04) point to.

- [ ] **Step 1: Rewrite `_config/shared/meeting-process.md`**

  Required sections (write full prose, no placeholders):

  - **`# Meeting Process`** — one paragraph: a board meeting is a single continuous conversation hosted by the board chair; the user is a participant; harness-agnostic across any agent that reads files.
  - **`## The Meeting Loop`** — the turn cycle: (1) user asks; (2) chair routes — names which advisor(s) the topic touches and convenes them (one or several); (3) advisors respond in character; (4) chair adds a short synthesis when more than one weighed in; (5) when a document would help, an advisor produces an **artifact** as a real file under the meeting's `artifacts/`; (6) the user reads/edits the artifact or requests changes, the producing advisor revises it, others react; (7) the loop continues; (8) the user may say "save this meeting" to write a transcript. Note that "single-advisor consult" is just a meeting with one convened voice.
  - **`## Convening Modes`** — **Sub-agent (preferred, where the harness supports it):** the chair convenes each advisor as an isolated sub-agent, handing it only its load list (its `CONTEXT.md`, the profile, shared rules, and any existing meeting artifacts relevant to its domain); the advisor writes its artifact file and returns a `## Handoff` summary to the chair — keeping the host's context small across a long meeting. **Inline (fallback):** in a harness without sub-agents, the host role-plays the advisor in the shared context and still writes artifact files. Both are file-based and produce identical records. Note this supersedes the old "manual vs delegated" framing.
  - **`## Artifacts`** — living documents; always written under `meetings/<meeting>/artifacts/<name>.md`; follow `conventions.md` (durable-figures rule, response style); the user may edit them directly and the meeting reads the edits; revisions overwrite the same file.
  - **`## The Meeting Record`** — the chair creates `meetings/<topic-slug>/` lazily (topic-only name; the date lives inside the files). A substantive meeting leaves **`brief.md`** (question + context + date) and **`minutes.md`** (decisions, each artifact and how to use it, next steps) as the standard record, plus **`artifacts/`** when produced; **`transcript.md`** is written only on request, for digging deeper. `brief.md`/`minutes.md` are the chair's to write — not a template the user fills in.
  - **`## A Bigger Decision`** — for a major, multi-domain decision the chair can deliberately run a fuller arc inside the meeting: get every relevant advisor's initial take → commission a full artifact set → reconvene the advisors over the artifacts → deliver an integrated synthesis. Same thoroughness as a formal board process, conducted live with the user present.

- [ ] **Step 2: Verify**
  - `rg -n 'Round 1|Round 2|Round 3|01-initial-meeting|02-artifacts|03-reconvene' _config/shared/meeting-process.md` → **no matches** (no staged-pipeline language).
  - File contains the six sections above; "Convening Modes" describes both sub-agent and inline; "The Meeting Record" specifies `brief.md` + `minutes.md` (+ `artifacts/`) as the record and `transcript.md` as optional, with topic-only folders.
  - No placeholder text.

- [ ] **Step 3: Commit**
  ```bash
  git add _config/shared/meeting-process.md
  git commit -m "feat: meeting-process.md — conversational meeting protocol replaces staged pipeline"
  ```

---

## Iteration 03: Reframe Root `CONTEXT.md` (Meeting Host)

**Files:**
- Modify: `CONTEXT.md` (root)

**Interfaces:**
- Consumes: `meeting-process.md` (Iter 02), the advisor roster.
- Produces: the Layer 1 host every meeting begins from.

- [ ] **Step 1: Rewrite the routing portion of root `CONTEXT.md`**

  Keep **First Launch Check** (profile → onboarding) and **Advisor Roster** (core 01–08 + extended 09–10) unchanged. Replace the old `## Routing` + `## Session Stages` + the `### Execution` note with a single **`## Hosting a Meeting`** section:
  - You are the board chair and **meeting host**. Engaging the system starts a meeting; the user is a participant.
  - The loop (concise restatement of `meeting-process.md`): read the user's message → name and convene the relevant advisor(s) → let them respond in character → add a short synthesis if several weighed in → when a document helps, have an advisor produce an artifact under `meetings/<meeting>/artifacts/` → the user reviews/edits/requests changes → continue → capture the record (`brief.md` + `minutes.md` next to any `artifacts/`); write the full `transcript.md` only on request.
  - **Convening:** prefer one sub-agent per advisor where the harness supports it (keeps your context small); otherwise role-play the advisor inline. Either way, artifacts are real files.
  - **Single advisor:** simply convene one advisor — no separate mode.
  - Pointer: "Full protocol, convening modes, and the meeting-record shape are in `_config/shared/meeting-process.md`."

  Keep the **Profile** section (always load `_config/profile/` when present).

- [ ] **Step 2: Verify**
  - `rg -n 'Round|01-initial-meeting|02-artifacts|03-reconvene|copy .*_template|00-brief' CONTEXT.md` → **no matches.**
  - The file has First Launch Check, Advisor Roster (10 advisors), `## Hosting a Meeting` (with convening modes + the meeting record: brief + minutes + artifacts, transcript optional), and Profile.
  - Points to `_config/shared/meeting-process.md`. ~300–450 words. No placeholders.

- [ ] **Step 3: Commit**
  ```bash
  git add CONTEXT.md
  git commit -m "feat: root CONTEXT.md becomes the live-meeting host"
  ```

---

## Iteration 04: Advisor Inputs + Conventions Handoff

Make every advisor meeting-aware and reposition the Handoff block. The new Inputs block is **identical across all 11 advisor files** (10 advisors + template) — no slug-specific lines remain.

**Files:**
- Modify: `advisors/_template/CONTEXT.md`
- Modify: `advisors/01..08/CONTEXT.md` (8)
- Modify: `advisors-extended/09..10/CONTEXT.md` (2)
- Modify: `_config/shared/conventions.md`

**Interfaces:**
- Consumes: `meeting-process.md` (Iter 02).
- Produces: advisors that load correctly when convened in a meeting; a Handoff block scoped to the sub-agent→chair return.

- [ ] **Step 1: Replace the `## Inputs` section in every advisor `CONTEXT.md`**

  Old Inputs had `### Load if standalone session` (output/), `### Load if board session — Round 1`, and `### Load if board session — Round 3` lists. Replace the entire `## Inputs` body with this exact block (identical for all 11 files):

  ```markdown
  ## Inputs

  ### Always load
  - `../../_config/shared/disclaimer.md`
  - `../../_config/shared/collaboration.md`
  - `../../_config/shared/conventions.md`
  - `../../_config/profile/` (all files, if profile exists)

  ### Load when convened in a meeting
  - The chair's question or topic for you this turn.
  - `../../meetings/[meeting-name]/artifacts/` — any existing meeting artifacts relevant to your domain, if the meeting has produced any.

  ### Load as needed
  - `references/` (see `references/CONTEXT.md` for navigation)
  ```

  For `advisors/_template/CONTEXT.md`, the same block, keeping the file's intentional bracket-placeholder style elsewhere intact.

- [ ] **Step 2: Reposition the Handoff block in `_config/shared/conventions.md`**

  Keep the exact Handoff format (the five bullets). Change only the surrounding framing: from "Every advisor response ends with this block" to:
  > **When an advisor is convened as a sub-agent, it returns this block to the chair** as the compact carrier of its result across the context boundary. In inline convening it is an optional summary the chair may record. The block's format is unchanged:

  Leave the durable-figures rule and response-style sections untouched.

- [ ] **Step 3: Verify**
  - `rg -n 'Round 1|Round 3|standalone session|01-initial-meeting|02-artifacts' advisors advisors-extended` → **no matches.**
  - All 11 files contain the new `### Load when convened in a meeting` heading and the `../../meetings/[meeting-name]/artifacts/` path.
  - Path check from `advisors-extended/09-oil-gas-specialist/CONTEXT.md`: `../../meetings/...` → `meetings/...` ✓ (identical depth to core).
  - `conventions.md` Handoff section reframed to the sub-agent→chair return; the five-bullet format is intact.
  - No placeholders (except `advisors/_template/` brackets).

- [ ] **Step 4: Commit**
  ```bash
  git add advisors advisors-extended _config/shared/conventions.md
  git commit -m "feat: advisors load meeting-aware; Handoff reframed as sub-agent->chair return"
  ```

---

## Iteration 05: `AGENTS.md`, `README.md`, Wrapper Wording — Meeting-First

**Files:**
- Modify: `AGENTS.md`
- Modify: `README.md` (narrative; the "See it in action" example links are finalized in Iter 07)
- Modify: `CLAUDE.md`, `GEMINI.md` (note section wording only)

**Interfaces:**
- Produces: a meeting-first description of the system for humans and harnesses.

- [ ] **Step 1: Update `AGENTS.md`**

  In `## Folder Structure`, replace the `sessions/` three-stage description with: `meetings/` holds **records of board meetings** — each a topic-named folder holding a `brief.md`, `minutes.md`, an `artifacts/` directory, and an optional `transcript.md`. Replace any "three-stage / Round 1→2→3" prose with the live-meeting model: you talk to the board, the chair convenes the relevant advisors and produces artifacts as the conversation needs them. Keep `## Getting Started` ("To begin, load `CONTEXT.md`").

- [ ] **Step 2: Update `README.md` narrative**

  - Replace the "single-advisor consult vs. full board session" quick-start with one **"Talk to your board"** flow: open the project in your harness, load `CONTEXT.md`, and ask — the chair convenes the right advisors and produces artifacts you can edit; the chair keeps a small record (brief + minutes + artifacts), with the full transcript on request.
  - Update any `sessions/`/staged-round wording to the meeting model.
  - Leave a clearly marked `## See it in action` stub referencing the two example meetings by name (`meetings/example-emergency-fund/`, `meetings/example-rental-property/`); Iter 07 fills its description after the records exist.

- [ ] **Step 3: Update wrapper note sections**

  In `CLAUDE.md` and `GEMINI.md`, replace the "single advisor / full board session" note bullets with a single line: *"To begin, load `CONTEXT.md` — it convenes your board as a live meeting."* Do not touch the import directive or the fallback line.

- [ ] **Step 4: Verify**
  - `rg -n --glob '!docs/superpowers/**' --glob '!tmp/**' -e 'board session' -e 'Round 1|Round 2|Round 3' -e '01-initial-meeting'` → **no matches.**
  - `AGENTS.md` describes `meetings/` records and the live-meeting model; ends with "load `CONTEXT.md`."
  - `README.md` has the "Talk to your board" flow and a `## See it in action` stub naming both example folders.
  - `CLAUDE.md` still starts with `@AGENTS.md` + fallback line; `GEMINI.md` with `<!-- @include AGENTS.md -->` + fallback; neither duplicates `AGENTS.md` body.

- [ ] **Step 5: Commit**
  ```bash
  git add AGENTS.md README.md CLAUDE.md GEMINI.md
  git commit -m "docs: AGENTS/README/wrappers describe the live-meeting model"
  ```

---

## Iteration 06: Remove Staged Scaffolding & `output/` Folders

**Files:**
- Delete: `meetings/_template/` (the staged template)
- Delete: `advisors/**/output/` and `advisors-extended/**/output/` (dirs + `.gitkeep`s)
- Modify: `.gitignore` (drop the `output/` rules)

**Interfaces:**
- Produces: a repo with one artifact home and no staged scaffolding. (The example folders are handled in Iter 07.)

- [ ] **Step 1: Remove the staged template and output dirs**
  ```bash
  git rm -r meetings/_template
  git rm -r advisors/**/output advisors-extended/**/output
  ```
  (If the shell does not expand `**`, remove each `advisors/NN-name/output/` and `advisors-extended/NN-name/output/` explicitly — 10 folders.)

- [ ] **Step 2: Drop the `output/` rules from `.gitignore`**

  Remove these four lines (and their comment):
  ```gitignore
  advisors/**/output/*
  advisors-extended/**/output/*
  !advisors/**/output/.gitkeep
  !advisors-extended/**/output/.gitkeep
  ```
  Leave the profile rules and the `meetings/*/` + `!meetings/example-*/` rules intact.

- [ ] **Step 3: Verify**
  - `ls meetings/_template` → not found; `rg -n 'output/' .gitignore` → no matches.
  - No `output/` directories remain under `advisors/` or `advisors-extended/` (`find advisors advisors-extended -name output -type d` → empty).
  - `git check-ignore -v meetings/my-topic/transcript.md` → ignored by `meetings/*/`; `git check-ignore -v meetings/example-rental-property/transcript.md` → **not** ignored (ships).

- [ ] **Step 4: Commit**
  ```bash
  git add -A
  git commit -m "refactor: retire staged meetings/_template and per-advisor output/ folders"
  ```

---

## Iteration 07: Regenerate the Two Examples as Meeting Records

Replace the old staged example folders with meeting records in the routed-file shape (`brief.md` + `minutes.md` + `artifacts/`, transcript optional). Personas stay fictional. Reuse the existing artifact *content* where it still fits. Folders are topic-only (no date).

**Files:**
- Rename + restructure: `meetings/example-2026-emergency-fund/` → `meetings/example-emergency-fund/` = `brief.md` + `minutes.md`
- Rename + restructure: `meetings/example-2026-rental-property/` → `meetings/example-rental-property/` = `brief.md` + `minutes.md` + `artifacts/{affordability-and-reserves-worksheet.md, rental-deal-screen-worksheet.md, due-diligence-and-location-checklist.md}` + `transcript.md` (kept because the user asked)
- Modify: `README.md` `## See it in action` (finalize)
- Delete: the old staged subfolders/files inside both example dirs (`00-brief.md`, `CONTEXT.md`, `01-initial-meeting/`, `02-artifacts/`, `03-reconvene/`)

**Interfaces:**
- Consumes: the regenerated advisor files (Iter 04), `meeting-process.md` (Iter 02). Reuses prior artifact content currently under each example's `02-artifacts/` / `01-initial-meeting/`.

- [ ] **Step 1: Rename the example folders (drop the year) and salvage the rental artifacts**

  ```bash
  git mv meetings/example-2026-emergency-fund meetings/example-emergency-fund
  git mv meetings/example-2026-rental-property meetings/example-rental-property
  mkdir -p meetings/example-rental-property/artifacts
  git mv meetings/example-rental-property/02-artifacts/financial-planner/affordability-and-reserves-worksheet.md meetings/example-rental-property/artifacts/affordability-and-reserves-worksheet.md
  git mv meetings/example-rental-property/02-artifacts/real-estate-advisor/rental-deal-screen-worksheet.md meetings/example-rental-property/artifacts/rental-deal-screen-worksheet.md
  git mv meetings/example-rental-property/02-artifacts/real-estate-advisor/due-diligence-and-location-checklist.md meetings/example-rental-property/artifacts/due-diligence-and-location-checklist.md
  ```
  The salvaged artifacts mention their meeting folder; update any `example-2026-rental-property` reference inside them to `example-rental-property`.

- [ ] **Step 2: Author the rental record — `brief.md` + `minutes.md` (+ kept `transcript.md`)**

  Write `meetings/example-rental-property/brief.md` (the question + Priya & Marcus's situation + date) and `meetings/example-rental-property/minutes.md` (the verdict that the $240k deal is a pass, what a "yes" looks like, each of the three artifacts with a one-line "what it's for / how to use it," the resolved appreciation-vs-discipline tension, and next steps). Keep figures illustrative-labeled. Because the user asked to save it, also keep a `transcript.md` showing the chair routing two advisors, commissioning artifacts, **the user requesting a worked passing example and the Financial Planner revising it in place while the Real Estate Advisor reacts**, and a board synthesis. *(Recommended: produce via sub-agents; the fictional user turns are authored as part of the transcript.)*

- [ ] **Step 3: Author the emergency-fund record — `brief.md` + `minutes.md` only**

  Write `meetings/example-emergency-fund/brief.md` (Daniel's question + situation + date) and `meetings/example-emergency-fund/minutes.md` (the 4-month / ~$12,800 HYSA recommendation, the build plan, the "stop at the target" discipline, and the flagged-for-later student-loan-vs-Roth item). No artifact, no transcript — this is the lightest record, showing that a single-advisor meeting leaves just two small files.

- [ ] **Step 4: Delete the old staged structure in both example dirs**
  ```bash
  git rm -r meetings/example-rental-property/00-brief.md meetings/example-rental-property/CONTEXT.md \
            meetings/example-rental-property/01-initial-meeting meetings/example-rental-property/02-artifacts \
            meetings/example-rental-property/03-reconvene
  git rm -r meetings/example-emergency-fund/00-brief.md meetings/example-emergency-fund/CONTEXT.md \
            meetings/example-emergency-fund/01-initial-meeting
  ```
  (If an earlier example pass left a `transcript.md` under emergency-fund, remove it too — the lightest record needs none.)

- [ ] **Step 5: Finalize `README.md` `## See it in action`**

  Two bullets: the emergency-fund record as the simplest path (single advisor; just `brief.md` + `minutes.md`); the rental-property record as the flagship (two advisors, three `artifacts/`, the mid-meeting revision, board synthesis; `brief.md` + `minutes.md` + `artifacts/` + kept `transcript.md`). Link the records and the rental artifacts.

- [ ] **Step 6: Verify**
  - Final trees: `meetings/example-emergency-fund/` = `brief.md` + `minutes.md`; `meetings/example-rental-property/` = `brief.md` + `minutes.md` + `artifacts/` (3) + `transcript.md`.
  - No `00-brief.md`, `CONTEXT.md`, `01-initial-meeting/`, `02-artifacts/`, `03-reconvene/`, and no `example-2026-*` folder names remain under `meetings/`.
  - The rental `minutes.md` lists each artifact with how-to-use; its `transcript.md` shows the user requesting a change and an advisor revising it. Personas fully fictional. Year-specific figures carry illustrative labels.
  - `README.md` "See it in action" links both records.

- [ ] **Step 7: Commit**
  ```bash
  git add -A
  git commit -m "feat: regenerate examples as meeting records (brief + minutes + artifacts)"
  ```

---

## Iteration 08: Integration Review

**Files:** No new files. Verification and gap-fixing only.

- [ ] **Step 1: Stale-reference scan (the key correctness gate)**
  ```bash
  rg -n --glob '!docs/superpowers/**' --glob '!tmp/**' \
     -e 'sessions/' -e 'board-process' -e '01-initial-meeting' -e '02-artifacts' -e '03-reconvene' \
     -e 'Round 1|Round 2|Round 3' -e '/output/' .
  ```
  Expected: **no matches.** Fix any hit in place.

- [ ] **Step 2: Path audit — core AND extended advisors**
  - From `advisors/01-financial-planner/CONTEXT.md` and from **both** `advisors-extended/09-…` and `…/10-…`, confirm `../../_config/shared/{disclaimer,collaboration,conventions}.md`, `../../_config/profile/`, and `../../meetings/[meeting-name]/artifacts/` all resolve (equal depth for core and extended).

- [ ] **Step 3: Structural presence check**
  - `_config/shared/meeting-process.md` exists; `_config/shared/board-process.md` does **not**.
  - `meetings/` has the two `example-*` records and no `_template/`.
  - No `output/` dirs under `advisors/`/`advisors-extended/`.
  - Root `CONTEXT.md` has `## Hosting a Meeting`; all 11 advisor files have `### Load when convened in a meeting`.

- [ ] **Step 4: `.gitignore` behavior**
  - `git check-ignore` confirms: profile data files ignored; `_config/profile/CONTEXT.md` tracked; a topic-only user meeting (e.g. `meetings/my-topic/`) ignored via `meetings/*/`; both `meetings/example-*` tracked; no `output/` rules remain.

- [ ] **Step 5: Conventions + fiction compliance**
  - Regenerated example artifacts and transcripts: every year-specific figure carries "illustrative — verify current-year value"; personas/companies/figures fully fictional.
  - `conventions.md` Handoff section reframed to the sub-agent→chair return with the five-bullet format intact.

- [ ] **Step 6: Placeholder scan**
  ```bash
  rg -n --glob '!docs/superpowers/**' --glob '!tmp/**' --glob '!advisors/_template/**' -e 'TBD|TODO|\[fill|\[your |\[Role' .
  ```
  Expected: no matches outside `advisors/_template/`.

- [ ] **Step 7: Final commit**
  ```bash
  git add -A
  git commit -m "chore: integration review — stale-ref scan, path audit, gitignore, conventions"
  ```

---

## Self-Review Against Spec

| Spec section | Covered by | Status |
|---|---|---|
| §1 Target = agentic only; extension not restart | Global constraints; all iters | ✓ |
| §2 Goal: meeting-first, chair-routed, living artifacts, absorb pipeline, routed record, rename | Iters 01–07 | ✓ |
| §3 Non-goals (no web chat, no index, no versioning) | Out of scope; nothing built | ✓ |
| §4 Interaction model (the loop, save, single-advisor) | Iter 02 (`meeting-process.md`), Iter 03 (host) | ✓ |
| §5.1 Meeting host (root CONTEXT.md) | Iter 03 | ✓ |
| §5.2 Advisors mode-aware (Inputs) | Iter 04 | ✓ |
| §5.3 Meeting protocol + convening modes | Iter 02 | ✓ |
| §5.4 Artifacts as living files | Iter 02; Iter 07 examples | ✓ |
| §5.5 Meeting record (brief + minutes + artifacts; transcript optional) | Iter 02; Iter 07 | ✓ |
| §5.6 Handoff repositioned | Iter 04 | ✓ |
| §6.1 Renames (sessions→meetings, board→meeting-process) | Iter 01 | ✓ |
| §6.2 Reframed files (root, AGENTS, advisors, conventions, README) | Iters 03–05 | ✓ |
| §6.3 New meeting-record shape | Iter 07 | ✓ |
| §6.4 Removals (staged template, examples, output/) | Iters 06, 07 | ✓ |
| §6.5 `.gitignore` updates | Iters 01, 06 | ✓ |
| §6.6 Untouched (identities, onboarding, disclaimer/ethics, wrappers, LICENSE) | (not modified) | ✓ |
| §7 Examples regenerated as records (fictional) | Iter 07 | ✓ |
| §8 Cross-harness (sub-agent vs inline, file-based) | Iter 02 | ✓ |
| §10 Implementation sequence + carried constraints | This plan, all iters | ✓ |

### Gaps Identified: None
</content>
</invoke>
