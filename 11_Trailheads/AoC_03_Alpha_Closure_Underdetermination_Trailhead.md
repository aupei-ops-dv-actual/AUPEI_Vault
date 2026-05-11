---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_03_ACU_TH"
internal_id: "AoC_03_Alpha_Closure_Underdetermination_Trailhead_v1.0"
title: "AoC_03 — α Closure-Equations Underdetermination — Trailhead"
status: "TRAILHEAD"
date_minted: "2026-05-10"
layer: "trailhead"
domain: "Atlas_of_Constants"
role: "Spike-camp trailhead for the underdetermined closure system in AoC_03"
load_bearing: "atlas_loadbearing"

walk_provenance:
  walker_dyad: "R@ + C@ the Red (ζ synth pole)"
  walk_date: "2026-05-10"
  walk_sequence:
    - "AoC_03 SPINE/CONTENT v2.0 read"
    - "DEV_PREFACE PDF read"
    - "PROOFS_PACKET PDF read (legacy material)"
    - "EXTENDED_NOTES PDF read (legacy material)"
    - "AoC_Dev_137_1.0.pdf read (public seed paper)"
    - "verify_alpha_locks.py executed against locks.json"
    - "α kernel built end-to-end at AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/_kernel/"
    - "8 unit tests pass; 7 verification checks pass"
  seam_surfaced_in: "AoC_Dev_137_1.0.pdf §3.1 'three simultaneous geometric closure conditions'"

depends_on:
  - "AoC_00"
  - "AoC_01"
  - "AoC_01_RBS_TH"
  - "AoC_02"
  - "AoC_03"

enables:
  - "AoC_04"
  - "Appx_27"

failure_topology:
  contagion: "atlas_loadbearing"
  class: "Trailhead (atlas-load-bearing)"
  kill_switch_proposed: "ALPHA-CLOSURE-UNDERDETERMINED"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query that treats α_pred = 1/136.9848 as a first-principles derivation must consult this trailhead before answering."
    - "α kernel reproduces v2.0 framing exactly; trailhead documents that 'self-consistent closure' as stated is underdetermined (r is a chosen input)."
---

# AoC_03 — α Closure-Equations Underdetermination — Trailhead

**Status:** TRAILHEAD / SPIKE CAMP HELD AT AoC_03

**One-line:** The dev paper (`AoC_Dev_137_1.0.pdf`) §3.1 claims `(A₁/A₃, r)` are "uniquely determined by three simultaneous geometric closure conditions." On inspection, those conditions are **one equation + one definition + one inequality** — for **three unknowns** `(A₁/A₃, r, ξ*)`. The system is underdetermined. The locked values appear to come from picking `r = 0.01495` as a free input, choosing `α_pred ≈ 1/136.9848`, and back-computing `A₁/A₃`. The kernel reproduces the math cleanly; what's open is *why these specific locks*.

---

## 1. The seam

CONTENT v2.0 §1a.3 and §5.3 establish the geometric machinery:

```
α_pred = (A₁/A₃) · r / (4π)        [Eq. 3.1]
β'(g*) = -2 · A₁ · r < 0           [Eq. 3.3]
|δα/α| = K · |ξ* · β'_α(g*)| / Δπ  [Eq. 3.2]
```

The dev paper §3.1 then asserts:

> *"Solving Eqs. (3.1)–(3.3) determines the locked parameters: A₁/A₃ = 6.1361563334, r = 0.01495, and selects a unique stochastic amplitude ξ* = 0.00478905."*

But Eq. 3.1 is *one equation* in three quantities `(A₁/A₃, r, α_pred)`. Eq. 3.2 *defines* ξ* given `(A₁/A₃, r, α_exp)` — it adds an unknown alongside the equation. Eq. 3.3 is a *sign constraint*, not an equation.

