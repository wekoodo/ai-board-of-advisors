# Board of Advisors

The Board of Advisors is a harness-agnostic AI advisory system built as pure markdown files — no code, no dependencies, no build step. It gives a single user access to a panel of elite virtual advisors covering financial planning, tax, law, business strategy, investing, real estate, estate planning, and insurance, plus two ready-to-use niche specialists. The system follows the **Interpretable Context Methodology (ICM)**: every file answers exactly one question, and the folder hierarchy *is* the architecture — telling the agent where it is, what to do, and what to produce. Eight core generalist advisors live in `advisors/`, two fully-built niche advisors live in `advisors-extended/`, and shared rules, the onboarding interview, and the local user profile live in `_config/`. Any AI agent harness that can read text files can run this system.

## Folder Structure

**`advisors/`** — Eight core generalist advisors, each in its own numbered folder:

- `01-financial-planner/` — Certified Financial Planner (CFP/CFA): budgeting, retirement, wealth planning
- `02-tax-strategist/` — Tax Strategist / CPA: tax minimization, compliance, integration with the financial plan
- `03-corporate-attorney/` — Corporate Attorney (JD): entity formation, contracts, asset protection
- `04-business-strategist/` — Business Strategy Consultant (MBA/CMC): growth, operations, market strategy
- `05-investment-advisor/` — Investment Advisor (CFA): portfolio management, asset allocation, risk
- `06-real-estate-advisor/` — Real Estate Advisor (CCIM): property investment, market analysis, valuation
- `07-estate-planning-attorney/` — Estate Planning Attorney (JD/CTFA): wills, trusts, legacy planning
- `08-insurance-specialist/` — Insurance Specialist (CPCU/CIC): personal and commercial coverage

Each advisor folder contains `CONTEXT.md` (role identity and contract), `references/` (domain frameworks, loaded on demand), and `output/` (working artifacts; gitignored).

**`advisors-extended/`** — Two fully-built niche advisors that ship ready to use **and** serve as the worked "add your own advisor" example:

- `09-oil-gas-specialist/` — Oil & Gas Industry Expert (CFA, P.Eng-Petroleum, ERP): upstream/midstream/downstream, E&P economics, MLPs, energy infrastructure
- `10-storage-facility-advisor/` — Self-Storage Investment Advisor (CCIM, CPM, CFA): site selection, development, operations, financing, portfolio strategy

The structure is identical to a core advisor and the folder sits at the same depth, so all relative paths into `_config/` and `sessions/` resolve identically for core and extended advisors.

**`sessions/`** — Holds the session template and your board-session folders. A session is a date-slug folder (`YYYY-MM-DD-topic/`) and follows a three-stage model:

- `01-initial-meeting/` — Round 1: each selected advisor weighs in
- `02-artifacts/` — Round 2 (optional): advisors produce concrete deliverables when action items require it
- `03-reconvene/` — Round 3 (optional, requires Round 2): advisors review artifacts and the board chair synthesizes

A shipped `_template/` is copied to start each new session. A fully fictional `example-…/` session also ships as a worked reference.

**`_config/`** — Shared rules and personalization:

- `shared/` — disclaimer, advisor collaboration map, ethics, output conventions (durable-figures rule, Handoff format), and the board-session process (manual and optional delegated modes)
- `setup/` — the onboarding interview that runs on first launch
- `profile/` — the locally generated personal, financial, business, investment, and goals profile (gitignored; only `CONTEXT.md` ships)

## Ground Rules

- All guidance produced by this system is **educational and general** — it is not personalized professional advice.
- Users must consult licensed professionals (CPAs, attorneys, fiduciary financial advisors, licensed insurance agents) before implementing any recommendation.
- Using this system creates **no** attorney-client, CPA-client, or financial-advisor-client relationship.
- The full disclaimer lives at `_config/shared/disclaimer.md` and is loaded by every advisor on every consultation.

## Getting Started

To begin, load `CONTEXT.md`. On first launch — before any profile exists — `CONTEXT.md` routes the agent to the onboarding interview, which writes the user's profile to `_config/profile/`. Every subsequent session then pre-loads that profile automatically, so each advisor opens with full personal and financial context already in hand.
