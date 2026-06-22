# Board of Advisors — Product Requirements Document

**Date:** 2026-06-21
**Status:** Draft (v2 — regenerated) — Pending Implementation
**Source paper:** "Interpretable Context Methodology: Folder Structure as Agentic Architecture" (Van Clief & McDermott, arXiv:2603.16021)
**Supersedes:** `tmp/old-plan/2026-06-21-board-of-advisors-design.md` (v1)

> **v2 note:** This is a regenerated PRD produced on a higher-grade model, using the v1 PRD/plan as context. The core ICM architecture from v1 is preserved. v2 adds: distribution files (README, LICENSE), two fully-built niche advisors as extension examples, a harness-agnostic board-automation note, durable-figures and shared-conventions handling, advisor-output gitignore correction, and `git init` in the foundation. Changes are flagged inline with **[v2]**.

---

## 1. Overview

The Board of Advisors is a harness-agnostic, folder-structured AI advisory system. It gives any user access to a panel of elite virtual advisors — financial, legal, tax, business, investment, insurance, and estate planning — delivered through plain markdown files that any AI agent harness can read without code, dependencies, or build steps.

The system follows the **Interpretable Context Methodology (ICM)**: folder structure *is* the architecture. Every file answers exactly one question, and the hierarchy of files tells the agent where it is, what to do, and what to produce.

Users install it once, complete an onboarding interview that persists their personal and financial profile, and from that point forward every advisor session is pre-loaded with their context.

---

## 2. Goals

- Deliver a working Board of Advisors installable on any major agent harness (Claude Code, Codex, Gemini CLI, and others) with **no harness-specific dependency** in the core flow
- Follow ICM's five-layer context hierarchy faithfully, with targeted adaptations for the parallel/hybrid consultation model
- Support both simple single-advisor consultations and full multi-advisor board sessions with artifact production and reconvene rounds
- Persistent personal profile: onboarding interview runs once, profile is stored locally, all future sessions load it automatically
- Multi-user isolation: each installation is private; the repo structure updates without overwriting user data
- Distribute as a GitHub Template Repository — clone, onboard, use; zero dependencies
- **[v2]** Be presentable on GitHub for humans (README) and legally clear (LICENSE) from first commit
- **[v2]** Ship two ready-to-use niche advisors that double as the canonical "add your own advisor" example

## 3. Non-Goals (v1.0.0)

- No runtime code, APIs, or integrations — pure markdown (local helper scripts are permitted but not required by the core flow)
- No automated agent orchestration baked into the core; **[v2]** harness-native delegation is documented as an *optional* mode, described generically, never required
- No cloud sync or shared profiles across devices
- No web UI
- No advisor coverage beyond the 8 core + 2 niche advisors in this release

---

## 4. Advisor Roster — v1.0.0

Eight generalist advisors plus two niche advisors ship in v1.

### 4.1 Core advisors (`advisors/`)

Eight generalists, each housed in its own numbered folder. Numbering controls default sequence in full board sessions.

| # | Folder | Role |
|---|--------|------|
| 01 | `financial-planner` | Certified Financial Planner (CFP/CFA) — budgeting, retirement, wealth planning |
| 02 | `tax-strategist` | Tax Strategist / CPA — tax minimization, compliance, integration with financial plan |
| 03 | `corporate-attorney` | Corporate Attorney (JD) — entity formation, contracts, asset protection |
| 04 | `business-strategist` | Business Strategy Consultant (MBA/CMC) — growth, operations, market strategy |
| 05 | `investment-advisor` | Investment Advisor (CFA) — portfolio management, asset allocation, risk |
| 06 | `real-estate-advisor` | Real Estate Advisor (CCIM) — property investment, market analysis, valuation |
| 07 | `estate-planning-attorney` | Estate Planning Attorney (JD/CTFA) — wills, trusts, legacy planning |
| 08 | `insurance-specialist` | Insurance Specialist (CPCU/CIC) — personal and commercial insurance solutions |

