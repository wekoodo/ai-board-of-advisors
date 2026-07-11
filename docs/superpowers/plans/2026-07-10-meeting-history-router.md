# Meeting History Router Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a tracked meeting-history router and a private compact index contract that lets agents locate and selectively load one prior meeting.

**Architecture:** `meetings/CONTEXT.md` is the tracked recursive router for the Layer-4 meeting area, while `meetings/index.md` is ignored, local-only routing metadata. Root and shared meeting contracts invoke this flow and maintain one index entry per meeting folder; meeting records remain authoritative and scoped search repairs missing or stale metadata.

**Tech Stack:** Pure Markdown, Git ignore rules, PowerShell, repository ICM audit script

## Global Constraints

- Keep the implementation pure Markdown and harness-agnostic.
- Preserve topic-only meeting folder names.
- Do not commit a sample `meetings/index.md` or migrate existing meeting records.
- Keep `meetings/agenda.md`, private meeting history, and shipped fictional examples distinct.
- Treat each meeting's `brief.md`, `minutes.md`, and artifacts as authoritative; the index is repairable routing metadata.
- Load no transcript, complete artifact directory, or complete meeting history by default.

---

### Task 1: Add the private-index boundary and recursive meeting router

**Files:**
- Create: `meetings/CONTEXT.md`
- Modify: `.gitignore`
- Test: repository shell assertions and Git ignore checks

**Interfaces:**
- Consumes: existing `meetings/<topic>/brief.md`, `minutes.md`, optional `artifacts/`, and optional `agenda.md`
- Produces: a tracked router contract for reading and maintaining local `meetings/index.md`

- [ ] **Step 1: Run pre-change assertions and verify the feature is absent**

Run:

```powershell
$failures = @()
if (Test-Path 'meetings/CONTEXT.md') { $failures += 'meetings/CONTEXT.md already exists' }
git check-ignore -q meetings/index.md
if ($LASTEXITCODE -eq 0) { $failures += 'meetings/index.md is already ignored' }
if ($failures.Count -eq 0) { Write-Output 'EXPECTED FAIL: meeting router and index ignore rule are absent'; exit 1 }
$failures
exit 1
```

Expected: exit 1 with `EXPECTED FAIL: meeting router and index ignore rule are absent` (or a precise message identifying unexpected pre-existing state).

- [ ] **Step 2: Add the explicit private-index ignore rule**

Under the `# User meetings` section of `.gitignore`, add:

```gitignore
# Compact private meeting-history routing metadata
/meetings/index.md
```

Keep the existing `meetings/*/` rule and example-directory exceptions unchanged.

- [ ] **Step 3: Create the recursive router contract**

Create `meetings/CONTEXT.md` with these sections and requirements:

```markdown
# Meeting History Router

## Purpose

Use this router when prior meeting context may matter. Locate one relevant meeting first, then load
only the record files needed for the current question.

## Private Index

`index.md` is local-only routing metadata, not authoritative meeting history. If it does not exist,
continue with the scoped fallback below. Never add shipped `example-*` meetings to this private index.

Each substantive user meeting has exactly one entry, keyed by its folder path:

### <Meeting title>
- Folder: `<topic-slug>/`
- Date: `YYYY-MM-DD`
- Status: `active` | `completed` | `paused`
- Purpose: <one sentence>
- Advisors: <advisor names or numbers>
- Tags: <search tags and any related agenda IDs, or `none`>
- Brief: [`brief.md`](<topic-slug>/brief.md)
- Minutes: [`minutes.md`](<topic-slug>/minutes.md) | `pending`

## Find a Prior Meeting

1. Read `index.md` if it exists.
2. Select one relevant entry by title, purpose, advisors, tags, agenda ID, date, or status.
3. Load that meeting's `brief.md` first.
4. Load `minutes.md` only for decisions, recommendations, status, or next steps.
5. Load individual artifacts only when the current question requires them.
6. Do not preload transcripts, complete artifact directories, or all meeting records.

## Scoped Fallback and Repair

When the index is missing, has no useful match, or points to a missing file:

1. Search topic folder names.
2. If needed, search only `brief.md` and `minutes.md` files for relevant terms.
3. Do not search transcripts or bulk-load artifacts by default.
4. Trust meeting record files over conflicting index metadata.
5. Create or repair the single entry keyed by folder path after locating a substantive user meeting.
6. Consolidate duplicate entries for the same folder path.

## Maintain the Index

Create or update the entry when the meeting folder is created under the existing lazy-creation rule:
when the question is clear enough for `brief.md`, the first artifact is produced, or the user asks to
save, whichever comes first. Use `pending` for minutes until `minutes.md` exists. Update the same
entry when minutes are created, material routing metadata changes, or status changes. Do not create
empty minutes solely for the index.

`agenda.md`, if present, tracks deferred questions and possible future work. `index.md` catalogs
meetings with actual records.

## Shipped Fictional Examples

- `example-emergency-fund/` — simple single-advisor meeting; start with its `brief.md`.
- `example-rental-property/` — multi-advisor meeting with artifacts; start with its `brief.md`, then
  use `minutes.md` to select an artifact.
```

