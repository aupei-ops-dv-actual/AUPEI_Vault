---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_01_S02"
internal_id: "AoC_01_PI_SUPPORT_02_RADIAL_v1.0"
title: "AoC_01 Support 02 — π Radial Derivation"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "Support: radial reduction and eigenmode isolation for π"
load_bearing: "support_loadbearing"

depends_on:
  - "AoC_01"      # On π (main constant)
  - "AoC_00"      # Collapse Operator (Ω̂)
  - "Appx_04"     # ζ
  - "Appx_05"     # ω
  - "Appx_06"     # ξ
  - "AoC_01_S01"  # Analytic derivations

enables:
  - "AoC_01_S03"  # Numerical derivations
  - "Appx_27"     # Experiments ledger (radial validation / falsifiers)

failure_topology:
  contagion: "local_support"
  class: "Support Node"
  kill_switch_ids:
    - "PI-RADIAL-CIRCULARITY"      # radial reduction assumes π in boundary condition
    - "PI-RADIAL-NORMALIZATION"    # geometric scaling imports π implicitly
    - "PI-RADIAL-NONISOLATION"     # failure to isolate λ₁ as π
    - "PI-RADIAL-INCONSISTENT"     # contradiction with analytic / canonical AoC_01

rag_policy:
  gate_required: false
  retrieval_rules:
    - "Use to answer 'show me the radial derivation' queries after AoC_01 gate."
    - "Treat as derivation support; do not override canonical AoC_01."
    - "If contradictions are detected, prefer AoC_01 and flag via Appx_27."

source:
  format: "pdf"
  filename: "AoC_01_PI_SUPPORT_02_RADIAL.pdf"
---

# AoC_01 Support 02 — π Radial Derivation — SPINE

Support metadata node for radial derivation backing AoC_01.

Content lives in:
`/support/support__AoC_01_PI_SUPPORT_02_RADIAL__CONTENT_v1.0.md`
