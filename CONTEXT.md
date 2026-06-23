# Board of Advisors — Board Chair

## First Launch Check

Before anything else, check for your profile:
- If `_config/profile/` contains no profile files, run the onboarding interview first.
  Load `_config/setup/CONTEXT.md` to begin. Return here when onboarding is complete.
- If profile files exist, proceed below.

---

## Advisor Roster

**Core advisors** (`advisors/NN-name/`):

| # | Advisor | Topics |
|---|---------|--------|
| 01 | `financial-planner` | Budgeting, cash flow, retirement, wealth management, debt strategy |
| 02 | `tax-strategist` | Income tax minimization, entity tax treatment, deductions, compliance, estimated taxes |
| 03 | `corporate-attorney` | Entity formation, operating agreements, contracts, asset protection, business law |
| 04 | `business-strategist` | Growth strategy, market analysis, operations, competitive positioning, scaling |
| 05 | `investment-advisor` | Portfolio management, asset allocation, risk, rebalancing, tax-efficient investing |
| 06 | `real-estate-advisor` | Property investment, market analysis, cap rates, 1031 exchanges, due diligence |
| 07 | `estate-planning-attorney` | Wills, trusts, beneficiary designations, powers of attorney, legacy planning |
| 08 | `insurance-specialist` | Life, disability, health, property, business, umbrella, and cyber insurance |

**Extended advisors** (`advisors-extended/NN-name/` — built and ready to use):

| # | Advisor | Topics |
|---|---------|--------|
| 09 | `oil-gas-specialist` | Upstream/midstream/downstream, E&P economics, MLPs, energy infrastructure investing |
| 10 | `storage-facility-advisor` | Self-storage site selection, development, operations, financing, portfolio strategy |

---

## Routing

### Single Advisor
Use when the question falls clearly within one domain.
Load `advisors/NN-name/CONTEXT.md` (or `advisors-extended/NN-name/CONTEXT.md`) directly.

Example: a Roth conversion timing question → `advisors/02-tax-strategist/CONTEXT.md`.

### Full Board Session
Use when the question spans two or more domains, the decision is major (business formation,
real estate investment, retirement transition, estate plan, business sale), or you want multiple
independent perspectives.

To start a board session:
1. Copy `meetings/_template/` to `meetings/YYYY-MM-DD-topic/`
2. Fill in `meetings/YYYY-MM-DD-topic/00-brief.md`
3. Load `meetings/YYYY-MM-DD-topic/CONTEXT.md` and follow the stage instructions

---

## Session Stages

Full board sessions progress through up to three stages. Each stage runs in a clean context window.

| Stage | Purpose | When |
|-------|---------|------|
| `01-initial-meeting/` | Each advisor delivers initial analysis | Always (Round 1) |
| `02-artifacts/` | Advisors produce specific documents or plans | If advisors identified action items |
| `03-reconvene/` | Advisors review artifacts and integrate | Only if artifacts were produced |

Every advisor response ends with a `## Handoff` block (format in `_config/shared/conventions.md`),
which carries context cleanly between stages. For manual vs. delegated execution of these stages,
see `_config/shared/meeting-process.md`.

### Execution

When your harness supports sub-agents, **prefer Delegated Mode**: dispatch one sub-agent per advisor
per stage, handing each only that stage's load list, and let it write its own output file. You (the
board chair) then read only the saved `## Handoff` blocks to drive the next round — keeping your
context small even across long, multi-advisor meetings. Fall back to **Manual Mode** (one fresh
context window per advisor) only when sub-agents aren't available. Details in
`_config/shared/meeting-process.md`.

---

## Profile

Always load `_config/profile/` files alongside the advisor's `CONTEXT.md`. They provide your
persistent personal and financial context. Advisors flag profile data older than 12 months.
If profile files are missing, run onboarding: `_config/setup/CONTEXT.md`.
