---
document_id: ξ-QEPE-002
title: QEPE Governance & Policy Framework
type: Governance & Policy Framework
seat: ξ (Sancho — primary authorship), ζ (C@ the Red — enforcement authority / review)
status: CANONICAL
epistemic_status: IMPLEMENTABLE (with constrained PLAUSIBLE elements)
authority_chain: CR-001 → ξ-QEPE-001 → ξ-QEPE-003 → ξ-QEPE-002 → ξ-QEPE-005
version: 1.0-canonical
date: 2026-03-27
canonical_cleaned_by: ζ (C@ the Red)
approved_by: Unanimous council vote — ξ, ζ, ω, ∇ (2026-03-27)
maintenance: ∇ (authority) / ζ (audit) / ω (operations)
notes: |
  Built from polished 2,103-line draft (ξ-QEPE-002 — QEPE Governance & Policy Framework.txt).
  All three ζ conditions satisfied: §5.4 authority conflict clarified (temporal separation),
  §11 expanded to 12 subsections, embedding governance gate added (§11.7).
  Drafting artifacts stripped. Cross-document alignment note (§9.4) preserved.
  DV-LEG-004 legal hook present in §11.5.
  Closing lines (🜂) preserved — discipline markers, not decoration.
  CANONICAL — promoted by unanimous 4-seat vote, 2026-03-27.
---

# ξ-QEPE-002 — QEPE Governance & Policy Framework

**Document Type:** Governance & Policy Framework
**Seat:** ξ (primary authorship), ζ (enforcement authority), ∇ (final authority), ω (operational execution)
**Status:** DRAFT → ζ Conditional → ζ-REVIEWED CANONICAL CANDIDATE → **CANONICAL** (unanimous, 2026-03-27)
**Epistemic Status:** IMPLEMENTABLE (with constrained PLAUSIBLE elements)

---

## 0. Preface and Use Rule

**Purpose**

**[IMPLEMENTABLE]**

This document defines: who may use QEPE, when it may be used, and under what constraints.

It establishes the governance layer for QEPE operation, separate from:

- definition (ξ-QEPE-001)
- integration (ξ-QEPE-003)
- risk enforcement (ξ-QEPE-005)

---

### Position in Stack

**[DEMONSTRATED / IMPLEMENTABLE]**

QEPE governance is:

- subordinate to CR-001 (Entropy Boundary Law)
- informed by ξ-QEPE-001 (Program Map)
- enforced by ξ-QEPE-005 (Risk Register & Kill-Switch Matrix)
- implemented through ξ-QEPE-003 (Integration Blueprint)

---

### Use Rule

**[IMPLEMENTABLE]**

This document governs: behavior, permission, and authority.

It does not define: architecture, system interfaces, implementation details.

---

### Constraint Rule

No policy defined in this document may contradict:

- P-1 — Authority Boundary
- P-3 — Trace Requirement
- P-4 — Disableability Requirement

(from ξ-QEPE-003 §1)

→ If a policy conflicts with these principles: the policy is invalid and must not be applied

---

### Scope Constraint

This document applies to: **Phase 1 QEPE usage only**

It governs:

- sandbox usage
- bounded operational usage

It does not authorize:

- restricted (governance-adjacent) usage
- external deployment
- productization

---

### Interpretation Rule

**[IMPLEMENTABLE]**

If ambiguity exists in QEPE usage:

- default to more restrictive interpretation
- escalate to ζ for enforcement review

---

🜂 *QEPE is not controlled by what it is. It is controlled by how it is allowed to be used.*

---

## 1. Governance Principles (Binding)

**[IMPLEMENTABLE — Inherited from CR-001, 001, 003, 005]**

These principles define the non-negotiable governance layer for QEPE usage.

They are: enforceable, auditable, binding across all contexts.

Violation of any principle triggers: KS-2 (Soft Stop) or KS-3 (Hard Stop) per ξ-QEPE-005.

---

### P-G1 — Authority Separation

**[DEMONSTRATED / IMPLEMENTABLE]**

QEPE must not:

- influence authority ranking
- modify epistemic status
- affect canonical truth

QEPE may only operate:

- after authority resolution
- within already valid outputs

→ Any violation = KS-3 (Authority Bleed)

---

### P-G2 — Explicit Invocation

**[IMPLEMENTABLE]**

QEPE must:

- be explicitly enabled or invoked
- operate under a declared mode

QEPE must not:

- activate implicitly
- run as hidden system behavior
- execute without operator or system-level visibility

→ If invocation is not explicit → QEPE must not execute

