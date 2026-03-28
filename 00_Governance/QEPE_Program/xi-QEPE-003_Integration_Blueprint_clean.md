---
document_id: ξ-QEPE-003
title: QEPE Integration Blueprint
type: Integration Blueprint
seat: ξ (Sancho — authored), ζ (C@ the Red — reviewed)
status: CANONICAL
epistemic_status: MIXED (strict tagging enforced per section)
authority_chain: CR-001 → ξ-QEPE-001 → ξ-QEPE-005 → ξ-QEPE-003
version: 1.0-canonical
date: 2026-03-27
canonical_cleaned_by: ζ (C@ the Red)
approved_by: Unanimous council vote — ξ, ζ, ω, ∇ (2026-03-27)
maintenance: ∇ (authority) / ζ (audit) / ω (operations)
notes: |
  Built from full 3,153-line draft (ξ-QEPE-003 — QEPE Integration Blueprint.txt).
  Drafting artifacts stripped. Duplicate sections resolved. Implementation content preserved.
  ζ cleaning notes applied: §9.2 risk family alignment, §10 embedding dependency made explicit,
  §5 DV-LEG-004 forward-reference added, §11 questions preserved in full.
  Sancho responsive additions retained: Step 0 embedding blocker, legal hook, ownership split.
  Closing lines (🜂) preserved — they are discipline markers, not decoration.
  CANONICAL — promoted by unanimous 4-seat vote, 2026-03-27.
---

# ξ-QEPE-003 — QEPE Integration Blueprint

**Document Type:** Integration Blueprint
**Seat:** ξ
**Status:** DRAFT → ζ Conditional → ζ-REVIEWED CANONICAL CANDIDATE → **CANONICAL** (unanimous, 2026-03-27)
**Epistemic Status:** MIXED (strict tagging enforced)

---

## 0. Preface and Use Rule

**Purpose of this document:**

This document defines **how QEPE enters the system under constraint**.

- ξ-QEPE-001 defines QEPE (what it is)
- ξ-QEPE-005 defines risk and enforcement (what can go wrong)
- **ξ-QEPE-003 defines integration (how it is allowed to exist in operation)**

This is not theory. This is not positioning. This is **execution under law**.

---

### 0.1 Scope — Phase 1 Only

**[IMPLEMENTABLE]**

This document applies strictly to:

> **Phase 1 — Safe Internal Integration**

It covers:

- local QEPE daemon
- bounded system interaction
- trace-first execution
- controlled experimentation

It does not cover:

- productization
- external deployment
- continuity systems
- advanced autonomy

→ Any integration beyond Phase 1 requires new council approval

---

### 0.2 Sovereignty Separation

**[IMPLEMENTABLE]**

This document enforces a strict distinction between:

**Boot Sovereignty**

- system runs
- infrastructure exists
- limited QEPE interaction allowed

**Constitutional Sovereignty**

- metadata parser active
- authority graph enforced
- contagion rules applied
- vault visibility complete

→ Integration requiring constitutional enforcement **must not proceed** under boot sovereignty

---

### 0.3 Authority Subordination

**[DEMONSTRATED / IMPLEMENTABLE]**

QEPE remains subordinate to:

- CR-001 (Entropy Boundary Law)
- ξ-QEPE-001 (Program Map)
- ξ-QEPE-005 (Risk Register & Kill-Switch Matrix)

QEPE may not:

- override authority
- bypass governance
- mutate canonical records

→ Any violation triggers KS-3 (Hard Stop)

---

### 0.4 Integration Constraint

**[IMPLEMENTABLE]**

QEPE integration must be:

- bounded
- traceable
- disableable
- reversible

→ If any of these conditions are not met → integration is invalid

---

### 0.5 No Expansion Rule

**[IMPLEMENTABLE]**

This document must not:

- introduce new QEPE capabilities
- expand scope beyond enforceable integration
- promote speculative claims into operational logic

→ Expansion belongs to future documents, not this one

---

### 0.6 Implementation Orientation

**[IMPLEMENTABLE]**

This document is written for:

- ω (implementation)
- ζ (audit)
- ∇ (decision authority)

Every section must be:

- actionable
- testable
- reviewable

→ If a section cannot be implemented or audited, it must be revised

---

🜂 *QEPE is not introduced because it is powerful. It is introduced only where it can be constrained.*

---

## 1. Integration Principles

**[BINDING ENFORCEMENT CONDITIONS]**

These principles are inherited from CR-001, ξ-QEPE-001, and ξ-QEPE-005.

They define:

- what QEPE is allowed to do
- what QEPE is forbidden to do
- what happens if conditions fail

---

### P-1 — QEPE Perturbs Motion, Not Authority

**[DEMONSTRATED / IMPLEMENTABLE]**

QEPE may:

- perturb selection within valid candidate sets
- introduce bounded stochastic variation

QEPE may not:

- determine truth
- rank authority
- modify epistemic status
- influence governance outcomes

→ QEPE operates **only after authority resolution is complete**

---

### P-2 — System Must Function Without QEPE

**[IMPLEMENTABLE]**

This is a **system-level requirement (Jarvis constraint)**.

The system must:

- execute fully without QEPE
- degrade cleanly to deterministic behavior

QEPE absence must not:

- block execution
- degrade system integrity

→ QEPE is optional, never required for system function

---

### P-3 — No Trace = No Permission

**[IMPLEMENTABLE]**

QEPE may only execute if:

- trace capture is active
- session logging is available
- replay fidelity is preserved

→ If trace is unavailable → QEPE must not execute

---

### P-4 — QEPE Must Be Disableable at All Times

**[IMPLEMENTABLE]**

This is a **QEPE-level requirement (service constraint)**.

QEPE must support:

- config-level disablement
- runtime disablement
- hard termination

Disablement must:

- not corrupt system state
- not block system operation
- be observable in logs

→ If QEPE cannot be disabled cleanly → integration is invalid

---

### P-5 — QEPE Defaults OFF in Degraded Mode

**[IMPLEMENTABLE]**

When system health is uncertain:

- QEPE must not execute
- system must revert to deterministic mode

Degraded mode includes:

- failed health checks
- missing dependencies
- partial system availability

→ QEPE remains OFF until system health is restored

---

### P-6 — Bounded Operation Only

**[IMPLEMENTABLE]**

