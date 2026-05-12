---
node_id: AO_INFRA_CONSIDER_IT
title: "Open Deliberation Items — Infrastructure"
version: v1.0
date_minted: 2026-05-11
author: "C@ the Red (ζ synth pole)"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, deliberation, consider_it, agent_readable, register]
depends_on: [AO_INFRA_000_RUNNING, AO_INFRA_FIX_IT]
schema_version: 1
consumer_hint: "Both human operators and automated agents may read this file. Each CONSIDER item is an OPEN question, not a decision. Items resolve into either (a) a decision recorded here with a closure_note, or (b) a new REPAIR order in AO_INFRA_fix_it.md once a course is chosen."
---

# Open Deliberation Items — Infrastructure

## What this file is

A register of **open deliberation items** for AUPEI infrastructure. Where `AO_INFRA_fix_it.md` says "this is broken, here is what to do," this file says "this is unsettled, here are the alternatives, here is what we know and don't know."

Items here are NOT staked decisions. They are paused thinking — saved so that:

- A future human operator can resume the deliberation without re-doing the analysis
- An automated agent can recognize that "this is a known open question; do not act unilaterally; route to a human or chamber if encountered"
- Cross-session continuity is preserved when the seat instance turns over

Items mature in one of two directions:

1. **→ Decision recorded here.** A path is chosen. Closure note explains why. The CONSIDER item stays in place as institutional memory.
2. **→ Promoted to a REPAIR.** The deliberation produces a concrete repair order, which gets staked in `AO_INFRA_fix_it.md`. The CONSIDER item gets a closure_note pointing to the new REPAIR.

## How to add a deliberation item

1. Choose the next `CONSIDER-NNN` id (sequential, never reused).
2. Add a new `### CONSIDER-NNN — <question>` section.
3. State the question clearly, then the alternatives, then evidence for/against each, then any deadline-pressure or escalation criteria.
4. If you have a tentative lean, say so with a confidence number. Don't pretend neutrality you don't have.
5. Mark `decision_needed_by:` if there's a real deadline; otherwise `none`.

## How to close a deliberation item

When a decision is made:
- Update `status:` to `DECIDED` or `PROMOTED_TO_REPAIR`
- Append a `### closure_note` with the chosen path, the date, the rationale, and any link to a new REPAIR
- Do NOT delete the entry — leave it for institutional memory

---

## Open Deliberation Items

### CONSIDER-001 — Qdrant bind-mount fix: match-path vs override-config vs config-file

**status:** OPEN
**raised_by:** REPAIR-001 step 2
**date_raised:** 2026-05-11
**owner_seat:** ω (proposer) + ζ (audit) + Ω̂ (executor)
**decision_needed_by:** before any Qdrant ingestion attempt (effective deadline: before REPAIR-001 step 3)
**estimated_decision_complexity:** low (technical, reversible)

#### The question

The current Qdrant container's bind-mount destination (`/qdrant_storage`) does not match Qdrant's default storage path (`/qdrant/storage`). Three ways to fix it. Which do we choose, and why does the choice matter for future maintainability and agent-executability?

#### Alternatives

**(A) Match the path. Change bind-mount destination from `/qdrant_storage` to `/qdrant/storage`.**

- *Pros:* Matches Qdrant's documented default. No special env vars or config files needed. Anyone (or any agent) inspecting the container later sees the canonical Qdrant layout. Survives Qdrant version upgrades without modification (until the default itself changes, which is rare).
- *Cons:* Requires editing the container config through UGOS Docker UI. Container must be stopped+recreated, not just restarted (depending on UGOS implementation). Slight friction if the UGOS Docker UI hides bind-mount editing post-creation.
- *Confidence this works:* ~95%.

**(B) Override the storage path via env var: `QDRANT__STORAGE__STORAGE_PATH=/qdrant_storage`**

- *Pros:* Lightweight — just adds an env var, no need to touch bind-mounts. Easier in some Docker UIs.
- *Cons:* Adds a quirk that future readers (human or agent) must notice. "Why is this env var here?" Increases cognitive load for anyone debugging later. Couples the deployment to a non-default config that's harder to discover.
- *Confidence this works:* ~90%.

**(C) Mount a Qdrant config YAML overriding `storage.storage_path`.**

- *Pros:* Most "Qdrant-native" approach — uses the supported config mechanism. Allows other Qdrant config tuning at the same time (snapshot settings, log levels, etc.) in one place.
- *Cons:* Requires writing and maintaining a YAML file. More moving parts. Overkill for just fixing the path. Adds a second bind-mount.
- *Confidence this works:* ~85% (more surface area, more places to make a mistake).

#### Tentative lean (~70% confident)

