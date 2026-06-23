# Stage 3: Reconvene

## Purpose
Each participating advisor reviews all Stage 2 artifacts and delivers an updated view — integrating
others' insights, refining their position, and flagging new considerations.

## For Each Participating Advisor
Open a **fresh context window**. Load:
1. `../../../advisors/NN-name/CONTEXT.md` (or `../../../advisors-extended/NN-name/CONTEXT.md`)
2. `../00-brief.md`
3. `../01-initial-meeting/[advisor-slug].md`
4. `../02-artifacts/**` — all artifact files from all advisors

Then prompt: "The board has produced the artifacts above. Review them and deliver your updated view."

## Output
Save each advisor's reconvene response to this directory as `[advisor-slug].md`. Every response ends
with a `## Handoff` block.

## Final Synthesis
After **all** advisors finish, load all `[advisor-slug].md` files in this directory plus `../00-brief.md`,
and produce a board-level synthesis that:
- Summarizes the board's consensus on the core question
- Highlights agreement across advisors
- Surfaces remaining tensions or trade-offs
- Provides a prioritized, integrated action plan

Save the synthesis to `00-synthesis.md` in this directory.

## Completion
Complete when all reconvene responses exist and `00-synthesis.md` is written. The board session is
complete; all files in `01-initial-meeting/`, `02-artifacts/`, and `03-reconvene/` form the permanent record.
Update all checkboxes in `../CONTEXT.md`.
