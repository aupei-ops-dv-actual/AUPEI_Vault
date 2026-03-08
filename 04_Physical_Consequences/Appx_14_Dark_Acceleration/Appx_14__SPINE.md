---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_14"
internal_id: "Appx_14_On_Dark_Acceleration_PF_v1.0"
title: "Appx_14 — Dark Geometry & Cosmic Acceleration"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Cosmic-Scale Geometry"
role: "Dynamic curvature replacement for Λ in expansion law"
load_bearing: "observational_anchor"

epistemic_status: "ANSATZ_TESTABLE"

depends_on:
  - "Appx_04"   # ζ
  - "Appx_05"   # ω
  - "Appx_06"   # ξ
  - "Appx_10"   # Extension Bounds
  - "Appx_12"   # Volumetric scaling shelves
  - "Appx_13"   # Neutrino probe channel

enables:
  - "Appx_27a"  # Axis coherence discriminator
  - "Appx_27b"  # Lensing cross-check
  - "Atlas_Global_Validation"

failure_topology:
  contagion: "cosmic_scale"
  class: "Observational Anchor Node"
  kill_switch_ids:
    - "NO-HIGHZ-DEVIATION"
    - "LAMBDA-FITS-BETTER"
    - "LENSING-MISMATCH"
    - "TIME-DELAY-INCONSISTENT"
    - "UNITS-FIREWALL-VIOLATION"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "No cosmological constant Λ insertion allowed."
    - "Dynamic curvature term f(ω, ζ) must be explicit or tightly bounded."
    - "All fits must separate monopole acceleration from axis/aniso claims."
    - "If ΛCDM outperforms in high-z regime, freeze dark-geometry claim."

source:
  format: "pdf"
  filename: "Appx_14_Dark_Acceleration_v1.0.pdf"
---

# Appx_14 — Dark Geometry & Cosmic Acceleration — SPINE

Defines cosmic acceleration as collapse-driven geometric instability, not vacuum energy.

---
## Dependency Links
**Depends on:**
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]
- [[Appx_10__SPINE|Appx_10]]
- [[Appx_12__SPINE|Appx_12]]
- [[Appx_13__SPINE|Appx_13]]

**Enables:**
- [[Appx_27a__SPINE|Appx_27a]]
- Appx_27b *(not in vault)*
- Atlas_Global_Validation *(not in vault)*

**Content:** [[Appx_14__CONTENT|Appx_14 CONTENT]]
