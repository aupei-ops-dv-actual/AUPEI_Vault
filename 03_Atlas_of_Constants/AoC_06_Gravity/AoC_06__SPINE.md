---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_06"
internal_id: AoC_06_On_G_v1.2
title: "AoC_06 — On G (Gravity as Coherence-Dilution Residual)"
status: "SPINE"
date_minted: "2026-03-01"
layer: "spine"
domain: "Atlas of Constants"
role: "Derivation of Newtonian gravity via ζ/ω interface and 7D reduction"

epistemic_status: "TRAILHEAD_UPGRADE"

load_bearing: "structural"
contagion: "downstream_total"

depends_on:
  - Appx_18X_Int_Meas_&_Norm_Close  # λ finiteness + κ7 provenance closure
  - "AoC_04"        # ζ-knot confinement & µ0 normalization
  - "Appx_09"       # Δ3 spatial scaffold
  - "Appx_18"       # 7D Einstein–Hilbert sector
  - "Appx_21"       # GR reduction channel
  - "Appx_04"       # ζ regulator definition
  - "Appx_05"       # ω regulator definition

enables:
  - "Appx_21"       # GR reduction confirmation
  - "Hierarchy_Chain"
  - "Mass_Gap_Program"

failure_topology:
  class: "Structural Constant Node"
  kill_switch_ids:
    - "NONUNIQUE-STRAIN-FUNCTIONAL"
    - "FREE-NORMALIZATION-CONSTANT"
    - "INTERFACE-CONSISTENCY-FAILURE"
    - "PLANCK-INSERTION"
    - "UNITS-FIREWALL-VIOLATION"
    - "DIVERGENT-LAMBDA"
    - "POSTHOC-KAPPA7-FIT"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "1/r^2 tail must arise from variational derivation."
    - "Exterior Laplacian must be Euler–Lagrange result."
    - "No free multiplicative constant in α^G."
    - "Units Firewall must use µ0 only."
    - "λ must be finite and regulator-consistent."
    - "κ7 must be upstream fixed, not tuned."

stability_rule:
  - "If Laplacian assumed rather than derived, node falsified."
  - "If α^G depends on arbitrary normalization, node falsified."
  - "If Units Firewall requires Planck mass, node falsified."
  - "If λ diverges, hierarchy collapses."
  - "If κ7 tuned post hoc, predictive status lost."

---

# AoC_06 — On G (Gravity as Coherence-Dilution Residual) — SPINE

Derives Newtonian gravity as the unique exterior response of an ω-bounded vacuum to a localized ζ-confined knot on Δ3.

Gravity is not imported.
It is the ω-restoring curvature tail of bounded ζ curvature.

Promotable to CANONICAL only after:
- κ7 fixed upstream,
- λ proven finite under regulator geometry,
- µ0 normalization chain closed,
- Γ_bind epistemic status resolved.
- Appx_21 consistency lock (KK vs curvature-collapse channel) verified.

---
## Dependency Links
**Depends on:**
- Appx_18X_Int_Meas_&_Norm_Close *(not in vault)*
- [[AoC_04__SPINE|AoC_04]]
- [[Appx_09__SPINE|Appx_09]]
- [[Appx_18__SPINE|Appx_18]]
- [[Appx_21__SPINE|Appx_21]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]

**Enables:**
- [[Appx_21__SPINE|Appx_21]]
- Hierarchy_Chain *(not in vault)*
- Mass_Gap_Program *(not in vault)*

**Content:** [[content__AoC_06_On_Gravity__CONTENT_v0.2_TRAILHEAD|AoC_06 CONTENT]]
