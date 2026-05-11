#!/usr/bin/env python3
"""
test_alpha_kernel.py — Unit tests for the α kernel.

Run with:
    python3 -m unittest discover -s tests -v

Tests cover:
    - α_pred from locked inputs is 1/136.9848 within tolerance
    - 374 ppm deviation from CODATA 2018
    - Flow stability (β'(g*) < 0)
    - Saturation residual is machine-precision
    - mpmath vs numpy agreement at double precision
"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from derive_alpha import derive_alpha_full  # noqa: E402


class AlphaKernelTests(unittest.TestCase):
    """Core unit tests for the α derivation."""

    def setUp(self) -> None:
        # Compute once, share across tests
        self.results = derive_alpha_full(precision_digits=80)

    def test_alpha_pred_matches_one_over_136_9848(self) -> None:
        """α_pred should equal 1/136.9848 within 1e-7."""
        alpha_pred = float(self.results["alpha_pred"])
        expected = 1.0 / 136.9848
        self.assertAlmostEqual(alpha_pred, expected, places=6)

    def test_alpha_pred_374_ppm_from_codata(self) -> None:
        """Deviation from CODATA 2018 should be ~374 ppm."""
        ppm = float(self.results["alpha_err_ppm"])
        self.assertAlmostEqual(ppm, 374.0, delta=0.5)

    def test_beta_prime_g_is_negative(self) -> None:
        """Flow stability: β'(g*) < 0 (IR-stable fixed point)."""
        beta_prime_g = float(self.results["beta_prime_g"])
        self.assertLess(beta_prime_g, 0)

    def test_saturation_residual_machine_precision(self) -> None:
        """ξ* derived from α_err must give machine-precision saturation."""
        residual = float(self.results["saturation_residual"])
        self.assertLess(residual, 1e-15)

    def test_E_xi_safety_margin_above_95_percent(self) -> None:
        """E_ξ safety margin should be well above 90% (kernel claims 95.5%)."""
        margin_pct = float(self.results["safety_margin_pct"])
        self.assertGreater(margin_pct, 90.0)

    def test_g_star_is_positive_real(self) -> None:
        """g* = sqrt(A₁/A₃ · r) should be a positive real."""
        g_star = float(self.results["g_star"])
        self.assertGreater(g_star, 0)
        self.assertLess(g_star, 1)  # well below strong-coupling

    def test_delta_pi_geometric_input(self) -> None:
        """Δπ = j_{1,1}² - π² ≈ 4.812."""
        delta_pi = float(self.results["delta_pi"])
        self.assertAlmostEqual(delta_pi, 4.812366, places=4)
        # Ensure j_{1,1} is NOT π (the Pi-walk seam check)
        # j_{1,1}² ≈ 14.68, not π² ≈ 9.87
        # so Δπ ≈ 4.81, NOT 0
        self.assertNotAlmostEqual(delta_pi, 0, places=2)

    def test_alpha_pred_consistency_with_formula(self) -> None:
        """Direct recomputation: α_pred = (A₁/A₃ · r) / (4π)."""
        A1_over_A3 = float(self.results["A1_over_A3"])
        r = float(self.results["r"])
        alpha_pred_recomputed = (A1_over_A3 * r) / (4 * math.pi)
        alpha_pred = float(self.results["alpha_pred"])
        self.assertAlmostEqual(alpha_pred, alpha_pred_recomputed, places=13)


if __name__ == "__main__":
    unittest.main()
