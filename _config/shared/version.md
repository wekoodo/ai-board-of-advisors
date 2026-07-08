# Product Version

Product (system/factory) release stamp. Not personal data.

| Field | Value |
|-------|--------|
| **version** | `0.1.0` |
| **released** | `2026-07-08` |
| **product_repo** | `https://github.com/wekoodo/ai-board-of-advisors` |
| **upstream_remote_name** | `upstream` |
| **changelog** | `CHANGELOG.md` (repo root) |

Compare **version** as semver (`MAJOR.MINOR.PATCH`). Higher wins.

---

## Soft check (meeting start — this file only)

**When:** Once per session at meeting start (with the `_inbox/` check), or if the user asks
“any updates?”. **Do not** load `updates.md` for a routine check.

1. Skip if this workspace looks like the **product/contributor** repo (`origin` URL matches
   **product_repo**). Personal boards only.
2. If remote **upstream_remote_name** is missing: one quiet line that they can say
   “connect product updates” — then continue the meeting. (Connect steps: `updates.md`.)
3. Else: `git fetch upstream` (fail soft if offline/no git — skip silently).
4. Read upstream version (first success):  
   `git show upstream/main:_config/shared/version.md`  
   or raw  
   `https://raw.githubusercontent.com/wekoodo/ai-board-of-advisors/main/_config/shared/version.md`
5. If upstream **version** is newer, one short notice, then continue:

```markdown
**Product update available:** local `X.Y.Z` → upstream `A.B.C`.
Profile and meetings stay local. Say **update the board** for commands or for me to apply it.
```

If current or local is newer: stay silent (or “you’re current” only if they asked).

**Load `_config/shared/updates.md` only when:** connecting upstream, applying an update, or
resolving conflicts after a merge. Never auto-merge from a soft check.