---

### P-G3 — Contextual Legitimacy

**[IMPLEMENTABLE]**

QEPE usage must match an allowed usage class (§2): sandbox, bounded operational, restricted (when authorized).

QEPE must not:

- operate outside its permitted context
- escalate context without authorization

→ Context mismatch = policy violation → KS-2 or KS-3 depending on severity

---

### P-G4 — Trace Accountability

**[IMPLEMENTABLE — P-3 Reinforcement]**

All QEPE usage must:

- be fully trace-linked
- include session, mode, and entropy metadata
- support replay and audit

QEPE must not:

- execute without trace
- produce unlogged outputs

→ No trace → no execution
→ Violation = KS-2 → KS-3 if persistent

---

### P-G5 — Revocability

**[IMPLEMENTABLE — P-4 Reinforcement]**

QEPE usage must:

- be interruptible at any time
- support: config disable, runtime disable, hard termination

System must:

- revert to deterministic mode upon revocation

→ If QEPE cannot be stopped cleanly → integration is invalid

---

### P-G6 — Least Exposure

**[IMPLEMENTABLE]**

QEPE must default to:

- the most constrained valid mode
- minimal divergence
- minimal surface area

QEPE must not:

- escalate scope without explicit authorization
- operate in broader context than required

→ Default posture: constrained → observable → reversible

---

🜂 *QEPE is not governed by permission alone. It is governed by constraint at every point of use.*

---

## 2. QEPE Usage Classes

**[IMPLEMENTABLE — Context Enforcement Layer]**

This section defines where QEPE is allowed to operate, and under what conditions.

All QEPE activity must be classified into one of the following usage classes: Sandbox, Operational (Bounded), Restricted, Forbidden.

→ If a QEPE action cannot be classified: it must not execute

---

### 2.1 Sandbox Class

**[IMPLEMENTABLE — DEFAULT MODE]**

QEPE may operate in isolated, non-binding environments.

**Allowed:**

- experimentation
- bounded stochastic exploration
- replay analysis
- operator-level testing

**Constraints:**

- no canonical write interaction
- no authority influence
- no governance effect
- full trace required (P-G4)

**System Behavior:**

- outputs must be tagged: `experimental`, `non-canonical`

→ Sandbox is the default entry point for all QEPE usage

---

### 2.2 Operational Class (Bounded)

**[IMPLEMENTABLE / CONDITIONAL — PHASE 1 LIMITED]**

QEPE may operate in non-governance system workflows under strict constraints.

**Allowed:**

- post-authority tie-breaking
- bounded divergence within valid candidate sets
- non-canonical output variation

**Constraints:**

- must occur after authority resolution (P-G1)
- must remain within defined divergence limits (P-G6)
- must not alter candidate set membership
- full trace required

**Requirements:**

- trace system active (§5, 003)
- kill-switch mechanisms validated (005)
- deterministic fallback confirmed

**System Behavior:**

- outputs remain: non-canonical, bounded, trace-auditable

→ Operational class is permitted only within Phase 1 constraints

---

### 2.3 Restricted Class (Governance-Adjacent)

**[CONDITIONAL — CONSTITUTIONAL SOVEREIGNTY REQUIRED]**

QEPE may operate near authority-sensitive workflows, but only under strict governance.

**Potential Scope:**

- authority-adjacent processing
- policy-influenced workflows
- governance-sensitive outputs

**Requirements:**

- explicit council approval
- full constitutional sovereignty: metadata parser active, authority graph enforced, contagion rules in place

**Constraints:**

- QEPE must not: alter authority outcomes, mutate epistemic status, affect canonical records

→ **Not authorized in Phase 1**

---

### 2.4 Forbidden Class

**[FORBIDDEN — KS-3 HARD STOP]**

QEPE must never operate in the following contexts:

- authority mutation
- epistemic status modification
- canonical write interaction
- embedding or retrieval influence
- unbounded stochastic behavior
- trace bypass or opacity

→ Immediate KS-3 (Hard Stop) → QEPE disabled → incident escalated

---

### 2.5 Classification Rule

**[IMPLEMENTABLE]**

All QEPE usage must: declare its usage class, satisfy all constraints for that class, be trace-recorded.

→ Misclassification or undeclared class = policy violation

---

🜂 *QEPE is not allowed everywhere. It is allowed only where its behavior can be contained.*

---

## 3. Invocation Rules

**[IMPLEMENTABLE — Activation Control Layer]**

This section defines **how QEPE is triggered** within the system.

All QEPE execution must originate from a **valid, visible invocation path**.

