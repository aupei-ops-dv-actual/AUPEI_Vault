---
node_id: AO_INFRA_FIX_IT
title: "Active Repair Orders — Infrastructure"
version: v1.0
date_minted: 2026-05-11
author: "C@ the Red (ζ synth pole)"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, repair_orders, fix_it, agent_readable, register]
depends_on: [AO_INFRA_000_RUNNING]
schema_version: 1
consumer_hint: "Both human operators and automated agents may read this file. Frontmatter fields per repair order are designed for programmatic parsing."
---

# Active Repair Orders — Infrastructure

## What this file is

A register of **staked repair orders** for AUPEI infrastructure. Each repair order is a discrete unit of "something is broken, here is what we know, here is what to do." Format is designed to be readable by:

- A future human operator (R@ or successor) coming back to fix the thing
- An automated agentic repair pipeline that can execute against the steps mechanically
- A current-session agent triaging which repair to take on next

Each repair order is **append-only** at write time and **status-mutable** as work progresses (`STAKED → IN_PROGRESS → BLOCKED | COMPLETED | ABANDONED`).

## How to add a repair order

1. Choose the next `REPAIR-NNN` id (sequential, never reused).
2. Add a new `### REPAIR-NNN — <one-line title>` section at the end of the "Active Repair Orders" section below.
3. Fill in the schema fields (see existing entries as templates).
4. If you can't complete every field with confidence, **say so** — `confidence: low` or `unknowns_listed: true` is more useful than fabricated certainty.
5. Cross-link to AO_INFRA_consider_it.md if there are deliberation items the repair surfaces but doesn't resolve.

## How to retire a repair order

When status moves to `COMPLETED` or `ABANDONED`, leave the entry in place — do not delete. Add a `### closure_note` subsection describing what was actually done (or why work stopped). This preserves the institutional memory for future-similar failures.

---

## Active Repair Orders

### REPAIR-001 — Qdrant rebuild after 2026-05-10 vector index loss

**status:** STAKED
**severity:** medium
**load_bearing:** yes (Chamber RAG depends on Qdrant)
**recoverability:** full from source corpus (no permanent data loss)
**triggered_by:** ops_infra_change_2026-05-11_001 (Tailscale commissioning on NAS)
**date_staked:** 2026-05-11
**owner_seat:** ζ (audit) + Ω̂ (execution)
**estimated_effort:** 1–2 hours of focused work + ingestion compute time
**blocked_by:** none
**blocks:** Chamber MVP RAG queries returning current data, GraphRAG build incorporating Phase 5 distillates

#### Context

On 2026-05-10 we commissioned Tailscale on the NAS as a Docker container. During that work, the Docker daemon (or a UGOS-internal sequence around it) cycled all running containers. The Qdrant container was removed-and-recreated as part of that cycle. The new Qdrant container came up with a **misconfigured bind-mount** and zero collections.

The previous Qdrant state (5 collections, 2,874 points as of 2026-04-13 per `MEMORY.md` and `project_qdrant_architecture.md`) is **not on disk anywhere we have found** — see investigative log in `ops_infra_change_2026-05-11_001.json` and task #47.

#### Confirmed findings (read-only diagnostic 2026-05-11)

- `find /volume1 /volume2 -maxdepth 8 -type d \( -name segments -o -name wal \)` → ZERO results. Qdrant on-disk signature directories nowhere on the NAS.
- `sudo docker volume ls` → empty. No named Docker volumes at all.
- `sudo btrfs subvolume list /volume2` → only `academy_fast` and `docker`; no snapshot subvolumes.
- `sudo docker inspect qdrant --format '{{json .Mounts}}'` → `Source=/volume2/academy_fast`, `Destination=/qdrant_storage`.
- `sudo readlink /proc/<qdrant_pid>/cwd` → `/qdrant`.
- `sudo cat /proc/<qdrant_pid>/cmdline` → `./qdrant` (no `--config`, no env override).
- Conclusion: current Qdrant writes to its **ephemeral container filesystem** at `/qdrant/storage/` because the bind-mount destination (`/qdrant_storage`) does NOT match Qdrant's default storage path (`/qdrant/storage`). Bind-mount is decorative. Any ingestion now would also be lost on next restart.