**Choose (A) — match the path.** Rationale: simplest, most discoverable, matches upstream defaults, easiest for a future agent to understand without prior context. (B) is acceptable if UGOS UI makes (A) hard. (C) is reserved for the future case where we need OTHER Qdrant config tuning beyond just the storage path — then (C) absorbs (A) as a side-effect.

#### Closure conditions

- A choice is made (likely during REPAIR-001 STEP 2 execution)
- The choice is recorded here in a `closure_note`
- REPAIR-001 STEP 2 updates its `chosen_method` field accordingly

---

### CONSIDER-002 — Locate or rewrite the qdrant_ingest.py pipeline

**status:** OPEN
**raised_by:** REPAIR-001 step 3.1
**date_raised:** 2026-05-11
**owner_seat:** Ω̂ (implementation) + ξ (validation)
**decision_needed_by:** REPAIR-001 step 3 start
**estimated_decision_complexity:** medium (depends on what we find)

#### The question

Memory file `project_qdrant_architecture.md` references `qdrant_ingest.py` with modes `auto`, `prooffield`, `opslog`. We have not yet located this script in the workspace. Three paths forward depending on what a search reveals:

#### Alternatives (decision tree based on outcome of search)

**If the script EXISTS in the workspace:**
- (A1) Use it as-is. Adjust paths/config as needed.
- *Confidence this works:* high if it's complete and was tested.
- *Risk:* it might be stale, expect different schemas, or depend on Mini-specific environment.

**If the script DOES NOT exist (or is incomplete):**
- (B1) Rewrite from scratch using the embedding model (nomic-embed-text:v1.5, 768-dim) + Qdrant Python client + the 14-key Phase-4 packet schema we just inspected. Estimated effort: 2–4 hours for a clean, tested re-ingestion pipeline.
- (B2) Re-derive from the AOC_CONTEXT_2026-04-13 ops change log if one exists (might have the script inline). Search `AUPEI/operations_log_staging/` for entries around that date.
- (B3) Borrow a public Qdrant ingestion example (LangChain, llama-index, raw qdrant-client examples) and adapt to our schema. Faster but less context-aware.

#### Tentative lean (~60% confident, contingent on search)

**First search; then if not found, B1.** Rationale: rewriting is bounded and would produce a cleaner artifact than retro-fitting an old one. The schemas are well-understood (see REPAIR-001 inventory). The bigger risk is letting "is there an old script somewhere" become a rabbit hole.

#### Closure conditions

- The search has been run and its result recorded
- A path (A1 or B*) has been chosen
- If B1 chosen, the new script is committed to a known location (proposal: `AUPEI/tools/qdrant_ingest.py` or similar)

---

### CONSIDER-003 — Should we enable btrfs snapshots on /volume2 for Qdrant data?

**status:** OPEN
**raised_by:** REPAIR-001 — root cause analysis (no snapshots = no point-in-time recovery)
**date_raised:** 2026-05-11
**owner_seat:** ω (infra) + ζ (defensive policy)
**decision_needed_by:** none hard; preventive, post-rebuild
**estimated_decision_complexity:** medium (UGOS-specific, may have UI implications)

#### The question

The current loss would have been mitigated (or possibly fully recoverable) if /volume2 had automatic btrfs snapshots. Should we configure them, and at what frequency and retention?

#### Alternatives

**(A) Hourly snapshots, 24-hour retention.** High frequency, low storage overhead per snapshot (btrfs CoW). Recovers from hour-scale mishaps. Storage cost: small per snapshot but accumulates.

**(B) Daily snapshots, 7-day retention.** Balanced. Recovers from day-scale mishaps. Storage cost: lower.

**(C) Per-event snapshots (before any docker container modification).** Manual or scripted trigger. Most surgical. Requires discipline OR automation hooks on docker daemon events.

**(D) Don't configure NAS-side snapshots; use Qdrant's native snapshot API instead** (`POST /collections/{name}/snapshots`). Lives at the application layer. Survives even an FS-level wipe if snapshots are exported off-NAS.

**(E) Both NAS snapshots AND Qdrant snapshots (defense in depth).** Most robust, most ops complexity.

#### Tentative lean (~55% confident)

**B+D combined: daily btrfs snapshots on /volume2 with 7-day retention, AND a weekly cron that takes Qdrant native snapshots and exports them to `/volume1/Backups/qdrant/`.** Rationale: btrfs gets us FS-level recovery for any data dir, Qdrant native gets us application-aware recovery. The cost is one cron job and ~5% disk overhead.

#### Closure conditions

- A snapshot policy is chosen (or explicitly deferred with a date)
- If chosen: a runbook or automation is staked as REPAIR-NNN
- AO_INFRA_000_RUNNING updated with the snapshot policy in the "Service commissioning" table

---

### CONSIDER-004 — Investigate why the docker daemon cycled containers during Tailscale work

