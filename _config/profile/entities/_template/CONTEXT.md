# Entity profile router

Last Updated: YYYY-MM-DD

Copy this folder to a stable lowercase slug under `entities/`. General onboarding requires only
`overview.md`. Create the remaining files during in-depth onboarding when they apply.

Every file answers one question and begins with `Last Updated: YYYY-MM-DD`.

After in-depth onboarding completes, this `CONTEXT.md` is the **meeting** router for the entity.
It is not an interview resume. Do not keep **Current state**, **Resume inputs**, or **Next work**
after the completion check. While onboarding is in progress, `../../../setup/entity-onboarding.md`
owns those resume sections.

## Purpose

Route this entity's work to the smallest applicable profile set without loading unrelated entities
and without restarting onboarding.

## Scope boundary

1. This folder owns the entity's legal identity, operations, finances, tax facts, risk, and the
   action register in `goals.md`.
2. Related household, trust, or entity profiles are cross-links only. Do not copy their action
   registers here.
3. Record each action once, in the profile that owns it.

## Status

- Entity status (depth): `basic` | `in-depth`
- Freshness: `current` | `stale`
- Next review: YYYY-MM-DD, or earlier after a material event.
- Do not restart onboarding unless the user asks to refresh or correct the profile.

## Scoped load

Load this file and only the rows that match the task. If a named path is a shim, follow
`../../../shared/icm-conventions.md` **Resolve a named profile path**.

| Layer | Path | Load for |
| --- | --- | --- |
| Stable profile | `overview.md` | Identity, relationship, purpose, and open questions |
| Action register | `goals.md` | Priorities, constraints, open questions, and next review |
| Evidence inventory | `sources.md` | On demand: reviewed and outstanding records |
| Domain | `governance.md` | On demand: ownership, control, agreements, succession |
| Domain | `operations.md` | On demand: activities, people, systems, operating model |
| Domain | `financial.md` | On demand: revenue, cash, assets, liabilities, reporting |
| Domain | `tax.md` | On demand: classification, filings, payroll, tax concerns |
| Domain | `risk-insurance.md` | On demand: contracts, liabilities, coverage |
| Related | named household, trust, or entity file | On demand: a documented relationship only |

Omit domain rows that do not apply. Do not add `../../../setup/entity-onboarding.md` to this table
after onboarding is complete.

## Action register

`goals.md` is the canonical action register. Load it for follow-up work, prioritization, and
next-review timing (the resolved action file when that path is a shim; never copy the register
into the shim). Domain files keep supporting facts.

## Board meetings

Entity-scoped meetings live under `meetings/<entity-slug>/<topic-slug>/`, not in this profile
folder. Follow `../../../../meetings/CONTEXT.md` **Existing records stay put**. Create the scope
folder only with the first meeting, and only when that path is not already a meeting record.
When a meeting changes standing facts for this entity, write those facts into the matching
files in this folder in the same session. Follow `../../../shared/meeting-process.md`
**Profile write-back**. Do not leave standing state only in `minutes.md`.

## Refresh / reopen

A material event or new source marks affected facts stale (index Freshness column and this
router's Freshness line, not overview onboarding status) and prompts a scoped fact review in
the current meeting (write-back). After those facts are confirmed, set Freshness `current`.
That is not an interview. Do not load
`../../../setup/entity-onboarding.md` unless the user explicitly asks to refresh or reopen a
domain. Then follow that contract for the reopened domain only. Do not recap completed domains.
Do not treat a meeting load of this file as an onboarding session.
