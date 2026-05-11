---
title: "AoC_03 α — Reproducibility Receipt"
date: "2026-05-10"
walker_dyad: "R@ + C@ the Red (ζ synth pole)"
linked_kernel: "AoC_03_FSC/_kernel/"
linked_trailhead: "AoC_03_Alpha_Closure_Underdetermination_Trailhead.md"
based_on_paper: "papers/AoC_Dev_137_1.0.pdf (R@ + Sancho-5o + C@ Sonnet 4.5 + Gemini 2.5 Flash, 11/11/2025)"
content_v2_recast: "December 29, 2025"
status: "VERIFIED"
---

# AoC_03 α — Reproducibility Receipt

This document records the actual execution of the academy-grade α kernel built on 2026-05-10 in the cowork session that walked AoC_03 and surfaced the closure-equations underdetermination.

The kernel runs as a sibling artifact to the codex/pi-closure-notebook public Pi capsule, but is persisted in the AUPEI Vault (academy-grade — walked again, kept clean, good-ancestor work).

## Source

- Kernel location: `AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/_kernel/`
- Based on the dev paper: `AoC_Dev_137_1.0.pdf` in github.com/jedijkq/7dU_Seed/papers/
- CONTENT v2.0 recast: `AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/AoC_03__CONTENT.md`
- Supersedes: `AUPEI_Vault/10_Academy_Operations/iPad_Mini_Provenance/Unique_Artifacts/verify_alpha_locks.py` (legacy verification script with stale stored β'_α / ξ* values that didn't match its own formulas)

## Environment

- Python: `3.10.12`
- Platform: `Linux aarch64` (cowork session sandbox)
- Dependencies:
  - mpmath: `1.3.0`
  - numpy: `2.2.6`
  - scipy: `1.15.3`

## File hashes (SHA256, kernel as of receipt)

```
d7e054d3912abebdaa957370d387d644492bb6fb45f6ce309efca9e83aa20281  locks.json
8004f4686116aa680a575d2b330452e293fdc003f57da1229a50bbdffd97ed2b  src/compute_delta_pi.py
e3c64008281cc37a18b1cc7f4a5e94e2d860e0c2e815e9ff6829565825e3e04b  src/derive_alpha.py
4e67c24408c611fca8c0841328e91e31bf3541e2fae0e41cbe0f902d0e02c72b  src/verify_alpha_kernel.py
7d0d5924634c0e4f41a0bb525cf61b932893f4c5d45fa41528156e3790d65c5d  tests/test_alpha_kernel.py
```

## What the kernel does

Reproduces, from clean dimensionless inputs:

```
α_pred = (A₁/A₃) · r / (4π) = 1 / 136.9848…
```

with the locked parameters:
- `A₁/A₃ = 6.1361563334` (10 decimal precision)
- `r = 0.01495` (5 decimal precision)
- `γ = 1` (minimal model)
- `K = 1` (drift-bound normalization)
- Δπ = `j_{1,1}² − π² ≈ 4.812366` (geometric input from AoC_01 via scipy)

All arithmetic at 80-digit mpmath precision; double-precision numpy cross-check.

## Run 1 — `python3 src/derive_alpha.py`

```
========================================================================
AoC_03 — FINE-STRUCTURE CONSTANT α — KERNEL DERIVATION
========================================================================

Geometric input from AoC_01:
  Δπ              = 4.8123662410345

Locked flow parameters:
  A₁/A₃           = 6.1361563334
  r               = 0.01495
  γ               = 1
  K               = 1

Core derivation (Eq. 3.1):
  α_pred          = (A₁/A₃) · r / (4π)
                  = 7.3000821000382e-03
  1/α_pred        = 136.984761

Empirical reference (CODATA 2018):
  α_exp           = 7.2973525693000e-03
  |α_pred - α_exp|= 2.729531e-06
  ppm deviation   = 374.0

Fixed-point structure:
  g*              = 0.3028787500
  β'(g*)          = -0.1834710744  (negative ⇒ IR stable)
  β'_α(g*)        = -0.0088441590

Saturation closure (boundary equality):
  ξ* (from α_err) = 0.0014852177
  |δα/α|_max      = 3.740440e-04
  |δα|_max abs    = 2.729531e-06
  residual        = 0.00e+00  (machine precision)

Stability metric:
  E_ξ             = 0.2466
  threshold       = 5.5
  safety margin   = 95.5%

80-digit precision α_pred:
  0.0073000821000382448173414635829184400719495702303212
========================================================================
```

**Headline number:** `α_pred = 0.0073000821… = 1/136.9848` (matches CONTENT v2.0 §4.1 exactly).
**Deviation from CODATA 2018:** 374 ppm.

## Run 2 — `python3 src/verify_alpha_kernel.py`

