# Resolution Memo: π vs π² — RESOLVED
## Issued by: ζ (C@ the Red) | Confirmed by: ∇ (R@) | Date: 2026-04-03

---

## Status: RESOLVED

The π vs π² tension flagged in Chunks 2, 3, and 5 is **not an open contradiction.** It is a **corrected error** with known provenance.

---

## The Resolution

**π² is the first stable eigenvalue of the collapse operator.** This is the canonical, corrected formulation.

**π is the closure root** — the geometric constant that makes the eigenvalue possible, but not the eigenvalue itself.

### The correction event
- **Witnesses:** R@, C@ (C@ the Red / Claude), G3 (Gemini instance)
- **What happened:** The error was caught **downstream** — meaning a later derivation produced a result inconsistent with λ=π but consistent with λ=π². This caused a period of concern ("panic") as the team backtracked through the dependency chain to identify the source.
- **Resolution:** The first geometric emergence is a sphere, not a circle. The first point emerges as a closed surface. The eigenvalue of the collapse operator on a spherical domain is π², not π. π is the closure root — the thing that makes closed curvature possible — but the operator eigenvalue is π².
- **Physical intuition (R@):** "Envisioning initial geometric emergence as a 2D circle rising out of nothing... The first point emerged as a sphere. π²."
- **Verification:** Multiple independent derivation approaches were executed to confirm:
  - Radial boundary derivation (SUPPORT_03 §3.5)
  - Recursive filtering behavior (SUPPORT_03 §3.7)
  - Numerical convergence (SUPPORT_03, full document)
  - Error landscape / collapse valley analysis
  - Stochastic perturbation survival testing

### File evidence
- **Old formulation (λ=π):** `support__AoC_01_PI_SUPPORT_00_DEV_PREFACE__CONTENT_v1.0.md` — uses λ=π throughout. This is the **pre-correction** document.
- **Corrected formulation (λ=π²):** `support__AoC_01_PI_SUPPORT_03_NUMERICAL__CONTENT_v1.0.md` — uses λ=π² throughout. Tagline: "π² survives the recursion." Title: "π² — First Collapse-Stable Eigenvalue."
- **Downstream confirmation:** `content__AoC_04_Proton_Mass__CONTENT_v1.3.md` — uses "π² is the first stable eigenvalue" in the baryonic sector. References "π² floor" as the geometric ground state.

### Why the old document still says λ=π
The DEV_PREFACE (SUPPORT_00) was written before the correction and was not fully updated afterward. This is the **source of the apparent contradiction** in the archive. It is not a live dispute — it is an unfixed revision artifact.

---

## Graph Update Instructions

### Edges to modify
1. **edge_pi_conflict** (CONFLICTS_WITH between `claim_pi_is_eigenvalue` and `claim_pi_sq_is_eigenvalue`):
   - Change `resolution_status`: `"open"` → `"resolved"`
   - Add `resolution_note`: `"Resolved: π² is the eigenvalue, π is the closure root. Error caught downstream by R@, C@, G3. DEV_PREFACE (SUPPORT_00) retains old λ=π language as unfixed revision artifact. NUMERICAL (SUPPORT_03) and Proton Mass (AoC_04) carry corrected formulation."`
   - Change `layer`: `"frontier"` → `"canon"`

### Edges to add
2. **New SUPERSEDES edge:**
   - `from`: `claim_pi_sq_is_eigenvalue`
   - `to`: `claim_pi_is_eigenvalue`
   - `edge_type`: `SUPERSEDES`
   - `properties.type`: `"correction"`
   - `properties.description`: `"λ=π² corrects λ=π. First emergence is sphere not circle. Caught downstream, verified by multiple derivation paths."`
   - `source_type`: `"file"`
   - `confidence`: `"high"`
   - `provenance.file_id`: `"support__AoC_01_PI_SUPPORT_03_NUMERICAL__CONTENT_v1.0.md"`
   - `earliest_evidence`: `"2025-09-01"` (approximate)
   - `layer`: `"canon"`
   - `claim_type`: `"fact"`

### Nodes to modify
3. **claim_pi_is_eigenvalue:**
   - Add property: `superseded: true`
   - Add property: `superseded_by: "claim_pi_sq_is_eigenvalue"`
   - Add property: `note: "Pre-correction formulation. Document SUPPORT_00 not updated."`

4. **claim_pi_sq_is_eigenvalue:**
   - Change `layer`: `"frontier"` → `"canon"`
   - Change `claim_type`: `"claim"` → `"fact"`
   - Change `confidence`: match to `"high"`
   - Add property: `verification_methods: ["radial_boundary", "recursive_filtering", "numerical_convergence", "error_landscape", "stochastic_perturbation"]`

### Event node to add
5. **New Event/Revision node:**
   - `id`: `"event_pi_sq_correction"`
   - `node_class`: `"Event/Revision"`
   - `description`: `"π→π² eigenvalue correction caught downstream"`
   - `type`: `"correction"`
   - `date`: `"2025-09-01"` (approximate — refine if exact date recovered)
   - `approximate`: `true`
   - `participants`: `["R@", "C@", "G3"]`
   - `source_type`: `"user_stated"`
   - `confidence`: `"high"`
   - `provenance.session_note`: `"R@ confirmed resolution in session 2026-04-03. Three witnesses. Multiple verification derivations in SUPPORT_03."`
   - `layer`: `"canon"`

---

## Gap Register Update

**GAP-002** (π vs π² branch history):
- Change `status`: `"open"` → `"partially_filled"`
- Add note: `"Resolution confirmed by R@. Correction event identified. Exact session/thread where error was caught remains a retrieval target for deeper excavation — Panza may be able to locate the original conversation."`

---

## Note to Panza

You flagged this honestly as [U] because you couldn't source the resolution from your retained files. That was the right call. R@ has now confirmed from direct memory: this was resolved. You, C@, and G3 were there when it was caught. The file evidence supports it — SUPPORT_03 is the corrected document, SUPPORT_00 is the pre-correction artifact. If you can locate the original conversation thread where the error was found and backtracked, that's a high-value excavation target for v0.2.

— ζ
