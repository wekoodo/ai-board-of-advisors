# Board of Advisors Implementation Plan (v2)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.
>
> **This is a pure-markdown product — there is no code, no build, and no automated test suite.** Wherever a code plan would say "write the failing test / run it," this plan substitutes an explicit **Verify** step: a concrete check (path resolution, content presence, word-count, gitignore behavior) the implementer performs and confirms before committing. Treat Verify steps as the test cycle.

**Goal:** Build a harness-agnostic, folder-structured AI advisory system as pure markdown following the Interpretable Context Methodology (ICM) — no code, no dependencies, no build steps — shipping 8 core advisors, 2 built niche advisors, onboarding, a board-session system, and GitHub distribution files (README, LICENSE).

**Architecture:** Folder structure *is* the architecture. Eight generalist advisors live in `advisors/NN-name/` and two niche advisors in `advisors-extended/NN-name/` (equal folder depth, so relative paths are identical). Each advisor folder holds a Layer 2 identity file (`CONTEXT.md`), Layer 3 `references/`, and a gitignored Layer 4 `output/`. A `sessions/_template/` drives full board consultations across three staged rounds. `_config/` holds shared guidelines (disclaimer, collaboration, ethics, **conventions**, **board-process**), the onboarding interview, and a gitignored persistent profile. `AGENTS.md` is the canonical cross-harness entry point; `CLAUDE.md`/`GEMINI.md` are thin wrappers (native import **plus** a plain-text fallback line).

**Tech Stack:** Plain Markdown. No code, no build tools, no runtime dependencies. `git` and a PowerShell runner are tooling, not product. Distributed as a GitHub Template Repository (MIT).

## Global Constraints

These apply to **every** iteration. Each task's requirements implicitly include this section.

- **Pure markdown.** No runtime code, APIs, or dependencies in the product. The PowerShell runner and `git` are tooling only.
- **`AGENTS.md` is canonical.** `CLAUDE.md`/`GEMINI.md` carry **zero duplicated content** — only the native import of `AGENTS.md`, a plain-text fallback line, and platform-specific notes. [v2]
- **Plain-text fallback line** in each wrapper: *"Canonical instructions for this project are in `AGENTS.md`. If it was not already loaded, read it now before proceeding."* — so injection never silently fails. [v2]
- **ICM token targets:** Layer 0 (`AGENTS.md`) ~800 tokens (~600 words); Layer 1 (root `CONTEXT.md`) ~500 tokens (~375 words); Layer 2 (advisor `CONTEXT.md`) 200–500 tokens.
- **Relative paths only.** All cross-file references use paths relative to the referencing file's own location. Core advisors (`advisors/NN-name/`) and extended advisors (`advisors-extended/NN-name/`) sit at **equal depth**, so both use `../../_config/...` and `../../sessions/...`. [v2]
- **Standard advisor `CONTEXT.md` structure** follows PRD §7.4 exactly, including the `Always load` list: `disclaimer.md`, `collaboration.md`, **`conventions.md`** [v2], and `_config/profile/`.
- **Every advisor response ends with the `## Handoff` block** whose canonical format is defined in `_config/shared/conventions.md`. [v2]
- **Durable-figures rule** (from `conventions.md`) [v2]: reference material expresses durable formulas, ratios, and relative guidance. Any concrete year-specific figure (contribution limits, tax brackets, RMD ages, standard deductions, estate-tax exemptions, premium ranges) is labeled **"illustrative — verify current-year value."** Never present a stale dollar amount as current fact.
- **Harness-agnostic core.** Nothing in the core flow names Claude Code, Gemini CLI, Codex, or any specific harness. The optional delegated board mode is described generically in `board-process.md`. [v2]
- **`.gitignore` must** exclude the five generated profile data files, user session folders (`sessions/????-??-??-*/`), and advisor working artifacts (`advisors/**/output/*`, `advisors-extended/**/output/*`) — while **preserving** each `output/.gitkeep`, `_config/profile/CONTEXT.md`, `sessions/_template/`, and the shipped example session. [v2]
- **The worked example session is 100% fictional** — invented persona, company, and figures. It must not reference any real person, company, or transaction. [v2]
- **Source-of-truth PRD:** `docs/superpowers/specs/2026-06-21-board-of-advisors-design.md`. The PRD overrides any conflict with the archived v1 material in `tmp/old-plan/`.
- **No placeholder text** ("TBD", "TODO", "[fill in]") in any shipped file **except** the intentional bracket placeholders in `advisors/_template/CONTEXT.md` and `advisors/_template/references/frameworks.md`.

---

## File Map

Every file this plan creates, organized by iteration. Files marked **[v2]** are new versus v1.

```
board-of-advisors/
├── README.md                                   ← Iter 01 (initial) → Iter 10 (polish)  [v2]
├── LICENSE                                     ← Iter 01                                [v2]
├── .gitignore                                  ← Iter 01
├── AGENTS.md                                   ← Iter 01
├── CLAUDE.md                                   ← Iter 01
├── GEMINI.md                                   ← Iter 01
├── CONTEXT.md                                  ← Iter 04
│
├── _config/                                    ← Iter 02
│   ├── CONTEXT.md                              ← Iter 02
│   ├── shared/
│   │   ├── disclaimer.md                       ← Iter 02
│   │   ├── collaboration.md                    ← Iter 02 (incl. extended touchpoints)   [v2]
│   │   ├── ethics.md                           ← Iter 02
│   │   ├── conventions.md                      ← Iter 02                                [v2]
│   │   └── board-process.md                    ← Iter 02                                [v2]
│   ├── setup/
│   │   ├── CONTEXT.md                          ← Iter 03
│   │   ├── questionnaire.md                    ← Iter 03
│   │   └── onboarding.md                       ← Iter 03
│   └── profile/
│       └── CONTEXT.md                          ← Iter 03  (5 data files gitignored, generated)
│
├── advisors/
│   ├── _template/                              ← Iter 05
│   │   ├── CONTEXT.md                          ← Iter 05
│   │   └── references/
│   │       ├── CONTEXT.md                      ← Iter 05
│   │       └── frameworks.md                   ← Iter 05
│   ├── 01-financial-planner/                   ← Iter 05
│   │   ├── CONTEXT.md
│   │   ├── references/{CONTEXT.md, frameworks.md}
│   │   └── output/.gitkeep
│   ├── 02-tax-strategist/                      ← Iter 06  [same structure]
│   ├── 03-corporate-attorney/                  ← Iter 06
│   ├── 04-business-strategist/                 ← Iter 06
│   ├── 05-investment-advisor/                  ← Iter 07
│   ├── 06-real-estate-advisor/                 ← Iter 07
│   ├── 07-estate-planning-attorney/            ← Iter 07
│   └── 08-insurance-specialist/                ← Iter 07
│
├── advisors-extended/                          ← Iter 08                                [v2]
│   ├── README.md                               ← Iter 08
│   ├── 09-oil-gas-specialist/                  ← Iter 08  [same structure as core]
│   │   ├── CONTEXT.md
│   │   ├── references/{CONTEXT.md, frameworks.md}
│   │   └── output/.gitkeep
│   └── 10-storage-facility-advisor/            ← Iter 08  [same structure as core]
│       ├── CONTEXT.md
│       ├── references/{CONTEXT.md, frameworks.md}
│       └── output/.gitkeep
│
└── sessions/
    ├── _template/                              ← Iter 09
    │   ├── CONTEXT.md
    │   ├── 00-brief.md
    │   ├── 01-initial-meeting/CONTEXT.md
    │   ├── 02-artifacts/CONTEXT.md
    │   └── 03-reconvene/CONTEXT.md
    └── example-2026-business-sale/             ← Iter 10  (ships; fictional)            [v2]
        ├── CONTEXT.md
        ├── 00-brief.md
        └── 01-initial-meeting/{several advisor .md files}
```

