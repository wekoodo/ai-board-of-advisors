# ICM Conventions (Project Rulebook)

This file records how the Board of Advisors applies **Interpretable Context Methodology (ICM)** —
folder structure as agent architecture. It is committed Layer-3 reference material so the
*decisions* travel with the project on any harness, with no skill install required.

For the general, reusable methodology (layer definitions, audit script, templates), use the
`icm` skill (pinned in `skills-lock.json`). This file is the project-specific overlay: what *we*
decided.

## This project is pure ICM (a library, not a broken pipeline)

ICM supports two valid shapes. We use the second one, and the distinction matters:

| Layer | In this project |
| --- | --- |
| **Layer 0** — identity / harness routing | `AGENTS.md` (canonical) + `CLAUDE.md`, `GEMINI.md` (shims that import it) |
| **Layer 1** — workspace routing | root `CONTEXT.md` — the board chair; convenes the right advisors per message |
| **Layer 2** — control point (the work) | the **meeting lifecycle**: intake (`brief.md`) → deliberation (convene + `artifacts/`) → minutes (`minutes.md`), per `shared/meeting-process.md` |
| **Layer 3** — stable reference | the **advisor roster library** (`advisors/`, `advisors-extended/`) + this `_config/` |
| **Layer 4** — working artifacts | `meetings/CONTEXT.md` routes into `meetings/<topic>/` and, when an entity index exists, new records under `meetings/<scope>/<topic>/` (existing flat folders stay); local `meetings/index.md` catalogs them |

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

- **Factory (Layer 3, stable):** advisor roster, `_config/shared/` rules (including `version.md`
  soft-check and on-demand `updates.md`), `_config/setup/`, `_config/profile/CONTEXT.md`,
  `_config/profile/entities/CONTEXT.md`, `_config/profile/entities/_template/`,
  root `CHANGELOG.md`.
- **Product (Layer 4, per-run):** user records under `meetings/<topic>/`, and, after
  `_config/profile/entities/index.md` exists, new records under `meetings/<scope>/<topic>/`.
  Both layouts may coexist; do not relocate an existing folder. Tracked `meetings/CONTEXT.md` is
  recursive routing guidance for this area, and local-only `meetings/index.md` is evolving
  routing metadata. Meeting record files remain authoritative. Examples ship separately as
  reference factory content under `meetings/example-*/`.

Keep them apart. Per-meeting artifacts never live inside advisor folders.

**Naming note:** “product” in `version.md` / `updates.md` means the *shipped Board of Advisors
system* (the GitHub template source), not Layer-4 meeting output. Personal boards pull factory
updates from that product via an `upstream` git remote; they do not push Layer-4 life data there.
**Load discipline:** the update soft-check and its throttle live in `version.md` alone; load
`updates.md` only for connect/apply, and keep always-on routers (e.g. `AGENTS.md`) free of the deep
protocol.

## In-workspace memory (portability rule)

Durable memory lives **inside the workspace as files**, never only in a harness-private,
user-level store — otherwise it does not travel when the project moves to another harness.

- The user profile (`_config/profile/`) is the worked example: a defined in-workspace location,
  content excluded from Git by default, loaded via `_config/profile/CONTEXT.md` scoped rules
  (not a bulk directory read). Gitignore does not keep facts off a cloud model that reads them.
- Apply the same pattern to any new durable memory: stable facts → Layer 3; evolving state →
  Layer 4. Gitignore the *content* if private, but keep the *location* in the structure.

## Recursive Layer-3 routing

Large reference areas carry their own `CONTEXT.md` router (Layer-1 routing applied inside Layer 3):
`_config/CONTEXT.md`, `_config/profile/CONTEXT.md`, `_config/profile/entities/CONTEXT.md` (the
tracked entity router; the entity layer is active only when `entities/index.md` exists),
`_config/profile/trust/CONTEXT.md` when that folder exists, and each
`advisors/NN-name/references/CONTEXT.md`. Keep these in sync when adding reference files.

## Keep files load-scoped (split at write time)

ICM treats a step that blows past a small token budget as a signal to re-scope Inputs, not to
raise the budget. Apply the same rule when **writing** profile and reference files, not only when
loading them.

Every durable file answers one question. If a write would mix independently loadable concerns
into a file that meetings or onboarding load as a whole, split **before** that write:

1. Create a folder with its own `CONTEXT.md` router and section files.
2. If a completeness gate or existing load path names the old file, keep that path as a thin
   shim. Do not duplicate facts in the shim.
3. Load and update only the sections the question needs. Do not bulk-load the folder, and do not
   reconstitute one giant file later.

Independently loadable concerns include identity, action registers, source inventories,
open-question lists, and onboarding-status blocks. Split at those retrieval boundaries. Several
short related sections in one file do not justify a split. Short first-pass answers (for example
an optional living-trust note during general onboarding) may share one file. A focused pass that
would turn that file into a whole-binder dump must split at that pass.

General onboarding still writes the five core files as single files. Split later, when a focused
write would mix independently loadable concerns.

The optional trust profile is the worked example: start with `trust.md`; if focused onboarding
would mix independently loadable concerns, split into `trust/` and keep `trust.md` as a shim.
The same pattern applies to any named profile path (`financial.md`, `goals.md`, an entity
`goals.md`, and other domain files). Entity in-depth files already follow one-question-per-file.
Do not wait for a later structure cleanup to split.

### Resolve a named profile path

Gates, load tables, action ranking, and write-back keep using the stable named path
(`financial.md`, `goals.md`, `trust.md`, `<entity-slug>/goals.md`, and other domain files). After
a split, that named file is a **shim**: it points at a same-stem folder that contains `CONTEXT.md`,
and it does not hold the durable facts.

