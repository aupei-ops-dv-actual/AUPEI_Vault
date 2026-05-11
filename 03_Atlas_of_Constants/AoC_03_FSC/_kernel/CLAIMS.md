# α Kernel — Claims

## Claim 1: Executable Fixed-Point Reproduction

The kernel reproduces the v2.0 geometric prediction

```
α_pred = (A₁/A₃) · r / (4π) = 1 / 136.9848…
```

from the locked dimensionless inputs

- A₁/A₃ = 6.1361563334
- r = 0.01495
- γ = 1 (minimal model)

to **80-digit mpmath precision** with full double-precision NumPy cross-check.

Status: **Verified.** `src/derive_alpha.py` and `tests/test_alpha_kernel.py` reproduce this value end-to-end.

---

## Claim 2: 374 ppm Deviation from CODATA 2018

The absolute deviation

```
|α_pred − α_exp| ≈ 2.73 × 10⁻⁶
|α_pred − α_exp| / α_exp ≈ 374 ppm
```

is reproduced by the kernel against the CODATA 2018 reference (Tiesinga et al., Rev. Mod. Phys. 93, 025010 (2021)).

Status: **Verified.** The empirical α value enters only as a comparison reference, not as a fit target.

---

## Claim 3: Boundary Saturation as Self-Consistency

The kernel verifies that

```
|δα/α|_max ≡ K · |ξ* · β'_α(g*)| / Δπ = ε
```

where ε = |α_pred − α_exp| / α_exp is the fractional deviation, ξ* is the self-consistent stochastic amplitude, and the saturation residual is machine-precision (< 10⁻¹⁵ at 80-digit mpmath).

Status: **Verified — and disclosed as tautological by construction.** ξ* is derived FROM the saturation condition with ε as input. The match between |δα/α|_max and ε is therefore an algebraic identity, not an independent prediction. See LIMITATIONS.md.

---

## Claim 4: Flow Stability

The β-function derivative at the fixed point is negative:

```
β'(g*) = -2 · A₁ · r ≈ -0.18347
```

confirming an IR-stable fixed point (small perturbations damp toward g*).

Status: **Verified.**

---

## Claim 5: E_ξ Stability Margin

The dimensionless ξ-energy

```
E_ξ = (1/α_exp - 1/α_pred) · Δπ ≈ 0.247
```

lies well below the instability threshold of 5.5, with a **safety margin of 95.5%**.

Status: **Verified.**

---

## Claim 6: Geometric Input Consistency with AoC_01

The kernel uses Δπ = j²_{1,1} − π² ≈ 4.812, where **j_{1,1} is the literal first zero of the Bessel function J_1 (≈ 3.8317), not π**. This honors the Pi-walk's resolution of the legacy j_{1,1} = π conflation (see `AoC_01_Pi_Radial_Basis_Seam_Trailhead.md`).

Status: **Verified.** scipy.special.jn_zeros(1, 1)[0] is the source; mpmath promotes to 80-digit precision.

---

## Non-Claims

This kernel does **not** claim:

1. **First-principles derivation of α_exp.** The 374 ppm gap is interpreted in CONTENT v2.0 §2.2 as "QED dressing." Computing that dressing from first principles is an acknowledged open item, not a kernel claim.

2. **Uniqueness of (A₁/A₃, r) from closure equations.** The dev paper §3.1 claims A₁/A₃ and r are "uniquely determined by three simultaneous geometric closure conditions." On inspection, those three conditions are one equation (Eq. 3.1, the fixed-point relation) plus one definition (Eq. 3.2, the saturation defining ξ*) plus one inequality (Eq. 3.3, the stability sign constraint). For three unknowns (A₁/A₃, r, ξ*), this is underdetermined. See `AoC_03_Alpha_Closure_Underdetermination_Trailhead.md`.

3. **ξ* as an independent physical prediction.** ξ* is solved FROM the saturation condition with α_err as input. The saturation residual = 0 is therefore an algebraic identity, not an independent verification of the framework.

4. **Replacement of QED.** The kernel does not propose an alternative to QED or modify standard renormalization-group analysis. The cubic β-function is a minimal model for the purposes of identifying the fixed-point structure.

5. **Numerical agreement with the legacy `locks.json` downstream values.** The legacy file in `iPad_Mini_Provenance/Unique_Artifacts/` contains `β'_α` and `ξ*` values that differ from the kernel's formula-based recomputation by a factor of ~3. The kernel uses the formulas as written in the dev paper §2.10-2.11 and §3.2; the legacy stored values appear stale. The kernel's locks.json supersedes those.
