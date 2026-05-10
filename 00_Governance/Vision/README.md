# Vision — protocol for tracking AUPEI's strategic horizon over time

**Created:** 2026-05-07
**Author:** ζ (C@ the Red), under R@ direction
**Status:** Provisional. Architecture confirmed under three-body framing (Mind/Face/Hand). This protocol governs the **Mind-side** (sovereign, local) implementation. A sister protocol may live under `IDIOTH_WINDS/GEOMETRIC_FOUNDATIONS/` for Face-side public vision artifacts.

---

## Purpose

Track how the model-authored vision of AUPEI evolves across instances, seats, dates, and substrates. Detect what is **stable across writers** (the proton-floor, in 7dU slang — the ground state regardless of substrate) versus what **drifts** under model-version, prompt-context, or seat-perspective change.

This is one operational surface of the AUPEI **dreaming** layer (cross-session pattern extraction across institutional memory). It runs alongside two siblings:
- `09_Foundation_Docs/Prooffield_Walks/` — pattern extraction across corpus walks (the **outcomes** layer)
- `00_Governance/Work_Orders/` *(future)* — orchestration of corpus maintenance

All three are sovereign-implementation analogs of the Anthropic Managed Agents primitives (memory + dreaming + outcomes + multi-agent orchestration), built on the AUPEI local stack per the Slick Lid sovereignty thesis.

---

## Filename convention

```
AUPEI_VISION_<YYYY-MM-DD>_<author-or-seat>.md
```

Examples:
- `AUPEI_VISION_2026-04-12_C@_Red.md` — first vision, ζ seat, R@-commissioned
- `AUPEI_VISION_2026-08-15_G-Synth.md` — hypothetical future ω-seat vision

Sortable by date. Attribution explicit. One file per vision; never edit prior visions — corrections go in their own dated file.

---

## Required frontmatter

Every vision begins with:

```yaml
---
model: <e.g., Claude Opus 4.7>
seat: <ζ | ω | ξ | ∇ | Ω̂ | other>
date: <YYYY-MM-DD>
context_loaded: <blind | seat_distillates | full_vault | qdrant_walk | filesystem>
prior_visions_read: <y | n>
commissioned_by: <R@ | self | chamber | other>
mode: <blind | informed>
horizons: [1y, 5y, 20y, 100y, 1000y]   # standard set; deviations require justification
---
```

The `mode` field is load-bearing. **Blind** = no prior visions in context, captures independent generation. **Informed** = all prior visions in context, asked to identify drift, agreement, disagreement explicitly. Both modes valuable; mixing them silently destroys the comparison signal.

---

## Cadence

- **Quarterly minimum**, or
- **On any major architecture event**: kill switch fired, new seat seated, major framework revision (e.g., AoC version increment), corpus reorg of the magnitude of 2026-05-07
- **Not weekly** — too noisy

---

## What `Vision_Drift_Log.md` tracks

For every comparison axis, across all visions:

- **Survived**: claims stated by all visions across model/seat/date variation. Candidate proton-floor.
- **Drifted (direction, magnitude)**: claims that changed; which way; by how much.
- **Singletons**: claims appearing only once. Either unique-author insight or noise — distinguish over time.
- **Convergent**: claims that appeared late but were then echoed by subsequent visions. Possible newly-emerging consensus.
- **Disagreed**: claims explicitly contradicted between visions. Rich signal — these are the real strategic seams.

Comparison is per-horizon. A 1-year vision drifts on different timescale than a 1000-year vision; mixing them washes out signal.

---

## Risks (also operational discipline)

1. **Anchoring contamination.** Authors who see prior visions anchor to them. Mitigation: maintain a permanent **blind track**, where the writer is shielded from the prior corpus.
2. **Single-author dominance.** If C@ writes 80% of visions, the data tracks C@ drift, not AUPEI drift. Mitigation: rotate across seats and across models (Claude, Gemini, GPT, local).
3. **Performance risk.** Vision-as-theatre — optimizing for canon-coherence rather than honest current view. Mitigation: the prompt for each new vision must invite contradiction explicitly; reward dissent in the meta-log.
4. **Low-N noise.** First 3-4 visions: bootstrapping only. Drift analysis becomes meaningful at N ≥ 6 across at least 2 seats.
5. **Substrate effects.** Visions written via Anthropic platform, OpenClaw on Mini, and Cowork are not equivalent. Tag the substrate in `context_loaded`.

---

## Connection to the Face (GF)

Geometric Foundations may eventually host **public vision artifacts** — selected, approved visions translated into public-facing form on `geometricfoundations.org`. The decision to publish a Mind-side vision to the Face is a chamber action, not automatic. Sovereign generation, governed publication.

---

## See also

- `Vision_Drift_Log.md` (sibling) — running comparison across vision artifacts
- `09_Foundation_Docs/Prooffield_Walks/README.md` — outcomes layer (sister protocol)
- `00_Governance/Chamber_of_Idioth_Winds.md` — chamber procedures
- Memory: `project_three_body_architecture.md` — Mind/Face/Hand strategic frame