- [ ] **Step 4: Run router and privacy assertions**

Run:

```powershell
git check-ignore -v meetings/index.md
if ($LASTEXITCODE -ne 0) { exit 1 }
git check-ignore -q meetings/CONTEXT.md
if ($LASTEXITCODE -eq 0) { Write-Error 'meetings/CONTEXT.md must be tracked'; exit 1 }
rg -n "not authoritative|exactly one entry|pending|Scoped Fallback|agenda\.md|example-emergency-fund|example-rental-property|Do not preload" meetings/CONTEXT.md
```

Expected: the first command identifies the explicit `/meetings/index.md` rule; the router is not ignored; `rg` finds every required contract concept.

- [ ] **Step 5: Commit the router boundary**

```powershell
git add -- .gitignore meetings/CONTEXT.md
git commit -m "feat: add private meeting history router"
```

---

### Task 2: Integrate lookup and index maintenance into the meeting lifecycle

**Files:**
- Modify: `CONTEXT.md`
- Modify: `_config/shared/meeting-process.md`
- Modify: `_config/shared/icm-conventions.md`
- Test: repository text assertions and ICM audit

**Interfaces:**
- Consumes: the routing and maintenance contract in `meetings/CONTEXT.md`
- Produces: chair behavior that selectively finds prior meetings and maintains one private index entry at the existing record threshold

- [ ] **Step 1: Run pre-change lifecycle assertions and verify integration is absent**

Run:

```powershell
$required = @(
  @{ Path = 'CONTEXT.md'; Pattern = 'meetings/CONTEXT\.md' },
  @{ Path = '_config/shared/meeting-process.md'; Pattern = 'meetings/index\.md' },
  @{ Path = '_config/shared/icm-conventions.md'; Pattern = 'meeting-history router|meeting history router' }
)
$found = foreach ($item in $required) {
  if (Select-String -Path $item.Path -Pattern $item.Pattern -Quiet) { $item.Path }
}
if ($found.Count -eq 0) { Write-Output 'EXPECTED FAIL: lifecycle integration is absent'; exit 1 }
Write-Error "Unexpected pre-existing integration in: $($found -join ', ')"
exit 1
```

Expected: exit 1 with `EXPECTED FAIL: lifecycle integration is absent`.

- [ ] **Step 2: Route prior-meeting lookup from the root chair contract**

In `CONTEXT.md`, add a concise instruction at meeting start or before the meeting loop:

```markdown
   - **Prior meeting context** — when the request refers to earlier work or prior context may matter,
     read `meetings/CONTEXT.md` and follow its index-first, selective-loading flow. Do not list or
     preload the complete meeting history.
```

Extend the record-capture step so it says that when the existing lazy record threshold is reached,
the chair creates or updates the meeting's single local index entry following
`meetings/CONTEXT.md`; `minutes.md` may remain `pending` until written.

- [ ] **Step 3: Define lifecycle maintenance and authority in the full meeting protocol**

In `_config/shared/meeting-process.md`:

- Add an index-first prior-meeting lookup paragraph pointing to `meetings/CONTEXT.md`.
- In `## The Meeting Record`, state that creation at the existing lazy threshold creates or updates
  exactly one `meetings/index.md` entry keyed by folder path.
- Allow `Minutes: pending` until `minutes.md` exists.
- Require updating the same entry when minutes appear, status changes, or material routing metadata
  changes.
- State that meeting record files override stale index metadata and that scoped search repairs the
  entry.
- Preserve the existing lazy-creation threshold verbatim and do not add a second definition of
  substantive meeting.

- [ ] **Step 4: Record the ICM classification**