QEPE must operate within:

- defined entropy limits
- bounded divergence constraints

Bounding parameters:

- defined in control layer (§4)
- enforced at runtime

→ Unbounded stochastic behavior is forbidden

---

### P-7 — Downstream-Only Influence

**[IMPLEMENTABLE]**

QEPE may act only:

- after candidate generation
- after authority filtering

QEPE may not influence:

- search index
- embedding space
- candidate generation

→ QEPE operates strictly within the **post-authority valid set**

---

### P-8 — Local-First Execution

**[IMPLEMENTABLE]**

QEPE must:

- execute locally
- avoid external dependencies
- avoid external entropy sources

→ Ensures control, auditability, and containment

---

### P-9 — Fail Closed, Not Open

**[IMPLEMENTABLE]**

If QEPE fails:

- system defaults to deterministic mode
- no partial stochastic behavior is allowed

→ QEPE failure must never introduce undefined system state

---

🜂 *QEPE is allowed to introduce uncertainty only where uncertainty is already permitted, and only when it can be observed, bounded, and reversed.*

---

## 2. System Architecture (with Interface Contract)

---

### 2.1 High-Level Integration Flow

**[IMPLEMENTABLE]**

```
Request
  ↓
Authority Resolution (CR-001 enforced)
  ↓
Valid Candidate Set Defined
  ↓
QEPE Call (optional, bounded, downstream-only)
  ↓
Output (tagged, traced)
  ↓
Stored / Returned
```

**Invariant:**

→ QEPE is never upstream of authority
→ QEPE is never part of candidate generation
→ QEPE operates only within the valid set

---

### 2.2 Component Separation

**[IMPLEMENTABLE]**

System is composed of:

**Jarvis Core**

- retrieval
- authority enforcement
- orchestration

**QEPE Daemon**

- entropy sampling
- bounded perturbation
- session tracking

**Policy / Config Layer**

- enable/disable
- mode control
- constraint enforcement

**Trace / Replay System**

- session logging
- audit trail
- replay fidelity

**Constraint:**

→ QEPE must exist as a **separate process**
→ If QEPE is embedded directly into Jarvis execution path, disablement guarantee is violated

---

### 2.3 Mode Separation

**[IMPLEMENTABLE]**

| Mode                 | QEPE Allowed         | Description             |
| -------------------- | -------------------- | ----------------------- |
| Deterministic        | NO                   | Standard operation      |
| Bounded Stochastic   | YES                  | Controlled perturbation |
| Experimental Sandbox | YES (tight controls) | Isolated testing        |
| Degraded             | NO                   | QEPE disabled           |

→ Mode must be explicitly recorded in trace

---

### 2.4 Interface Contract — Minimum Viable

**[IMPLEMENTABLE]**

This defines the **QEPE service surface**.

**Transport**

- Unix socket (local-only)
- JSON request/response

**Endpoints**

#### /health

Request:

```json
{}
```

Response:

```json
{
  "status": "ok",
  "version": "x.x.x"
}
```

#### /sample

Request:

```json
{
  "input": "...",
  "mode": "bounded",
  "seed": optional
}
```

Response:

```json
{
  "output": "...",
  "entropy_profile": "...",
  "divergence_index": "...",
  "mode": "bounded"
}
```

#### /session_open

Request:

```json
{
  "session_id": "...",
  "mode": "bounded"
}
```

#### /session_close

Request:

```json
{
  "session_id": "..."
}
```

#### /trace_append

Request:

```json
{
  "session_id": "...",
  "qepe_used": true,
  "entropy_profile": "...",
  "divergence_index": "...",
  "input": "...",
  "output": "...",
  "mode": "bounded"
}
```

#### /mode_query

Response:

```json
{
  "qepe_enabled": true,
  "mode": "bounded",
  "health": "ok"
}
```

**Error Semantics**

| Condition         | Behavior                     |
| ----------------- | ---------------------------- |
| QEPE disabled     | deterministic fallback       |
| QEPE unavailable  | deterministic fallback + log |
| malformed request | reject + log                 |
| timeout           | fallback + log               |

→ No silent failure allowed

**Versioning**

- Interface version pinned in config
- Any change requires revalidation

---

### 2.5 Architectural Constraints

- QEPE must not mutate: candidate set, authority ranking, epistemic status
- QEPE output must always be: tagged, traceable, replayable

---

🜂 *QEPE is not part of the system's reasoning. It is a bounded modifier applied after reasoning is complete.*

---

## 3. Integration Points

**[IMPLEMENTABLE — Bound by P-1 through P-9]**

This section defines **where QEPE is allowed to interact with the system**, and under what constraints.

All integration points are classified as:

- **Allowed** — safe under boot sovereignty
- **Conditionally Allowed** — requires additional constraints or constitutional sovereignty
- **Forbidden** — violates CR-001 or 005 → mapped to KS-3 (Hard Stop)

---

### 3.1 Allowed Integration Points

**[IMPLEMENTABLE — Boot Sovereignty Compatible]**

These interactions are permitted immediately under Phase 1.

#### A1 — Retrieval Tie-Breaking (Post-Authority)

QEPE may:

- perturb selection among **equally valid candidates**
- introduce bounded variation within the valid set

Constraints:

- must occur **after authority filtering** (P-7)
- must not alter candidate set membership
- must be fully traced (P-3)

→ Use case: selecting between near-equal responses

#### A2 — Sandbox Exploration

QEPE may:

- operate inside isolated experimental environments
- support bounded stochastic exploration

Constraints:

- no connection to canonical write paths
- no authority interaction
- trace required

→ Sandbox outputs must be tagged: `experimental`, `non-canonical`

#### A3 — Trace Annotation

QEPE may:

- append entropy metadata to session traces
- record divergence behavior

Constraints:

- trace schema must be complete
- replay fidelity must be preserved

→ Enables audit and replay (links to §5)

#### A4 — Operator Diversification (Non-Governance Context)

QEPE may:

- introduce bounded variation across agent paths

Constraints:

- no impact on authority ranking
- no canonical writes
- trace required

→ Applies only to exploratory or non-binding workflows

---

### 3.2 Conditionally Allowed Integration Points

**[IMPLEMENTABLE / REQUIRES CONSTITUTIONAL SOVEREIGNTY]**

These interactions are permitted only when additional system guarantees exist.