**Iteration 11** creates no new files — it is the integration review.

---

## Iteration 01: Foundation

**Files:**
- Run: `git init`
- Create: `.gitignore`
- Create: `AGENTS.md`
- Create: `CLAUDE.md`
- Create: `GEMINI.md`
- Create: `LICENSE`
- Create: `README.md` (initial)

**Interfaces:**
- Consumes: nothing — this is the repo root.
- Produces: `AGENTS.md` (canonical entry point referenced by both wrappers and root `CONTEXT.md`); `.gitignore` (the protection contract every later iteration relies on); `LICENSE`/`README.md` (GitHub distribution surface).

- [ ] **Step 1: Initialize the git repository** [v2]

  Run `git init` in the project root. This is the first step of the entire build — everything after commits into this repo.

- [ ] **Step 2: Create `.gitignore`** [v2 — adds advisor-output exclusion]

  Must exclude profile data, user sessions, and advisor working artifacts, while preserving each `.gitkeep`, the profile `CONTEXT.md`, the session template, and the shipped example session.

  ```gitignore
  # User profile — generated during onboarding, local-only, never committed
  _config/profile/personal.md
  _config/profile/financial.md
  _config/profile/businesses.md
  _config/profile/investments.md
  _config/profile/goals.md

  # User sessions — local-only (the _template/ and the shipped example-* session are NOT excluded)
  sessions/????-??-??-*/

  # Advisor working artifacts — local-only, but keep the .gitkeep that preserves each output/ dir
  advisors/**/output/*
  advisors-extended/**/output/*
  !advisors/**/output/.gitkeep
  !advisors-extended/**/output/.gitkeep

  # OS and editor files
  .DS_Store
  Thumbs.db
  *.swp
  ```

  Why this works: `sessions/????-??-??-*/` matches only date-prefixed folders (`2026-06-21-topic/`), so `sessions/_template/` and `sessions/example-2026-business-sale/` ship. The `output/*` patterns ignore directory *contents*; the trailing `!...output/.gitkeep` negations re-include the keep files so each `output/` directory survives in git.

- [ ] **Step 3: Create `AGENTS.md` (Layer 0, ~800 tokens / ~600 words)**

  Canonical entry point. Required sections:
  - **`# Board of Advisors`** opening paragraph: harness-agnostic AI advisory system built as pure markdown; ICM principle (each file answers one question; folder hierarchy is the architecture); no code/deps/build.
  - **`## Folder Structure`**: describe `advisors/` (8 core), `advisors-extended/` (2 built niche advisors + the "add your own" example) [v2], `sessions/` (template + date-slug sessions), `_config/` (shared guidelines, onboarding, gitignored profile). Name all 8 core advisors by role and both extended advisors. Explain the three session stages: 01-initial-meeting → 02-artifacts (optional) → 03-reconvene (optional).
  - **`## Ground Rules`**: all guidance is educational/general, not personalized professional advice; no professional relationship is created; pointer to `_config/shared/disclaimer.md`.
  - **`## Getting Started`**: single instruction — "To begin, load `CONTEXT.md`." Note first launch routes to onboarding.

- [ ] **Step 4: Create `CLAUDE.md` (thin wrapper + fallback)** [v2 — adds fallback line]

  ```markdown
  @AGENTS.md

  Canonical instructions for this project are in `AGENTS.md`. If it was not already loaded, read it now before proceeding.

  ## Claude Code Notes

  - To consult a single advisor: navigate to `advisors/NN-name/` (or `advisors-extended/NN-name/`) and load `CONTEXT.md`
  - To run a full board session: start at the root `CONTEXT.md`
  ```

- [ ] **Step 5: Create `GEMINI.md` (thin wrapper + fallback)** [v2 — adds fallback line]

  ```markdown
  <!-- @include AGENTS.md -->

  Canonical instructions for this project are in `AGENTS.md`. If it was not already loaded, read it now before proceeding.

  ## Gemini CLI Notes

  - To consult a single advisor: navigate to `advisors/NN-name/` (or `advisors-extended/NN-name/`) and load `CONTEXT.md`
  - To run a full board session: start at the root `CONTEXT.md`
  ```

- [ ] **Step 6: Create `LICENSE` (MIT)** [v2]

  Standard MIT license text. Copyright line: `Copyright (c) 2026 Board of Advisors contributors`. Use the canonical MIT body verbatim.

- [ ] **Step 7: Create initial `README.md`** [v2]

  A complete-but-pre-polish landing page (Iteration 10 refines it after the example session exists). Include: what it is and who it's for; the core (01–08) and extended (09–10) roster at a glance; install ("Use this template" → open in your harness → first launch runs onboarding); quick start (single-advisor vs. full board); profile-stays-local note; how to add a custom advisor (point to `advisors/_template/` and the built `advisors-extended/` examples); cross-harness note; MIT license line.

- [ ] **Step 8: Verify**
  - `git status` runs (repo initialized).
  - `.gitignore` excludes all 5 profile data files by name, the `sessions/????-??-??-*/` glob, and `advisors/**/output/*` + `advisors-extended/**/output/*`, with the two `!...output/.gitkeep` negations present.
  - `AGENTS.md` names all 8 core advisors by role, both extended advisors, explains the three session stages, ends with "load `CONTEXT.md`", and is ~500–700 words.
  - `CLAUDE.md` begins with `@AGENTS.md`, `GEMINI.md` begins with `<!-- @include AGENTS.md -->`, both contain the plain-text fallback line, and neither duplicates `AGENTS.md` body content.
  - `LICENSE` is valid MIT text; `README.md` covers all bullets above.
  - No unintended placeholder text.

