# Board of Advisors

A panel of elite virtual advisors — financial, tax, legal, business, investment, real estate, estate, and insurance — delivered as pure markdown that any AI agent harness can read. No code, no dependencies, no build step. Complete a one-time onboarding interview, and every future session opens with your full personal and financial context already in hand.

Built for individuals — operators, business owners, investors — who want a thinking partner across the full surface area of their financial and business life, without paying eight different professionals to assemble around the same table.

**Current product version:** see [`_config/shared/version.md`](_config/shared/version.md) · **Changes:** [`CHANGELOG.md`](CHANGELOG.md)

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

---

## Use vs contribute (two doors)

These are **different** GitHub paths. Pick the one that matches your goal.

| Goal | Use this | Why |
|------|----------|-----|
| **Run your own board** (profile, meetings, private life context) | **[Use this template](https://github.com/wekoodo/ai-board-of-advisors/generate)** | Creates *your* independent repo. Best for daily use. Private repos feel natural. Your instance is not framed as a fork of the product. |
| **Improve the product for everyone** (fix advisors, docs, protocol) | **[Fork](https://github.com/wekoodo/ai-board-of-advisors/fork)** the product repo | Clear contribution path: branch → PR into the canonical project. Use a **clean** workspace with no real profile or meeting data. |

**Do not** open pull requests from a personal board that contains real financial profile or meeting content. Contribute from a fork (or clean clone) of the product only.

Adding a git remote named `upstream` on a **personal board** only enables **pulling system updates**. It does **not** turn your board into a fork, share your history with the product, or upload gitignored profile/meetings.

---

## Install (personal board)

1. On GitHub, click **[Use this template](https://github.com/wekoodo/ai-board-of-advisors/generate)** to create your own copy (private recommended).
2. Clone *your* repo and open it in your AI agent harness (Claude Code, Codex, Gemini CLI, or any harness that reads project markdown).
3. On first launch the agent detects no profile and runs the onboarding interview. Answer the questions; your profile gets written to `_config/profile/`.
4. Near the end of onboarding, the agent offers to **connect product updates** — adding an `upstream` remote that points at this product repo. Accepting is recommended so the board can notice new releases later. You can also ask anytime: “connect product updates.”

No build step, no package install, no API keys.

### Contribute instead

```bash
# Fork on GitHub, then:
git clone https://github.com/<you>/ai-board-of-advisors.git
cd ai-board-of-advisors
git remote add upstream https://github.com/wekoodo/ai-board-of-advisors.git
# branch, change system files only, open a PR against wekoodo/ai-board-of-advisors
```

---

## Talk to your board

Open the project in your AI agent harness and load `CONTEXT.md`. Ask your question — the board chair convenes the relevant advisor(s), they respond in character, and the chair produces artifacts (worksheets, plans, checklists) as the conversation needs them. Those artifacts are real files under `meetings/<meeting>/artifacts/` that you can read and edit while the meeting is still running; the advisors will react to your edits. The chair keeps a small record of each meeting — a `brief.md` (what you asked), a `minutes.md` (the decisions and how to use each artifact), and the `artifacts/` themselves; ask to keep the full `transcript.md` only when you want the complete back-and-forth.

Consulting a single advisor is just a meeting with one voice convened — there is no separate mode.

At most **once a day** (or whenever you ask “any updates?”), the chair soft-checks for **product updates** — only when `upstream` is set and the network/git allow it. If something newer is available, you get a short one-line notice; the meeting is never blocked. Most sessions run no check at all.

## Keeping your board up to date

GitHub **does not** notify template-created repos when the product changes. Personal boards stay current by merging from `upstream`.

| Piece | Role |
|-------|------|
| [`_config/shared/version.md`](_config/shared/version.md) | Version stamp + soft-check steps (loaded for a check — at most once a day, or on request) |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each product release |
| [`_config/shared/updates.md`](_config/shared/updates.md) | Connect upstream / apply merge — loaded only when you update or connect |

**Typical flow**

1. Onboarding (or “connect product updates”) adds:
   `git remote add upstream https://github.com/wekoodo/ai-board-of-advisors.git`
2. On the day's first meeting (at most once a day), the chair may notice: local `0.1.0` → upstream `0.2.0` (example).
3. You say you want to update. The agent shows **commands to run yourself** and offers to **apply the merge for you** (with your consent — never auto-merge).

**Do it yourself**

```bash
git fetch upstream
git merge upstream/main
```

**What merges vs what stays local**

| Updated from the product (system) | Stays on your machine (gitignored) |
|-----------------------------------|-------------------------------------|
| Advisors, shared rules, chair protocol, examples, docs | Profile (`_config/profile/`), your meetings, `_inbox/` docs |

If you customized **system** files in place, merges can conflict — prefer adding new advisors under `advisors-extended/` over editing core files. Full detail: [`_config/shared/updates.md`](_config/shared/updates.md).

## Your profile stays local

The onboarding interview writes your personal, financial, business, investment, and goals data into `_config/profile/`. Those files are listed in `.gitignore`. They never get committed, never leave your machine, and never sync upstream. Merging product updates does not require or overwrite them.

## Add your own advisor

Two ways:

- Copy `advisors/_template/` to `advisors/NN-your-advisor/` and fill in the identity, inputs, process, and outputs sections of `CONTEXT.md`.
- Or study the built `advisors-extended/09-oil-gas-specialist/` and `advisors-extended/10-storage-facility-advisor/` — they are complete advisor implementations and double as the canonical "how to add a custom advisor" reference.

Then add your new advisor to the roster in the root `CONTEXT.md` so the board chair knows it exists. See also [`advisors-extended/README.md`](advisors-extended/README.md).

## Cross-harness

`AGENTS.md` is the canonical identity file and works on any harness that reads project markdown. `CLAUDE.md` and `GEMINI.md` are thin wrappers that natively import `AGENTS.md` and include a plain-text fallback line so the canonical content gets loaded even when the import directive isn't honored. The core flow has no harness-specific dependency.

## License

MIT — see [LICENSE](LICENSE).
