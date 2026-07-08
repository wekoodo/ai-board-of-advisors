# Config Directory

This directory contains shared infrastructure loaded by all advisors and the onboarding system.

## Contents

| Directory / File | Purpose |
|------------------|---------|
| `shared/disclaimer.md` | Legal/educational disclaimer loaded by every advisor |
| `shared/collaboration.md` | Cross-advisor referral map loaded by every advisor |
| `shared/ethics.md` | Shared ethical guidelines loaded by every advisor |
| `shared/conventions.md` | Durable-figures rule, the `## Handoff` block format, and response style |
| `shared/meeting-process.md` | The live-meeting protocol and convening modes (sub-agent / inline) |
| `shared/icm-conventions.md` | How this project applies ICM (layer map, numbers-as-IDs, in-workspace memory, tooling vs. content) |
| `shared/version.md` | Product semver stamp + soft-check recipe (default update path) |
| `shared/updates.md` | Connect upstream / apply merge — load only when needed |
| `setup/` | Onboarding interview and installation guide (loaded only during first-launch onboarding) |
| `profile/` | Your persistent profile — written during onboarding, gitignored, local-only |

> **Related — repo root:** `_inbox/` is the intake point for pre-meeting documents. The chair checks
> it at meeting start and moves relevant files into `meetings/<meeting>/inputs/`; full detail is in
> `shared/meeting-process.md`.

## When to Load

- `shared/disclaimer.md`, `shared/collaboration.md`, and `shared/conventions.md` are referenced automatically in each advisor's `CONTEXT.md` under "Always load"
- `shared/meeting-process.md` is loaded by the board chair when hosting a meeting
- `shared/version.md` — chair loads **only this** for the start-of-meeting soft update check
- `shared/updates.md` — load **only** when connecting `upstream` or applying an update (setup
  post-profile step, or user asks to update the board)
- `profile/` files are referenced automatically in each advisor's `CONTEXT.md` under "Always load"
- `setup/` is loaded only when the onboarding interview is running (first launch or profile update)
