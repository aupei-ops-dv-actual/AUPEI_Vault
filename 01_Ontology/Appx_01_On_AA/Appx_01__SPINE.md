---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_01"
internal_id: "Appx_01_On_AA_v1.2c"
title: "Appx_01 — On Absolute Absence (AA)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Ontology"
role: "Root gate: uninstantiable no-structure condition"
load_bearing: "root"

depends_on: []
enables:
  - "Appx_02"   # AE
  - "Appx_03"   # AS
  - "Appx_04"   # ζ
  - "Appx_05"   # ω
  - "Appx_06"   # ξ
  - "Appx_00"   # Collapse Map (as topology reference)
  - "Appx_27"   # Experiments ledger (kill switch host)

failure_topology:
  contagion: "downstream_total"
  class: "Root Spine"
  kill_switch_ids:
    - "AA-NO-MODEL"           # Falsifier A: Model of AA under describability
    - "AA-SFR-FAILURE"        # Falsifier B: SFR mechanism invalid
    - "AA-CATEGORY-ERROR"     # Falsifier C: AA treated as object/state/empty set/zero

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query that touches origin/initialization/emptiness/zero/void must pass Appx_01 gate."
    - "If AA kill_switch is triggered, freeze all enabled nodes in responses."

source:
  format: "pdf"
  filename: "Appx_01_On_AA_v1.1c.pdf"
---

# Appx_01 — On Absolute Absence (AA) — SPINE

This is the **structural metadata node** for GraphRAG gating.

- Content lives in: `/content/Appx_01_On_AA__CONTENT_v1.2c.md`
- This spine node exists to enforce **dependency-gated retrieval** and **contagious falsification**.

---
## Dependency Links

**Enables:**
- [[Appx_02__SPINE|Appx_02]]
- [[Appx_03__SPINE|Appx_03]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]
- [[Appx_00__SPINE|Appx_00]]
- [[Appx_27__SPINE|Appx_27]]

**Content:** [[Appx_01__CONTENT|Appx_01 CONTENT]]