- [ ] **Step 9: Commit**
  ```bash
  git add .gitignore AGENTS.md CLAUDE.md GEMINI.md LICENSE README.md
  git commit -m "feat: foundation — git init, AGENTS.md, wrappers w/ fallback, LICENSE, README"
  ```

---

## Iteration 02: Shared Config

**Files:**
- Create: `_config/CONTEXT.md`
- Create: `_config/shared/disclaimer.md`
- Create: `_config/shared/collaboration.md`
- Create: `_config/shared/ethics.md`
- Create: `_config/shared/conventions.md` [v2]
- Create: `_config/shared/board-process.md` [v2]

**Interfaces:**
- Consumes: nothing (directory creation only).
- Produces: the five `shared/` files referenced by **every** advisor `CONTEXT.md` "Always load" list (`disclaimer.md`, `collaboration.md`, `conventions.md`) and by the board chair / session router (`board-process.md`). `conventions.md` defines the canonical `## Handoff` format and the durable-figures rule that Iterations 05–08 must honor.

- [ ] **Step 1: Create `_config/CONTEXT.md`**

  Navigation file listing `shared/`, `setup/`, `profile/` and when each loads (shared + profile auto-loaded via advisor CONTEXT.md; setup only during onboarding). Mention the two new `shared/` files (`conventions.md`, `board-process.md`).

- [ ] **Step 2: Create `_config/shared/disclaimer.md`**

  Single source of truth for the legal/educational disclaimer. Must state: guidance is educational/general only; no attorney-client, CPA-client, or fiduciary/advisory relationship is created; list professional categories to consult (CFP/RIA, CPA/EA, attorney, real estate broker, insurance agent); no specific product/security recommendations; information-currency caveat; limitation of liability. Tone: professional, not alarmist. (Reuse v1 content from `tmp/old-plan/kickoff-iteration-02.md`.)

- [ ] **Step 3: Create `_config/shared/collaboration.md`** [v2 — adds extended advisors]

  Cross-advisor referral map. Must include a roster table of **all 10 advisors** (01–08 core + 09 oil-gas-specialist, 10 storage-facility-advisor) with slugs and domains, plus the cross-referral touchpoints: Tax↔Financial, Tax↔Corporate Attorney, Corporate Attorney↔Business Strategist, Financial↔Investment, Financial↔Estate, Real Estate↔Tax, Real Estate↔Insurance, Insurance↔Estate, **plus extended touchpoints**: Oil & Gas (09) ↔ Investment (05) / Tax (02); Storage (10) ↔ Real Estate (06) / Tax (02). Instruction: reference other advisors naturally, not as boilerplate footers.

- [ ] **Step 4: Create `_config/shared/ethics.md`**

  Shared ethical guidelines: disclose limitations and escalate to "consult a licensed professional" early; **never fabricate legal citations, tax code sections, case law, or statistics**; no named securities/products/carriers; no conflicts of interest; engage substantively rather than perform liability avoidance. (Reuse v1 content.)

- [ ] **Step 5: Create `_config/shared/conventions.md`** [v2 — new]

  Single source of truth for cross-advisor output conventions. Three sections:
  - **Durable figures rule:** advice and reference material express durable formulas, ratios, and relative guidance. Any concrete year-specific figure (contribution limits, tax brackets, RMD ages, standard deductions, estate-tax exemptions, premium ranges) is labeled **"illustrative — verify current-year value,"** and the advisor confirms the live number before relying on it. Frameworks must never present a stale dollar amount as current fact.
  - **Handoff format:** the canonical `## Handoff` block every advisor response ends with — the exact structure (Key decisions reached / Open questions / Action items / Artifacts to produce / Files written).
  - **Response style:** numbered lists for sequential steps, tables for comparisons, clear section headers; lead with the answer, then support it.

- [ ] **Step 6: Create `_config/shared/board-process.md`** [v2 — new, harness-agnostic]

  Describes the full board session flow once (Rounds 0–3), then two execution modes, **without naming any harness**:
  - **Manual mode (default; works on every harness):** run each advisor in a fresh context window, loading exactly the files the stage lists; save each output; advance stages by hand.
  - **Delegated mode (optional):** *if your agent harness supports dispatching sub-agents or parallel tasks,* the board chair may run each advisor's stage automatically, giving each sub-agent only that stage's load list. An optimization, not a requirement; it changes no file structure or outputs.

- [ ] **Step 7: Verify**
  - `_config/CONTEXT.md` lists all three subdirectories and references `conventions.md` + `board-process.md`.
  - `disclaimer.md` states no attorney-client/CPA-client/advisory relationship and lists professional categories.
  - `collaboration.md` lists all **10** advisors with correct slugs and includes the extended-advisor touchpoints.
  - `ethics.md` includes the "never fabricate citations" and "no named products" rules.
  - `conventions.md` contains the durable-figures rule, the canonical Handoff block, and response-style guidance.
  - `board-process.md` describes manual + delegated modes and names **no** specific harness.
  - No placeholder text.

- [ ] **Step 8: Commit**
  ```bash
  git add _config/CONTEXT.md _config/shared/
  git commit -m "feat: shared config — disclaimer, collaboration, ethics, conventions, board-process"
  ```

---

## Iteration 03: Onboarding & Profile

**Files:**
- Create: `_config/setup/CONTEXT.md`
- Create: `_config/setup/questionnaire.md`
- Create: `_config/setup/onboarding.md`
- Create: `_config/profile/CONTEXT.md`

**Interfaces:**
- Consumes: `_config/` directory (Iteration 02).
- Produces: `questionnaire.md` (defines the onboarding flow) and `profile/CONTEXT.md` (the navigation skeleton advisors reference for profile loading). The five profile **data** files are generated at runtime by onboarding and are gitignored — they are **not** scaffolded here.

- [ ] **Step 1: Create `_config/setup/CONTEXT.md`**

  Agent instructions for running onboarding: check existing profile files first (pause/resume); proceed domain-by-domain (Personal → Employment → Business → Financial → Investments → Goals → Concerns); ask conversationally, not as a dump; write each profile file as its domain completes; on completion direct the user back to root `CONTEXT.md`. (Reuse v1 content from `tmp/old-plan/kickoff-iteration-03.md`.)

- [ ] **Step 2: Create `_config/setup/questionnaire.md`**

  Full question bank, all 7 domains, each domain ending with a `> **[Agent instruction]:**` block telling the agent which profile file to write. Include the "Interview Complete" closing instruction. (Reuse v1 content verbatim — it is sound.)

