---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_05"
internal_id: "AoC_05_Neutron_Mass_v1.3"
title: "AoC_05 — Neutron Mass (mₙ)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "Metastable baryonic excitation; weak-penalty mass gap enforcer"
load_bearing: "atlas_loadbearing"

depends_on:
  - "AoC_00"
  - "AoC_01"
  - "AoC_02"
  - "AoC_03"
  - "AoC_04"
  - "Appx_04"
  - "Appx_05"
  - "Appx_06"

enables:
  - "Appx_12"
  - "Appx_13"
  - "Appx_17"
  - "Appx_27"

failure_topology:
  contagion: "mass_sector"
  class: "Atlas Constant"
  kill_switch_ids:
    - "MN-NOT-GREATER-MP"
    - "MN-NO-WEAK-PENALTY"
    - "MN-DUAL-BARE-SCALE"
    - "MN-BINDING-ADHOC"
    - "MN-BETA-MISMATCH"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Gate through AoC_04 (proton baseline)."
    - "Neutron treated as metastable modification, not independent ground state."
    - "If δW derivation fails, freeze weak-sector claims."

source:
  format: "pdf"
  filename: "Appx_7_AoC_05_Neutron_Mass_v1.3.pdf"
---

# AoC_05 — Neutron Mass (mₙ) — SPINE

Structural metadata node for dependency-gated retrieval.

Content lives in:
`/content/content__AoC_05_Neutron_Mass__CONTENT_v1.3.md`

---
## Dependency Links
**Depends on:**
- [[AoC_Ledger__SPINE|AoC_00]]
- [[AoC_01__SPINE|AoC_01]]
- [[AoC_02__SPINE|AoC_02]]
- [[AoC_03__SPINE|AoC_03]]
- [[AoC_04__SPINE|AoC_04]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]

**Enables:**
- [[Appx_12__SPINE|Appx_12]]
- [[Appx_13__SPINE|Appx_13]]
- [[Appx_17__SPINE|Appx_17]]
- [[Appx_27__SPINE|Appx_27]]

**Content:** [[AoC_05__CONTENT|AoC_05 CONTENT]]
