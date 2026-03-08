---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_01"
internal_id: "AoC_01_On_Pi_v1.3"
title: "AoC_01 — On π"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "First fixed point of collapse; geometric eigenvalue gate"
load_bearing: "atlas_loadbearing"

depends_on:
  - "AoC_00"   # Collapse Operator (Ω̂)
  - "Appx_04"  # ζ
  - "Appx_05"  # ω
  - "Appx_06"  # ξ

enables:
  - "AoC_02"   # c (expected to inherit stability protocol)
  - "AoC_03"   # α
  - "AoC_04"   # m_p
  - "Appx_17"  # Renormalization/EFT (eigenvalue running discipline)
  - "Appx_27"  # Experiments ledger (replication + falsifiers)
  - "Appx_27a" # Experimental path containers (when π tests branch)

failure_topology:
  contagion: "atlas_total"
  class: "Atlas Constant"
  kill_switch_ids:
    - "PI-NONCONVERGENCE"        # grid refinement diverges away from π
    - "PI-CIRCULAR-KAHLER"       # Kähler calibration shown to assume π
    - "PI-DOMAIN-IMPORT"         # π imported via boundary/coordinate choice
    - "PI-NORMALIZATION-FAIL"    # s_geom fails to remove geometric scale
    - "PI-REPLICATION-FAIL"      # independent replication fails pass criteria

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query that relies on π as an emergent constant must consult AoC_01 after AoC_00 gating."
    - "Do not treat π as assumed circle-ratio; treat it as eigenvalue of Ω̂ with explicit protocol evidence."
    - "If any π kill_switch triggers, freeze AoC downstream constants and route to Appx_27 / support derivations."

source:
  format: "pdf"
  filename: "Appx_7_AoC_01_On_Pi_v1.3.pdf"
---

# AoC_01 — On π — SPINE

Structural metadata node for dependency-gated retrieval.

Content lives in:
`/content/content__AoC_01_On_Pi__CONTENT_v1.3.md`

---
## Dependency Links
**Depends on:**
- [[AoC_Ledger__SPINE|AoC_00]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]

**Enables:**
- [[AoC_02__SPINE|AoC_02]]
- [[AoC_03__SPINE|AoC_03]]
- [[AoC_04__SPINE|AoC_04]]
- [[Appx_17__SPINE|Appx_17]]
- [[Appx_27__SPINE|Appx_27]]
- [[Appx_27a__SPINE|Appx_27a]]

**Content:** [[AoC_01__CONTENT|AoC_01 CONTENT]]
