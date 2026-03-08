---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_25"
internal_id: "Appx_25_On_Selection_Law_PF_v1.2"
title: "Appx_25 — The Selection Law (Geometric Natural Selection)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Selection / Survivorship"
role: "Constitutional Gate: defines what may be called a Survivor"
load_bearing: "constitutional"

epistemic_status: "FORTRESS_GATE"

depends_on:
  - "Appx_04"   # ζ (constraint)
  - "Appx_05"   # ω (extension)
  - "Appx_06"   # ξ (chance)
  - "Appx_19"   # singularity firewall discipline
  - "Appx_17"   # running ledger / invariants discipline

enables:
  - "AoC_*"     # constants ledger is governed by this selection law
  - "Appx_15"   # SM parameter ledger must tag by selection class
  - "Appx_27"   # discriminator packaging and freeze logic
  - "Appx_24"   # Linda selection link (deferred extension)
  - "Appx_23_COG_*"  # cognition survivorship link (deferred extension)

failure_topology:
  contagion: "total"
  class: "Constitutional Gate"
  kill_switch_ids:
    - "NONUNIQUE-SELECTION"            # multiple incompatible survivor sets fit equally well
    - "SURVIVOR-DRIFT"                 # invariants run under scale/conditioning
    - "ADHOC-PARAMETER-IMPORT"         # required free constants inserted to recover results
    - "RETROFIT-ONLY"                  # selection explains after-the-fact but predicts nothing
    - "CROSS-DOMAIN-INCONSISTENT"       # selection criteria change per domain without justification

rag_policy:
  gate_required: true
  retrieval_rules:
    - "No claim of 'derived constant' is valid unless Appx_25 gates it as [SURVIVOR] or [DERIVED-SURVIVOR]."
    - "Any parameter tagged [TUNED] or [CALIBRATED] must be treated as epistemic debt."
    - "If a discriminator fails, freeze dependent nodes in the spine (no downstream serving)."
    - "Selection criteria must be uniform: ζ-minimality, ω-consistency, ξ-stability."
  tagging:
    allowed_tags:
      - "[SURVIVOR]"
      - "[DERIVED-SURVIVOR]"
      - "[EFFECTIVE]"
      - "[CALIBRATED]"
      - "[TUNED]"
      - "[UNRESOLVED]"

extension_policy:
  default_scope: "AoC (physical constants)"
  deferred_extensions:
    - "COG survivorship (identity longevity) — deferred"
    - "Linda survival distribution mapping — deferred"
  rule:
    - "Extensions may reference Appx_25 but may not be governed by it until formalized in their own gates."

source:
  stub:
    format: "pdf"
    filename: "Appx_25_On_Selection_Law_STUB_v1.0.pdf"
  trailhead:
    format: "text"
    filename: "app _25_trailhead_notes_.txt"
---

# Appx_25 — The Selection Law — SPINE

This is the constitutional gate that prevents AoC from degrading into curve-fit lore.

---
## Dependency Links
**Depends on:**
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]
- [[Appx_19__SPINE|Appx_19]]
- [[Appx_17__SPINE|Appx_17]]

**Enables:**
- AoC_* *(not in vault)*
- [[Appx_15__SPINE|Appx_15]]
- [[Appx_27__SPINE|Appx_27]]
- [[Appx_24__SPINE|Appx_24]]
- Appx_23_COG_* *(not in vault)*

**Content:** [[Appx_25__CONTENT|Appx_25 CONTENT]]