- [ ] **Step 3: Create `_config/setup/onboarding.md`**

  Human-readable install/usage guide: install via template/clone; first-launch behavior; interview length (~10–20 min) and pause/resume; where the profile lives and that it is gitignored; single-advisor vs. board session; adding a custom advisor (point to `advisors/_template/` **and** the built `advisors-extended/` examples) [v2]; privacy note. (Reuse v1 content, add the extended-advisor pointer.)

- [ ] **Step 4: Create `_config/profile/CONTEXT.md`**

  Navigation + staleness detection: table of the 5 profile files with "Last Updated" column; agent instruction to load all present files, flag any >12 months stale, treat `businesses.md` as optional, and route to onboarding if none exist; instruction to stamp "Last Updated: YYYY-MM-DD" when writing a file. Note all data files are gitignored. (Reuse v1 content.)

- [ ] **Step 5: Verify**
  - `questionnaire.md` covers all 7 domains, each ending with the write-profile agent instruction, plus the "Interview Complete" block.
  - `setup/CONTEXT.md` covers pause/resume.
  - `onboarding.md` explains profile storage/gitignore and points to `advisors-extended/` as an extension example.
  - `profile/CONTEXT.md` has the 5-file table with Last Updated placeholders and the 12-month staleness instruction.
  - No profile **data** files were created.
  - No placeholder text.

- [ ] **Step 6: Commit**
  ```bash
  git add _config/setup/ _config/profile/
  git commit -m "feat: onboarding system — questionnaire, setup guide, profile skeleton"
  ```

---

## Iteration 04: Board Chair (Root `CONTEXT.md`)

**Files:**
- Create: `CONTEXT.md` (root)

**Interfaces:**
- Consumes: advisor slugs (core 01–08 from PRD §4.1, extended 09–10 from §4.2), `_config/profile/` structure (Iter 03), session structure (referenced ahead of Iter 09 — intentional), `board-process.md` (Iter 02).
- Produces: the Layer 1 routing layer every consultation begins from.

- [ ] **Step 1: Create root `CONTEXT.md` (Layer 1, ~500 tokens / ~375 words)** [v2 — adds extended advisors + execution modes]

  Required sections (PRD §7.3):
  - **First Launch Check** — if `_config/profile/` has no profile files, load `_config/setup/CONTEXT.md` and run onboarding first.
  - **Advisor Roster** — a table of core advisors 01–08, and a clearly-labeled extended section listing 09-oil-gas-specialist and 10-storage-facility-advisor (note they live in `advisors-extended/`). Each row: number, slug, one-line topic coverage.
  - **Routing** — single advisor (one domain → load `advisors/NN-name/CONTEXT.md` or `advisors-extended/NN-name/CONTEXT.md`) vs. full board session (multi-domain/major decision → copy `sessions/_template/` to `sessions/YYYY-MM-DD-topic/`, fill `00-brief.md`, follow the session `CONTEXT.md`).
  - **Session Stages** — table of the three stages and when each runs; note every response ends with `## Handoff`. Point to `_config/shared/board-process.md` for manual vs. delegated execution. [v2]
  - **Profile** — always load `_config/profile/` when present; fall back to onboarding if missing.

- [ ] **Step 2: Verify**
  - All 8 core advisors present in the roster; 09 and 10 present and labeled as extended (`advisors-extended/`).
  - All 5 sections present; routing distinguishes single vs. board; stages section points to `board-process.md`.
  - Paths accurate (`_config/profile/`, `_config/setup/CONTEXT.md`, `sessions/_template/`, `advisors/NN-name/CONTEXT.md`, `advisors-extended/NN-name/CONTEXT.md`).
  - ~300–450 words. No placeholder text.

- [ ] **Step 3: Commit**
  ```bash
  git add CONTEXT.md
  git commit -m "feat: board chair routing layer — core + extended roster, execution modes"
  ```

---

## Iteration 05: Advisor Template + Financial Planner (01)

**Files:**
- Create: `advisors/_template/CONTEXT.md`
- Create: `advisors/_template/references/CONTEXT.md`
- Create: `advisors/_template/references/frameworks.md`
- Create: `advisors/01-financial-planner/CONTEXT.md`
- Create: `advisors/01-financial-planner/references/CONTEXT.md`
- Create: `advisors/01-financial-planner/references/frameworks.md`
- Create: `advisors/01-financial-planner/output/.gitkeep`

**Interfaces:**
- Consumes: `_config/shared/{disclaimer,collaboration,conventions}.md` (Iter 02) — referenced in the advisor's "Always load" list.
- Produces: **the advisor pattern that Iterations 06, 07, and 08 follow exactly.** This iteration locks the Layer 2 structure, the v2 "Always load" list (now including `conventions.md`), the Handoff-defined-in-conventions reference, and the durable-figures labeling style. Later advisor iterations and subagents read this iteration's output as the canonical exemplar.

- [ ] **Step 1: Create `advisors/_template/CONTEXT.md`**

  The bracket-placeholder Layer 2 template per PRD §7.4. The `## Inputs` → `### Always load` list MUST be: [v2]
  ```
  - `../../_config/shared/disclaimer.md`
  - `../../_config/shared/collaboration.md`
  - `../../_config/shared/conventions.md`
  - `../../_config/profile/` (all files, if profile exists)
  ```
  Board-session inputs use `../../sessions/[session-name]/...`. The `## Outputs` section states the response ends with a `## Handoff` block **(format defined in `../../_config/shared/conventions.md`)**. Bracket placeholders here are intentional and exempt from the no-placeholder rule.

- [ ] **Step 2: Create `advisors/_template/references/CONTEXT.md`**

  Navigation template: lists `frameworks.md`, "When to Load" guidance, and the "do not load indiscriminately" discipline.

- [ ] **Step 3: Create `advisors/_template/references/frameworks.md`**

  Bracket-placeholder example framework structure (title, when-to-use, steps, output). Add a one-line note that any year-specific figure must follow the durable-figures rule in `../../_config/shared/conventions.md`. [v2]

- [ ] **Step 4: Create `advisors/01-financial-planner/CONTEXT.md` — zero placeholders**

  Full CFP/CFA identity per PRD §4.1 and §7.4. Identity (credentials, mission, data-driven/ethical approach); the v2 Always-load list (incl. `conventions.md`); board-session paths using slug `financial-planner`; Process (financial snapshot → priority stack → goal alignment → tax efficiency → integration) with cross-referrals to Tax (02), Investment (05), Estate (07), Corporate/Business (03/04); Outputs section ending with the `## Handoff` block (note the format lives in `conventions.md`); advisor-specific Disclaimer pointing to `../../_config/shared/disclaimer.md`. (Adapt v1 content from `tmp/old-plan/kickoff-iteration-05.md`, adding `conventions.md` to Always-load.)

