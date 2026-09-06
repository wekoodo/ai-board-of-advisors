# Meeting Process

A board meeting is **one continuous conversation** hosted by the board chair. The user is a participant
in the room — asking, reacting, editing the documents that get produced — not an outsider operating a
pipeline from the edge. The protocol below is harness-agnostic: any AI agent that can read project
files and follow instructions can host a meeting, whether it supports sub-agents or only a single
context window.

## The Meeting Loop

At the **start of the meeting**, before the first cycle, the chair does two soft checks (once per
session — not every turn):

1. **`_inbox/` drop zone** — list any documents waiting there, surface them to the user, and ask
   which are relevant to this meeting. **Move** the confirmed files into
   `meetings/<meeting>/inputs/` (creating that directory), and leave the rest in `_inbox/` for
   future meetings. `_inbox/` documents are local-only (gitignored); they become part of the meeting
   record once assigned. If `_inbox/` is empty, skip silently. Follow `meetings/CONTEXT.md` for
   whether `<meeting>` is the existing record's path, a new `<topic-slug>/`, or a new
  `<scope>/<topic-slug>/`. Choose the meeting path before moving files.

2. **Product-update check** — follow `_config/shared/version.md`, the single source for the
   on-demand/daily, fail-soft check. Load `_config/shared/updates.md` only to **connect** `upstream`
   or **apply** an update.

When the request refers to earlier work or prior meeting context may matter, follow
`meetings/CONTEXT.md`: use its index-first, selective-loading flow to choose one meeting before
loading its record. Do not list or preload the complete meeting history.

A meeting unfolds turn by turn. Each cycle:

1. **The user asks** — a question, a topic, a decision they're weighing, a problem they want a fresh
   look at.
2. **The chair routes** — load `convening.md` before picking seats. Names which advisor(s) the
   topic actually touches (one, several, or occasionally the whole board) and convenes them.
   Default to the fewest seats that can own the question. Routing is per-message, not per-meeting:
   a later turn may pull in a different mix.
3. **The advisors respond in character** — each convened advisor answers from its own domain, following
   the response style in `conventions.md` and grounded in the user's profile.
4. **The chair synthesizes when several weighed in** — a short integration call-out: where the advisors
   agree, where they diverge, and what the user should take away. When only one advisor was convened,
   no synthesis is needed.
5. **An artifact is produced when a document would help** — a worksheet, checklist, comparison, plan,
   model, or memo. The producing advisor writes it as a real file under the meeting's `artifacts/`
   directory and the chair surfaces it in the conversation.
6. **The user collaborates on the artifact** — reads it, edits it directly in the file, or asks for
   changes in the conversation. The producing advisor revises the file; other advisors react to the
   revision when their domain is implicated.
7. **The loop continues** — the user asks the next thing, the chair routes again, the meeting keeps
   going. There is no fixed length and no required end state.
8. **The meeting is captured as a small record** — as the meeting reaches decisions, the chair writes
   a `brief.md` (the question and context) and a `minutes.md` (the decisions, each artifact and how to
   use it, profile updates, and next steps) alongside any `artifacts/`. The full turn-by-turn
   `transcript.md` is written only if the user asks to keep it ("save the full transcript").
9. **Standing facts go back to the profile** — follow **Profile write-back** below. Run this as
   facts land and again when minutes are written. Do not skip it because the user did not ask.

A "single-advisor consult" is not a separate mode of the system — it is simply a meeting in which the
chair convenes one voice. The same loop applies; the synthesis step in (4) just collapses.

## Convening Modes

The chair convenes advisors in one of two ways depending on what the host harness supports. Both are
file-based and produce identical records. This supersedes the older **manual vs. delegated** framing —
there is now one protocol with two execution modes.

### Sub-agent mode (preferred, where the harness supports it)

The chair convenes each advisor as an **isolated sub-agent**, handing it only its load list:

- The advisor's own `CONTEXT.md`.
- `_config/profile/CONTEXT.md`, then only the profile files that router names for this question.
  Do not bulk-load `entities/`.
