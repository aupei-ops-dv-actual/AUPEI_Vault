---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "Appx_27"
internal_id: "Appx_27_Proposed_Experiments_v1.0"
title: "Appx_27 — Proposed Experiments / Experimental Ledger"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Experimental Falsification"
role: "Bounty board / living falsification ledger across ξ, ζ, ω"
load_bearing: "operational"

depends_on:
  - "Appx_00"   # Collapse Map (spine gating)
  - "Appx_01"   # AA
  - "Appx_02"   # AE
  - "Appx_04"   # ζ
  - "Appx_05"   # ω
  - "Appx_06"   # ξ
  - "Appx_12"   # Force unification (feeds test targets)
  - "Appx_14"   # Dark Acceleration (macro tests)
  - "Appx_22"   # Black Holes (macro tests)

enables:
  - "Appx_27a"  # Experiment lane: Gravity Threshold / Discriminator
  - "Appx_27b"  # Future experiment lane (reserved)
  - "Appx_27c"  # Future experiment lane (reserved)
  - "NL_01"     # NL Lab (shared falsification pattern)
  - "COG_00"    # CCT / cognitive stress tests (Sector C)

failure_topology:
  contagion: "framework_integrity"
  class: "Operational Spine"
  kill_switch_ids:
    - "LEDGER_FROZEN"          # no active falsification stream → framework drifts to myth
    - "NO_DIFFERENTIATOR_TEST" # experiments cannot distinguish structure from story
    - "RESULTS_UNLOGGED"       # work not encoded back into ledger → loses continuity

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any claim of physical relevance should route here to find or propose a falsifier."
    - "Appx_27 is not a static appendix; treat it as a living ledger with statuses."
    - "Prefer experiment-lane nodes (27a/27b/27c) for detailed models and active results."
    - "All experiment outputs must log: assumptions, units firewall, horizon, and CQI-like robustness where applicable."

ledger_protocol:
  bounty_statuses: ["PROPOSED", "ACTIVE", "FALSIFIED", "PROMOTED", "INCONCLUSIVE"]
  required_fields:
    - "claim"
    - "target_domain"
    - "regulators_in_play"   # subset of {ζ, ω, ξ}
    - "units_firewall"
    - "method"
    - "success_condition"
    - "falsification_condition"
    - "data_or_sim_refs"
    - "status"

source:
  format: "canonical_artifact + trailhead"
  reference:
    - "Appx_27_Proposed_Experiments_v1.0.pdf"
    - "Appx_27_Experimental_Ledger_Trailhead_v1.0"
---

# Appx_27 — Proposed Experiments / Experimental Ledger (SPINE)

Appx_27 is the Proofield’s active falsification interface:
a living bounty board where experiments, simulations, and retrospective mining attempt to differentiate structure from story.

Collapse consequence:
A theory without tests becomes belief; coherence collapses when falsification stops.

Container principle:
Appx_27 is the ledger spine; Appx_27a/27b/27c... are experiment lanes (each a contained path with its own models, datasets, and results).


---
## Dependency Links
**Depends on:**
- [[Appx_00__SPINE|Appx_00]]
- [[Appx_01__SPINE|Appx_01]]
- [[Appx_02__SPINE|Appx_02]]
- [[Appx_04__SPINE|Appx_04]]
- [[Appx_05__SPINE|Appx_05]]
- [[Appx_06__SPINE|Appx_06]]
- [[Appx_12__SPINE|Appx_12]]
- [[Appx_14__SPINE|Appx_14]]
- [[Appx_22__SPINE|Appx_22]]

**Enables:**
- [[Appx_27a__SPINE|Appx_27a]]
- Appx_27b *(not in vault)*
- Appx_27c *(not in vault)*
- [[spine__NL_01_Lab__SPINE_v0.1_TRAILHEAD|NL_01]]
- COG_00 *(not in vault)*

**Content:** [[Appx_27__CONTENT|Appx_27 CONTENT]]
