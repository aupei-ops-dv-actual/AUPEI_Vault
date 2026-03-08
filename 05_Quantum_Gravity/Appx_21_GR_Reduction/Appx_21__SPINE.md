---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_21"
internal_id: "Appx_21_GR_Reduction_PF_v1.2"
title: "Appx_21 — Dimensional Reduction to General Relativity"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Classical Limit"
role: "Compatibility Gate — GR Containment Proof"
load_bearing: "classical_recovery"

epistemic_status: "PROOF_CORE"

depends_on:
  - "Appx_18"   # HoQG bridge
  - "Appx_19"   # Hamiltonian kernel
  - "Appx_20"   # Entropy quantization
  - "Appx_04"   # ζ regulator discipline
  - "Appx_05"   # ω regulator discipline
  - "Appx_06"   # ξ regulator discipline

enables:
  - "Appx_14"   # Dark acceleration interpretation
  - "Experimental_GW_Discriminators"
  - "Atlas_Global_Validation"

failure_topology:
  contagion: "classical_total"
  class: "Compatibility Gate"
  kill_switch_ids:
    - "NO-CLEAN-TENSOR-REDUCTION"
    - "SURVIVOR-DRIFT"
    - "GR-LIMIT-INEXACT"
    - "SINGULARITY-FIREWALL-VIOLATION"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Reduction must act on curvature contributions, not field annihilation."
    - "Extended regulators must become flat (zero gradients), not zero-valued."
    - "Einstein tensor convergence must be exact."
    - "Stress-energy projection must reduce cleanly."
---

# Appx_21 — Dimensional Reduction to GR — SPINE

Defines the classical compatibility proof of 7dU.

---
## Dependency Links
**Depends on:**
- [[Appx_18__SPINE|Appx_18]]
- [[Appx_19__SPINE|Appx_19]]
- [[Appx_20__SPINE|Appx_20]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]

**Enables:**
- [[Appx_14__SPINE|Appx_14]]
- Experimental_GW_Discriminators *(not in vault)*
- Atlas_Global_Validation *(not in vault)*

**Content:** [[Appx_21__CONTENT|Appx_21 CONTENT]]
