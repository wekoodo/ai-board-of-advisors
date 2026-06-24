# Board of Advisors

A panel of elite virtual advisors — financial, tax, legal, business, investment, real estate, estate, and insurance — delivered as pure markdown that any AI agent harness can read. No code, no dependencies, no build step. Complete a one-time onboarding interview, and every future session opens with your full personal and financial context already in hand.

Built for individuals — operators, business owners, investors — who want a thinking partner across the full surface area of their financial and business life, without paying eight different professionals to assemble around the same table.

## The Board

### Core advisors — `advisors/`

| # | Advisor | Topics |
|---|---------|--------|
| 01 | Financial Planner (CFP/CFA) | Budgeting, retirement, wealth planning |
| 02 | Tax Strategist (CPA) | Tax minimization, compliance, planning integration |
| 03 | Corporate Attorney (JD) | Entity formation, contracts, asset protection |
| 04 | Business Strategist (MBA/CMC) | Growth, operations, market strategy |
| 05 | Investment Advisor (CFA) | Portfolios, asset allocation, risk |
| 06 | Real Estate Advisor (CCIM) | Property investment, market analysis, valuation |
| 07 | Estate Planning Attorney (JD/CTFA) | Wills, trusts, legacy planning |
| 08 | Insurance Specialist (CPCU/CIC) | Personal and commercial coverage |

### Extended advisors — `advisors-extended/`

| # | Advisor | Topics |
|---|---------|--------|
| 09 | Oil & Gas Specialist (CFA, P.Eng-Petroleum, ERP) | Upstream/midstream/downstream, E&P, MLPs, energy infrastructure |
| 10 | Storage Facility Advisor (CCIM, CPM, CFA) | Site selection, development, operations, financing, portfolio strategy |

The two extended advisors are fully usable today **and** serve as worked examples of how to add your own niche advisor. They sit in their own folder so the core roster stays focused.

## See it in action

Two worked examples ship with the repo as reference meeting records — each a small, routed set of files rather than one monolithic document. Personas, companies, and figures are fully fictional; year-specific numbers are labeled illustrative.

- **[`meetings/example-emergency-fund/`](meetings/example-emergency-fund/)** — *the simplest path.* Fictional Daniel asks how big his emergency fund should be and where to park it. The chair convenes a single advisor, the Financial Planner answers in one turn, and the user is satisfied. The record is just a [`brief.md`](meetings/example-emergency-fund/brief.md) and a [`minutes.md`](meetings/example-emergency-fund/minutes.md) — no artifact, no transcript needed.
- **[`meetings/example-rental-property/`](meetings/example-rental-property/)** — *the flagship.* Fictional Priya and Marcus weigh their first single-family rental. The [`minutes.md`](meetings/example-rental-property/minutes.md) is the scannable summary; the [`brief.md`](meetings/example-rental-property/brief.md) frames the question. The chair routes to the Real Estate Advisor and the Financial Planner, then commissions three artifacts: a [deal-screen + cash-flow worksheet](meetings/example-rental-property/artifacts/rental-deal-screen-worksheet.md), a [due-diligence and location checklist](meetings/example-rental-property/artifacts/due-diligence-and-location-checklist.md), and an [affordability & reserves worksheet](meetings/example-rental-property/artifacts/affordability-and-reserves-worksheet.md). **The user reviews the affordability worksheet, asks for a worked passing example, the Financial Planner revises the file in place, and the Real Estate Advisor reacts** — the collaborative-artifact loop the system is built around. Because they asked to keep it, the full [`transcript.md`](meetings/example-rental-property/transcript.md) is there too, for digging deeper.

## Install

1. On GitHub, click **Use this template** to create your own copy of the repo.
2. Open the repo in your AI agent harness (Claude Code, Codex, Gemini CLI, or any other harness that reads project markdown).
3. On first launch the agent detects no profile and runs the onboarding interview. Answer the questions; your profile gets written to `_config/profile/`.

No build step, no package install, no API keys.

## Talk to your board

Open the project in your AI agent harness and load `CONTEXT.md`. Ask your question — the board chair convenes the relevant advisor(s), they respond in character, and the chair produces artifacts (worksheets, plans, checklists) as the conversation needs them. Those artifacts are real files under `meetings/<meeting>/artifacts/` that you can read and edit while the meeting is still running; the advisors will react to your edits. The chair keeps a small record of each meeting — a `brief.md` (what you asked), a `minutes.md` (the decisions and how to use each artifact), and the `artifacts/` themselves; ask to keep the full `transcript.md` only when you want the complete back-and-forth.

Consulting a single advisor is just a meeting with one voice convened — there is no separate mode.

## Your profile stays local

The onboarding interview writes your personal, financial, business, investment, and goals data into `_config/profile/`. Those files are listed in `.gitignore`. They never get committed, never leave your machine, and never sync upstream. The repo can be updated freely without touching your profile.

## Add your own advisor

Two ways:

- Copy `advisors/_template/` to `advisors/NN-your-advisor/` and fill in the identity, inputs, process, and outputs sections of `CONTEXT.md`.
- Or study the built `advisors-extended/09-oil-gas-specialist/` and `advisors-extended/10-storage-facility-advisor/` — they are complete advisor implementations and double as the canonical "how to add a custom advisor" reference.

Then add your new advisor to the roster in the root `CONTEXT.md` so the board chair knows it exists.

## Cross-harness

`AGENTS.md` is the canonical identity file and works on any harness that reads project markdown. `CLAUDE.md` and `GEMINI.md` are thin wrappers that natively import `AGENTS.md` and include a plain-text fallback line so the canonical content gets loaded even when the import directive isn't honored. The core flow has no harness-specific dependency.

## License

MIT — see [LICENSE](LICENSE).
