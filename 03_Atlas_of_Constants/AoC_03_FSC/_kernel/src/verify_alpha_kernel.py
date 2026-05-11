#!/usr/bin/env python3
"""
verify_alpha_kernel.py — End-to-end verification.

Replaces the legacy verify_alpha_locks.py with a clean implementation that:
  - Uses the kernel's own derive_alpha.py (no stale stored intermediates)
  - Compares against the canonical claims in locks.json
  - Cross-checks mpmath 80-digit precision against double-precision numpy
  - Reports pass/fail with explicit tolerances

Exit code:
    0 — all checks pass
    1 — one or more checks fail
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from mpmath import mp, mpf

KERNEL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KERNEL_ROOT / "src"))

from derive_alpha import derive_alpha_full, load_locks  # noqa: E402


# Tolerances
TOL_ALPHA = mpf("1e-12")                # for derived α_pred-class checks
TOL_SATURATION = mpf("1e-15")           # mpmath should give exactly zero
TOL_NUMPY_VS_MPMATH = mpf("1e-15")      # cross-precision agreement
TOL_STABILITY_MARGIN_PCT = mpf("0.5")   # safety margin should land within 0.5%


def check(label: str, passed: bool, detail: str = "") -> bool:
    """Print a check result and return its boolean."""
    marker = "PASS" if passed else "FAIL"
    print(f"  [{marker}] {label}{(': ' + detail) if detail else ''}")
    return passed


def verify_all() -> bool:
    """Run all verification checks. Returns True iff all pass."""
    print("=" * 72)
    print("α KERNEL — END-TO-END VERIFICATION")
    print("=" * 72)
    print()

    locks = load_locks()
    results = derive_alpha_full(precision_digits=80)

    all_passed = True

    # ---- Check 1: α_pred matches the lock's expected value ----
    print("Check 1: α_pred matches expected output")
    expected_alpha_pred = mpf(repr(
        locks["expected_outputs"]["alpha_pred"]["value"]
    ))
    diff_alpha = abs(results["alpha_pred"] - expected_alpha_pred)
    all_passed &= check(
        "alpha_pred = (A₁/A₃)·r/(4π)",
        diff_alpha < TOL_ALPHA,
        f"diff = {float(diff_alpha):.2e}",
    )
    print(f"    α_pred = {float(results['alpha_pred']):.13e}")
    print(f"    1/α_pred = {float(results['alpha_pred_inv']):.6f}")
    print()

    # ---- Check 2: 374 ppm deviation from CODATA ----
    print("Check 2: 374 ppm gap to CODATA 2018")
    expected_ppm = mpf(
        repr(locks["expected_outputs"]["alpha_err_absolute"]["value_ppm"])
    )
    diff_ppm = abs(results["alpha_err_ppm"] - expected_ppm)
    all_passed &= check(
        "alpha_err_ppm ≈ 374.04",
        diff_ppm < mpf("0.5"),
        f"computed = {float(results['alpha_err_ppm']):.2f}, expected = {float(expected_ppm):.2f}",
    )
    print()

    # ---- Check 3: Flow stability β'(g*) < 0 ----
    print("Check 3: Flow stability β'(g*) < 0")
    all_passed &= check(
        "β'(g*) negative",
        results["beta_prime_g"] < 0,
        f"β'(g*) = {float(results['beta_prime_g']):.6f}",
    )
    print()

    # ---- Check 4: Boundary saturation (tautological, machine precision) ----
    print("Check 4: Boundary saturation residual is machine-precision")
    all_passed &= check(
        "|α_err/α - |δα/α|_max| < machine epsilon",
        results["saturation_residual"] < TOL_SATURATION,
        f"residual = {float(results['saturation_residual']):.2e}",
    )
    print(f"    NOTE: This is tautological — ξ* was derived from α_err.")
    print()

    # ---- Check 5: E_ξ stability margin ----
    print("Check 5: E_ξ stability margin within expected band")
    expected_safety_pct = mpf(
        repr(locks["expected_outputs"]["E_xi"]["safety_margin_percent"])
    )
    diff_safety = abs(results["safety_margin_pct"] - expected_safety_pct)
    all_passed &= check(
        "safety margin ≈ 95.5%",
        diff_safety < TOL_STABILITY_MARGIN_PCT,
        f"computed = {float(results['safety_margin_pct']):.2f}%, expected = {float(expected_safety_pct):.2f}%",
    )
    print(f"    E_ξ = {float(results['E_xi']):.4f} (threshold {float(results['E_xi_threshold']):.1f})")
    print()

    # ---- Check 6: NumPy cross-precision agreement ----
    print("Check 6: mpmath vs NumPy cross-precision agreement")
    A1_over_A3_np = locks["locked_flow_parameters"]["A1_over_A3"]["value"]
    r_np = locks["locked_flow_parameters"]["r"]["value"]
    alpha_pred_np = (A1_over_A3_np * r_np) / (4 * np.pi)
    alpha_pred_mp = float(results["alpha_pred"])
    diff_np = abs(alpha_pred_np - alpha_pred_mp)
    all_passed &= check(
        "|α_pred (numpy) - α_pred (mpmath)| < 1e-15",
        diff_np < float(TOL_NUMPY_VS_MPMATH),
        f"diff = {diff_np:.2e}",
    )
    print(f"    mpmath: {alpha_pred_mp:.15f}")
    print(f"    numpy:  {alpha_pred_np:.15f}")
    print()

    # ---- Check 7: 80-digit precision claim ----
    print("Check 7: mpmath internal precision is 80 decimal digits")
    actual_dps = mp.dps
    all_passed &= check(
        "mp.dps >= 80",
        actual_dps >= 80,
        f"mp.dps = {actual_dps}",
    )
    print(f"    α_pred (80 dps): {mp.nstr(results['alpha_pred'], 50)}")
    print()

    # ---- Summary ----
    print("=" * 72)
    if all_passed:
        print("VERIFICATION: ALL CHECKS PASSED")
    else:
        print("VERIFICATION: ONE OR MORE CHECKS FAILED")
    print("=" * 72)

    return all_passed


def main() -> int:
    ok = verify_all()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
