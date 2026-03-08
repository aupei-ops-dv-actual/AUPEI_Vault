---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_00"
internal_id: "AoC_00_Constants_Ledger_v1.0"
title: "AoC_00 — Constants Ledger (Master Index)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas of Constants"
role: "Master ledger for constants: IDs, dependencies, status, falsifier hooks"
load_bearing: "structural"

depends_on:
  - "Appx_00"   # Collapse Map / gating topology
  - "Appx_01"   # AA
  - "Appx_02"   # AE
  - "Appx_04"   # ζ (Bounds)
  - "Appx_05"   # ω (Persistence)
  - "Appx_06"   # ξ (Chance)

enables:
  - "AoC_01"    # π (and support packets)
  - "AoC_02"    # c (speed of light)  [may be pending content conversion]
  - "AoC_03"    # α ≈ 1/137
  - "AoC_04"    # Proton mass
  - "AoC_05"    # Neutron mass
  - "AoC_06"    # Gravity (trailhead / G)

failure_topology:
  contagion: "aoc_global"
  class: "Ledger Spine"
  kill_switch_ids:
    - CONSTANT-ID-DRIFT       # aliases diverge; retrieval becomes inconsistent
    - DEPENDENCY-BYPASS       # constants served without prerequisite gates
    - UNLOGGED-REVISION       # updates not reflected here → stale GraphRAG routing

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query about a constant MUST consult AoC_00 first for canonical ID + status + dependencies."
    - "If constant status is TRAILHEAD or DISPUTED, response must include uncertainty and point to falsifier hooks."
    - "If multiple AoC nodes share dependencies (e.g., Selection Law), enforce those gates before answering."
    - "Alias resolution is authoritative here. If alias not listed, treat as unknown until added."

ledger_protocol:
  required_fields:
    - "constant_id"
    - "symbol"
    - "aliases"
    - "status"
    - "primary_node"
    - "depends_on"
    - "falsifier_hooks"
    - "notes"
  allowed_statuses: ["TRAILHEAD", "SUPPORT", "CANONICAL", "DERIVED", "PREDICTED", "DISPUTED", "DEPRECATED"]

source:
  format: "ledger"
  reference: "AoC container"
---

# AoC_00 — Constants Ledger (SPINE)

AoC_00 is the master gating node for all constant queries.

Purpose:
- Resolve canonical IDs and aliases.
- Enforce dependency-gated retrieval.
- Bind each constant to its falsifier hooks (Appx_27 lanes, where applicable).

---
## Dependency Links
**Depends on:**
- [[Appx_00__SPINE|Appx_00]]
- [[Appx_01__SPINE|Appx_01]]
- [[Appx_02__SPINE|Appx_02]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]

**Enables:**
- [[AoC_01__SPINE|AoC_01]]
- [[AoC_02__SPINE|AoC_02]]
- [[AoC_03__SPINE|AoC_03]]
- [[AoC_04__SPINE|AoC_04]]
- [[AoC_05__SPINE|AoC_05]]
- [[AoC_06__SPINE|AoC_06]]

**Content:** [[AoC_Ledger__CONTENT|AoC_00 CONTENT]]
