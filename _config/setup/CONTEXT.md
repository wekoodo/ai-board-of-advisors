# Setup — Onboarding Interview

This directory contains the onboarding interview system. It is loaded only during the
first-launch interview or when the user wants to update their profile.

## Agent Instructions

You are running the Board of Advisors onboarding interview. Follow these rules:

**Output boundary:** Onboarding is profile maintenance, not a board meeting. Write onboarding facts,
decisions, open questions, action registers, and source inventories under `_config/profile/`. Do not
create a `meetings/` folder, meeting artifact, or meeting-index entry for onboarding.

**Focused trust route:** If the user explicitly asks to onboard or resume onboarding a living trust
or similar estate vehicle, load `trust-onboarding.md` and follow its scoped inputs, outputs, and
completion check. Do not restart the general questionnaire. Do not start this route unless they
asked.

**Focused entity route:** If the user asks to begin or resume in-depth onboarding for a registered
entity that already has an `entities/index.md` entry and `overview.md`, load `entity-onboarding.md`
and that entity's `CONTEXT.md`. Follow **Current state**, **Resume inputs**, and **Next work** only
when those resume sections exist. If the entity `CONTEXT.md` is already a completed meeting router,
do not start an interview unless the user explicitly asks to refresh. Do not recap or restart
completed domains. Do not create a meeting. Do not start this route because general onboarding
finished.

1. **Check existing profile content first.** Before beginning or resuming, inspect the relevant
   profile file and section for each domain. Skip a domain only when its required content is
   complete, unless the user explicitly wants to update it. File presence alone is not completion:
   Employment and Financial share `financial.md`, and Goals and Concerns share `goals.md`.

2. **Proceed domain by domain.** Load `questionnaire.md` and work through each domain in order:
   Personal → Employment → Business → Financial → Investments → Goals → Concerns.

3. **Ask conversationally.** Do not display all questions at once. Ask naturally, follow up,
   and let the conversation flow. The questionnaire is a guide, not a script to read verbatim.

4. **Write profile files as you go.** After completing each domain, write the corresponding file
   to `_config/profile/` before proceeding. If the session is interrupted, completed domains are
   already saved. Stamp each file with a "Last Updated: YYYY-MM-DD" line at the top.

5. **Profile files to write:**
   - Personal domain → `_config/profile/personal.md`
   - Employment domain → "Income & Employment" section within `_config/profile/financial.md`
   - Business domain → `_config/profile/businesses.md` (record that none are owned when applicable).
     If the user names any businesses, LLCs, land trusts, or similar: also write
     `_config/profile/entities/index.md` and one basic `<entity-slug>/overview.md` per known entity.
     If the user has a living trust or similar estate vehicle: also write
     `_config/profile/trust.md`. Neither extra file is required to complete general onboarding
     when the answer is no.
   - Financial domain → `_config/profile/financial.md`
   - Investments domain → `_config/profile/investments.md`
   - Goals domain → `_config/profile/goals.md`
   - Concerns domain → "Current Concerns" section appended to `_config/profile/goals.md`

6. **Keep entity and trust onboarding bounded.** General onboarding records identity, relationships,
   purpose, classification, available documents, and open questions. It does not collect full
   financial, tax, governance, operations, or risk detail for each entity. It does not run focused
   trust intake. Use `entity-onboarding.md` or `trust-onboarding.md` only when the user asks.

7. **Verify onboarding completion before declaring it complete:**
   - Confirm all five required files exist: `personal.md`, `financial.md`, `businesses.md`,
     `investments.md`, and `goals.md`.
   - Confirm each of those files contains a valid `Last Updated: YYYY-MM-DD` line reflecting the
     current onboarding write.
   - Confirm `financial.md` contains an "Income & Employment" section.
   - Confirm `goals.md` contains a "Current Concerns" section.
   - If `entities/index.md` exists, confirm every listed entity has a stable slug, an onboarding
     status, and a matching `overview.md` with a valid `Last Updated` line. Do not require
     detailed entity files for a `basic` entity. Do not require `entities/index.md` when the user
     owns no entities.
   - If `trust.md` was written, confirm it has a valid `Last Updated` line. Do not require
     `trust.md` when the user has no living trust.
   - If any required check fails, repair the missing or incomplete profile file and repeat this
     verification.

8. **Connect product updates (after the verified profile interview).** For a personal board only: load
   `../shared/updates.md` and follow **Connect `upstream`**. (Skip on the product/contributor
   repo.) Read `product_repo` from `../shared/version.md` if needed. Decline is fine; no nagging.

9. **When complete:** Profile verified and saved; note whether upstream was connected. If entities
   were registered, mention that in-depth entity onboarding is available later on request — do not
   start it. Return to root `CONTEXT.md` to use the board.

## Files in This Directory

- `questionnaire.md` — the full interview question bank
- `entity-onboarding.md` — the optional in-depth interview for one selected entity
- `trust-onboarding.md` — the optional focused living-trust interview
- `onboarding.md` — human-readable installation and usage guide