- Shared protocol: `_config/shared/disclaimer.md`, `collaboration.md`, `ethics.md`, and
  `conventions.md`.
- Skill overlay when writing: `google-doc-style-overlay.md`.
- Any existing artifacts under `meetings/<meeting>/artifacts/` relevant to the advisor's domain.
- The chair's specific question or task for it this turn.

The advisor responds in character, writes any artifact file directly to `meetings/<meeting>/artifacts/`,
and returns a compact `## Handoff` summary to the chair. The chair stitches the handoff into the
conversation and surfaces the artifact to the user.

This mode keeps the host's context **small across a long meeting**: the host carries the running
transcript and each advisor's returned handoff — never the full identity files, references, and
profile each advisor loaded. That separation is what lets a multi-turn, multi-advisor meeting run for
hours without exhausting the host's context window.

### Inline mode (fallback, when sub-agents are unavailable)

In a harness without sub-agents, the host role-plays the convened advisor directly in the shared
context. The advisor's identity, profile, and shared rules are already in scope, and the host still
writes any artifact file to `meetings/<meeting>/artifacts/` as a real file on disk. The `## Handoff`
block is optional in this mode — the chair may record one when it's useful for synthesis or for the
eventual transcript — because there is no context boundary to carry the handoff across.

Inline mode produces the same on-disk record as sub-agent mode. The only difference is where the
advisor's reasoning runs.

## Artifacts

Artifacts are the **living documents** of a meeting — the worksheets, plans, checklists, comparisons,
and memos advisors produce when a document will serve the user better than prose in a transcript.

- **Location.** Every artifact lives at `meetings/<meeting>/artifacts/<name>.md`. There is no other
  artifact home; the per-advisor `output/` directories from earlier versions of this system are
  retired.
- **Authoring rules.** Artifacts follow `conventions.md`: durable formulas and ratios are stated
  plainly, but any concrete year-specific figure (contribution limits, tax brackets, exemption
  amounts, premium ranges, rate assumptions) is labeled **"illustrative — verify current-year
  value."** Format follows the response style guidance — lead with the answer, use numbered lists for
  steps and tables for comparisons. Use the user's real profile facts; do not substitute sample
  names or example.com data. See `google-doc-style-overlay.md`.
- **The user may edit them directly.** The user can open an artifact in their editor and change it.
  The meeting reads those edits on the next turn — the chair and advisors react to the artifact as it
  now is, not as it was when produced.
- **Revisions overwrite the same file.** When the user requests a change in conversation, the
  producing advisor revises the artifact and writes back to the same path. The file always
  reflects the current state. Private meeting records are gitignored, so Git does not keep
  their revision history. For a consequential change, record the prior decision or assumption
  in `minutes.md` or in the artifact; do not commit personal data to the product repository.

## The Meeting Record

A meeting record is a folder named from a short **topic slug only** — the date lives inside the
files, not in the folder name. Follow `meetings/CONTEXT.md`: `meetings/<topic-slug>/` when
`_config/profile/entities/index.md` is absent; new meetings use `meetings/<scope>/<topic-slug>/`
when that index exists (`personal`, `trust`, or an entity slug). Resume an existing record at its
current path; do not move a flat folder after the index appears. A substantive meeting leaves a small set of
**routed, single-purpose files** rather than one monolithic document:

- **`brief.md`** — *what the meeting was about*: the user's question, the relevant context, and the
  date. The entry point — read this first to know what was on the table.
- **`minutes.md`** — *what happened and what to do now*: which advisors were convened, the key
  decisions and recommendations, each artifact with a one-line note on what it is and how to use it,
  profile updates, and the open questions / next steps. This is the scannable summary — read it
  instead of replaying the whole conversation.
- **`artifacts/`** — present whenever the meeting produced one or more deliverables. Each file is a
  living document the user can read and edit.
- **`inputs/`** — present whenever the user supplied pre-meeting documents. Holds the source files
  moved from `_inbox/` when the meeting started (contracts, statements, spreadsheets). Local-only,
  like the rest of a real meeting record.
