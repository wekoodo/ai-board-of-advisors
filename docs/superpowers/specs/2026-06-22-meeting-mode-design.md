# Board of Advisors — Meeting-Mode Redesign

**Date:** 2026-06-22
**Status:** Draft — Pending Implementation
**Supersedes (in part):** the staged board-session model in `2026-06-21-board-of-advisors-design.md` (§8 Consultation Flow, §7.10 board-process)
**Builds on:** the existing ICM architecture, advisor identities, onboarding/profile, and shared config from v2

---

## 1. Overview

The current system models a board consultation as a **staged file pipeline**: the user copies a session
template, writes a brief, then triggers Round 1 → Round 2 → Round 3, reading advisor output files between
stages. The user operates the process from the outside and receives deliverables; it is one-shot and
non-conversational.

This redesign replaces that with a **live meeting**: the board chair becomes a meeting *host*, and the
user is a participant in one continuous, multi-turn conversation. The chair routes each message to the
relevant advisor(s), convenes them, and — when useful — has them produce **artifacts as living files** the
user can read along with, edit directly, or request changes to. The meeting continues until the user is
done and can be resumed later.

The staged pipeline is **absorbed**, not kept alongside: "initial takes," "artifact production," and
"reconvene" stop being a rigid external sequence and become natural moves the chair makes *inside* a
meeting when the conversation warrants. There is one way to use the system: **talk to your board.**

This is an **extension** of the existing system. Every expensive asset — the 10 advisor identity/contract
files, onboarding + persistent profile, shared disclaimer/ethics/conventions/collaboration, and the
cross-harness wrappers — is reused unchanged or lightly adapted. What changes is the orchestration layer.

### Target environment

The system targets **agentic harnesses that read project files** (Claude Code, Codex, OpenCode, Hermes,
and similar). A filesystem is always assumed; artifacts are always real files. Plain web-chat usage
(claude.ai / ChatGPT / Gemini chat) is **explicitly not a target** — no canvas/artifact-panel branch, no
Project/Gem/GPT packaging.

---

## 2. Goals

- Make a new agent session naturally behave as a new **board meeting** — conversational, multi-turn, with
  the user as a participant — with no required command (a `/meeting` convenience may exist but is optional).
- Have the chair **route to the relevant advisor(s)** per message rather than always convening the full board.
- Treat **artifacts as living documents**: produced inline during the meeting as real files, reviewable and
  editable by the user, with advisors reacting to the user's edits and change requests.
- **Absorb** the staged Round 1/2/3 pipeline into the meeting so there is a single interaction model.
- Preserve **context discipline**: where the harness supports sub-agents, convene each advisor as an
  isolated sub-agent so a long meeting does not exhaust the host's context window; fall back to in-context
  role-play (still file-based) where it does not.
- **Hybrid persistence**: write artifacts to disk whenever they are produced; write a full meeting
  transcript only when the user asks to "save/checkpoint."
- Rename `sessions/` → `meetings/` to remove the ambiguity between *board meetings* and *agent sessions /
  context windows*.

## 3. Non-Goals

- No web-chat support, no canvas mechanism, no Project/Gem/Custom-GPT packaging.
- No meeting index, search, or cross-meeting navigation tooling.
- No profile versioning or change history beyond what already exists.
- No resume mechanism beyond reopening the meeting folder in an agentic harness (the harness's own
  conversation history covers in-session continuity).
- No new advisors; no changes to advisor domain expertise.

---

## 4. Interaction Model

A single continuous conversation hosted by the board chair.

1. **Engage** — On engaging the system, the chair checks `_config/profile/`. If no profile exists, it runs
   onboarding first (unchanged), then returns to host the meeting. If a profile exists, the meeting begins.
2. **Ask** — The user asks a question or raises a topic.
3. **Route** — The chair names which advisor(s) the topic touches and convenes them (one or several).
4. **Respond** — Convened advisors answer in character. The chair adds a short synthesis when more than one
   weighed in.
5. **Artifact (when useful)** — An advisor produces a document (a worksheet, checklist, plan, comparison)
   as a real file under the meeting's `artifacts/`. The chair surfaces it in the conversation.
6. **Collaborate** — The user reads the artifact, edits it directly, or requests changes. The producing
   advisor revises it; other advisors react as relevant.
