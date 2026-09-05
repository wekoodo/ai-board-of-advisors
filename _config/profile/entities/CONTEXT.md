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

Tracked router and template files ship in this directory. The entity layer is active only
when `index.md` exists. If `index.md` is absent, stay on the core profile files and keep
meeting folders flat under `meetings/<topic-slug>/`. If `index.md` is created later, leave
existing flat meeting folders in place.

## Index

If `index.md` is absent, the entity layer is inactive. Otherwise read `index.md` first. It
records each entity's stable slug, relationship, onboarding status, and available profile
files. `index.md` is local-only.

Allowed depth values (Status column — do not replace these with a freshness flag):

- `basic` — `overview.md` exists and contains enough information to route a meeting.
- `in-depth` — the relevant detailed profile files exist and the completion check passed.

Freshness is a separate column. `current` is the default. If an older index has no Freshness
column, treat missing values as `current`. `stale` means facts are older than 12 months or a
material event made them unreliable. A stale `in-depth` entity is still in-depth. A
new source or material event sets freshness `stale` on the index Freshness column (and the
entity router Freshness line) and prompts a scoped fact update; it does not start an
interview. After those facts are confirmed, set freshness `current`. Do not write freshness
into overview onboarding status.

Suggested `index.md` shape (create on first entity; do not commit real names):

```markdown
# Entity registry

Last Updated: YYYY-MM-DD

| Entity | Slug | Relationship | Status | Freshness | Available files |
| --- | --- | --- | --- | --- | --- |
| Legal Name, LLC | `legal-name-llc` | Owner and role | `basic` | `current` | `overview.md` |
```

## Load an entity

1. Select the entity or entities from `index.md`.
2. If the selected folder contains `CONTEXT.md`, load it as the entity's scoped meeting
   router. Follow **Current state**, **Resume inputs**, and **Next work** only when those
   resume sections exist *and* the user asked to continue that entity's in-depth onboarding.
   A completed router is not an interview. Do not start in-depth onboarding because a
   meeting mentioned the entity.
3. Load `overview.md` from each selected folder. If a named path is a shim, follow
   `../../shared/icm-conventions.md` **Resolve a named profile path**.
4. Load only the detailed files that match the question (resolve shims the same way):
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
   profile folder. Follow `../../../meetings/CONTEXT.md` **Existing records stay put** (including
   occupancy: do not nest inside a path that is already a meeting record). Create the scope
   folder only with the first meeting in that scope, and only when that path is not already a
   meeting record. Household meetings use `meetings/personal/`. A living-trust meeting uses
   `meetings/trust/` when `../trust.md` exists.
7. When a meeting changes this entity's standing facts, write the delta into the matching
   files in that entity folder in the same session. Follow `../../shared/meeting-process.md`
   **Profile write-back**. That is a scoped fact update, not onboarding. Do not restart an
   interview.

## Create or deepen an entity

- After general onboarding, register a new entity with `../../setup/entity-registration.md`.
  Reuse `../businesses.md`. Do not restart household onboarding. Preserve every existing
  entity's status.
- For basic registration during general onboarding or that later route, create only
  `<entity-slug>/overview.md` and update `index.md`.
- Do not add a Personal or household slug under this directory.
- For in-depth onboarding, follow `../../setup/entity-onboarding.md` and create only the
  detailed files that apply. In-depth onboarding is optional. General onboarding is complete
  without it.
- On an explicit deepen request, if `<entity-slug>/CONTEXT.md` is missing or is not a
  completed meeting router and lacks **Current state**, **Resume inputs**, and **Next work**,
  that onboarding contract creates the resume sections before asking in-depth questions.
- If those resume sections exist, follow them and do not restart completed domains. After the
  completion check, replace those resume sections with the meeting-router shape in
  `_template/CONTEXT.md`.
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
   that has one. If `../trust.md` exists, load only its action list (the resolved action file
   the folder router names). If a named path is a shim, follow
   `../../shared/icm-conventions.md` **Resolve a named profile path** and load the resolved
   action register, not the shim alone.
3. Rank unchecked actions using deadlines, legal or compliance exposure, dependency order,
   cash-flow effect, downside severity, reversibility, and the user's available time.
4. Answer in conversation. Do not create a `meetings/` folder for the ranking unless the user
   asks to save it or then starts work on a named action.
5. Record household actions in `../goals.md` and entity actions in that entity's `goals.md`.
   If a named path is a shim, edit the resolved action file; never copy the register into the
   shim. Do not create a duplicate global action register.
