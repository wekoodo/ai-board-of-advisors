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

Two shipped example sessions — both fully fictional personas, and both **actually produced by running the system end-to-end** (in delegated/sub-agent mode), not hand-authored:

- [`sessions/example-2026-emergency-fund/`](sessions/example-2026-emergency-fund/) — the simplest path: a single advisor (Financial Planner) resolving a one-domain question in a single round.
- [`sessions/example-2026-rental-property/`](sessions/example-2026-rental-property/) — the full natural flow: a two-advisor initial meeting (Real Estate Advisor + Financial Planner), Round 2 artifacts (an affordability/reserves worksheet and a deal-screen + due-diligence checklist), and a Round 3 reconvene closing with a board synthesis.

## Install

1. On GitHub, click **Use this template** to create your own copy of the repo.
2. Open the repo in your AI agent harness (Claude Code, Codex, Gemini CLI, or any other harness that reads project markdown).
3. On first launch the agent detects no profile and runs the onboarding interview. Answer the questions; your profile gets written to `_config/profile/`.

No build step, no package install, no API keys.

## Quick start

**Single-advisor consult.** Open `advisors/NN-name/` (e.g. `advisors/02-tax-strategist/`) and tell your agent to load `CONTEXT.md`. The advisor assumes its role, loads your profile, and answers in-character. Add a `## Handoff` block to capture decisions you want to carry forward.

**Full board session.** Start at the repository root by loading `CONTEXT.md`. The board chair routes the topic. Copy `sessions/_template/` to a date-slug folder (e.g. `sessions/2026-06-21-business-sale/`), fill in `00-brief.md`, and run the three stages — initial meeting, optional artifacts, optional reconvene — per the session's stage instructions.

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
