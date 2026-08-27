# Handoff: ICM cleanup product rules

**Date:** 2026-08-27  
**Branch:** main  
**For:** Factory agent on this repo (`wekoodo/ai-board-of-advisors`)

---

## Do not copy the personal board

These rules came from an ICM structure cleanup on a personal instance of the product. That instance
has real family, trust, and entity data. **None of that data is product.**

Copy **tracked contracts** (routers, templates, setup, advisor Inputs, `.gitignore` comments).
Do not copy gitignored profile files, entity slugs, dollar amounts, Drive URLs, or machine-local
paths to other workspaces.

Worked **product-shaped** copies (tracked files only) live in the sibling instance:

`/home/angellops/projects/board-of-advisors-drewangell`

Use those files as the intended *shape*. Strip instance names and local paths when you port.

The instance working log (not this handoff) is
`docs/handoffs/2026-08-27-upstream-board-factory-notes.md` in that repo. This file is the
implementable product brief.

## Factory `main` versus the instance

Factory `main` today still ships the original five-file profile (`personal.md`, `financial.md`,
`businesses.md`, `investments.md`, `goals.md`) and still contains `docs/superpowers/`.

The instance already has routed trust and entity profile contracts in **tracked** files. This
handoff is not "merge the entire personal board." It is the product rules the cleanup proved you
need, in two packages:

1. **Package A** — ship on current factory `main`. No trust or entity folders required.
2. **Package B** — bake into trust and entity routing **when you ship that system**. Factory `main`
   does not have it yet. If you ship those folders without these guards, the next clone repeats the
   cleanup.

Do both packages. Do not treat Package B as "later cleanup on each personal board."

---

## Package A — current product

### A1. Load `ethics.md` on every Always-load list

**Defect.** `_config/CONTEXT.md` **Contents** already says every advisor loads `shared/ethics.md`.
The shipped **Always load** lists (template, core `01`–`08`, extended `09`–`10`) and **When to
Load** omit it. The file already has the citation and named-product rules.

**Why it showed up:** an ICM pass found Contents and Inputs out of sync. Not caused by one family's
onboarding.

**Ship:**

1. Add `../../_config/shared/ethics.md` to every advisor **Always load** list, after
   `collaboration.md`: `advisors/_template/CONTEXT.md`, core `01`–`08`, extended `09`–`10`.
2. Add `shared/ethics.md` to `_config/CONTEXT.md` **When to Load** next to disclaimer and
   collaboration.

### A2. Delete `docs/superpowers/` from product `main`

**Defect.** The `obra/superpowers` *skill* is already gone from `skills-lock.json`. The leftover
*docs* tree (`docs/superpowers/{plans,specs,handoffs}/`) still ships. GitHub **Use this template**
has no exclude list: it copies the product default branch as-is. An instance that deletes the tree
gets it back on `git merge upstream` if product `main` still has it. An ICM audit classifies that
tree as `coexist-process`.

**Why it showed up:** the personal board deleted the tree locally so the working copy matches the
intended product. Until factory `main` drops it, a product-update merge can restore it.

**Ship:**

1. Delete `docs/superpowers/` from product `main`. Do not replace it with a README that keeps the
   tree in the template.
2. This handoff lives in that tree. After you implement Packages A and B, do not leave the tree on
   product `main`. Keep a copy of factory authoring on a **non-default branch** or in a private
   factory workspace if you still need the record. Templates do not copy other branches unless
   **Include all branches** is checked.
3. In `_config/shared/icm-conventions.md`, replace the **Coexisting conventions** bullet (the one
   that treats `docs/superpowers/` as historical process sitting beside ICM) with: factory
   authoring history is not product; live control is root `CONTEXT.md` plus
   `shared/meeting-process.md`; do not add a `stages/` pipeline to explain historical files. After
   the tree is gone, an ICM audit can report native ICM instead of `coexist-process`.
4. Changelog the removal when you cut it from `main`.

Intended wording: instance `_config/shared/icm-conventions.md` **Tooling vs. workspace content**
bullet **Factory authoring history is not product.** Port that bullet only; see **What not to
port** later.

### A3. Skills management: overlays are not Always-load protocol

**Defect.** Product treated a writing overlay as the same class of Always-load protocol as ethics.
The overlay is a committed constraint on an optional locked skill. Workspace content must still
travel without a skill install. Factory `main` pins `google-doc-style` in `skills-lock.json` but
does not ship an overlay file or a load-class contract.

**Why it showed up:** the ethics fix (A1) made the overlay look like the next Always-load file.
It is not.

**Ship:**