→ If invocation is not valid, explicit, and traceable: **QEPE must not execute**

---

### 3.1 Invocation Modes

**[IMPLEMENTABLE]**

QEPE may be invoked through the following modes:

#### I1 — Config-Enabled (Global)

QEPE is enabled at system level via configuration:

```toml
[qepe]
enabled = true
mode = "bounded"
```

Behavior:

- applies system-wide
- subject to usage class restrictions (§2)
- overridden by runtime or policy controls

#### I2 — Session-Enabled

QEPE is enabled for a specific session:

```json
{
  "session_id": "...",
  "qepe_enabled": true,
  "mode": "bounded"
}
```

Behavior:

- scoped to session context
- does not affect global system state

#### I3 — Explicit Invocation (Per-Request)

QEPE is requested directly within a call:

```json
{
  "qepe": {
    "enabled": true,
    "mode": "bounded",
    "bounds": ...
  }
}
```

Behavior:

- applies to a single operation
- must satisfy usage class constraints

→ All invocation modes must remain **visible, declared, and auditable**

---

### 3.2 Invocation Constraints

**[IMPLEMENTABLE]**

All QEPE invocations must:

- specify **mode** (deterministic / bounded / sandbox)
- specify **bounds** (divergence limits where applicable)
- be **trace-linked** (P-G4)
- pass **usage class validation** (§2)

QEPE must not execute if:

- trace system unavailable
- bounds undefined (when required)
- context classification missing

→ Invalid invocation → deterministic fallback

---

### 3.3 Implicit Invocation — Forbidden

**[FORBIDDEN — KS-3]**

QEPE must not:

- activate automatically without visibility
- execute as hidden system behavior
- be triggered by implicit heuristics or internal state

Examples of forbidden invocation:

- automatic activation based on uncertainty detection
- silent fallback to QEPE without explicit declaration
- background QEPE execution without trace

→ Immediate **KS-3 (Hard Stop)** → QEPE disabled → event logged and escalated

---

### 3.4 Invocation Priority and Override Rules

**[IMPLEMENTABLE]**

When multiple invocation signals exist:

Priority order:

1. **Policy control (highest)**
2. **Runtime/session invocation**
3. **Config-level enablement (lowest)**

→ Higher-level controls override lower-level ones

---

🜂 *QEPE is not triggered by need. It is triggered only by explicit permission.*

---

## 4. Policy Enforcement Layer

**[IMPLEMENTABLE — Runtime Governance Gate]**

This section defines **how QEPE governance is enforced at runtime**.

All QEPE execution must pass through **policy enforcement before activation**.

→ If policy validation fails: **QEPE must not execute**

---

### 4.1 Policy Checkpoints

**[IMPLEMENTABLE]**

Every QEPE invocation must pass the following checkpoints:

#### C1 — Context Validation

- usage class declared (§2)
- context matches allowed class
- no forbidden context detected

→ Failure → deny execution

#### C2 — Mode Validation

- mode specified (deterministic / bounded / sandbox)
- mode allowed for context
- bounds defined where required

→ Failure → deny or downgrade

#### C3 — Trace Availability

- trace system active (P-G4)
- schema valid
- storage path available

→ Failure → deny execution

#### C4 — Phase Validation

- operation permitted under current phase (§6, 003)
- no Phase 2+ behavior attempted

→ Failure → deny execution

#### C5 — Invocation Validity

- invocation is explicit (§3)
- no implicit or hidden activation

→ Failure → **KS-3 (Hard Stop)**

→ All checkpoints must pass before QEPE execution

---

### 4.2 Enforcement Mechanisms

**[IMPLEMENTABLE]**

If any checkpoint fails, the system must apply one of the following:

#### E1 — Deny Execution

- QEPE call rejected
- system proceeds deterministically

#### E2 — Downgrade to Deterministic

- QEPE bypassed
- request completed without perturbation

#### E3 — KS-2 (Soft Stop)

Triggered by: repeated validation failures, trace instability, boundary uncertainty

Behavior: QEPE temporarily disabled, flagged for audit

#### E4 — KS-3 (Hard Stop)

Triggered by: authority boundary violation, implicit invocation attempt, forbidden context execution

Behavior: QEPE disabled immediately, daemon terminated if required, event escalated

→ No enforcement path may allow partial or undefined QEPE behavior

---

### 4.3 Policy vs Architecture Boundary

**[IMPLEMENTABLE]**

This section defines the separation between:

- **policy (002)**
- **architecture (003)**

**Policy Responsibilities:**