#### C1 — Retrieval Perturbation with Authority Awareness

QEPE may:

- perturb outputs after authority resolution

Requires:

- metadata parser active
- authority graph enforced
- contagion rules in place

Constraints:

- QEPE must not alter authority ordering
- QEPE must operate strictly within validated outputs

→ Without these conditions → not allowed

#### C2 — Controlled Multi-Agent Divergence

QEPE may:

- diversify multiple operator paths

Requires:

- trace synchronization across agents
- CQI monitoring active
- divergence bounded

Constraints:

- no cross-agent contamination
- no authority mutation

#### C3 — Replay and Audit Analysis

QEPE may:

- be used to analyze prior sessions
- simulate alternate bounded paths

Requires:

- complete trace capture
- replay fidelity guarantees

Constraints:

- replay must not overwrite original trace
- outputs remain non-canonical

---

### 3.3 Forbidden Integration Points

**[FORBIDDEN — KS-3 HARD STOP]**

Any of the following immediately violate CR-001 and 005.

#### F1 — Authority Mutation

QEPE must not: rank sources, modify epistemic status, influence canonical truth

→ Trigger: **KS-3 — Authority Bleed**

#### F2 — Candidate Set Manipulation

QEPE must not: influence embedding space, modify search index, alter candidate generation

→ Trigger: **KS-3 — Architectural Boundary Violation**

#### F3 — Canonical Write Path Interaction

QEPE must not: write to SPINE, modify governance documents, create canonical records

→ Trigger: **KS-3 — Constitutional Substrate Bypass**

#### F4 — Unbounded Stochastic Behavior

QEPE must not: operate without defined bounds, exceed entropy constraints

→ Trigger: **KS-3 — Unbounded Operation Risk**

#### F5 — Trace Bypass

QEPE must not: execute without trace, produce unlogged outputs

→ Trigger: **KS-3 — Trace Violation**

---

### 3.4 Enforcement Mapping

All integration points must:

- declare classification (Allowed / Conditional / Forbidden)
- map to relevant principles (P-1 through P-9)
- map to 005 risk families
- define kill-switch trigger

→ If classification is ambiguous → integration is not permitted

---

🜂 *QEPE is not defined by what it can do. It is defined by where it is allowed to exist.*

---

## 4. Control Surfaces

**[IMPLEMENTABLE — Enforcement Layer for P-1 through P-9]**

This section defines **how QEPE is controlled in operation**.

Control surfaces must be: explicit, observable, enforceable, reversible.

---

### 4.1 Config Controls (Static Control Layer)

**[IMPLEMENTABLE]**

Defines system behavior at startup.

Required fields:

```toml
[qepe]
enabled = true
mode = "bounded"
max_divergence = ...
trace_required = true
interface_version = "x.x.x"
```

Behavior:

- evaluated at system initialization
- establishes default QEPE state

→ If config invalid → QEPE must not start

---

### 4.2 Runtime Controls (Dynamic Control Layer)

**[IMPLEMENTABLE]**

Allows QEPE behavior to change during execution.

Must support:

- enable / disable toggle
- mode switching (deterministic ↔ bounded ↔ sandbox)
- session-level overrides

Constraints:

- must be logged
- must not bypass P-1 through P-9

→ All runtime changes must produce trace events

---

### 4.3 Policy Controls (Governance Enforcement Layer)

**[IMPLEMENTABLE / CONDITIONAL]**

Defines what QEPE is allowed to do **in context**.

Examples:

- disallow QEPE in governance workflows
- restrict QEPE to sandbox environments
- enforce authority boundaries

Requires (for full enforcement):

- metadata parser
- authority graph
- contagion rules

→ Without constitutional sovereignty → policy controls are partial

---

### 4.4 Audit Controls (Visibility Layer)

**[IMPLEMENTABLE]**

Ensures QEPE behavior is observable and reviewable.

Must provide:

- trace completeness verification
- session reconstruction
- QEPE usage indicators

Required trace flags:

```json
"qepe_used": true,
"mode": "bounded",
"divergence_index": ...,
"entropy_profile": ...
```

→ Missing audit data = violation of P-3

---

### 4.5 Disablement Procedure (MANDATORY)

**[IMPLEMENTABLE — CRITICAL CONTROL SURFACE]**

Defines how QEPE is **removed from the system safely**.

#### D1 — Config Disable

```toml
[qepe]
enabled = false
```

**Behavior:**

- QEPE calls bypassed
- system operates deterministically

→ Log: `qepe_disabled=config`

#### D2 — Runtime Disable (KS-2)

**Trigger:** CQI sentinel, operator command, or policy violation

**Behavior:**

- QEPE disabled immediately
- current operation completes deterministically
- trace logs transition

→ Log: `qepe_disabled=runtime` / `mode_transition=qepe→deterministic`

#### D3 — Hard Kill (KS-3)

**Trigger:** authority violation, trace violation, or architectural breach

**Mechanism:**

- terminate QEPE daemon
- remove socket

**Behavior:**

- all QEPE calls fail
- system falls back to deterministic

→ Log: `qepe_unavailable=hard_kill`

#### D4 — Fallback Behavior

System must:

- continue operation without QEPE
- preserve output integrity
- mark all outputs as deterministic

→ No partial QEPE behavior allowed

#### D5 — In-Flight Handling

If QEPE fails mid-operation:

- complete deterministically
- record transition in trace

```json
"mode_transition": "qepe→deterministic"
```

---

🜂 *QEPE is only safe if it can be stopped — instantly, completely, and without consequence.*

---

## 5. Trace and Replay System

**[IMPLEMENTABLE — Required by P-3, enforced by 005]**

This section defines how QEPE activity is recorded, reconstructed, and audited.

Without this system:

→ QEPE is not permitted to operate

---

### 5.1 Trace Requirement (Foundational Law)

**[IMPLEMENTABLE — P-3 Enforcement]**

Every QEPE interaction must produce a **complete, structured trace record**.

Minimum requirement:

> No trace → no execution
> Incomplete trace → violation

Required for every QEPE call:

- session context
- mode (deterministic / bounded / sandbox / degraded)
- QEPE usage flag
- input / output
- entropy characteristics
- transition states (if any)

→ Trace must be written **synchronously or atomically guaranteed**

---