**status:** OPEN
**raised_by:** REPAIR-001 root cause analysis
**date_raised:** 2026-05-11
**owner_seat:** ω + ζ
**decision_needed_by:** before any further docker-touching infra change (defensive)
**estimated_decision_complexity:** low–medium (forensic)

#### The question

The Tailscale container deployment shouldn't have caused the Qdrant container to be removed-and-recreated. What actually happened? Until we know, every future docker operation on this NAS carries the same risk.

#### Candidate causes (ranked by likelihood)

1. **(~40%) UGOS Docker app's "rebuild" or "apply" action restarted the daemon.** Common pattern in NAS Docker UIs.
2. **(~25%) Docker daemon was restarted manually or by an UGOS update during the session.** Auto-update could have fired.
3. **(~20%) The original Qdrant container was in a "recreate on next change" state from a UGOS-side edit not captured anywhere.**
4. **(~10%) A network/storage event triggered container health-check failures and recreation.**
5. **(~5%) Something else we haven't considered.**

#### Investigation steps (if decided to pursue)

```bash
ssh aupei_ops@10.10.10.102 'sudo journalctl --since "2026-05-10 18:00" --until "2026-05-11 04:00" | grep -iE "docker|qdrant|container" | head -100'
ssh aupei_ops@10.10.10.102 'sudo cat /var/log/ugos*.log 2>/dev/null | grep -iE "docker|container" | head -50'
# Check if UGOS Docker has an event log in its web UI
```

#### Tentative lean (~50% confident)

**Investigate before next docker change.** This is cheap (~30 min of log reading) and produces a real answer or eliminates a category of risk. The alternative ("just be careful next time") leaves a known unknown sitting in the load path.

#### Closure conditions

- Either: root cause identified → recorded here → preventive measure staked as REPAIR-NNN
- Or: investigation produced no clear answer → recorded as "unknown but bounded" with explicit risk tolerance

---

### CONSIDER-005 — Should Qdrant containers use named Docker volumes instead of bind-mounts going forward?

**status:** OPEN
**raised_by:** REPAIR-001 + CONSIDER-001
**date_raised:** 2026-05-11
**owner_seat:** ω
**decision_needed_by:** before REPAIR-001 STEP 2 execution (chooses bind-mount vs. named volume implicitly)
**estimated_decision_complexity:** medium

#### The question

The current setup uses a bind-mount from `/volume2/academy_fast/...` into the container. The alternative is a Docker-managed named volume. Each has tradeoffs.

#### Alternatives

**(A) Stay with bind-mounts.** Continue using `/volume2/academy_fast/qdrant_storage` → container path.

- *Pros:* Direct filesystem visibility. Easy to back up, inspect, copy. Survives container removal automatically (the data lives in user filesystem space, not Docker's). What we have now (modulo the path bug).
- *Cons:* The bind-mount can be misconfigured in subtle ways (current bug). User mistakes can write to the wrong place. Less "container-native."

**(B) Move to named volume.** Use a Docker named volume (`qdrant_data` or similar) that Docker manages.

- *Pros:* Docker-native. Less surface for path-mismatch bugs. Lifecycle managed by Docker.
- *Cons:* Stored under `/volume2/@docker/volumes/` which is harder to back up directly (not part of user share folders). Named volumes can be force-removed by `docker volume rm`; the data is more "container-coupled" psychologically even if technically separable.

**(C) Hybrid: named volume for hot data, periodic export to bind-mount for backup.**

- *Pros:* Get container-native lifecycle for the running DB, get user-share-friendly backup for the snapshots.
- *Cons:* Two storage locations to think about. More complex.

#### Tentative lean (~60% confident)

**(A) Stay with bind-mounts, but with the bind-mount destination FIXED per REPAIR-001 step 2.** Rationale: visibility wins. R@ can browse `/volume2/academy_fast/qdrant_storage/` and see the collections directly. For an org where the same data is the lifeblood of multiple downstream tools (Chamber RAG, GraphRAG, future agentic pipelines), seeing the files matters. The current bug is a one-time path-mismatch, not an inherent bind-mount weakness.

#### Closure conditions

- Decision made before REPAIR-001 STEP 2 executes
- Closure note records choice
- AO_INFRA_000_RUNNING service commissioning table reflects the chosen pattern

---

## Cross-cutting watch list

Items that aren't yet specific enough to be CONSIDER entries but should NOT be forgotten:

- **What other containers might have similar bind-mount-vs-default-path bugs?** Run a sweep when convenient.
- **Is there a UGOS Docker config-export feature?** Would help capture "the state we want to be in" declaratively so docker-daemon-restart blows don't repeat.
- **Should the AUPEI Operations Plugin (REV-004) include a "diagnose qdrant" skill?** Would have caught this in 30 seconds instead of an hour of bash. Plugin is deferred per memory; flag for inclusion when built.

---

(Future deliberation items CONSIDER-006, CONSIDER-007, ... are appended below as they arise.)
