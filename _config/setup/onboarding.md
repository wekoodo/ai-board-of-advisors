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

## Talk to Your Board

1. Load the root `CONTEXT.md`. That convenes the board chair, who hosts the meeting and routes each
   question to the relevant advisor(s).
2. Ask your question. The chair convenes one advisor, several, or the whole board — whichever the
   topic actually touches — and they respond in character.
3. The chair produces artifacts (worksheets, plans, checklists) as real files under
   `meetings/<meeting>/artifacts/` whenever a document would help. You can read and edit them while
   the meeting is still running.
4. When you're done, say **"save this meeting"** and the chair writes a `transcript.md` next to the
   artifacts.

A single-advisor consult is just a meeting with one voice convened — there is no separate mode.

See `_config/shared/meeting-process.md` for the full protocol and the sub-agent vs. inline
convening modes.

## Updating Your Profile
- Edit any file in `_config/profile/` directly, or ask an advisor to update a section.
- `_config/profile/CONTEXT.md` tracks when each section was last updated; advisors flag data older than 12 months.

## Adding Custom Advisors
1. Copy `advisors/_template/` to `advisors/NN-my-advisor/` — or study the built `advisors-extended/`
   examples (oil & gas, storage), which are fully working advisors and reference implementations of the template
2. Fill in `CONTEXT.md` (identity, inputs, process, outputs)
3. Add the advisor to the routing map in the root `CONTEXT.md`
4. Optionally seed `references/frameworks.md` with domain knowledge

The numbered prefix controls the advisor's slot in the roster and the default ordering when the
chair convenes several advisors in one turn.

## Privacy Note
Your profile data (`_config/profile/*.md`) and user-created meetings (`meetings/YYYY-MM-DD-*/`)
are gitignored and stay local. The shipped example meetings under `meetings/example-*/` are
included in the repo as worked references.