7. **Continue** — The user asks follow-ups; the loop repeats. The chair may, for a big decision,
   deliberately run a fuller arc (every relevant advisor's initial take → a full artifact set → a
   reconvene) — the old pipeline's thoroughness, conducted live.
8. **Save (optional)** — At any point the user says "save this meeting" and the chair writes a
   `transcript.md` capturing the conversation and decisions alongside the artifacts already on disk.

"Single-advisor consult" is not a separate mode — it is simply a meeting in which the chair convenes one
advisor.

---

## 5. Architecture & Components

### 5.1 Meeting host (board chair) — root `CONTEXT.md`, reframed
- Performs the first-launch profile/onboarding check (unchanged behavior).
- Hosts the meeting loop in §4: routing, convening, synthesis, artifact orchestration, and the "save"
  action.
- The prior "single advisor vs. full board session" routing decision collapses into "convene whoever is
  relevant — one or many."

### 5.2 Advisors — the 10 identity files (+ `_template`), made mode-aware
- Unchanged identity, expertise, process, and disclaimer.
- The `Inputs` section is rewritten: the rigid `Load if board session — Round 1` / `Round 3` lists are
  replaced by meeting-aware loading: *when convened in a meeting, load your identity, the profile, the
  shared rules, and any existing meeting artifacts relevant to your domain.*
- All `../../sessions/…` path references become `../../meetings/…`.

### 5.3 Meeting protocol — `_config/shared/meeting-process.md` (replaces `board-process.md`)
Defines the conversational loop, and how convening degrades by harness capability:
- **Sub-agent mode (preferred, where supported):** the chair convenes each advisor as an isolated
  sub-agent, handing it only its load list; the advisor writes its artifact file and returns a `## Handoff`
  summary to the chair. Keeps the host's context small across a long meeting.
- **Inline mode (fallback):** in a harness without sub-agents, the host role-plays the advisor in the
  shared context and still writes artifact files.
This is the same "delegated vs manual" distinction already adopted, reframed for the conversational model;
both are file-based.

### 5.4 Artifacts — living files
- Always written under the meeting's `artifacts/` directory.
- Follow existing `conventions.md` (durable-figures rule, response style).
- Editable by the user; the meeting reads edits and responds. Revisions overwrite the same file.

### 5.5 Meeting record — `meetings/`
- A meeting record is `meetings/YYYY-MM-DD-topic/` containing:
  - `artifacts/` — documents advisors produced (written whenever artifacts exist)
  - `transcript.md` — written on "save/checkpoint"
- The chair creates the folder lazily — on first artifact or on "save" — naming it from the meeting's date
  and a short topic slug (`YYYY-MM-DD-topic`). No template to copy, no brief file to fill in. The record
  shape is documented in `meeting-process.md`.

### 5.6 `conventions.md` — Handoff reframed
- The `## Handoff` block is repositioned from "what every stage file ends with" to "what a convened
  sub-agent advisor returns to the chair." It remains the compact carrier between the sub-agent's context
  and the host's. Format unchanged.

---

## 6. File & Structure Changes

### 6.1 Renames
- `sessions/` → `meetings/`
- `_config/shared/board-process.md` → `_config/shared/meeting-process.md` (rewritten)

### 6.2 Reframed files
- Root `CONTEXT.md` — meeting host (see §5.1).
- `AGENTS.md` — "how it works" description updated from staged sessions to meeting-first.
- All advisor `CONTEXT.md` (core 01–08, extended 09–10, and `advisors/_template/`) — `Inputs` rewritten
  (§5.2); `sessions/` paths → `meetings/`.
- `_config/profile/CONTEXT.md`, `_config/shared/collaboration.md`, and any other file referencing
  `sessions/` — path updates.
- `conventions.md` — Handoff repositioned (§5.6).
- `README.md` — "See it in action" points at the two meeting records; the single-advisor-vs-board
  quick-start collapses into "just talk to your board"; install unchanged ("Use this template" → onboard).

### 6.3 New meeting-record shape
Replaces the `01-initial-meeting/`, `02-artifacts/`, `03-reconvene/` staged subfolders:
```
meetings/
├── example-2026-emergency-fund/
│   └── transcript.md                     # (+ artifacts/ if any)
├── example-2026-rental-property/
│   ├── transcript.md
│   └── artifacts/
│       ├── affordability-and-reserves-worksheet.md
│       ├── rental-deal-screen-worksheet.md
│       └── due-diligence-and-location-checklist.md
└── YYYY-MM-DD-topic/                     # user meetings (gitignored)
```