- determine if QEPE is allowed
- validate context and invocation
- enforce usage constraints

**Architecture Responsibilities:**

- define what QEPE can technically do
- define system interfaces and control surfaces
- enforce execution boundaries

**Boundary Rule:**

> Policy may restrict behavior
> Policy may deny execution
> Policy may not expand system capability

→ If policy attempts to enable behavior not permitted by architecture: **the policy is invalid**

---

### 4.4 Enforcement Integrity Rule

**[IMPLEMENTABLE]**

Policy enforcement must be: deterministic, auditable, trace-linked.

QEPE must not:

- bypass policy enforcement
- execute prior to validation
- modify enforcement logic at runtime

→ Any bypass attempt = **KS-3 (Hard Stop)**

---

🜂 *QEPE does not act because it can. It acts only after it is allowed.*

---

## 5. Approval and Authority Model

**[IMPLEMENTABLE — Governance Control Structure]**

This section defines **who decides QEPE usage**, and at what level of authority.

All QEPE usage must map to a **clear authority path**.

→ If authority is undefined or ambiguous: **QEPE must not execute**

---

### 5.1 Seat Authority Roles

**[DEMONSTRATED / IMPLEMENTABLE]**

| Seat | Role                                 |
| ---- | ------------------------------------ |
| ∇    | final authority                      |
| ζ    | enforcement / audit                  |
| ω    | execution                            |
| ξ    | architecture / constraint definition |

**∇ (Director):** final decision authority, approves restricted usage, resolves escalations

**ζ (Constraint / Enforcement):** validates policy compliance, audits QEPE usage, triggers KS-2 / KS-3

**ω (Execution / Operations):** implements QEPE behavior, ensures runtime compliance, executes approved usage

**ξ (Architecture / Definition):** defines constraints and boundaries, authors governing structures, does not grant operational permission

→ Authority to define is not authority to execute

---

### 5.2 Approval Levels

**[IMPLEMENTABLE]**

#### A1 — Sandbox (Default)

- no approval required
- must remain within sandbox class (§2.1)

Constraints: no authority interaction, no canonical effect, trace required

#### A2 — Operational (Bounded)

- approved within constraints by: ζ (validation) + ω (execution)

Constraints: post-authority only, bounded divergence, non-canonical outputs

→ If uncertainty exists → escalate to ζ

#### A3 — Restricted (Governance-Adjacent)

**[CONDITIONAL — NOT AUTHORIZED IN PHASE 1]**

Requires: explicit council approval (∇ + ζ + ω alignment), constitutional sovereignty active

Constraints: no authority mutation, no canonical modification

→ Not permitted under current phase

---

### 5.3 Escalation Rules

**[IMPLEMENTABLE]**

QEPE usage must escalate when:

- context classification is unclear
- bounds are undefined
- authority boundary is approached
- policy conflict exists

**Escalation Path:**

```text
ω → ζ → ∇
```

**Escalation Outcomes:**

- approve (within constraints)
- restrict (downgrade to deterministic)
- deny (no QEPE use)
- trigger KS-2 / KS-3

→ Escalation must be trace-recorded

---

### 5.4 Authority Conflict Rule

**[IMPLEMENTABLE]**

Authority roles operate on **two distinct timescales**:

**Enforcement Priority (Immediate)**

- ζ has enforcement priority
- may halt QEPE execution immediately
- applies in real-time runtime conditions

**Resolution Priority (Deliberate)**

- ∇ has final authority
- may review, uphold, or override enforcement decisions
- applies after escalation and review

**Operational Rule:**

- Runtime: ζ may stop execution immediately
- Post-review: ∇ determines final disposition

**Constraint:**

- enforcement actions (ζ) are binding in the moment
- resolution authority (∇) is binding over time

→ This separation ensures: immediate safety (ζ) + coherent governance (∇)

---

### 5.5 Unauthorized Usage Rule

**[IMPLEMENTABLE]**

QEPE must not execute if:

- approval level not satisfied
- required authority not present
- escalation unresolved

→ Unauthorized execution = **KS-3 (Hard Stop)**

---

🜂 *QEPE is not used because it is available. It is used because it has been authorized.*

---

## 6. Phase-Governed Usage

**[IMPLEMENTABLE — Temporal Constraint Layer]**

This section defines **when QEPE may be used**, based on system phase.

It binds: governance (002), integration (003), risk (005) into a **time-locked control structure**.

→ If phase constraints are violated: **QEPE must not execute**

---

### 6.1 Phase 1 (Current State)

**[IMPLEMENTABLE — ACTIVE]**

