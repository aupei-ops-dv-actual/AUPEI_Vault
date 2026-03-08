---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_01_S00"
internal_id: "AoC_01_PI_SUPPORT_00_DEV_PREFACE_v1.0"
title: "AoC_01 Support 00 — π Dev Preface"
status: "SPINE"
date_minted: "2026-02-21"
layer: "spine"
domain: "Atlas_of_Constants"
role: "Support: development preface + framing for π emergence"
load_bearing: "support_subordinate"

depends_on:
  - "AoC_01"   # On π (main constant node)

enables:
  - "AoC_01_S01"  # Analytic derivations
  - "AoC_01_S02"  # Radial derivations
  - "AoC_01_S03"  # Numerical derivations

failure_topology:
  contagion: "local_support"
  class: "Support Node"
  kill_switch_ids:
    - "PI-SUPPORT-PREFACE-CONTRADICTION"   # Preface contradicts canonical AoC_01 definition/protocol

rag_policy:
  gate_required: false
  retrieval_rules:
    - "Use as context/framing only; do not treat as primary proof if it conflicts with AoC_01."
    - "If contradictions are detected, prefer AoC_01 canonical and flag via Appx_27."

source:
  format: "pdf"
  filename: "AoC_01_PI_SUPPORT_00_DEV_PREFACE.pdf"
---

# AoC_01 Support 00 — π Dev Preface — SPINE

Support metadata node for π workstream.

Content lives in:
`/support/content__AoC_01_PI_SUPPORT_00_DEV_PREFACE__CONTENT_v1.0.md`
