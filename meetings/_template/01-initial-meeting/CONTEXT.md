# Stage 1: Initial Meeting

## Purpose
Each participating advisor delivers an initial analysis based on the brief. First-pass round —
each advisor works independently without seeing the others' responses.

## For Each Participating Advisor
Open a **fresh context window** for each advisor. Load in this order:
1. `../../../advisors/NN-name/CONTEXT.md` — for an extended advisor use `../../../advisors-extended/NN-name/CONTEXT.md`
2. `../00-brief.md`
3. `../../../_config/shared/disclaimer.md`
4. `../../../_config/shared/collaboration.md`
5. `../../../_config/shared/conventions.md`
6. `../../../_config/profile/` — all files, if profile exists

Then prompt: "You are [Advisor Name]. Read the brief and deliver your initial analysis and recommendations."

## Output
Save each advisor's response to this directory as `[advisor-slug].md` (e.g., `financial-planner.md`).
**Every response must end with a `## Handoff` block** (format in `../../../_config/shared/conventions.md`).

## Completion
Stage 1 is complete when all participating advisors have responses saved here.
- If any Handoff listed artifacts to produce → proceed to Stage 2.
- If none → Stage 3 can proceed with notes, or the session ends here.

Update the checkboxes in `../CONTEXT.md` when this stage is complete.
