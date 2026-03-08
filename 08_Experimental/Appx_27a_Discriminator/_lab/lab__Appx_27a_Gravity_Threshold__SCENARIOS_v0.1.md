---
atlas_id: "7dU_GraphRAG_Lab"
node_id: "Appx_27a_SCENARIOS"
internal_id: "lab__Appx_27a_Gravity_Threshold__SCENARIOS_v0.1"
title: "Appx_27a — Gravity Threshold Discriminator (Scenario Suite)"
status: "LAB_SCENARIOS"
date_minted: "2026-02-21"
layer: "lab"
domain: "Experimental Lane — Gravitational Threshold"
lane_parent: "Appx_27a"
ledger_parent: "Appx_27"
---

# Appx_27a — Scenario Suite
**Objective:** provide runnable experimental templates that can distinguish a mass-threshold gravity transition (M*) from classical GR + particulate dark matter.

Each scenario must:
- Define test family (A, B, or C).
- Declare Units Firewall.
- Expose falsification path.
- Produce reproducible outputs.

---

# SCENARIO 1 — Low-Mass Laboratory Deviation

## Family
A — Direct Micro-Gravity Test

## Hypothesis
For test masses M << M*, measured effective gravitational coupling deviates from G according to:
  Geff(M) = G exp(-M/M*)

## Setup
- Two-body Cavendish-type torsion balance.
- Test mass range: 10^-n kg to upper apparatus limit.
- Separation distance r fixed and controlled.
- Environmental noise floor quantified.

## Required Inputs
- Apparatus sensitivity threshold.
- Measurement uncertainty σ_G.
- Mass resolution precision.

## Procedure
1. Measure G across descending mass values.
2. Fit deviation curve to exponential model.
3. Compare to null model (Geff = G constant).

## Outputs
- ΔG(M) vs M curve.
- Best-fit M* (if deviation observed).
- Confidence interval.
- Null rejection confidence.

## Falsification Exposure
Fails H27a if:
- No statistically significant deviation in predicted low-mass region.
- Observed deviation incompatible with exponential form.

---

# SCENARIO 2 — Dwarf Galaxy Rotation Curve Discriminator

## Family
B — Astrophysical Fit Discriminator

## Hypothesis
Low-mass galactic constituents fall below M*, weakening effective coupling and mimicking dark matter effects.

## Dataset Class
- Dwarf galaxies
- Low Surface Brightness (LSB) galaxies

## Units Firewall
Hold fixed:
- Stellar mass-to-light ratio assumptions
- Gas mass modeling framework
Allow variation:
- Single global M*

## Procedure
1. Fit classical GR-only model (baseline).
2. Fit GR + particulate DM halo (ΛCDM baseline).
3. Fit GR with Geff(M) threshold model.
4. Cross-validate using holdout galaxy subset.

## Outputs
- Residual comparison across models.
- Best-fit M* distribution.
- Out-of-sample predictive error.

## Decision Rule
If single M* improves predictive performance without extra free parameters,
model strengthens.
If inconsistent M* required per galaxy class,
lane weakens.

---

# SCENARIO 3 — Weak Lensing Mass Profile Test

## Family
B — Macro-Scale Discriminator

## Hypothesis
Effective gravitational coupling attenuates for sub-threshold mass structures, altering shear profiles.

## Dataset Class
- Weak lensing surveys
- Cluster mass reconstructions

## Procedure
1. Compute predicted lensing profile under classical GR.
2. Compute profile under Geff(M) attenuation.
3. Compare to observational shear data.
4. Evaluate residual structure vs redshift and halo mass.

## Outputs
- Shear residual distribution.
- Required M* for fit consistency.
- Redshift dependence test.

## Falsification Exposure
Fails if:
- No measurable profile divergence at predicted mass scales.
- Attenuation produces contradictions at stellar or cluster scales.

---

# SCENARIO 4 — Compact Object Desert Search

## Family
C — Structural Census Test

## Hypothesis
There exists a suppressed stability band near M* (transition desert).

## Dataset Class
- Stellar remnant catalogs
- Brown dwarf and compact object surveys
- Sub-stellar mass distributions

## Procedure
1. Define mass window around candidate M* (log scale).
2. Construct expected background mass distribution.
3. Compare observed frequency to expected frequency.
4. Evaluate statistical significance.

## Outputs
- Mass histogram around M*.
- Significance of deficit or absence.
- Robustness under binning variation.

## Falsification Exposure
Fails if:
- Stable object frequency near M* matches background expectation.
- No measurable structural suppression exists.

---

# SCENARIO 5 — Unified Cross-Scale Fit

## Family
Hybrid — Families A + B + C

## Hypothesis
Single M* parameter explains:
- Lab-scale deviations (if detectable)
- Galactic rotation curves
- Lensing deviations
- Compact object desert

## Procedure
1. Estimate M* from astrophysical fits.
2. Predict lab deviation magnitude.
3. Predict census desert band.
4. Test cross-consistency.

## Success Condition
- One M* value (within uncertainty bounds) satisfies multiple domains.

## Failure Condition
- Domain-specific M* values diverge wildly.
- Model requires additional free parameters to remain viable.

---

# Versioning Rules

Each scenario run must log:
- Scenario ID (e.g., 27a-S2-YYYYMMDD-01)
- Dataset used
- Parameter count
- Fit quality metrics
- Cross-validation performance
- Falsification exposure
- Status update

---

# Structural Guardrail

This suite must not:

- Add unconstrained tuning parameters.
- Change functional form without versioning.
- Hide null results.
- Collapse into narrative justification.

If M* cannot produce coherent cross-scale predictions,
H27a weakens.

If it does,
gravity transitions from deterministic curvature to probabilistic threshold.

The purpose is decision.
Not preservation.