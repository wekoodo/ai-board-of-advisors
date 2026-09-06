# In-depth entity onboarding

## Purpose

Deepen one selected entity profile when the user is ready to work on that entity. Do not expand the
scope to other entities unless a relationship is necessary to understand the selected entity.

This route is optional. General onboarding is complete with a basic `overview.md` per known entity.
Do not start this interview because the general profile is complete, because a meeting mentioned
the entity, or because `index.md` lists a next candidate. Start only when the user asks to deepen
or to reopen a domain of a registered entity that already has an index entry and `overview.md`.
A material event or new source is not that request: mark affected facts stale and write a scoped
update; do not start this interview.

If the user asked to deepen an entity that has no index entry or no `overview.md`, load
`entity-registration.md` first, then return here.

This contract is for in-progress onboarding and for an explicit refresh of a completed entity. A
completed entity `CONTEXT.md` is a meeting router. Loading it during a meeting does not start this
interview.

## Inputs

- `_config/profile/entities/CONTEXT.md` — entity routing and file ownership.
- `_config/profile/entities/index.md` — selected entity, relationships, and status.
- `_config/profile/entities/<entity-slug>/CONTEXT.md` — while onboarding is in progress, this file
  is a resume contract. Follow **Current state**, **Resume inputs**, and **Next work** when those
  sections exist. After the completion check, the same file is a meeting router; do not treat
  **Refresh / reopen** as an invitation to restart the interview.
- `_config/profile/entities/<entity-slug>/overview.md` — known facts and open questions.
- Source documents identified by the user or assigned from `_inbox/`.

## Output ownership

- Entity onboarding is profile maintenance, not a board meeting.
- Write every durable onboarding output under `_config/profile/entities/<entity-slug>/`.
- Do not create a `meetings/` record, meeting artifact, or meeting-index entry for onboarding.
- Use `<entity-slug>/goals.md` as the single canonical action register. Create it when the first
  actionable item appears, even when the Goals interview domain has not started.
- Add actions discovered in any domain to the canonical action register. Domain files keep the
  supporting facts, decisions, risks, and open questions.
- Record every reviewed, deferred, superseded, or outstanding source in the entity's `sources.md`.
  Move a confirmed local source from `_inbox/` to
  `_config/profile/entities/<entity-slug>/sources/`; do not create a meeting `inputs/` folder.

## Interview

**Create the resume contract when it is missing.** If the selected entity has an index entry and
`overview.md` but no `CONTEXT.md`, or its `CONTEXT.md` is not a completed meeting router and
lacks **Current state**, **Resume inputs**, and **Next work**, write that file as the resume
contract *before* asking in-depth questions. Use this shape:

```markdown
# <Entity name> — in-depth onboarding (in progress)

Last Updated: YYYY-MM-DD

## Current state
- Depth: `basic` (in-progress deepen; not yet `in-depth`)
- Completed domains: none
- Partial domain: none
- Domain files written: none

## Resume inputs
- `overview.md`
- `../index.md` row for this slug

## Next work
- Ask the first unanswered Governance questions (or the next unfinished domain).
- Do not recap completed domains.
```

Reuse overview facts. Do not restart general onboarding. Do not copy this resume shape into a
completed meeting router.

**Resume.** If those three sections exist, follow them. Do not restart a domain that file marks
complete. On a fresh session, the first user-facing turn follows **Next work** exactly: ask the
unanswered questions listed there, and do not recap completed domains. Ask no more than two or
three closely related questions at a time. After each answered cluster, and before pausing,
update **Current state**, **Resume inputs**, **Next work**, and the domain file. Partial answers
in an unfinished domain belong in **Next work** and in that domain file as known-so-far, not as
a completed domain.

**Completed router.** If the selected entity `CONTEXT.md` is already a post-onboarding meeting
router (Purpose, Scope boundary, Status, Scoped load, Action register, **Refresh / reopen**) and
has no **Next work**, do not run this interview unless the user explicitly asks to refresh or
reopen a domain. Then reopen that domain only. Keep the meeting router; do not replace it with
resume sections. A new source or material event is not that ask.

Otherwise proceed conversationally and save each completed domain before moving on. Stamp
`Last Updated` on the file and `As of` on each section just confirmed
(`_config/profile/CONTEXT.md` **Fact dates**):

1. **Governance** — formation, ownership, control, managers, governing documents, registrations,
   decision authority, transfer restrictions, succession, and related entities.
2. **Operations** — activities, revenue model, people, customers, vendors, systems, assets,
   intellectual property, and operating constraints.
3. **Financial** — revenue, expenses, profitability, cash, banking, assets, liabilities, debt,
   guarantees, reporting, and available statements.
4. **Tax** — classification, elections, filing jurisdictions, payroll, owner compensation, material
   transactions, compliance calendar, and known concerns.
5. **Risk and insurance** — contracts, licenses, disputes, liabilities, guarantees, privacy or cyber
   exposure, and existing coverage.
6. **Goals** — near-term priorities, longer-term direction, pending decisions, constraints, open
   questions, and next review.

Create only the files that apply. Use the matching files in
`_config/profile/entities/_template/` as the field structure.

## Completion check

Before changing the entity status to `in-depth`:

- Confirm `overview.md` and every applicable detailed file exist. If a named path is a shim,
  follow `_config/shared/icm-conventions.md` **Resolve a named profile path**; the named path
  must still exist.
- Confirm each resolved owning file has a valid `Last Updated: YYYY-MM-DD` line.
- Confirm contradictions and unavailable facts are visible as open questions rather than guesses.
- When documents were used, confirm `sources.md` identifies what was reviewed and what remains
  outstanding. Do not require `sources.md` for an entity with no reviewed materials.
- Confirm `goals.md` (the named path, or its resolved action register if that path is a shim)
  contains the canonical action register and every actionable item discovered during onboarding.
- Replace any interview-resume sections in `CONTEXT.md` (**Current state**, **Resume inputs**,
  **Next work**, session checkpoints) with the post-onboarding meeting-router shape from
  `_template/CONTEXT.md`. Stamp `Last Updated: YYYY-MM-DD`. Put remaining operational follow-up in
  `goals.md` (the resolved action file when that path is a shim; never copy the register into the
  shim). Do not leave instructions that a fresh session should continue the interview. Do not
  add this onboarding contract to the completed router's scoped-load table.
- Update `_config/profile/entities/index.md` with depth `in-depth`, freshness `current`,
  empty Stale reasons, available files, and next review.

If a first-time deepen is still incomplete, keep depth at `basic` and keep the resume contract.
If an explicit reopen of a completed entity is still incomplete, keep depth `in-depth`, keep
the meeting router, and checkpoint partial answers only in the reopened domain file. Do not
convert the meeting router back into an interview resume. Do not replace depth with a
freshness flag. If facts became unreliable, set freshness `stale` and the affected Stale reasons; keep
the recorded depth.
