# Entity profile router

## Purpose

Route entity-scoped work to a small private profile without loading unrelated folders.
Real entity profiles are local-only. `_template/` is the tracked factory pattern.

Household identity, finance, investments, and actions live in the core profile files
(`../personal.md`, `../financial.md`, `../investments.md`, `../goals.md`). Do not register
Personal as an entity.

A living trust or similar estate vehicle lives in `../trust.md` (or `../trust/` if that file
has been split). Do not register that estate vehicle as an entity. Land trusts, LLCs,
corporations, and other operating or holding structures belong here.

This directory exists only after general onboarding records at least one entity. If
`index.md` is absent, there is no entity layer: stay on the core profile files and keep
meeting folders flat under `meetings/<topic-slug>/`.

## Index

Read `index.md` first when this directory exists. It records each entity's stable slug,
relationship, onboarding status, and available profile files. `index.md` is local-only.

Allowed onboarding states:

- `basic` — `overview.md` exists and contains enough information to route a meeting.
- `in-depth` — the relevant detailed profile files exist and the completion check passed.
- `needs-refresh` — facts are older than 12 months or a material event made them unreliable.

Suggested `index.md` shape (create on first entity; do not commit real names):

```markdown
# Entity registry

Last Updated: YYYY-MM-DD

| Entity | Slug | Relationship | Status | Available files |
| --- | --- | --- | --- | --- |
| Legal Name, LLC | `legal-name-llc` | Owner and role | `basic` | `overview.md` |
```

## Load an entity

1. Select the entity or entities from `index.md`.
2. If the selected folder contains `CONTEXT.md`, load it as the entity's scoped meeting
   router. Follow **Current state**, **Resume inputs**, and **Next work** only when those
   resume sections exist *and* the user asked to continue that entity's in-depth onboarding.
   A completed router is not an interview. Do not start in-depth onboarding because a
   meeting mentioned the entity.
3. Load `overview.md` from each selected folder.
4. Load only the detailed files that match the question:
   - `governance.md` — ownership, control, formation, agreements, and succession.
   - `operations.md` — activities, people, systems, customers, vendors, and operating model.
   - `financial.md` — revenue, expenses, balance sheet, cash, debt, and source documents.
   - `tax.md` — tax classification, elections, filings, payroll, and tax concerns.
   - `risk-insurance.md` — contracts, liabilities, guarantees, licensing, and coverage.
   - `goals.md` — the canonical entity action register, priorities, decisions, constraints,
     open questions, and next review.
   - `sources.md` — reviewed and outstanding evidence. Load only for source provenance,
     document review, or outstanding-record work.
5. Do not load files from unrelated entity folders.
6. Entity-scoped board meetings live at `meetings/<entity-slug>/<topic-slug>/`, not in this
   profile folder. Follow `../../../meetings/CONTEXT.md`. Create the scope folder only with
   the first meeting in that scope. Household meetings use `meetings/personal/`. A living-trust
   meeting uses `meetings/trust/` when `../trust.md` exists.
7. When a meeting changes this entity's standing facts, write the delta into the matching
   files in that entity folder in the same session. Follow `../../shared/meeting-process.md`
   **Profile write-back**. That is a scoped fact update, not onboarding. Do not restart an
   interview.

## Create or deepen an entity

- For basic registration, create only `<entity-slug>/overview.md` and update `index.md`.
- Do not add a Personal or household slug under this directory.
- For in-depth onboarding, follow `../../setup/entity-onboarding.md` and create only the
  detailed files that apply. In-depth onboarding is optional. General onboarding is complete
  without it.
- If `<entity-slug>/CONTEXT.md` has **Current state**, **Resume inputs**, and **Next work**,
  it is the in-progress resume contract: follow those sections and do not restart completed
  domains. After the completion check, replace those resume sections with the meeting-router
  shape in `_template/CONTEXT.md`.
- During in-depth onboarding, keep all output in the selected entity folder. Do not create a
  meeting record. Create `goals.md` when the first actionable item appears and use it as the
  single canonical action register across every domain.
- When source documents are used, create `<entity-slug>/sources.md` from `_template/sources.md`.
  A basic entity with no reviewed sources does not require `sources.md`.
- Copy field structure from `_template/`; do not place real data in the template.
- Stamp every private profile file with `Last Updated: YYYY-MM-DD`.
- Update the entity's status in `index.md` after verification.

## Prioritize actions across entities

When the user asks what to prioritize across entities or the whole profile:

1. Read `index.md`.
2. Load `../goals.md` for household actions. Load only `goals.md` from each registered entity
   that has one. If `../trust.md` exists, load only its action list (the file itself, or
   `../trust/planning-actions.md` when that folder exists).
3. Rank unchecked actions using deadlines, legal or compliance exposure, dependency order,
   cash-flow effect, downside severity, reversibility, and the user's available time.
4. Answer in conversation. Do not create a `meetings/` folder for the ranking unless the user
   asks to save it or then starts work on a named action.
5. Record household actions in `../goals.md` and entity actions in that entity's `goals.md`.
   Do not create a duplicate global action register.