- **`transcript.md`** — the full, turn-by-turn conversation. Written **only when the user asks to
  keep it** ("save the full transcript" / "keep the record"). It exists for digging deeper into how a
  conclusion or an artifact came about — not as the default record.

The chair creates the folder **lazily** — when the meeting's question and context are clear enough to
write a `brief.md`, when the first artifact is produced, or when the user asks to save, whichever
comes first. `brief.md` and `minutes.md` are the chair's to write — not a template the user fills in.
A quick exchange that needs nothing written down leaves no record, and that is fine; but once a
meeting reaches a real decision or produces an artifact, capture it as a `brief.md` + `minutes.md`
pair so the user can return to a small, scannable summary instead of re-reading everything.

Do not create a folder for a test, an exploratory question, or a ranking of work already listed on
profile action registers (`goals.md`, an entity `goals.md`, or trust planning actions). Those
answers stay in conversation unless the user asks to save the ranking or then starts work on a
named action.

At that same lazy-creation threshold, create or update exactly one local `meetings/index.md` entry,
keyed by the meeting folder path, following `meetings/CONTEXT.md`. The minutes field may remain
`pending` until `minutes.md` exists; do not create empty minutes solely to satisfy the index. Update
the same entry when minutes are written, the meeting status changes, or material routing metadata
changes. Meeting record files are authoritative: when an entry is stale, missing, or duplicated,
use the router's scoped search, trust the record files, and repair or consolidate the entry.

## Profile write-back

Meetings are working records. Profiles are standing facts. When a meeting establishes, changes, or
completes a standing fact, write that fact to the owning profile file **in the same session**. Do
not wait for the user to ask.

This is a **chair duty**. Convened advisors flag candidates in the `## Handoff` **Profile updates**
line. The chair still runs this check if that line is missing or says `none` incorrectly.

### When

1. As soon as a standing fact is established — a decision, executed instrument, new or changed
   coverage, ownership or tax status, completed or new action, or other material event.
2. Whenever `minutes.md` is written or updated. Minutes are not complete until this check has run.
3. When the user ends a meeting that already has a record.

If nothing standing changed (analysis, options not chosen, ranking, exploratory Q&A), write
`none — profiles already current` in minutes and stop. Do not invent a profile edit.

A durable fact stated in conversation still belongs in the profile even when no meeting folder is
created. Write the profile file; do not create a meeting only to hold that fact.

### What belongs in the profile

Write the **smallest owning file or files**, following `_config/profile/CONTEXT.md` and, when it
exists, `_config/profile/entities/CONTEXT.md`:

| Change | Typical home |
| --- | --- |
| Household standing facts or household actions | `personal.md`, `financial.md`, `investments.md`, `goals.md` (resolved owning sections when a named path is a shim) |
| High-level entity map | `businesses.md` — summary only; details stay in the entity folder when one exists |
| Entity identity, purpose, relationship, status | `<entity-slug>/overview.md`, and `entities/index.md` when routing status (depth) changes |
| Entity freshness (`current` / `stale`) | `entities/index.md` Freshness column, and the entity router's Freshness line. Not overview onboarding status. After scoped facts are confirmed, set `current`. |
| Ownership, control, agreements, succession | `<entity-slug>/governance.md` (resolved owning section when a shim) |
| Activities, people, systems, operating model | `<entity-slug>/operations.md` (resolved owning section when a shim) |
| Revenue, cash, assets, liabilities, reporting | `<entity-slug>/financial.md` (resolved owning section when a shim) |
| Tax classification, elections, filings, payroll | `<entity-slug>/tax.md` (resolved owning section when a shim) |
| Contracts, liabilities, licensing, coverage | `<entity-slug>/risk-insurance.md` (resolved owning section when a shim) |
| Entity actions added, completed, or retargeted | `<entity-slug>/goals.md` (resolved action file when that path is a shim) |
| Evidence inventory for a reviewed source | `<entity-slug>/sources.md` (create only when that inventory is needed) |
| Living-trust standing facts or trust actions | `trust.md` (resolved owning section when a shim; never copy facts into the shim) |