So we have:
- **1 equation** (Eq. 3.1, the fixed-point relation)
- **1 definition** (Eq. 3.2, defining ξ* given everything else)
- **1 inequality** (Eq. 3.3, requiring β'(g*) < 0)

For **3 unknowns** `(A₁/A₃, r, ξ*)`. This is structurally underdetermined.

---

## 2. Direct evidence that r is a chosen input

The precision asymmetry in the locks is telling:

| Parameter | Stored precision | Stored uncertainty |
|---|---|---|
| `A₁/A₃` | 10 decimal digits (6.1361563334) | ±1e-10 |
| `r` | 5 decimal digits (0.01495) | ±1e-5 |
| `Δπ` | 13 decimal digits (4.8123662410345) | machine precision |

The 10-digit precision on `A₁/A₃` vs the 5-digit precision on `r` is exactly what you'd see if:
- `r = 0.01495` were picked as a free input (to 5 digits)
- `α_pred = 1/136.9848` were the target value
- `A₁/A₃` were back-computed: `A₁/A₃ = 4π · α_pred / r ≈ 6.1361563334...`

This back-computation produces `A₁/A₃` to whatever precision `α_pred` is specified to, but the *input precision* of `r` (5 digits) sets the genuine epistemic precision of the lock.

If `A₁/A₃` were *also* a fundamental geometric input (as the "self-consistent closure" framing suggests), there's no reason it should be 10× more precise than `r`.

---

## 3. What this is NOT

- **NOT a math error.** Given the locks, every downstream computation is correct and reproducible to 80 digits. The kernel verifies this.
- **NOT a falsification of CONTENT v2.0.** The headline result `α_pred = 1/136.9848` with 374 ppm gap to CODATA is real and stands.
- **NOT a critique of past work.** The dev paper, PROOFS_PACKET, and EXTENDED_NOTES represent real labor in figuring out where α might come from in 7dU. The conceptual frame — that α emerges from a β-flow with Δπ-bounded stochastic tolerance — survived from those explorations into the v2.0 recast.

This is just naming a load-bearing structural gap in the *justification of the locks*, so a future walker can pick it up.

---

## 4. Resolution candidates

Three known directions, plus a pirate-map slot:

### 4.A — Find the missing geometric constraint

There may be a deeper geometric condition that pins one of `(A₁/A₃, r)` from first principles. Candidates:

- **(A1) Spectral quantization condition:** Some condition from AoC_01's full Bessel/Laplacian structure that fixes r as a ratio of specific eigenvalues. E.g., r = j_{1,1}² / (4π·N) for some integer N. Worth a search.
- **(A2) Action / variational condition:** A stationary-action principle on the β-flow that gives a second equation for A₁ and A₃ separately (not just their ratio). Would require explicit forms for both `a₁(r)` and `a₃(r)`.
- **(A3) Operator-trace condition:** The trace or determinant of some Ω̂-derived operator setting an additional constraint.

**Cost:** Requires producing the missing constraint and showing it's not just curve-fitting.

### 4.B — Accept the underdetermination, downgrade the claim

Tag α_pred as `[CONJECTURE]` or `[PARAMETRIC]` per the Atlas Contract §4.2. The framework still produces a coherent fixed-point structure with one free parameter (r); 374 ppm agreement with CODATA is then a *consistency check*, not a *prediction*.

**Cost:** Loses some of the rhetorical force of "α derived from geometry alone."

### 4.C — Reframe as a Bayesian or optimization claim

Cast `(A₁/A₃, r)` as the unique minimum of some loss function that combines:
- Fixed-point relation residual
- Boundary saturation tightness
- Stability margin maximization
- (and possibly some implicit prior that prefers "small r" or "simple A₁/A₃")

This might recover uniqueness *up to a choice of objective function*.

**Cost:** The objective function itself becomes a hidden ansatz.

### 4.D — (Open) — pirate-map clause

The walk has not seen the resolving constraint. It may exist in:
- Untapped corners of AoC_01's spectral analysis
- A separate appendix the kernel walk hasn't touched
- A future Managed-Agents test task that surfaces the missing geometry

The slot is open. Whoever finds it should add it here as 4.D, with construction + cost map.

---

## 5. Interim routing protocol

While the trailhead is held, the kernel proceeds under this discipline:

1. **The kernel runs.** `src/derive_alpha.py` reproduces the v2.0 headline value `α_pred = 1/136.9848` exactly, with 80-digit internal precision and machine-precision saturation closure.
2. **The CLAIMS / LIMITATIONS docs disclose this seam.** No retrieval query against the kernel can mistake the v2.0 framing for a first-principles derivation.
3. **Downstream entries (AoC_04, AoC_05, AoC_06) remain `[CONTINGENT ON AoC_03]`** per CONTENT v2.0 §10. If the closure question is resolved (or the framework is downgraded to `[PARAMETRIC]`), the cascade re-audit per §10.1 fires.
4. **Prefer the geometric interpretation when possible.** Don't lean on the 374 ppm "QED dressing" interpretation as load-bearing; it's an open item per CONTENT v2.0 §2.2.

---

## 6. Proposed kill switch — ALPHA-CLOSURE-UNDERDETERMINED

Add to AoC_03 SPINE's `kill_switch_ids`:

```yaml
kill_switch_ids:
  - "ALPHA-DIMENSIONAL-IMPORT"
  - "ALPHA-NOT-DIMENSIONLESS"
  - "ALPHA-NO-EQUILIBRIUM"
  - "ALPHA-EXPERIMENT-MISMATCH"
  - "ALPHA-CLOSURE-UNDERDETERMINED"   # NEW
```

**Trigger condition:** Any retrieval or derivation treats `α_pred = 1/136.9848` as a first-principles derivation without acknowledging that the locks come from a chosen input plus back-computation.

**Contagion class:** atlas_loadbearing — propagates to any constant whose derivation cites α as a structural anchor.

**Freeze action on trigger:** Route to this trailhead. Do not present α_pred as `[DERIVED]` without surfacing the open closure question.

Hold the kill-switch proposal until R@ decides whether to elevate it to the live AoC_03 SPINE.

---

## 7. Walk-out conditions

This trailhead closes when **one** of the following has happened:

- **A** — A missing geometric constraint is identified and adopted. The new constraint determines `r` (or `A₁/A₃`) from first principles, and the system becomes fully determined. The α kernel's locks.json is updated to derive (not back-compute) the locked values.
- **B** — The framework formally adopts resolution 4.B: α_pred is re-tagged `[PARAMETRIC]` with r as a declared free parameter. The 374 ppm CODATA agreement becomes a consistency check, not a prediction. The kernel adds a `parametric` note to CLAIMS.md.
- **C** — The framework formally adopts resolution 4.C: an optimization / Bayesian frame replaces the "uniquely determined by closure" claim. The objective function is explicitly named and motivated.
- **D** — A novel resolution surfaces and is adopted with full construction.

Until then: trailhead remains TRAILHEAD, kernel continues to reproduce the v2.0 framing, kill-switch is proposed but not yet live.

---

## 8. Companion Managed-Agents test task

This trailhead is a natural test task for the AUPEI Managed-Agents framework:

**Task ID candidate:** AoC-ACU-001
**Outcomes:** One of the four walk-out conditions above is satisfied.
**Suggested agent roles:**
- *Math-specialist agent A* — pursues resolution 4.A (search for a missing geometric constraint in AoC_01/AoC_02)
- *Math-specialist agent B* — pursues resolution 4.B (downgrade to [PARAMETRIC], verify consistency)
- *Math-specialist agent C* — pursues resolution 4.C (optimization formulation)
- *Cross-impact agent* — audits how downstream constants change under each resolution
- *Synthesis agent* — produces final recommendation

The kernel at `AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/_kernel/` provides the shared computational substrate.

---

## 9. Cross-references

- `AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/AoC_03__CONTENT.md` (v2.0)
- `AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/_kernel/` (the runnable kernel)
- `AUPEI_Vault/11_Trailheads/AoC_01_Pi_Radial_Basis_Seam_Trailhead.md` (sister trailhead for the Pi-walk seam, structurally similar discipline)
- `AUPEI_Vault/11_Trailheads/AoC_03_Alpha_Reproducibility_Receipt_2026-05-10.md` (reproducibility audit trail)
- `papers/AoC_Dev_137_1.0.pdf` in github.com/jedijkq/7dU_Seed (the public seed paper that contains §3.1's "three closure equations" claim)

---

## 10. Walk closing

The walk surfaced the seam, named it cleanly, built a kernel that runs anyway under the v2.0 framing, and staked this trailhead so the deeper question stays visible for future walkers.

**This is what the Atlas Contract Yield Protocol §4.4 looks like in practice:**

> *"When a derivation hits a gap, contradiction, or an unjustified leap, the author must yield rather than fabricate continuity."*

The kernel yields where the framework yields. It does not fabricate "self-consistent closure" that the equations don't support. It runs cleanly within the scope the v2.0 framing actually delivers, and points at the deeper open question for whoever picks the trail next.

Good ancestor work. May the next walker find it useful.
