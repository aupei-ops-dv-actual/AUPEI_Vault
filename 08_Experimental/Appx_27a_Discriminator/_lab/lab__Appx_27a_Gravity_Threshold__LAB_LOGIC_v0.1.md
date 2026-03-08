---
atlas_id: "7dU_GraphRAG_Lab"
node_id: "Appx_27a_LAB"
internal_id: "lab__Appx_27a_Gravity_Threshold__LAB_LOGIC_v0.1"
title: "Appx_27a — Gravity Threshold Discriminator (Lab Logic)"
status: "LAB_LOGIC"
date_minted: "2026-02-21"
layer: "lab"
domain: "Experimental Falsification / Macro+Micro Gravity"
lane_parent: "Appx_27a"
ledger_parent: "Appx_27"
---

# Appx_27a — Gravity Threshold Discriminator (Lab Logic)
**Decision objective:** distinguish a mass-threshold gravity transition from classical universal gravity + particulate dark matter explanations.

---

## 0) Core Hypothesis (H27a)

There exists a critical mass scale **M\*** such that:

- **M >> M\*** ⇒ \( G_{\text{eff}} \rightarrow G \) (classical)
- **M << M\*** ⇒ \( G_{\text{eff}}(M) = G \exp(-M/M^*) \) (attenuated / probabilistic)

This lane asserts **mass-dependent coupling** in the low-mass regime as a discriminating signature.

---

## 1) Variables & Control Surfaces

### Primary parameter
- **M\*** (threshold mass scale)

### Observable surfaces (what the world gives us)
- **Rotation curves** (galaxies, dwarfs, LSB galaxies)
- **Weak lensing** (shear profiles, halo-mass relations)
- **Compact object census** (mass distribution gaps/deserts)
- **Laboratory gravity measurements** (micro-mass regimes)

### Control knobs (what the lab can vary)
- test mass \( M \)
- separation distance \( r \)
- environment isolation / noise floor
- dataset selection criteria and priors

---

## 2) Test Families (Minimal Set)

The lane is valid only if it runs **at least two independent test families**.

### Family A — Lab Micro-Gravity (direct)
Goal: detect deviation in measured effective coupling at low mass.

Minimum deliverable:
- A predicted deviation curve:
  \( \Delta G(M) = G - G_{\text{eff}}(M) \)
- Instrument sensitivity threshold required to resolve it.
- A clear statement of whether current instrumentation can or cannot detect it.

Primary outputs:
- measured \( G_{\text{eff}} \) vs \( M \) (and uncertainty)
- decision: deviation / no deviation / inconclusive

---

### Family B — Astrophysical Fit Discriminator (indirect)
Goal: assess whether a single M\* can explain rotation and lensing systematics without particulate DM.

Minimum deliverable:
- Fit \( M^* \) on a training set.
- Predict out-of-sample on a test set (no refitting).
- Compare to baseline models:
  - ΛCDM + DM halos
  - MOND-like phenomenology (if included)
  - Classical GR-only null model

Primary outputs:
- best-fit \( M^* \) distribution (mean, variance)
- residuals by class (galaxy type, mass range)
- cross-validation performance

---

### Family C — Census / “Desert” Prediction (structural)
Goal: test whether there is an instability band near M\* (no stable structures).

Minimum deliverable:
- Define “desert” hypothesis precisely:
  - mass window around M\* (log-scale band)
  - expected suppression relative to background distribution
- Identify catalogs / datasets used
- Statistical significance thresholds

Primary outputs:
- mass histogram around predicted M\*
- significance of deficit (or absence)

---

## 3) Measurement Standards (What Counts as Measurement)

A “measurement” is valid only if it includes:

1) explicit unit regime and assumptions (Units Firewall)
2) uncertainty bounds
3) baseline comparison model
4) an out-of-sample check OR independent dataset replication
5) a falsification criterion that could fail the lane

If any of these are missing, classify as **PROPOSED**, not **ACTIVE**.

---

## 4) Falsification Criteria (Hard-Edged)

The lane moves to **FALSIFIED** if any of the following are robustly true:

### F1 — No low-mass deviation
High-sensitivity lab tests show:
\( G_{\text{eff}}(M) \approx G \) across the predicted low-mass region,
with error bars that exclude the exponential attenuation model.

### F2 — No single-threshold consistency
Astrophysical fits require wildly incompatible M\* values across classes,
with no coherent scaling law and no reproducible predictive power.

### F3 — Particulate DM is required
Rotation/lensing/census anomalies cannot be matched without invoking particulate DM,
even after allowing M\* variation within reasonable bounds.

### F4 — Transition signature absent
No coherent “knee,” inflection, or threshold behavior exists in any observable surface
where the model predicts it should.

---

## 5) “Metric Gaming” / Failure Modes (Anti-Artifact Discipline)

This lane is especially vulnerable to:
- overfitting M\* to any dataset (“M\* as duct tape”)
- post-hoc selection of galaxy classes that behave well
- priors that smuggle in the conclusion

### Disallowed behaviors (auto-fail to INCONCLUSIVE)
- fitting and validating on the same population without holdout
- changing the definition of M\* midstream without versioning
- hiding null results
- cherry-picking catalogs without stating exclusion rules
- adding unbounded free parameters to rescue the exponential form

**Rule:** if the model needs >1 new unconstrained parameter beyond M\* to fit, it is drifting toward story.

---

## 6) Status Protocol (Ledger Binding)

Every run must log:

- claim tested
- dataset or apparatus
- assumptions / Units Firewall
- priors and selection rules
- parameter count
- results + uncertainty
- whether it supports, weakens, or falsifies H27a

Allowed statuses (Appx_27 standard):
- PROPOSED
- ACTIVE
- INCONCLUSIVE
- FALSIFIED
- PROMOTED

Promotion standard:
- at least **two independent test families** produce coherent evidence
- at least one out-of-sample prediction succeeds
- failure modes addressed explicitly

---

## 7) Minimal Logging Template (Copy/Paste)

**Run ID:** 27a-YYYYMMDD-###  
**Test Family:** A / B / C  
**Claim:** (one sentence)  
**Units Firewall:** (what is held fixed; what is allowed to vary)  
**Data/Apparatus:**  
**Selection Rules / Priors:**  
**Model:** \( G_{\text{eff}}(M)=G\exp(-M/M^*) \)  
**Free Params:** (count and list)  
**Result:** (M\* estimate, fit quality, uncertainty)  
**Out-of-sample:** yes/no (describe)  
**Falsification exposure:** which F1–F4 could this have failed?  
**Status:** PROPOSED / ACTIVE / INCONCLUSIVE / FALSIFIED / PROMOTED  
**Notes:** (short)

---

## 8) Lane Motto (operational)
Low cost. High differentiator. Clean falsifier.

This lane exists to decide, not to decorate.