1. Add `_config/shared/google-doc-style-overlay.md`. Intended shape: instance
   `_config/shared/google-doc-style-overlay.md`. Generalize any instance-only wording; keep the
   product rules (real profile data vs sample placeholders, board "we", do not restyle agent
   contracts, do not edit vendored skills).
2. Add `_config/shared/icm-conventions.md` **Skills management**: lockfile vs gitignored skill
   trees vs committed overlays vs load lists vs harness-bundled skills; required protocol vs
   optional tooling; Always load vs chair-only vs on-demand; do not edit vendored skills; do not
   restyle agent contracts as public docs. Intended section: instance file of the same name.
3. Advisor Inputs (template, core `01`–`08`, extended `09`–`10`): overlay under **Load when writing
   to the user**, not **Always load**. `_config/CONTEXT.md` **When to Load** must use the same
   classes.
4. `conventions.md` states that the overlay is a writing load, not protocol. Chair root
   `CONTEXT.md` loads it when writing to the user or producing artifacts.
5. `meeting-process.md` sub-agent bundle: shared protocol (`disclaimer`, `collaboration`,
   `ethics`, `conventions`) plus overlay when writing. After A1, `ethics.md` belongs on that
   protocol list.
6. `advisors-extended/README.md`: keep the writing-overlay line when copying an advisor.

Do not vendor extra skills. Do not patch `.agents/skills/`. Harness-bundled skills stay host
tooling until they are pinned in `skills-lock.json` and given a committed overlay.

---

## Package B — when shipping trust and entity profile routing

Ship these guards in the same product work that adds Domain 2 `trust.md` and `_config/profile/entities/`.
Do not ship those folders and "clean them up later" on each clone.

### B1. Household facts stay in the family files; do not register Personal as an entity

**Defect.** The shipped family-profile contract already puts household facts in `personal.md`,
`financial.md`, `investments.md`, and `goals.md`. The entity router did not say "do not register
Personal as an entity." An agent can invent a Personal (or household) slug even on a clean
questionnaire.

**Why it showed up:** one personal board ran entity onboarding out of questionnaire order, thinned
`personal.md`, and parked household operations under `entities/personal/`. A board that finishes
general onboarding first must not create that folder. The factory guard still matters on a clean
run.

**Ship:**

1. In tracked `entities/CONTEXT.md` and the entity template notes: household identity, finance,
   investments, and actions live in the family files. Do not register Personal as an entity or
   planning-scope slug under `entities/`.
2. Keep general onboarding order as the product path: family questionnaire first, then in-depth
   onboard one real entity at a time.

Intended shape: instance `_config/profile/entities/CONTEXT.md` (Purpose and **Create or deepen**)
and `_config/profile/entities/_template/` notes. Strip instance-only binder and systems language.

### B2. Completed entity `CONTEXT.md` is a meeting router

**Defect.** The product described only the *in-progress* resume (`Current state`, `Resume inputs`,
`Next work`) and never a completed meeting router.

- `_config/profile/entities/_template/CONTEXT.md` was copy-instruction lines. Agents filled live
  entity `CONTEXT.md` files as interview resumes and left them that way after the completion check.
- `entity-onboarding.md` told every later session to follow **Next work** whenever `CONTEXT.md`
  existed, including after `in-depth` status.
- Root `CONTEXT.md`, setup, and profile routers assumed **Next work** was the load path. A meeting
  that loads a completed entity still opened a resume-shaped router (and those routers pointed at
  `entity-onboarding.md`).
- The completion check did not convert `CONTEXT.md` from resume to meeting router, did not require
  `Last Updated` on that file, and did not forbid leftover interview checkpoints.

**Why it showed up:** long session checkpoints and leftover "continue this domain" sentences are
interview residue. The specific recap text does not need to ship. The missing conversion step is
what lets that class of leftover persist.

**Ship:**

1. Post-onboarding meeting-router template: Purpose, Scope boundary, Status, Scoped load, Action
   register, Refresh / reopen, `Last Updated`. Intended shape: instance
   `_config/profile/entities/_template/CONTEXT.md`.
2. Teach `entity-onboarding.md` two states: resume sections while in progress; meeting router after
   the completion check.
3. Completion check conversion: strip **Current state** / **Resume inputs** / **Next work** /
   session checkpoints; put operational follow-up in `goals.md`; do not add the onboarding contract
   to the completed scoped-load table; stamp `Last Updated`.
4. Guard every "follow **Next work**" sentence: only when those resume sections exist. A completed
   router is not an interview. Apply the same guard on root `CONTEXT.md`, `_config/setup/CONTEXT.md`,
   `_config/profile/CONTEXT.md`, and `entities/CONTEXT.md`.
