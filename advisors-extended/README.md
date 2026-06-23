# Extended Advisors (`advisors-extended/`)

This folder holds **niche, specialist advisors**. They serve two purposes at once:

1. **Ready-to-use advisors.** Advisors 09 (Oil & Gas Specialist) and 10 (Self-Storage Investment
   Advisor) are fully built. You can consult them right now — standalone or as part of a board
   session — exactly like the eight core advisors in `advisors/`.
2. **Reference implementations of the extension pattern.** They are the worked example of how to add
   your own custom advisor. Study them alongside `advisors/_template/` to see a real, fleshed-out
   advisor built to spec.

## Why a separate folder?

Core generalist advisors (01–08) live in `advisors/`. Niche specialists live here in
`advisors-extended/`. The two folders sit at **the same depth** in the repository, which matters:

```
board-of-advisors/
├── _config/
├── advisors/            <- core advisors 01–08
│   ├── 01-financial-planner/
│   └── ...
└── advisors-extended/   <- niche advisors 09–10 (same depth)
    ├── 09-oil-gas-specialist/
    └── 10-storage-facility-advisor/
```

Because `advisors-extended/NN-name/` is at the same depth as `advisors/NN-name/`, **every relative
path inside an extended advisor is identical to a core advisor's** — `../../_config/...`,
`../../meetings/...`. Nothing changes. Do **not** add an extra `../`.

## How to add your own advisor

1. **Copy a starting point.** Either copy `advisors/_template/` (a clean, bracketed scaffold) or
   copy one of the built advisors here (`09-oil-gas-specialist/` or `10-storage-facility-advisor/`)
   if your new advisor is close in spirit. Place the copy in `advisors-extended/NN-your-slug/`,
   using the next available number and a short kebab-case slug.
2. **Fill in `CONTEXT.md`.** Write the Identity (credentials, mission, approach), keep the v2
   "Always load" list as-is, write the Process (analytical steps + cross-referrals to other advisors
   by number + slug), keep the Outputs Handoff reference, and adapt the Disclaimer to your domain.
3. **Fill in `references/CONTEXT.md` and `references/frameworks.md`.** Give your advisor the
   frameworks, checklists, and analytical tools it needs. Obey the durable-figures rule: express
   formulas and ratios, and label any concrete year-specific or market-specific figure
   "illustrative — verify current-year value."
4. **Keep `output/.gitkeep`.** It preserves the working-artifact directory in git; the contents of
   `output/` are gitignored.
5. **Register the advisor in the roster.** Add your new advisor (number, title, slug, one-line
   description) to the root `CONTEXT.md` roster so the board and standalone flows can find it. If it
   should participate in board sessions, also add it to `_config/shared/collaboration.md`.

## Path reminder

Extended advisors sit at the same depth as core advisors, so relative paths are unchanged:
`../../_config/shared/disclaimer.md`, `../../_config/shared/conventions.md`,
`../../meetings/[meeting-name]/00-brief.md`. If you nest your advisor deeper, you must adjust the
`../` count accordingly — but the standard `advisors-extended/NN-name/` placement needs no change.