In `_config/shared/icm-conventions.md`, update the Layer-4 description and factory/product boundary:

```markdown
- `meetings/CONTEXT.md` is tracked recursive routing guidance for the Layer-4 meeting area.
- `meetings/index.md` is local-only, evolving Layer-4 routing metadata; meeting record files remain
  authoritative.
```

Keep shipped `meetings/example-*/` classified separately as tracked reference factory content.

- [ ] **Step 5: Run focused integration assertions**

Run:

```powershell
rg -n "meetings/CONTEXT\.md|index-first|selective|complete meeting history" CONTEXT.md _config/shared/meeting-process.md
rg -n "exactly one|folder path|pending|record files|authoritative|scoped search|status" _config/shared/meeting-process.md meetings/CONTEXT.md
rg -n "meetings/CONTEXT\.md|meetings/index\.md|Layer 4|authoritative|example-" _config/shared/icm-conventions.md
```

Expected: every concept appears in the appropriate contract without contradictory lifecycle language.

- [ ] **Step 6: Run the ICM audit**

Run:

```powershell
python .\.agents\skills\maintaining-icm\scripts\audit_routed_context.py .
```

Expected: exit 0 with no ICM audit failures.

- [ ] **Step 7: Commit lifecycle integration**

```powershell
git add -- CONTEXT.md _config/shared/meeting-process.md _config/shared/icm-conventions.md
git commit -m "feat: integrate meeting history routing"
```

---

### Task 3: Verify acceptance criteria and repository cleanliness

**Files:**
- Verify: `.gitignore`
- Verify: `meetings/CONTEXT.md`
- Verify: `CONTEXT.md`
- Verify: `_config/shared/meeting-process.md`
- Verify: `_config/shared/icm-conventions.md`

**Interfaces:**
- Consumes: completed Tasks 1 and 2
- Produces: fresh evidence that routing, privacy, ICM structure, and Git state meet the design

- [ ] **Step 1: Run the complete ICM audit and whitespace validation**

Run:

```powershell
python .\.agents\skills\maintaining-icm\scripts\audit_routed_context.py .
git diff HEAD~2 --check
```

Expected: both commands exit 0; the audit reports no failures and Git reports no whitespace errors.

- [ ] **Step 2: Verify privacy and tracked-router behavior**

Run:

```powershell
git check-ignore -v meetings/index.md
if ($LASTEXITCODE -ne 0) { exit 1 }
git check-ignore -q meetings/CONTEXT.md
if ($LASTEXITCODE -eq 0) { Write-Error 'meetings/CONTEXT.md is unexpectedly ignored'; exit 1 }
git ls-files --error-unmatch meetings/CONTEXT.md
if ($LASTEXITCODE -ne 0) { exit 1 }
git ls-files meetings/index.md
```

Expected: `index.md` resolves to its explicit ignore rule; `CONTEXT.md` is tracked and not ignored; the final command prints nothing.

- [ ] **Step 3: Verify contract coverage**

Run:

```powershell
$files = @('meetings/CONTEXT.md', 'CONTEXT.md', '_config/shared/meeting-process.md', '_config/shared/icm-conventions.md')
$patterns = @('pending', 'folder path', 'authoritative', 'scoped', 'agenda.md', 'example-emergency-fund', 'example-rental-property')
foreach ($pattern in $patterns) {
  $match = Select-String -Path $files -Pattern ([regex]::Escape($pattern)) -SimpleMatch:$false
  if (-not $match) { Write-Error "Missing contract concept: $pattern"; exit 1 }
}
Write-Output 'All meeting-history contract concepts are present.'
```

Expected: exit 0 and `All meeting-history contract concepts are present.`

- [ ] **Step 4: Confirm no private meeting data is staged or tracked**

Run:

```powershell
git status --short
git diff --cached --name-only
git ls-files 'meetings/*' | Sort-Object
```

Expected: working tree is clean after the two implementation commits; staged output is empty; tracked meeting files consist only of `meetings/CONTEXT.md` and shipped `example-*` records.

- [ ] **Step 5: Review the final commit range**

Run:

```powershell
git log -3 --oneline
git diff HEAD~2 --stat
git diff HEAD~2 -- .gitignore meetings/CONTEXT.md CONTEXT.md _config/shared/meeting-process.md _config/shared/icm-conventions.md
```

Expected: exactly the router boundary and lifecycle integration changes described by this plan, with no unrelated edits.
