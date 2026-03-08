---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_00"
internal_id: "Appx_00_The_Collapse_Map_v1.1"
title: "Appx_00 — The Collapse Map (Failure Topology)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Topology"
role: "Global dependency registry + epistemic gates + kill-switch enforcement"
load_bearing: "structural"
epistemic_status: "CANONICAL"

depends_on:
  - "GFUP"

enables:
  - "ALL"

failure_topology:
  contagion: "downstream_total"
  class: "Root Topology Node"
  kill_switch_ids:
    - "TOPOLOGY-INCONSISTENT"
    - "ENUM-DRIFT"
    - "ORPHAN-NODE"
    - "UNRESOLVED-DEPENDENCY"
    - "UNDECLARED-MODULE"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Gate-first execution: read node metadata before serving content."
    - "Dependency walking is mandatory (full transitive closure)."
    - "Contagion block: FALSIFIED or FROZEN upstream blocks downstream content."
    - "Metadata exception: metadata-only allowed to explain a block."
    - "TRAILHEAD dependencies must be surfaced as warnings when used beneath CANONICAL."

source:
  format: "curated_spine"
  reference: "7dU_GNS_MoP_RAG"
---

# Appx_00 — The Collapse Map (Failure Topology) — SPINE

## Section 1 — Purpose

This map is the **global failure topology** for the 7dU/GNS corpus.
It defines what nodes exist, what depends on what, and what breaks when something fails.
It forbids “flat retrieval” across the corpus: no node may be served without passing its dependency gates.
It enforces quarantine-first falsification so the system preserves **ruins** without serving compromised content.

---

## Section 2 — Taxonomy & gates

### 2.1 `epistemic_status` (Truth / Authority)

- **CANONICAL** — authoritative; may serve as foundation for downstream derivation.
- **TRAILHEAD** — usable, but must be explicitly labeled as non-foundational extension.
- **STUB** — placeholder; excluded from default retrieval.
- **PROPOSED** — speculative candidate; excluded from default retrieval.
- **FROZEN** — quarantined due to upstream failure; metadata-only allowed.
- **FALSIFIED** — failed discriminator/proof; metadata-only allowed.

### 2.2 `layer` (Document Role)

- **spine** — structural metadata (dependencies, kill-switches, retrieval gates).
- **content** — canonical text for retrieval/embedding.
- **support** — proofs/derivations supporting a primary node.
- **lab** — experimental protocols, scenarios, runnable designs.

### 2.3 `load_bearing` (Collapse Mechanics)

- **structural** — foundation; failure freezes downstream per contagion policy.
- **interpretive** — meaning layer; failure is local unless explicitly overridden.
- **experimental** — lab layer; failure is local; may flag assumptions but does not auto-freeze roots.

### 2.4 `contagion` (Failure Propagation)

- **downstream_total** — freeze all downstream nodes in `enables` (direct + transitive).
- **local** — freeze only the target node.
- **none** — no automatic freezing.

Default mapping:
- structural → downstream_total
- interpretive → local
- experimental → local

---

## Section 3 — Query protocol (AI traversal)

1. **Gate-first execution**  
   Resolve node metadata (`epistemic_status`, `depends_on`, `load_bearing`, `kill_switch_ids`) before retrieving semantic text.

2. **Dependency walking**  
   Resolve and validate all parents in `depends_on` (transitively, parents-first topological order).  
   Default depth is full transitive closure.

3. **Contagion block**  
   If any dependency in the resolved chain is `FALSIFIED` or `FROZEN`, content retrieval for the target node is blocked.

4. **Metadata exception**  
   Metadata-only response is permitted to explain a block (never full content).

5. **Trailhead warning**  
   If a retrieved dependency is `TRAILHEAD` while the target node is `CANONICAL`, responses must include a `[TRAILHEAD DEPENDENCY]` warning.

---

## Section 4 — Kill-switch policy (quarantine-first)

**Trigger:** A condition in `kill_switch_ids` is satisfied for a target node.

**Execution:**
1. Set target node `epistemic_status` → `FALSIFIED`.
2. Apply recursive freeze to downstream nodes reachable via `enables` edges (per contagion policy).  
   Downstream nodes become `FROZEN` (quarantined), not `FALSIFIED`, unless they have their own direct failure.

**Serving rules for blocked nodes:**
- Blocked nodes (`FROZEN` or `FALSIFIED`) never serve full content.
- On query, return a metadata-only error object:

[COMPROMISED NODE]
	•	node_id:
	•	epistemic_status:
	•	blocking_parent_id: (if FROZEN)
	•	kill_switch_id(s): (if FALSIFIED)
	•	contagion_policy_applied:

---

## Section 5 — Global topology registry (machine)

**Columns:**
- node_id
- title
- epistemic_status
- load_bearing
- module (for compressed packs)
- depends_on
- enables

| node_id   | title                            | epistemic_status  | load_bearing    | module | depends_on                           | enables                  |
|----------|----------------------------------|-------------------|-----------------|--------|--------------------------------------|--------------------------|
| GFUP     | Geometric Foundations for Unified Physics (GFUP) | CANONICAL        | structural      | M00    | —                                    | Appx_00                  |
| Appx_00  | The Collapse Map                 | CANONICAL        | structural      | M00    | GFUP                                 | Appx_01…Appx_27          |
| Appx_01  | On Absolute Absence (AA)         | CANONICAL        | structural      | M01    | Appx_00                              | Appx_02                  |
| Appx_02  | On Absolutely Everything (AE)    | CANONICAL        | structural      | M01    | Appx_01                              | Appx_03, Appx_04…Appx_06 |
| Appx_03  | On Absolutely Something (AS)     | CANONICAL        | structural      | M01    | Appx_01, Appx_02                     | Appx_04…Appx_06          |
| Appx_04  | On Zero (ζ)                      | CANONICAL        | structural      | M01    | Appx_03                              | Appx_08…Appx_27          |
| Appx_05  | On Infinity (ω)                  | CANONICAL        | structural      | M01    | Appx_03                              | Appx_08…Appx_27          |
| Appx_06  | On Chance (ξ)                    | CANONICAL        | structural      | M01    | Appx_03                              | Appx_07, Appx_12…Appx_27 |
| Appx_07  | Atlas of Constants (AoC)         | CANONICAL        | structural      | M02    | Appx_06                              | AoC_00…AoC_06            |
| AoC_00   | Constants Ledger                 | CANONICAL        | structural      | M02    | Appx_07                              | AoC_01…AoC_06            |
| AoC_01   | On π                             | CANONICAL        | structural      | M02    | AoC_00                               | AoC_02                   |
| AoC_02   | On c                             | CANONICAL        | structural      | M02    | AoC_01                               | AoC_03                   |
| AoC_03   | FSC / 137 (α)                    | CANONICAL        | structural      | M02    | AoC_02                               | AoC_04, AoC_05           |
| AoC_04   | Proton Mass                      | CANONICAL        | structural      | M02    | AoC_03                               | AoC_06                   |
| AoC_05   | Neutron Mass                     | CANONICAL        | structural      | M02    | AoC_03                               | AoC_06                   |
| AoC_06   | On Gravity (trailhead)           | TRAILHEAD        | interpretive    | M02    | AoC_04, AoC_05                       | Appx_21, Appx_27         |
| Appx_08  | On Time                          | CANONICAL        | structural      | M03    | Appx_04, Appx_05, Appx_06            | Appx_09                  |
| Appx_09  | On Spatial Dimensions            | CANONICAL        | structural      | M03    | Appx_08                              | Appx_10                  |
| Appx_10  | On Extension Bounds              | CANONICAL        | structural      | M03    | Appx_09                              | Appx_11                  |
| Appx_11  | On Gauge Structure (Structural Filter) | CANONICAL        | structural      | M04 | Appx_04, Appx_05, Appx_06, Appx_09, Appx_10 | Appx_15, Appx_17 |
| Appx_12  | Force Unification                | CANONICAL        | structural      | M04    | Appx_11                              | Appx_15                  |
| Appx_13  | On Neutrinos                     | CANONICAL        | interpretive    | M04    | Appx_12                              | Appx_15, Appx_22         |
| Appx_14  | Dark Acceleration                | CANONICAL        | interpretive    | M04    | Appx_12                              | Appx_24                  |
| Appx_15  | On the Standard Model            | CANONICAL        | structural      | M05    | Appx_11, Appx_12                     | Appx_16…Appx_20          |
| Appx_16  | On the Higgs                      | TRAILHEAD        | interpretive    | M05    | Appx_15                              | Appx_20                  |
| Appx_17  | EFT / RG                          | CANONICAL        | structural      | M05    | Appx_11                              | Appx_18, Appx_19         |
| Appx_18  | HoQG                              | CANONICAL        | interpretive    | M06    | Appx_17                              | Appx_20                  |
| Appx_19  | Hamiltonian / Lagrangian          | CANONICAL        | interpretive    | M06    | Appx_17                              | Appx_20                  |
| Appx_20  | QG Quantization                   | CANONICAL        | interpretive    | M06    | Appx_18, Appx_19                     | Appx_21                  |
| Appx_21  | GR Reduction                      | CANONICAL        | interpretive    | M06    | Appx_20                              | Appx_22                  |
| Appx_22  | On Black Holes                    | CANONICAL        | interpretive    | M06    | Appx_21                              | Appx_24                  |
| Appx_23  | COG (container)                   | TRAILHEAD        | experimental    | M07    | Appx_17, Appx_19                     | —                        |
| Appx_24  | Linda Function / Cosmic Rebirth   | CANONICAL        | interpretive    | M07    | Appx_14, Appx_22                     | —                        |
| Appx_25  | Selection Law                     | CANONICAL        | structural      | M07    | Appx_06                              | Appx_27                  |
| Appx_26  | Nomos Logica                      | CANONICAL        | interpretive    | M07    | Appx_03, Appx_04…Appx_06             | Appx_23 (optional)       |
| Appx_27  | Experiments / Discriminators      | CANONICAL        | experimental    | M08    | Appx_25                              | —                        |

