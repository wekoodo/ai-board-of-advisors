# Session: [Topic Slug]
Created: YYYY-MM-DD

## Brief
See `00-brief.md` — fill this in before beginning.

## Advisors Participating
Check the advisors relevant to this session's question. Uncheck all others.

- [ ] 01-financial-planner
- [ ] 02-tax-strategist
- [ ] 03-corporate-attorney
- [ ] 04-business-strategist
- [ ] 05-investment-advisor
- [ ] 06-real-estate-advisor
- [ ] 07-estate-planning-attorney
- [ ] 08-insurance-specialist
- [ ] 09-oil-gas-specialist        (extended — in advisors-extended/)
- [ ] 10-storage-facility-advisor  (extended — in advisors-extended/)

## Stages
- [ ] 01-initial-meeting — always run for full board sessions
- [ ] 02-artifacts — only if advisors identified action items requiring documents
- [ ] 03-reconvene — only if artifacts were produced in Stage 2

## Execution
This session can be run in **manual** mode (default — works on any harness) or **delegated** mode
(if your harness supports sub-agents/parallel tasks). The flow, files, and outputs are identical
either way. See `../../_config/shared/board-process.md`.

## Stage Load Instructions

### Stage 1: Initial Meeting
For each participating advisor, open a fresh context window and load:
1. `../../advisors/NN-name/CONTEXT.md` — for an extended advisor use `../../advisors-extended/NN-name/CONTEXT.md`
2. `00-brief.md`
3. `../../_config/shared/disclaimer.md`
4. `../../_config/shared/collaboration.md`
5. `../../_config/shared/conventions.md`
6. `../../_config/profile/` — all files, if profile exists

Then prompt the advisor for their initial analysis.
**Output:** save each response to `01-initial-meeting/[advisor-slug].md`, ending with a `## Handoff` block.
See `01-initial-meeting/CONTEXT.md` for detail.

### Stage 2: Artifacts (optional)
For each advisor whose Handoff listed artifacts, open a fresh context window and load:
1. `../../advisors/NN-name/CONTEXT.md` (or `../../advisors-extended/NN-name/CONTEXT.md`)
2. `00-brief.md`
3. `01-initial-meeting/[advisor-slug].md`

**Output:** save artifacts to `02-artifacts/[advisor-slug]/[artifact-name].md`.
See `02-artifacts/CONTEXT.md` for detail.

### Stage 3: Reconvene (optional — requires Stage 2)
For each participating advisor, open a fresh context window and load:
1. `../../advisors/NN-name/CONTEXT.md` (or `../../advisors-extended/NN-name/CONTEXT.md`)
2. `00-brief.md`
3. `01-initial-meeting/[advisor-slug].md`
4. `02-artifacts/**`

Then prompt for their updated view, integrating all artifacts.
**Output:** save each response to `03-reconvene/[advisor-slug].md`. After all advisors finish, load
all `03-reconvene/` files and produce a board-level synthesis to `03-reconvene/00-synthesis.md`.
See `03-reconvene/CONTEXT.md` for detail.

## Session Complete
All responses in `01-initial-meeting/`, `02-artifacts/`, and `03-reconvene/` form the permanent
record of this session.