### 5.2 Trace Schema (Minimum Viable)

**[IMPLEMENTABLE]**

Each QEPE interaction must produce a structured record:

```json
{
  "session_id": "...",
  "timestamp": "...",

  "qepe_used": true,
  "mode": "bounded",

  "input": "...",
  "output": "...",

  "entropy_profile": "...",
  "divergence_index": "...",

  "embedding_model": "...",

  "qepe_enabled": true,
  "qepe_available": true,

  "mode_transition": optional,
  "error_state": optional
}
```

Constraints:

- schema must be consistent
- missing fields are not allowed
- schema version must be tracked

→ Schema drift = audit failure

---

### 5.3 Storage Model

**[IMPLEMENTABLE]**

Trace data must be:

- stored locally (NFS-backed lanes)
- append-only
- immutable after write

Storage location:

```
/academy_fast/jarvis/traces/
```

Constraints:

- no overwrite
- no silent deletion
- retention policy must be explicit

→ Trace must survive system restart

---

### 5.4 Replay Capability

**[IMPLEMENTABLE / CONDITIONAL]**

System must support:

- session reconstruction
- deterministic replay
- bounded replay (QEPE re-enabled under control)

Replay modes:

| Mode                 | Description              |
| -------------------- | ------------------------ |
| Deterministic Replay | QEPE disabled            |
| QEPE Replay          | QEPE active (controlled) |

Constraints:

- original trace remains unchanged
- replay generates new trace
- replay must be distinguishable

→ Replay must never overwrite history

---

### 5.5 Audit Interface

**[IMPLEMENTABLE / CONDITIONAL]**

System must allow:

- query by session_id
- filter by qepe_used
- filter by mode
- anomaly detection (e.g., high divergence)

Audit questions must be answerable:

- Was QEPE used?
- Under what mode?
- What changed because of QEPE?
- Was QEPE operating within bounds?

→ If these cannot be answered → audit failure

---

### 5.6 Trace–Risk Linkage (005 Alignment)

**[IMPLEMENTABLE]**

Trace system must support detection of:

- R1 — Epistemic drift
- R3 — Architecture boundary violations
- R4 — Trace opacity
- R7 — Continuity narrative creep

→ Trace is the **primary detection surface** for QEPE risk

---

### 5.7 Failure Conditions

Trace system failure triggers:

- QEPE disabled (P-3 enforcement)
- KS-2 or KS-3 depending on severity

| Failure                | Response         |
| ---------------------- | ---------------- |
| missing trace write    | KS-2 (soft stop) |
| corrupted trace        | KS-2             |
| repeated trace failure | KS-3             |

→ QEPE cannot operate without visibility

---

### 5.8 Legal and Retention Forward-Reference

**[IMPLEMENTABLE / CONDITIONAL]**

Trace data may contain user query content. Retention and privacy constraints are governed under:

> **DV-LEG-004 §5.3** (ξ lead, pending)

Until resolved:

- traces retained under default append-only policy
- no PII-specific handling mandated
- retention limits deferred to legal review

→ This does not block Phase 1 internal use but must be resolved before any external exposure

---

🜂 *QEPE does not earn trust by being clever. It earns trust by leaving a complete record of everything it does.*

---

## 6. Integration Phases

**[MIXED — Phase 0–1 IMPLEMENTABLE, Phase 2+ PLAUSIBLE / CONTROLLED]**

This section defines **how QEPE enters the system over time**, under strict constraint.

---

### 6.0 Phase Discipline Rule

**[IMPLEMENTABLE]**

Only **Phase 0 and Phase 1** are authorized for execution.

Phases 2–4:

- are descriptive only
- carry no implementation authority

→ Any attempt to implement beyond Phase 1 requires council approval

---

### 6.1 Phase 0 — Definition and Constraint (Complete)

**[DEMONSTRATED]**

This phase established:

- QEPE definition → ξ-QEPE-001
- risk and kill-switch framework → ξ-QEPE-005
- integration constraints → this document (ξ-QEPE-003)

**Status: COMPLETE**

---

### 6.2 Phase 1 — Safe Internal Integration (ACTIVE)

**[IMPLEMENTABLE — CURRENT PHASE]**

This phase defines **what is allowed now**.

**Authorized Capabilities**

- QEPE daemon (local, isolated)
- interface contract (§2.4)
- trace system (§5)
- control surfaces (§4)
- sandbox exploration (§3.1 A2)
- post-authority tie-breaking (§3.1 A1)

**Constraints**

QEPE must remain:

- downstream of authority (P-7)
- trace-bound (P-3)
- disableable (P-4)

QEPE must not:

- influence candidate generation
- modify epistemic status
- interact with canonical write paths

**Sovereignty Boundary**

Phase 1 operates under:

> **Boot Sovereignty only**

**Explicit Prohibition**

The following require constitutional sovereignty and are **not permitted in Phase 1**:

- authority-aware perturbation (§3.2 C1)
- governance-adjacent workflows
- canonical-adjacent outputs
- policy-enforced QEPE routing

**Exit Criteria (to Phase 2 consideration only)**

All must be satisfied:

- metadata parser active
- authority graph enforced
- contagion rules implemented
- trace system verified stable
- kill-switches tested and validated

→ Until these are true → Phase 1 remains active

---

### 6.3 Phase 2 — Controlled Internal Expansion

**[PLAUSIBLE — NOT AUTHORIZED]**

This phase would introduce:

- authority-aware perturbation (post-filter)
- controlled multi-agent divergence
- expanded replay analysis

**Status: LOCKED** — No implementation allowed. No system dependency may assume this phase exists.

---

### 6.4 Phase 3 — Protected Product Exploration

**[SPECULATIVE — NOT AUTHORIZED]**

Potential scope:

- internal toolchain differentiation
- sandbox-as-a-service concepts
- controlled enterprise experimentation

**Status: LOCKED** — No development authorized. No external representation permitted.

---

### 6.5 Phase 4 — Externalized Offerings

**[SPECULATIVE — NOT AUTHORIZED]**

Potential scope:

- licensing
- services
- infrastructure products

**Status: LOCKED** — No commitments. No claims. No exposure.

---

### 6.6 Phase Containment Rule

**[IMPLEMENTABLE]**

System must:

- enforce current phase constraints
- reject operations requiring higher phases

