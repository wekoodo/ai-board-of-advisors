---
name: maintaining-icm
description: "Use when building, auditing, or maintaining a folder-based agent context architecture (Interpretable Context Methodology / ICM) — AGENTS.md/CLAUDE.md entrypoints, CONTEXT.md routing, numbered stage pipelines OR numbered reference libraries (rosters), references, working artifacts, and review gates. Use when a project wants portable, model/harness-agnostic, plain-markdown agent context instead of monolithic prompts, and whenever structure should be kept ICM-compliant as it grows."
---

# Maintaining ICM

## Core Idea

Use folder structure as agent architecture. A project should tell agents where they are, where to go, what to do at one step, which stable references constrain behavior, and which working artifacts to transform. This is an *ongoing* discipline — build the structure once, then keep it compliant as the project grows.

Keep the system plain-text and harness-agnostic. Use scripts for deterministic mechanical work; use Markdown contracts for judgment, synthesis, routing, and review.

Read [icm-patterns.md](references/icm-patterns.md) for layer definitions, the two valid Layer-2/3 shapes, folder templates, fit criteria, token budgets, contract examples, and the validation checklist.

## Two valid shapes (read this before auditing)

ICM as published describes a **sequential stage pipeline**. But the same five layers support a second, equally valid shape, and confusing them is the most common audit error:

- **Stage pipeline** — a `stages/` directory of numbered, sequential contracts (`01_research/` → `02_draft/`). Layer 2 = stage contracts. Use for sequential, reviewable, repeatable workflows.
- **Reference library (roster)** — a directory of numbered `NN-name/` members each with a `CONTEXT.md` (e.g. `advisors/01-financial-planner/`). **A library is Layer 3 reference material, not a broken pipeline.** A controlling stage *selects from* it per run; the members are not executed in sequence.

A project may have a pipeline, a library, both, or neither. **A numbered folder is not automatically a stage.** If its members are personas/specialists/domains selected by topic rather than run in order, it is a Layer-3 library — do not flag the absence of `stages/`.

> Example: a live "board meeting" system is pure ICM. Layer 2 is the *meeting lifecycle* (intake → deliberation → minutes). Layer 3 is the *advisor roster library*, selected per topic. Layer 4 is the per-meeting artifacts. The conversational feel of deliberation is an execution-style choice, not an architectural violation.

## Workflow

### 1. Explore existing context

- Read root `AGENTS.md`, `CLAUDE.md`, `README.md`, `CONTEXT.md`, `CONTEXT-MAP.md`, `docs/agents/`, `handoffs/`, `_config/`, `.cursor/rules`, `.github/copilot-instructions.md`, and local scripts only as relevant.
- Identify the canonical Layer-0 entrypoint. If a tool-specific file is only a shim (e.g. `CLAUDE.md` importing `AGENTS.md`), preserve the shim and edit the canonical file.
- Notice ignored/generated projection directories (`.claude/`, `.codex/`, `.agents/`). Do not duplicate canonical content into them — they are re-installable tooling, not workspace content.

### 2. Check fit and identify the shape

- Sequential, repeatable, human-reviewed-per-step work → **stage pipeline**.
- A roster of roles/specialists/domains selected by topic → **reference library**.
- Durable context but no workflow yet → Layers 0–1 (+3) only; add a pipeline or library later.
- Prefer conventional code for real-time multi-agent messaging, high concurrency, or automated mid-pipeline branching on model output.

### 3. Map the context layers

- **Layer 0** — root identity + harness routing (`AGENTS.md`, `CLAUDE.md`).
- **Layer 1** — workspace routing (`CONTEXT.md`/`CONTEXT-MAP.md`): which stage handles a task, what shared resources exist.
- **Layer 2** — the control point: stage contracts (`Inputs`/`Process`/`Outputs`, optional `Verify`), OR a controlling stage that selects Layer-3 library members per run. The Inputs table names exact files *and the relevant sections*.
- **Layer 3** — stable reference material (`_config/`, `references/`, `shared/`): conventions, domain frameworks, and **roster libraries**. Large reference collections may carry their own `CONTEXT.md` router (recursive Layer-1 routing).
- **Layer 4** — per-run working artifacts (`output/`, `meetings/`, `handoffs/`, generated `.md`/`.json`).

### 4. Design files and folders

- Make each stage (or library member) one job / one role with one clear contract.
- Number folders to encode order (pipeline) or stable identity (library). Treat numbers as stable IDs: never renumber survivors after a deletion; leave the gap and scrub cross-references.
- In every contract, list exact Layer-3 and Layer-4 inputs. Avoid whole-repo reads when a scoped list is possible.
- Keep instructions and intermediate artifacts in Markdown/JSON/YAML/plain text.
- Put deterministic mechanical work in local scripts; keep semantic decisions in Markdown contracts.
- Keep a stage's delivered context small (the paper's target: ~2–8k tokens; Layers 0–2 ≈ 1.3–1.6k). If a step needs far more, re-scope its Inputs.

### 5. Edit conservatively

- Preserve existing repo guidance and user terminology.
- Update the canonical router instead of appending duplicate routing blocks.
- Separate factory from product: stable rules/rosters → Layer 3; per-run outputs → Layer 4.
- Persist durable memory as files **inside** the workspace (Layer 3 for stable facts, Layer 4 for evolving state), not in harness-private user-level stores, so the project stays portable.
- Treat repeated output edits as diagnostic: if the same fix recurs, change the contract or reference source, not the output.

### 6. Validate

- Run `python <skill>/scripts/audit_routed_context.py <project-root>`. It recognizes pipelines, reference libraries, recursive routing, and Layer-4 areas; a complete library-only project audits clean.
- Manually check: each stage has reviewable output, a scoped input list, no irrelevant context loading, and no hidden dependency on one model or harness.
- If the project keeps project-specific ICM decisions in a committed reference file (e.g. `_config/shared/icm-conventions.md`), audit against it too.

## Deliverable shape

Prefer a small changed set:

- `AGENTS.md`/`CLAUDE.md` (Layer 0), `CONTEXT.md`/`CONTEXT-MAP.md` (Layer 1).
- `stages/NN_slug/CONTEXT.md` + `output/` for pipelines, OR `NN-name/CONTEXT.md` library members for rosters.
- `references/`, `_config/`, `shared/` for stable reference material; a committed conventions file for project-specific ICM decisions.
- Local scripts only when they replace repeated deterministic work.
