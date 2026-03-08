---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_17"
internal_id: "Appx_17_On_EFT_RG_PF_v1.2"
title: "Appx_17 — Renormalization as Survivability Bookkeeping"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Scale Architecture"
role: "Running Ledger Gate — Scale Dependence Discriminator"
load_bearing: "scale_integrity"

epistemic_status: "TRAILHEAD_STRONG"

depends_on:
  - "Appx_10"   # Extension Bounds
  - "Appx_11"   # Gauge admissibility
  - "Appx_12"   # Volumetric scaling (ξ^{-3n})
  - "Appx_15"   # SM Ledger
  - "AoC_03"    # α invariant discipline

enables:
  - "Appx_18"   # HoQG interface
  - "Appx_27"   # Discriminator packaging
  - "Atlas_Global_Validation"

failure_topology:
  contagion: "scale_total"
  class: "Running Integrity Gate"
  kill_switch_ids:
    - "SURVIVOR-DRIFT"
    - "PURE-RESTATEMENT-OF-RG"
    - "NO-PREDICTIVE-FLOW-CONSTRAINT"
    - "UNITS-FIREWALL-BREACH"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "True survivors (π, c, Δπ, base α_geom) must not run."
    - "Only effective couplings and operator coefficients may drift."
    - "RG flow must be derivable from volumetric constraint, not post-hoc fit."
    - "EFT cutoff must map to explicit Extension Bound window."
---

# Appx_17 — Renormalization as Survivability Bookkeeping — SPINE

Defines scale dependence as geometric constraint management.

---
## Dependency Links
**Depends on:**
- [[Appx_10__SPINE|Appx_10]]
- [[Appx_11__SPINE|Appx_11]]
- [[Appx_12__SPINE|Appx_12]]
- [[Appx_15__SPINE|Appx_15]]
- [[AoC_03__SPINE|AoC_03]]

**Enables:**
- [[Appx_18__SPINE|Appx_18]]
- [[Appx_27__SPINE|Appx_27]]
- Atlas_Global_Validation *(not in vault)*

**Content:** [[Appx_17__CONTENT|Appx_17 CONTENT]]