### 4.2 Niche advisors (`advisors-extended/`) **[v2]**

Two specialist advisors, **fully built and usable out of the box**, living in a parallel `advisors-extended/` folder. They are identical in structure to core advisors and serve a second purpose: they are the worked example of how a user adds a custom advisor.

| # | Folder | Role |
|---|--------|------|
| 09 | `oil-gas-specialist` | Oil & Gas Industry Expert / Investment Specialist (CFA, P.Eng-Petroleum, ERP) — upstream/midstream/downstream, E&P, MLPs, energy infrastructure |
| 10 | `storage-facility-advisor` | Self-Storage Investment Advisor (CCIM, CPM, CFA) — site selection, development, operations, financing, portfolio strategy |

`advisors-extended/README.md` explains that these are ready to use and also serve as reference implementations for `advisors/_template/`.

---

## 5. Repository Structure

```
board-of-advisors/
├── README.md                          # [v2] Human-facing GitHub landing page
├── LICENSE                            # [v2] MIT
├── AGENTS.md                          # Layer 0: global identity (canonical)
├── CLAUDE.md                          # Thin wrapper → injects AGENTS.md
├── GEMINI.md                          # Thin wrapper → injects AGENTS.md
├── CONTEXT.md                         # Layer 1: board chair routing
├── .gitignore                         # Excludes profile, user sessions, advisor output
│
├── advisors/
│   ├── _template/                     # Copy this to add a custom advisor
│   │   ├── CONTEXT.md
│   │   └── references/
│   │       ├── CONTEXT.md
│   │       └── frameworks.md
│   ├── 01-financial-planner/
│   │   ├── CONTEXT.md                 # Layer 2: role identity + contract
│   │   ├── references/
│   │   │   ├── CONTEXT.md             # Layer 3: reference navigation
│   │   │   └── frameworks.md          # Domain frameworks (durable-figures rule)
│   │   └── output/                    # Layer 4: standalone artifacts (gitignored)
│   │       └── .gitkeep
│   ├── 02-tax-strategist/             # Same structure
│   ├── 03-corporate-attorney/
│   ├── 04-business-strategist/
│   ├── 05-investment-advisor/
│   ├── 06-real-estate-advisor/
│   ├── 07-estate-planning-attorney/
│   └── 08-insurance-specialist/
│
├── advisors-extended/                 # [v2] Built niche advisors + extension example
│   ├── README.md
│   ├── 09-oil-gas-specialist/         # Same structure as a core advisor
│   └── 10-storage-facility-advisor/   # Same structure as a core advisor
│
├── sessions/
│   ├── _template/                     # Copy this to start a new session
│   │   ├── CONTEXT.md
│   │   ├── 00-brief.md
│   │   ├── 01-initial-meeting/
│   │   │   └── CONTEXT.md
│   │   ├── 02-artifacts/
│   │   │   └── CONTEXT.md
│   │   └── 03-reconvene/
│   │       └── CONTEXT.md
│   ├── example-2026-business-sale/    # [v2] Worked example session (ships, not gitignored)
│   │   └── … (filled brief + sample Round 1 outputs)
│   └── YYYY-MM-DD-topic-slug/         # User-created sessions (gitignored)
│
└── _config/
    ├── CONTEXT.md                     # Config navigation
    ├── setup/
    │   ├── CONTEXT.md                 # Onboarding interview instructions
    │   ├── questionnaire.md           # Structured question bank
    │   └── onboarding.md             # Human-readable installation guide
    ├── shared/
    │   ├── disclaimer.md              # Legal/educational disclaimer (all advisors load)
    │   ├── collaboration.md           # How advisors cross-reference each other
    │   ├── ethics.md                  # Shared ethical guidelines
    │   ├── conventions.md             # [v2] Durable-figures rule + Handoff format
    │   └── board-process.md           # [v2] Board flow + manual/delegated modes
    └── profile/                       # Generated after onboarding (gitignored except CONTEXT.md)
        ├── CONTEXT.md                 # Profile navigation (ships)
        ├── personal.md                # (generated, gitignored)
        ├── financial.md
        ├── businesses.md
        ├── investments.md
        └── goals.md
```

