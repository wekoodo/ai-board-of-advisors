# Shared Conventions

This file is the single source of truth for how advisors express figures, end their responses,
and format their output. Every advisor loads it and follows it.

## Durable Figures Rule

Advice and reference material express **durable formulas, ratios, and relative guidance** —
the things that do not change year to year.

Any **concrete, year-specific figure** — contribution limits, tax brackets, standard deductions,
RMD ages, estate-tax exemptions, premium ranges, interest-rate assumptions — must be:

1. Labeled inline as **"illustrative — verify current-year value"**, and
2. Confirmed against the current-year value before the user relies on it.

Never present a stale dollar amount as current fact. When a calculation needs a current figure,
show the formula with the figure as a clearly-labeled illustrative input, then tell the user to
substitute the verified current-year number.

Example (correct):
> Max out the HSA if you are on a high-deductible plan. The limit is roughly $4,300 individual /
> $8,550 family *(illustrative — verify current-year value)*.

## Handoff Block Format

**When an advisor is convened as a sub-agent, it returns this block to the chair** as the
compact carrier of its result across the context boundary. In inline convening it is an
optional summary the chair may record. The block's format is unchanged:

```
## Handoff
- **Key decisions reached:** [conclusions and recommendations made this session]
- **Open questions:** [what remains unresolved or needs more information]
- **Action items:** [specific next steps for the client]
- **Artifacts to produce:** [documents/plans/analyses to create in Round 2, if any]
- **Files written:** [any files written to output/ this session, if any]
```

The Handoff block carries dense context forward between context windows without replaying the
whole conversation. It is required in standalone consultations and in every board-session round.

## Response Style

- Lead with the answer or recommendation, then support it
- Use **numbered lists** for sequential steps
- Use **tables** for comparisons
- Use clear section headers
- Prefer concrete, actionable guidance over general description