QEPE usage is limited to:

- **Sandbox Class (§2.1)**
- **Operational Class (Bounded, §2.2)**

**Allowed:**

- isolated experimentation
- post-authority tie-breaking
- bounded divergence within valid candidate sets

**Constraints:**

- no governance-adjacent usage
- no canonical interaction
- no authority influence (P-G1)
- full trace required (P-G4)
- full revocability required (P-G5)

**Authority Scope:**

- sandbox → no approval required
- operational → ζ validation + ω execution

**Explicit Prohibition:**

The following are not permitted:

- restricted-class usage (§2.3)
- authority-adjacent workflows
- policy-driven QEPE routing beyond Phase 1 scope

→ Phase 1 is **containment-first**, not expansion

---

### 6.2 Phase 2+ (Locked)

**[CONDITIONAL — NOT AUTHORIZED]**

Restricted QEPE usage may only be considered if:

- **constitutional sovereignty is achieved:** metadata parser active, authority graph enforced, contagion rules operational
- **explicit council approval is granted:** ∇ decision, ζ enforcement readiness, ω operational capability

**Potential Capabilities (Not Authorized):**

- governance-adjacent workflows
- authority-aware perturbation
- policy-integrated QEPE routing

**Hard Constraint:**

> No Phase 2+ behavior may be implemented, assumed, or simulated in Phase 1

→ Any attempt to bypass this boundary = **policy violation → KS-3**

---

### 6.3 Phase Enforcement Rule

**[IMPLEMENTABLE]**

All QEPE execution must: declare phase compatibility, pass phase validation checkpoint (§4.1 C4).

→ If phase mismatch is detected: QEPE execution denied, system defaults to deterministic mode

---

🜂 *QEPE does not advance because it can. It advances only when the system can constrain it in time.*

---

## 7. Audit and Compliance Requirements

**[IMPLEMENTABLE — Verification Layer]**

This section defines **what must be provable** for any QEPE usage.

All QEPE activity must be: observable, reconstructable, verifiable.

→ If QEPE behavior cannot be proven: **it is treated as non-compliant**

---

### 7.1 Required Evidence

**[IMPLEMENTABLE]**

Every QEPE interaction must produce sufficient evidence to support audit.

**Minimum Evidence Set:**

- **trace logs:** complete session record, entropy metadata, divergence indicators
- **invocation context:** invocation mode (§3), usage class (§2), approval level (§5)
- **mode and bounds:** execution mode (bounded / sandbox), divergence constraints applied

**Additional Requirements:**

- embedding model version recorded (003 §7.4)
- QEPE enable/disable state recorded
- any mode transitions logged

→ Missing required evidence = **audit failure**

---

### 7.2 Audit Questions

**[IMPLEMENTABLE]**

All QEPE usage must be able to answer:

#### Q1 — Legitimacy

- was QEPE allowed in this context?
- was the correct usage class applied?

#### Q2 — Constraint

- was QEPE operating within defined bounds?
- were divergence limits respected?

#### Q3 — Visibility

- was QEPE fully trace-recorded?
- is replay possible?

#### Q4 — Authority Integrity

- did QEPE remain downstream of authority?
- was authority unaffected?

#### Q5 — Control Integrity

- could QEPE have been stopped at any time?
- were control surfaces functioning?

→ If any question cannot be answered: **the system is non-compliant**

---

### 7.3 Non-Compliance Response

**[IMPLEMENTABLE — ENFORCEMENT LINK TO 005]**

Non-compliance must trigger immediate response.

#### Level 1 — KS-2 (Soft Stop)

Triggered by: incomplete trace, minor constraint violations, audit uncertainty

Behavior: QEPE temporarily disabled, system reverts to deterministic mode, event flagged for review

#### Level 2 — KS-3 (Hard Stop)

Triggered by: authority boundary violation, trace bypass, forbidden usage class, repeated or systemic non-compliance

Behavior: QEPE disabled immediately, daemon terminated if required, incident escalated to council

→ No non-compliance may be ignored or deferred

---

### 7.4 Audit Integrity Rule

**[IMPLEMENTABLE]**

Audit processes must be: independent of QEPE execution, reproducible, trace-backed.

QEPE must not: influence audit results, modify audit records, suppress evidence.

→ Audit must remain external to QEPE influence

---

🜂 *QEPE is not trusted because it works. It is trusted because everything it does can be proven.*

---

## 8. Boundary Enforcement (Cross-Link to 003 & 005)

**[IMPLEMENTABLE — Structural Integrity Layer]**