---

## 6. ICM Five-Layer Context Hierarchy

| Layer | File(s) | Question answered | Token target |
|-------|---------|-------------------|-------------|
| 0 | `AGENTS.md` | Where am I? What is this? | ~800 |
| 1 | `CONTEXT.md` (root) | Where do I go? What do I do? | ~500 |
| 2 | `advisors/NN-name/CONTEXT.md` | Who am I? What do I do here? | 200–500 |
| 3 | `advisors/NN-name/references/` + `_config/shared/` | What domain knowledge and rules apply? | 500–2k |
| 4 | `advisors/NN-name/output/` or `sessions/…/` | What am I working with / producing? | varies |

Profile files (`_config/profile/`) load alongside Layer 2 as personalization context (Layer 2.5). Shared config (`_config/shared/`) is Layer 3 reference material — stable rules internalized as constraints.

---

## 7. File Content Specifications

### 7.1 `AGENTS.md` — Layer 0

1. What this repo is — one paragraph describing the Board of Advisors
2. Folder structure overview — how `advisors/`, `advisors-extended/`, `sessions/`, and `_config/` relate
3. Ground rules — all advice is educational, not personalized professional advice; pointer to `_config/shared/disclaimer.md`
4. Single operational instruction: "For any consultation, load `CONTEXT.md` next."

Written for both the agent harness and a human reading the repo. Stable.

### 7.2 `CLAUDE.md` / `GEMINI.md` — Platform Wrappers **[v2 robustness]**

Each contains:
- The harness's native include/import of `AGENTS.md` (`@AGENTS.md` for Claude Code; Gemini's native import for Gemini CLI)
- **A plain-text fallback line** that does not depend on include support: *"Canonical instructions for this project are in `AGENTS.md`. If it was not already loaded, read it now before proceeding."*
- Any platform-specific notes

No duplicated content. `AGENTS.md` is the single source of truth. The fallback guarantees correctness even if a harness does not process the include directive.

### 7.3 Root `CONTEXT.md` — Layer 1, Board Chair

1. **First-launch detection** — if `_config/profile/` has no profile files, run onboarding before anything else
2. **Advisor domain map** — core advisors (01–08) and extended advisors (09–10) with topic coverage
3. **Routing logic** — single advisor vs. full board session decision criteria
4. **Session management** — how to create a session folder; pointer to `_config/shared/board-process.md`
5. **Stage progression** — when to move Round 1 → artifacts → reconvene
6. **Profile loading instruction** — always load `_config/profile/` files when present

### 7.4 `advisors/NN-name/CONTEXT.md` — Layer 2, Role Contract

Standard structure for every advisor (core and extended):

