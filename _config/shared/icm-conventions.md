# ICM Conventions (Project Rulebook)

This file records how the Board of Advisors applies **Interpretable Context Methodology (ICM)** —
folder structure as agent architecture. It is committed Layer-3 reference material so the
*decisions* travel with the project on any harness, with no skill install required.

For the general, reusable methodology (layer definitions, audit script, templates), use the
`maintaining-icm` skill. This file is the project-specific overlay: what *we* decided.

## This project is pure ICM (a library, not a broken pipeline)

ICM supports two valid shapes. We use the second one, and the distinction matters:

| Layer | In this project |
| --- | --- |
| **Layer 0** — identity / harness routing | `AGENTS.md` (canonical) + `CLAUDE.md`, `GEMINI.md` (shims that import it) |
| **Layer 1** — workspace routing | root `CONTEXT.md` — the board chair; convenes the right advisors per message |
| **Layer 2** — control point (the work) | the **meeting lifecycle**: intake (`brief.md`) → deliberation (convene + `artifacts/`) → minutes (`minutes.md`), per `shared/meeting-process.md` |
| **Layer 3** — stable reference | the **advisor roster library** (`advisors/`, `advisors-extended/`) + this `_config/` |
| **Layer 4** — working artifacts | `meetings/<topic>/` (brief, artifacts, minutes) |

**The advisors are a Layer-3 reference library, not Layer-2 stages.** They are numbered for stable
identity, *not* execution order, and are *selected by topic*, not run in sequence. Convening the
relevant advisors each turn is the controlling stage scoping its Inputs — core ICM, not an
extension of it. The conversational feel of a meeting is an execution-style choice; every layer,
file, and handoff is plain-text ICM.

## Numbers are stable IDs

Advisor numbers (01–10, spanning `advisors/` 01–08 and `advisors-extended/` 09–10) are primary
keys, like database IDs:

- Never renumber survivors after deleting an advisor. Leave the gap; use the next *unused* number
  for the next advisor.
- Advisors cross-reference each other by **number + slug**. On deletion, scrub references in the
  root `CONTEXT.md` roster, `shared/collaboration.md`, and any other advisor's Process section.
- See `advisors-extended/README.md` for the add/remove checklists.

## Factory vs. product

- **Factory (Layer 3, stable):** advisor roster, `_config/shared/` rules, `_config/setup/`.
- **Product (Layer 4, per-run):** everything under `meetings/`.

Keep them apart. Per-meeting artifacts never live inside advisor folders.

## In-workspace memory (portability rule)

Durable memory lives **inside the workspace as files**, never only in a harness-private,
user-level store — otherwise it does not travel when the project moves to another harness.

- The user profile (`_config/profile/`) is the worked example: a defined in-workspace location,
  content gitignored for privacy, loaded every session via each advisor's "Always load".
- Apply the same pattern to any new durable memory: stable facts → Layer 3; evolving state →
  Layer 4. Gitignore the *content* if private, but keep the *location* in the structure.

## Recursive Layer-3 routing

Large reference areas carry their own `CONTEXT.md` router (Layer-1 routing applied inside Layer 3):
`_config/CONTEXT.md` and each `advisors/NN-name/references/CONTEXT.md`. Keep these in sync when
adding reference files.

## Tooling vs. workspace content (what is and isn't ICM)

- **Workspace content** (committed, harness-agnostic): `AGENTS.md`, `CONTEXT.md`, `advisors*/`,
  `_config/`, `meetings/example-*/`. This *is* the project and must travel self-contained.
- **Agent tooling** (re-installable, not the project): skills under `.agents/skills/` (with
  `.claude/`/`.codex/` symlinked to it). The content dirs are gitignored like `node_modules`;
  `skills-lock.json` is committed like a lockfile so a clone can reinstall them.
- **Coexisting conventions:** `docs/superpowers/` holds plan/spec artifacts from the
  [superpowers](https://skills.sh) skill set (dev-process tooling). It sits *beside* ICM and does
  not define ICM structure — do not mistake it for a Layer.
- **The `maintaining-icm` skill** is this methodology's own linter/scaffolder. It lives in
  `.agents/skills/maintaining-icm/` and is tracked in-place via a `.gitignore` exception for now;
  once published to skills.sh it becomes a normal `skills-lock.json` entry and the exception goes.
