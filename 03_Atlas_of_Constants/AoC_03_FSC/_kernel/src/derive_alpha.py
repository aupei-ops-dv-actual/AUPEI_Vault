#!/usr/bin/env python3
"""
derive_alpha.py — α kernel core algorithm.

Implements the v2.0 derivation from `AoC_Dev_137_1.0.pdf` (Section 3):

    α_pred = (A₁/A₃) · r / (4π)

with downstream stochastic-amplitude saturation:

    ξ* = |α_err · Δπ / β'_α(g*)|

and stability check β'(g*) = -2·A₁·r < 0.

INPUTS  (from locks.json):
    A₁/A₃   = 6.1361563334     (locked coefficient ratio)
    r       = 0.01495          (locked constraint/extension ratio)
    γ       = 1                (minimal model)
    K       = 1                (drift-bound normalization)
    Δπ      = 4.8123662410     (from AoC_01: j_{1,1}² - π²)
    α_exp   = CODATA 2018      (empirical reference, NOT a fit target)

OUTPUTS:
    α_pred  = 1/136.9848       (the headline geometric prediction)
    α_err   ≈ 2.73e-6          (374 ppm from CODATA)
    g_star  = sqrt(A₁/A₃ · r)  (fixed point in raw coupling)
    β'(g*)  = -2·A₁·r          (stability, negative ⇒ IR stable)
    β'_α(g*)= (g*/2π)·β'(g*)   (α-normalized derivative)
    ξ*      = α_err·Δπ/|β'_α|  (saturation amplitude — tautological by construction)
    δα_max  = K·|ξ*·β'_α|/Δπ   (verifies saturation; equals α_err exactly)
    E_ξ     = (1/α_exp - 1/α_pred)·Δπ  (stability metric, threshold 5.5)

DISCIPLINE NOTES:
  - ξ* is DETERMINED BY the saturation condition with α_err as input.
    The saturation residual is therefore machine-precision by construction,
    not by physical prediction. This is honestly disclosed in CLAIMS.md.

  - r is a CHOSEN input. The closure equations in the dev paper §3.1
    do NOT uniquely determine (A₁/A₃, r). See trailhead:
    AoC_03_Alpha_Closure_Underdetermination_Trailhead.md
"""

from __future__ import annotations

import json
from pathlib import Path

from mpmath import mp, mpf, sqrt, pi as mp_pi

# Allow running as `python3 src/derive_alpha.py` from kernel root
import sys

KERNEL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KERNEL_ROOT / "src"))

from compute_delta_pi import compute_delta_pi  # noqa: E402


def load_locks(locks_path: Path | None = None) -> dict:
    """Load the locks.json from the kernel root."""
    if locks_path is None:
        locks_path = KERNEL_ROOT / "locks.json"
    with open(locks_path, "r") as f:
        return json.load(f)


