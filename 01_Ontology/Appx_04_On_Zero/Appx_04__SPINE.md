---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_04"
internal_id: "Appx_04_On_Zero_v1.1"
title: "Appx_04 — On Zero (ζ)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Operators"
role: "Constraint operator; lower boundary of coherent emergence"
load_bearing: "operator_core"

depends_on:
  - "Appx_01"   # AA
  - "Appx_02"   # AE
  - "Appx_03"   # AS

enables:
  - "Appx_07"   # AoC Preface (admissibility / Units Firewall)
  - "AoC_00"    # Collapse operator / selection
  - "Appx_10"   # Extension bounds
  - "Appx_11"   # Gauge structure (needs constraint framing)
  - "Appx_12"   # Force unification
  - "Appx_21"   # GR reduction (limit behavior)
  - "Appx_27"   # Experiments ledger

failure_topology:
  contagion: "downstream_total"
  class: "Operator Spine"
  kill_switch_ids:
    - "ZETA-UNSTABLE"          # If ζ cannot be defined as stable constraint
    - "ZETA-LEAKAGE"           # If constraints cannot prevent divergence / boundary failure
    - "ZETA-NONOPERATOR"       # If ζ reduces to mere symbol without operational role
    - "ZETA-NO-COHERENCE"      # If coherence does not require a lower bound

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query about constraints, bounds, zero, origins of measurement must consult Appx_04 after ontology gates."
    - "Treat ζ as an operator/constraint, not the empty set, not a coordinate, not absolute absence."
    - "If any ζ kill_switch triggers, freeze dependent nodes and route to Appx_27."

source:
  format: "pdf"
  filename: "Appx_04_On_Zero_v1.1.pdf"
---

# Appx_04 — On Zero (ζ) — SPINE

Structural metadata node for dependency-gated retrieval.

Content lives in:
`/content/content__Appx_04_On_Zero__CONTENT_v1.1.md`

---
## Dependency Links
**Depends on:**
- [[Appx_01__SPINE|Appx_01]]
- [[Appx_02__SPINE|Appx_02]]
- [[Appx_03__SPINE|Appx_03]]

**Enables:**
- Appx_07 *(not in vault)*
- [[AoC_Ledger__SPINE|AoC_00]]
- [[Appx_10__SPINE|Appx_10]]
- [[Appx_11__SPINE|Appx_11]]
- [[Appx_12__SPINE|Appx_12]]
- [[Appx_21__SPINE|Appx_21]]
- [[Appx_27__SPINE|Appx_27]]

**Content:** [[Appx_04__CONTENT|Appx_04 CONTENT]]