Record each action once, in the profile that owns it. Link the meeting folder from the profile when
the meeting is the provenance of a standing fact. Use that record's current path; do not rewrite the
link to a scoped layout unless the folder actually moved (it should not — see
`meetings/CONTEXT.md` **Existing records stay put**). Do not copy the minutes or artifacts into the
profile.

### What stays in the meeting

Analysis, options not chosen, worksheets, drafts, recommendations not adopted, and the narrative of
how a conclusion was reached. Those remain in `brief.md`, `minutes.md`, and `artifacts/`.

### How

1. Identify scopes from the brief (`personal`, `trust`, entity slugs) plus any related profile the
   decision actually changed.
2. Load only the profile files that would own the new facts. If a named path is a shim, follow
   `icm-conventions.md` **Resolve a named profile path** at load; do not compare facts against
   the shim body. Do not bulk-load every entity folder.
3. Compare those files to the decisions, executed instruments, and completed actions from this
   session.
4. Write the delta to the resolved owning file (if a named path is a shim, follow
   `icm-conventions.md` **Resolve a named profile path**). Follow
   `_config/profile/entities/CONTEXT.md` **Fact ownership** for entity facts: owner first,
   then any summary that still repeats the fact. Stamp `Last Updated: YYYY-MM-DD` only on
   files actually edited. That stamp does not re-verify unrelated facts in the file. Follow
   `icm-conventions.md` **Keep files load-scoped**.
5. If a fact is still hypothetical, or the user has not decided, do not write it as standing
   fact and do not add it to the action register. If the user adopted an intention (pursue an
   election, change coverage, form an entity) but it is not yet implemented, record that
   intention in the owning action register as pending — not as an effective fact. Ask once
   when file ownership is unclear.
6. Record the result in `minutes.md` under **Profile updates**: each path and a one-line change, or
   `none — profiles already current`.

### Do not

- Start or restart onboarding because a meeting happened. A write-back is a scoped fact update.
  A material event or new source is written here. Set that entity's index Freshness column (and
  the entity router's Freshness line) to `stale`; do not change depth or overview onboarding
  status. After the scoped facts are confirmed and written, set Freshness back to `current`.
  If some facts could not be confirmed, keep `stale` and list them as open questions. Do not
  start an entity interview. Load `../setup/entity-onboarding.md` only when the user asks to
  reopen a domain.
- Duplicate an action into more than one register.
- Write an adopted plan as an effective tax, ownership, or coverage fact before
  implementation is confirmed.
- Invent `sources.md` for an ordinary fact update.

## A Bigger Decision

Some questions deserve more than a single turn or two. For a **major, multi-domain decision** — a
business restructure, a large real-estate purchase, an estate plan overhaul, an employer-equity event,
a career change with cross-cutting financial implications — the chair can deliberately run a fuller
arc *inside* the meeting:

1. **Get every relevant advisor's initial take.** The chair convenes each implicated advisor in turn
   (or in parallel, in sub-agent mode) and lets them weigh in from their domain before the meeting
   converges on a direction.
2. **Commission a full artifact set.** Advisors produce the documents the decision actually needs — a
   cash-flow model, a deal screen, a tax projection, an entity comparison, an insurance gap analysis
   — each written into `artifacts/`.
3. **Reconvene the advisors over the artifacts.** With the artifacts on disk, the chair brings the
   advisors back so each can review the full set (including any user edits) and update their position
   in light of what the others produced.
4. **Deliver an integrated synthesis.** The chair pulls the threads together into a single
   recommendation the user can act on — flagging where advisors aligned, where trade-offs remain, and
   which next steps belong to the user versus to licensed professionals outside this system.

This is the same thoroughness an old-style formal board process delivered, now conducted live with
the user in the room — able to interrupt, redirect, edit an artifact mid-arc, or ask for a different
advisor at any point.