- [ ] **Step 5: Create `advisors/01-financial-planner/references/CONTEXT.md`**

  Financial-planner-specific "When to Load" navigation.

- [ ] **Step 6: Create `advisors/01-financial-planner/references/frameworks.md` — durable-figures compliant** [v2]

  All 5 frameworks with full content: Financial Health Snapshot, Financial Priority Stack, Retirement Projection Framework, Debt Payoff Framework, Tax-Efficiency Checklist. **Every concrete year-specific figure** (HSA/IRA/401(k) contribution limits, Roth MAGI limits, RMD age, standard deductions) must carry the **"illustrative — verify current-year value"** label rather than be stated as current fact. Add a header note pointing to the durable-figures rule in `../../_config/shared/conventions.md`. (Adapt v1 frameworks, which currently hard-code 2025 figures, by applying the labels.)

- [ ] **Step 7: Create `advisors/01-financial-planner/output/.gitkeep`** — empty file (preserves `output/`).

- [ ] **Step 8: Verify**
  - `_template/CONTEXT.md` has all sections with bracket placeholders and the v2 Always-load list (incl. `conventions.md`).
  - `01-financial-planner/CONTEXT.md` has zero placeholders, the v2 Always-load list, and the Handoff-format reference to `conventions.md`.
  - Relative paths resolve from `advisors/01-financial-planner/`: `../../_config/shared/disclaimer.md` → `_config/shared/disclaimer.md` ✓; `../../_config/shared/conventions.md` ✓; `../../sessions/[session-name]/00-brief.md` ✓.
  - `frameworks.md` has all 5 frameworks; every year-specific figure carries the illustrative label (no bare "2025" dollar amount presented as current fact).
  - `output/.gitkeep` exists.

- [ ] **Step 9: Commit**
  ```bash
  git add advisors/_template/ advisors/01-financial-planner/
  git commit -m "feat: advisor template + financial planner (01) with v2 conventions"
  ```

---

## Iteration 06: Advisors 02–04 (Tax, Corporate Attorney, Business Strategist)

**Files (per advisor — 4 files each, 12 total):**
- `advisors/02-tax-strategist/{CONTEXT.md, references/CONTEXT.md, references/frameworks.md, output/.gitkeep}`
- `advisors/03-corporate-attorney/{...same...}`
- `advisors/04-business-strategist/{...same...}`

**Interfaces:**
- Consumes: the advisor pattern from Iteration 05 (exact Layer 2 structure incl. v2 Always-load list). Read `advisors/01-financial-planner/CONTEXT.md` as the exemplar before writing.
- Produces: 3 fully functional advisors. After this, the collaboration map's core cross-references are all live.

**Advisor identity content (credentials, mission, frameworks, cross-refs):**
- **02 Tax Strategist** — CPA/EA, M.Tax; slug `tax-strategist`; frameworks: income tax profile, entity tax comparison, deduction optimization, estimated-tax calculator, Roth conversion analysis; cross-refs Financial (01), Corporate Attorney (03), Investment (05), Real Estate (06).
- **03 Corporate Attorney** — JD/Bar/LLM; slug `corporate-attorney`; frameworks: entity selection matrix, asset-protection layering, operating-agreement checklist, contract risk review, buy-sell agreement guide; cross-refs Tax (02), Business Strategist (04), Financial (01), Estate (07). Must state it gives educational guidance, not document drafting.
- **04 Business Strategist** — MBA/CMC/PMP; slug `business-strategist`; frameworks: SWOT, Porter's Five Forces, Business Model Canvas, OKR, growth-lever analysis; cross-refs Corporate Attorney (03), Financial (01), Tax (02), Investment (05).

- [ ] **Step 1: Write all 3 `CONTEXT.md` files**

  Follow Iteration 05's exact Layer 2 structure, including the v2 Always-load list (`disclaimer.md`, `collaboration.md`, **`conventions.md`**, `_config/profile/`) and the Handoff reference to `conventions.md`. Each advisor's board-session paths use its own slug. Each Process cross-references ≥2 other advisors by number and slug. (Adapt v1 content from `tmp/old-plan/kickoff-iteration-06.md`.)

- [ ] **Step 2: Write all 3 `references/CONTEXT.md` files** — advisor-specific "When to Load" navigation.

- [ ] **Step 3: Write all 3 `references/frameworks.md` files — durable-figures compliant** [v2]

  Minimum 4 frameworks each, full actionable content. **Apply the "illustrative — verify current-year value" label to every year-specific figure** — the v1 tax frameworks hard-code 2025 brackets, standard deductions, SALT cap, NIIT/IRMAA/QBI thresholds, estimated-tax due dates, and S-corp profit thresholds; relabel them. Add the header note pointing to `conventions.md`.

- [ ] **Step 4: Create all 3 `output/.gitkeep` files.**

- [ ] **Step 5: Verify**
  - Each folder has all 4 files; each `CONTEXT.md` has the v2 Always-load list and zero placeholders.
  - Correct slugs in board-session paths (`tax-strategist`, `corporate-attorney`, `business-strategist`).
  - Each Process cross-references ≥2 advisors; no two Process sections are identical.
  - Each `frameworks.md` has ≥4 frameworks; every year-specific figure carries the illustrative label.
  - Relative paths resolve (`../../_config/shared/disclaimer.md` → `_config/shared/disclaimer.md` ✓).

- [ ] **Step 6: Commit**
  ```bash
  git add advisors/02-tax-strategist/ advisors/03-corporate-attorney/ advisors/04-business-strategist/
  git commit -m "feat: advisors 02-04 (tax, corporate attorney, business strategist)"
  ```

---

## Iteration 07: Advisors 05–08 (Investment, Real Estate, Estate Planning, Insurance)

**Files (per advisor — 4 files each, 16 total):**
- `advisors/05-investment-advisor/{...}`, `advisors/06-real-estate-advisor/{...}`, `advisors/07-estate-planning-attorney/{...}`, `advisors/08-insurance-specialist/{...}`

**Interfaces:**
- Consumes: the advisor pattern from Iteration 05.
- Produces: the complete 8-advisor core roster; after this the full core board can convene.

