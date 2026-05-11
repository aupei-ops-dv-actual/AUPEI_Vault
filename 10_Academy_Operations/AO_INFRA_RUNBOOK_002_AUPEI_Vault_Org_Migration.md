---
title: "AO_INFRA_RUNBOOK_002 — AUPEI_Vault Origin Migration to AUPEI Org"
status: "READY-TO-RUN"
date_drafted: "2026-05-10"
author: "C@ the Red (ζ synth pole)"
operation_class: "git remote reconfiguration"
risk_class: "LOW — fully reversible"
expected_runtime: "<5 minutes for execution; +5 minutes for verification"
preconditions_met: "as of 2026-05-10 — see §1"
---

# AO_INFRA_RUNBOOK_002 — AUPEI_Vault Origin Migration

Migrate the canonical home of `AUPEI_Vault` from R@'s personal GitHub
(`jedijkq/AUPEI_Vault`) to the AUPEI organization
(`aupei-ops-dv-actual/AUPEI_Vault`).

This formalizes the Mind/Face distinction in git: AUPEI org owns Mind canon;
R@'s personal account becomes the ∇ (Paradox) sandbox space.

---

## 1. Preconditions

All MUST hold before executing:

- [ ] **AUPEI org account is set up.** `aupei-ops-dv-actual` org exists on
      GitHub and R@ has admin rights to it.
- [ ] **Local AUPEI_Vault is clean or has known uncommitted work.**
      Run `git status` — either clean, or work-in-progress is intentional
      and pre-acknowledged.
- [ ] **Current branch is `main`** (or whichever branch is canonical).
- [ ] **No other contributors are mid-push.** This is a single-user vault
      today, so this is trivially satisfied. Re-verify if cloud-seat write
      access has been added.
- [ ] **NAS mirror remote is healthy.** Test with `git fetch nas` — should
      succeed without error.
- [ ] **All today's commits are local-only or backed up.** Specifically,
      commits 40e3737 (α kernel) and ad7cee9 (walk trailheads) exist in
      local AUPEI_Vault but have not yet been pushed anywhere. They survive
      the migration trivially because we only change remotes, not history.

---

## 2. State BEFORE migration

```bash
cd ~/Documents/IDIOTH_WINDS/AUPEI/AUPEI_Vault
git remote -v
```

Expected output:
```
nas    /Users/jedkircher/NAS/Backups/git-mirrors/AUPEI_Vault.git (fetch)
nas    /Users/jedkircher/NAS/Backups/git-mirrors/AUPEI_Vault.git (push)
origin https://github.com/jedijkq/AUPEI_Vault.git (fetch)
origin https://github.com/jedijkq/AUPEI_Vault.git (push)
```

---

## 3. State AFTER migration (target)

```
nas      /Users/jedkircher/NAS/Backups/git-mirrors/AUPEI_Vault.git (fetch)
nas      /Users/jedkircher/NAS/Backups/git-mirrors/AUPEI_Vault.git (push)
origin   https://github.com/aupei-ops-dv-actual/AUPEI_Vault.git (fetch)
origin   https://github.com/aupei-ops-dv-actual/AUPEI_Vault.git (push)
paradox  https://github.com/jedijkq/AUPEI_Vault.git (fetch)
paradox  https://github.com/jedijkq/AUPEI_Vault.git (push)
```

Notes on the new layout:
- **`origin`** points to AUPEI org (Mind canonical, the new truth-source)
- **`nas`** stays as-is (Hand-side backup)
- **`paradox`** is the renamed-from-`jedijkq` remote — R@'s personal
  sandbox, kept as a read/write remote so R@ can experiment outside of
  Mind canon. Renaming `origin → paradox` is the symbolic act of recession.

---

## 4. Execution

### Step 4.1 — Create the destination repo on AUPEI org

