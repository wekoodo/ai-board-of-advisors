# Meeting Process

A board meeting is **one continuous conversation** hosted by the board chair. The user is a participant
in the room — asking, reacting, editing the documents that get produced — not an outsider operating a
pipeline from the edge. The protocol below is harness-agnostic: any AI agent that can read project
files and follow instructions can host a meeting, whether it supports sub-agents or only a single
context window.

## The Meeting Loop

At the **start of the meeting**, before the first cycle, the chair checks the `_inbox/` drop zone:
list any documents waiting there, surface them to the user, and ask which are relevant to this
meeting. **Move** the confirmed files into `meetings/<meeting>/inputs/` (creating that directory),
and leave the rest in `_inbox/` for future meetings. `_inbox/` documents are local-only (gitignored);
they become part of the meeting record once assigned. If `_inbox/` is empty, skip silently.

A meeting unfolds turn by turn. Each cycle:

1. **The user asks** — a question, a topic, a decision they're weighing, a problem they want a fresh
   look at.
2. **The chair routes** — names which advisor(s) the topic actually touches (one, several, or
   occasionally the whole board) and convenes them. Routing is per-message, not per-meeting: a later
   turn may pull in a different mix.
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
   use it, and next steps) alongside any `artifacts/`. The full turn-by-turn `transcript.md` is written
   only if the user asks to keep it ("save the full transcript").

A "single-advisor consult" is not a separate mode of the system — it is simply a meeting in which the
chair convenes one voice. The same loop applies; the synthesis step in (4) just collapses.

## Convening Modes

The chair convenes advisors in one of two ways depending on what the host harness supports. Both are
file-based and produce identical records. This supersedes the older **manual vs. delegated** framing —
there is now one protocol with two execution modes.

### Sub-agent mode (preferred, where the harness supports it)

The chair convenes each advisor as an **isolated sub-agent**, handing it only its load list:

- The advisor's own `CONTEXT.md`.
- `_config/profile/` (the user's profile).
- `_config/shared/disclaimer.md`, `collaboration.md`, and `conventions.md`.
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
  steps and tables for comparisons.
- **The user may edit them directly.** The user can open an artifact in their editor and change it.
  The meeting reads those edits on the next turn — the chair and advisors react to the artifact as it
  now is, not as it was when produced.
- **Revisions overwrite the same file.** When the user requests a change in conversation, the
  producing advisor revises the artifact and writes back to the same path. The history of edits lives
  in git; the file always reflects the current state.

## The Meeting Record

A meeting record is a folder at `meetings/<topic-slug>/`, named from a short **topic slug only** —
the date lives inside the files, not in the folder name. A substantive meeting leaves a small set of
**routed, single-purpose files** rather than one monolithic document:

- **`brief.md`** — *what the meeting was about*: the user's question, the relevant context, and the
  date. The entry point — read this first to know what was on the table.
- **`minutes.md`** — *what happened and what to do now*: which advisors were convened, the key
  decisions and recommendations, each artifact with a one-line note on what it is and how to use it,
  and the open questions / next steps. This is the scannable summary — read it instead of replaying
  the whole conversation.
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
