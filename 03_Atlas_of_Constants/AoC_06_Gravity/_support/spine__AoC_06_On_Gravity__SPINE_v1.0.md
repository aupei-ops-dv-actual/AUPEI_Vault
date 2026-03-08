---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_06"
internal_id: "Appx_07_AoC_06_On_Gravity_PF_v0.2_Trailhead"
title: "AoC_06 — On Gravity (αᴳ, G)"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "Trailhead: derivation program for gravity as coherence-dilution residual"
load_bearing: "atlas_trailhead"

epistemic_status: "TRAILHEAD"
non_claim: "No completed derivation yet; structural + falsification scaffold only."

depends_on:
  - "AoC_00"   # Ω̂
  - "AoC_01"   # π
  - "AoC_02"   # c
  - "AoC_03"   # α
  - "AoC_04"   # m_p
  - "AoC_05"   # m_n
  - "Appx_10a"  # Gravity Threshold Discriminator (27a-style container ok)
  - "Appx_10"   # HoQG
  - "Appx_13"   # GR Reduction (or GR interface appendix)
  - "Appx_08"   # Time / dimensionality (if split)
  - "Appx_09"   # Spatial dimensionality (if split)
  - "Appx_16"   # CCT-1
  - "Appx_17"   # Linda Function
  - "Appx_20"   # Black holes
  - "Appx_21"   # Experiments (or experiment appendix)

enables:
  - "AoC_07"   # (reserved) downstream gravity-coupled constants if any
  - "Appx_27"  # Experiments ledger (promotion gate + falsifiers)

failure_topology:
  contagion: "atlas_total_if_promoted"
  class: "Atlas Trailhead"
  promotion_gates:
    required_for_derivation:
      - "explicit_coherence_measure"
      - "long_mode_suppression_law"
      - "derive_alphaG_without_importing_G"
      - "survivability_window_analysis"
      - "observational_falsifiers_defined"
  kill_switch_ids:
    - "AG-IMPORT-G"                 # G smuggled in before αᴳ exists
    - "AG-NO-COHERENCE-MEASURE"     # no explicit coherence observable
    - "AG-NO-DILUTION-LAW"          # cannot derive 1/r^2 tail (or required tail form)
    - "AG-EPOCH-SCALE-FAIL"         # αᴳ fails scale/epoch consistency checks
    - "AG-STRONG-CURVATURE-FAIL"    # breaks in strong-curvature regime without new parameters

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Treat AoC_06 as TRAILHEAD: answer with program + tests, not a claimed derivation."
    - "Always separate dimensionless survivor αᴳ from unitful calibration G (Units Firewall)."
    - "If user requests numerical value of G, respond with calibration-only framing unless αᴳ is derived."
    - "If any kill-switch triggers, freeze any gravity-derived downstream claims and route to Appx_27."

source:
  primary:
    format: "text"
    filename: "gravity_trailhead.txt"
  secondary:
    format: "pdf"
    filename: "Appx_07_AoC_06_On_G_STUB.pdf"
---

# AoC_06 — On Gravity (αᴳ, G) — SPINE (TRAILHEAD)

This node is a **trailhead marker**: it holds the **derivation program**, **dependency spine**, and **falsification hooks** for gravity.

Content lives in:
`/content/content__AoC_06_On_Gravity__CONTENT_v0.2_TRAILHEAD.md`
