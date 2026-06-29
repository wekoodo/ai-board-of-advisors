# Routed Context Patterns

This reference distills Interpretable Context Methodology (ICM) into reusable project guidance. Use it to design, audit, or refactor folder-based context systems for AI agents.

## Fit Criteria

Use routed context when the work is:

- Reviewable: a human should inspect or edit the artifacts.
- Repeatable: the same process runs with different input.
- File-friendly: inputs, references, and outputs can live as readable files.

And it takes one of two shapes (see "Two Valid Shapes" below):

- Sequential: step 2 follows step 1 → a **stage pipeline**.
- Selective: a roster of roles/specialists/domains chosen by topic → a **reference library**.

Avoid using routed context alone when the workflow needs:

- Real-time agent-to-agent message passing.
- High-concurrency multi-user execution.
- Automated branching based on model decisions (a human branching between steps is fine).
- Hidden state that cannot be represented as files.

## Two Valid Shapes

ICM as published describes the **stage pipeline**. The same five layers also support a **reference library**, and mistaking one for the other is the most common audit error.

| | Stage pipeline | Reference library (roster) |
| --- | --- | --- |
| Folder | `stages/01_research/`, `02_draft/` … | `advisors/01-name/`, `02-name/` … |
| Numbering means | Execution order | Stable identity (not order) |
| Members run | In sequence | Selected per run by topic |
| Layer | Each member is a **Layer 2** stage contract | The library is **Layer 3** reference material |
| Member contract | `Inputs`/`Process`/`Outputs` | Role identity + domain frameworks |

**A numbered folder is not automatically a stage.** If members are selected by topic rather than run in order, the directory is a Layer-3 library — the absence of `stages/` is not a defect.

A project may have a pipeline, a library, both, or neither. A live "board meeting" system, for example, is pure ICM: Layer 2 is the meeting lifecycle (intake → deliberation → minutes), Layer 3 is the advisor roster *library* selected per topic, Layer 4 is the per-meeting artifacts. Selecting which advisors to convene is the controlling stage scoping its Inputs — core ICM, not an extension. The conversational feel of deliberation is an execution-style choice, not an architectural violation.

## Five-Layer Hierarchy

| Layer | Role | Typical Files | Agent Question |
| --- | --- | --- | --- |
| 0 | Global identity and harness routing | `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` | Where am I? |
| 1 | Workspace routing | `CONTEXT.md`, `CONTEXT-MAP.md` | Where do I go? |
| 2 | Stage contract (control point) | `stages/NN_slug/CONTEXT.md` | What do I do? |
| 3 | Stable reference material (incl. roster libraries) | `_config/`, `references/`, `shared/`, `advisors/` | What rules apply? |
| 4 | Working artifacts | `input/`, `output/`, `meetings/`, `handoffs/`, generated `.md`/`.json` | What am I working with? |

Layer 3 is the factory: stable constraints, style guides, domain rules, roster libraries, examples, and setup decisions.

Layer 4 is the product: source input, stage outputs, handoffs, drafts, audit files, and other per-run artifacts.

Keep Layer 3 and Layer 4 visibly separate so agents know what to follow as a constraint and what to transform as input.

**Layer 2 is the control point.** Its Inputs table names the exact Layer-3 and Layer-4 files to load *and the relevant sections of each*, so the agent neither loads the whole repo nor guesses. This is also what the orchestrator reads to scope context for any sub-agents it spawns: the folder structure does double duty — the human's control surface and the model's delegation spec.

**Token budget (a design check).** Scoped loading keeps each step small: Layers 0–2 ≈ 1.3–1.6k tokens, Layer 3 ≈ 0.5–2k scoped to the step, total ≈ 2–8k per step — versus a monolithic prompt that loads everything (30–50k, much of it irrelevant). If a step's context blows past ~8k, that is the signal to re-scope its Inputs, not to raise the budget.

**Recursive routing.** A large reference collection may carry its own `CONTEXT.md` router that points to the right files within it — the Layer-1 routing pattern applied inside Layer 3 (e.g. `advisors/01-name/references/CONTEXT.md`).

**In-workspace memory.** Persist durable memory as files inside the workspace — stable facts/preferences as Layer 3, evolving state as Layer 4 — not in a harness's private user-level store. Otherwise the project stops being portable: move it to another harness and the memory does not travel.

## Minimal Project Context Layout

Use this when a repo needs durable agent context but not a stage pipeline yet:

```text
project/
  AGENTS.md
  CLAUDE.md
  CONTEXT.md
  docs/
    agents/
      issue-tracker.md
      domain.md
      triage-labels.md
  handoffs/
```

