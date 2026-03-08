---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_01_S01"
internal_id: "AoC_01_PI_SUPPORT_01_ANALYTIC_v1.0"
title: "AoC_01 Support 01 — π Analytic Derivations"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "Support: analytic derivations for π emergence (Ω̂ eigenvalue)"
load_bearing: "support_loadbearing"

depends_on:
  - "AoC_01"      # On π (main constant)
  - "AoC_00"      # Collapse Operator (Ω̂)
  - "Appx_04"     # ζ
  - "Appx_05"     # ω
  - "Appx_06"     # ξ
  - "AoC_01_S00"  # Dev Preface

enables:
  - "AoC_01_S02"  # Radial derivations
  - "AoC_01_S03"  # Numerical derivations
  - "Appx_27"     # Experiments ledger (replication criteria)

failure_topology:
  contagion: "local_support"
  class: "Support Node"
  kill_switch_ids:
    - "PI-ANALYTIC-CIRCULARITY"      # analytic proof assumes π explicitly
    - "PI-ANALYTIC-NORMALIZATION"    # s_geom or domain normalization imports π
    - "PI-ANALYTIC-NONCONVERGENCE"   # analytic derivation fails to isolate stable eigenvalue
    - "PI-ANALYTIC-INCONSISTENT"     # contradictions with AoC_01 protocol/claims

rag_policy:
  gate_required: false
  retrieval_rules:
    - "Use to answer 'show me the analytic derivation' queries after AoC_01 gate."
    - "Do not override AoC_01 canonical; treat as proof support."
    - "If contradictions are detected, prefer AoC_01 and flag via Appx_27."

source:
  format: "pdf"
  filename: "AoC_01_PI_SUPPORT_01_ANALYTIC.pdf"
---

# AoC_01 Support 01 — π Analytic Derivations — SPINE

Support metadata node for analytic derivations backing AoC_01.

Content lives in:
`/support/support__AoC_01_PI_SUPPORT_01_ANALYTIC__CONTENT_v1.0.md`