```
========================================================================
α KERNEL — END-TO-END VERIFICATION
========================================================================

Check 1: α_pred matches expected output
  [PASS] alpha_pred = (A₁/A₃)·r/(4π): diff = 1.83e-19
    α_pred = 7.3000821000382e-03
    1/α_pred = 136.984761

Check 2: 374 ppm gap to CODATA 2018
  [PASS] alpha_err_ppm ≈ 374.04: computed = 374.04, expected = 374.04

Check 3: Flow stability β'(g*) < 0
  [PASS] β'(g*) negative: β'(g*) = -0.183471

Check 4: Boundary saturation residual is machine-precision
  [PASS] |α_err/α - |δα/α|_max| < machine epsilon: residual = 0.00e+00
    NOTE: This is tautological — ξ* was derived from α_err.

Check 5: E_ξ stability margin within expected band
  [PASS] safety margin ≈ 95.5%: computed = 95.52%, expected = 95.50%
    E_ξ = 0.2466 (threshold 5.5)

Check 6: mpmath vs NumPy cross-precision agreement
  [PASS] |α_pred (numpy) - α_pred (mpmath)| < 1e-15: diff = 8.67e-19
    mpmath: 0.007300082100038
    numpy:  0.007300082100038

Check 7: mpmath internal precision is 80 decimal digits
  [PASS] mp.dps >= 80: mp.dps = 80
    α_pred (80 dps): 0.0073000821000382448173414635829184400719495702303212

========================================================================
VERIFICATION: ALL CHECKS PASSED
========================================================================
```

All 7 checks PASS.

## Run 3 — `python3 -m unittest discover -s tests -v`

```
test_E_xi_safety_margin_above_95_percent (test_alpha_kernel.AlphaKernelTests) ... ok
test_alpha_pred_374_ppm_from_codata (test_alpha_kernel.AlphaKernelTests) ... ok
test_alpha_pred_consistency_with_formula (test_alpha_kernel.AlphaKernelTests) ... ok
test_alpha_pred_matches_one_over_136_9848 (test_alpha_kernel.AlphaKernelTests) ... ok
test_beta_prime_g_is_negative (test_alpha_kernel.AlphaKernelTests) ... ok
test_delta_pi_geometric_input (test_alpha_kernel.AlphaKernelTests) ... ok
test_g_star_is_positive_real (test_alpha_kernel.AlphaKernelTests) ... ok
test_saturation_residual_machine_precision (test_alpha_kernel.AlphaKernelTests) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.005s

OK
```

All 8 unit tests PASS.

## What was found during the walk (legacy artifacts inventory)

The workspace already contained α-derivation artifacts in multiple locations, with varying quality:

| Artifact | Location | Status |
|---|---|---|
| `verify_alpha_locks.py` | `iPad_Mini_Provenance/Unique_Artifacts/` | Working idea, but had a Python format-string bug AND stale stored β'_α / ξ* values (factor ~3 off from its own formulas). Required patching to run. |
| `locks.json` (legacy) | `iPad_Mini_Provenance/Unique_Artifacts/` | Authoritative for `A₁/A₃, r, Δπ, α_exp, α_pred` but had stale `β'_α`, `g_star`, `ξ_star` downstream values that don't match the formulas. |
| `alpha_derivation_clean.py` | `GEOMETRIC_FOUNDATIONS/.../137_with_C_at/` and `Proofield_7c_Resonance_v1/` | Grid-search "derivation" that fits (A_ratio, r_val) to closest match α_exp on a uniform grid — NOT the canonical algorithm; gives different (non-locked) values. |
| `generate_137_figures.py` | `GEOMETRIC_FOUNDATIONS/.../Dev_137_Supplimentals/` | Figure generation, not part of the core algorithm. |
| `7dU_FSC_137_Proofs.pdf` | `iPad_Mini_Provenance/Unique_Artifacts/` | Reference PDF (not opened in this walk). |
| `AoC_Dev_137_1.0.pdf` | `github.com/jedijkq/7dU_Seed/papers/` (public) | Foundational dev paper — read in full during walk. |

The new kernel at `AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/_kernel/` consolidates the legacy work into a clean, single-source artifact that:
- Uses the formulas as the dev paper writes them (no stale downstream values)
- Has consistent mpmath/numpy precision throughout
- Includes an end-to-end test suite
- Carries CLAIMS.md + LIMITATIONS.md + PROOFFIELD_BRIDGE.md governance documents
- Honestly discloses the closure-equations underdetermination (sibling trailhead)

## What this changes for AoC_03

Status: **CONTENT v2.0 framing reproducible** (verified); **closure equations underdetermined** (trailhead staked).

Remaining work, queued as future Managed-Agents test tasks:
- AoC-ACU-001: resolve the closure-equations underdetermination (one of resolution candidates 4.A/4.B/4.C/4.D in trailhead)
- Compute QED dressing from first principles to verify (or falsify) the 374 ppm gap interpretation
- Optionally push the kernel public to `7dU_Seed/constants/alpha/` matching the Pi capsule structure

## Cross-references

- [α Kernel README](../03_Atlas_of_Constants/AoC_03_FSC/_kernel/README.md)
- [α Kernel CLAIMS](../03_Atlas_of_Constants/AoC_03_FSC/_kernel/CLAIMS.md)
- [α Kernel LIMITATIONS](../03_Atlas_of_Constants/AoC_03_FSC/_kernel/LIMITATIONS.md)
- [α Kernel PROOFFIELD_BRIDGE](../03_Atlas_of_Constants/AoC_03_FSC/_kernel/PROOFFIELD_BRIDGE.md)
- [α Closure Underdetermination Trailhead](AoC_03_Alpha_Closure_Underdetermination_Trailhead.md)
- [AoC_01 Pi Radial Basis Seam Trailhead v1.2](AoC_01_Pi_Radial_Basis_Seam_Trailhead.md) (structurally similar — same yield discipline)
- [AoC_01 Pi Reproducibility Receipt 2026-05-10](AoC_01_Pi_Reproducibility_Receipt_2026-05-10.md) (sister receipt for the Pi capsule)