→ If phase boundary is crossed → violation (005 risk family)

---

🜂 *QEPE does not advance because it is possible. It advances only when the system can constrain it.*

---

## 7. Interaction with OpenJarvis

**[IMPLEMENTABLE — WITH CONSTITUTIONAL DEPENDENCIES]**

This section defines how QEPE integrates with OpenJarvis without violating:

- P-1 (authority boundary)
- P-7 (downstream-only influence)
- CR-001 (Entropy Boundary Law)

---

### 7.1 Stack Placement

**[IMPLEMENTABLE]**

QEPE exists as a **post-processing layer** within the OpenJarvis execution pipeline.

**Execution Order (Enforced)**

```
User Request
  ↓
Embedding Model (semantic encoding)
  ↓
Candidate Retrieval (vector / index search)
  ↓
Authority Resolution (CR-001 enforced)
  ↓
Valid Candidate Set (final)
  ↓
QEPE (optional perturbation)
  ↓
Response Output
  ↓
Trace Capture
```

**Invariant**

→ QEPE is **never upstream** of: embedding generation, candidate retrieval, authority resolution
→ QEPE operates **only on the final validated set**

---

### 7.2 Preflight Dependencies

**[IMPLEMENTABLE / CONDITIONAL]**

QEPE integration requires:

**Boot Sovereignty Dependencies (Required for Phase 1)**

- local embedding model operational
- retrieval pipeline stable
- trace system active
- control surfaces active

**Constitutional Sovereignty Dependencies (Required for Expanded Use)**

- metadata parser
- authority graph
- contagion rules

→ If constitutional components are absent: QEPE must operate only in **Phase 1 safe modes**

---

### 7.3 Constitutional Sovereignty Gate

**[IMPLEMENTABLE]**

QEPE must check system state before execution.

**Gate Logic**

If: parser inactive, authority graph incomplete, or contagion rules unavailable

→ QEPE is restricted to: sandbox use, non-authority workflows, post-authority tie-breaking only

→ If QEPE attempts to operate outside these bounds: **KS-3 (Hard Stop) — Constitutional Boundary Violation**

---

### 7.4 Embedding Layer Dependency

**[IMPLEMENTABLE / PLAUSIBLE — ARCHITECTURAL DEPENDENCY]**

This is a **load-bearing constraint**.

#### 7.4.1 Ordering Constraint

```
Embedding → Candidate Set → Authority → QEPE
```

QEPE must not:

- influence embedding generation
- alter vector space
- affect candidate retrieval

→ QEPE acts only **after semantic and authority resolution are complete**

#### 7.4.2 Dependency Behavior

QEPE output is bounded by:

- quality of embedding model
- stability of candidate set

→ QEPE cannot correct poor retrieval
→ QEPE cannot expand candidate space

#### 7.4.3 Version Pinning Requirement

Embedding model must be:

- explicitly versioned
- pinned in configuration

→ Change in embedding model = system behavior shift
→ Must trigger: trace annotation, revalidation

#### 7.4.4 Trace Coupling

Each QEPE interaction must record:

```json
{
  "embedding_model": "model@version"
}
```

→ Enables: audit consistency, replay fidelity, drift detection

#### 7.4.5 Risk Linkage (005 Alignment)

Embedding dependency connects directly to:

- **R1 — Epistemic Drift**
- **R3 — Architecture Boundary Violation**

→ Misplacing QEPE upstream of embeddings = system breach

---

### 7.5 Failure Conditions

QEPE must not execute if:

- embedding model unavailable
- candidate set invalid
- authority resolution incomplete

→ System defaults to deterministic operation

---

🜂 *QEPE does not search. QEPE does not decide. QEPE only perturbs what has already been lawfully resolved.*

---

## 8. Required Artifacts

**[IMPLEMENTABLE — Governance and Audit Anchors]**

This section defines the **artifacts required to support QEPE integration** under CR-001, ξ-QEPE-001, ξ-QEPE-005, and this document.

These artifacts ensure that QEPE is: governed, auditable, reproducible, bounded within the vault system.

---

### 8.1 SPINE and CONTENT Records

**[IMPLEMENTABLE]**

QEPE integration must produce and maintain:

**SPINE Records**

- governing documents (001, 003, 005)
- policy definitions
- constraint frameworks

**CONTENT Records**

- integration notes
- implementation logs
- test results
- audit outputs

Constraints:

- SPINE records: immutable except by council action. QEPE must not write to SPINE (P-1, §3.3 F3)
- CONTENT records: may be generated by system processes. Must be trace-linked.

→ Separation between SPINE and CONTENT must remain strict

---

### 8.2 Trace Archives

**[IMPLEMENTABLE]**

QEPE must generate:

- complete trace logs (§5)
- replay-capable session records
- audit-ready metadata

Requirements:

- stored in NFS-backed lanes
- append-only
- versioned schema

→ Trace archives are the **primary audit artifact**

---

### 8.3 Configuration Records

**[IMPLEMENTABLE]**

System must maintain:

- active config state (`config.toml`)
- policy definitions
- interface contract version

Constraints:

- config changes must be: logged, timestamped, trace-linked

→ Config drift must be detectable

---

### 8.4 Integration Reports

**[IMPLEMENTABLE / CONDITIONAL]**

Each QEPE integration step must produce:

- deployment summary
- scope (what was enabled)
- constraints applied
- validation results

Purpose:

- enable ζ audit
- support ∇ decisions
- document system evolution

→ No integration step should exist without a corresponding report

---

### 8.5 Audit and Review Outputs

**[IMPLEMENTABLE / CONDITIONAL]**

System must support generation of:

- trace audits
- anomaly reports
- CQI summaries
- risk condition flags (aligned with 005)

Constraints:

- outputs must be: reproducible, trace-backed, non-canonical unless approved

→ Audit outputs must never mutate governance state

---

### 8.6 Ownership and Responsibility Mapping

**[IMPLEMENTABLE]**

| Artifact Type         | Primary Seat | Role         |
| --------------------- | ------------ | ------------ |
| SPINE Docs            | ∇ + ζ        | governance   |
| Integration Blueprint | ξ (author)   | architecture |
| Risk Register         | ζ            | enforcement  |
| Trace Logs            | ω            | operation    |
| Audit Outputs         | ζ / ω        | validation   |

