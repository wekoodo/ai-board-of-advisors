# Board Process

This file describes how a full board session runs, and the two ways you can execute it.
It is harness-agnostic: it works with any AI agent that can read files and follow instructions.

## The Session Flow

**Round 0 — Brief.** Copy `sessions/_template/` to `sessions/YYYY-MM-DD-topic/` and fill in
`00-brief.md` with your question and context.

**Round 1 — Initial Meeting (`01-initial-meeting/`).** The board chair reads the brief, selects
the relevant advisors, and routes to each. Each advisor consults independently and saves its
response to `01-initial-meeting/[advisor-slug].md`, ending with a `## Handoff` block.

**Round 2 — Artifact Production (`02-artifacts/`) — optional.** Advisors whose Handoff listed
artifacts produce them, loading the brief, their own identity file, and their Round 1 handoff.
Output goes to `02-artifacts/[advisor-slug]/`.

**Round 3 — Reconvene (`03-reconvene/`) — optional, requires Round 2.** Each advisor reviews the
brief, its Round 1 handoff, and all artifacts, then produces an updated view. The board chair
synthesizes all reconvene outputs into `03-reconvene/00-synthesis.md`.

## Execution Modes

The flow above is identical regardless of how you execute it. **Prefer Delegated Mode when your
harness supports sub-agents; otherwise use Manual Mode.** The file structure, load lists, and outputs
are identical either way — a session run in delegated mode is indistinguishable from one run manually.

### Delegated Mode (preferred — when the harness supports sub-agents)

If your agent harness can dispatch sub-agents or parallel tasks, the board chair runs each advisor's
stage by sub-agent: it spawns **one sub-agent per advisor**, gives that sub-agent **only** the files
in that stage's load list, and has it write its output to the path the stage specifies. Advisors
within a single stage are independent, so their sub-agents can run in parallel.

This keeps the board chair's own context small: the chair holds the brief and each advisor's saved
output — the `## Handoff` block carries decisions forward — but never the full identity files,
references, and profile each advisor loads. That separation is what lets a multi-advisor, multi-round
session run without exhausting a single context window.

### Manual Mode (universal fallback — works everywhere)

When sub-agents aren't available, run each advisor in its own fresh context window. For each advisor
in a stage:
1. Load exactly the files that stage's load instructions list (advisor `CONTEXT.md`, the brief,
   shared config, profile, and — in later rounds — prior handoffs and artifacts).
2. Prompt the advisor for that stage's output.
3. Save the output to the path the stage specifies.
4. Advance to the next advisor, then the next stage, by hand.

This mode depends on no special features — only the ability to open a fresh context and read files.