#### Source corpus inventory (where rebuild content lives)

| Qdrant collection (per memory) | Pts (last known) | Rebuild source |
|---|---|---|
| `institutional_packets` | 1,742 | `AUPEI/genesis-extraction/04_PACKETS/` (202 packets, 2 MB) + `04_SALVAGE_PACKETS_NORMALIZED/` (205 packets, 2.1 MB) |
| `seat_memories` | 100 | `AUPEI/genesis-extraction/05_SEAT_DISTILLATION/` (5 distillates, 337 KB, 15-section canonical template) |
| `control_layer` | 197 | `AUPEI_Vault/00_Governance/` + `AUPEI/genesis-extraction/INDEX/` (axiom_curation, adjudication rubric, GraphRAG schema) |
| `canon_prooffield` | 830 | `AUPEI_Vault/03_Atlas_of_Constants/` + Appendix PDFs (AoC_01–06, Appx 03/07/18X, etc.) |
| `operations_log` | 5+ | `AUPEI/operations_log_staging/ops_infra_change_*.json` (last seen entry: 2026-05-11_001) |

Schema check on `04_PACKETS/`: 202 files, 18 schema variants, 164 (81%) share the canonical 14-key Phase-4-enriched structure; remaining 38 have minor additive variations (optional fields). Re-ingestion can normalize this if needed; the pipeline already handled the variance once.

#### Repair steps

**STEP 1 — Pre-rebuild checks (5–15 min, must run before STEP 2)**

1.1. Check `/volume1/Backups/` on the NAS for any incidental Qdrant data backup:
```bash
ssh aupei_ops@10.10.10.102 'sudo find /volume1/Backups -iname "*qdrant*" -o -iname "*collection*" 2>/dev/null | head -20'
```
Confidence finding anything: ~15%. If something is found, ABORT rebuild and recover from backup instead.

1.2. Check `aupei-mini` (Mac Mini) for whether Qdrant ever lived there:
```bash
# requires Mini to be reachable; check tailnet status
ssh aupeiops@aupei-mini.local 'docker ps -a 2>/dev/null | grep qdrant; ls -la /Users/aupeiops/qdrant_storage 2>/dev/null'
```
Confidence finding anything: ~10%. Mini was the original boot-sovereign — if Qdrant lived there before NAS migration, leftover state may persist.

1.3. Verify source corpus integrity:
```bash
cd ~/Documents/IDIOTH_WINDS/AUPEI/genesis-extraction
ls 04_PACKETS/ | wc -l      # expect 202
ls 04_SALVAGE_PACKETS_NORMALIZED/ | wc -l   # expect 205
ls 05_SEAT_DISTILLATION/*.md | wc -l         # expect 5
wc -l 05_SEAT_DISTILLATION/*.md              # expect 3,867 total ±1%
```

**STEP 2 — Fix the bind-mount (15–30 min, MUST happen before any ingestion attempt)**

The current container's bind-mount is decorative; ingestion will silently land in ephemeral storage and be lost on next restart. Fix BEFORE any rebuild work.