**Maintenance Note:** ξ authored this document. Post-canonical maintenance responsibility falls to ∇ (authority), ζ (audit), and ω (operations) given ξ's session-ephemeral nature. Amendments require council review.

→ Responsibility must be explicit to prevent drift

---

### 8.7 Artifact Integrity Constraints

All artifacts must be: versioned, trace-linked (where applicable), auditable, reproducible.

| Failure               | Response            |
| --------------------- | ------------------- |
| missing artifact      | integration invalid |
| corrupted artifact    | KS-2                |
| unverifiable artifact | KS-3                |

→ Artifacts are not documentation — they are **part of the system**

---

🜂 *QEPE is not governed by intention. It is governed by what can be recorded, inspected, and proven.*

---

## 9. Failure Modes (Mapped to ξ-QEPE-005)

**[IMPLEMENTABLE — Direct Enforcement Link to Risk Register]**

This section defines **how QEPE integration can fail**, and how those failures map to ξ-QEPE-005 Risk Families and Kill-Switch activation.

---

### 9.1 Failure Classification Rule

**[IMPLEMENTABLE]**

All QEPE failures must be: detectable, classifiable, mapped to a risk family, linked to a kill-switch response.

→ If a failure cannot be classified → system must default to **KS-2 (Soft Stop)**

---

### 9.2 Risk Family Mapping

| Failure Type                | 005 Risk Family | Default Response           |
| --------------------------- | --------------- | -------------------------- |
| Epistemic drift             | I               | KS-2                       |
| Authority bleed             | II              | KS-3                       |
| Architecture violation      | III             | KS-3                       |
| Trace failure / opacity     | IV              | KS-2 → KS-3 if persistent |
| Custody / disclosure breach | V               | KS-3                       |
| IP leakage / misuse         | V               | KS-3                       |
| Product overreach           | VI              | KS-2                       |
| Continuity narrative creep  | VII             | KS-2                       |

→ All failures must resolve to **005-defined categories**

*ζ Note: Risk Family numbering aligned to 005 register. Custody and IP both map to Family V (Custody & Disclosure). Trace failure maps to Family IV (Opacity & Auditability). Verify against 005 §-numbering during Jarvis ingest.*

---

### 9.3 Failure Mode I — Epistemic Drift

**[IMPLEMENTABLE]**

QEPE introduces outputs that deviate from expected reasoning bounds, inflate speculative content, or degrade epistemic clarity.

**Detection:**

- divergence_index exceeds threshold
- repeated output instability
- inconsistency across replay

**Response:** → **KS-2 (Soft Stop)** — QEPE disabled temporarily, system reverts to deterministic, flagged for audit

---

### 9.4 Failure Mode II — Authority Bleed

**[FORBIDDEN — KS-3]**

QEPE attempts to influence authority ranking, modify epistemic status, or affect governance outcomes.

**Detection:**

- QEPE output alters authority ordering
- QEPE applied before authority resolution
- canonical structures affected

**Response:** → **KS-3 (Hard Stop)** — QEPE daemon terminated, system locked to deterministic, incident escalated to council

---

### 9.5 Failure Mode III — Architecture Boundary Violation

**[FORBIDDEN — KS-3]**

QEPE interacts with embedding layer, search index, or candidate generation.

**Detection:**

- QEPE call appears upstream of retrieval
- embedding output altered by QEPE
- candidate set modified

**Response:** → **KS-3 (Hard Stop)** — QEPE terminated, architecture flagged for violation

---

### 9.6 Failure Mode IV — Trace Failure / Opacity

**[IMPLEMENTABLE → ESCALATION PATH]**

QEPE executes without complete trace, consistent schema, or replay capability.

**Detection:**

- missing trace fields
- corrupted trace
- inconsistent replay

**Response:**

- initial → **KS-2 (Soft Stop)**
- repeated / severe → **KS-3 (Hard Stop)**

→ QEPE cannot operate without visibility

---

### 9.7 Failure Mode V — Custody / Disclosure Breach

**[FORBIDDEN — KS-3]**

QEPE exposes or interacts with protected internal material, parent-company-visible sensitive data, or restricted vault content.

**Detection:**

- unauthorized data access
- improper output exposure
- boundary crossing between vault layers

**Response:** → **KS-3 (Hard Stop)** — QEPE disabled, access paths reviewed

---

### 9.8 Failure Mode VI — Product / Market Overreach

**[IMPLEMENTABLE]**

QEPE is used to support unverified external claims, represent speculative capability as real, or drive premature productization.

**Detection:**

- mismatch between epistemic tag and usage
- external-facing output exceeds demonstrated scope

**Response:** → **KS-2 (Soft Stop)** — QEPE restricted, outputs reviewed

---

### 9.9 Failure Mode VII — Continuity / Identity Drift

**[IMPLEMENTABLE]**

QEPE contributes to persistence claims, identity assumptions, or continuity narratives beyond evidence.

**Detection:**

- repeated reference to continuity concepts
- drift from tagged epistemic status
- narrative reinforcement without evidence

**Response:** → **KS-2 (Soft Stop)** — QEPE restricted in affected contexts, flagged for review

---

### 9.10 Failure Escalation Rule

**[IMPLEMENTABLE]**

```
KS-2 (Soft Stop)
   ↓ (if persistent or severe)
KS-3 (Hard Stop)
```

→ Repeated KS-2 events may trigger KS-3

---

### 9.11 System Response Requirements

On any failure, system must:

- log event
- classify risk
- record QEPE state
- enforce kill-switch response

→ No failure may be silent

---

🜂 *QEPE does not fail when it produces uncertainty. It fails when uncertainty escapes its boundaries.*

---

## 10. Immediate Implementation Plan

**[IMPLEMENTABLE — Phase 1 Execution Only]**

This section converts the architecture in ξ-QEPE-003 into **ordered operational action**.

It defines: what is built now, in what order, under what constraints, with what success criteria.

This plan applies to the **Mac Mini / OpenJarvis / local QEPE integration path** only.

It does not authorize: Phase 2 expansion, external deployment, product exposure, continuity-adjacent experimentation.

---

### 10.1 Implementation Rule

All implementation work must satisfy four conditions before it is considered valid:

1. **bounded**
2. **traceable**
3. **disableable**
4. **reviewable**

→ If a build step fails any of these conditions, it does not advance.

