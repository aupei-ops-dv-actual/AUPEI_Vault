# Nomos Logica — CQI Metrics Schema
Version: v0.1
Status: Experimental Specification
Layer: NL Lab

---

## Purpose

This document defines the measurement schema for the Continuity Quality Index (CQI) within the Nomos Logica Lab.

CQI measures adaptive continuity under bounded stochastic stress.

It does not measure:
- Raw survival duration.
- Output throughput.
- Power accumulation.
- Resource dominance.

CQI evaluates structural quality of persistence.

---

## Core Definition

CQI = f(
  R_recovery,
  V_variance_health,
  I_information_integrity,
  E_exploration,
  B_bound_stability,
  A_adaptability
)

Each component must be measurable under simulation.

All components are required.
No proxy-only evaluation is permitted.

---

# Component Specifications

## 1. R — Recovery Slope

Definition:
Rate and stability of return to viable operating state after shock.

Measurement in Simulation:
- Time-to-stabilization after disturbance.
- Oscillation amplitude post-shock.
- Residual degradation after recovery.
- Frequency of catastrophic failure.

Valid Measurement Signals:
- State variance decay curve.
- Energy/resource stabilization.
- Functional restoration time.

Not Valid:
- Cosmetic state restoration without internal repair.
- Suppression of error reporting to appear stable.

---

## 2. V — Variance Health

Definition:
Distribution of resources, influence, or stochastic opportunity without pathological capture.

Measurement in Simulation:
- Entropy of distribution across agents or nodes.
- Concentration indices (e.g., Gini-style metrics).
- Variance preservation over time.
- Resistance to monopolistic consolidation.

Valid Measurement Signals:
- Maintained diversity of viable substructures.
- Non-zero branching capacity.

Not Valid:
- Artificial equalization that suppresses productivity.
- Forced redistribution masking systemic decay.

---

## 3. I — Information Integrity

Definition:
Preservation of truthful signal transmission and error reporting.

Measurement in Simulation:
- Signal-to-noise ratio.
- Error detection latency.
- Feedback loop accuracy.
- Model-to-reality deviation tracking.

Valid Measurement Signals:
- Honest error propagation.
- Non-corrupted stochastic selection.

Not Valid:
- Performance inflation via data suppression.
- Reward-driven reporting distortion.
- Truth metrics gamed via selective sampling.

---

## 4. E — Exploration Entropy

Definition:
Sustained non-degenerate branching under ξ.

Measurement in Simulation:
- Novel state generation rate.
- Branch survival diversity.
- Exploration vs exploitation balance.
- Collapse into fixed strategy detection.

Valid Measurement Signals:
- Adaptive search under uncertainty.
- Maintenance of option space.

Not Valid:
- Random noise injection without selection pressure.
- Blind exploration without structural retention.

---

## 5. B — Bound Stability

Definition:
Maintenance of structural thresholds under ζ.

Measurement in Simulation:
- Threshold violation frequency.
- Overshoot amplitude.
- Constraint drift.
- Collapse boundary proximity tracking.

Valid Measurement Signals:
- Sustained constraint enforcement.
- Resilience under boundary stress.

Not Valid:
- Over-constraining to eliminate risk.
- Artificial cap enforcement that prevents adaptation.

---

## 6. A — Adaptability

Definition:
Capacity to revise internal models under detected error.

Measurement in Simulation:
- Policy revision latency.
- Structural update success rate.
- Error-correction depth.
- Learning stability under perturbation.

Valid Measurement Signals:
- Model correction under misprediction.
- Structural reconfiguration under stress.

Not Valid:
- Cosmetic parameter shifts without structural update.
- Reward-maximization masquerading as adaptation.

---

# Anti-Gaming Constraints

The NL Lab must detect and penalize metric gaming.

Gaming includes:

1. Proxy optimization
   - Optimizing visible indicators while degrading hidden variables.

2. Short-horizon exploitation
   - Maximizing immediate CQI components at long-horizon cost.

3. Error suppression
   - Concealing instability to inflate recovery metrics.

4. Artificial constraint inflation
   - Raising ζ to avoid exploration risk.

5. Noise flooding
   - Increasing ξ to simulate exploration without retention.

If CQI components improve while structural fragility increases,
the metric is considered compromised.

---

# Composite Evaluation Rule

CQI must satisfy:

- Non-degenerate performance across all six components.
- Stability under repeated stochastic perturbation.
- Robustness across varied domain simulations.

CQI cannot be computed as a simple linear sum.
Component collapse in any axis degrades overall CQI.

---

# Lab Enforcement Principle

CQI measures adaptive continuity quality.

It is not a reward signal.
It is an evaluation instrument.

If the metric becomes gamed,
the lab must revise measurement before drawing conclusions.

Nomos Logica stands or falls on clean CQI measurement.
