---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_13"
internal_id: "Appx_13_On_Neutrinos_PF_v1.1"
title: "Appx_13 — Neutrinos (Curvature Messengers)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Geometric Probes"
role: "Curvature-dependent oscillation and mass emergence channel"
load_bearing: "probe_channel"

epistemic_status: "TRAILHEAD_UPGRADE"

depends_on:
  - "AoC_05"   # Neutron mass & beta decay channel
  - "Appx_12"  # Force hierarchy shelves
  - "Appx_09"  # 3D scaffold
  - "Appx_10"  # Extension Bounds
  - "Appx_04"  # ζ
  - "Appx_05"  # ω
  - "Appx_06"  # ξ

enables:
  - "Appx_14"  # Dark Acceleration / cosmic structure
  - "Appx_27"  # Discriminator packaging
  - "Appx_17"  # EFT/renormalization consistency

failure_topology:
  contagion: "probe_channel"
  class: "Structural Probe Node"
  kill_switch_ids:
    - "NO-CURVATURE-DEPENDENCE"
    - "MSW-NOT-ISOLATED"
    - "INVARIANT-MASS-SPECTRUM"
    - "DARK-SECTOR-MISMATCH"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Separate curvature-dependence from MSW matter effects explicitly."
    - "Neutrino mass must remain dimensionless-survivor derived until calibrated."
    - "If oscillation probabilities show zero gravitational dependence, freeze curvature-messenger claim."
    - "No dark-matter replacement claims without rotation-curve modeling."

source:
  original:
    format: "pdf"
    filename: "Appx_13_On_Neutrinos_v1.0.pdf"
  rewrite:
    format: "text"
    filename: "Appx_13_rewrite_trailhead.txt"
---

# Appx_13 — Neutrinos — SPINE

Defines neutrinos as curvature-dependent geometric messengers.

---
## Dependency Links
**Depends on:**
- [[AoC_05__SPINE|AoC_05]]
- [[Appx_12__SPINE|Appx_12]]
- [[Appx_09__SPINE|Appx_09]]
- [[Appx_10__SPINE|Appx_10]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]

**Enables:**
- [[Appx_14__SPINE|Appx_14]]
- [[Appx_27__SPINE|Appx_27]]
- [[Appx_17__SPINE|Appx_17]]

**Content:** [[Appx_13__CONTENT|Appx_13 CONTENT]]
