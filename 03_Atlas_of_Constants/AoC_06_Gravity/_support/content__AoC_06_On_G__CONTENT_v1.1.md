# AoC_06 — On G (Gravity as Coherence-Dilution Residual)

## 0. Objective

This node derives Newtonian gravitation in 7dU as:

- The unique exterior harmonic response of an ω-bounded vacuum
- To a localized ζ-confined knot on Δ3
- With zero tunable parameters

It defines a dimensionless gravitational invariant α^G
and converts it to G strictly via the Units Firewall.

---

## 1. Variational Origin of Exterior Field

Exterior domain:
Δ3 \ B_{r0}

Admissible strain functional constraints:
1. Locality
2. Quadratic first-derivative form
3. SO(3) isotropy
4. Sobolev/ω compatibility

These force the unique Dirichlet functional:

S_strain[Φ] = ∫ |∇Φ|^2 dV

Euler–Lagrange variation yields:

∇^2 Φ = 0

This is derived.
It is not assumed.

---

## 2. ζ/ω Interface Matching

Interior confinement mode fixed by:

k r0 = j_{1,1}

Interface conditions at r = r0:

Φ_ext(r0) = Φ_int(r0)
∂r Φ_ext(r0) = ∂r Φ_int(r0)

Exterior harmonic solution:

Φ_ext(r) = C / r

Matching yields identity:

r0 = - Φ_int(r0) / ∂r Φ_int(r0)

This is an over-determined consistency condition.

Failure activates kill switch.

---

## 3. Geometric Dilution

From flux conservation on Δ3:

∮_S ∇Φ · dS = constant

Thus:

∂r Φ_ext = -C / r^2

Inverse-square law emerges from:

- Variational uniqueness
- 3D geometry
- Compact interior source

No inverse-square assumption inserted.

---

## 4. 7D Einstein–Hilbert Reduction

Upstream gravitational action:

S7 = (1/2κ7) ∫ d^7x √(-g7) R7 + S_matter

Dimensional reduction yields:

G4 = κ7 / (8π λ)

where:

λ = ∫ d^3y √det(h)

Hierarchy suppression enters via 1/λ.

Scalar “strain+source” route fails because λ cancels.
EH route required.

---

## 5. Dimensionless Invariant

Define:

α^G = - r0 ∂r Φ_ext(r0)

Substitute:

α^G = (κ7 Mζ) / (8π λ r0)

This is structural result.

No free normalization allowed.

---

## 6. Units Firewall

Standard coupling:

α^G = (G m^2) / (ħ c)

Solve:

G = α^G (ħ c) / m^2

Firewall constraint:

m = µ0 (bare confinement scale)

Thus:

G = α^G (ħ c) / µ0^2

Planck mass forbidden.
Empirical tuning forbidden.

---

## 7. Hierarchy Interpretation

Gauge–gravity ratio:

α / α^G = (8π λ r0 / κ7 Mζ) α

Hierarchy localized to:

λ / κ7

Not fine-tuning.
Reduction dilution.

---

## 8. Structural Risk Surface

Load-bearing links:

1. Strain functional uniqueness
2. Interior normalization via µ0
3. Interface consistency identity
4. Firewall mass discipline
5. Finiteness of λ
6. Upstream fixation of κ7

Failure of any link invalidates AoC_06.

---

## Promotion Conditions

AoC_06 may be promoted to CANONICAL when:

- κ7 fixed without tuning
- λ regulator-geometry proven finite
- µ0 chain fully canonical
- Γ_bind epistemic status closed

Until then: TRAILHEAD_UPGRADE