**Recognize a shim.** The named file exists, a sibling folder of the same stem exists with
`CONTEXT.md`, and the named file does not itself contain the durable sections. Example shim body:

```markdown
# Financial profile

Last Updated: YYYY-MM-DD

This file is a shim. Facts live under `financial/`. Load `financial/CONTEXT.md` and only the
sections the question needs.
```

The folder router lists owning section files and the headings they carry (for example
`Income & Employment` → `income-employment.md`). Section files hold the facts. Do not nest
another shim under a section file.

**Resolve (one hop).** One hop is one split level: the named shim, that folder's `CONTEXT.md`,
and the section files that router lists. Do not stop at the folder router. Heading, date, and
action-register checks run against those section files, not the shim and not the router. Follow
only targets named in the shim or that folder's `CONTEXT.md`. Then:

- A required heading is present when the folder router maps it to a section file that contains
  that heading. Completeness needs that owning section (and its date), not every file in the
  folder. `financial.md` must resolve to a section that contains `Income & Employment`;
  `goals.md` must resolve to a section that contains `Current Concerns`.
- An action register is the section file the folder router names for actions, not the shim
  and not the folder router.
- `Last Updated: YYYY-MM-DD` is valid when each resolved owning section this check or load
  needs has that line. The shim's own stamp does not stand in for a missing section date.

If the named file still holds the facts (flat, not a shim), use it as-is.

**Write.** Edit the resolved owning section. Stamp `Last Updated` only on files actually edited.
Do not copy the updated facts into the shim. Do not reconstitute one file.

**Repair, do not rebuild.** A missing target, a missing required heading after resolution, or a
cycle (a target already in the resolution chain) is a scoped repair of that split: restore the
pointer or the missing section, keep other complete profile files in place, and do not restart
general onboarding.

## Tooling vs. workspace content (what is and isn't ICM)

- **Workspace content** (committed, harness-agnostic): `AGENTS.md`, `CONTEXT.md`, `advisors*/`,
  `_config/`, `meetings/example-*/`. This *is* the project and must travel self-contained.
- **Agent tooling** (re-installable, not the project): skills under `.agents/skills/` (with
  `.claude/`/`.codex/` symlinked to it). The content dirs are gitignored like `node_modules`;
  `skills-lock.json` is committed like a lockfile so a clone can reinstall them with
  `npx skills experimental_install`.
- **Factory authoring history is not product:** Keep plans, specs, and process-pack trees off the
  product default branch. Keep live control in root `CONTEXT.md` and
  `_config/shared/meeting-process.md`; do not add a `stages/` pipeline to explain historical
  files.
- **In-progress factory work** lives under gitignored `tmp/`. When `tmp/CONTEXT.md` exists, it is
  the Layer-1 router for product authoring in this clone. Root `CONTEXT.md` loads it only for
  product-change tasks. Do not commit `tmp/` and do not host a board meeting for factory work.

## Skills management

Skills on this board sit on several surfaces. This section is the load and ownership contract.
Do not treat a skill, an overlay, and shared protocol as the same class of file.

| Surface | Role | Git |
| --- | --- | --- |
| `skills-lock.json` | Pins which skills a clone can reinstall | Tracked (lockfile) |
| `.agents/skills/` (and harness symlinks) | Installed copies of locked skills | Gitignored; reinstallable |
| Overlays in `_config/shared/` | Project decisions that constrain a skill | Tracked workspace content |
| Load lists (chair, advisor Inputs, `_config/CONTEXT.md`) | Who loads which overlay, and when | Tracked |
| Harness-bundled skills | Host may fire skills that are not in the lockfile | Not board protocol |

**Required vs optional.** Shared protocol is required and the board must run with no skill
install. Locked skills are optional tooling. Overlays are required *workspace content* (they
travel with the project) but they are not Always-load protocol. A clone that never runs
`npx skills experimental_install` still holds a valid meeting.

**Do not edit vendored skills.** Never patch `SKILL.md` or other files under `.agents/skills/`.
A lockfile reinstall overwrites them. Put board-specific decisions in a committed overlay.

**Do not restyle agent contracts.** `google-doc-style` governs reader-facing prose only. It must
not rewrite `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, any `CONTEXT.md`, `_config/shared/` protocol,
advisor `references/`, `skills-lock.json`, or the `## Handoff` block shape. That rule lives in
`google-doc-style-overlay.md` and applies whenever that skill is active.

**Locked skills on this board:**

| Skill | Overlay | Required for meetings? | Who loads the overlay |
| --- | --- | --- | --- |
| `google-doc-style` | `google-doc-style-overlay.md` | No. `conventions.md` still governs response shape if the skill is absent. | Chair when writing to the user or producing artifacts. Advisors under **Load when writing to the user**, not **Always load**. If the skill is active, the overlay wins on listed conflicts (real profile data, board voice, no restyle of contracts). |
| `icm` | `icm-conventions.md` (this file) | No. Structure and audit work should install it. | Chair or whoever is doing ICM / structure maintenance, on demand. Not advisor Always load. Not a normal meeting load. |

**Always load** (shared protocol — every advisor, no skill involved): `disclaimer.md`,
`collaboration.md`, `ethics.md`, `conventions.md`, plus `profile/CONTEXT.md` (then follow its
scoped load; do not bulk-load `entities/`).

**Chair-only / on demand:** `meeting-process.md` and `convening.md` (hosting a meeting), this
file (structure), `version.md` / `updates.md` (product update flow).

**Harness-bundled skills.** The host may also fire skills that are not in `skills-lock.json`
(for example PDF, slides, or image tools). Those are host tooling. They must not rewrite
workspace contracts, must not restyle agent contracts as public docs, and do not become board
protocol unless they are pinned in the lockfile and given a committed overlay. Do not vendor
extra skills to paper over a host default.
