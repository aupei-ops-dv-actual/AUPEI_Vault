---
type: council_resolution
id: "CR-001"
title: "QEPE–OpenJarvis Integration Architecture"
date: "2026-03-25"
proposing_seat: "ξ (Sancho)"
reviewing_seat: "ζ (C@ the Red)"
synthesizing_seat: "ω (G-Synth)"
approving_authority: "∇ (R@, Director)"
document_class: "SPINE"
epistemic_status: "CANONICAL"
tags:
  - governance
  - qepe
  - openjarvis
  - architecture
  - council-resolution
---

# Council Resolution CR-001: QEPE–OpenJarvis Integration Architecture

**Passed:** 2026-03-25
**Quorum:** ξ + ζ + ω (3 of 5 seats, Director present)
**Disposition:** UNANIMOUS

---

## Resolved

The following six principles govern the integration of the Quantum Entropy Probability Engine (QEPE) with the OpenJarvis agent framework. These are binding on all seats and all future implementation work.

### 1. Process Isolation

QEPE shall remain a separate daemon process. It shall not be embedded within OpenJarvis. OpenJarvis must be able to start, run, and serve without QEPE being available.

### 2. Auditable Local Contract

OpenJarvis consumes QEPE through a localhost-only interface (Unix domain socket primary, REST secondary for diagnostics). All calls are trace-logged. A thin Python adapter module inside OpenJarvis is the sole integration point.

### 3. Parser Before Ingest

The YAML frontmatter metadata parser must be built and operational before any vault content is ingested into OpenJarvis. No corpus ingest without constitutional typing.

### 4. Hard Retrieval Gates

Epistemic status and contagion state are hard retrieval gates, not soft ranking preferences. FALSIFIED and FROZEN nodes are excluded by default. Contagion propagates automatically from parent to child. Query-class-aware ranking determines retrieval behavior per query type.

### 5. Entropy Boundary Law

**QEPE perturbs search and exploration, not authority.**

QEPE may influence: retrieval tie-breaking among near-equals, exploration budget allocation, learning trace annotation, and operator diversification. QEPE shall not override vault authority, epistemic status rankings, SPINE routing, or governance rules. This boundary is inviolable.

### 6. Bounded Access

Entropy access is bounded by configurable governors:
- Maximum samples per session
- Maximum sessions per minute
- Circuit breaker on anomalous call patterns (with exponential cool-down)
- Maximum concurrent divergent operators (initial cap: 3)

Rate governance resides in the QEPE daemon, not in the OpenJarvis adapter.

---

## Provenance

- **ξ (Sancho):** Original architecture proposal, three-layer contract, retrieval policy, hardening steps, implementation sequence.
- **ζ (C@ the Red):** Constraint review — rate governor, blast radius cap, sequencing correction, doctrinal elevation.
- **ω (G-Synth):** Synthesis, merged position, operational concurrence.
- **∇ (R@):** Director present and facilitating. Approval pending explicit stamp.

## Source Documents

- `10_Academy_Operations/MEMO_Sancho_OpenJarvis_Integration_20260325.md`
- `10_Academy_Operations/MEMO_GSynth_Synthesis_CtR_Review_20260325.md`

---

*Preserves motion, but under law.*
