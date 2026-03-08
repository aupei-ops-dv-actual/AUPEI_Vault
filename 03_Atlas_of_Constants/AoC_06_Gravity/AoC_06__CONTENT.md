# content__AoC_06_On_G__CONTENT_v1.2

**Node:** AoC_06 — On G (Gravity as Coherence-Dilution Residual)  
**Artifact:** Appx_07_AoC_06_On_G_v1.2.pdf  
**Last updated:** 2026-03-04

## Purpose (what this node does)

This node derives Newtonian gravitation within 7dU as the **unique exterior response** of an **ω-bounded vacuum** to a **localized ζ-confined knot** on the compact spatial scaffold Δ₃.

Deliverables:

- Variational derivation of the **exterior vacuum equation** (Dirichlet strain functional ⇒ ∇²Φ = 0 on Δ₃ \ B_{r0}).
- Boundary matching at r = r₀ (fixed upstream by the **j₁,₁** confinement mode) ⇒ unique exterior amplitude and **1/r²** tail.
- Definition of the **dimensionless gravitational invariant** α^G at the ζ/ω interface.
- Route A coupling closure: **7D Einstein–Hilbert reduction** ⇒ G₄ = κ₇/(8πλ) ⇒ α^G = κ₇ M_ζ /(8π λ r₀).
- **Units Firewall:** α^G → G using **only** {μ₀, ħ, c}, with explicit exclusion of Planck insertion.

No empirical tuning constants are permitted inside this node.

## Section map (v1.2)

### 0. Scope, Deliverables, and Falsifiability
- Objective: derive the 1/r² curvature tail as a mandatory geometric consequence of the ζ/ω partition on Δ₃.
- Kill switches: Laplacian assumed; non-unique strain functional; free normalization in α^G; interior normalization not fixed upstream; boundary matching inconsistency; any Planck-scale insertion or empirical tuning in Units Firewall.

### 1. Geometric Setting and Variational Origin of the Collapse Operator
- Δ₃ scaffold and ζ/ω partition.
- **Uniqueness of admissible strain functional** under locality + quadratic first-derivative form + SO(3) isotropy + ω-compatibility ⇒ Dirichlet energy.
- Euler–Lagrange ⇒ ∇²Φ = 0 on the exterior domain.

### 2. Hybrid Derivation: Boundary Matching and Geometric Dilution
- Interior mode fixed upstream by AoC_04 (j₁,₁ confinement) and μ₀ normalization.
- Continuity of Φ and ∂ₙΦ at r = r₀ ⇒ unique C and the **consistency identity**
  \[
  r_0 = -\frac{\Phi_\mathrm{int}(r_0)}{\partial_r\Phi_\mathrm{int}(r_0)}.
  \]
- Flux conservation ⇒ 1/r² curvature tail (no inverse-square assumption).

### 3. Dimensionless Invariant α^G (Route A — Einstein–Hilbert Reduction)
- Reject scalar “strain + source” coupling route due to **λ-cancellation**.
- Adopt 7D Einstein–Hilbert action with independent matter sector:
  \[
  S_7 = \frac{1}{2\kappa_7}\int d^7x\,\sqrt{-g^{(7)}}\,R^{(7)} + S_{\mathrm{matter}}^{(7)}.
  \]
- Dimensional reduction over internal 3-sector gives
  \[
  G_4 = \frac{\kappa_7}{8\pi\lambda}.
  \]
- Newtonian limit: ∇²Φ = 4πG₄ρ; vacuum gives ∇²Φ = 0.
- Flux law ⇒ C = −G₄M_ζ and
  \[
  \alpha^G = \frac{G_4 M_\zeta}{r_0} = \frac{\kappa_7 M_\zeta}{8\pi\lambda r_0}.
  \]
- Open dependencies: λ finiteness + regulator consistency; κ₇ provenance; M_ζ/Γ_bind closure; Appx_21 reduction-channel compatibility.

### 4. Units Firewall: α^G → G
- Permitted anchors: μ₀ (bare confinement scale), ħ (admitted unless derived upstream), c (AoC_02 null-slope invariant).
- Firewall mapping:
  \[
  \alpha^G \equiv \frac{G m^2}{\hbar c}
  \quad\Rightarrow\quad
  G = \alpha^G\,\frac{\hbar c}{\mu_0^2}.
  \]
- Bare vs dressed: m_p = μ₀ Γ_bind; substituting m_p directly is a **procedural** protocol violation (directionality break), not a “small numerical” issue.

### 5. Hierarchy Interpretation
- α^G ≪ α interpreted as **geometric reduction dilution**, not fine-tuning.
- Hierarchy ratio:
  \[
  \frac{\alpha}{\alpha^G} = \frac{8\pi\lambda r_0}{\kappa_7 M_\zeta}\,\alpha.
  \]
- Scope: α denotes any ζ-local gauge coupling; inter-gauge hierarchy belongs to Appx_12.
- Counterattack boundary: relocation is explanatory only if λ and κ₇ are **derived** (not fitted).

## 6. Structural Risk Summary

The audit surface of **AoC_06** reduces to **six** load-bearing links. Everything else is mechanically forced once these hold.

1. **Uniqueness of the exterior functional (Section 1).**  
   The exterior vacuum operator must arise uniquely as the Euler–Lagrange equation of the **ω-compatible**, **local**, **SO(3)-isotropic** quadratic first-derivative functional. If uniqueness fails, the operator is not forced and the tail is conditional.

2. **Interior normalization path via μ₀ (Section 2).**  
   The ζ-knot source normalization must be fixed upstream (through μ₀ and the confinement derivation chain), leaving no multiplicative freedom that could re-enter α^G.

3. **Boundary consistency identity (Section 2).**  
   The over-determined matching condition must be well-posed and satisfied at the interface:  

   \[
   r_0 \,=\, -\frac{\Phi_{\mathrm{int}}(r_0)}{\partial_r\Phi_{\mathrm{int}}(r_0)},
   \qquad \partial_r\Phi_{\mathrm{int}}(r_0)\neq 0
   \]

   for the relevant confinement mode. Failure invalidates the ζ/ω interface.

4. **Bare vs dressed mass handling (Section 4).**  
   The Units Firewall must use μ₀ as the dimensional anchor and must not silently substitute the dressed proton mass m_p without explicitly accounting for Γ_bind (epistemically bounded until closed).

5. **Finiteness and regulator-consistency of λ (Sections 3 and 6; closure node: Appx_18X).**  
   The internal volume factor λ must be finite and fixed by internal-sector structure **without coordinate-convention dependence** (compactness/periodicity or decay/localization must be **derived**, not chosen). If λ diverges or is convention-dependent, the reduction mechanism fails.

6. **κ₇ provenance and non–post-fit constraint (Sections 3 and 6; closure node: Appx_18X).**  
   The 7D coupling κ₇ must be fixed by upstream convention/geometry and must not be fitted post hoc to reproduce the observed value of G once λ is computed. κ₇ must be locked (or its normalization convention fixed) before numerical evaluation, so κ₇/λ is a **prediction** rather than a **recovery**.

