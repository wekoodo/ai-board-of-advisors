# Config Directory

This directory contains shared infrastructure loaded by all advisors and the onboarding system.

## Contents

| Directory / File | Purpose |
|------------------|---------|
| `shared/disclaimer.md` | Legal/educational disclaimer loaded by every advisor |
| `shared/collaboration.md` | Cross-advisor referral map loaded by every advisor |
| `shared/ethics.md` | Shared ethical guidelines loaded by every advisor |
| `shared/conventions.md` | Durable-figures rule, the `## Handoff` block format, and response style |
| `shared/meeting-process.md` | Board session flow and execution modes (manual / delegated) |
| `setup/` | Onboarding interview and installation guide (loaded only during first-launch onboarding) |
| `profile/` | Your persistent profile — written during onboarding, gitignored, local-only |

## When to Load

- `shared/disclaimer.md`, `shared/collaboration.md`, and `shared/conventions.md` are referenced automatically in each advisor's `CONTEXT.md` under "Always load"
- `shared/meeting-process.md` is loaded by the board chair and session router when running a board session
- `profile/` files are referenced automatically in each advisor's `CONTEXT.md` under "Always load"
- `setup/` is loaded only when the onboarding interview is running (first launch or profile update)
