# Handoff: ICM cleanup product rules

Last Updated: 2026-08-27

This is product structure maintenance on the factory repository
(`wekoodo/ai-board-of-advisors`), not a board meeting and not onboarding.

- Do not create a `meetings/` record.
- Do not run or change the personal-board onboarding flow beyond the queue item in scope.
- Do not copy private profile content from a personal board.
- Do not push unless the user asks.
- Work one queue item per session, and then stop.

## Next session

**Next open item:** Item 3 — remove factory authoring history from product `main`.

Present Item 3 using its **Issue** and **Proposed resolution** sections. Wait for the user to say
**go** or revise the resolution. Do not edit files before approval.

## Protocol (do not skip)

Work **one queue item per session**, in order:

1. Load this file.
2. Present the next open item: a short refresh of the issue and the proposed resolution.
3. Stop and wait for the user to say **go** or change the resolution.
4. Implement that item only. Keep the change set scoped.
5. Run the item's verification checks and the ICM audit when routing structure changes.
6. Update `CHANGELOG.md` for that item.
7. Update this handoff before committing:
   - Move the completed item from **Queue** to **Done**.
   - Record the files changed and verification performed.
   - Leave the remaining items in **Queue**.
   - Set **Next session** to the next open item.
   - Stamp `Last Updated`.
8. Commit all tracked files changed for that item, including this handoff.
9. Stop the session. Tell the user what landed, provide the commit hash, and explain how to resume.
   Do not present or start the next item.

If the user asks to skip, defer, or change an item, update this handoff, set **Next session**, commit
the logger change, and stop. Do not start the next item.

Item 3 is the final-item exception: it deletes all of `docs/superpowers/`, including this handoff.
Its commit records the deletion and ends the cleanup. Do not recreate the handoff elsewhere on
product `main`.

## Git rules

- Work on `main` unless the user directs otherwise.
- Use one implementation commit per queue item.
- Commit only files that belong to the active item. Preserve unrelated user changes.
- Use a short imperative commit subject with no AI attribution or `Co-Authored-By` trailer.
- Do not push unless the user asks.
- Leave the tracked working tree clean after each item commit.
- Private profile files remain gitignored and must not enter a commit.

## Product boundary

The sibling personal board at
`/home/angellops/projects/board-of-advisors-drewangell` contains worked product-shaped contracts,
but it also contains real family, trust, and entity data.

When consulting that repository:

- Port only tracked contract shape and the specific sections named by the active item.
- Generalize instance wording.
- Do not copy entity slugs, names, amounts, Drive URLs, local paths, or gitignored profile data.
- Do not edit vendored skills under `.agents/skills/`.
- Do not restyle agent contracts or shared protocol as public documentation.

## Decisions already made

- Implement the three Package A corrections in this repository.
- Keep the writing overlay separate from Always-load protocol.
- Remove `docs/superpowers/` from product `main` as the final item.
- Do not introduce trust or entity routing as part of this cleanup.
- Track the four Package B requirements as GitHub feature issues instead of burying them in this
  temporary handoff.

## Package B GitHub issues

These issues are outside this cleanup queue. Do not implement them unless the user starts that
feature work separately:

- [#3 — Keep household facts out of entity profile routing](https://github.com/wekoodo/ai-board-of-advisors/issues/3)
  (handoff B1)
- [#1 — Convert completed entity onboarding resumes into meeting routers](https://github.com/wekoodo/ai-board-of-advisors/issues/1)
  (handoff B2)
- [#4 — Use one control surface for entity onboarding status](https://github.com/wekoodo/ai-board-of-advisors/issues/4)
  (handoff B3)
- [#2 — Split oversized trust profiles at write time](https://github.com/wekoodo/ai-board-of-advisors/issues/2)
  (handoff B4)

Each issue is gated on the future product work that adds the trust or entity subsystem it governs.

## Queue

Status values: `open` | `done` | `skipped`

### Item 3 — remove factory authoring history from product `main`

**Status:** `open`

**Issue**

The removed Superpowers skill no longer appears in `skills-lock.json`, but its plans, specs, and
handoffs remain under `docs/superpowers/`. GitHub templates copy the default branch as-is, and an
upstream merge can reintroduce this authoring tree into personal boards. The ICM audit therefore
classifies the repository as `coexist-process` instead of native ICM.

**Proposed resolution**

1. Replace the **Coexisting conventions** bullet in `_config/shared/icm-conventions.md` with the
   product rule that factory authoring history is not product:
   - Keep plans, specs, and process-pack trees off the product default branch.
   - Keep live control in root `CONTEXT.md` and `_config/shared/meeting-process.md`.
   - Do not add a `stages/` pipeline to explain historical files.
2. Record the removal in `CHANGELOG.md`.
3. Delete all of `docs/superpowers/`, including this handoff. Do not leave a README placeholder.

**Verification**

- Confirm `docs/superpowers/` no longer exists on `main`.
- Confirm no tracked file describes Superpowers authoring docs as a live process or ICM layer.
- Run the ICM audit and confirm that it reports `icm-native`.
- Confirm the tracked working tree is clean after the commit.

## Done

### Item 2 — separate the writing overlay from Always-load protocol

**Status:** `done`

**Issue**

`google-doc-style` was pinned in `skills-lock.json`, but the product had no committed board overlay
or load-class contract. A writing overlay is not the same class as legal, ethical, collaboration,
or response protocol. It belongs in writing-time Inputs, not **Always load**.

**Resolution**

- Added a committed board overlay that preserves real profile facts, board voice, agent-contract
  structure, shared protocol, and the installed skill boundary.
- Added the **Skills management** ownership and load-class contract to the ICM conventions.
- Added **Load when writing to the user** to the advisor template and advisors `01`–`10`, with the
  overlay outside **Always load**.
- Aligned the chair, config router, shared conventions, meeting process, and extended-advisor
  instructions with the same writing-time load class.
- Recorded the correction in `CHANGELOG.md`.

**Files changed**

- `_config/shared/google-doc-style-overlay.md`
- `_config/shared/icm-conventions.md`
- `_config/shared/conventions.md`
- `_config/shared/meeting-process.md`
- `_config/CONTEXT.md`
- `CONTEXT.md`
- `advisors/_template/CONTEXT.md`
- `advisors/01-financial-planner/CONTEXT.md` through
  `advisors/08-insurance-specialist/CONTEXT.md`
- `advisors-extended/09-oil-gas-specialist/CONTEXT.md`
- `advisors-extended/10-storage-facility-advisor/CONTEXT.md`
- `advisors-extended/README.md`
- `CHANGELOG.md`
- `docs/superpowers/handoffs/2026-08-27-icm-cleanup-product-rules.md`

**Verification performed**

- Confirmed that the overlay exists as workspace content and contains the real-data safeguard.
- Confirmed that all 11 advisor contracts load the overlay once under **Load when writing to the
  user** and keep `ethics.md` once under **Always load**.
- Confirmed that the chair, config router, shared conventions, and meeting process use the same
  load classes.
- Confirmed that no files under `.agents/skills/` changed.
- Ran `git diff --check` successfully.
- Ran the ICM audit successfully. It reported `coexist-process`, as expected until Item 3 removes
  `docs/superpowers/`.

### Item 1 — load `ethics.md` consistently

**Status:** `done`

**Issue**

`_config/CONTEXT.md` said that every advisor loads `shared/ethics.md`, but the advisor Inputs and
the config router's **When to Load** section omitted it. The stable reference contract and the
scoped load lists disagreed.

**Resolution**

- Added `../../_config/shared/ethics.md` after `collaboration.md` in the advisor template, core
  advisors `01`–`08`, and extended advisors `09`–`10`.
- Added `shared/ethics.md` to `_config/CONTEXT.md` **When to Load**.
- Recorded the correction in `CHANGELOG.md`.

**Files changed**

- `advisors/_template/CONTEXT.md`
- `advisors/01-financial-planner/CONTEXT.md` through
  `advisors/08-insurance-specialist/CONTEXT.md`
- `advisors-extended/09-oil-gas-specialist/CONTEXT.md`
- `advisors-extended/10-storage-facility-advisor/CONTEXT.md`
- `_config/CONTEXT.md`
- `CHANGELOG.md`
- `docs/superpowers/handoffs/2026-08-27-icm-cleanup-product-rules.md`

**Verification performed**

- Confirmed that all 11 advisor contracts contain the same Always-load protocol list.
- Confirmed that `_config/CONTEXT.md` **Contents** and **When to Load** agree.
- Confirmed that the advisor diff changes only the Always-load lists, with no identity or process
  changes.
- Ran `git diff --check` successfully.
- Ran the ICM audit successfully. It reported `coexist-process`, as expected until Item 3 removes
  `docs/superpowers/`.
