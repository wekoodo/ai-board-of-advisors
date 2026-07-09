# Product Version

Product (system/factory) release stamp. Not personal data.

| Field | Value |
|-------|--------|
| **version** | `0.1.0` |
| **released** | `TBD` (set at first tag) |
| **product_repo** | `https://github.com/wekoodo/ai-board-of-advisors` |
| **upstream_remote_name** | `upstream` |
| **changelog** | `CHANGELOG.md` (repo root) |

Compare **version** as semver (`MAJOR.MINOR.PATCH`); higher wins. `released` is cosmetic — the
check never uses it.

---

## Soft check (single source of truth)

This file holds the whole procedure. `CONTEXT.md` and `meeting-process.md` only *point* here and
pre-gate the throttle so this file isn't even loaded on repeat same-day sessions. Keep the steps in
this one place.

### When to run

- **On demand** — the user asks (“any updates?”, “am I current?”, “update the board”). Always runs;
  ignores the throttle.
- **Opportunistically** — at meeting start, **at most once per calendar day** (throttle in step 1).
  Most sessions therefore do no network and don't load this file at all.

### Steps

1. **Throttle & stamp** (skip this step only when the user explicitly asked). Read
   `_config/profile/.update-check`. If it already holds today's date, **stop** — no fetch, no
   notice. Otherwise write today's date (`YYYY-MM-DD`) to it *now*, before fetching: that bounds the
   check to one attempt per day even when offline. This file is local-only bookkeeping — gitignored,
   not profile data.
2. **Product-repo skip.** If this workspace *is* the product/contributor repo, stop (it ships via
   releases/PRs, not `upstream` merges). Compare **normalized** remotes, not raw URLs: take `origin`
   and **product_repo**, strip the scheme (`https://`, `git@`), any `user@`, the `:` a host may use
   before the path, and a trailing `.git`; lowercase; compare the remaining `host/owner/repo`.
   Example — these are the **same** repo: `git@github.com:wekoodo/ai-board-of-advisors.git` and
   `https://github.com/wekoodo/ai-board-of-advisors`.
3. **No `upstream` yet?** If the remote named by **upstream_remote_name** is missing, emit one quiet
   line that they can say “connect product updates,” then continue the meeting. (Connect steps live
   in `updates.md` — do not load it for a check.)
4. **Fetch, fail soft.** `git fetch upstream`. If it fails (offline / no git), skip silently.
5. **Read upstream version** (first that works): `git show upstream/main:_config/shared/version.md`,
   or the raw form of **product_repo**:
   `https://raw.githubusercontent.com/wekoodo/ai-board-of-advisors/main/_config/shared/version.md`.
6. **Compare and notify.** If upstream **version** is newer (semver), print the notice once, then
   continue — never block:

   ```markdown
   **Product update available:** local `X.Y.Z` → upstream `A.B.C`.
   Profile and meetings stay local. Say **update the board** for commands or for me to apply it.
   ```

   If current or local is ahead, stay silent (say “you’re current” only if they asked).

**Never** auto-merge from a check. Load `_config/shared/updates.md` only to **connect** `upstream`,
**apply** an update, or resolve merge conflicts.

> **Throttle interval is a knob.** Daily is the default; for weekly, compare the stored date against
> a 7-day window in step 1 instead of an exact match.