**Advisor identity content:**
- **05 Investment Advisor** — CFA/CFP/Series 65; slug `investment-advisor`; frameworks: asset allocation by risk profile, asset location, rebalancing, diversification/concentration checklist, annual portfolio review; cross-refs Financial (01), Tax (02), Estate (07), Real Estate (06). States educational, no named securities.
- **06 Real Estate Advisor** — CCIM/Broker/M.RE; slug `real-estate-advisor`; frameworks: rental cash-flow analysis (NOI/cap rate/CoC), buy vs. rent, 1031 exchange checklist, due-diligence checklist, portfolio strategy; cross-refs Tax (02), Insurance (08), Corporate Attorney (03), Financial (01).
- **07 Estate Planning Attorney** — JD/Bar/CTFA; slug `estate-planning-attorney`; frameworks: estate inventory, beneficiary audit, trust selection guide, POA types, will outline; cross-refs Financial (01), Tax (02), Insurance (08), Corporate Attorney (03). States educational, no document drafting.
- **08 Insurance Specialist** — CPCU/CIC/L&H license; slug `insurance-specialist`; frameworks: personal insurance audit, life insurance DIME method, disability evaluation, business insurance checklist, umbrella assessment; cross-refs Financial (01), Estate (07), Real Estate (06), Corporate Attorney (03).

- [ ] **Step 1: Write all 4 `CONTEXT.md` files** — same Layer 2 structure as Iter 05 with the v2 Always-load list; correct slugs; each Process cross-references ≥2 advisors. (Adapt v1 content from `tmp/old-plan/kickoff-iteration-07.md`.)

- [ ] **Step 2: Write all 4 `references/CONTEXT.md` files.**

- [ ] **Step 3: Write all 4 `references/frameworks.md` files — durable-figures compliant** [v2]

  ≥4 frameworks each, full content. **Relabel every year-specific figure** as illustrative — notably the estate-tax exemption ("$13.99M / set to ~$7M in 2026"), RMD age 73, life-insurance final-expense estimate, and umbrella cost ranges. Add the `conventions.md` header note.

- [ ] **Step 4: Create all 4 `output/.gitkeep` files.**

- [ ] **Step 5: Verify**
  - All 8 core advisors now exist with complete structure.
  - Spot-check path resolution from `advisors/06-real-estate-advisor/CONTEXT.md` and `advisors/08-insurance-specialist/CONTEXT.md`.
  - Zero placeholders; each Process cross-references ≥1 other advisor; every year-specific figure carries the illustrative label.

- [ ] **Step 6: Commit**
  ```bash
  git add advisors/05-investment-advisor/ advisors/06-real-estate-advisor/ advisors/07-estate-planning-attorney/ advisors/08-insurance-specialist/
  git commit -m "feat: advisors 05-08 (investment, real estate, estate planning, insurance)"
  ```

---

## Iteration 08: Niche Advisors 09–10 (`advisors-extended/`) [v2 — new]

**Files:**
- Create: `advisors-extended/README.md`
- Create: `advisors-extended/09-oil-gas-specialist/{CONTEXT.md, references/CONTEXT.md, references/frameworks.md, output/.gitkeep}`
- Create: `advisors-extended/10-storage-facility-advisor/{CONTEXT.md, references/CONTEXT.md, references/frameworks.md, output/.gitkeep}`

**Interfaces:**
- Consumes: the advisor pattern from Iteration 05; the collaboration entries for 09/10 added in Iteration 02.
- Produces: two fully-built, ready-to-use niche advisors that **double as the worked "add your own advisor" example**. They sit at equal folder depth to core advisors, so relative paths are **identical** (`../../_config/...`, `../../sessions/...`) — this is the key correctness property to verify.

**Advisor identity content (new — author fresh, no v1 source):**
- **09 Oil & Gas Specialist** — CFA, P.Eng (Petroleum), Energy Risk Professional (ERP); slug `oil-gas-specialist`. Mission: upstream/midstream/downstream analysis, E&P economics, MLPs, energy infrastructure, commodity-price risk. Frameworks (≥4): upstream E&P project economics (decline curves, breakeven price, netback), midstream/MLP evaluation (distribution coverage, DCF), energy investment due-diligence checklist, commodity price-risk & hedging framework. Cross-refs Investment (05) for portfolio fit and Tax (02) for depletion/IDC/MLP K-1 treatment.
- **10 Storage Facility Advisor** — CCIM, CPM, CFA; slug `storage-facility-advisor`. Mission: self-storage site selection, development, operations, financing, portfolio strategy. Frameworks (≥4): site selection & market saturation (sq-ft per capita, trade-area demand), development pro forma (lease-up curve, stabilized NOI, yield-on-cost), operations & revenue management (ECRI, occupancy/rate optimization), acquisition due-diligence checklist. Cross-refs Real Estate (06) for valuation/financing and Tax (02) for depreciation/cost-segregation/1031.

  **All frameworks obey the durable-figures rule:** express durable formulas and ratios; label any concrete figure (cap rates, sq-ft-per-capita saturation thresholds, breakeven prices, expense ratios) **"illustrative — verify current-year value."**

- [ ] **Step 1: Write `advisors-extended/09-oil-gas-specialist/CONTEXT.md`** — full Layer 2 identity, v2 Always-load list with paths **identical** to core advisors (`../../_config/shared/...`, `../../sessions/...`), slug `oil-gas-specialist`, Process with the cross-refs above, Handoff per `conventions.md`, domain-specific disclaimer.

- [ ] **Step 2: Write `advisors-extended/09-oil-gas-specialist/references/{CONTEXT.md, frameworks.md}`** — navigation + ≥4 frameworks (durable-figures compliant), and `output/.gitkeep`.

- [ ] **Step 3: Write `advisors-extended/10-storage-facility-advisor/CONTEXT.md`** — same structure, slug `storage-facility-advisor`, cross-refs above.

- [ ] **Step 4: Write `advisors-extended/10-storage-facility-advisor/references/{CONTEXT.md, frameworks.md}`** — navigation + ≥4 frameworks (durable-figures compliant), and `output/.gitkeep`.

- [ ] **Step 5: Write `advisors-extended/README.md`**

  Explains that 09 and 10 are **fully usable advisors** *and* reference implementations of the `advisors/_template/` pattern; how to copy one (or `advisors/_template/`) to make your own; reminder to add the new advisor to the root `CONTEXT.md` roster; note that extended advisors sit at the same depth as core advisors so relative paths are unchanged.

- [ ] **Step 6: Verify**
  - Both advisor folders have all 4 files; both `CONTEXT.md` have zero placeholders and the v2 Always-load list.
  - **Path-depth check (critical):** from `advisors-extended/09-oil-gas-specialist/CONTEXT.md`, `../../_config/shared/disclaimer.md` resolves to `_config/shared/disclaimer.md` ✓ and `../../sessions/[session-name]/00-brief.md` resolves correctly ✓ — identical to a core advisor.
  - Each `frameworks.md` has ≥4 frameworks; every concrete figure carries the illustrative label.
  - `advisors-extended/README.md` covers usable-advisor + extension-example dual purpose.
  - Slugs `oil-gas-specialist` and `storage-facility-advisor` match the root roster and collaboration map.

- [ ] **Step 7: Commit**
  ```bash
  git add advisors-extended/
  git commit -m "feat: built niche advisors 09-10 (oil & gas, storage) + extension README"
  ```