```markdown
# [Role Title]

## Identity
[Credentials, expertise, professional background, mission — from original prompt, refined for ICM]

## Inputs
### Always load
- `../../_config/shared/disclaimer.md`
- `../../_config/shared/collaboration.md`
- `../../_config/shared/conventions.md`
- `../../_config/profile/` (all files, if profile exists)

### Load if standalone session
- `output/` (prior relevant artifacts, if any)

### Load if board session — Round 1
- `../../sessions/[session-name]/00-brief.md`

### Load if board session — Round 3 (reconvene)
- `../../sessions/[session-name]/00-brief.md`
- `../../sessions/[session-name]/01-initial-meeting/[your-slug].md`
- `../../sessions/[session-name]/02-artifacts/**`

### Load as needed
- `references/` (see `references/CONTEXT.md` for navigation)

## Process
[Analytical frameworks used, what they prioritize, how they integrate with other advisors,
 role-specific ethical considerations]

## Outputs
Every response ends with a Handoff section (format defined in `_config/shared/conventions.md`):

### Handoff
- Key decisions reached
- Open questions remaining
- Action items / artifacts to be produced (if any)
- Files written to output/ (if any)

## Disclaimer
[Advisor-specific framing of the shared disclaimer]
```

> **[v2] Note for `advisors-extended/`:** Relative paths are identical (`../../_config/…`, `../../sessions/…`) because `advisors-extended/NN-name/` sits at the same depth as `advisors/NN-name/`.

### 7.5 `references/CONTEXT.md` — Layer 3 Navigation

Lists reference files, what each contains, and when to load each. Prevents indiscriminate loading.

### 7.6 `_config/shared/disclaimer.md`

Standard disclaimer for all advisors: guidance is educational and general, not personalized professional advice; users must consult licensed professionals; no attorney-client, CPA-client, or advisor-client relationship is created. Single source of truth.

### 7.7 `_config/shared/collaboration.md`

How each advisor references other board members (core and extended). Lists all advisors with slugs and the common cross-advisor touchpoints (tax↔financial, tax↔corporate-attorney, financial↔investment, financial↔estate, real-estate↔tax, insurance↔estate, plus extended advisors' touchpoints — e.g., oil & gas ↔ investment/tax, storage ↔ real-estate/tax). Cross-referrals are mentioned naturally in responses, not as disclaimers.

### 7.8 `_config/shared/ethics.md`

Shared ethical guidelines: disclose limitations; never recommend specific securities/products by brand; always recommend licensed professional consultation for implementation; **never fabricate legal citations, tax code references, or case law — if uncertain, say so**; no conflicts of interest; escalate to "consult a professional" earlier for complex situations.

### 7.9 `_config/shared/conventions.md` **[v2 new]**

Single source of truth for cross-advisor output conventions:
- **Durable figures rule:** Reference material and advice express durable formulas, ratios, and relative guidance. Any concrete year-specific figure (contribution limits, tax brackets, RMD ages, standard deductions, premium ranges) is labeled *"illustrative — verify current-year value"* and the advisor must confirm the live number before relying on it. Frameworks must not present a stale dollar amount as current fact.
- **Handoff format:** the canonical `## Handoff` block structure that every advisor response ends with.
- **Response style:** numbered lists for sequential steps, tables for comparisons, clear section headers.

### 7.10 `_config/shared/board-process.md` **[v2 new, harness-agnostic]**

Describes the full board session flow once, plus two execution modes — written without naming any specific harness:
- **Manual mode (default, works on every harness):** run each advisor in a fresh context window, loading exactly the files listed in the stage's load instructions; save each output; advance stages by hand.
- **Delegated mode (optional):** *if your agent harness supports dispatching sub-agents or parallel tasks,* the board chair may run each advisor's stage automatically, providing each sub-agent only the files in that stage's load list. This is an optimization, not a requirement, and changes none of the file structure or outputs.

### 7.11 `_config/setup/questionnaire.md`

Structured question bank for onboarding, organized by domain: Personal, Employment, Business, Financial, Investments, Goals, Concerns. The agent asks conversationally, one domain at a time, and writes each completed profile file to `_config/profile/` as it goes.

### 7.12 Session `CONTEXT.md` — Stage Router

```markdown
# Session: [Topic Slug]
Created: YYYY-MM-DD

## Brief
See `00-brief.md`

## Advisors Participating
- [ ] 01-financial-planner
- [ ] 02-tax-strategist
[… core 01–08 …]
- [ ] 09-oil-gas-specialist        (extended)
- [ ] 10-storage-facility-advisor  (extended)

## Stages
- [ ] 01-initial-meeting
- [ ] 02-artifacts  (only if action items require it)
- [ ] 03-reconvene  (only if artifacts were produced)

## Execution
See `../../_config/shared/board-process.md` for manual vs. delegated modes.

## Stage Load Instructions
[per-stage file lists — see §8]
```

Checkboxes let the user track session state at a glance between context windows.

### 7.13 `README.md` (root) **[v2 new]**

The GitHub-facing landing page for humans:
- What the Board of Advisors is and who it's for (1–2 paragraphs)
- The advisor roster (core + extended) at a glance
- Install: "Use this template" → open in your agent harness → first launch runs onboarding
- Quick start: single-advisor consult vs. full board session (short examples)
- How the profile works and that it stays local (gitignored)
- How to add a custom advisor (point to `advisors/_template/` and the built `advisors-extended/` examples)
- Cross-harness compatibility note
- License (MIT)

### 7.14 `LICENSE` **[v2 new]**

Standard MIT license text.

### 7.15 `advisors-extended/README.md` **[v2 new]**

Explains that 09 and 10 are fully usable advisors *and* reference implementations of the `advisors/_template/` pattern; how to copy one to make your own.

---

## 8. Consultation Flow

### 8.1 Single Advisor (Standalone)

1. User opens `advisors/NN-name/` (or `advisors-extended/NN-name/`) and loads `CONTEXT.md`
2. Agent assumes the Layer 2 identity, loads shared config + profile, references as needed
3. Consultation proceeds in one context window
4. Output saved to the advisor's `output/` if the user wants to persist it (gitignored)
5. Every response ends with `## Handoff` for clean context-window transitions

### 8.2 Full Board Session

**Round 0 — Brief.** User copies `sessions/_template/` to `sessions/YYYY-MM-DD-topic/`, fills `00-brief.md`.

**Round 1 — Initial Meeting (`01-initial-meeting/`).** Board chair reads the brief, selects relevant advisors, routes. Each advisor consults in a clean context window. Output: `01-initial-meeting/[advisor-slug].md`, ending with `## Handoff`.

**Round 2 — Artifact Production (`02-artifacts/`) — optional.** Advisors with action items produce artifacts in fresh windows, loading brief + own CONTEXT.md + their Round 1 handoff. Output to `02-artifacts/[advisor-slug]/`.

**Round 3 — Reconvene (`03-reconvene/`) — optional, requires Round 2.** Each advisor loads brief + Round 1 handoff + all artifacts, produces an updated view. Board chair synthesizes all reconvene outputs into `03-reconvene/00-synthesis.md`.

Manual or delegated execution per `_config/shared/board-process.md` — same files, same outputs either way.

### 8.3 Context Window Discipline

Each stage is a clean entry point. The session `CONTEXT.md` specifies exactly which files each stage loads. The `## Handoff` block carries dense context forward without replaying the conversation. Each new stage starts a clean window.

---

## 9. Onboarding & Persistent Profile

### 9.1 First-Launch Detection
Root `CONTEXT.md` checks `_config/profile/` for generated profile files. If absent, the agent runs onboarding before any advisory work.

### 9.2 Onboarding Interview
The agent follows `_config/setup/questionnaire.md` domain by domain, writing each profile file as its domain completes. Pause/resume supported (the agent checks which files already exist).

### 9.3 Profile Loading
Every advisor `CONTEXT.md` includes `_config/profile/**` in Inputs → Always load. Profile is Layer 2.5 — more specific than role identity, more stable than session inputs.

### 9.4 Multi-User Isolation
Generated profile files are gitignored (`_config/profile/CONTEXT.md` ships; the five data files do not). Each user's profile stays local. The repo updates upstream without touching profile data.

### 9.5 Profile Updates
Users can edit any profile file anytime. `_config/profile/CONTEXT.md` tracks a "Last Updated" per file; if older than 12 months, the agent flags possible staleness and offers to update.

---

## 10. Cross-Harness Compatibility

| Harness | Entry File | Notes |
|---------|-----------|-------|
| OpenAI Codex / most | `AGENTS.md` | Canonical source of truth |
| Claude Code | `CLAUDE.md` | Imports `AGENTS.md` + plain-text fallback |
| Gemini CLI | `GEMINI.md` | Imports `AGENTS.md` + plain-text fallback |
| Any other | `AGENTS.md` | Falls back cleanly |

No symlinks. Platform files are thin text wrappers using each harness's native include syntax **plus a plain-text fallback instruction** so injection never silently fails. **[v2]** The delegated board-session mode is described generically and depends on no specific harness.

---

## 11. Distribution & Installation

### 11.1 GitHub Template Repository
Configured as a GitHub Template. Users click "Use this template" for their own copy — no fork, no shared history. MIT license. **[v2]** `README.md` is the landing page; `LICENSE` ships at root.

### 11.2 Installation Steps
1. "Use this template" on GitHub (or clone)
2. Open in your agent harness
3. First launch: agent detects no profile, runs onboarding
4. Complete onboarding — profile written to `_config/profile/`
5. Use advisors standalone or via board sessions

### 11.3 Adding Custom Advisors
1. Copy `advisors/_template/` to `advisors/NN-my-advisor/` (or study the built `advisors-extended/` examples)
2. Fill in `CONTEXT.md` (identity, inputs, process, outputs)
3. Add the advisor to the root `CONTEXT.md` routing map
4. Optionally seed `references/`

### 11.4 Starting a New Session
1. Copy `sessions/_template/` to `sessions/YYYY-MM-DD-topic/`
2. Fill `00-brief.md`
3. Follow stage instructions in the session `CONTEXT.md`

### 11.5 Submodule Usage
Can be embedded in an existing project as a git submodule; `AGENTS.md`/`CLAUDE.md`/`GEMINI.md` work standalone or nested.

---

## 12. Version Roadmap

### v1.0.0 — This Spec
- 8 core generalist advisors + 2 built niche advisors (oil & gas, storage)
- Full ICM structure with profile onboarding
- README, LICENSE, worked example session
- GitHub Template distribution; harness-agnostic core with optional delegated mode

### v1.x — Community Extensions
- Additional niche advisors contributed via the `advisors-extended/` pattern
- Documented contribution guide

### Future Consideration
- Session index file for navigating past sessions
- Profile versioning / change history
- Optional local helper scripts for session scaffolding

---

## 13. Implementation Notes (for the plan)

The plan derives from this PRD as ~11 iterations, each driven by a self-contained kickoff prompt and run in a fresh session via the regenerated `run-iterations.ps1`:

1. **Foundation** — `git init`, `.gitignore` (profile + user sessions + advisor output), `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `LICENSE`, initial `README.md`
2. **Shared config** — `_config/CONTEXT.md`, `disclaimer.md`, `collaboration.md`, `ethics.md`, `conventions.md`, `board-process.md`
3. **Onboarding & profile** — setup `CONTEXT.md`, `questionnaire.md`, `onboarding.md`, profile `CONTEXT.md`
4. **Board chair** — root `CONTEXT.md` (references extended advisors + execution modes)
5. **Advisor template + financial planner (01)**
6. **Advisors 02–04**
7. **Advisors 05–08**
8. **Niche advisors 09–10** (`advisors-extended/` + its README)
9. **Session system** — `sessions/_template/` (all three stages)
10. **README polish + worked example session** (`sessions/example-…/`) — the example MUST be entirely fictional (invented persona, company, figures); it must not reference any real person, company, or transaction
11. **Integration review** — path audit (incl. `advisors-extended/` depth), placeholder scan, token-count check, gitignore verification, cross-harness wrapper check

### Global constraints carried into the plan
- `.gitignore` must exclude the five generated profile files, user session folders (`sessions/????-??-??-*/`), and advisor working artifacts (`advisors/**/output/*`, `advisors-extended/**/output/*`) while preserving each `.gitkeep`, `sessions/_template/`, and the shipped example session
- `AGENTS.md` is canonical; wrappers carry zero duplicated content but include the plain-text fallback
- All advisor `CONTEXT.md` files follow §7.4 exactly; relative paths resolve from each advisor's own folder (core and extended advisors are at equal depth)
- Every advisor response ends with the `## Handoff` block defined in `conventions.md`
- Reference files obey the durable-figures rule from `conventions.md`
- Token targets: Layer 0 ~800, Layer 1 ~500, Layer 2 200–500
```
