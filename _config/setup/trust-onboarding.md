# Focused trust onboarding

## Purpose

Deepen a living-trust (or similar estate-vehicle) profile when the user asks. This route is
optional. General onboarding is complete without `trust.md`. Do not start this interview because
the general profile is complete or because an estate-planning meeting mentioned a will or
beneficiaries.

A living trust is a household estate vehicle. It is not an entity. Land trusts and operating
entities belong under `_config/profile/entities/`.

## Inputs

| Layer | Path and scope | Use |
| --- | --- | --- |
| Layer 3 router | `../profile/CONTEXT.md` — trust-scoped load rules | Keep profile loading narrow |
| Layer 3 profile | `../profile/trust.md`, or that shim plus `../profile/trust/` section files | Authoritative facts |
| Layer 3 entity routing | `../profile/businesses.md` and `../profile/entities/index.md` — ownership summaries only, when those files exist and funding or ownership is active | Reconcile trust and entity relationships without loading entity folders |
| User sources | Only documents the user identifies for this question | Verify facts without loading a complete binder |

## Process

1. If `trust.md` does not exist yet, create it with identity, trustees, beneficiaries, connected
   assets, professionals, open questions, and a short action list. Stamp
   `Last Updated: YYYY-MM-DD`.
2. If `trust.md` is already a shim to `trust/`, write facts to the resolved owning sections.
   Follow `_config/shared/icm-conventions.md` **Resolve a named profile path**. Do not
   reconstitute a single file.
3. Follow `_config/shared/icm-conventions.md` **Keep files load-scoped**. A first-pass
   `trust.md` may hold short answers. If a focused pass would mix independently loadable
   concerns (identity, succession, connected assets, professionals, sources, open questions,
   planning actions) into one file loaded as a whole, split into `trust/` with a `CONTEXT.md`
   router and keep `trust.md` as a thin shim.
4. Ask one conversational question at a time. Save each answer before moving on.
5. Classify facts per `_config/shared/conventions.md` **Evidence and calculation**. Document
   facts are sourced; user confirmations are user-reported; legal inferences are assumed until
   a sourced rule or licensed determination supports them; unresolved professional
   determinations stay open questions.
6. Keep trust actions in the resolved action file the folder router names (worked example:
   `trust/planning-actions.md`). If `trust.md` is still a single file, keep them there. Never
   copy that register into `trust.md` once it is a shim. Do not create a duplicate action
   register.
7. Do not create a `meetings/` record, meeting artifact, transcript, or meeting-index entry.

## Completion check

Before marking focused trust onboarding complete:

- Confirm identity, grantors, trustees, authority, beneficiaries, succession, incapacity, death
  administration, funding, connected entities (if any), professional relationships, and open
  questions are documented or explicitly unknown.
- Confirm every unresolved item is answered, deferred, or assigned to an external owner with a
  next step.
- Confirm `trust.md` and each edited `trust/` section file (if any) have a valid
  `Last Updated: YYYY-MM-DD` line.
