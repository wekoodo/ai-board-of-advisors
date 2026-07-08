# Getting Started with Board of Advisors

Welcome. This guide explains how to install and begin using the Board of Advisors — and how that
differs from contributing to the product.

## Two doors: use vs contribute

| Goal | Path |
|------|------|
| **Your personal board** (daily use, profile, meetings) | GitHub **Use this template** → your own repo |
| **Improve the product** (PRs, fixes, new system content) | **Fork** the canonical product repo → clean workspace → PR |

Do **not** open product PRs from a personal board that holds real profile or meeting data.
Details: root `README.md` (*Use vs contribute*).

---

## Installation (personal board)

**Option A — GitHub Template (recommended)**

1. Click **Use this template** on the [product repository](https://github.com/wekoodo/ai-board-of-advisors)
2. Name your repository and choose visibility (**private** recommended)
3. Clone *your* new repository to your local machine

**Option B — Direct clone of the product** (fine for browsing; for a life board, prefer the template so your repo is clearly *yours*)

```bash
git clone https://github.com/wekoodo/ai-board-of-advisors.git my-advisors
cd my-advisors
```

## First launch

Open the repository in your AI agent harness. The agent reads `AGENTS.md` (or `CLAUDE.md`/`GEMINI.md`)
then `CONTEXT.md`. If no profile exists, it detects this and begins the **onboarding interview**.

The interview:

- Takes ~10–20 minutes
- Covers 7 domains: Personal, Employment, Business, Financial, Investments, Goals, Concerns
- Is conversational and can be paused/resumed — each completed domain is written immediately

Your profile is stored in `_config/profile/`. All profile data files are gitignored and never
committed. Your data stays on your machine.

### Connect product updates (end of onboarding)

After the profile domains are done, the agent offers to connect **product updates**:

- Adds a git remote named `upstream` pointing at the canonical product repo
- That remote is **only** for checking and merging **system** changes (advisors, shared rules, docs)
- It does **not** upload your profile, meetings, or inbox files

Recommended: accept. You can also say later: “connect product updates.”

Agents: connect steps in `_config/shared/updates.md`; routine version checks use
`_config/shared/version.md` only.

## Talk to your board

1. Load the root `CONTEXT.md`. That convenes the board chair, who hosts the meeting and routes each
   question to the relevant advisor(s).
2. Ask your question. The chair convenes one advisor, several, or the whole board — whichever the
   topic actually touches — and they respond in character.
3. The chair produces artifacts (worksheets, plans, checklists) as real files under
   `meetings/<meeting>/artifacts/` whenever a document would help. You can read and edit them while
   the meeting is still running.
4. The chair keeps a small, routed record of each meeting — a `brief.md` (what you asked), a
   `minutes.md` (the decisions and how to use each artifact), and the `artifacts/` themselves. Ask to
   keep the full `transcript.md` only when you want the complete back-and-forth.
5. At **meeting start**, the chair soft-checks versions via `version.md` (not the full update
   protocol). If an update exists, you get a short notice. Say you want to update for DIY commands
   or agent-apply (with consent).

A single-advisor consult is just a meeting with one voice convened — there is no separate mode.

See `_config/shared/meeting-process.md` for the full protocol and the sub-agent vs. inline
convening modes.

## Updating your profile

- Edit any file in `_config/profile/` directly, or ask an advisor to update a section.
- `_config/profile/CONTEXT.md` tracks when each section was last updated; advisors flag data older than 12 months.

## Keeping the product system up to date

GitHub does not auto-notify template children. With `upstream` set:

```bash
git fetch upstream
git merge upstream/main
```

Or ask the board: “update the board” — the agent will show these commands and offer to run the
merge after you confirm. See `_config/shared/updates.md` and root `CHANGELOG.md`.

## Adding custom advisors

1. Copy `advisors/_template/` to `advisors/NN-my-advisor/` — or study the built `advisors-extended/`
   examples (oil & gas, storage), which are fully working advisors and reference implementations of the template
2. Fill in `CONTEXT.md` (identity, inputs, process, outputs)
3. Add the advisor to the routing map in the root `CONTEXT.md`
4. Optionally seed `references/frameworks.md` with domain knowledge

Prefer **new** advisor folders over editing core system files — future product merges stay easier.
See `advisors-extended/README.md`.

## Contributing to the product

1. Fork [wekoodo/ai-board-of-advisors](https://github.com/wekoodo/ai-board-of-advisors)
2. Work in a clean tree (no real personal profile/meetings)
3. Open a PR against the product `main` branch

## Privacy note

Your profile data (`_config/profile/*.md`) and user-created meetings (`meetings/<topic>/`)
are gitignored and stay local. The shipped example meetings under `meetings/example-*/` are
included in the repo as worked references.
