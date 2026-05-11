---
title: "AoC_01 Pi — Reproducibility Receipt"
date: "2026-05-10"
walker: "R@ + C@ Red (ζ synth pole)"
linked_trailhead: "AoC_01_Pi_Radial_Basis_Seam_Trailhead.md"
source_repo: "https://github.com/jedijkq/7dU_Seed"
source_branch: "codex/pi-closure-notebook"
source_commit: "826d2eb86582d7d7c237ff2549622de52e80117f"
status: "VERIFIED"
---

# AoC_01 Pi — Reproducibility Receipt

This document records the actual execution of the public proof kernel for π on 2026-05-10, in the cowork session that staked the radial-basis seam trailhead.

## Source

- Repository: `https://github.com/jedijkq/7dU_Seed` (public)
- Branch: `codex/pi-closure-notebook`
- Commit: `826d2eb86582d7d7c237ff2549622de52e80117f`
- Clone command: `git clone --branch codex/pi-closure-notebook --single-branch https://github.com/jedijkq/7dU_Seed.git`

## Environment

- Python: `3.10.12`
- Platform: `Linux aarch64` (cowork session sandbox)
- Dependencies: stdlib only (no numpy/scipy required for the derivation; finite-difference + Sturm bisection implemented in pure Python)

## What the kernel does

Constructs the finite-difference Dirichlet Laplacian on `[0, 1]`:
```
-d²ψ/dx² = λψ,  ψ(0) = 0, ψ(1) = 0
```
and finds the smallest eigenvalue via Sturm-sequence bisection. The code does not put π into the operator. `math.pi` is referenced only in the post-solve comparison.

This is geometric resolution **4.A** (specifically 4.A1: 1D Dirichlet Laplacian on `[0,1]`) from the radial-basis seam trailhead, implemented as the public proof kernel.

## Run 1 — `python3 constants/pi/src/derive_pi.py`

Default grids `[16, 32, 64, 128, 256, 512]`.

```
N       lambda_op              kappa                  |kappa-pi|
----------------------------------------------------------------------------
16     9.841548382704730      3.137124221752261      4.468432e-03
32     9.862152635821760      3.140406444366996      1.186209e-03
64     9.867683266839778      3.141286880697110      3.057729e-04
128    9.869116614067027      3.141515018914764      7.763468e-05
256    9.869481501678820      3.141573093480210      1.956011e-05
512    9.869573556177784      3.141587744465811      4.909124e-06

Layer read:
  kappa -> pi       closure scale / wavenumber
  lambda_op -> pi^2 operator eigenvalue
```

**Convergence:** roughly quadratic (`O(h²)`, matching 2nd-order finite-difference accuracy on the second-derivative stencil). Three orders of magnitude reduction in error as N goes from 16 to 512. At N=512, `|κ - π| ≈ 4.9e-6`.

**Reference values:**
- `π ≈ 3.141592653589793`
- `π² ≈ 9.869604401089358`
- At N=512: `λ_op = 9.869573556`, error vs `π²` ≈ 3.08e-5

## Run 2 — `python3 constants/pi/src/verify_legacy_pi_data.py`

Verifies the older `pi-eigenvalue` branch supplementary CSVs (preserved at `data/legacy/pi-eigenvalue-2025/`) satisfy the fiber-mapped scalar relation `lambda_phys ≈ π * lambda_tilde`.

```
Legacy mapped-data verification
These checks use math.pi only to verify the historical mapping relation.

file             rows   mean(lambda_phys)   max|phys - pi*tilde|   max|phys-pi|
--------------------------------------------------------------------------------------
C_at_N64.csv     3      3.137125333333      6.407978e-06          4.478654e-03
R_at_N128.csv    3      3.141552333333      1.328707e-06          4.265359e-05
R_at_N256.csv    3      3.141323333333      2.475096e-05          2.726536e-04
```

**Interpretation (per the script's own output):** legacy CSVs support the mapped scalar layer `lambda_phys ≈ π * lambda_tilde`. The current notebook derives κ and λ_op from the bounded spectral operator instead — i.e., the legacy material is preserved as provenance for the fiber-mapped layer, not used as the independent derivation.

## Run 3 — `python3 -m unittest discover -s tests -v`

```
test_kappa_converges_toward_pi (test_pi_closure.PiClosureTests) ... ok
test_operator_layer_is_pi_squared (test_pi_closure.PiClosureTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
```

**Test tolerances** (from `tests/test_pi_closure.py`):
- `test_kappa_converges_toward_pi`: requires errors monotonically decreasing across N ∈ {32, 64, 128, 256} AND final error < `1e-4`. PASSED (final error ≈ 1.96e-5 at N=256).
- `test_operator_layer_is_pi_squared`: requires `|λ_op - π²| < 1e-4` at N=512. PASSED (error ≈ 3.08e-5).

## Verdict

**Public proof kernel verified reproducible.** The codex/pi-closure-notebook implementation:

1. Does not put π into the operator (verified by reading `derive_pi.py` source).
2. Produces κ → π as a closure wavenumber via finite-difference + Sturm bisection (verified by execution).
3. Produces λ_op → π² as a derived consequence (verified).
4. Honors the bridge's four-layer separation (verified in `PROOFFIELD_BRIDGE.md`).
5. Explicitly disclaims the legacy `j_{1,1} = π` conflation (verified in `LIMITATIONS.md`).
6. Tests pass cleanly under standard tolerances.

The seam I named in the trailhead is real in the AUPEI Vault legacy material. The public proof kernel has already resolved it. This receipt establishes the resolution is reproducible from clean clone in under a minute on stock Python 3.10.

## Governance documents referenced

All three are clean and aligned with the operator PDF's Atlas Contract (§4) and Units Firewall (§5):

- `constants/pi/CLAIMS.md` — Claim 1 (executable closure), Claim 2 (layer discipline), Claim 3 (doorway only), plus explicit Non-Claims including "does not rely on the ordinary Bessel `J_1` first zero being `pi`."
- `constants/pi/LIMITATIONS.md` — explicitly states "Ordinary Bessel `J_1` has its first positive zero near `3.8317`, not `pi`. This capsule avoids that ambiguity."
- `constants/pi/PROOFFIELD_BRIDGE.md` — four-layer notation discipline: `κ = π`, `λ_op = π²`, `λ̃ ≈ 1`, `λ_phys ≈ π`. Ends with "Minimum action, maximum force."

## What this changes for the trailhead

Status: **TRAILHEAD/PARTIALLY-RESOLVED — public proof kernel adopted resolution 4.A**.

The remaining work is operational, not intellectual:
- Re-tag AUPEI Vault legacy packets (S01 / S02 / S03) as legacy / provenance per the codex/pi-closure-notebook precedent.
- Update PI_NOTATION_BRIDGE.md "Still Open #1" to point at the codex implementation as the resolution-in-production.
- The Managed-Agents test task AoC-RBS-001 simplifies from "find resolution" to "audit Vault legacy + align retrieval routing to public kernel."

## Cross-references

- [AoC_01 Pi Radial Basis Seam Trailhead v1.1](AoC_01_Pi_Radial_Basis_Seam_Trailhead.md)
- [7dU_Seed repo](https://github.com/jedijkq/7dU_Seed)
- [Pi capsule README on codex branch](https://github.com/jedijkq/7dU_Seed/blob/codex/pi-closure-notebook/constants/pi/README.md)