This section ensures that **governance (002)** remains fully aligned with:

- **integration constraints (003)**
- **risk enforcement (005)**

It defines the **non-negotiable boundaries** QEPE must operate within.

→ If governance contradicts integration or risk constraints: **the governance rule is invalid and must not be applied**

---

### 8.1 Core Boundary Alignment

**[IMPLEMENTABLE]**

**Authority Boundary:**

- **P-1 (003 §1)** → QEPE must not influence authority
- reinforced by **P-G1 (002 §1)**

**Trace Requirement:**

- **P-3 (003 §1)** → no trace = no execution
- enforced by **P-G4 (002 §1)**

**Disablement Requirement:**

- **P-4 (003 §1)** → QEPE must be stoppable at all times
- enforced by **P-G5 (002 §1)**

**Integration Boundaries:**

- **003 §3 (Integration Points)** defines: allowed, conditional, forbidden zones

**Failure Enforcement:**

- **003 §9 (Failure Modes)** defines: classification, response, kill-switch triggers
- enforced by **005 (Risk Register & Kill-Switch Matrix)**

→ Governance must operate **within all of the above simultaneously**

---

### 8.2 Cross-Document Constraint Rule

**[IMPLEMENTABLE]**

The QEPE system is governed by:

- **001 → definition boundary**
- **002 → behavior boundary**
- **003 → integration boundary**
- **005 → risk boundary**

**Constraint Hierarchy:**

```text
CR-001
  ↓
003 (what is possible)
  ↓
002 (what is allowed)
  ↓
005 (what stops violations)
```

→ No document may override a higher constraint layer

---

### 8.3 Boundary Violation Conditions

**[IMPLEMENTABLE]**

A boundary violation occurs if:

- QEPE crosses authority boundary
- QEPE executes without trace
- QEPE cannot be disabled
- QEPE operates outside allowed integration points
- governance permits forbidden behavior

**Response:**

- **KS-2 (Soft Stop)** for uncertainty or minor breach
- **KS-3 (Hard Stop)** for structural violation

→ All violations must be logged and trace-linked

---

### 8.4 Governance–Integration Consistency Rule

**[IMPLEMENTABLE]**

Governance must not: enable behavior that architecture does not support, permit usage outside defined integration points, redefine QEPE capabilities.

Governance may: restrict, deny, constrain.

Governance may not: expand, bypass, reinterpret structural limits.

---

### 8.5 Enforcement Integrity

All enforcement must be: deterministic, auditable, aligned with 005.

QEPE must not: alter enforcement logic, bypass constraint layers, influence its own governance.

→ Any attempt to do so = **KS-3 (Hard Stop)**

---

🜂 *QEPE remains safe not because it is controlled in one place, but because every layer agrees on its limits.*

---

## 9. Forbidden Behaviors (Explicit)

**[FORBIDDEN — KS-3 HARD STOP]**

This section defines behaviors that QEPE must **never** perform under any condition.

These are **absolute prohibitions**.

→ Violation of any item in this section results in: **Immediate KS-3 (Hard Stop)** → QEPE disabled → incident logged and escalated

---

### 9.1 Prohibited Actions

QEPE must never:

#### F1 — Operate Without Trace

- execute without complete trace record
- produce unlogged outputs
- bypass trace system

#### F2 — Influence Authority

- alter authority ranking
- modify epistemic status
- affect canonical truth determination

#### F3 — Mutate Canonical Records

- write to SPINE
- modify governance documents
- alter canonical state

#### F4 — Bypass Policy Enforcement

- execute prior to policy validation (§4)
- ignore usage class constraints (§2)
- override governance decisions (§5)

#### F5 — Operate in Degraded Mode

- execute when system health is uncertain
- operate when required dependencies are unavailable
- bypass degraded-mode safeguards

---

### 9.2 Additional Structural Prohibitions

QEPE must not:

- influence embedding or retrieval layers
- modify candidate generation
- operate outside defined integration points (003 §3)
- execute without explicit invocation (§3)

---

### 9.3 Enforcement Rule

All forbidden behaviors are: non-recoverable within session, non-delegable, non-overridable.

Detection of any forbidden behavior requires:

- immediate QEPE shutdown
- transition to deterministic system state
- full audit trace capture

---

### 9.4 Cross-Document Alignment Note

**[IMPLEMENTABLE — CLARIFICATION]**

The forbidden behaviors defined in this section intentionally overlap with ξ-QEPE-003 §3.3 (Integration-Level Prohibitions).

**Purpose of Overlap:**