---

## Section 6 — Edge list (machine)

Format:
- parent
- child
- relation: enables / depends_on
- contagion override (optional)

- GFUP → Appx_00 (enables)
- Appx_00 → Appx_01 (enables)
- Appx_01 → Appx_02 (enables)
- Appx_01 → Appx_03 (enables)
- Appx_02 → Appx_03 (enables)
- Appx_03 → Appx_04 (enables)
- Appx_03 → Appx_05 (enables)
- Appx_03 → Appx_06 (enables)

- Appx_06 → Appx_07 (enables)
- Appx_07 → AoC_00 (enables)
- AoC_00 → AoC_01 (enables)
- AoC_01 → AoC_02 (enables)
- AoC_02 → AoC_03 (enables)
- AoC_03 → AoC_04 (enables)
- AoC_03 → AoC_05 (enables)
- AoC_04 → AoC_06 (enables)
- AoC_05 → AoC_06 (enables)

- Appx_04 → Appx_08 (enables)
- Appx_05 → Appx_08 (enables)
- Appx_06 → Appx_08 (enables)
- Appx_08 → Appx_09 (enables)
- Appx_09 → Appx_10 (enables)
- Appx_10 → Appx_11 (enables)

- Appx_11 → Appx_15 (enables)
- Appx_11 → Appx_17 (enables)
- Appx_11 → Appx_12 (enables)
- Appx_12 → Appx_13 (enables)
- Appx_12 → Appx_14 (enables)
- Appx_15 → Appx_16 (enables)
- Appx_15 → Appx_20 (enables)
- Appx_17 → Appx_18 (enables)
- Appx_17 → Appx_19 (enables)
- Appx_18 → Appx_20 (enables)
- Appx_19 → Appx_20 (enables)
- Appx_20 → Appx_21 (enables)
- Appx_21 → Appx_22 (enables)
- Appx_22 → Appx_24 (enables)
- Appx_14 → Appx_24 (enables)

- Appx_06 → Appx_25 (enables)
- Appx_25 → Appx_27 (enables)

---

## Section 7 — Human-readable “routes”

### 7.1 Ontology spine
AA → AE → AS → ζ / ω / ξ

### 7.2 Scaffold path
Time → Space → Bounds → Gauge → Standard Model

### 7.3 Constants path
AoC_00 → π → c → α → m_p / m_n → G

### 7.4 Audit path
Selection Law → Experiments

---

## Section 8 — ChangeLog (map evolution)

- v1.1: Added quarantine-first policy (FALSIFIED vs FROZEN), explicit query protocol, and machine registry/edge list.
- v1.1 patch: Normalized Appx_11 `load_bearing` enum to `structural` (kept “Structural Filter” as title annotation).
---
## Dependency Links
**Depends on:**
- GFUP *(not in vault)*

**Enables:**
- ALL *(not in vault)*
