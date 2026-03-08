---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "7dU_GFUP"
internal_id: "7dU_GFUP_v1.2"
title: "GFUP — Geometric Foundations for Unified Physics (v1.2)"
status: "SPINE"
date_minted: "2026-03-01"
layer: "spine"
domain: "Foundation Paper"
role: "Root foundation: declares 7dU regulators, metric extension, and top-level claims"
epistemic_status: "CANONICAL"
load_bearing: "structural"
contagion: "downstream_total"

depends_on: []

enables:
  - "7dU_GNS_Prooffield_Index"
  - "Appx_00"
  - "Appx_01"
  - "Appx_02"
  - "Appx_03"
  - "Appx_04"
  - "Appx_05"
  - "Appx_06"
  - "Appx_08"
  - "Appx_09"
  - "Appx_10"
  - "Appx_11"
  - "Appx_12"
  - "Appx_14"
  - "Appx_15"
  - "Appx_17"
  - "Appx_18"
  - "Appx_20"
  - "Appx_21"
  - "Appx_27"
  - "AoC_00"

failure_topology:
  class: "Root Foundation Node"
  kill_switch_ids:
    - "REGULATORS-NONIRREDUCIBLE"         # ζ/ω/ξ not required or not independent
    - "METRIC-NOT-EXTENDED"               # 7D extension collapses to re-labeled 4D
    - "UNITS-FIREWALL-BROKEN"             # unit-bearing constants required as survivors
    - "GR-NOT-RECOVERED"                  # GR limit/reduction fails in declared domain
    - "QFT-NOT-RECOVERED"                 # QFT limit/reduction fails in declared domain
    - "FALSIFICATION-NONCONTAGIOUS"       # downstream nodes remain valid after root failure
    - "PREDICTION-NONUNIQUE"              # outputs require arbitrary tuning / free functions

rag_policy:
  gate_required: true
  retrieval_rules:
    - "GFUP is the root: read SPINE metadata before any downstream semantic retrieval."
    - "If any GFUP kill-switch triggers, all dependent nodes are FROZEN unless independently re-founded."
    - "Downstream nodes may not override GFUP axioms; conflicts must be flagged as incompatibilities."
    - "GFUP does not serve as a substitute for appendices; it routes to them."

source:
  format: "markdown"
  filename: "7dU_GFUP_v1.2.md"
---

# GFUP — Geometric Foundations for Unified Physics (v1.2) — SPINE

GFUP is the **root declaration** of the 7dU framework:
- sets boundary conditions (AA/AE),
- defines irreducible regulators (ζ/ω/ξ),
- declares the 7D extension and the Units Firewall discipline,
- states top-level recovery claims (GR/QFT limits),
- routes all technical proof to appendices.

If GFUP fails, the corpus is quarantined downstream by default (FROZEN), pending re-foundation.
---
## Dependency Links

**Enables:**
- 7dU_GNS_Prooffield_Index *(not in vault)*
- [[Appx_00__SPINE|Appx_00]]
- [[Appx_01__SPINE|Appx_01]]
- [[Appx_02__SPINE|Appx_02]]
- [[Appx_03__SPINE|Appx_03]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]
- [[Appx_08__SPINE|Appx_08]]
- [[Appx_09__SPINE|Appx_09]]
- [[Appx_10__SPINE|Appx_10]]
- [[Appx_11__SPINE|Appx_11]]
- [[Appx_12__SPINE|Appx_12]]
- [[Appx_14__SPINE|Appx_14]]
- [[Appx_15__SPINE|Appx_15]]
- [[Appx_17__SPINE|Appx_17]]
- [[Appx_18__SPINE|Appx_18]]
- [[Appx_20__SPINE|Appx_20]]
- [[Appx_21__SPINE|Appx_21]]
- [[Appx_27__SPINE|Appx_27]]
- [[AoC_Ledger__SPINE|AoC_00]]

**Content:** [[7dU_GFUP__CONTENT|7dU_GFUP CONTENT]]