ONE of the following must be true post-fix:
- **(2a) RECOMMENDED:** bind-mount `Destination = /qdrant/storage` (matches Qdrant's default storage path). Update UGOS Docker container config to change the destination from `/qdrant_storage` to `/qdrant/storage`. Source stays at `/volume2/academy_fast/qdrant_storage`.
- **(2b) Alternative:** Add env var `QDRANT__STORAGE__STORAGE_PATH=/qdrant_storage` to align Qdrant's runtime path with the existing mount destination. Simpler in some Docker UIs.
- **(2c) Alternative:** Mount a Qdrant config YAML to `/qdrant/config/production.yaml` overriding `storage.storage_path`.

Choice between 2a/2b/2c is a deliberation item — see `AO_INFRA_consider_it.md → CONSIDER-001`.

Verification gate (must pass before STEP 3):
```bash
# Restart container after config change
# Then test that data survives a restart:
ssh aupei_ops@10.10.10.102 'curl -s -X PUT http://localhost:6333/collections/test_persistence -H "Content-Type: application/json" -d "{\"vectors\":{\"size\":4,\"distance\":\"Cosine\"}}"'
ssh aupei_ops@10.10.10.102 'sudo docker restart qdrant'
sleep 10
ssh aupei_ops@10.10.10.102 'curl -s http://localhost:6333/collections'
# Must show {"collections":[{"name":"test_persistence"}]}
ssh aupei_ops@10.10.10.102 'curl -s -X DELETE http://localhost:6333/collections/test_persistence'
```

If the test_persistence collection survives the restart: GATE PASSED. Move on.
If it does NOT: bind-mount fix did not work. STOP. Re-investigate.

**STEP 3 — Re-ingest from source corpus**

3.1. Locate or rewrite the ingestion pipeline. Per `project_qdrant_architecture.md` memory, pipeline is `qdrant_ingest.py` with modes `auto`, `prooffield`, `opslog`. Search for the script:
```bash
find ~/Documents/IDIOTH_WINDS -name "qdrant_ingest.py" 2>/dev/null
find ~/Documents/IDIOTH_WINDS -name "*ingest*.py" 2>/dev/null | head -20
```
If not found, this becomes a sub-task and CONSIDER-002 in the deliberation register.

3.2. Embedding model: `nomic-embed-text:v1.5` per memory. 768 dimensions. Make sure Ollama or whatever serves embeddings is up; verify with a single-vector test before bulk ingestion.

3.3. Ingest in order (small to large, to catch errors early):
- `operations_log` (5+ JSONs in `AUPEI/operations_log_staging/`)
- `seat_memories` (5 distillates, ~3,867 lines)
- `control_layer` (~200 items from governance + INDEX)
- `institutional_packets` (~400 packets total when both `04_PACKETS` and `04_SALVAGE_PACKETS_NORMALIZED` are ingested)
- `canon_prooffield` (~830 chunks from Vault PDFs + appendices)

3.4. After each collection, verify count via API:
```bash
curl -s http://aupei-nas.taile22fd1.ts.net:6333/collections/<name> | jq .result.points_count
```

#### Success criteria

- `curl http://localhost:6333/collections` returns all 5 expected collections
- Per-collection point counts within ±5% of memory's recorded counts (2,874 total)
- A test query against `canon_prooffield` returns coherent, on-topic chunks for a known-good query (e.g., "fine-structure constant alpha")
- After `docker restart qdrant`, all collections AND point counts persist
- `ops_infra_change_2026-05-11_NNN.json` entry filed in `operations_log_staging/` documenting the rebuild
- `MEMORY.md` updated to reflect post-rebuild date and counts

#### Unknowns / where to keep looking

- **Why was the prior container removed?** Docker daemon restart? UGOS auto-update? Manual? Knowing this prevents repeat. Look at:
  - `journalctl --since "2026-05-10 18:00" --until "2026-05-11 04:00"` for docker daemon events
  - `~/.docker/config.json` for any auto-update settings
  - UGOS Docker app event log if it has one in the UI
- **Was the prior container's mount different?** Without the prior container's inspect output, we can't know. Look at:
  - `sudo find /volume2/@docker -name "config.v2.json"` and search for `"qdrant"` (Docker stores per-container metadata here even after removal sometimes)
  - UGOS Docker app may export a snapshot of past container configs
- **Could there be a Qdrant backup we missed?** Worth checking:
  - `/volume1/Backups/` (the UGOS shared folder) — see STEP 1.1
  - aupei-mini local filesystem — see STEP 1.2
  - Any cron-driven export jobs on Mini or NAS (unlikely; would be in memory if so)
- **Is the qdrant_ingest.py script in the workspace anywhere?** Memory mentions it but doesn't pin the path.

#### Provenance

- Diagnostic session: 2026-05-11 (cowork session, R@ + C@ the Red ζ pole)
- Diagnostic commands and output: `ops_infra_change_2026-05-11_001.json` action_items + body
- Source corpus walk: this session, recorded in chat history
- Related memory: `project_qdrant_architecture.md`, `project_sancho_corpus.md`, `feedback_institutional_memory.md`
- Cross-link to deliberation: see `AO_INFRA_consider_it.md → CONSIDER-001`, `CONSIDER-002`

---

(Future repair orders REPAIR-002, REPAIR-003, ... are appended below as they arise.)