### 6.4 Removals
- `sessions/_template/` (the staged template) and `sessions/example-*` (old staged examples).
- `advisors/**/output/` and `advisors-extended/**/output/` folders and their `.gitkeep`s — one artifact
  home (`meetings/…/artifacts/`) makes per-advisor output dirs redundant.

### 6.5 `.gitignore`
- Swap `sessions/????-??-??-*/` → `meetings/????-??-??-*/` (user meetings local; `example-*` shipped).
- Drop the `advisors/**/output/*` and `advisors-extended/**/output/*` rules and their `.gitkeep` negations.

### 6.6 Untouched
The 10 advisor identities themselves, onboarding + profile system, `disclaimer.md`, `ethics.md`,
`collaboration.md` (content), the `CLAUDE.md` / `GEMINI.md` wrappers, and `LICENSE`.

---

## 7. Examples

Both examples are regenerated as real meeting records by running the new protocol via sub-agents
(dogfooding it). Personas remain fully fictional.

- **`meetings/example-2026-emergency-fund/`** — a short single-advisor meeting: the chair routes to the
  Financial Planner, the advisor answers, the user is satisfied. Demonstrates the simplest path and that
  "single advisor" is just a one-voice meeting. `transcript.md`; `artifacts/` only if one is produced.
- **`meetings/example-2026-rental-property/`** — the flagship. The chair routes to Real Estate + Financial
  Planner; they weigh in; the chair commissions the affordability and deal-screen artifacts; **the user
  reviews the affordability worksheet and requests a change; the advisor revises it; the other advisor
  reacts**; the user says "save this meeting." Its `transcript.md` shows the new collaborative-artifact
  capability end to end, with the revised documents in `artifacts/`.

The fictional user's turns are authored as part of the transcript. Existing artifact content from the
current rental example may be reused/adapted into `artifacts/` rather than regenerated from scratch where
it still fits.

---

## 8. Cross-Harness Behavior

| Harness capability | Convening | Artifacts | Transcript |
|---|---|---|---|
| Sub-agents + filesystem (e.g. Claude Code) | Isolated sub-agent per advisor (preferred) | Real files | On "save" |
| Filesystem, no sub-agents | Host role-plays advisor inline | Real files | On "save" |

Both paths are file-based and produce identical records. The chair selects the mode based on harness
capability, defaulting to sub-agents where available.

---

## 9. Out of Scope (YAGNI)

- Web-chat / canvas / Project-Gem-GPT packaging.
- Meeting index, search, or navigation tooling.
- Profile versioning / change history.
- Any resume mechanism beyond reopening the meeting folder.
- New advisors or changes to advisor expertise.

---

## 10. Implementation Notes (for the plan)

Suggested sequence (each step independently verifiable):

1. **Rename sweep** — `sessions/` → `meetings/`; `board-process.md` → `meeting-process.md`; update every
   `sessions/` path reference across advisor files, root `CONTEXT.md`, `collaboration.md`, profile
   `CONTEXT.md`, README, and `.gitignore`.
2. **Write `meeting-process.md`** — the conversational protocol (§4, §5.3), sub-agent vs inline convening,
   artifact lifecycle, the meeting-record shape, and the "save" action.
3. **Reframe root `CONTEXT.md`** — meeting host; collapse single-vs-board routing; keep the onboarding check.
4. **Update advisor `Inputs`** — meeting-aware loading across all 10 advisors + `advisors/_template/`.
5. **Reposition Handoff in `conventions.md`.**
6. **Update `AGENTS.md`** and **`README.md`** to meeting-first.
7. **Remove** `sessions/_template/`, old `sessions/example-*`, and the `output/` folders; update
   `.gitignore`.
8. **Regenerate the two examples** as meeting records under `meetings/`, via sub-agents.
9. **Integration review** — path audit (incl. `advisors-extended/` depth), placeholder scan, gitignore
   verification, cross-harness wrapper check, and confirm no stale `sessions/` or `output/` references
   remain.

### Constraints carried into the plan
- Examples remain entirely fictional (invented persona, figures); no real person, company, or transaction.
- Advisor relative paths must continue to resolve identically for core and extended advisors (equal depth).
- Artifacts obey the durable-figures rule from `conventions.md`.
- The profile/onboarding flow and the cross-harness wrappers must keep working unchanged.
</content>
</invoke>
