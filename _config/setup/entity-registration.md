# Basic entity registration (after general onboarding)

## Purpose

Register one or more operating or holding entities when the five-file core profile already
exists. Collect only missing basics. Do not restart household onboarding. Do not start in-depth
entity onboarding unless the user also asked to deepen.

Use this route when the user explicitly asks to add, register, or list an entity after general
onboarding, or asks to create a registry for holdings already listed in `businesses.md`. Do not
start it from a meeting mention, a source document, a candidate name in conversation, or the
mere presence of names in `businesses.md`.

A living trust is not an entity. If the user asked to onboard a living trust, load
`trust-onboarding.md` instead.

## Inputs

- `_config/profile/CONTEXT.md` — confirm the core profile is complete; if it is not, load
  `CONTEXT.md` in this directory for general onboarding instead of this route.
- `_config/profile/businesses.md` — known holdings map. Reuse it.
- `_config/profile/entities/index.md` — if it exists. Preserve every existing entity's status
  and files.
- `_config/profile/entities/<slug>/overview.md` — if it exists for an entity being discussed.
- `questionnaire.md` **Domain 3: Entities** — question bank for missing basics only.

## Process

1. Do not create a `meetings/` record, meeting artifact, or meeting-index entry.
2. Read `businesses.md` and `entities/index.md` when they exist. Do not re-ask facts already
   recorded. Ask only what those files and any existing overview still omit (legal name, short
   name, structure, formation, tax classification if known, ownership/control, relationships,
   purpose/stage, open questions).
3. If `entities/index.md` is absent, create it from `_config/profile/entities/CONTEXT.md`
   **Index**. Create `overview.md` only for entities being registered in this session.
4. For each entity being added: write `<entity-slug>/overview.md` from
   `_template/overview.md`, set Status `basic` and Freshness `current`, and add one index
   row. If the existing table has no Freshness column, add it for every row (existing rows
   → `current`) rather than mixing shapes. Copy field structure from the template; do not
   write real data into `_template/`. Do not change another row's depth or freshness.
5. If the user pointed at an entity that is already in the index but whose `overview.md` is
   missing, repair that overview from known facts. Do not rebuild unrelated entities.
6. Do not change an existing entity from `in-depth` (or in-progress deepen) back to `basic`.
   Do not create detailed domain files on this route.
7. Update `businesses.md` as the high-level map only. Details stay in the entity folder.
8. Stamp `Last Updated: YYYY-MM-DD` on each file written.

## Completion

- Each entity registered in this session has a stable slug, an index row, and an `overview.md`
  with a valid `Last Updated` line.
- Existing entities keep their prior depth, freshness, files, and resume or meeting router.
- Tell the user that in-depth onboarding for a registered entity is available on request. Do
  not start `entity-onboarding.md` unless they asked to deepen in the same request. If they
  did, load `entity-onboarding.md` for that entity next.
