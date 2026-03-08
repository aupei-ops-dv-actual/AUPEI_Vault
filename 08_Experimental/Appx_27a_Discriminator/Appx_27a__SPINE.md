---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_27a"
internal_id: "Appx_27a_Gravity_Threshold_v1.0"
title: "Appx_27a — Gravity Threshold Discriminator"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Gravitational Transition / Experimental Lane"
role: "Mass-dependent gravity discriminator"
load_bearing: "experimental_lane"

depends_on:
  - "Appx_27"   # Experimental Ledger
  - "Appx_04"   # ζ (Constraint)
  - "Appx_05"   # ω (Extension)
  - "Appx_06"   # ξ (Chance)
  - "Appx_14"   # Dark Acceleration (macro implications)
  - "Appx_13"   # Neutrinos (optional mass-regime link)

enables:
  - "LowMass_G_Tests"
  - "Galaxy_Rotation_Modeling"
  - "Weak_Lensing_Deviation_Tests"
  - "Compact_Object_Census"

failure_topology:
  contagion: "sector_B_macro"
  class: "Experimental Lane"
  kill_switch_ids:
    - "NO_LOW_MASS_G_DEVIATION"
    - "PARTICULATE_DM_REQUIRED"
    - "STABLE_OBJECT_AT_THRESHOLD"
    - "NO_TRANSITION_SIGNATURE"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "All gravitational anomaly claims must reference M* explicitly."
    - "Effective coupling must be treated as mass-dependent only within this lane."
    - "Do not generalize beyond exponential discriminator without test evidence."
    - "Log status: PROPOSED / ACTIVE / FALSIFIED / PROMOTED / INCONCLUSIVE."

lane_metadata:
  discriminator_parameter: "M*"
  governing_law: "Geff(M) = G exp(-M/M*)"
  classical_limit: "M >> M*"
  probabilistic_regime: "M << M*"
  regulators_in_play: ["ζ", "ω", "ξ"]

source:
  format: "canonical_artifact"
  reference: "Appx_27a_Gravity_Threshold_Discriminator_v1.0.pdf"
---

# Appx_27a — Gravity Threshold Discriminator (SPINE)

This lane tests the hypothesis that gravity transitions from classical to probabilistic behavior at a critical mass scale M*.

Above M*:
  Geff → G (classical regime)

Below M*:
  Geff = G exp(-M/M*)

This lane exists to differentiate:

• Structural threshold transition
vs
• Particulate dark matter explanation

Collapse consequence:
If no threshold exists, gravity remains classical at all scales.
---
## Dependency Links
**Depends on:**
- [[Appx_27__SPINE|Appx_27]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]
- [[Appx_14__SPINE|Appx_14]]
- [[Appx_13__SPINE|Appx_13]]

**Enables:**
- LowMass_G_Tests *(not in vault)*
- Galaxy_Rotation_Modeling *(not in vault)*
- Weak_Lensing_Deviation_Tests *(not in vault)*
- Compact_Object_Census *(not in vault)*

**Content:** [[Appx_27a__CONTENT|Appx_27a CONTENT]]