Rules:

- Make one file canonical for Layer 0. Tool-specific files may be thin shims.
- Put task routing and "what to read next" in Layer 1.
- Put durable domain rules in references or `docs/agents/`.
- Put resumable working state in `handoffs/`, not chat history.

## Stage Pipeline Layout

Use this when the project has a repeated multi-step workflow:

```text
workspace/
  AGENTS.md
  CONTEXT.md
  stages/
    01_research/
      CONTEXT.md
      references/
      output/
    02_draft/
      CONTEXT.md
      references/
      output/
    03_review/
      CONTEXT.md
      references/
      output/
  _config/
  shared/
  setup/
    questionnaire.md
```

Rules:

- Number stages to encode execution order.
- Keep each stage to one job.
- Let each `output/` folder become the next stage's Layer 4 input.
- Keep stable cross-stage preferences in `_config/` or `shared/`.
- Use per-stage `references/` for stable material that only applies to one stage.

## Reference Library Layout

Use this when the project has a roster of roles/specialists/domains selected by topic (Layer 3), with a controlling stage that convenes them:

```text
workspace/
  AGENTS.md
  CONTEXT.md          <- Layer 1 router: convenes the right members per request
  advisors/
    01-name/
      CONTEXT.md       <- role identity + process (NOT a sequential stage)
      references/
        CONTEXT.md     <- optional recursive router
        frameworks.md
    02-name/ ...
  _config/             <- shared rules, setup, profile (Layer 3)
  meetings/            <- Layer 4: per-run artifacts (brief, artifacts, minutes)
    <topic>/
```

Rules:

- Numbers are stable identities, not order. Never renumber survivors after a deletion; leave the gap and scrub cross-references (members refer to each other by number + slug).
- Keep each member to one role with one contract.
- The controlling stage (often Layer 1 + a meeting lifecycle) selects which members to load — that selection is Inputs scoping, not pipeline branching.
- Per-run artifacts go in a Layer-4 area (`meetings/`, `output/`), never inside member folders.

## Stage Contract Template

```markdown
# 02 Draft

## Purpose

Transform the research output into a draft using the configured voice and structure.

## Inputs

| Layer | Path | Use |
| --- | --- | --- |
| Layer 4 working | `../01_research/output/research.md` | Source material to transform |
| Layer 3 reference | `../../_config/voice.md` | Voice and tone constraints |
| Layer 3 reference | `references/structure.md` | Draft structure rules |

## Process

1. Read only the listed inputs.
2. Convert the research into a draft.
3. Apply the voice and structure constraints.
4. Preserve unresolved questions in a final notes section.

## Outputs

- Write `draft.md` to `output/`.

## Review Gate

Stop after writing the output. The human may edit `output/draft.md` before the next stage runs.

## Verify

- Confirm the draft reflects the research claims.
- Confirm all required sections from `references/structure.md` are present.
```

`Verify` is optional, but useful for cross-stage trace checks and final alignment passes.

## Design Rules

- Prefer explicit scoped file lists over broad repo reads.
- Keep stage outputs readable, diffable, and editable.
- Use Markdown contracts as both instructions and human documentation.
- Use local scripts for fetching, formatting, moving files, rendering, or other deterministic steps.
- Let humans branch between stages when judgment is needed.
- When a user repeatedly edits the same kind of output, change the source contract or reference file.

## Anti-Patterns

- One giant prompt or context file that every task loads.
- Stage contracts that say "read everything relevant" instead of naming inputs.
- Stable guidance mixed into per-run output folders.
- Per-run drafts mixed into reference folders.
- Tool-specific projection folders used as the only source of truth.
- Binary-only intermediate artifacts with no readable summary.
- Hidden state that exists only in chat history.

## Validation Checklist

- A canonical Layer 0 entrypoint exists (tool-specific files are shims).
- Layer 1 tells agents where to go for common tasks.
- The Layer-2 shape is identified: pipeline, library, both, or neither — a library is not flagged for lacking `stages/`.
- Every numbered stage (pipeline) or member (library) has a `CONTEXT.md`.
- Every stage contract has `Inputs`, `Process`, and `Outputs`; Inputs name files *and sections*, distinguishing Layer 3 from Layer 4.
- Every stage writes to a reviewable output location.
- Stable references/rosters (Layer 3) and working outputs (Layer 4) are in separate folders.
- Durable memory lives in the workspace, not a harness-private store.
- Per-step delivered context stays roughly within the 2–8k token budget.
- The layout can be copied, committed, and understood without a custom framework.