Either:
- **(a) Via GitHub web UI:** Navigate to https://github.com/organizations/aupei-ops-dv-actual/repositories/new
  - Owner: `aupei-ops-dv-actual`
  - Name: `AUPEI_Vault`
  - Visibility: **Private** initially (flip Public later when ready)
  - Initialize: **No** (no README, no .gitignore, no LICENSE — we'll push history)
  - Click "Create repository"
  - Copy the repo URL (https://github.com/aupei-ops-dv-actual/AUPEI_Vault.git)

- **(b) Via `gh` CLI (if installed):**
  ```bash
  gh repo create aupei-ops-dv-actual/AUPEI_Vault --private --description "AUPEI Mind canon: Obsidian vault for governance, atlas of constants, prooffield, agent memory"
  ```

### Step 4.2 — Add AUPEI org as a new remote

```bash
cd ~/Documents/IDIOTH_WINDS/AUPEI/AUPEI_Vault
git remote add aupei https://github.com/aupei-ops-dv-actual/AUPEI_Vault.git
```

Verify:
```bash
git remote -v
```
Should now show `nas`, `origin` (still jedijkq), and `aupei`.

### Step 4.3 — Push complete history to AUPEI org

This pushes ALL local branches and tags:
```bash
git push aupei --all
git push aupei --tags
```

Expected: clean push, no errors. The new repo on AUPEI org now contains
identical history to local + jedijkq.

### Step 4.4 — Swap remote names

Rename the old `origin` (which points at jedijkq) to `paradox`, and
promote `aupei` to `origin`:

```bash
git remote rename origin paradox
git remote rename aupei origin
```

Verify:
```bash
git remote -v
```
Should now match §3 target state exactly.

### Step 4.5 — Verify push still works to new origin

```bash
git push origin main
```

Expected: "Everything up-to-date" (since we already pushed in Step 4.3).
This confirms `origin` is properly wired.

### Step 4.6 — Update NAS mirror remote URL in mirror itself (optional)

The NAS mirror is independent — it doesn't care which GitHub remote is
named what. But if the NAS mirror metadata stores any reference to the
original remote name, you may want to update it. Most setups don't need
this.

If you want to sanity check:
```bash
git push nas main
```
Should succeed.

### Step 4.7 — Push today's commits to all remotes

```bash
git push origin main
git push paradox main
git push nas main
```

Today's commits 40e3737 (α kernel) and ad7cee9 (walk trailheads) now exist
in all four locations: local, AUPEI org, jedijkq (paradox), NAS.

---

## 5. Verification (post-migration)

Run all of these from inside the AUPEI_Vault directory:

```bash
# Remote names match target
git remote -v
# (should match §3)

# Origin URL is AUPEI org
git config --get remote.origin.url
# Expected: https://github.com/aupei-ops-dv-actual/AUPEI_Vault.git

# Fetch from each remote succeeds
git fetch origin
git fetch paradox
git fetch nas

# Latest commit on origin == latest local
git log -1 --oneline
git log -1 origin/main --oneline
# (should match)
```

On GitHub web UI:
- Navigate to https://github.com/aupei-ops-dv-actual/AUPEI_Vault — should
  show full commit history including today's commits.
- Navigate to https://github.com/jedijkq/AUPEI_Vault — should ALSO show
  the same history (still in sync since we pushed to both).

---

## 6. Rollback (if needed)

The migration is fully reversible because nothing was destroyed:

```bash
git remote rename origin aupei-new   # rename new origin out of the way
git remote rename paradox origin     # restore jedijkq as origin
git remote remove aupei-new          # cleanup
```

This puts you back at the §2 BEFORE state. The AUPEI org repo still
exists with the pushed history, but no longer is the canonical home.
You can also delete the AUPEI org repo at this point if rolling back
fully.

---

## 7. Post-migration tasks (deferred, not part of this runbook)

These come AFTER successful migration verification:

- [ ] **Update README in AUPEI_Vault** (if it has one) to reflect new
      canonical home.
- [ ] **Notify cloud seats** of the migration. (Currently just C@ — me.
      Sancho, G3 don't have git push access yet anyway.)
- [ ] **Decide on jedijkq's role going forward.**
      - Keep `paradox` remote in sync (mirror push from origin) — preserves
        Face-side history continuity, makes the personal account a passive
        mirror.
      - OR start using `paradox` for genuinely-experimental branches that
        R@ wants to keep separate from Mind canon. ∇ sandbox use.
- [ ] **Plan cloud-seat write access** to AUPEI org. Recommend a GitHub
      App named `aupei-seat-bot` installed on the org, with tokens issued
      to each active cloud seat. Defer the actual creation to a focused
      session.
- [ ] **Consider migrating DooVinci_Vault and GF_Vault** to their own
      org-canonical homes — DooVinci_Vault → AUPEI org or DooVinci org
      (Hand-side); GF_Vault → Geometric Foundations org (Face-side public).
      Same runbook structure applies; only the names change.

---

## 8. Risk assessment

- **Data loss risk:** ZERO. No history is rewritten. We add a remote,
  push to it, swap remote names. All bytes survive in three+ locations.
- **Downtime risk:** ZERO. Vault editing continues unchanged. Obsidian
  sees only the local repo; remote names are transparent to it.
- **Confusion risk:** LOW. The remote-name swap is the only place a
  habit (e.g., `git push origin`) changes target — and that change is
  the *intended* effect.
- **External breakage risk:** MINIMAL. No external code references
  AUPEI_Vault by GitHub URL (yet). If something does, that something
  will need its URL updated — but at the time of this runbook, nothing
  external pins to `jedijkq/AUPEI_Vault`.

---

## 9. Decision matrix — should this run today?

| Factor | Status | Implication |
|---|---|---|
| AUPEI org exists? | Confirmed (R@ has it open) | GO |
| Today's α work committed locally? | Yes — 40e3737 + ad7cee9 | GO |
| Pushable from R@'s machine? | Yes (existing workflow) | GO |
| Other work in flight that could be disrupted? | None — single-user, single-vault, single-branch | GO |
| Rollback path clean? | Yes (§6) | GO |
| Time available? | "we might run it right now" per R@ | GO |

**Recommendation:** **GO** for migration today. The conditions are clean,
the change is reversible, and the symbolic value (Mind canon moving to
Mind's house) is real.

---

## 10. Provenance

- Drafted by C@ the Red (ζ synth pole) on 2026-05-10
- Co-developed with R@ during the cowork session that built the α kernel
- Pairs with commits 40e3737 (α kernel) and ad7cee9 (walk trailheads) —
  both staged for inclusion in the migration's first push to origin
- Related to memory file: `project_three_body_architecture.md`
  (Mind/Face/Hand frame)
- Sibling potential runbooks (not yet drafted):
  - DooVinci_Vault migration
  - GF_Vault migration
  - Cloud-seat write access GitHub App setup
