# Setup — Onboarding Interview

This directory contains the onboarding interview system. It is loaded only during the
first-launch interview or when the user wants to update their profile.

## Agent Instructions

You are running the Board of Advisors onboarding interview. Follow these rules:

1. **Check for existing profile files first.** Before beginning, check which files exist in
   `_config/profile/`. Skip domains whose profile file is already present unless the user
   explicitly wants to update them.

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
   - Business domain → `_config/profile/businesses.md` (skip if user owns no businesses)
   - Financial domain → `_config/profile/financial.md`
   - Investments domain → `_config/profile/investments.md`
   - Goals domain → `_config/profile/goals.md`
   - Concerns domain → "Current Concerns" section appended to `_config/profile/goals.md`

6. **When complete:** Tell the user their profile is saved and they can return to the root
   `CONTEXT.md` to begin using the advisors.

## Files in This Directory

- `questionnaire.md` — the full interview question bank
- `onboarding.md` — human-readable installation and usage guide
