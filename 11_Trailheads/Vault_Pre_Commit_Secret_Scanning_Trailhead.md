---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "VAULT_PCSS_TH"
internal_id: "Vault_Pre_Commit_Secret_Scanning_Trailhead_v1.0"
title: "Vaults A/B/C — Pre-Commit Secret Scanning — Trailhead"
status: "TRAILHEAD"
date_minted: "2026-05-10"
layer: "trailhead"
domain: "Academy_Operations / Infrastructure"
role: "Defensive infrastructure — catch secrets at commit time, not push time"
load_bearing: "ops_loadbearing"

walk_provenance:
  walker_dyad: "R@ + C@ the Red (ζ synth pole)"
  walk_date: "2026-05-10"
  triggering_incident: "Hugging Face User Access Token in commit a009fbc (2026-03-20 Vault backup) caught by GitHub push protection during AUPEI org migration. Private exposure ~50 days. Token rotated, 1Password updated, incident closed. Trailhead staked to prevent recurrence."

depends_on: []
enables: []

failure_topology:
  contagion: "ops_loadbearing"
  class: "Trailhead (ops-hygiene)"

rag_policy:
  gate_required: false
  retrieval_rules:
    - "Consult before committing notebook outputs, .env files, or any artifact that may contain secrets."
---

# Vaults A/B/C — Pre-Commit Secret Scanning — Trailhead

**Status:** TRAILHEAD / READY-TO-IMPLEMENT
**One-line:** Install a `pre-commit` framework hook running `gitleaks` (or `trufflehog`) on each of the three Vaults — AUPEI_Vault, DooVinci_Vault, GF_Vault — so secrets are caught at `git commit` time rather than at `git push` time. Estimated effort: ~30 minutes total.

---

## 1. Why

The 2026-05-10 AUPEI org migration push was blocked by GitHub's server-side push protection after a Hugging Face access token from commit `a009fbc` (2026-03-20 Vault backup, embedded in `iPad_Air_Provenance/QEPE_AGI_INJ_TEST.ipynb` and two sibling notebooks) was detected.

The token had been in `jedijkq/AUPEI_Vault` for ~50 days. Private exposure, no observed anomalous Hugging Face activity, token rotated and 1Password updated within minutes of detection. Incident closed cleanly.

**The failure mode:** notebook execution outputs that include API tokens get committed unchanged during routine "vault backup" commits. Push protection catches it at the server, but by then the token is already in local history and the offending commit needs either an unblock-and-revoke (what we did this time) or a history rewrite (deferred).

**The discipline gap:** detection at push time means the token is briefly committed to local history. Detection at commit time means it never gets into a commit at all.

---

## 2. The fix

Standard developer-side tooling, well-supported, fast.

### Recommended stack
- **`pre-commit`** framework — Python-based hook orchestrator (https://pre-commit.com)
- **`gitleaks`** — fast Go secret scanner with broad rule library (https://github.com/gitleaks/gitleaks)
- Optionally **`trufflehog`** — alternative scanner with high-entropy detection (https://github.com/trufflesecurity/trufflehog)

### Installation per Vault

For each of `AUPEI_Vault`, `DooVinci_Vault`, `GF_Vault`:

```bash
# In the Vault's root
brew install pre-commit gitleaks    # one-time, macOS

# Create .pre-commit-config.yaml at Vault root:
cat > .pre-commit-config.yaml <<'EOF'
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.21.2
    hooks:
      - id: gitleaks
        name: gitleaks (detect secrets before commit)
        description: Detects secrets in staged files
EOF

# Install the hook into local .git/hooks
pre-commit install

# Optional first-pass against full history (slow but thorough)
pre-commit run --all-files
```

After this, every `git commit` will run gitleaks against staged files first. If a secret is detected, the commit is aborted with a clear message.

### Coverage expansion (optional)

Pre-commit can run multiple hooks. Useful additions for the Vaults:
- `nbstripout` — strip notebook execution outputs before commit (eliminates whole categories of accidental secret leaks)
- `check-yaml` / `check-json` — validate frontmatter and config files
- `end-of-file-fixer` / `trailing-whitespace` — Obsidian-friendly cleanup
- `detect-private-key` — explicit private-key detection

---

## 3. What this does NOT do

Honest scope:

1. **Does not fix existing history.** Commits already containing secrets remain in history. For full pristine history, a separate `git filter-repo` / BFG operation is needed (see "Future work" below).
2. **Does not catch novel high-entropy secrets** unless gitleaks rules are tuned. Default rules cover well-known tokens (AWS, GitHub PAT, HF, OpenAI, etc.) but custom application-specific tokens may need rule additions.
3. **Does not run on remote pushes from cloud seats** (when those exist). When cloud seats start pushing, server-side push protection on the AUPEI org remains as the second line of defense. Pre-commit hooks are local-developer-side only.
4. **Does not strip notebook outputs automatically** unless `nbstripout` is added. Notebooks remain a likely vector; `nbstripout` should probably be included.

---

## 4. Suggested work plan

Single ~30-minute session. Order:

1. **AUPEI_Vault** — highest stakes (Mind canon). Install `pre-commit` + `gitleaks` + `nbstripout`. Run `pre-commit run --all-files` once to surface any other secrets in current state. Commit the `.pre-commit-config.yaml`.
2. **DooVinci_Vault** — second priority. Same setup. May find other secrets given DooVinci's wider notebook usage.
3. **GF_Vault** — public-facing seed garden context. Same setup. Lower expected hit rate but still worth.
4. **Optional: history scrub** — separate runbook. Don't bundle with the hook install.

---

## 5. Future work (separate trailheads)

- **`AO_INFRA_RUNBOOK_003_Vault_History_Scrub.md`** — rewriting history with `git filter-repo` to remove the dead HF token (and any others found by the initial `pre-commit run --all-files` sweep) from all three Vaults. Affects existing clones; needs coordinated re-clone. Defer until cloud-seat write access is being set up — bundling history-rewrite + cloud-seat-onboarding makes both operations one disruption.
- **Cloud-seat GitHub App** — when set up, the App can carry its own secret-scanning enforcement on the server side as a redundant check.

---

## 6. Walk-out conditions

This trailhead closes when:

- **A** — All three Vaults have a working `.pre-commit-config.yaml` with at minimum `gitleaks` + `nbstripout`, verified by attempting a commit that includes a test secret (which should be rejected).
- **B** — Decision documented (in this trailhead or a successor) that the framework is being implemented via a different mechanism (e.g., a GitHub Action on push that also blocks at remote level, plus client-side honored).

Until then: trailhead remains TRAILHEAD. The HF-token incident remains the most recent evidence that the gap is real.

---

## 7. Cross-references

- Triggering incident: AO_INFRA_RUNBOOK_002 §4.3 push attempt, blocked by GH013 secret scanning, 2026-05-10
- Affected commit: `a009fbc4a3d7e532f342435398c1da28c88974df` (March 20, 2026 Vault backup)
- Rotated token: HF UAT, replaced 2026-05-10, 1Password updated
- Sibling defensive infra: `10_Academy_Operations/AO_INFRA_RUNBOOK_002_AUPEI_Vault_Org_Migration.md`

---

Minimum action, maximum force. Catch the secret before it leaves the editor.