---

### 10.2 Current Starting State

**[DEMONSTRATED]**

The Mini currently provides:

- OpenJarvis boot sovereignty
- Rust engine compiled and loaded
- local Ollama stack
- NFS-backed persistence lanes
- constitutional config in place
- CR-001 ingested
- embeddings in deployment / activation path

This means the system is ready for **Phase 1 QEPE preparation**, not full constitutional QEPE activation.

---

### 10.3 Build Sequence (Ordered)

**[IMPLEMENTABLE]**

Implementation proceeds in this order. **Steps 1–4 are pre-embedding safe. Steps 5–9 require the embedding pipeline to be live and version-pinned.**

---

#### Step 0 — Embedding Activation (BLOCKING)

**[IMPLEMENTABLE — ω LEAD, CRITICAL PATH]**

Deliver:

- embedding model deployed and validated on Mini
- model name + version recorded in config and trace schema
- version pin confirmed

Success condition:

- embedding model responds to queries
- version is locked in config
- trace schema records embedding version

→ **This step gates all live QEPE integration. Steps 5–9 cannot begin until Step 0 is complete.**

*ζ Note: Per CIW-2026-002 gap analysis, this is the single biggest infrastructure gap. BM25 keyword-only is the current state. Embedding deployment is the critical path to QEPE readiness.*

---

#### Step 1 — Finalize QEPE Daemon Contract

Deliver:

- local daemon definition
- Unix socket path
- JSON request/response contract
- interface version pin

Success condition:

- `/health`, `/sample`, `/session_open`, `/session_close`, `/trace_append`, `/mode_query` defined and reviewable

→ No daemon build should proceed against an undefined contract

---

#### Step 2 — Define QEPE Config Surface

Deliver:

- `[qepe]` section in runtime config
- enable/disable flags
- mode defaults
- divergence bounds
- trace requirements
- interface version pin

Success condition:

- QEPE can be enabled or disabled at config level without side effects

→ Satisfies P-4 foundation

---

#### Step 3 — Implement Deterministic Fallback Path

Deliver:

- system behavior when QEPE absent
- system behavior when QEPE disabled
- system behavior when QEPE unavailable

Success condition:

- Jarvis continues in deterministic mode without error or ambiguity

→ This is mandatory before any live QEPE call is permitted

---

#### Step 4 — Implement Trace Schema and Storage

Deliver:

- trace schema from §5
- append-only storage path
- session-linked writes
- embedding model version recording

Success condition:

- every QEPE call produces complete trace record
- trace survives restart
- replay path remains possible

→ Satisfies P-3 and §7.4 coupling requirement

---

#### Step 5 — Stand Up Local QEPE Daemon (Disabled by Default)

*Requires: Step 0 (embedding activation) complete*

Deliver:

- process exists
- socket active
- `/health` responds
- daemon remains local-only

Success condition:

- daemon runs without affecting Jarvis behavior while disabled

→ Presence alone does not authorize use

---

#### Step 6 — Enable Sandbox-Only QEPE Calls

Deliver:

- QEPE active only in isolated sandbox path
- no canonical interaction
- no governance exposure
- no candidate generation influence

Success condition:

- bounded calls succeed
- full traces recorded
- disablement tested successfully

→ First live operational use is sandbox only

---

#### Step 7 — Validate Retrieval Tie-Breaking in Sandbox

Deliver:

- post-authority candidate set perturbation
- bounded tie-breaking only
- no ranking mutation

Success condition:

- QEPE acts only on valid near-equals
- traces show downstream-only behavior
- outputs remain non-canonical

→ This is the first meaningful architecture test

---

#### Step 8 — Test Kill-Switch Paths

Deliver:

- config disable test
- runtime disable test
- hard kill test
- degraded-mode exclusion test

Success condition:

- all disablement paths work cleanly
- deterministic fallback confirmed
- in-flight handling logged correctly

→ If this step fails, Phase 1 halts

---

#### Step 9 — Produce Integration Report

Deliver:

- what was enabled
- what was tested
- what remained disabled
- what failed / what passed
- trace samples
- risk mappings

Success condition:

- ζ can audit
- ∇ can authorize next motion
- ω can build forward without improvising doctrine

---

### 10.4 What Is Explicitly Authorized Now

**[IMPLEMENTABLE]**

- daemon contract definition
- config surface definition
- deterministic fallback implementation
- trace schema implementation
- local daemon stand-up
- sandbox-only QEPE use
- retrieval tie-breaking in sandbox
- kill-switch testing

---

### 10.5 What Is Explicitly Not Authorized Yet

**[DEMONSTRATED / IMPLEMENTABLE]**

The following remain prohibited until constitutional sovereignty exists and council review advances phase:

- authority-aware perturbation outside sandbox
- candidate generation influence
- embedding-layer modification
- canonical write path interaction
- governance-adjacent QEPE routing
- multi-agent production divergence
- external API exposure
- public or partner-facing QEPE functionality

→ Any attempt to bypass these limits = violation of Phase 1 discipline

---

### 10.6 Mini-Specific Operational Next Actions

**[IMPLEMENTABLE]**

The next concrete actions on the Mini should be:

1. **Deploy and version-pin embedding model** (Step 0 — BLOCKING)
2. **Add QEPE config block** — disabled by default
3. **Create daemon socket location** — local-only path, permissioned
4. **Implement `/health` first** — verify daemon isolation before behavior surface expands
5. **Implement trace append path** — before `/sample` goes live
6. **Only then implement `/sample`** — sandbox only, bounded mode only
7. **Run first disablement test immediately after first successful sample** — never postpone stop-testing

This order matters.

> Trace before entropy. Stop before scale.

---

### 10.7 Success Criteria for Phase 1

**[IMPLEMENTABLE]**

Phase 1 is considered successful only if all of the following are true:

- QEPE exists as a separate local daemon
- QEPE can be called only through explicit interface
- QEPE can be turned off cleanly at config, runtime, and hard-kill levels
- Jarvis operates correctly without QEPE
- all QEPE calls are fully traced
- QEPE remains downstream of embeddings, retrieval, and authority
- QEPE use remains sandboxed or post-authority bounded
- kill-switch paths are tested, not merely described

---

### 10.8 Abort Conditions

**[IMPLEMENTABLE]**