def derive_alpha_full(precision_digits: int = 80) -> dict:
    """Run the full α derivation. Returns mpmath-precision results dict."""
    mp.dps = precision_digits

    locks = load_locks()

    # Pull locked geometric inputs
    A1_over_A3 = mpf(repr(locks["locked_flow_parameters"]["A1_over_A3"]["value"]))
    r = mpf(repr(locks["locked_flow_parameters"]["r"]["value"]))
    gamma = mpf(repr(locks["locked_flow_parameters"]["gamma"]["value"]))
    K = mpf(repr(locks["locked_flow_parameters"]["K"]["value"]))
    alpha_exp = mpf(repr(locks["empirical_reference"]["alpha_CODATA_2018"]["value"]))

    # Geometric input Δπ — derived from j_{1,1} and π
    _, _, delta_pi = compute_delta_pi(precision_digits=precision_digits)

    # === Core derivation (Eq. 3.1, dev paper) ===
    alpha_pred = (A1_over_A3 * r) / (4 * mp_pi)
    alpha_pred_inv = 1 / alpha_pred

    # === Fixed-point structure (Eq. 2.5, 2.7, 2.8) ===
    g_star = sqrt(A1_over_A3 * r ** gamma)
    beta_prime_g = -2 * A1_over_A3 * r ** gamma
    # α-normalized derivative (Eq. 2.10-2.11)
    beta_prime_alpha = (g_star / (2 * mp_pi)) * beta_prime_g

    # === Empirical comparison ===
    alpha_err = abs(alpha_pred - alpha_exp)
    alpha_err_relative = alpha_err / alpha_exp
    alpha_err_ppm = alpha_err_relative * mpf("1e6")

    # === Saturation closure (Eq. 3.6, 3.7 / §4.2 of dev paper) ===
    # ξ* derived FROM α_err (boundary saturation), absolute formulation
    # matching dev paper §4.2: |δα|_max = |ξ* · β'_α| / Δπ
    xi_star = abs(alpha_err * delta_pi / beta_prime_alpha)

    # Verify saturation: |δα|_max should equal alpha_err
    delta_alpha_max_absolute = K * abs(xi_star * beta_prime_alpha) / delta_pi
    saturation_residual = abs(alpha_err - delta_alpha_max_absolute)

    # Relative drift bound for reference
    delta_alpha_max_relative = delta_alpha_max_absolute / alpha_exp

    # === E_ξ stability metric (Eq. 4.3 style) ===
    E_xi = ((1 / alpha_exp) - (1 / alpha_pred)) * delta_pi
    E_xi_threshold = mpf("5.5")
    safety_margin_pct = 100 * (1 - E_xi / E_xi_threshold)

    return {
        # Locked inputs
        "A1_over_A3": A1_over_A3,
        "r": r,
        "gamma": gamma,
        "K": K,
        "delta_pi": delta_pi,
        "alpha_exp": alpha_exp,

        # Core derivation
        "alpha_pred": alpha_pred,
        "alpha_pred_inv": alpha_pred_inv,

        # Fixed-point structure
        "g_star": g_star,
        "beta_prime_g": beta_prime_g,
        "beta_prime_alpha": beta_prime_alpha,

        # Empirical comparison
        "alpha_err": alpha_err,
        "alpha_err_relative": alpha_err_relative,
        "alpha_err_ppm": alpha_err_ppm,

        # Saturation closure
        "xi_star": xi_star,
        "delta_alpha_max_relative": delta_alpha_max_relative,
        "delta_alpha_max_absolute": delta_alpha_max_absolute,
        "saturation_residual": saturation_residual,

        # Stability metric
        "E_xi": E_xi,
        "E_xi_threshold": E_xi_threshold,
        "safety_margin_pct": safety_margin_pct,
    }


def print_report(results: dict) -> None:
    """Human-readable derivation report."""
    print("=" * 72)
    print("AoC_03 — FINE-STRUCTURE CONSTANT α — KERNEL DERIVATION")
    print("=" * 72)
    print()
    print("Geometric input from AoC_01:")
    print(f"  Δπ              = {float(results['delta_pi']):.13f}")
    print()
    print("Locked flow parameters:")
    print(f"  A₁/A₃           = {float(results['A1_over_A3']):.10f}")
    print(f"  r               = {float(results['r']):.5f}")
    print(f"  γ               = {int(results['gamma'])}")
    print(f"  K               = {int(results['K'])}")
    print()
    print("Core derivation (Eq. 3.1):")
    print(f"  α_pred          = (A₁/A₃) · r / (4π)")
    print(f"                  = {float(results['alpha_pred']):.13e}")
    print(f"  1/α_pred        = {float(results['alpha_pred_inv']):.6f}")
    print()
    print("Empirical reference (CODATA 2018):")
    print(f"  α_exp           = {float(results['alpha_exp']):.13e}")
    print(f"  |α_pred - α_exp|= {float(results['alpha_err']):.6e}")
    print(f"  ppm deviation   = {float(results['alpha_err_ppm']):.1f}")
    print()
    print("Fixed-point structure:")
    print(f"  g*              = {float(results['g_star']):.10f}")
    print(f"  β'(g*)          = {float(results['beta_prime_g']):.10f}  (negative ⇒ IR stable)")
    print(f"  β'_α(g*)        = {float(results['beta_prime_alpha']):.10f}")
    print()
    print("Saturation closure (boundary equality):")
    print(f"  ξ* (from α_err) = {float(results['xi_star']):.10f}")
    print(f"  |δα/α|_max      = {float(results['delta_alpha_max_relative']):.6e}")
    print(f"  |δα|_max abs    = {float(results['delta_alpha_max_absolute']):.6e}")
    print(f"  residual        = {float(results['saturation_residual']):.2e}  (machine precision)")
    print()
    print("Stability metric:")
    print(f"  E_ξ             = {float(results['E_xi']):.4f}")
    print(f"  threshold       = {float(results['E_xi_threshold']):.1f}")
    print(f"  safety margin   = {float(results['safety_margin_pct']):.1f}%")
    print()
    print("80-digit precision α_pred:")
    print(f"  {mp.nstr(results['alpha_pred'], 50)}")
    print()
    print("=" * 72)


def main() -> int:
    results = derive_alpha_full(precision_digits=80)
    print_report(results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