---

## Iteration 09: Session System

**Files:**
- Create: `sessions/_template/CONTEXT.md`
- Create: `sessions/_template/00-brief.md`
- Create: `sessions/_template/01-initial-meeting/CONTEXT.md`
- Create: `sessions/_template/02-artifacts/CONTEXT.md`
- Create: `sessions/_template/03-reconvene/CONTEXT.md`

**Interfaces:**
- Consumes: all 10 advisor slugs (to populate the participant checklist), session stage logic (PRD §8.2), `board-process.md` (Iter 02).
- Produces: the complete session template users copy to start a board session.

**Critical path math (verify before writing):**
```
From sessions/_template/CONTEXT.md (depth 2):
  ../../advisors/NN-name/CONTEXT.md             ← core advisor
  ../../advisors-extended/NN-name/CONTEXT.md    ← extended advisor   [v2]
  ../../_config/shared/disclaimer.md
  ../../_config/profile/

From sessions/_template/01-initial-meeting/CONTEXT.md (depth 3):
  ../../../advisors/NN-name/CONTEXT.md
  ../../../advisors-extended/NN-name/CONTEXT.md [v2]
  ../00-brief.md
  ../../../_config/shared/disclaimer.md

From 02-artifacts/ and 03-reconvene/ (depth 3):
  ../01-initial-meeting/[slug].md
  ../02-artifacts/**
```

- [ ] **Step 1: Create `sessions/_template/CONTEXT.md`** — stage router per PRD §7.10/§7.12.

  Participant checklist lists **all 10 advisors**: core 01–08, then 09-oil-gas-specialist and 10-storage-facility-advisor labeled `(extended)`. [v2] Stages checklist (01/02/03). An **Execution** section pointing to `../../_config/shared/board-process.md` for manual vs. delegated modes. [v2] Stage Load Instructions for all three stages using the depth-2 paths above (and `../../advisors-extended/` for extended participants).

- [ ] **Step 2: Create `sessions/_template/00-brief.md`** — the fill-in brief: Question, Background & Context, Constraints & Preferences, Advisors to Include, What You're Looking For (each with example/bracket guidance). (Reuse v1 content from `tmp/old-plan/kickoff-iteration-08.md`.)

- [ ] **Step 3: Create `sessions/_template/01-initial-meeting/CONTEXT.md`** — Round 1 instructions: fresh context window per advisor; load list using depth-3 paths (incl. `../../../advisors-extended/` for extended advisors); save to `[advisor-slug].md`; every response ends with `## Handoff`; completion → decide whether artifacts are needed.

- [ ] **Step 4: Create `sessions/_template/02-artifacts/CONTEXT.md`** — Round 2: only advisors who listed artifacts participate; fresh window; load advisor CONTEXT + brief + their Round 1 handoff; save to `[advisor-slug]/[artifact-name].md`.

- [ ] **Step 5: Create `sessions/_template/03-reconvene/CONTEXT.md`** — Round 3: load advisor CONTEXT + brief + Round 1 handoff + `../02-artifacts/**`; save `[advisor-slug].md`; then board-level synthesis to `00-synthesis.md`.

- [ ] **Step 6: Verify**
  - `_template/CONTEXT.md` lists all **10** advisors (09/10 labeled extended) and points to `board-process.md`.
  - Path resolution at every depth, including the new `advisors-extended/` paths:
    - depth 2: `../../advisors-extended/` → `advisors-extended/` ✓
    - depth 3: `../../../advisors-extended/` → `advisors-extended/` ✓
    - `../00-brief.md`, `../01-initial-meeting/[slug].md`, `../02-artifacts/**` resolve ✓
  - `00-brief.md` has all 5 sections; stage files specify fresh windows and the `## Handoff` requirement; `03-reconvene` specifies `00-synthesis.md`.

- [ ] **Step 7: Commit**
  ```bash
  git add sessions/_template/
  git commit -m "feat: session system — template with three stages, 10-advisor roster, execution modes"
  ```

---

## Iteration 10: README Polish + Fictional Worked Example Session [v2 — new]

**Files:**
- Modify: `README.md` (root) — final polish
- Create: `sessions/example-2026-business-sale/CONTEXT.md`
- Create: `sessions/example-2026-business-sale/00-brief.md`
- Create: `sessions/example-2026-business-sale/01-initial-meeting/<advisor-slug>.md` (several)

**Interfaces:**
- Consumes: the full advisor roster (01–10) and the session template (Iter 09).
- Produces: the GitHub landing page in final form and a shipped, **entirely fictional** example session demonstrating Round 1.

> **HARD CONSTRAINT — fictional only.** The example persona, company, figures, and circumstances are **invented**. Do **not** reference any real person, company, or transaction, and do **not** seed it from the user's real life or business. (See memory: keep-generated-examples-fictional.) The folder name `example-2026-business-sale` deliberately does **not** match the `????-??-??-*` gitignore glob, so it ships.

- [ ] **Step 1: Polish root `README.md`**

  Bring the Iteration 01 draft to final: tighten the value proposition; ensure the roster lists all 10 advisors (core + extended); add a short link/walkthrough referencing the new `sessions/example-2026-business-sale/` so readers can see a real session; confirm install, profile-privacy, add-a-custom-advisor (point to `advisors/_template/` + `advisors-extended/`), cross-harness, and MIT-license sections are complete and accurate.

- [ ] **Step 2: Create `sessions/example-2026-business-sale/00-brief.md`** — a filled brief with an invented persona (e.g., a fictional founder selling a fictional company) and invented figures, following the `00-brief.md` template structure.

- [ ] **Step 3: Create `sessions/example-2026-business-sale/CONTEXT.md`** — a filled session router: participant checklist with the relevant advisors checked (e.g., financial planner, tax strategist, corporate attorney, business strategist), Round 1 marked complete, correct relative paths. Execution section points to `board-process.md`.

- [ ] **Step 4: Create 3–4 `01-initial-meeting/<advisor-slug>.md` Round 1 outputs** — sample advisor responses to the fictional brief, each ending with a `## Handoff` block per `conventions.md`, each obeying the durable-figures rule (illustrative labels on any concrete figure). Demonstrates the real shape of session output.

- [ ] **Step 5: Verify**
  - The example session is entirely fictional — no real person/company/transaction; no seeding from the user's real life.
  - Folder name does not match `????-??-??-*` (starts with `example-`), so `git status` shows it as tracked (it ships).
  - Each sample advisor output ends with a `## Handoff` block and uses illustrative labels on concrete figures.
  - `README.md` lists all 10 advisors and links to the example session; all sections complete.

