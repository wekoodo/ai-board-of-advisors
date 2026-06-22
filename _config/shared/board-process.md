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

The flow above is identical regardless of how you execute it. Choose the mode your tools support.

### Manual Mode (default — works everywhere)

Run each advisor in its own fresh context window. For each advisor in a stage:
1. Load exactly the files that stage's load instructions list (advisor `CONTEXT.md`, the brief,
   shared config, profile, and — in later rounds — prior handoffs and artifacts).
2. Prompt the advisor for that stage's output.
3. Save the output to the path the stage specifies.
4. Advance to the next advisor, then the next stage, by hand.

This mode depends on no special features — only the ability to open a fresh context and read files.

### Delegated Mode (optional)

*If your agent harness supports dispatching sub-agents or parallel tasks,* the board chair may run
each advisor's stage automatically: it spawns a sub-task per advisor, gives that sub-task **only**
the files in that stage's load list, collects the output, and saves it to the same path.

This is an optimization, not a requirement. It changes none of the file structure, load lists, or
outputs — a session run in delegated mode is indistinguishable from one run manually.
