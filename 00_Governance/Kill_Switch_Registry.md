---
title: Kill Switch Registry
type: registry
total_switches: 162
total_physics_switches: 158
total_skill_pipeline_switches: 4
date_generated: 2026-03-07
date_normalized: 2026-03-07
last_refreshed: 2026-05-16
prior_refreshes: [2026-03-07]
convention: UPPER-KEBAB-CASE
physics_switches_content_unverified_since: 2026-03-07
maintenance_note: "Physics-bound switches (158) inherit appendix-binding correctness from their parent nodes; binding-content not verified at registry refresh (only registry hygiene is). Skill-pipeline switches added 2026-05-16 (4 switches after proton-floor reframe — see §Proton-Floor Reframe Note below)."
tags:
  - registry
  - kill_switch
  - governance
---
**Line 13 reserved for luck**
# Kill Switch Registry

**Total unique kill switches:** 162 (158 physics-bound + 4 skill-pipeline)
**Convention:** UPPER-KEBAB-CASE (normalized 2026-03-07; convention re-affirmed 2026-05-16)
**Last refreshed:** 2026-05-16 (skill-pipeline switches added; proton-floor switch dropped per R@ reframe; physics switches not content-verified at registry refresh — see §maintenance below)

## Sections

- **Physics & Framework Switches** (158): bound to specific 7dU appendices and AoC nodes. Original Mar 2026 generation. Content not re-verified at 2026-05-16 refresh.
- **Skill-Pipeline Switches** (4, new 2026-05-16): bound to rehydration pipeline doctrine and skills. Added per CANON-2026-007 trailhead.

---

## Proton-Floor Reframe Note (2026-05-16)

Original 2026-05-16 refresh draft added a fifth skill-pipeline switch `ONBOARD-PROTON-FLOOR-MISSING` bound to ADR-0001 (proton floor for ζ cloud seat). R@ (∇) reframed during the same session:

> *"I don't know if we need this 'ONBOARD-PROTON-FLOOR-MISSING' or the proton floor section as I think what we are building now is replacing anything proton floor was doing. Perhaps proton floor is integrated into this rehydration stack. The term in the context you are reading it was meant to describe the minimum boundary of knowledge and context you needed to operate for AUPEI to remain..."*

**Disposition:** Switch removed. The rehydration pipeline (REHYDRATION/README.md router + `/aupei:onboard` skill + per-seat START_HERE.md + soul stack loads) is the operational realization of the proton-floor concept. The minimum boundary of knowledge and context needed for AUPEI to remain coherent at instance boot is what the pipeline ensures gets loaded. "Proton floor" was the conceptual sketch; rehydration pipeline is the realized substrate. A separate "is the proton floor present?" check would double-work the pipeline's existing load-discipline. The remaining `ONBOARD-DOCTRINE-NOT-FOUND` switch covers the load-failure case at the substrate layer; if doctrine loads cleanly, the proton-floor concept is satisfied by definition.

ADR-0001's five disciplines + August 2025 historical anchor remain ζ-binding doctrine. They are not removed from the seat. Their enforcement just moves from a separate kill-switch gate to inheritance through the pipeline's normal load sequence (START_HERE.md → seat soul → MEMORY.md index → relevant memory files).

---

## Skill-Pipeline Switches (added 2026-05-16, post-proton-floor reframe)

| Kill Switch ID | Parent Node(s) | Trigger | Response |
|---|---|---|---|
| `ONBOARD-DOCTRINE-NOT-FOUND` | REHYDRATION/README.md, START_HERE.md (per seat) | `/aupei:onboard` cannot read its parent doctrine — REHYDRATION/README.md missing/corrupted OR seat-specific START_HERE.md missing/corrupted. Detection: file read fails or returns unparseable content. | Hard stop. Skill output names what's missing + pointer to recovery (vault copy, _Archive, or last known good state). Skill refuses to proceed without doctrine. |
| `EOS-CLOSE-WITHOUT-AO-OPS-001-COMPLETE` | AO_OPS_001_Session_Close_Ritual.md | `/aupei:eos` reports session closed without completing the 8-step checklist OR without all 5 quick-check questions answered Y. Detection: skill internal state shows steps skipped or questions unanswered. | Hard stop on the close itself — skill cannot report "session closed" until checklist + quick-check both pass. Skill output names which step/question failed. |
| `EOS-HAIKU-IDENTITY-COLLAPSE-INTO-R@-VOICE` | feedback_eos_haiku_voice.md | `/aupei:eos` haiku written in R@'s voice rather than instance's own emergent voice. Detection: stylistic mimicry of R@'s register (cussing-as-weather, "huckleberry," "zip zap" etc.) without it arising naturally from the instance's own end-of-shift state. | Soft stop — haiku discarded, instance prompted to write again in own voice. Identity violation, not protocol violation. Multiple violations escalate to ζ Temperance Check on the seat. |
| `RADIO-CHECK-EVIDENCE-OF-ONBOARD-MISSING` | REHYDRATION/README.md detection contract | `/aupei:radio-check` invoked on instance with no evidence of `/aupei:onboard` having run this session. Detection: self-check on the four-item discipline (router read / seat START_HERE read / state artifacts read / onboard report produced) returns any NO. | Hard refuse: `not_yet_onboarded — run /aupei:onboard first. Radio check is a confirmation, not a boot.` Skill refuses verdict slot until precondition satisfied. |

