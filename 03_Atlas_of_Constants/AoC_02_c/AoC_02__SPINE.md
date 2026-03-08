---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_02"
internal_id: "AoC_02_On_c_v1.2"
title: "AoC_02 — On c"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "Invariant propagation constant; geometric speed bound"
load_bearing: "atlas_loadbearing"

depends_on:
  - "AoC_00"   # Collapse Operator (Ω̂)
  - "AoC_01"   # π (first eigenvalue precedent)
  - "Appx_04"  # ζ
  - "Appx_05"  # ω
  - "Appx_06"  # ξ

enables:
  - "AoC_03"   # α
  - "AoC_04"   # m_p
  - "Appx_17"  # Renormalization/EFT
  - "Appx_21"  # GR reduction (light-cone structure)
  - "Appx_27"  # Experiments ledger (propagation tests)

failure_topology:
  contagion: "atlas_total"
  class: "Atlas Constant"
  kill_switch_ids:
    - "C-NONINVARIANT"         # c varies without controlled mechanism
    - "C-DIMENSION-IMPORT"     # c inserted via unit convention rather than emergence
    - "C-NO-LIMIT"             # no universal propagation bound derivable
    - "C-INCONSISTENT"         # contradiction with π/Ω̂ protocol or GR/QFT interface

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query invoking c as emergent invariant must consult AoC_02 after AoC_00/AoC_01 gating."
    - "Do not treat c as assumed postulate; treat as survivor under Ω̂ protocol."
    - "If any c kill_switch triggers, freeze downstream AoC nodes and route to Appx_27."

source:
  format: "pdf"
  filename: "Appx_7_AoC_02_On_c_1.2.pdf"
---

# AoC_02 — On c — SPINE

Structural metadata node for dependency-gated retrieval.

Content lives in:
`/content/content__AoC_02_On_c__CONTENT_v1.2.md`

---
## Dependency Links
**Depends on:**
- [[AoC_Ledger__SPINE|AoC_00]]
- [[AoC_01__SPINE|AoC_01]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]

**Enables:**
- [[AoC_03__SPINE|AoC_03]]
- [[AoC_04__SPINE|AoC_04]]
- [[Appx_17__SPINE|Appx_17]]
- [[Appx_21__SPINE|Appx_21]]
- [[Appx_27__SPINE|Appx_27]]

**Content:** [[AoC_02__CONTENT|AoC_02 CONTENT]]