5. Completing a federated owner profile must still run the same meeting-router conversion. Do not
   leave domain-interview instructions in the local `CONTEXT.md`.

### B3. One control surface for in-depth onboarding status

**Defect.** `businesses.md` is a high-level compatibility summary. `entities/index.md` is the
status register. Live routing already follows the index **Next in-depth onboarding** line.

General onboarding still asks which entity receives the first in-depth pass and writes
`businesses.md` in the same step. If that answer is stored as an **Onboarding priority** or
"active in-depth" pointer in `businesses.md`, it is a second control surface. Entity completion
updates `index.md` only, so the summary pointer stays live after the interview is done.

**Why it showed up:** one board left a completed entity named as the active `businesses.md` target.
`businesses.md` is gitignored; do not port that sentence. The missing write rule is the product
piece.

**Ship:**

1. Do not put an active in-depth target in `businesses.md`. Point at `entities/index.md` for
   status.
2. If Domain 4 (entity registry) records the first selected entity, write it only on the index
   **Next in-depth onboarding** line.
3. The entity-onboarding completion check must clear that index line. It must not also have to
   edit `businesses.md`.

### B4. Split oversized profile files at write time (`trust.md` is the pattern)

**Defect.** Domain 2 still ships as a single required file, `_config/profile/trust.md`. General
onboarding should keep writing that one file. A later focused trust pass can grow it past a useful
load size. Completeness still needs a file named `trust.md` (first-launch check, questionnaire
Domain 2).

ICM already says every file answers one question and a step that blows the token budget must
re-scope Inputs. This product never applied that rule to **writes**. Domain 2 and
`trust-onboarding.md` said "save each answer to `trust.md`," so the agent appended identity,
succession, assets, sources, open questions, and the action register into one file that estate
meetings then loaded whole.

**Why it showed up:** a focused trust pass produced a ~36 KB single file. The split on that board
is local. Tracked load-path sentences and the write-time rule are the factory piece.

**Ship:**

1. Allow `trust.md` to be a thin shim to `trust/` with a `CONTEXT.md` router and section files.
   Do not require every clone to split on day one.
2. Advisor Inputs, `_config/profile/CONTEXT.md`, and `trust-onboarding.md` must follow the shim
   and load only the sections the question needs. Do not bulk-load `trust/`.
3. Keep the completeness gate on `trust.md`. If the shim exists, writes go to the named section
   files; do not reconstitute one giant file.
4. `.gitignore` already ignores `_config/profile/*` except tracked routers. A `trust/` folder stays
   local. A comment that Domain 2 may be a shim plus section files is enough; do not un-ignore
   instance `trust/CONTEXT.md`.
5. Ship **Keep files load-scoped (split at write time)** in `_config/shared/icm-conventions.md`.
   That file is committed Layer-3 overlay: clones get it with no skill install. Point
   `_config/profile/CONTEXT.md` **Updating Profile Files** at it. Entity in-depth already splits
   by question (`overview.md`, `governance.md`, `goals.md`, `sources.md`); Domain 2 was the hole.

Do **not** put the rule only in the `icm` skill. Workspace content must travel without a skill
install. Do **not** replace Domain 2 with a `trust/` folder on a fresh clone: general onboarding
still writes one short `trust.md`. The split is required at the focused pass that would mix
independently loadable concerns (identity, action register, source inventory, open questions,
onboarding status) into a file loaded as a whole. Keep a thin shim when the completeness gate
still names `trust.md`.

Write-path contracts to align:

- `questionnaire.md` Domain 2 — first pass may share one file; if `trust.md` is already a shim,
  write to the named section files.
- `trust-onboarding.md` — save to the matching section file, not an ever-growing single file.
- `_config/setup/CONTEXT.md` — same shim-aware Domain 2 write.

Do not add a byte or token cutoff as the primary trigger. One-question-per-file plus "split
before the next mixed write" is the control. A numeric cap invites packing until the cap.

Intended wording: instance `_config/shared/icm-conventions.md` **Keep files load-scoped (split at
write time)**. Generalize the worked example ("a focused trust pass", not a named family trust).

---

## Optional (not required for meetings)

Joint onboarding of two related entities is allowed when a relationship is necessary, but the
product has no co-primary pattern. A short note in `entity-onboarding.md` is enough if you want
later boards to keep two `CONTEXT.md` files in sync without inventing resume coupling.

---

## What not to change

