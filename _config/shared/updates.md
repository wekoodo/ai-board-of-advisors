# Product Updates Protocol

**Load this file only when needed** — not on every meeting start.

| Load when… | Skip when… |
|------------|------------|
| Connecting `upstream` (onboarding or “connect product updates”) | Routine advisory work |
| User wants to **apply** an update (“update the board”) | Soft version check only → use `version.md` |
| Merge conflicts or post-update recovery | Product/contributor clone (use PRs/releases) |

Routine soft checks: **`version.md` only**. Humans: root `README.md` (Use vs contribute; Keeping your board up to date).

---

## Roles

| Role | How | Purpose |
|------|-----|---------|
| **Personal board** | GitHub **template** | Daily use; pull system updates via `upstream` |
| **Product repo** | Canonical clone | Releases / this system |
| **Contributor** | **Fork** (+ clean tree) | PRs — no real profile/meetings |

`upstream` on a personal board is not a fork. Profile, meetings, and `_inbox/` are gitignored and are not pushed to the product.

**Identity fields** (do not hardcode a second source): `_config/shared/version.md`
(`product_repo`, `upstream_remote_name`, `version`).

**Workspace kind:** If `origin` matches **product_repo**, skip personal-board update/apply flows
(or say to use releases/PRs). Otherwise treat as a personal board.

---

## Connect `upstream` (onboarding or on request)

After the profile interview, or when the user asks to connect updates:

1. Briefly: `upstream` only enables **system** updates; profile/meetings/inbox stay local.
2. If remote `upstream` is missing, offer to add it (recommend **yes**). On consent:

```bash
git remote add upstream https://github.com/wekoodo/ai-board-of-advisors.git
```

   Use **product_repo** from `version.md` if it differs. If `upstream` exists but points elsewhere,
   show the URL and ask before `git remote set-url`.
3. Optional: `git fetch upstream` once to verify; on failure, leave the remote and say so.
4. If they decline: do not nag every session; they can ask later.

---

## Apply an update (user asked)

Present **both** options. Merge only after clear consent for agent-apply.

### Option A — DIY

```bash
git fetch upstream
git merge upstream/main
```

Rebase alternative: `git fetch upstream` then `git rebase upstream/main`.  
Then fix conflicts if any; reopen the board. Profile/meetings should not appear in the merge.

### Option B — Agent applies

1. Confirm: “I’ll fetch `upstream` and merge into your current branch. Continue?”
2. On yes: `git fetch upstream` then `git merge upstream/main`.
3. Report: clean merge → new version from `version.md`, optional CHANGELOG highlights; or list conflicts and help resolve (usually edited **system** files — prefer new advisors over editing core).
4. **Never** force-push, `reset --hard`, or discard work without explicit consent.
5. **Never** commit private profile/meeting files or weaken `.gitignore` as part of an update.

After success: local `version.md` should match upstream (via the merge). Custom extended advisors in new folders are usually untouched.

---

## What merges vs stays local

| From upstream (system) | Stays local |
|------------------------|-------------|
| Advisors, `_config/shared/`, setup, root chair/docs, examples | Profile, your meetings, `_inbox/*` (except tracked README) |

**Contribute to the product:** fork/clean clone → PR. Do not PR from a personal board with real life data.
