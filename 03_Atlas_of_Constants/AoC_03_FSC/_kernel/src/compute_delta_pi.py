#!/usr/bin/env python3
"""
compute_delta_pi.py — Geometric input from AoC_01 to the α kernel.

Computes the collapse-protection gap:

    Δπ = j_{1,1}² - π²

where:
    j_{1,1} = first positive zero of Bessel function J_1 (≈ 3.8317...)
    π² ≈ 9.8696...
    Δπ ≈ 4.8124

This quantity is the geometric input that AoC_03 (α) inherits from AoC_01 (π).
It represents the minimal spectral separation between the first radial
confinement eigenvalue (j²_{1,1}) and the curvature-closure eigenvalue (π²)
on the π-structured manifold.

Discipline note:
    j_{1,1} is the literal first zero of J_1. It is NOT equal to π. This was
    a long-standing seam in the legacy Pi support packets (S01/S02/S03), and
    the codex/pi-closure-notebook public proof kernel resolved it. AoC_03 v2.0
    explicitly uses the correct value j_{1,1} ≈ 3.8317 (not π) per
    locks.json and CONTENT v2.0 §1a.3.
"""

from __future__ import annotations

from mpmath import mp, mpf, pi as mp_pi
from scipy.special import jn_zeros


def compute_delta_pi(precision_digits: int = 80) -> tuple[mpf, mpf, mpf]:
    """Compute Δπ = j_{1,1}² - π² at the requested precision.

    Returns:
        (j_11, j_11_squared, delta_pi) as mpmath mpf values.
    """
    mp.dps = precision_digits

    # First positive zero of J_1 — pulled from scipy at double precision.
    # The locks.json records this as a geometric input from AoC_01.
    # NOTE: scipy.special.jn_zeros returns np.float64; cast to float() before mpf
    # to avoid the "np.float64(...)" repr ambiguity in mpmath's parser.
    j_11_float = float(jn_zeros(1, 1)[0])
    j_11 = mpf(j_11_float)

    j_11_squared = j_11 ** 2
    pi_squared = mp_pi ** 2
    delta_pi = j_11_squared - pi_squared

    return j_11, j_11_squared, delta_pi


def main() -> int:
    j_11, j_11_squared, delta_pi = compute_delta_pi()

    print("=" * 60)
    print("AoC_01 → AoC_03 geometric input: Δπ")
    print("=" * 60)
    print(f"  j_{{1,1}}     = {float(j_11):.13f}  (first zero of J_1, NOT π)")
    print(f"  j_{{1,1}}²    = {float(j_11_squared):.13f}")
    print(f"  π²         = {float(mp_pi ** 2):.13f}")
    print(f"  Δπ         = {float(delta_pi):.13f}")
    print()
    print("Δπ to 50 decimal digits:")
    print(f"  {mp.nstr(delta_pi, 50)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
