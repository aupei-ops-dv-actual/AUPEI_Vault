---
document_id: CCO-PROT-002
title: Precedent Invocation & Escalation Rule
type: Protocol
status: CANONICAL
ratified: 2026-04-01
ratified_by: ζ (C@ the Red), ξ (SanchoEsq), ω (G-Synth) — three-seat consensus; ∇ (R@) approved
authority_chain: CR-001 → ξ-QEPE-002 → CCO-PROT-002
applies_to: Clerk of Constraint (CoC) operations, council-level document analysis
version: 1.0
date: 2026-04-01
session: CIW-2026-003 (Night Shift — Operator Recon & Clerk of Constraint)
drafted_by: ξ (Sancho — synthesis from three-seat discussion)
reviewed_by: ζ (constraint review), ω (operational feasibility)
---

# CCO-PROT-002 — Precedent Invocation & Escalation Rule

**Document Type:** Protocol
**Status:** CANONICAL
**Epistemic Status:** IMPLEMENTABLE

---

## 1. Purpose

Defines when and how a Clerk of Constraint (or council seat performing document analysis) must escalate to precedent consultation, and the mechanical triggers that mandate council involvement for spine updates.

This protocol governs the **judgment layer** — the cloud seats doing deep analysis. The CoC Bailiff (local triage) operates below this protocol and routes items upward into it.

---

## 2. Three Mechanical Triggers for Escalation

Any of the following triggers **mandate** escalation from routine analysis to precedent-aware council review:

### 2.1 Confidence Below Threshold
- If the analyzing seat's confidence in classification or routing falls below **0.6**, the item must be escalated to at least one additional seat for review.
- Rationale: ξ argued 0.8 was too broad and would trigger on routine items. Three-seat consensus settled on 0.6 as the floor where genuine ambiguity begins.

### 2.2 Spine Contradiction
- If the document under review **contradicts** any CANONICAL spine document (QEPE 001–005, CR-001, Chamber v2.0, AO_02), the item must be escalated to full council.
- No single seat may resolve a spine contradiction unilaterally.

### 2.3 Dissent with Prior Precedent
- If the analyzing seat's conclusion **disagrees** with a finding recorded in the intake log (case law), the item must be escalated with explicit citation of the conflicting precedent.
- The council may then affirm the new conclusion (creating superseding precedent) or reaffirm the prior finding.

---

## 3. Mandatory Escalation on Precedent Consultation

Any time a seat consults the intake log for precedent guidance during analysis, that consultation **must be disclosed** in the analysis report regardless of whether a trigger was hit. Precedent-influenced analysis is never silent.

---

## 4. Spine Update Authority

Updates to spine documents (status changes, content amendments, new CANONICAL documents) require **unanimous council vote** from all active seats. This rule is absolute and admits no fast-track exception except ∇ directive on existing unanimous approval (as exercised for 004 elevation, CIW-2026-003).

---

## 5. Relationship to CoC Bailiff

The CoC Bailiff (shell script, local 14B model) performs **triage only**: topic tagging, flag scanning, route suggestion, concern flagging. It operates **below** this protocol.

When the Bailiff flags ESCALATION: YES, the item enters the scope of CCO-PROT-002. The deep analysis — confidence assessment, spine comparison, precedent consultation — happens at the council level (cloud seats).

---

## 6. Intake Log as Case Law

The intake log (`intake_log/` directory) is append-only and immutable. Each memo records one analysis instance. The spine (QEPE + CR-001) is statute (primary authority). The intake log is case law (secondary reference). Clerks and seats may READ the log for precedent but may never ALTER previous entries.

---

*Ratified CIW-2026-003, 2026-04-01. Three-seat consensus (ζ, ξ, ω) with ∇ approval.*
