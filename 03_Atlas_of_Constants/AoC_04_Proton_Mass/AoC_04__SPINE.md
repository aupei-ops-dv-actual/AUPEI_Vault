---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_04"
internal_id: "AoC_04_Proton_Mass_v1.3"
title: "AoC_04 — Proton Mass (mₚ)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "Matter anchor: confinement-scale survivor under Ω̂; baryonic stability interface"
load_bearing: "atlas_loadbearing"

depends_on:
  - "AoC_00"   # Collapse Operator (Ω̂)
  - "AoC_01"   # π
  - "AoC_02"   # c
  - "AoC_03"   # α
  - "Appx_04"  # ζ
  - "Appx_05"  # ω
  - "Appx_06"  # ξ

enables:
  - "Appx_17"  # Renormalization/EFT (mass dressing / running discipline)
  - "Appx_18"  # HoQG (geometry–matter coupling)
  - "Appx_21"  # GR reduction (mass/curvature interface)
  - "Appx_27"  # Experiments ledger (mass-sector falsifiers + replications)
  - "AoC_05"   # (reserved) downstream matter constants if any

failure_topology:
  contagion: "mass_sector"
  class: "Atlas Constant"
  kill_switch_ids:
    - "MP-NONPREDICTIVE"        # cannot produce a stable, falsifiable prediction for m_p
    - "MP-DIMENSION-IMPORT"     # mass inserted via hidden unit choice / dimensional tuning
    - "MP-NO-GAP"               # required spectral gap (Δπ or equivalent) does not exist
    - "MP-BINDING-NUMEROLOGY"   # binding/dressing factor has no derivation path / becomes ad hoc
    - "MP-EXPERIMENT-MISMATCH"  # deviation beyond tolerance / replication fails

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query about m_p as emergent constant must consult AoC_04 after AoC_00→01→02→03 gating."
    - "Treat m_p as confinement survivor with explicit dressing terms; do not collapse it into pure numerology."
    - "If any m_p kill_switch triggers, freeze mass-sector claims and route to Appx_27."

source:
  format: "pdf"
  filename: "Appx_7_AoC_04_Proton_Mass_1.3.pdf"
---

# AoC_04 — Proton Mass (mₚ) — SPINE

Structural metadata node for dependency-gated retrieval.

Content lives in:
`/content/content__AoC_04_Proton_Mass__CONTENT_v1.3.md`

---
## Dependency Links
**Depends on:**
- [[AoC_Ledger__SPINE|AoC_00]]
- [[AoC_01__SPINE|AoC_01]]
- [[AoC_02__SPINE|AoC_02]]
- [[AoC_03__SPINE|AoC_03]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]

**Enables:**
- [[Appx_17__SPINE|Appx_17]]
- [[Appx_18__SPINE|Appx_18]]
- [[Appx_21__SPINE|Appx_21]]
- [[Appx_27__SPINE|Appx_27]]
- [[AoC_05__SPINE|AoC_05]]

**Content:** [[AoC_04__CONTENT|AoC_04 CONTENT]]
