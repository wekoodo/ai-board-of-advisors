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

Use `upstream` to fetch system changes. Personal boards can opt in to sync records to their own
private `origin` using the root `README.md` **Sync context to a private repository** procedure.

**Identity fields** (do not hardcode a second source): `_config/shared/version.md`
(`product_repo`, `upstream_remote_name`, `version`).

**Workspace kind:** Profile data is the durable signal; follow `version.md` step 1. A workspace with
at least one defined profile file is a personal board, whether it came from a template or direct
clone. A clean canonical clone or contributor fork has no profile data and skips this flow.

---

## Connect `upstream` (onboarding or on request)

After the profile interview, or when the user asks to connect updates:

1. Explain that `upstream` fetches system updates and that private sync uses the board's own `origin`.
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
git merge --no-overwrite-ignore upstream/main
```

If Git reports unrelated histories, follow **First update from a template**. With shared history,
`git rebase upstream/main` after the fetch is also an option. Resolve conflicts before reopening
the board. The upstream changes should contain only product files.

### Option B — Agent applies

1. Confirm: “I’ll fetch `upstream` and merge into your current branch. Continue?”
2. On yes: `git fetch upstream`, then `git merge --no-overwrite-ignore upstream/main`.
   If Git reports unrelated histories, explain the one-time merge below and confirm before running it.
3. Report: clean merge → new version from `version.md`, optional CHANGELOG highlights; or list conflicts and help resolve (usually edited **system** files — prefer new advisors over editing core).
4. **Never** force-push, `reset --hard`, or discard work without explicit consent.
5. Keep the board's current sync choice when resolving `.gitignore` conflicts. Enabling sync and
   committing board records are separate from applying an update.

After success: local `version.md` should match upstream (via the merge). Custom extended advisors in new folders are usually untouched.

---

## First update from a template

GitHub's **Use this template** starts with independent history. After fetching and verifying
`upstream` points to the public product repository, run `git merge-base HEAD upstream/main`.
If it finds no common ancestor, start on a branch with a clean tracked worktree.

### Join at a matching template snapshot

Find the root commit of your board and compare its tree ID to the upstream tree IDs. Both
commands print the tree ID followed by the commit ID.

```bash
git log --first-parent --max-parents=0 --format="%T %H" HEAD
git log --format="%T %H" upstream/main
```

If the tree IDs match, use the **matching upstream commit ID** for `UPSTREAM_SNAPSHOT` in the
first command. This records the known template snapshot as an ancestor while preserving your
board's files and customizations. The second command applies the product changes since that snapshot.

```bash
git merge --allow-unrelated-histories --strategy=ours UPSTREAM_SNAPSHOT
git merge --no-overwrite-ignore upstream/main
```

### Join without a matching snapshot

If you cannot establish a matching tree, review the full merge once:

```bash
git merge --allow-unrelated-histories --no-overwrite-ignore upstream/main
```

The first merge can report add/add conflicts in system files. Review upstream changes against
your customizations and stage only the resolved system files by path. Use `git merge --abort`
if you need to stop before finishing a conflicted merge. After a successful merge, use the
normal update command for later releases. [Git merge options](https://git-scm.com/docs/git-merge)

**Contribute to the product:** fork/clean clone → PR. Do not PR from a personal board with real life data.
