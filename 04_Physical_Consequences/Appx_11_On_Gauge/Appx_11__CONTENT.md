# Appx_11 — On Gauge Structure (∇_μ)

## 0. Orientation

Gauge structure emerges from the requirement that local transformations preserve physical equivalence under regulated extension.

Locality under ζ-bounded curvature and ω-extension pressure requires compensatory transport structure.

This appendix formalizes that structure.

---

## 1. Global Symmetry

Let G be a compact Lie group with generators T^a:

[T^a, T^b] = i f^{abc} T^c

A field ψ transforms as:

ψ → U ψ  
U = exp(i α^a T^a)

For constant α^a, the Lagrangian:

L = ψ̄ iγ^μ ∂_μ ψ

is invariant.

This defines global symmetry.

---

## 2. Local Promotion

Promote:

α^a → α^a(x)

Ordinary derivative fails covariance:

∂_μ ψ → ∂_μ (U ψ)

To preserve locality, introduce covariant derivative:

D_μ = ∂_μ + i g A_μ^a T^a

Transformation rule:

A_μ → U A_μ U^{-1} - (i/g)(∂_μ U) U^{-1}

Local invariance is restored.

Locality forces connection structure.

---

## 3. Field Strength Tensor

Define via commutator:

[D_μ, D_ν] = i g F_μν^a T^a

Explicit form:

F_μν^a =
∂_μ A_ν^a
- ∂_ν A_μ^a
+ g f^{abc} A_μ^b A_ν^c

Non-Abelian term arises from Lie algebra closure.

For U(1), structure constants vanish.

---

## 4. Yang–Mills Action

Pure gauge Lagrangian:

L_YM = -1/4 F_μν^a F^{μν a}

Properties:

- Gauge invariant
- Second-order differential structure
- Nonlinear self-interaction (non-Abelian case)
- No explicit mass term

Explicit mass term:

m^2 A_μ A^μ

violates gauge invariance and is excluded at structural level.

Mass generation occurs downstream (Appx_16).

---

## 5. Units Firewall

Coupling g must be dimensionless at structural level.

Any insertion of unit-bearing coupling violates firewall integrity.

Running couplings are effective quantities (Appx_17).

---

## 6. Geometric Admissibility

Admissible gauge groups must:

1. Be compact.
2. Possess closed Lie algebra.
3. Preserve locality.
4. Embed within regulated extension bounds (Appx_10).
5. Avoid introduction of extra degrees of freedom beyond admissible fiber structure.

Failure triggers kill-switch conditions.

---

## 7. Spectral Structure and Mass Gap

For compact non-Abelian G:

Self-interaction term:

g f^{abc} A_μ^b A_ν^c

introduces nonlinear confinement dynamics.

Under regulated extension, this structure permits:

- Confinement behavior.
- Nonzero spectral gap in pure Yang–Mills sector.

Mass gap possibility is structural, not inserted.

This node establishes admissibility for mass-gap program.

---

## 8. Bridge to Appx_15

Standard Model gauge group:

G_SM = U(1) × SU(2) × SU(3)

must pass through this admissibility layer.

No symmetry may be assumed without satisfying local transport and closure constraints.

Gauge structure is a regulator-stabilized transport requirement.