- Do not copy gitignored profile content from the personal board.
- Do not register Personal as an entity in templates, examples, or setup.
- Do not restyle `AGENTS.md`, `CONTEXT.md`, or `_config/shared/` protocol as public docs.
- Do not vendor extra skills or patch `.agents/skills/`.
- Do not add a numeric file-size or token cap as the split trigger.
- Do not require a fresh clone to start with `trust/` already split.
- Do not un-ignore instance `trust/` or entity folders.
- Do not port instance-only boundaries (named finance or systems workspaces, Google Drive binder
  paths, machine-local `rclone` notes).
- When editing `icm-conventions.md`, port only the sections named in this handoff (**Keep files
  load-scoped**, **Factory authoring history is not product**, **Skills management**, and the
  recursive-router lines that name `entities/CONTEXT.md` and `trust/CONTEXT.md` *once those
  folders ship*). Do not port **External official records** or other instance-only sections.
- Do not leave `docs/superpowers/` on product `main` after this work (Package A2).

---

## Suggested file map

Use this as a checklist, not a mandate to touch unrelated prose.

### Package A (factory `main` today)

| File | Change |
| --- | --- |
| `advisors/_template/CONTEXT.md` | `ethics.md` on Always load; overlay under **Load when writing to the user** |
| `advisors/01`–`08` and `advisors-extended/09`–`10` `CONTEXT.md` | Same Inputs as the template |
| `_config/CONTEXT.md` | When to Load classes; Contents line for the overlay |
| `_config/shared/icm-conventions.md` | Skills management; replace Coexisting conventions bullet |
| `_config/shared/google-doc-style-overlay.md` | Create |
| `_config/shared/conventions.md` | Overlay is a writing load |
| `_config/shared/meeting-process.md` | Sub-agent bundle: protocol + overlay when writing |
| `CONTEXT.md` (root) | Load overlay when writing; ethics already via advisors |
| `advisors-extended/README.md` | Keep overlay line when copying an advisor |
| `docs/superpowers/` | Delete from product `main` after the rest of this handoff is implemented |
| `CHANGELOG.md` | Ethics load, overlay/load classes, Superpowers docs removal |

### Package B (with trust/entity product work)

| File | Change |
| --- | --- |
| `_config/profile/entities/CONTEXT.md` | No Personal slug; completed `CONTEXT.md` is a meeting router; follow **Next work** only when resume sections exist |
| `_config/profile/entities/_template/CONTEXT.md` | Post-onboarding meeting-router factory |
| `_config/setup/entity-onboarding.md` | Two states + conversion in the completion check; clear index in-progress line only |
| `_config/setup/trust-onboarding.md` | Write to section files; follow the shim |
| `_config/setup/questionnaire.md` | Domain 2 shim-aware write; Domain 4 writes next-entity only on `index.md` |
| `_config/setup/CONTEXT.md` | Same write rules; follow **Next work** only when resume sections exist |
| `_config/profile/CONTEXT.md` | Follow shim into `trust/`; scoped entity load; **Updating Profile Files** points at load-scoped writes |
| Root `CONTEXT.md` | Same **Next work** guard |
| Advisor Inputs **Load when trust or entity scoped** | Follow `trust.md` into `trust/` |
| `.gitignore` | Comment that Domain 2 may be a shim plus `trust/` section files |
| `_config/shared/icm-conventions.md` | **Keep files load-scoped**; recursive routers for `entities/` and `trust/` when those exist |

---

## Verification

After implementing, confirm:

- [ ] Every advisor **Always load** list includes `ethics.md`. `_config/CONTEXT.md` **When to Load** matches **Contents**.
- [ ] `google-doc-style-overlay.md` exists. Advisor Inputs load it under **Load when writing to the user**, not **Always load**.
- [ ] `icm-conventions.md` has **Skills management** and no longer describes `docs/superpowers/` as a coexisting process layer.
- [ ] `docs/superpowers/` is gone from product `main` (including this file). Authoring copies, if kept, are not on the template default branch.
- [ ] `CHANGELOG.md` records the product changes.
- [ ] Entity template `CONTEXT.md` is a meeting router, not an interview resume. Completion check converts live files to that shape.
- [ ] No product sentence tells an agent to follow **Next work** unless those resume sections exist.
- [ ] No product sentence puts an active in-depth target in `businesses.md`.
- [ ] Tracked entity docs forbid a Personal or household slug under `entities/`.
- [ ] Domain 2 may stay one short `trust.md` after general onboarding; a focused pass that would mix independently loadable concerns splits at write time and keeps a `trust.md` shim.
- [ ] No gitignored profile data from the personal board was committed here.