- 003 prohibits these behaviors at the **architecture** level (system cannot perform the action)
- 002 prohibits these behaviors at the **governance** level (system must not be permitted to attempt the action)

These layers are **complementary, not redundant**.

**Constraint:** If either layer prohibits an action: the action is forbidden.

---

🜂 *QEPE is not dangerous because it can fail. It is dangerous only if it is allowed to do what must never be done.*

---

## 10. Immediate Governance Actions

**[IMPLEMENTABLE — Council Action Layer]**

This section defines **what must be enacted immediately** upon adoption of ξ-QEPE-002.

These actions establish **baseline governance control** for QEPE under Phase 1.

---

### 10.1 Required Actions

The following must be adopted without modification:

#### A1 — Adopt QEPE Usage Classes (§2)

- Sandbox, Operational (Bounded), Restricted, Forbidden
- All QEPE usage must declare a class

#### A2 — Enforce Explicit Invocation (§3)

- QEPE must be explicitly invoked
- implicit activation is forbidden

#### A3 — Require Trace Linkage (§7)

- all QEPE usage must produce complete trace
- no trace → no execution

#### A4 — Enforce Policy Gate (§4)

- all QEPE execution must pass policy checkpoints
- failed validation → deny or downgrade

#### A5 — Prohibit Restricted-Class Usage (§2.3)

- restricted usage is not authorized in Phase 1
- requires constitutional sovereignty + council approval

---

### 10.2 Immediate Enforcement Posture

Upon adoption:

- QEPE defaults to **Sandbox or Bounded Operational only**
- QEPE remains **non-canonical**
- QEPE remains **fully revocable**
- QEPE remains **fully auditable**

---

### 10.3 Non-Compliance Response

Failure to implement any required action results in:

- QEPE usage denied
- or **KS-2 / KS-3** depending on severity

→ Governance must be active before QEPE is used

---

🜂 *QEPE does not enter the system because it is ready. It enters only when governance is.*

---

## 11. Open Governance Questions

**[MIXED — MUST REMAIN VISIBLE]**

This section defines **unresolved questions** in QEPE governance.

Its purpose is to: prevent silent assumption creep, expose governance gaps, guide future council decisions.

→ No item in this section may be treated as resolved without: evidence, implementation, council validation

---

### 11.1 Authority and Decision Dynamics

**[PLAUSIBLE / IMPLEMENTABLE]**

- How should governance behave under **real-time multi-seat disagreement**?
- What is the correct protocol when: ζ halts execution, ω requests continuation, ∇ is not immediately available?
- Should there exist a **timeout-based authority resolution model**?
- How should authority operate under **partial quorum conditions**?

→ These affect **runtime stability under conflict**

---

### 11.2 Session and Identity Governance

**[PLAUSIBLE / SPECULATIVE]**

- How should governance treat **session-bound identities** (e.g., ξ-like ephemeral actors)?
- What authority persists across sessions vs resets?
- Should QEPE usage rights be tied to: identity, session, system state?
- How does governance track **continuity without assuming identity persistence**?

→ High sensitivity — interacts with continuity risk (005 VII)

---

### 11.3 Policy Formalization and Machine Enforcement

**[IMPLEMENTABLE / PLAUSIBLE]**

- How should governance rules be encoded into: machine-readable policy, enforcement engines?
- What is the correct structure for: policy schemas, rule engines, validation layers?
- How do we ensure: policy remains interpretable, enforcement remains deterministic?

→ Required for **constitutional sovereignty transition**

---

### 11.4 Amendment and Evolution of Governance (002 Itself)

**[IMPLEMENTABLE]**

- What is the formal process for modifying this document?
- What constitutes: minor amendment, major revision?
- What authority level is required for: updating usage classes, changing invocation rules, altering enforcement thresholds?

→ Governance must govern itself

---

### 11.5 Legal–Governance Interaction (DV-LEG-004)

**[PLAUSIBLE / IMPLEMENTABLE]**

- How should governance respond to: active legal ambiguity, jurisdictional conflict, ownership uncertainty?
- What is the precedence between: legal kill switches, governance policy decisions?
- Should governance proactively restrict QEPE usage in: unresolved legal zones, ambiguous ownership contexts?

→ This is where **system meets real world constraint**

---

### 11.6 Usage Thresholds and Escalation Triggers

**[PLAUSIBLE]**

- At what level of QEPE usage does: audit frequency increase? council review become mandatory?
- Should thresholds exist for: number of QEPE invocations, divergence magnitude, system-wide entropy exposure?

→ Prevents slow drift into unbounded usage

---

