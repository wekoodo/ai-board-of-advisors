# Google-doc-style overlay (this board)

The locked `google-doc-style` skill (from `wekoodo/skills`, pinned in `skills-lock.json`)
governs **reader-facing prose**. This file is the project overlay: when that skill conflicts with
this board, **this file wins**. It is not shared protocol (not Always load next to ethics). Who
loads it is in `icm-conventions.md` **Skills management**. Do not edit the installed skill under
`.agents/skills/`; a lockfile reinstall overwrites it.

The skill's own precedence already defers to environment constraints. This overlay *is* that
environment for the Board of Advisors.

## What the skill may shape

Chat answers, synthesis, `brief.md`, `minutes.md`, and meeting artifacts written for the user to
read. Clarity, sentence case, active voice, serial commas, and code font in running text still
apply.

## What the skill must not change

- **Code, identifiers, string literals, comments, commit messages, configuration, and machine-read
  output** — including the `## Handoff` block *shape* in `conventions.md` (heading and field names
  stay exact).
- **Agent contracts:** `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, any `CONTEXT.md`, `_config/shared/`
  protocol files, advisor `references/`, and `skills-lock.json`. Match surrounding voice and
  structure; do not restyle them as public docs.
- **Word-list substitutions inside those files or in code** (`execute` → `run`, `terminate` →
  `stop`, `config` → `configuration`, `repo` → `repository`, `master` → `main`). Keep the project's
  actual terms.
- **Hidden reasoning and tool arguments.** Style rules apply to text the user reads, not to
  planning, tool-call payloads, or file contents that are not prose for the user.

## Real data vs illustrative samples

This board writes about **this user's actual situation**.

- Use real names, entities, amounts, addresses, and facts from `_config/profile/` and the meeting
  in chat answers and artifacts.
- Do **not** replace them with example.com, `dana@example.com`, or fictional sample people.
- Year-specific tax and limit figures still follow the durable-figures rule in `conventions.md`
  (`illustrative — verify current-year value`). That rule is about stale statutory numbers, not
  about anonymizing the user.

## Voice on this board

- Advisors and the chair may use **first-person plural ("we")** as the board. Do not rewrite that
  to second-person "you."
- Address the user as **you**. "The user" / "the client" in advisor text means this person, not
  a third-party audience.
- Keep advisor character (credentials, domain voice). Do not flatten it into generic developer-doc
  tone.
- Response shape in `conventions.md` still applies: lead with the answer, numbered lists for
  steps, tables for comparisons.

## Self-check (before finishing)

1. Did I change code, identifiers, comments, commits, config, or a `CONTEXT.md` / Handoff contract
   to satisfy google-doc-style? If yes, revert that.
2. Did I replace the user's real facts with sample/example data? If yes, put the real facts back.
3. Did I strip "we" from board or advisor voice? If yes, restore it.
