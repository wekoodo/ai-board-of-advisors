# Getting Started with Board of Advisors

Welcome. This guide explains how to install and begin using the Board of Advisors.

## Installation

**Option A — GitHub Template (recommended)**
1. Click "Use this template" on the GitHub repository page
2. Name your repository and choose visibility (private recommended for your profile data)
3. Clone your new repository to your local machine

**Option B — Direct clone**
```bash
git clone https://github.com/[owner]/board-of-advisors.git my-advisors
cd my-advisors
```

## First Launch

Open the repository in your AI agent harness. The agent reads `AGENTS.md` (or `CLAUDE.md`/`GEMINI.md`)
then `CONTEXT.md`. If no profile exists, it detects this and begins the **onboarding interview**.

The interview:
- Takes ~10–20 minutes
- Covers 7 domains: Personal, Employment, Business, Financial, Investments, Goals, Concerns
- Is conversational and can be paused/resumed — each completed domain is written immediately

Your profile is stored in `_config/profile/`. All profile data files are gitignored and never
committed. Your data stays on your machine.

## Single-Advisor Consultation
1. Navigate to `advisors/NN-name/` (e.g., `advisors/02-tax-strategist/`) — or an extended advisor in `advisors-extended/NN-name/`
2. Tell your agent to load `CONTEXT.md` from that folder
3. Ask your question — the advisor loads your profile automatically

## Full Board Session
1. Copy `meetings/_template/` to `meetings/YYYY-MM-DD-topic/`
2. Fill in `00-brief.md`
3. Load the session `CONTEXT.md` and follow the stage instructions (Round 1 → Artifacts → Reconvene)

See `_config/shared/meeting-process.md` for manual vs. delegated execution.

## Updating Your Profile
- Edit any file in `_config/profile/` directly, or ask an advisor to update a section.
- `_config/profile/CONTEXT.md` tracks when each section was last updated; advisors flag data older than 12 months.

## Adding Custom Advisors
1. Copy `advisors/_template/` to `advisors/NN-my-advisor/` — or study the built `advisors-extended/`
   examples (oil & gas, storage), which are fully working advisors and reference implementations of the template
2. Fill in `CONTEXT.md` (identity, inputs, process, outputs)
3. Add the advisor to the routing map in the root `CONTEXT.md`
4. Optionally seed `references/frameworks.md` with domain knowledge

The numbered prefix controls sequence in full board sessions.

## Privacy Note
Your profile data (`_config/profile/*.md`) and user-created sessions (`meetings/YYYY-MM-DD-*/`)
are gitignored and stay local. The `meetings/_template/` folder and the shipped example session
are included in the repo.
