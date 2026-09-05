# Config Directory

This directory contains shared infrastructure loaded by all advisors and the onboarding system.

## Contents

| Directory / File | Purpose |
|------------------|---------|
| `shared/disclaimer.md` | Legal/educational disclaimer loaded by every advisor |
| `shared/collaboration.md` | Cross-advisor referral map loaded by every advisor |
| `shared/ethics.md` | Shared ethical guidelines loaded by every advisor |
| `shared/conventions.md` | Durable-figures rule, the `## Handoff` block format, and response style |
| `shared/google-doc-style-overlay.md` | Overlay on the locked `google-doc-style` skill (real data, voice, no restyle of contracts) — not Always-load protocol |
| `shared/meeting-process.md` | The live-meeting protocol and convening modes (sub-agent / inline) |
| `shared/convening.md` | Chair seat-selection map (fewest owners; 01 vs 05 vs 09/10 disambiguation) |
| `shared/icm-conventions.md` | How this project applies ICM (layer map, numbers-as-IDs, in-workspace memory, tooling vs. content, skills management) |
| `shared/version.md` | Product semver stamp + soft-check recipe (on demand, else once a day) |
| `shared/updates.md` | Connect upstream / apply merge — load only when needed |
| `setup/` | Onboarding interview and installation guide (loaded only during first-launch onboarding) |
| `profile/` | Your persistent profile — written during onboarding, gitignored, local-only. Tracked: `CONTEXT.md` and `entities/_template/` |

> **Related — repo root:** `_inbox/` is the intake point for pre-meeting documents. The chair checks
> it at meeting start and moves relevant files into `meetings/<meeting>/inputs/`; full detail is in
> `shared/meeting-process.md`.

## When to Load

Load classes follow `shared/icm-conventions.md` **Skills management**. Shared protocol is not
the same class as a skill overlay.

- **Always load** (shared protocol): `shared/disclaimer.md`, `shared/collaboration.md`,
  `shared/ethics.md`, and `shared/conventions.md` — every advisor `CONTEXT.md`
- **Load when writing to the user** (skill overlay): `shared/google-doc-style-overlay.md` —
  chair (root `CONTEXT.md`) and advisors. Not Always-load protocol.
- `shared/meeting-process.md` and `shared/convening.md` — board chair when hosting a meeting
  (process first, then the convening map before picking seats)
- `shared/icm-conventions.md` — structure, audit, or ICM maintenance; not a meeting Always load
- `shared/version.md` — the complete update soft-check (on demand, otherwise at most once daily)
- `shared/updates.md` — load **only** when connecting `upstream` or applying an update (setup
  post-profile step, or user asks to update the board)
- `profile/CONTEXT.md` is referenced in each advisor's `CONTEXT.md` under "Always load"; follow
  its scoped load and do not bulk-load `entities/`
- `setup/` is loaded only when the onboarding interview is running (first launch or profile update)
- Root `tmp/CONTEXT.md` (gitignored, only if it exists) — product-authoring work in this clone;
  not a meeting load and not onboarding