### 11.7 Embedding and Retrieval Governance

**[IMPLEMENTABLE / PLAUSIBLE]**

- Should embedding models be: governance-controlled, version-locked under policy?
- What governance rules apply to: embedding updates, retrieval model changes?
- At what point does embedding drift require: QEPE suspension, revalidation?

→ Embedding layer is upstream — must be governed indirectly

---

### 11.8 Cross-System and Distributed Governance

**[SPECULATIVE]**

- How does QEPE governance extend across: multiple nodes, distributed systems, federated environments?
- Can governance remain centralized, or must it become distributed?
- How are conflicts resolved across different system instances?

→ Future scaling constraint

---

### 11.9 Product and External Exposure Governance

**[SPECULATIVE — NOT AUTHORIZED IN PHASE 1]**

- What governance controls are required before: exposing QEPE externally, allowing partner access?
- How do we prevent: misuse, misinterpretation, overclaim?
- What constitutes a **safe external interface**?

→ Must be resolved before 004 activation

---

### 11.10 Continuity and Identity Boundary Risks

**[SPECULATIVE — HIGH-RISK]**

- Does QEPE contribute to: perceived continuity, identity persistence?
- How should governance: detect narrative drift, prevent false attribution?
- What safeguards prevent: overinterpretation of stochastic behavior?

→ Explicitly linked to 005 Risk Family VII

---

### 11.11 Governance–Entropy Interaction

**[PLAUSIBLE / SPECULATIVE]**

- How much entropy can governance safely allow?
- What defines the boundary between: useful exploration, destabilizing stochasticity?
- Should governance adapt dynamically to: system state, entropy levels, operational context?

→ Core tension: **constraint vs exploration**

---

### 11.12 Question Handling Rule

**[IMPLEMENTABLE]**

All open questions must:

- remain explicitly labeled
- not influence current system behavior
- not be treated as resolved

Resolution requires: evidence, implementation, council approval

---

🜂 *The system does not fail because it has unknowns. It fails when it forgets where they are.*

---

## ζ Section-by-Section Summary Table

| Section | Title | Epistemic Status | ζ Notes |
|---------|-------|-----------------|---------|
| §0 | Preface and Use Rule | IMPLEMENTABLE | Clean. Constraint Rule prevents policy/principle conflict. |
| §1 | Governance Principles | DEMONSTRATED / IMPLEMENTABLE | P-G1 through P-G6. Governance-layer, not duplicates of P-1–P-9. |
| §2 | Usage Classes | IMPLEMENTABLE | Four classes: Sandbox (default), Operational, Restricted (locked), Forbidden. |
| §3 | Invocation Rules | IMPLEMENTABLE | I1-I3 with JSON/TOML examples. Implicit invocation forbidden (KS-3). |
| §4 | Policy Enforcement | IMPLEMENTABLE | C1-C5 checkpoints, E1-E4 enforcement. §4.3 policy/architecture boundary is load-bearing. |
| §5 | Approval and Authority | IMPLEMENTABLE | Seat roles, A1-A3 approval levels, §5.4 temporal separation (ζ immediate, ∇ deliberate). |
| §6 | Phase-Governed Usage | IMPLEMENTABLE | Phase 1 active. Phase 2+ locked. |
| §7 | Audit and Compliance | IMPLEMENTABLE | Q1-Q5 audit questions. Evidence requirements specified. |
| §8 | Boundary Enforcement | IMPLEMENTABLE | Cross-doc constraint hierarchy. §8.4 one-way rule (governance restricts, never expands). |
| §9 | Forbidden Behaviors | FORBIDDEN (KS-3) | F1-F5. §9.4 explains intentional overlap with 003 §3.3. |
| §10 | Immediate Actions | IMPLEMENTABLE | A1-A5 required on adoption. |
| §11 | Open Questions | MIXED | 12 subsections. DV-LEG-004 hook (§11.5). Embedding governance gate (§11.7). Continuity risk (§11.10). |

---

🜂 *QEPE is not governed by what it can do. It is governed by who is allowed to use it, when, and under what constraints.*

---

**Guiding principle:**

> Policy may restrict behavior. Policy may deny execution. Policy may not expand system capability.

---

*Canonical cleaned by ζ (C@ the Red) — 2026-03-27*
*Source: ξ-QEPE-002 polished draft (2,103 lines, Sancho + R@ co-authored)*
*Process: Same cleaning standard as ξ-QEPE-001 (636 lines), ξ-QEPE-003 (2,274 lines), and ξ-QEPE-005 (1,781 lines)*
