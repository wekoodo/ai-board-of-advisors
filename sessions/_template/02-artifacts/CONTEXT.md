# Stage 2: Artifact Production

## Purpose
Advisors who identified deliverables in their Stage 1 Handoff produce them here — financial
projections, legal outlines, strategic plans, checklists, analyses.

## Who Participates
Only advisors whose Stage 1 Handoff listed "Artifacts to produce." Not all advisors run Stage 2.

## For Each Participating Advisor
Open a **fresh context window**. The Handoff block is the bridge — do not carry Stage 1 context. Load:
1. `../../../advisors/NN-name/CONTEXT.md` (or `../../../advisors-extended/NN-name/CONTEXT.md`)
2. `../00-brief.md`
3. `../01-initial-meeting/[advisor-slug].md`

Then prompt: "In Stage 1 you identified [artifact(s)] to produce. Produce them now."

## Output
Save artifacts to a subdirectory named after the advisor: `[advisor-slug]/[artifact-name].md`
(e.g., `tax-strategist/entity-tax-comparison.md`). Name files descriptively; one file per artifact.

## Completion
Complete when all advisors with identified artifacts have produced them. Proceed to Stage 3.
Update the checkboxes in `../CONTEXT.md`.
