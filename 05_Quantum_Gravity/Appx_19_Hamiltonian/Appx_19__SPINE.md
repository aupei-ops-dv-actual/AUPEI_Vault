---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_19"
internal_id: "Appx_19_Hamiltonian_Lagrangian_PF_v1.1"
title: "Appx_19 — Hamiltonian–Lagrangian Formalism (Constraint Before Motion)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Force Geometry Engine"
role: "Dynamic Curvature Kernel — Singular-Resistance Gate"
load_bearing: "engine_block"

epistemic_status: "DERIVATION_CORE"

depends_on:
  - "Appx_04"   # ζ (collapse regulator)
  - "Appx_05"   # ω (emergence regulator)
  - "Appx_06"   # ξ (stochastic regulator)
  - "Appx_18"   # HoQG narrative bridge
  - "Appx_17"   # Running ledger discipline

enables:
  - "Simulation_MVPs"
  - "Appx_27"   # Experimental discriminator packaging
  - "Atlas_Global_Validation"

failure_topology:
  contagion: "engine_total"
  class: "Dynamic Consistency Gate"
  kill_switch_ids:
    - "SINGULARITY-NOT-RESISTED"
    - "SURVIVOR-DRIFT"
    - "WDW-INCONSISTENT"
    - "STOCHASTIC-NON-HERMICITY-UNCONTROLLED"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Momentum denominators (ζ², ω², ξ²(t)) enforce geometric resistance."
    - "c remains invariant survivor."
    - "ξ stochasticity must not violate Units Firewall."
    - "Classical GR recovery must remain exact in regulator-collapse limit."
---

# Appx_19 — Hamiltonian–Lagrangian Formalism — SPINE

Defines the dynamic kernel of 7dU: constraint governs motion, not force insertion.

---
## Dependency Links
**Depends on:**
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]
- [[Appx_18__SPINE|Appx_18]]
- [[Appx_17__SPINE|Appx_17]]

**Enables:**
- Simulation_MVPs *(not in vault)*
- [[Appx_27__SPINE|Appx_27]]
- Atlas_Global_Validation *(not in vault)*

**Content:** [[Appx_19__CONTENT|Appx_19 CONTENT]]
