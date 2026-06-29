# Extended Advisors (`advisors-extended/`)

This folder holds **niche, specialist advisors**. They serve two purposes at once:

1. **Ready-to-use advisors.** Advisors 09 (Oil & Gas Specialist) and 10 (Self-Storage Investment
   Advisor) are fully built. The board chair can convene them in any meeting — alone, alongside
   each other, or with the core eight — exactly like the advisors in `advisors/`.
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
4. **Register the advisor in the roster.** Add your new advisor (number, title, slug, one-line
   description) to the root `CONTEXT.md` roster so the board chair can convene it. If it should be
   visible to the other advisors as a cross-referral target, also add it to
   `_config/shared/collaboration.md`.

## How to remove an advisor

Numbers are **stable identifiers, not sequence positions** — there is no code that counts
`01..N` or expects them to be contiguous. Deleting an advisor leaves a gap (e.g. removing 04
leaves `01, 02, 03, 05, …`), and that is fine. The thing that actually breaks is **dangling
cross-references**, since advisors refer to each other by number + slug. To remove an advisor cleanly:

1. **Delete the folder** (`advisors/NN-name/` or `advisors-extended/NN-name/`).
2. **Remove its roster row** from the root `CONTEXT.md`.
3. **Remove its row and any referral rules** from `_config/shared/collaboration.md`.
4. **Scrub cross-referrals** in any *other* advisor's `CONTEXT.md` Process section that pointed to
   it by number (e.g. "the Tax Strategist (02)").
5. **Leave the number gap. Do not renumber the survivors.** Treat numbers like database IDs:
   assigned once, never reused. When you add the next advisor, use the next *unused* number — not
   the gap. Renumbering would force renaming folders *and* rewriting every `(NN)` cross-reference
   across the repo, for a purely cosmetic gain.

## Path reminder

Extended advisors sit at the same depth as core advisors, so relative paths are unchanged:
`../../_config/shared/disclaimer.md`, `../../_config/shared/conventions.md`,
`../../_config/profile/`, `../../meetings/[meeting-name]/artifacts/`. If you nest your advisor
deeper, you must adjust the `../` count accordingly — but the standard `advisors-extended/NN-name/`
placement needs no change.
