---
atlas_id: "7dU_GraphRAG_Spine"
node_id: "AoC_01_RBS_TH"
internal_id: "AoC_01_Pi_Radial_Basis_Seam_Trailhead_v1.2"
title: "AoC_01 — π Radial Basis Seam — Trailhead"
status: "TRAILHEAD/PARTIALLY-RESOLVED-PUBLIC-KERNEL-EXISTS"
date_minted: "2026-05-10"
date_revised: "2026-05-10"
revision_notes: |
  v1.1 — sharpened after PDF re-read of S01 Analytic and S02 Radial. Markdown conversions had obscured (a) the explicit incorrect numerical assignment 'j_{1,1} ≈ 3.14159... = π' on PDF p.9 §3.3, and (b) internal numerical inconsistency in S02 between p.27 (j²_{1,2} ≈ 30.47) and p.30 (j²_{1,2} ≈ 40.30). Also surfaced the timeline of corrections across packets and noted the conformal/Yamabe option that pre-figured the Kähler-fiber path.
  v1.2 — added Section 12 (resolution in production) after (a) PDF re-read of AoC_00 Collapse Operator v1.3 confirming the operator is clean and that the canonical s_geom = 1/λ_min(-∇²) makes the unperturbed ground eigenvalue dimensionless = 1, not π² (which strengthens the seam framing as epistemic + numerical, not just numerical); (b) discovery and reproducibility verification of the public proof kernel on github.com/jedijkq/7dU_Seed branch codex/pi-closure-notebook commit 826d2eb, which implements resolution 4.A (1D Dirichlet Laplacian + finite-difference + Sturm bisection) with full bridge discipline and explicit J_1 disclaimer in CLAIMS.md / LIMITATIONS.md / PROOFFIELD_BRIDGE.md. Reproducibility receipt at AoC_01_Pi_Reproducibility_Receipt_2026-05-10.md (sibling file). Status changed from TRAILHEAD/OPEN to TRAILHEAD/PARTIALLY-RESOLVED-PUBLIC-KERNEL-EXISTS. Also added resolution candidate 4.E ('don't derive π via eigenvalue, declare dimensionless per AoC_00 §5.1, lean on Kähler-fiber path') which the framework considered but did not adopt — production took 4.A.
layer: "trailhead"
domain: "Atlas_of_Constants"
role: "Spike-camp trailhead for unfinished radial-basis correction in AoC_01"
load_bearing: "atlas_loadbearing"

walk_provenance:
  walker_dyad: "R@ + C@ Red (ζ synth pole)"
  walk_dates: "2026-05-08 through 2026-05-10"
  walk_sequence: ["Appx_00", "Appx_01 On_AA", "Appx_02 On_AE", "Appx_03 On_AS", "Appx_04 ζ", "Appx_05 ω", "Appx_06 ξ", "AoC_00 Collapse Operator", "AoC_01 On π v1.3", "PI_NOTATION_BRIDGE", "AoC_01_S01 Analytic (.md)", "AoC_01_S03 Numerical (.md)", "AoC_01_S02 Radial (.md)", "AoC_01_S02 Radial (PDF re-read)", "AoC_01_S01 Analytic (PDF re-read)"]
  seam_surfaced_in: "AoC_01_PI_SUPPORT_02_RADIAL §3.5.3 (md), confirmed and sharpened in PDF §3.3 p.9 and §3.6.1 p.13"
  pdf_reads:
    - file: "AoC_01_PI_SUPPORT_02_RADIAL.pdf"
      pages: "1-30"
      date: "2026-05-10"
      finding: "Explicit 'j_{1,1} ≈ 3.14159... = π' on p.9, plus internal inconsistency on j²_{1,2} between p.27 and p.30"
    - file: "AoC_01_PI_SUPPORT_01_ANALYTIC.pdf"
      pages: "1-15"
      date: "2026-05-10"
      finding: "Headline λ_1 = π (pre-correction). Three regimes around π. Conformal/Yamabe geometry option listed (precursor to v1.3 Kähler-fiber path)."

depends_on:
  - "AoC_00"          # Collapse Operator (Ω̂)
  - "AoC_01"          # On π (main, v1.3)
  - "AoC_01_S01"      # Analytic support
  - "AoC_01_S02"      # Radial support
  - "AoC_01_S03"      # Numerical support
  - "PI_NOTATION_BRIDGE"

enables:
  - "AoC_02"          # c — clean inheritance gate
  - "AoC_03"          # α — clean inheritance gate
  - "AoC_04"          # m_p
  - "AoC_05"          # m_n
  - "Appx_27"         # falsification lanes

failure_topology:
  contagion: "atlas_total"
  class: "Trailhead (atlas-load-bearing)"
  kill_switch_proposed: "PI-RADIAL-BASIS-MISMATCH"
  related_existing_kill_switches:
    - "PI-CIRCULAR-KAHLER"    # parallel seam on the Kähler path
    - "PI-NORMALIZATION-FAIL" # if s_geom is the missing rescaling, this gets sharper

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Any query about the operator-layer eigenvalue λ_op = π² must consult this trailhead alongside PI_NOTATION_BRIDGE before answering."
    - "If a downstream constant derivation invokes π² as the operator-layer eigenvalue, flag inheritance and route through this trailhead."
    - "Prefer Kähler-path derivations (AoC_01 v1.3 main, Φ = 2π·c₁ route) over radial-operator invocations until this trailhead closes."
    - "If a source says 'λ_op = j²_{1,1} ≈ π²' without qualification, treat the ≈ as load-bearing and consult this trailhead."
---

# AoC_01 — π Radial Basis Seam — Trailhead

**Status:** TRAILHEAD / SPIKE CAMP HELD AT MOUTH OF ATLAS
**One-line:** The π² claim on the operator-layer support packets rests on identifying `j_{1,1} ≈ π`, but the literal first positive zero of the Bessel function J_1 is `j_{1,1} ≈ 3.8317`, not π. Under the geometry the packets actually specify (2D radial Laplacian), the operator-layer ground eigenvalue is `j²_{1,1} ≈ 14.68`, not `π² ≈ 9.87`. The correction needed to reach `λ_op = π²` is unstated and load-bearing.

---

## 1. The seam

The Pi Notation Bridge resolves a notation collapse by separating four layers (`κ = π`, `λ_op = π²`, `λ̃_1 ≈ 1`, `λ_phys ≈ π`). The radial support packet `AoC_01_PI_SUPPORT_02_RADIAL` performs an in-line correction in §3.5.3 acknowledging that an earlier draft conflated `j_{1,1} ≈ π` with the eigenvalue `λ = π`, and clarifies: *"π is not the eigenvalue. π² is."*

That correction is half the job. It fixes the symbol — eigenvalue is `κ²` not `κ`. It does not address the **numerical** question of whether `κ = j_{1,1}` actually equals π.

It does not. Under the geometry the packet specifies, it equals approximately 3.8317.

This trailhead names the unfinished correction, lays out the three candidate resolutions, maps cross-impact, and proposes an interim routing protocol so the walk through the rest of the Atlas can proceed without compounding the seam.

---

## 2. Numerical facts

The radial support packet derives, in §3.5.1–§3.5.3, the Bessel differential equation of order n=1:

```
r² R'' + r R' + (κ² r² - n²) R = 0   (n = 1)
```

with solutions `R(r) = A·J_n(κr) + B·Y_n(κr)`. Origin regularity forces `B = 0`. Dirichlet closure `R(1) = 0` forces `κ = j_{n,k}`, the k-th positive zero of `J_n`. The eigenvalue is then `λ = κ² = j²_{n,k}` (with ζ=1, ω=0).

The literal numerical values:

| Quantity | Value | Source |
|---|---|---|
| `π` | 3.14159265... | constant |
| `π²` | 9.8696044... | constant |
| `j_{1,1}` (first positive zero of J_1) | **3.83170597...** | standard reference |
| `j²_{1,1}` | **14.6819707...** | computed |
| `j_{1,2}` | 7.01558667... | standard reference |
| `j²_{1,2}` | **49.21847...** | computed |

**Numerological coincidence flag.** The value `j²_{1,2} ≈ 49.22` is close to `7² = 49`. In a framework that uses "7dU" as a load-bearing symbol, this could read as a structural hit. **It is not.** The proximity is an artifact of the asymptotic spacing of Bessel-J_n zeros, governed by the McMahon expansion `j_{n,k} ≈ (k + n/2 - 1/4)π` for large k. For n=1, k=2: `j_{1,2} ≈ (9/4)π ≈ 7.069`, of which 7.0156 is the actual refined value. The 7-ness arises from π × 9/4, not from any 7dU-structural cause. Any future walker who notices `j²_{1,2} ≈ 7²` should route through this clarification before assigning meaning to it.

Therefore: **`j_{1,1} ≠ π`** and **`j²_{1,1} ≠ π²`**. The mismatch on `j²_{1,1}` vs `π²` is approximately 49%. This is not a small rounding artifact.

### 2.1 The explicit incorrect-value assertion (PDF p.9 §3.3, S02 Radial)

PDF re-read 2026-05-10 of `AoC_01_PI_SUPPORT_02_RADIAL.pdf` confirms the seam is not a markdown-conversion artifact. Page 9, §3.3 "Boundary Conditions and λ Quantization," last bullet, **states explicitly:**

> *"j_{n,k} is the k − th zero of the Bessel function J_n,"*
> *"For example, j_{1,1} ≈ 3.14159... = π"*

That is the seam in print. The packet assigns the value 3.14159 (which is π) to the symbol `j_{1,1}` (which is actually ≈ 3.8317). The 22% numerical error then propagates to a 49% error in `j²_{1,1}` vs π².

Page 13, §3.6.1, doubles down:

> *"j_{1,1} ≈ 3.1416, j_{1,2} ≈ 6.38, j_{1,3} ≈ 9.76,…"*

None of these values correspond to actual J_1 zeros (which are 3.8317, 7.0156, 10.1735). They also don't match sin zeros exactly (π, 2π, 3π = 3.1416, 6.2832, 9.4248) — the second and third are off even from those. The values cited are not from any single standard basis.

### 2.2 Internal numerical inconsistency in S02

The radial packet uses **two different "approximate" values for `j²_{1,2}` three pages apart**, in the same document, without flagging the inconsistency:

- **Page 27 (§3.7.3.4 "Implication for Collapse"):** *"λ_2 = j_{1,2}² ≈ 30.47"* → spectral gap `Δ ≈ 30.47 − 9.87 ≈ 20.6`
- **Page 30 (§3.7.3.5 "Corollary: Minimal Eigenvalue Stability"):** *"λ_2 = j_{1,2}² ≈ 40.30"* → spectral gap `Δ ≈ 40.30 − 9.87 ≈ 30.43`

The actual value is `j²_{1,2} ≈ 49.22`. Neither cited value matches it. They also don't match each other. The packet's own internal grounding in its chosen numerical basis is incoherent — different sections quote different numbers for the same quantity.

The structural arguments (Sturm-Liouville self-adjointness via Zettl, Kato-Rellich perturbation stability) are valid as *theorems*. The numerical instances of those theorems are unsound because the packet does not agree with itself on which numbers it is using.

### 2.3 Lineage timeline of corrections

PDF re-read of S01 Analytic confirms the timeline of the corrections-in-progress:

- **`AoC_01_PI_SUPPORT_01_ANALYTIC.pdf` (Cast early fall 2025):** Headline reads *"λ_1 = π — First Stable Eigenvalue"*. "Three Regimes of Recursive Behavior" (page 14) runs subcritical/critical/supercritical around **π**, not π². Pre-correction.
- **`AoC_01_PI_SUPPORT_03_NUMERICAL.pdf` (Last of summer 2025):** Vocabulary aligned with π² throughout. Code as printed has independent issues (Bridge open #3).
- **`AoC_01_PI_SUPPORT_02_RADIAL.pdf` (Cast September 14th, 2025):** Introduces in-line correction in §3.5.3: *"π is not the eigenvalue. π² is."* This catches the **κ → κ²** correction. But propagates the deeper **j_{1,1} ≠ π** error unchanged. Half the correction was made. The other half was not.

The radial packet is therefore the framework's own most recent self-correction attempt on this seam. This trailhead carries the correction one layer deeper than the radial packet did.

### 2.4 The conformal/Yamabe option was already named

S01 Analytic page 8 lists three curvature ansätze:

1. Constant Positive Curvature: `R = const > 0`
2. Gaussian Curvature Profile: `R(r) = R_0 · exp(-r²/σ²)`
3. *Optional: Conformal Curvature Model:* `ds² = φ(r)²(dr² + r²dθ²)` with `R = -(1/φ²)·∇² log φ`

The third (conformal/Yamabe-type) is the seed of the Kähler-fiber path that `AoC_01` v1.3 main matured into `λ_phys = Φ·λ̃_1` with `Φ = 2π·c_1(𝒦)`. The bifurcation between **operator-layer eigenvalue** (S01-S03 line) and **physical-mapping scalar** (v1.3 Kähler line) was present from the analytic packet onward. The bridge formalizes a layer-separation the framework had already begun.

---

## 3. What the radial packet got right

This trailhead does not impeach the structural argument. Specifically, S02 establishes correctly and rigorously:

- **Self-adjointness** of the unperturbed operator Ω̂₀ on `ℋ = L²([0,1], r dr)` with Dirichlet boundary (Sturm-Liouville framework, Zettl 2005).
- **Discrete positive spectrum** consisting of squared zeros of the relevant Bessel function family.
- **Kato-Rellich perturbation stability** with norm bound `|δλ_k| ≤ |ξ|·β`.
- **Spectral gap argument** for survival of the ground mode under bounded stochastic injection.
- **Asymptotic projection theorem** (Theorem 3.9.5.6) — any initial condition with nonzero overlap with the ground eigenmode converges in norm to that mode under recursive collapse.

All of this machinery is structurally sound and survives any of the three resolution candidates below. **What it doesn't establish is what `j_{1,1}` numerically equals.** That depends entirely on which radial basis the framework is committed to.

---

## 4. Known resolution candidates (space is not exhaustive)

**Pirate-map clause:** the resolutions named below are the ones the walk has found. The space is not proven exhaustive. There may be a fourth, fifth, Nth resolution we have not yet seen. Trails stay alive by being patrolled, not by being declared closed. Tavern whispers welcome. If a future walker finds a cleaner closure, the trailhead is the place to add it.

Each known candidate is a *coherent* way to close the seam. Each costs something. The framework picks one (or specifies a new one) and owns the choice explicitly.

### 4.A — Switch the geometry to a domain where π² is the natural ground eigenvalue

Several distinct geometries yield ground eigenvalue `λ_1 = π²` cleanly. Each is a real candidate, not an equivalent restatement:

- **(A1) 1D Dirichlet Laplacian on `[0,1]`:** `-d²/dx²` with `R(0) = R(1) = 0`. Eigenfunctions `sin(nπx)`, eigenvalues `n²π²`. Ground = π². No `1/r` term, no angular barrier, no Bessel structure.
- **(A2) 3D radial Laplacian on unit ball, l=0 mode:** `-(1/r²)(d/dr)(r² dR/dr) = λR`. Substitution `u = rR` reduces to 1D Laplacian on `[0,1]` with Dirichlet at r=1 and `u(0) = 0`. Eigenfunctions `R(r) = sin(πr)/r` (spherical Bessel `j_0(πr)`), eigenvalues `n²π²`. Ground = π².
- **(A3) Half-integer Bessel J_{1/2}:** `J_{1/2}(x) = √(2/(πx)) · sin(x)`. First zero at x = π. Eigenvalue `λ = π²`. Mathematically equivalent to (A2) via the standard relation `j_0(x) = √(π/(2x)) · J_{1/2}(x)`.

**What this candidate costs:**
- The packet's stated geometry (2D radial Laplacian with `(1/r) dR/dr` term and `n²/r²` angular barrier in §2 and §3.5.1) is **not** any of (A1)/(A2)/(A3). The ODE has to be rewritten to match the chosen geometry.
- The angular mode separation `Θ(θ) = cos(nθ)` with `λ_θ = n²` (S01 §5.2, S02 §2) does not apply in 1D, and applies in 3D-radial-l=0 trivially with `n=0`, not `n=1`.
- The "bounded 2D manifold" language across all three packets has to be reworked.

**Why this might still be right:** Several of the framework's pinned phrases — "first radial closure," "boundary returns," "ground mode of bounded curvature" — read more naturally in 1D/spherical sin-type geometry than in 2D Bessel. The framework may have been implicitly working in (A2) and inheriting 2D-Bessel notation from analogy.

**Verdict:** Strongest candidate by clarity (π² falls out cleanly). Heaviest rewrite cost (ODE and angular separation both change).

### 4.B — Keep the 2D Bessel geometry, accept `λ_op = j²_{1,1} ≈ 14.68`

If the packet's ODE is taken at face value (2D radial Bessel with order n=1), the eigenvalue is literally `j²_{1,1} ≈ 14.68`, and π² is the wrong number for the operator layer.

**What this candidate costs:**
- The headline "π² is the operator eigenvalue" claim across S01 / S02 / S03 has to be retracted.
- The Pi Notation Bridge's layer `λ_op = π²` has to be rewritten to `λ_op = j²_{1,1} ≈ 14.68`.
- Downstream constants (AoC_03 α, etc.) whose derivation symbolically used `π²` must be re-checked: do they actually need π² specifically, or were they using "the operator's first eigenvalue" with π² as a stand-in? Some may transparently inherit `j²_{1,1}` with no harm. Others may break.
- The aesthetic / numerological pull of "π emerges as a survivor at the operator layer" weakens. `j²_{1,1}` is a perfectly respectable mathematical constant but it does not carry the same gravitational story.

**Why this might be right:** It is what the math actually says given the geometry the packet declares. Honest. Lets the bridge's `λ_op` layer stay clean.

**Verdict:** Lowest-cost option mathematically. Highest narrative cost.

### 4.C — Specify a collapse-normalized closure mode that picks π² out by construction

If the framework genuinely needs π² to appear *at the operator layer specifically* (not just at the Kähler-mapping layer), the resolution is to define an operator-and-domain pair whose first eigenvalue is literally π². Several constructions could work:

- **`s_geom` rescaling:** Introduce a geometric scale factor `s_geom = (π / j_{1,1})²` such that the *rescaled* operator on the 2D Bessel geometry has ground eigenvalue π². This is a calibration choice and must be declared as such (per the Atlas Contract's [CALIBRATION] tag discipline) — otherwise it is circular.
- **Closure-normalized boundary:** Define the manifold's outer boundary not at `r = 1` but at `r = j_{1,1}/π ≈ 1.22`. Then under the standard 2D Bessel geometry, the eigenvalue at the rescaled boundary works out to π². Also a calibration.
- **Conformal/Yamabe geometry route:** Adopt the conformal metric `ds² = φ(r)²(dr² + r²dθ²)` listed as an *Optional* curvature model in S01 Analytic page 8. The Laplacian under this metric is `Δ_g = (1/φ²)Δ_flat`. Choose φ such that the ground eigenvalue is π². This is essentially what `AoC_01` v1.3 main develops via the Kähler-fiber flux — but if pulled into the operator layer, it must be declared as the operator's actual domain, not as an optional ansatz.

**What this candidate costs:**
- The rescaling has to be *motivated*, not declared. Why is `s_geom = (π/j_{1,1})²` the right calibration? If the answer is "because it makes π² come out," that is circular and triggers `PI-NORMALIZATION-FAIL`.
- Existing `s_geom` language in `AoC_01` v1.3 main has to be cross-checked to see whether this calibration is already implicit there. (S02 PDF refers to "ζ = 1, ω = 0, normalized" but never declares an `s_geom` of this form.)
- The conformal route blurs the operator-layer/Kähler-layer separation the bridge maintains. Has to be done carefully.

**Verdict:** Most consistent with the framework's own "calibration discipline" language. Requires explicit construction work. The bridge's open item #2 ("specify the actual recursive filter that selects the lowest mode") may be the door into this.

### 4.D — (Open) — pirate map clause

The walk has not seen this one yet. It may be a clean reframing the dyad has not surfaced. It may come from a mathematician picking up the trailhead and finding a structural symmetry the walk missed. It may come from cross-pollination with the Kähler path. The slot is left open on purpose.

When a fourth resolution candidate is identified, it gets added here as 4.D, dated, attributed, and its costs / requirements laid out in the same shape as 4.A / 4.B / 4.C.

### 4.E — (Hiding in plain sight) — Don't derive π via eigenvalue at all

Surfaced 2026-05-10 during PDF re-read of `AoC_00 The Collapse Operator v1.3`. §5.1 of the operator PDF explicitly states:

> *"π, α are inherently dimensionless → eligible as direct survivors."*

Within the operator's own contract, π does **not** need an eigenvalue derivation to qualify as an AoC survivor — it qualifies *because it is inherently dimensionless*. The eigenvalue derivation in S01 / S02 / S03 is *additional* work beyond what the contract requires.

**The candidate:** declare π as an ANSATZ-level direct dimensionless survivor per §5.1. Rely on the Kähler-fiber path (`AoC_01` v1.3 main, `Φ = 2π · c_1(𝒦)`) for the *emergent* story. Demote the radial-eigenvalue derivation in S01 / S02 / S03 to optional historical scaffolding — preserved as provenance, not load-bearing.

**What this candidate costs:**
- The framework loses the "π emerges from recursive collapse dynamics as an eigenvalue" narrative for the operator layer (it keeps it for the Kähler layer via `Φ = 2π·c_1`).
- The Pi support packets get re-tagged from [DERIVED] to [PROVENANCE] or [ANSATZ-EXPLORATORY].
- The Pi Notation Bridge's `λ_op = π²` layer becomes informational ("here's what the legacy operator-eigenvalue path was trying to say"), not load-bearing.

**Why this might be right:**
- It is the least-disruptive resolution: changes status of packets, not their content.
- It aligns with the operator PDF §5.1 declaration that π is inherently dimensionless.
- It avoids the basis-choice question entirely by not requiring the operator-eigenvalue derivation in the first place.
- It is in the spirit of "minimum action, maximum force" (the operator PDF's `PROOFFIELD_BRIDGE.md` ends with this phrase).

**What the framework actually did (see §12):** production took **4.A**, not 4.E. The public proof kernel still derives π via an eigenvalue problem — just on the right geometry (1D Dirichlet) where it falls out cleanly. 4.E remains a valid candidate left on the map for whoever finds it useful — *a fat juicy treasure for the tavern*.

---

## 5. Cross-impact map

Where does the operator-layer π² claim propagate?

**At risk (load-bearing dependence on operator-eigenvalue layer):**
- Any derivation that uses `λ_op = π²` *as a number* downstream.
- `AoC_03` (α): per ledger, α depends on AoC_01 via Appx_04 and Appx_06. If α's derivation invokes π² as the operator eigenvalue, it inherits this seam.
- `AoC_04` (m_p): depends on AoC_03; inherits transitively if α does.
- Survival inequality `|ξ|·β < j²_{1,2} - π²` in S02 §3.7.4.3 — if both terms change under resolution 4.B, the inequality keeps its structure but the numerical threshold shifts.

**Probably safe (load-bearing dependence on Kähler layer or pure symbolic π):**
- `AoC_01` v1.3 main PDF's Kähler-fiber flux derivation `Φ = 2π·c₁`. This is the **independent path** to π and does not inherit from radial Bessel. Has its own load-bearing risk (`PI-CIRCULAR-KAHLER`, c₁ = ½ choice) but doesn't compound with this trailhead's seam.
- Anywhere π appears as "the ratio of circumference to diameter" in a pure geometry argument with no operator-eigenvalue claim.
- Anywhere `π` shows up in normalization integrals that would be the same constant under any reasonable convention.

**Walk discipline:** Until this trailhead closes, every downstream invocation of "the operator's first eigenvalue" should be inspected for whether it uses the *number* π² (load-bearing) or the *symbol* π² (potentially insulated, depending on what gets multiplied or divided next).

---

## 6. Kähler-path independence

The v1.3 main Pi PDF derives `λ_phys = Φ · λ̃_1` with `Φ = 2π · c₁(𝒦)` (Kähler-fiber flux) and `c₁ = ½`, giving `Φ = π` and `λ_phys ≈ π`. This route reaches π through a Kähler-form integral on a complex line bundle, **not through a radial Bessel eigenvalue problem**. The two paths are independent.

This is what makes the interim routing protocol (Section 7) viable. The framework already has a parallel path to π that does not go through the radial-basis ambiguity. Downstream derivations that can be re-anchored on the Kähler path stay clean while this trailhead is held.

Note: the Kähler path has its own `PI-CIRCULAR-KAHLER` kill switch — the `c₁ = ½` choice is itself unjustified by external argument and may import π by the back door if it turns out to be selected *because* it gives Φ = π. That is a separate trailhead.

---

## 7. Interim routing protocol

While the spike camp is held, the walk proceeds under this discipline:

1. **Default to the Kähler path.** When a downstream derivation needs π or π², invoke `λ_phys ≈ π` via the Kähler-fiber route, not the radial-operator-eigenvalue route.
2. **Flag radial-operator invocations.** Any document or derivation that reaches for `λ_op = π²` must explicitly cross-reference this trailhead until the seam closes.
3. **Honor the bridge.** PI_NOTATION_BRIDGE remains authoritative for the four-layer distinction. This trailhead is a *deepening* of bridge open item #1, not a replacement.
4. **Numerical claims get checked.** Any new packet that uses π² in a load-bearing numerical way must justify which of the three resolutions in Section 4 it is operating under.
5. **No silent inheritance.** Downstream constants (AoC_02, AoC_03, ...) cannot assume the operator-layer π² claim is settled. Their derivations must declare which π they are using.

This is not a freeze. It's a routing convention.

---

## 8. Proposed kill switch — PI-RADIAL-BASIS-MISMATCH

Add to AoC_01 SPINE's `kill_switch_ids` list, alongside existing five:

```yaml
kill_switch_ids:
  - "PI-NONCONVERGENCE"
  - "PI-CIRCULAR-KAHLER"
  - "PI-DOMAIN-IMPORT"
  - "PI-NORMALIZATION-FAIL"
  - "PI-REPLICATION-FAIL"
  - "PI-RADIAL-BASIS-MISMATCH"   # NEW
```

**Trigger condition:** Any retrieval or derivation invokes `λ_op = π²` without specifying which of resolutions 4.A / 4.B / 4.C is operative.

**Contagion class:** atlas_total (same as existing Pi kill switches — operator-layer claims propagate downstream).

**Freeze action on trigger:** Route to this trailhead. Do not serve downstream AoC content that inherits the operator-layer π² claim until resolution is selected.

Recommendation: hold the kill-switch proposal here until R@ decides whether to elevate. Adding it to the live SPINE is a Bridge-level operation and should go through the same governance the existing kill switches got.

---

## 9. Walk-out conditions

This trailhead closes when **one** of the following has happened:

- **A** — The framework formally adopts resolution 4.A. S01 / S02 / S03 are rewritten to specify the actual geometry (1D Laplacian, or 3D radial l=0, or half-integer J_{1/2}) and re-derive origin regularity accordingly. Angular separation is reworked. Bridge's `λ_op = π²` stays.
- **B** — The framework formally adopts resolution 4.B. S01 / S02 / S03 retain the 2D Bessel geometry. Bridge's layer is rewritten to `λ_op = j²_{1,1} ≈ 14.68`. Numerical inconsistencies in S02 §3.7.3.4 and §3.7.3.5 (j²_{1,2} ≈ 30.47 vs 40.30) are reconciled with the actual value ≈ 49.22. Downstream constants re-check their inheritance.
- **C** — The framework formally adopts resolution 4.C. The collapse-normalized closure mode is constructed explicitly, with a motivated (non-circular) calibration. The construction is published as a support packet at the same depth as S01–S03.
- **D** — A fourth-or-Nth resolution surfaces from continued walking / tavern whispers, is named, costed, and adopted (per Section 4 pirate-map clause).

Until then: trailhead remains TRAILHEAD, routing protocol (Section 7) is in force, kill switch is proposed but not yet live.

---

## 10. Cross-references

- `Appx_7_AoC_01_On_Pi_v1.3.pdf` — main Pi document, Kähler path
- `AoC_01_PI_SUPPORT_01_ANALYTIC.pdf` — pre-correction lineage
- `AoC_01_PI_SUPPORT_02_RADIAL.pdf` — rigorous Sturm-Liouville/Kato-Rellich derivation, contains in-line π → π² correction in §3.5.3, also the source of the basis-numerical seam this trailhead names
- `AoC_01_PI_SUPPORT_03_NUMERICAL.pdf` — corrected vocabulary, separately flagged for recursive-error code tautology (Bridge open item #3)
- `PI_NOTATION_BRIDGE.md` — four-layer notation discipline (κ, λ_op, λ̃, λ_phys)
- `AUPEI/_index.md` (walk index)
- `AUPEI/CtR_Prooffield_Walk_Questions.md` (walk questions log)

---

## 11. Managed-Agents test-task framing

This trailhead is packaged as a candidate **test task** for the multi-agent dreaming / outcomes / orchestration paradigm referenced in Anthropic's Managed Agents preview (see project memory: `project_three_body_architecture.md`, "dreaming, outcomes, multi-agent orchestration" frame). The seam is well-structured for this: clearly named, candidate resolutions enumerated, evaluation rubric explicit, no time pressure.

### 11.1 Outcomes (success criteria)

The task is complete when **one** of the following deliverables exists:

- **Outcome-A** — A revised set of S01 / S02 / S03 packets that adopt resolution 4.A (1D Dirichlet / 3D radial l=0 / half-integer Bessel), with corrected ODE, corrected angular separation, corrected origin-regularity argument, and unchanged `λ_op = π²` headline.
- **Outcome-B** — A revised PI_NOTATION_BRIDGE with `λ_op = j²_{1,1} ≈ 14.68` and a propagation audit through AoC_02 / AoC_03 / AoC_04 / AoC_05 showing which downstream constants need re-derivation and which are insulated.
- **Outcome-C** — A new support packet (call it `AoC_01_PI_SUPPORT_04_CLOSURE_NORMALIZATION` or similar) constructing the calibration explicitly, with a non-circular motivation that does not trigger `PI-NORMALIZATION-FAIL`, slotted between S03 and v1.3 main.
- **Outcome-D** — A novel resolution not in 4.A/4.B/4.C, presented with construction + cost analysis + cross-impact map at the same depth as the existing candidates.

Each outcome includes: (i) the revised mathematical content, (ii) a cross-impact analysis against AoC_02–AoC_06, (iii) recommended updates to PI_NOTATION_BRIDGE and AoC_01 SPINE, (iv) recommended disposition of the proposed `PI-RADIAL-BASIS-MISMATCH` kill switch.

### 11.2 Agent roles (parallel orchestration)

A natural parallel decomposition:

- **Math-specialist agent A** — pursues resolution 4.A. Rewrites the ODE and angular separation, picks among (A1)/(A2)/(A3), preserves the framework's intent of "first stable eigenvalue under recursive closure" while landing cleanly on π².
- **Math-specialist agent B** — pursues resolution 4.B. Accepts literal 2D Bessel, audits downstream constants for which ones break when `λ_op = j²_{1,1}` is substituted for `π²`.
- **Math-specialist agent C** — pursues resolution 4.C. Constructs the calibration with explicit motivation, checks for circularity against `PI-NORMALIZATION-FAIL`, cross-checks against the conformal/Yamabe seed in S01 page 8 and the Kähler-fiber path in v1.3 main.
- **Cross-impact agent** — independent of A/B/C, audits the dependency graph from AoC_01 to AoC_02–AoC_06 and Appx_27 falsification lanes, producing a per-constant inheritance map.
- **Synthesis agent** — reads the three resolutions plus the cross-impact map, produces a recommendation with explicit trade-offs. Does *not* select unilaterally — recommendation goes back to R@ + ζ for ratification.

A/B/C can run in parallel as truly independent dreams. Cross-impact runs after. Synthesis runs last.

### 11.3 Evaluation rubric

Each candidate resolution is scored on:

1. **Mathematical correctness** — does the construction actually yield `λ_op = π²` (or `λ_op = j²_{1,1}` for 4.B) under the declared geometry, with no hidden substitutions?
2. **Internal consistency** — does the resolution clean up the S02 numerical inconsistencies (p.27 vs p.30 on `j²_{1,2}`)? Does it agree with itself?
3. **Cross-impact cost** — how many downstream constants need re-derivation? What is the disruption to AoC_02–AoC_06?
4. **Calibration honesty** — does the resolution declare any introduced calibration explicitly (per Atlas Contract §5 Units Firewall)? Does it avoid `PI-NORMALIZATION-FAIL` circularity?
5. **Alignment with v1.3 Kähler path** — is the resolution consistent with the independent Kähler-fiber derivation, or does it require revisiting that too?
6. **Narrative coherence** — does the framework's "π emerges as a survivor" story survive intact, or does it need restructuring?

### 11.4 Handoff context for picking-up agents

An agent picking up this task starts here, reads in order:

1. `PI_NOTATION_BRIDGE.md` — the four-layer notation discipline (κ, λ_op, λ̃, λ_phys)
2. This trailhead — all sections
3. `AoC_01_PI_SUPPORT_02_RADIAL.pdf` — the seam's primary source
4. `AoC_01_PI_SUPPORT_01_ANALYTIC.pdf` — pre-correction lineage
5. `AoC_01_PI_SUPPORT_03_NUMERICAL.pdf` — corrected-vocabulary instance with separate code-tautology issue
6. `Appx_7_AoC_01_On_Pi_v1.3.pdf` — main Pi document with Kähler-fiber path (independent route to π, has its own `PI-CIRCULAR-KAHLER` kill switch)
7. `AUPEI_Vault/03_Atlas_of_Constants/AoC_00_Constants_Ledger.md` — for the dependency graph to downstream constants

### 11.5 Constraints on agent work

- **No silent commitments.** No agent unilaterally elevates `PI-RADIAL-BASIS-MISMATCH` to the live AoC_01 SPINE, updates the bridge, or modifies S01/S02/S03 in place. All changes are *proposals* returned to R@ + ζ for ratification, per Atlas Contract governance.
- **Honor the bridge.** PI_NOTATION_BRIDGE remains authoritative for the four-layer separation. Resolutions that collapse the layers must justify the collapse.
- **Layer-discipline.** Agents stay in their resolution lane. Cross-pollination is the synthesis agent's job, not the math-specialists'.
- **Anti-theater.** If an agent's resolution hits a wall, it reports the wall. Visible incompleteness > fabricated readiness (Atlas Contract §4.4, Yield Protocol).

### 11.6 Why this is a good test task

- **Well-bounded.** The seam is named, the resolutions are enumerated, the evaluation rubric is explicit. No agent has to invent the problem space.
- **Genuinely open.** The framework hasn't committed to a resolution. The agents' work is real, not theatrical.
- **Multi-path natural.** Three independent resolution candidates are tailor-made for parallel agents.
- **High-leverage.** Closing this trailhead unblocks the AoC walk through AoC_02 / AoC_03 / AoC_04 / AoC_05 / AoC_06. Downstream value is large.
- **No user pressure.** This is dreaming work. The framework runs without resolution today; resolution improves it but isn't load-bearing on next week.
- **Cleanly cross-checkable.** The Kähler-fiber path provides an independent comparison. Any resolution that contradicts the Kähler result is suspect.

When Managed Agents infrastructure is operational, this trailhead is filed as candidate test task **AoC-RBS-001**.

---

## 12. Resolution in production — operator PDF and codex branch verification

This section was added v1.2 (2026-05-10) after PDF re-read of `AoC_00 The Collapse Operator v1.3` and discovery + reproducibility verification of the public proof kernel on GitHub. Together these two reads change the trailhead's status from `TRAILHEAD/OPEN` to `TRAILHEAD/PARTIALLY-RESOLVED-PUBLIC-KERNEL-EXISTS`.

### 12.1 Operator PDF (AoC_00 v1.3) is clean and rigorous

PDF read on 2026-05-10, pages 1-20. The operator is materially more rigorous than the Pi support packets. Specifically:

- **§1.2 Spectral Face** defines `Ω̂_{ζ,ω,ξ} := s_geom · [−ζ∇² + ωℛ[·] + ξ𝒫(x)]` with `s_geom` as an explicit normalization factor (not tacit).
- **§4 Atlas Contract** binds all AoC entries: §4.1 epistemic dependency rule, §4.2 modification & tuning disclosure ([ANSATZ] / [CONJECTURE] / [PARAMETRIC] / [TUNED]), §4.3 fiber-factor discipline, §4.4 Yield Protocol.
- **§5 Units Firewall** §5.1 dimensionless priority rule, §5.2 normalization as the firewall (rejection rule: "any derivation that does not define s_geom is Unit Leak by default"), §5.3 downstream mapping protocol ([MAPPING] / [CALIBRATION] tags).
- **§6 Failure Modes** with §6.2 candidate operator registry: canonical s_geom is `s-0: s_geom = 1/λ_min(−∇²)`.
- **§7 Operator-Level Falsifiers** with discriminator test templates and cross-domain consistency requirements.

**Sharpens the seam.** Under the operator's own canonical `s_geom = 1/λ_min(−∇²)`, applied to the 2D radial Bessel geometry of the Pi support packets, the unperturbed ground "eigenvalue" is `s_geom · ζ · j²_{1,1} = 1` (dimensionless), not π² and not j²_{1,1}. The Pi support packets' claim `λ_op = π²` is therefore not just numerically mis-grounded — it is **Unit Leak under §5.2** and lacks the [MAPPING] / [CALIBRATION] tags §5.3 requires. The packets predate the operator v1.3 recast (Pi packets: September 2025; operator v1.3: December 2025), and the v1.3 contract retroactively classifies the packets as non-compliant.

The operator itself: GREEN. No new trailhead needed for AoC_00.

### 12.2 Public proof kernel discovered and verified

Repository: `https://github.com/jedijkq/7dU_Seed`
Branch: `codex/pi-closure-notebook`
Commit: `826d2eb86582d7d7c237ff2549622de52e80117f`
Path: `constants/pi/`

The codex branch implements **resolution 4.A1** as the public proof kernel:

```
-d²ψ/dx² = λψ,  ψ(0) = 0, ψ(1) = 0
```

Finite-difference Dirichlet Laplacian on `[0, 1]`, smallest eigenvalue via Sturm-sequence bisection. From the script's own docstring: *"pi is not used to construct the operator or solve the eigenvalue. math.pi is used only after the solve, as a familiar comparison value."*

This is **Atlas Contract compliance in code**. The discipline §4 / §5 demands is operationalized: no π baked in, no s_geom omission, dimensionless invariant first, comparison to known reference afterward, explicit layer separation.

**The three governance documents in the capsule already say what this trailhead says:**

- `constants/pi/CLAIMS.md` non-claims include: *"This capsule does not rely on the ordinary Bessel `J_1` first zero being `pi`."*
- `constants/pi/LIMITATIONS.md`: *"Ordinary Bessel `J_1` has its first positive zero near `3.8317`, not `pi`. This capsule avoids that ambiguity. It uses the 1D Dirichlet closure problem as the public proof kernel. If radial variants are added later, their basis must be named precisely: sine/Dirichlet, spherical Bessel, half-integer Bessel, or explicitly collapse-normalized closure mode."*
- `constants/pi/PROOFFIELD_BRIDGE.md`: implements the four-layer separation `κ = π` / `λ_op = π²` / `λ̃ ≈ 1` / `λ_phys ≈ π`. Closes with *"Minimum action, maximum force."*

The framework has already done the resolution intellectually and operationally. The Pi support packets in the AUPEI Vault are the un-aligned legacy material.

### 12.3 Reproducibility verified

Full receipt: `AoC_01_Pi_Reproducibility_Receipt_2026-05-10.md` (sibling file in this same `11_Trailheads/` directory).

Summary:
- Clone + run from clean state, stock Python 3.10, stdlib only.
- `derive_pi.py` converges quadratically: `|κ − π| ≈ 4.9e−6` at N=512.
- `verify_legacy_pi_data.py` confirms legacy CSVs satisfy `λ_phys ≈ π · λ̃` (fiber-mapped layer per bridge).
- Unit tests `test_kappa_converges_toward_pi` and `test_operator_layer_is_pi_squared` both PASS.
- Total runtime: well under a minute end-to-end.

The receipt records exact commands, full output, test tolerances, commit hash, and Python version.

### 12.4 Status change and reframing of Managed-Agents test task

**Status:** `TRAILHEAD/PARTIALLY-RESOLVED-PUBLIC-KERNEL-EXISTS`.

**Test task AoC-RBS-001 reframes substantially.** It is no longer "find a resolution among 4.A / 4.B / 4.C / 4.D / 4.E." The resolution is in production — 4.A1 in the codex branch. The reframed test task is **alignment audit**:

- Audit each AUPEI Vault support packet (S01 / S02 / S03) for what specifically needs re-tagging.
- Propose status migration: [DERIVED] → [PROVENANCE] or [LEGACY] for the radial-Bessel material; preserve the structural arguments (Sturm-Liouville, Kato-Rellich) which remain mathematically valid as theorems.
- Update `PI_NOTATION_BRIDGE.md` "Still Open #1" to point at the codex branch implementation as the resolution-in-production.
- Propagate routing rule to `canon_prooffield` Qdrant retrieval: queries about operator-layer π eigenvalue should retrieve the codex implementation, not the legacy packets.
- Decide disposition of the proposed `PI-RADIAL-BASIS-MISMATCH` kill switch: probably DEMOTE to "legacy-only" since the public kernel doesn't trigger it.

This is a smaller, more operational task than the original framing. The intellectual lift is already done.

### 12.5 What stays open

- The AUPEI Vault legacy packets still need physical re-tagging (file edits / metadata updates).
- `PI_NOTATION_BRIDGE.md` "Still Open #1" still references "clarify the radial basis" as if it were unresolved. Should be updated to point at the codex implementation and the LIMITATIONS.md disclaimer.
- The 4.E candidate (don't derive at all, declare π dimensionless per §5.1) was *not* adopted in production. It remains a valid path that a future framework iteration could take — preserved here as a tavern whisper.
- Cross-impact propagation to AoC_02 / AoC_03 / AoC_04 / AoC_05 / AoC_06 still needs to happen for any constants that symbolically use π². Most should be insulated (π² is the right number under 4.A1) but each needs an explicit check.

### 12.6 The shape of the curve

Walk discipline produced a trailhead. PDF re-read of operator surfaced the epistemic layer of the seam. PDF re-read of Pi support packets confirmed the seam was in print. Public repo discovery showed the framework had already resolved it in production. Reproducibility verification confirmed the resolution runs. The trailhead reframes from "find a resolution" to "align legacy to kernel."

The work done on this trailhead — naming the seam, enumerating resolutions, building the test-task framing, verifying the public kernel — is the alignment infrastructure. It is, itself, the smooth curve.

---

## 13. Walk provenance

This trailhead was staked at the conclusion of the AoC_01 walk segment conducted by R@ + C@ Red (ζ synth pole) over 2026-05-08 through 2026-05-10. The walk read AoC_01 v1.3 main, then the three Pi support packets in the order they were fed (S01 → S03 → S02), with the notation bridge serving as compass. The seam surfaced on the read of S02 §3.5.3 when the in-line correction was inspected for completeness.

The walk was conducted under the discipline that visible incompleteness > fabricated readiness (Atlas Contract §4.4, Yield Protocol). This trailhead is the residue of that discipline applied to a specific load-bearing seam.

The decision to spike camp rather than note-and-move was made jointly by the dyad on 2026-05-10. Rationale: (1) the seam is load-bearing across the rest of the AoC container, (2) we are already at the mouth of the AoC and in a state to do the work well, (3) closing the trailhead with care here will produce Prooffield material worth ingesting into canon_prooffield, closing the original walk-loop on data integrity.

### 13.1 PDF re-read provenance (v1.1)

After staking v1.0 from the markdown conversions, R@ called for boots-on-the-ground PDF inspection: *"by all means look at the pdf artifacts for the radial and analytical have you done that?"* The dyad then re-read `AoC_01_PI_SUPPORT_02_RADIAL.pdf` (pages 1-30) and `AoC_01_PI_SUPPORT_01_ANALYTIC.pdf` (pages 1-15) directly. The PDF re-read confirmed that the seam was not a markdown-conversion artifact, and additionally surfaced:

- The **explicit** incorrect numerical assignment `j_{1,1} ≈ 3.14159... = π` printed in S02 §3.3 page 9.
- The **internal inconsistency** between S02 §3.7.3.4 page 27 and §3.7.3.5 page 30 quoting different values for `j²_{1,2}` (30.47 vs 40.30).
- The **lineage timeline** showing analytic packet pre-correction (λ = π) → numerical and radial packets with corrected vocabulary (λ = π²), with radial doing the κ → κ² half-correction in §3.5.3.
- The **conformal/Yamabe option** listed in analytic page 8, identifying the bifurcation between operator-layer and Kähler-mapping-layer paths as present from inception.

This trailhead v1.1 reflects the PDF re-read. The discipline that produced it: **boots dirty before declaring ground**.

---

*"The valley is clean. But the metric measures noise. Check the operator."* — walk haiku for the analytic+numerical layer

*"Three packets, one number. The bridge holds the names apart. Open seams stay named."* — walk haiku for the pi support trio