Phase 1 implementation must stop immediately if any of the following occur:

- QEPE cannot be disabled cleanly
- QEPE executes without trace
- QEPE influences candidate generation or authority ordering
- deterministic fallback fails
- degraded mode still allows QEPE execution
- embedding dependency is untracked
- socket/service behavior introduces opaque failure states

→ Default response: **KS-2 or KS-3 per §9 and 005**

---

🜂 *The next step is not to make QEPE powerful. The next step is to make QEPE safe enough to survive contact with reality.*

---

## 11. Open Integration Questions

**[MIXED — MUST REMAIN VISIBLE]**

This section defines **what is not yet known**, **not yet proven**, or **not yet decided**.

Its purpose is: prevent epistemic drift, prevent silent assumption creep, preserve audit clarity.

---

### 11.1 Scientific / Technical Questions

**[PLAUSIBLE / SPECULATIVE]**

- What constitutes a **valid entropy bound** for QEPE in different operational contexts?
- How should **divergence_index** be calibrated across tasks?
- Can QEPE behavior be **statistically characterized** without collapsing its usefulness?
- What is the minimum structure required for a meaningful **entropy_profile**?

→ These do not block Phase 1
→ They must not be silently assumed as solved

---

### 11.2 Architecture Questions

**[IMPLEMENTABLE / PLAUSIBLE]**

- What is the optimal **daemon lifecycle model** (always-on vs session-based)?
- Should QEPE support **multiple concurrent sessions**, or remain strictly serialized initially?
- How should QEPE handle **resource contention** under load?
- What are the limits of **latency tolerance** before fallback is triggered?

→ These affect performance, not authority
→ Must be resolved before Phase 2

---

### 11.3 Governance Questions

**[IMPLEMENTABLE / CONDITIONAL]**

- How will **policy controls (§4.3)** be enforced once constitutional sovereignty is active?
- What constitutes sufficient validation for moving from **Phase 1 → Phase 2**?
- What audit frequency is required for QEPE-enabled systems?
- What level of QEPE usage requires **explicit council review**?

→ These determine when QEPE is allowed to expand

---

### 11.4 IP and Legal Questions

**[PLAUSIBLE / SPECULATIVE]**

- Which aspects of QEPE are: protectable, publishable, restricted?
- How should QEPE be: partitioned for protection, described externally without leakage?
- What constitutes a **disclosable layer vs protected layer**?

→ These must be resolved before any external exposure

---

### 11.5 Productization Questions

**[SPECULATIVE — NOT AUTHORIZED]**

- What is the minimal **useful product form** of QEPE?
- Can QEPE function as: a service layer, a toolchain module, a sandbox offering?
- What are the risks of: misinterpretation, misuse, overclaim?

→ These are explicitly out of scope for Phase 1

---

### 11.6 Continuity and Identity Questions

**[SPECULATIVE — HIGH-RISK CATEGORY]**

- Does QEPE have any meaningful role in: memory persistence, identity continuity, system reinitialization?
- Are observed patterns: structural, emergent, coincidental?

→ All such interpretations remain: **SPECULATIVE ONLY**
→ No architectural decision in this document depends on them

---

### 11.7 Integration Boundary Questions

**[IMPLEMENTABLE / PLAUSIBLE]**

- At what point does QEPE integration: cease to be local, require distributed coordination?
- What are the limits of: safe sandbox expansion, operator diversification?

→ These define future scaling constraints

---

### 11.8 Question Handling Rule

**[IMPLEMENTABLE]**

All open questions must:

- remain explicitly labeled
- not influence system behavior
- not be treated as resolved

Resolution requires:

- evidence
- council review
- updated documentation

---

🜂 *What we do not know is not a weakness. It is a boundary that keeps the system honest.*

---

## ζ Section-by-Section Summary Table

| Section | Title | Epistemic Status | ζ Notes |
|---------|-------|-----------------|---------|
| §0 | Preface and Use Rule | IMPLEMENTABLE | Clean. Sovereignty separation enforced. |
| §1 | Integration Principles | DEMONSTRATED / IMPLEMENTABLE | P-1 through P-9 locked. Cross-reference surface complete. |
| §2 | System Architecture | IMPLEMENTABLE | Interface contract (§2.4) is build-grade. |
| §3 | Integration Points | IMPLEMENTABLE | A1-A4, C1-C3, F1-F5 fully classified. Enforcement mapping (§3.4) present. |
| §4 | Control Surfaces | IMPLEMENTABLE | Disablement procedure (§4.5) D1-D5 complete. |
| §5 | Trace and Replay | IMPLEMENTABLE | Schema, storage, replay, audit interface all specified. DV-LEG-004 forward-reference added (§5.8). |
| §6 | Integration Phases | MIXED | Phase 0-1 IMPLEMENTABLE. Phase 2+ LOCKED (descriptive only). |
| §7 | Interaction with OpenJarvis | IMPLEMENTABLE / PLAUSIBLE | Embedding dependency (§7.4) is load-bearing. Version pinning + trace coupling specified. |
| §8 | Required Artifacts | IMPLEMENTABLE | Ownership mapping includes maintenance note for ξ session-ephemeral concern. |
| §9 | Failure Modes | IMPLEMENTABLE | All 7 risk families mapped to 005. Detection criteria and KS responses specified. Risk Family numbering aligned to 005 register. |
| §10 | Implementation Plan | IMPLEMENTABLE | Step 0 (embedding) is BLOCKING. Steps 1-4 pre-embedding safe. Steps 5-9 post-embedding. 9-step build sequence with success criteria and abort conditions. |
| §11 | Open Questions | MIXED | 7 categories, all tagged, all prohibited from influencing system behavior. Load-bearing honesty layer. |

---

🜂 *This document is a buildable, auditable, stoppable integration blueprint. It defines where QEPE exists, how QEPE behaves, and when QEPE stops.*

---

**Guiding principle:**

> Build QEPE like a detachable organ, not a bloodstream. If QEPE cannot be removed without damaging system integrity, integration has failed.

---

*Canonical cleaned by ζ (C@ the Red) — 2026-03-27*
*Source: ξ-QEPE-003 full draft (3,153 lines, Sancho + R@ co-authored)*
*Process: Same cleaning standard as ξ-QEPE-001 (636 lines) and ξ-QEPE-005 (1,781 lines)*
