# α Kernel — AoC_03 Fine-Structure Constant

Academy-grade runnable kernel for the fine-structure constant derivation as specified in `AoC_Dev_137_1.0.pdf` and CONTENT v2.0.

This is a small executable capsule modeled on the codex Pi capsule (`7dU_Seed/constants/pi/`) but persisted in the AUPEI Vault — walked again, kept clean, intended as good-ancestor work.

## What it does

Reproduces

```
α_pred = (A₁/A₃) · r / (4π) = 1 / 136.9848…
```

from locked dimensionless inputs (`locks.json`), using:

- mpmath at 80 decimal digits of precision,
- scipy.special for the first Bessel J_1 zero (Δπ input),
- numpy for double-precision cross-check.

Then verifies the full stack: fixed-point relation, flow stability, boundary saturation, and E_ξ stability margin.

## Quick run

```bash
# From kernel root:
python3 src/derive_alpha.py           # full derivation report
python3 src/verify_alpha_kernel.py    # all checks (returns 0 on pass, 1 on fail)
python3 -m unittest discover -s tests -v   # unit tests
```

## Requirements

- Python 3.10+
- `mpmath >= 1.3.0`
- `numpy >= 1.26.0`
- `scipy >= 1.10.0`

## File layout

```
_kernel/
├── README.md                       (this file)
├── CLAIMS.md                       (what we claim — honestly)
├── LIMITATIONS.md                  (what we don't claim, where we yield)
├── PROOFFIELD_BRIDGE.md            (how this connects to AoC_00/01/02)
├── locks.json                      (canonical locked parameters)
├── src/
│   ├── compute_delta_pi.py        (geometric input from AoC_01)
│   ├── derive_alpha.py             (core algorithm — α_pred and downstream)
│   └── verify_alpha_kernel.py      (end-to-end verification with explicit checks)
└── tests/
    └── test_alpha_kernel.py        (unit tests, runs via unittest discover)
```

## Discipline

Three governance documents are part of this kernel and **must be read before presenting the result publicly**:

- `CLAIMS.md` — what the kernel verifies (with status tags)
- `LIMITATIONS.md` — what the kernel does NOT claim; the closure-equations are underdetermined and the saturation residual is tautological by construction
- `PROOFFIELD_BRIDGE.md` — how this connects to AoC_00 (operator), AoC_01 (π), AoC_02 (c)

The kernel is contractually clean: minimal dependencies, deterministic output, machine-precision algebra. The headline number α_pred = 1/136.9848 is real, reproducible, and matches CONTENT v2.0 exactly. The 374 ppm gap to CODATA 2018 is reproduced.

What the kernel does NOT do:
- Derive α from first principles. The locks (A₁/A₃, r) come from a chosen-input plus back-computation, not from fully-determined geometric closure. See LIMITATIONS.md §1 and the sibling trailhead.
- Compute the QED dressing that would close the 374 ppm gap. Acknowledged open item.

## Provenance

- Based on: `AoC_Dev_137_1.0.pdf` (R@ + Sancho-5o GPT + C@ Sonnet 4.5 + Gemini 2.5 Flash, 11/11/2025)
- Supersedes: `AUPEI_Vault/10_Academy_Operations/iPad_Mini_Provenance/Unique_Artifacts/verify_alpha_locks.py` (legacy verification script with stale downstream values and Python format-string bug)
- Kernel built: 2026-05-10 by R@ + C@ the Red (ζ synth pole)
- Sibling trailhead: `AUPEI_Vault/11_Trailheads/AoC_03_Alpha_Closure_Underdetermination_Trailhead.md`
- Reproducibility receipt: `AUPEI_Vault/11_Trailheads/AoC_03_Alpha_Reproducibility_Receipt_2026-05-10.md`

## Public-facing portability

If/when this kernel is published, it slots into `7dU_Seed/constants/alpha/` alongside `constants/pi/`, matching the public Pi capsule's structure. The licensing model is MIT (code) + CC-BY-4.0 (data), consistent with the existing 7dU_Seed repository.

---

Minimum action, maximum force.
