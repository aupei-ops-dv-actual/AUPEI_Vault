# α Kernel — Limitations

## The honest scope

This kernel reproduces, verifies, and audit-trails the **v2.0 fixed-point relation**

```
α_pred = (A₁/A₃) · r / (4π)
```

with the locked dimensionless inputs from `locks.json`. It is contractually clean as a *runnable artifact* — minimal dependencies, deterministic output, machine-precision saturation closure, end-to-end test coverage.

What it is **not**: a first-principles derivation of α from geometry alone. Several load-bearing questions remain open, and this document names them honestly so future walkers can pick them up.

---

## Limitation 1: The closure equations are underdetermined

The dev paper §3.1 names "three simultaneous geometric closure conditions" (Eqs. 3.1–3.3). On inspection these are:

- **Eq. 3.1** — fixed-point relation: `α_pred = (A₁/A₃)·r/(4π)`. This is *one equation* relating three quantities (A₁/A₃, r, α_pred).
- **Eq. 3.2** — boundary saturation: `|δα/α| = K·|ξ*·β'_α(g*)|/Δπ`. This *defines* ξ* given (A₁/A₃, r, α_exp), but adds ξ* as an unknown.
- **Eq. 3.3** — flow stability: `β'(g*) = -2·A₁·r < 0`. This is an *inequality* (sign constraint), not an equation.

For three unknowns (A₁/A₃, r, ξ*) we have **one equation + one definition + one inequality**. The system is underdetermined.

The locks A₁/A₃ = 6.1361563334 (10 decimal digits) and r = 0.01495 (5 decimal digits) appear to come from picking r as a free input, choosing α_pred ≈ 1/136.9848, and back-computing A₁/A₃ from the fixed-point relation. The precision asymmetry (10 digits vs 5 digits) is evidence of this.

**This is a structural open question, not a fatal flaw.** A complete framework would supply the missing constraint (perhaps from an additional geometric condition AoC_01 imposes on r, or from a quantization condition on A₁/A₃). The trailhead `AoC_03_Alpha_Closure_Underdetermination_Trailhead.md` documents this for a future Managed-Agents test task.

---

## Limitation 2: Boundary saturation is tautological

The saturation residual `|α_err/α - |δα/α|_max|` is machine-precision (~ 10⁻¹⁵ in float, ~ 10⁻⁵⁰ in mpmath at 80 digits). This is presented in the dev paper Figure 2 as "exact equality |α_err| = |δα|_max."

**But ξ* is derived FROM the saturation condition with α_err as input.** The kernel's `derive_alpha.py` computes:

```python
xi_star = abs(alpha_err_relative * delta_pi / beta_prime_alpha)
delta_alpha_max_relative = K * abs(xi_star * beta_prime_alpha) / delta_pi
# Substituting xi_star:
#   delta_alpha_max_relative = K * abs((alpha_err_relative * delta_pi / beta_prime_alpha) * beta_prime_alpha) / delta_pi
#                            = K * alpha_err_relative                       (K = 1)
#                            = alpha_err_relative      [exact algebraic identity]
```

So `|δα/α|_max = |α_err|/α_exp` is an algebraic identity by construction, not an independent verification.

This does not mean the framework is wrong. It means the saturation relation is *consistent* with the chosen ξ*, not that the framework *predicts* the saturation independently. A genuine independent prediction would require ξ* to come from some physical principle (e.g., a noise model derived from AoC_06 quantum-vacuum considerations) and *then* check that the saturation happens to hold.

---

## Limitation 3: The QED dressing gap is interpretive, not derived

CONTENT v2.0 §2.2 interprets the 374 ppm gap between α_pred and α_exp as "QED vacuum polarization dressing on top of the geometric baseline." The framework explicitly disclaims (§2.2 non-claim #1) that it derives the dressing from first principles:

> *"Computing that dressing from first principles is logged as an open item, not as a completed result."*

The kernel inherits this scope. The 374 ppm claim is *consistent with* a future QED-dressing computation producing exactly this shift, but the kernel does not provide that computation. Falsifier 9.1.2 in CONTENT v2.0 names this: if high-precision QED can show that the geometric-baseline-to-experimental dressing is NOT ~374 ppm, the AoC_03 bridge to physical α breaks.

---

## Limitation 4: γ = 1 is asserted, not derived

The minimal model fixes the power-law exponent γ = 1 in `a₁(r) = A₁·r^γ`. The dev paper §2.1 justifies this as "minimality and non-degeneracy" but notes that γ ≠ 1 can be absorbed into a power-law renormalization of r without changing α. So γ = 1 is a *normalization choice*, not a derived value.

This is fine for the kernel's purpose (testing the fixed-point structure), but means the model has a hidden degree of freedom that γ ≠ 1 would expose.

---

## Limitation 5: K = 1 is a minimal-model assertion

The drift-bound normalization constant K is set to 1. The dev paper §2.5 notes robustness over K ∈ [0.5, 2]. The kernel inherits this; if K is later constrained by a deeper geometric argument to a non-unity value, the saturation interpretation will scale accordingly.

---

## Limitation 6: The 80-digit precision is internal, not predictive

The mpmath 80-digit precision tracks the *internal arithmetic* of the kernel. It does **not** mean α_pred is predicted to 80 significant figures of physical accuracy. Physical accuracy is bounded by:

- The CODATA 2018 reference uncertainty (1.1 × 10⁻¹¹ on α_exp itself), and
- The 374 ppm gap interpretation (currently a conjecture, not a verified prediction).

So "α_pred to 80-digit precision" is a statement about the *computation*, not about *nature*.

---

## What WOULD close these limitations

The kernel becomes a *first-principles derivation* of α (rather than a self-consistent reproduction of a chosen value) when:

1. **An independent constraint determines r.** Some additional condition — possibly from AoC_01's spectral structure, possibly from a deeper appendix on the constraint/extension ratio's allowed values — that pins r without circular reference to α_exp.

2. **ξ* has a physical origin.** Some derivation that produces ξ* ≈ 0.00148 from independent considerations (vacuum-fluctuation amplitudes, RG-scale jitter, etc.) that the boundary saturation then verifies *post hoc*.

3. **The QED dressing is computed.** A first-principles QED calculation showing that the vacuum-polarization correction to the geometric baseline is exactly the 374 ppm shift observed.

Until those three items close, the kernel is **a clean verification of self-consistency at the v2.0 framing level**, not a derivation of α from geometry alone.

This is honest scope, in the spirit of the Atlas Contract §4.4 (Yield Protocol): "When a derivation hits a gap, contradiction, or an unjustified leap, the author must yield rather than fabricate continuity."

The kernel yields where the framework yields. It does not invent closure that isn't there.