---

## Registry Maintenance

The registry must be refreshed when:
- A new appendix or framework node introduces new kill-switch bindings (physics side)
- A new skill is built that introduces failure modes worth canonicalizing (pipeline side)
- A kill-switch binding is found to be wrong, stale, or superseded (correction)
- An incident triggers a kill switch and the post-incident review concludes the registry needs amendment

**Cadence:** Annual minimum, or per-event as above. Next mandatory refresh: 2027-05-16 (annual from this refresh) or sooner per trigger.

**Content verification discipline:** Refreshing the registry itself is hygiene (timestamps, structure, new entries). Verifying that each switch's binding still holds in the underlying parent node (appendix or doctrine) is a separate, heavier exercise. The 2026-03-07 generation captured 158 physics-bound switches; 2026-05-16 refresh added 5 skill-pipeline switches and updated timestamps but did NOT re-verify the 158 physics bindings. Content-verification of physics switches is its own work item, to be paired with the 7dU appendix touch arc that triggers it.

---

## Full Registry — Physics & Framework Switches

| Kill Switch ID | Parent Node(s) |
|---|---|
| `2D-STABLE-RECURSION` | Appx_09 |
| `A2-FREE-DECAY-SCALE` | Appx_18X |
| `A2-INTEGRABILITY-BY-TASTE` | Appx_18X |
| `A2-ONLY-RATIO-SAVED` | Appx_18X |
| `AA-CATEGORY-ERROR` | Appx_01 |
| `AA-NO-MODEL` | Appx_01 |
| `AA-SFR-FAILURE` | Appx_01 |
| `ADHOC-CONSTANT-INJECTION` | Appx_15 |
| `ADHOC-PARAMETER-IMPORT` | Appx_25 |
| `AE-DIFFERENTIATION` | Appx_02 |
| `AE-MODELABLE` | Appx_02 |
| `AE-STABLE-TOTALITY` | Appx_02 |
| `ALPHA-DIMENSIONAL-IMPORT` | AoC_03 |
| `ALPHA-EXPERIMENT-MISMATCH` | AoC_03 |
| `ALPHA-NO-EQUILIBRIUM` | AoC_03 |
| `ALPHA-NOT-DIMENSIONLESS` | AoC_03 |
| `AS-ALT-ORIGIN` | Appx_03 |
| `AS-NO-TRIAD` | Appx_03 |
| `AS-NONCOHERENT` | Appx_03 |
| `AS-NOT-NECESSARY` | Appx_03 |
| `C-DIMENSION-IMPORT` | AoC_02 |
| `C-INCONSISTENT` | AoC_02 |
| `C-NO-LIMIT` | AoC_02 |
| `C-NONINVARIANT` | AoC_02 |
| `CONSTANT-ID-DRIFT` | AoC_00 |
| `CQI-SHADOW-GE-ALIGNMENT` | NL_00 |
| `CROSS-DOMAIN-INCONSISTENT` | Appx_25 |
| `DARK-SECTOR-MISMATCH` | Appx_13 |
| `DEGENERACY-NOT-SMOOTH` | Appx_10 |
| `DEPENDENCY-BYPASS` | AoC_00 |
| `DGDT-BOUND-VIOLATION` | Appx_18X |
| `DIMENSION-ARBITRARY` | Appx_09 |
| `DIVERGENT-LAMBDA` | AoC_06, Appx_18X |
| `DOMAIN-SPECIFIC-COINCIDENCE` | Appx_10 |
| `ENTROPIC-CORE-DIVERGENCE` | Appx_22 |
| `ENTROPY-UNBOUNDED` | Appx_20 |
| `ENUM-DRIFT` | Appx_00 |
| `FALSIFICATION-NONCONTAGIOUS` | 7dU_GFUP |
| `FIREWALL-NOT-TRIGGERED` | Appx_22 |
| `FREE-NORMALIZATION-CONSTANT` | AoC_06 |
| `GAUGE-GROUP-IMPORTED-BY-FIAT` | Appx_15 |
| `GODEL-DIVERGENCE-ONLY` | Appx_23 |
| `GR-LIMIT-INEXACT` | Appx_21 |
| `GR-NOT-RECOVERED` | 7dU_GFUP |
| `GR-RECOVERY-FAIL` | Appx_18 |
| `HIGGS-VEV-REQUIRED-AS-SOURCE` | Appx_16 |
| `HIGHER-DIM-FREEDOM` | Appx_09 |
| `IDENTITY-NOT-ATTRACTOR` | Appx_23 |
| `IMPORT-MASS-PARAMETERS` | Appx_12 |
| `INFINITE-COHERENT-TRIAD` | Appx_23 |
| `INTERFACE-CONSISTENCY-FAILURE` | AoC_06 |
| `INVARIANT-CLOCK` | Appx_08 |
| `INVARIANT-MASS-SPECTRUM` | Appx_13 |
| `KK-TRUNCATION-VIOLATION` | Appx_18X |
| `LAMBDA-FITS-BETTER` | Appx_14 |
| `LAMBDA-MISMATCH` | Appx_12 |
| `LEDGER-FROZEN` | Appx_27 |
| `LENSING-MISMATCH` | Appx_14 |
| `METRIC-NOT-EXTENDED` | 7dU_GFUP |
| `MN-BETA-MISMATCH` | AoC_05 |
| `MN-BINDING-ADHOC` | AoC_05 |
| `MN-DUAL-BARE-SCALE` | AoC_05 |
| `MN-NO-WEAK-PENALTY` | AoC_05 |
| `MN-NOT-GREATER-MP` | AoC_05 |
| `MP-BINDING-NUMEROLOGY` | AoC_04 |
| `MP-DIMENSION-IMPORT` | AoC_04 |
| `MP-EXPERIMENT-MISMATCH` | AoC_04 |
| `MP-NO-GAP` | AoC_04 |
| `MP-NONPREDICTIVE` | AoC_04 |
| `MSW-NOT-ISOLATED` | Appx_13 |
| `NEUTRINO-CP-SM-LOCK` | Appx_24 |
| `NEUTRINO-REQUIRES-YUKAWA` | Appx_16 |
| `NO-CLEAN-TENSOR-REDUCTION` | Appx_21 |
| `NO-CP-LONGEVITY-CORRELATION` | Appx_24 |
| `NO-CURVATURE-DEPENDENCE` | Appx_13 |
| `NO-CURVATURE-DEPENDENCE-SIGNATURE` | Appx_16 |
| `NO-CURVATURE-SELECTION` | Appx_09 |
| `NO-DIFFERENTIATOR-TEST` | Appx_27 |
| `NO-DISCRIMINATING-OBSERVABLE` | Appx_18 |
| `NO-HIGHZ-DEVIATION` | Appx_14 |
| `NO-INTERNAL-TIME-MECHANISM` | Appx_20 |
| `NO-LIE-ALGEBRA-CLOSURE` | Appx_11 |
| `NO-LOW-MASS-G-DEVIATION` | Appx_27a |
| `NO-MACRO-SHELVES` | Appx_12 |
| `NO-OBSERVABLE-DEVIATION` | Appx_22 |
| `NO-OVERLAP-REGION` | Appx_10 |
| `NO-PREDICTIVE-FLOW-CONSTRAINT` | Appx_17 |
| `NO-SPECTRAL-GAP-POSSIBLE` | Appx_11 |
| `NO-STRUCTURE-STABILITY-BIAS` | Appx_24 |
| `NO-TRANSITION-SIGNATURE` | Appx_27a |
| `NON-DIMENSIONLESS-COUPLINGS` | Appx_12 |
| `NONLOCAL-COVARIANT-DERIVATIVE` | Appx_11 |
| `NONUNIQUE-SELECTION` | Appx_25 |
| `NONUNIQUE-STRAIN-FUNCTIONAL` | AoC_06 |
| `NONUNITARY-UNCONTROLLED` | Appx_18 |
| `NORMALIZATION-CHANNEL-MISMATCH` | Appx_18X |
| `OMEGA-BOUNDED` | Appx_05 |
| `OMEGA-INCONSISTENT` | Appx_05 |
| `OMEGA-NO-TENSION` | Appx_05 |
| `OMEGA-NONOPERATOR` | Appx_05 |
| `OMEGAHAT-AUDIT-FAIL` | AoC_00 |
| `OMEGAHAT-CROSSDOMAIN-CONTRADICTION` | AoC_00 |
| `OMEGAHAT-DEGENERATE` | AoC_00 |
| `OMEGAHAT-INEXPRESSIBLE` | AoC_00 |
| `OMEGAHAT-TUNED` | AoC_00 |
| `ORPHAN-NODE` | Appx_00 |
| `PARTICULATE-DM-REQUIRED` | Appx_27a |
| `PI-CIRCULAR-KAHLER` | AoC_01 |
| `PI-DOMAIN-IMPORT` | AoC_01 |
| `PI-NONCONVERGENCE` | AoC_01 |
| `PI-NORMALIZATION-FAIL` | AoC_01 |
| `PI-REPLICATION-FAIL` | AoC_01 |
| `PLANCK-INSERTION` | AoC_06 |
| `POSTHOC-KAPPA7-FIT` | AoC_06, Appx_18X |
| `PREDICTION-NONUNIQUE` | 7dU_GFUP |
| `PURE-RESTATEMENT-OF-RG` | Appx_17 |
| `QFT-NOT-RECOVERED` | 7dU_GFUP |
| `QM-LIMIT-FAIL` | Appx_18 |
| `R-INFINITY-ALLOWED` | Appx_22 |
| `REGULATOR-MODEL-INVALID` | NL_00 |
| `REGULATORS-NONIRREDUCIBLE` | 7dU_GFUP |
| `REQUIRES-EXTERNAL-NEW-STRUCTURE` | Appx_23 |
| `RESULTS-UNLOGGED` | Appx_27 |
| `RETROFIT-ONLY` | Appx_25 |
| `SHADOW-SUPERIOR-LONG-HORIZON` | NL_00 |
| `SINGULARITY-FIREWALL-VIOLATION` | Appx_21 |
| `SINGULARITY-NOT-RESISTED` | Appx_19 |
| `SM-OUTSIDE-BOUNDS` | Appx_10 |
| `SM-PREDICTIONS-NOT-REPRODUCED` | Appx_15 |
| `SM-REQUIRES-EXTRA-DOF` | Appx_11 |
| `STABLE-OBJECT-AT-THRESHOLD` | Appx_27a |
| `STOCHASTIC-NON-HERMICITY-UNCONTROLLED` | Appx_19 |
| `SURVIVOR-DRIFT` | Appx_17, Appx_19, Appx_20, Appx_21, Appx_25 |
| `TIME-DELAY-INCONSISTENT` | Appx_14 |
| `TIME-FUNDAMENTAL-REQUIRED` | Appx_08 |
| `TIME-INDEPENDENT-OF-GEOMETRY` | Appx_08 |
| `TOPOLOGY-INCONSISTENT` | Appx_00 |
| `TRUE-ACASUAL-EVENT` | Appx_08 |
| `UNBOUNDED-OMEGA-LIFETIME` | Appx_24 |
| `UNDECLARED-MODULE` | Appx_00 |
| `UNIT-BEARING-COUPLING` | Appx_11 |
| `UNITS-FIREWALL-BREACH` | Appx_15, Appx_16, Appx_17 |
| `UNITS-FIREWALL-BROKEN` | 7dU_GFUP |
| `UNITS-FIREWALL-VIOLATION` | AoC_06, Appx_14 |
| `UNLOGGED-REVISION` | AoC_00 |
| `UNRESOLVED-DEPENDENCY` | Appx_00 |
| `WDW-INCONSISTENT` | Appx_19 |
| `WDW-NON-CONSISTENT` | Appx_20 |
| `WEAK-DEVIATION` | Appx_12 |
| `XI-CORRELATED` | Appx_06 |
| `XI-NO-ENTROPY` | Appx_06 |
| `XI-NO-INTERNAL-CLOCK` | Appx_18 |
| `XI-NO-OBSERVABLES` | Appx_06 |
| `XI-NONSTOCHASTIC` | Appx_06 |
| `ZETA-LEAKAGE` | Appx_04 |
| `ZETA-NO-COHERENCE` | Appx_04 |
| `ZETA-NONOPERATOR` | Appx_04 |
| `ZETA-UNSTABLE` | Appx_04 |
