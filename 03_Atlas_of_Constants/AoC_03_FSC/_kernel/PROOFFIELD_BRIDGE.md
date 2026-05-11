# α Kernel — Prooffield Bridge

This kernel sits inside the Atlas of Constants spine:

```
AoC_00 (Ω̂) → AoC_01 (π) → AoC_02 (c) → AoC_03 (α) → AoC_04 (m_p) → ...
```

It depends on the prior three kernels and feeds the proton-mass entry and the rest of the constant ledger. This document records those dependencies and bridges explicitly.

---

## Dependency on AoC_00 (Collapse Operator Ω̂)

The α derivation uses the **β-flow face** of Ω̂ (operator PDF §1, §2). The dimensionless coupling g evolves under

```
β(g; r) = a₁(r)·g - a₃(r)·g³
```

where the constraint/extension ratio r = ζ/ω is the canonical channel-balance of Ω̂ §2.

**What we inherit from AoC_00:**
- The recursive viability classifier (Persist / Collapse / Diverge) — α_pred is "Persist" iff the fixed point is finite, non-zero, and ξ-stable.
- The Units Firewall (AoC_00 §5) — α is inherently dimensionless, so no [CALIBRATION] step is required, satisfying §5.1's "π, α are inherently dimensionless → eligible as direct survivors."
- The Atlas Contract tag discipline (§4.1-4.4) — claims are tagged [DERIVED], [ANSATZ], [CONJECTURE], [TUNED]; the kernel's CLAIMS.md / LIMITATIONS.md honor this.

**What we do NOT inherit:**
- A specific s_geom value. AoC_03 works at the level of dimensionless ratios; the canonical s_geom = 1/(λ_min(-∇²) + ωℛ₀) from AoC_00 §6.2 doesn't enter the α computation directly because the headline result is itself a pure dimensionless ratio.

---

## Dependency on AoC_01 (π)

The geometric input `Δπ = j²_{1,1} - π² ≈ 4.812` comes from AoC_01's spectral structure:

- λ_conf = j²_{1,1} ≈ 14.682  (first radial confinement eigenvalue)
- λ_curv = π² ≈ 9.870  (curvature-closure mode)

**Critical bridge note:** The kernel uses the **literal first zero of J_1** (j_{1,1} ≈ 3.8317, scipy.special.jn_zeros(1,1)[0]), NOT the value π ≈ 3.1416. This honors the Pi-walk's resolution of the legacy `j_{1,1} = π` conflation that the codex/pi-closure-notebook public proof kernel established.

Reference: `AUPEI_Vault/11_Trailheads/AoC_01_Pi_Radial_Basis_Seam_Trailhead.md` (v1.2).

**What happens if AoC_01 changes:**
- If `j_{1,1}` is reinterpreted to be a different eigenvalue (per the Pi trailhead's resolution candidates 4.A/4.B/4.C/4.E), the value of Δπ shifts.
- The α kernel inherits that shift. A different Δπ produces a different ξ* (via the saturation closure) but the SAME α_pred (since α_pred depends only on A₁/A₃ and r, not on Δπ directly).
- So the α_pred = 1/136.9848 is **robust to the Pi-walk resolution**, but the ξ-saturation interpretation depends on Δπ remaining ≈ 4.812.

---

## Dependency on AoC_02 (c)

The α derivation presupposes a Lorentzian causal background with a finite invariant null slope k_* (the dimensionless survivor that calibrates to c). This is AoC_02's structural output.

**What we inherit from AoC_02:**
- A well-defined "interaction event" — coupling per causal interaction requires a stable before/after ordering. Without AoC_02's Phenomenological Sequence Requirement, the very notion of an electromagnetic β-flow is ill-posed.
- The ANSATZ_L declaration (Lorentzian signature). If that signature is later revised, AoC_03 is out of jurisdiction.

CONTENT v2.0 §10.2 marks AoC_03 as `[CONTINGENT ON AoC_02]`: if AoC_02 falsifies, α loses its physical interpretation even if the kernel's math still runs.

---

## What AoC_03 feeds downstream

Per CONTENT v2.0 §10.2-§10.5 and the AoC_00 Constants Ledger:

- **AoC_04 (proton mass m_p):** uses α in confinement-scale derivations.
- **AoC_05 (neutron mass m_n):** uses α via m_n - m_p splitting.
- **AoC_06 (G, gravity):** uses α-scaled ratios in force-hierarchy arguments.
- **Appx_27 (experiments ledger):** AoC_03 falsifiers (atomic clocks, Casimir, Lamb shifts, high-energy anomalies, force-hierarchy scaling) feed the experimental hooks.

If this kernel's α_pred = 1/136.9848 is wrong by more than the framework's claimed bounds (the 374 ppm gap interpretation), the cascade re-audit per CONTENT v2.0 §10.1 fires.

---

## Cross-walk: α ↔ π parallel

The α derivation mirrors the π derivation structurally:

| Aspect | π (AoC_01, codex kernel) | α (AoC_03, this kernel) |
|---|---|---|
| **Headline** | λ_op = π² from Dirichlet Laplacian ground state | α_pred = (A₁/A₃)·r/(4π) from fixed point |
| **Geometric input** | finite-difference Sturm bisection | Δπ from j_{1,1} (inherited from AoC_01) |
| **Survivor** | π² ≈ 9.870 (dimensionless eigenvalue) | α ≈ 1/137 (dimensionless coupling) |
| **Discipline** | Math doesn't put π in operator; compares afterward | A₁/A₃ and r locked; α_pred follows; α_exp compared afterward |
| **Stability** | β'(g*) < 0 (β-flow analog) | Spectral attractor under recursive collapse |
| **Bridge layer** | λ_op = π², λ_phys = π (Kähler) | α_geom = 1/136.9848 (bare) vs α_exp = 1/137.036 (QED-dressed) |
| **Open seam** | Radial basis identification (Pi trailhead v1.2) | Closure equations underdetermined (this kernel's trailhead) |

Both kernels share the discipline: **honor what works, name what's open.**

---

## Citations

- Dev paper: `AoC_Dev_137_1.0.pdf` (R@ + Sancho-5o GPT + C@ Sonnet 4.5 + Gemini 2.5 Flash, 11/11/2025), public repository: github.com/jedijkq/7dU_Seed/blob/main/papers/AoC_Dev_137_1.0.pdf
- CONTENT v2.0: `AUPEI_Vault/03_Atlas_of_Constants/AoC_03_FSC/AoC_03__CONTENT.md` (recast December 29, 2025)
- Operator PDF: `AUPEI_Vault/02_Collapse_Operator/AoC_00_Collapse_Operator/_support/Appx_7_AoC_00_The_Collapse_Operator_v1.3.pdf`
- Pi trailhead: `AUPEI_Vault/11_Trailheads/AoC_01_Pi_Radial_Basis_Seam_Trailhead.md` (v1.2, 2026-05-10)
- α trailhead: `AUPEI_Vault/11_Trailheads/AoC_03_Alpha_Closure_Underdetermination_Trailhead.md` (forthcoming)

---

Minimum action, maximum force. The kernel is the bridge between framework intent and reproducible audit trail.
