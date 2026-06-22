# Profile

Your persistent profile is stored in this directory. It is loaded by all advisors at the start
of every session to personalize their guidance. All files here are gitignored and stay on your machine.

## Profile Files

| File | Contains | Last Updated |
|------|----------|--------------|
| `personal.md` | Name, location, family structure, health | [not yet created] |
| `financial.md` | Income, assets, liabilities, cash flow, insurance coverage | [not yet created] |
| `businesses.md` | Business holdings, entity types, revenue, stage | [not yet created — optional] |
| `investments.md` | Portfolio allocation, accounts, risk tolerance, time horizon | [not yet created] |
| `goals.md` | Short, medium, and long-term goals; current concerns | [not yet created] |

## Agent Instructions

1. Load all files present in this directory.
2. If a file's "Last Updated" date is more than 12 months ago, note it at the start of the
   session and offer to update.
3. `businesses.md` is optional — if it says "no businesses owned," no further action needed.
4. If no profile files exist yet, stop and direct the user to run onboarding: load
   `_config/setup/CONTEXT.md` to begin.

## Updating Profile Files

Edit any file directly, or ask an advisor to update a section. When writing or updating a profile
file, include a "Last Updated: YYYY-MM-DD" line at the top so the staleness check works.