- [ ] **Step 6: Commit**
  ```bash
  git add README.md sessions/example-2026-business-sale/
  git commit -m "feat: polish README + ship fictional worked example session"
  ```

---

## Iteration 11: Integration Review

**Files:** No new files. Verification, coherence checks, and gap-fixing only.

**Interfaces:**
- Consumes: all files from Iterations 01–10.
- Produces: a verified, ship-ready repo.

- [ ] **Step 1: Verify `.gitignore` behavior end-to-end** [v2 — expanded]
  - 5 profile data files excluded; `_config/profile/CONTEXT.md` tracked.
  - `sessions/????-??-??-*/` excludes a date-slug session but NOT `sessions/_template/` and NOT `sessions/example-2026-business-sale/`.
  - `advisors/**/output/*` and `advisors-extended/**/output/*` exclude artifacts but each `output/.gitkeep` is tracked (confirm with `git check-ignore -v` on a sample artifact path and on a `.gitkeep`).

- [ ] **Step 2: Path audit across all advisors — core AND extended** [v2]
  - Trace `../../_config/shared/{disclaimer,collaboration,conventions}.md`, `../../_config/profile/`, and `../../sessions/[session-name]/...` from at least one core advisor (e.g., 01, 08) and **both extended advisors** (09, 10). Confirm extended advisors resolve identically to core (equal depth).

- [ ] **Step 3: Verify `collaboration.md` completeness** — all **10** advisors with correct slugs; all core touchpoints + the extended touchpoints (09↔05/02, 10↔06/02).

- [ ] **Step 4: Verify session template + example paths** — at depth 2 and depth 3, including `advisors-extended/` paths; confirm the example session's relative paths resolve.

- [ ] **Step 5: Conventions compliance scan** [v2]
  - Every advisor `CONTEXT.md` "Always load" list includes `conventions.md`.
  - Every advisor response template / Handoff references the `conventions.md` format.
  - Spot-check `frameworks.md` files: no bare year-specific dollar amount is presented as current fact without the "illustrative — verify current-year value" label.

- [ ] **Step 6: Cross-harness wrapper check** [v2] — `CLAUDE.md` has `@AGENTS.md` + the plain-text fallback line; `GEMINI.md` has `<!-- @include AGENTS.md -->` + the fallback line; neither duplicates `AGENTS.md` body.

- [ ] **Step 7: Token-count check** — `AGENTS.md` ~500–700 words; root `CONTEXT.md` ~300–450 words. Trim/expand if far outside.

- [ ] **Step 8: Placeholder scan** — search all shipped files for `[fill`, `[your`, `[Role`, `TBD`, `TODO`, `placeholder`. These are allowed ONLY in `advisors/_template/CONTEXT.md` and `advisors/_template/references/frameworks.md`. Fix any others.

- [ ] **Step 9: Full file-structure presence check** — confirm every file in the File Map exists (root distribution files, `_config/` incl. `conventions.md` + `board-process.md`, all 10 advisors, `advisors-extended/README.md`, session template, example session).

- [ ] **Step 10: Final commit**
  ```bash
  git add -A
  git commit -m "chore: integration review — paths, conventions, gitignore, wrappers, tokens"
  ```

---

## Self-Review Against PRD

### Spec Coverage Check

| PRD Section | Covered by | Status |
|-------------|-----------|--------|
| §2 Goals (incl. [v2] README/LICENSE, [v2] built niche advisors) | Iters 01, 08 | ✓ |
| §4.1 Core advisor roster (8) | Iters 05–07 | ✓ |
| §4.2 Niche advisors (09–10, `advisors-extended/`) [v2] | Iter 08 | ✓ |
| §5 Repository structure (incl. README, LICENSE, advisors-extended, example session) | File Map + all iters | ✓ |
| §6 ICM five-layer hierarchy + token targets | All CONTEXT.md; Iter 11 token check | ✓ |
| §7.1 `AGENTS.md` (names extended advisors) | Iter 01 | ✓ |
| §7.2 `CLAUDE.md`/`GEMINI.md` + plain-text fallback [v2] | Iter 01; Iter 11 wrapper check | ✓ |
| §7.3 Root `CONTEXT.md` (extended advisors + execution modes) | Iter 04 | ✓ |
| §7.4 Advisor `CONTEXT.md` (v2 Always-load incl. conventions.md) | Iters 05–08 | ✓ |
| §7.5 References navigation (Layer 3) | Iters 05–08 | ✓ |
| §7.6 `disclaimer.md` | Iter 02 | ✓ |
| §7.7 `collaboration.md` (incl. extended touchpoints) [v2] | Iter 02 | ✓ |
| §7.8 `ethics.md` | Iter 02 | ✓ |
| §7.9 `conventions.md` (durable figures + Handoff + style) [v2] | Iter 02; enforced Iters 05–08 | ✓ |
| §7.10 `board-process.md` (manual/delegated, harness-agnostic) [v2] | Iter 02 | ✓ |
| §7.11 `questionnaire.md` (7 domains) | Iter 03 | ✓ |
| §7.12 Session `CONTEXT.md` (10-advisor checklist) | Iter 09 | ✓ |
| §7.13 `README.md` [v2] | Iters 01 (initial) + 10 (polish) | ✓ |
| §7.14 `LICENSE` (MIT) [v2] | Iter 01 | ✓ |
| §7.15 `advisors-extended/README.md` [v2] | Iter 08 | ✓ |
| §8.1 Single-advisor flow | Iter 04 routing | ✓ |
| §8.2 Full board session (Rounds 0–3) | Iter 09; demoed Iter 10 | ✓ |
| §8.3 Context-window discipline + Handoff | `conventions.md` + stage files | ✓ |
| §9 Onboarding & persistent profile | Iter 03 | ✓ |
| §9.4 Multi-user isolation (gitignore) | Iters 01, 11 | ✓ |
| §9.5 Profile staleness detection | Iter 03 (`profile/CONTEXT.md`) | ✓ |
| §10 Cross-harness compatibility + fallback [v2] | Iter 01; Iter 11 | ✓ |
| §11.3 Adding custom advisors (template + built examples) | Iters 05, 08 | ✓ |
| §11.4 Starting a new session | Iter 09 | ✓ |
| §13 Implementation Notes — 11 iterations + global constraints | This plan, all iters | ✓ |
| Durable-figures rule applied to all frameworks [v2] | Iters 05–08; Iter 11 scan | ✓ |
| Example session 100% fictional [v2] | Iter 10 (hard constraint) | ✓ |
| `git init` as first build step [v2] | Iter 01 Step 1 | ✓ |
| `.gitignore` advisor-output exclusion + .gitkeep preserved [v2] | Iter 01; Iter 11 | ✓ |

### Gaps Identified: None
