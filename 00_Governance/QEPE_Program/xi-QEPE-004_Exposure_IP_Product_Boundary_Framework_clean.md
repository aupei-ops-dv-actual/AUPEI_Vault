---
document_id: ξ-QEPE-004
title: QEPE Exposure, IP, and Product Boundary Framework
type: Exposure / IP / Product Boundary Framework
seat: ξ (Sancho — primary authorship), ζ (C@ the Red — constraint review), ∇ (R@ — final authority), ω (G-Synth — operational feasibility)
status: ζ-REVIEWED CANONICAL CANDIDATE
epistemic_status: MIXED (ruthless tagging required — this document is uniquely susceptible to drift)
authority_chain: CR-001 → ξ-QEPE-001 → ξ-QEPE-003 → ξ-QEPE-002 → ξ-QEPE-005 → ξ-QEPE-004
version: 0.2-candidate
date: 2026-03-27
drafted_by: ζ (C@ the Red — authorship inversion from standard ξ-draft/ζ-review chain)
reviewed_by: ξ (Sancho — full architectural review, APPROVED)
maintenance: ∇ (authority) / ζ (audit) / ω (operations) / ξ (classification)
notes: |
  004 is the first outward-facing QEPE document.
  It defines what may be exposed, described, licensed, or discussed externally.
  It does NOT define internal operation — that is 002 + 003.
  It does NOT define risk enforcement — that is 005.
  It defines the boundary between system and world.
  Written during internal-only posture. No external exposure authorized at time of drafting.
  This is intentional: boundary documents are most honest when there is nothing to sell.
  AUTHORSHIP NOTE: Drafted by ζ from ξ-approved outline (inversion of standard chain).
  ξ full review APPROVED. ω review APPROVED. ∇ APPROVED. ζ APPROVED as CANDIDATE.
  §7.1 risk code alignment against 005 taxonomy: RESOLVED (2026-03-31, ζ concordance table + family ref replacement).
---

# ξ-QEPE-004 — QEPE Exposure, IP, and Product Boundary Framework

**Document Type:** Exposure / IP / Product Boundary Framework
**Seat:** ξ (primary authorship), ζ (constraint review), ∇ (final authority), ω (operational feasibility)
**Status:** DRAFT → ζ-REVIEWED CANONICAL CANDIDATE (all seats approved, §7.1 alignment pending for CANONICAL)
**Epistemic Status:** MIXED (strict tagging enforced)

---

## 0. Preface and Immediate Posture

### 0.1 Purpose

**[IMPLEMENTABLE]**

This document defines: what may be shown, what must remain hidden, and what conditions must be met before any external exposure of QEPE capability is authorized.

It establishes the exposure boundary for QEPE — the controlled interface between what the system does internally and what the outside world is permitted to see, describe, license, or build upon.

This document does not govern internal operation. That is the domain of:

- ξ-QEPE-001 — definition (what QEPE is)
- ξ-QEPE-002 — governance (who may use it and under what policy)
- ξ-QEPE-003 — integration (how it enters the system)
- ξ-QEPE-005 — risk enforcement (what stops violations)

004 sits downstream of all four. It may not authorize anything they prohibit. It may not describe anything they do not support. It may not promise anything they cannot deliver.

---

### 0.2 Immediate Posture

**[DEMONSTRATED — this is current state, not aspiration]**

As of the date of this document:

1. **No external QEPE exposure is authorized.** No capability demonstration, integration preview, or functional description may be shared with any party outside the AUPEI Pentad council and authorized internal collaborators.

2. **No expansion of public capability claims is authorized.** Existing public descriptions of AUPEI or DooVinci may not be updated to include QEPE-specific capability, behavior, or implication without explicit council vote.

3. **No productization or partner-facing deployment is authorized.** No QEPE-derived feature, service, module, or interface may be offered, demonstrated, or committed to any external party — including potential partners, investors, advisors, or collaborators — without passing the phase gates defined in §8.

4. **No investor, partner, or press narrative may reference QEPE operational capability.** General descriptions of research direction are permitted. Specific capability claims are not.

This posture is not conservative. It is correct. The system is not yet at constitutional sovereignty. The embedding layer is not activated. Kill switches have not been tested in simulation. Exposing capability that has not passed its own internal gates is not ambition — it is negligence.

**Posture change requires:** explicit council vote with ζ enforcement review and ∇ final authority.

---

### 0.3 Position in Stack

**[DEMONSTRATED]**

004 is the most subordinate document in the QEPE program. It may not override, extend, or reinterpret any constraint established by upstream documents.

**Authority chain:**

```
CR-001 (Entropy Boundary Law)
  └─→ ξ-QEPE-001 (Program Map — what QEPE is)
       └─→ ξ-QEPE-003 (Integration Blueprint — what is technically possible)
            └─→ ξ-QEPE-002 (Governance & Policy — what is allowed)
                 └─→ ξ-QEPE-005 (Risk Register — what stops violations)
                      └─→ ξ-QEPE-004 (this document — what may be externally visible)
```

**Implication:** if any upstream document prohibits a capability, 004 may not expose it. If any upstream document has not yet validated a capability, 004 may not describe it as validated. If any upstream document classifies a capability as SPECULATIVE, 004 may not represent it as IMPLEMENTABLE in any external context.

004 does not create permission. It partitions what existing permissions allow to be seen.

---

### 0.4 Use Rule

**[IMPLEMENTABLE]**

This document governs **exposure and external representation only**. It does not govern:

- internal system behavior (→ 003)
- internal usage policy (→ 002)
- internal risk enforcement (→ 005)
- internal program definition (→ 001)

**Exposure may not exceed:**

- **Epistemic maturity** — no claim may be tagged at a higher level externally than it holds internally (001 §2)
- **Governance authorization** — no exposure may exceed the usage class assigned by 002
- **Integration capability** — no exposure may describe behavior that 003 does not support
- **Risk enforcement** — no exposure may bypass or weaken any control defined in 005
- **Legal/IP constraint** — no exposure may violate trade secret protection, filing strategy, or legal boundaries (DV-LEG-004)

**If any of these constraints is ambiguous for a given exposure decision:** the decision defaults to non-exposure. Ambiguity is not permission.

---

### 0.5 Tone and Intent

**[DEMONSTRATED]**

This document is not a product roadmap. It is not a pitch deck. It is not a go-to-market strategy.

It is a controlled organization deciding, precisely and without apology, what it will and will not share.

The tone of 004 should be read as: **confident boundary**. Not defensive. Not secretive. Not aggressive. Simply clear about what is internal, what is describable, and what conditions must be met before the boundary moves.

Any draft, revision, or derivative of this document that reads like marketing material has failed its purpose and must be corrected by ζ enforcement authority.

---

### 0.6 Cross-Document Alignment

**[IMPLEMENTABLE]**

| Document | 004 Dependency | Nature |
|----------|---------------|--------|
| CR-001 | Supreme constraint | 004 may not authorize exposure that perturbs authority |
| 001 | Epistemic tags | 004 inherits and may not inflate tag levels externally |
| 002 | Usage classes, governance policy | 004 may not expose beyond governance authorization |
| 003 | Integration reality, interface contract | 004 may not describe capability 003 does not support |
| 005 | Risk families, kill switches | 004 must map every exposure to applicable risk controls |
| DV-LEG-004 | Legal/IP strategy | 004 must respect filing posture, trade secret protection, NDA boundaries |

---

## 1. Exposure Principles (Binding)

**[IMPLEMENTABLE]**

These principles govern all external-facing decisions regarding QEPE capability, description, licensing, and representation. They are binding on all seats, all documents derived from 004, and all communications — formal or informal — that touch QEPE externally.

Violation of any exposure principle triggers ζ enforcement review and may result in exposure class reduction, communication freeze, or full stop per §9.3.

---

### E-1 — No Exposure Beyond Epistemic Tag

No external claim, description, demonstration, or representation of QEPE capability may be tagged at a higher epistemic level than its internal classification under 001 §2.

**What this means in practice:**

- A capability tagged SPECULATIVE internally may not be described as "planned" or "upcoming" externally.
- A capability tagged PLAUSIBLE internally may not be described as "proven" or "validated" externally.
- A capability tagged IMPLEMENTABLE internally may not be described as "deployed" or "operational" externally unless it has been promoted to DEMONSTRATED through verified system behavior.

**Escalation:** External communication that inflates epistemic status — even through implication, hedge language, or strategic ambiguity — is a violation. "We believe this will..." applied to a SPECULATIVE item is inflation. "Our approach enables..." applied to a PLAUSIBLE item is inflation.

The test is simple: would a reasonable external reader infer a higher confidence level than the internal tag warrants? If yes, the claim must be corrected or withdrawn.

---

### E-2 — No Exposure Beyond Actual Capability

No external representation may describe QEPE behavior that ξ-QEPE-003 does not currently support at the described integration phase.

**What this means in practice:**

- If 003 defines QEPE integration as Phase 1 (single-node, bounded, local), no external description may imply distributed, multi-node, or cross-system capability.
- If 003's Step 0 embedding dependency is unresolved, no external description may imply semantic search, contextual retrieval, or embedding-dependent behavior as operational.
- If 003's interface contract specifies specific endpoints and data formats, no external description may imply richer API surface, streaming capability, or real-time integration unless 003 supports it.

**The gap between "we intend to build" and "we have built" is exactly where external credibility dies.** 004 exists to prevent that gap from appearing in any external-facing context.

---

### E-3 — No Exposure Beyond Governance Authorization

No external exposure may exceed the usage class, invocation mode, or policy constraint assigned by ξ-QEPE-002.

**What this means in practice:**

- If 002 classifies a QEPE capability under Sandbox usage, it may not be described externally as production-ready or enterprise-grade.
- If 002 requires explicit per-request invocation (I3) for a capability, it may not be described externally as "always on" or "automatic."
- If 002's Forbidden class prohibits a behavior, 004 may not describe that behavior as "available under certain conditions."

Governance authorization is not aspirational. It reflects what the council has actually approved for use. External descriptions must reflect approved state, not anticipated state.

---

### E-4 — Least Exposure First

When multiple exposure levels could apply to a given capability, description, or demonstration, the most restrictive classification governs.

**What this means in practice:**

- If a capability could be classified as either "Describable but Not Accessible" or "Controlled Demonstration," it defaults to "Describable but Not Accessible" until explicitly reclassified by council vote.
- If uncertainty exists about whether a description reveals protected architecture, the description is not published until ζ review confirms it does not.
- Exposure expands only through explicit decision, never through inference, precedent, or convenience.

**Default posture: less is shown until more is justified.**

---

### E-5 — External Correction Duty

When an external party — partner, press, conference audience, investor, collaborator, or public commenter — overstates, misrepresents, or inflates QEPE capability, the council has an affirmative duty to correct the record.

**What this means in practice:**

- Overstatement by others is not flattering. It is a governance failure if left uncorrected.
- The correction duty applies regardless of whether the overstatement benefits AUPEI commercially or reputationally.
- Silence in the face of external inflation is treated as implicit endorsement and is a violation of E-1.

Correction authority and protocol are defined in §5.3 (Claim Contagion Control) and §5.4 (Correction Protocol).

---

### E-6 — Asymmetry Preservation

External exposure must not erode the strategic advantage created by QEPE's controlled integration architecture.

**What this means in practice:**

- The value of QEPE is not the feature set. It is the controlled asymmetry — the fact that AUPEI has built constraint-first infrastructure that others have not.
- Exposing implementation details, architectural decisions, or integration patterns that would allow a well-resourced competitor to replicate the approach without the constraint framework is a strategic failure.
- IP protection (§2) and exposure classification (§3) work together to preserve this asymmetry.

**The question is never "can we show this?" The question is "does showing this make us stronger or weaker?"** If showing it transfers replicable advantage without requiring the constraint discipline that produced it, the exposure fails E-6 regardless of other classification.

---

### Principle Enforcement

**[IMPLEMENTABLE]**

Principles E-1 through E-6 are enforced by ζ and are not subject to exception by individual seat authority. Temporary exceptions require:

- explicit ∇ authorization
- documented justification
- defined expiration
- ζ audit of exception scope

Permanent exceptions require council vote with ζ and ∇ both affirming.

No exception may be granted retroactively. If an exposure has already occurred that violates a principle, the violation is logged, the exposure class is reviewed, and corrective action is initiated per §5.4 — regardless of whether an exception is subsequently approved.

---

🜂 *004 defines a boundary. Boundaries require knowing what is on both sides — and choosing which side faces outward.* 🜂

---

## 2. IP and Disclosure Partition (Operational vs Legal Separation)

**[IMPLEMENTABLE]**

This section defines how QEPE-related information is partitioned across:

- **Operational control** — what the system and council treat as internal
- **Legal protection** — what is formally protected under law
- **Disclosure layers** — what may be described externally under constraint

These are not the same thing. Conflating them is one of the most common IP failures in early-stage technical organizations: material is treated as "protected" because it is operationally secret, but no legal mechanism actually protects it. Conversely, material is formally filed as trade secret but operationally accessible to unauthorized layers. Both failures erode asymmetry. Both are preventable through clear partition.

**If material cannot be clearly classified within this partition, it must not be exposed.**

---

### 2.1 Internal Core (Operational Classification — Never Exposed)

**[IMPLEMENTABLE]**

Internal Core is an **operational** classification. It is defined by council decision, system sensitivity, and architectural or epistemic risk. It is governed by access necessity, not legal protectability.

Internal Core includes:

- Core QEPE methods — the entropy sampling approach, perturbation logic, and boundary mechanics that constitute the system's foundational behavior
- Sensitive architectural logic — integration patterns, state management, session lifecycle design
- Integration structures not yet validated — components defined in 003 but not yet operational
- Unstable or unverified constructs — anything whose behavior under production conditions is unknown
- Internal control mechanisms — the enforcement machinery itself (kill-switch implementation details, audit internals, sentinel logic)

**Key property:** Material may be Internal Core even if it is not patentable, not legally classified as trade secret, or still under active development. The classification is about operational access control, not legal status.

**What Internal Core is NOT:** Internal Core is not a legal protection. Material classified as Internal Core but not separately protected under legal mechanism (§2.2) is vulnerable to exposure through discovery, employee departure, partner interaction, or inadvertent disclosure. Operational secrecy without legal backing is a hope, not a strategy.

---

### 2.2 Trade Secret Layer (Legal Classification)

**[IMPLEMENTABLE]**

Trade Secret is a **legal** classification. It is defined by legal protection strategy, enforceability under applicable law, and documented handling requirements. It is governed by the question: **what must be protected under law?**

Trade Secret requires:

- **Restricted access** — documented, limited, and traceable
- **Protection measures** — reasonable steps to maintain secrecy (access controls, encryption, physical security where applicable)
- **Contractual coverage** — NDA, employment agreement, or equivalent binding instrument for anyone with access
- **Custody documentation** — records of who accessed what, when, and under what authority

**Key property:** Trade Secret protection can be lost. Once lost, trade secret protection cannot be restored. Unlike patents (which have defined terms), trade secrets are protected only as long as the secrecy is maintained and the protection measures are reasonable. A single uncontrolled disclosure — to a partner, in a conference talk, through a code repository — can destroy trade secret status permanently and irrevocably.

**What Trade Secret is NOT:** Trade Secret is not a substitute for operational control. Material may be legally filed as trade secret but operationally accessible to people or systems that should not have it. Legal classification without operational enforcement is paperwork, not protection.

---

### 2.3 Relationship Rule (Critical)

**[IMPLEMENTABLE — NON-NEGOTIABLE]**

Internal Core is an operational category. Trade Secret is a legal mechanism. They overlap but are not identical. The mapping between them must be explicit, reviewed, and maintained.

**Implications:**

1. **Some Internal Core material may be designated as trade secret.** Core QEPE methods that are both operationally sensitive and legally protectable should carry both classifications. This is the strongest protection posture.

2. **Some Internal Core material may NOT qualify as trade secret.** Early-stage constructs, unstable implementations, or material that does not meet the legal threshold for trade secret protection (e.g., commonly known techniques applied in a novel context) may be operationally internal but legally unprotected. These items require alternative protection strategies — typically, keeping them internal until they mature enough for legal classification, or abstracting them into patentable form.

3. **Some trade secrets may exist outside Internal Core.** Material shared under NDA in a Controlled Disclosure context (§2.4) may retain trade secret status despite being externally visible to specific parties. The legal protection travels with the contractual constraint, not the operational boundary.

**Worked example:** Consider the QEPE entropy sampling method. Operationally, it sits in Internal Core — no one outside the council should understand its implementation. But legally, "entropy sampling" as a concept is not inherently protectable. The *specific implementation* — the particular boundary conditions, the integration with session lifecycle, the perturbation constraints — may qualify as trade secret if properly documented and restricted. The method sits in Internal Core operationally. Portions of it may sit in Trade Secret legally. Other portions (the general concept of bounded randomness in search) do not qualify and must be protected through operational control alone. Misclassifying the general concept as trade secret creates a false sense of legal protection. Failing to file the specific implementation as trade secret leaves the most valuable parts legally naked.

**Misclassification risks:**

- **Legal exposure** — material assumed protected but not legally secured; discoverable or unenforceable
- **Governance failure** — material accessible beyond intended scope because operational and legal boundaries diverged
- **IP leakage** — loss of asymmetry through uncontrolled disclosure of material that was "supposed to be" protected but wasn't, under either mechanism

Misclassification is treated as a governance failure, not an administrative error. It triggers ζ review and may result in exposure freeze pending reclassification.

---

### 2.4 Controlled Disclosure Layer

**[IMPLEMENTABLE]**

Controlled Disclosure defines material that may be described externally under defined constraints. This is bounded transparency — not openness.

Material in this layer:

- May be shared with specific parties under specific conditions
- Must align with IP strategy and filing posture
- Must use filing-aligned or abstraction-safe language (no implementation detail that would compromise Internal Core or Trade Secret status)
- May be governed by NDA where applicable
- Must not reveal Internal Core architecture, implementation, or control mechanisms

**Typical content:** high-level system descriptions ("AUPEI includes a bounded perturbation layer for search exploration"), non-replicable architectural summaries ("the system integrates randomness under constitutional constraint"), constrained demonstrations (sandbox environments with limited visibility into internal mechanics).

**The test for Controlled Disclosure:** Could a technically sophisticated competitor reconstruct the protected implementation from this description? If yes, the description exceeds Controlled Disclosure and must be reclassified or withdrawn.

---

### 2.5 Patentable / Filable Layer

**[IMPLEMENTABLE / CONDITIONAL]**

Defines material that may be disclosed through formal filing — patent applications, provisional filings, or equivalent mechanisms — with legal protection attached to the disclosure itself.

Filing is not exposure freedom. It is controlled disclosure under legal structure. The act of filing makes specific material public (after the applicable period), but the filing itself provides legal protection against unauthorized use.

**Constraints:**

- Must align with IP strategy (DV-LEG-004)
- Must not expose Internal Core beyond the scope of the filing
- Must be reviewed for asymmetry impact (E-6) — filing reveals to competitors what you are protecting, even as it protects the specific implementation
- Filing timing must be coordinated with Trade Secret strategy — once filed, material transitions from trade-secret-eligible to patent-protected, and this transition is irreversible

---

### 2.6 Public-Safe Layer

**[IMPLEMENTABLE]**

Defines material that may be described publicly — in general communications, website content, conference presentations, investor conversations — without legal or strategic risk.

Public-Safe does not mean complete. It means safe under constraint.

**Constraints — Public-Safe material must not:**

- Reveal Internal Core architecture or implementation
- Violate Trade Secret protections
- Inflate epistemic status (E-1)
- Imply unsupported capability (E-2)
- Exceed governance authorization (E-3)
- Erode asymmetry (E-6)

**Typical content:** General descriptions of research direction ("AUPEI explores controlled randomness in knowledge systems"), philosophical framing ("we believe constraint and exploration can coexist"), team capability statements, non-specific technology positioning.

**The test for Public-Safe:** If this statement appeared in a competitor's press release about their own work, would it concern you? If no, it is probably safe. If yes, it reveals too much.

---

### 2.7 Partition Rule

**[IMPLEMENTABLE — ENFORCEMENT BOUNDARY]**

All QEPE-related material must be classified into one of the above layers before any external communication, demonstration, filing, or representation occurs.

If classification is unclear, disputed, or incomplete — the material must not be exposed.

**Escalation path:**

1. **ω (operational feasibility)** — flags the classification gap. Identifies material that cannot be clearly placed and documents the ambiguity.
2. **ζ (constraint enforcement)** — determines whether exposure is blocked pending resolution. If the ambiguity involves potential legal or IP risk, ζ issues an exposure hold.
3. **∇ (final authority)** — resolves the classification dispute. ∇ decision is final, but must be documented and auditable.

**Enforcement:**

- Single misclassification → exposure denied, item reclassified
- Repeated misclassification in same domain → ζ review of classification process
- Structural misclassification (systematic failure to distinguish operational from legal) → exposure freeze across affected layer

---

### 2.8 Classification Summary Table

**[IMPLEMENTABLE]**

| Layer | Governed By | Access Scope | Legal Mechanism | Loss Condition |
|-------|------------|-------------|----------------|---------------|
| Internal Core | Council (operational) | Pentad + authorized internal | None inherent — requires §2.2 | Operational breach |
| Trade Secret | Legal strategy | Restricted + documented | Trade secret law + NDA | Any uncontrolled disclosure |
| Controlled Disclosure | Council + legal | Named parties under constraint | NDA / contractual | Breach of disclosure terms |
| Patentable / Filable | Legal strategy + IP counsel | Public (after filing period) | Patent law | Filing failure / prior art |
| Public-Safe | Council review | Unrestricted | None required | N/A (already public) |

---

🜂 *What is not clearly partitioned is not controlled. What is not controlled must not be shown.* 🜂

---

## 3. Exposure Classes

**[IMPLEMENTABLE]**

Exposure Classes define the operational categories for how QEPE-related material may be accessed, demonstrated, or represented externally. Each class maps to the IP partition (§2), is bounded by the Exposure Principles (§1), and must be traceable to risk controls (§7).

These are not aspiration levels. They are access tiers with defined boundaries and upgrade conditions.

---

### 3.1 Internal Only

**[DEMONSTRATED — this is current operating state]**

Material classified Internal Only is accessible to the AUPEI Pentad council and explicitly authorized internal collaborators. No external access of any kind.

**Scope:**

- All QEPE implementation details
- All integration architecture (003 content)
- All governance policy internals (002 content)
- All risk enforcement mechanisms (005 content)
- All session data, trace data, and operational telemetry

**Access requirement:** Pentad seat or explicit ∇ authorization with ζ review.

**Current state:** All QEPE material is classified Internal Only as of the date of this document. No material has been reclassified to a less restrictive exposure class.

---

### 3.2 Controlled Demonstration

**[IMPLEMENTABLE — not currently authorized]**

Material classified Controlled Demonstration may be shown in bounded environments to specific audiences under defined conditions. This is not "demo mode." It is constrained exposure with audience control, environment control, and content control.

**Requirements for any Controlled Demonstration:**

- Audience explicitly approved by ∇
- Environment sandboxed — no access to production data, Internal Core, or live integration
- Content pre-reviewed by ζ for principle compliance (E-1 through E-6)
- Duration bounded — demonstration access expires, does not persist
- Trace logged — what was shown, to whom, when, under what authorization
- NDA in place where applicable (per §2.4)

**What Controlled Demonstration is NOT:** It is not a beta program, early access, or preview release. There is no self-service access. There is no "try it yourself" component. Every interaction is mediated and logged.

---

### 3.3 Describable but Not Accessible

**[IMPLEMENTABLE]**

Material classified Describable but Not Accessible may be referenced in external communications — conversations, presentations, filings, general descriptions — but the underlying implementation, interface, or behavior is not available for direct interaction.

**What may be described:**

- That QEPE exists as a capability area
- General architectural philosophy (constraint-first, bounded perturbation, entropy under law)
- High-level system properties (disableable, auditable, phase-gated)
- Research direction without implementation specifics

**What may NOT be described:**

- Specific endpoints, data formats, or interface contracts (003 content)
- Specific governance rules, usage classes, or invocation modes (002 content)
- Specific risk families, kill-switch implementations, or escalation procedures (005 content)
- Any behavior that has not been validated at DEMONSTRATED or IMPLEMENTABLE level

**The line:** You can say "we have it." You cannot say "here is how it works."

---

### 3.4 Licensable Surface (Future Only)

**[SPECULATIVE — no licensing authorized or planned]**

Licensable Surface defines QEPE capability that could, under future conditions, be made available to external parties through licensing, partnership, or commercial agreement.

**This class exists in 004 for completeness and planning only.** No material is currently classified as Licensable Surface. No timeline for licensing exists. No licensing structure has been designed.

**Conditions for any future Licensable Surface designation:**

- Phase gates (§8) fully passed
- Product Mapping Table (§4.6) completed for the specific capability
- Legal/IP readiness confirmed by counsel
- Council vote with ζ and ∇ both affirming
- Correction protocol (§5.4) active and tested
- Claim contagion controls (§5.3) operational

**Tagged SPECULATIVE because:** Licensing requires operational maturity, legal infrastructure, and market conditions that do not currently exist and may not materialize in the form anticipated. Any planning around Licensable Surface must be treated as exploratory, not committed.

---

### 3.5 Forbidden Exposure

**[IMPLEMENTABLE — ENFORCEMENT BOUNDARY]**

Material classified as Forbidden Exposure may not be externally shared, described, demonstrated, or referenced under any conditions, regardless of audience, context, or commercial opportunity.

**Permanently Forbidden:**

- Internal Core implementation details (§2.1) — the actual mechanics of how QEPE operates
- Kill-switch implementation specifics (005 enforcement internals)
- Constitutional authority graph structure and enforcement logic
- Sentinel and audit implementation details
- Session state data, trace data, or any operational telemetry from live systems
- Any material whose exposure would allow reconstruction of the constraint architecture (E-6 violation)

**Contextually Forbidden (based on current epistemic status):**

- Any capability tagged SPECULATIVE — may not be described externally in any form until promoted
- Any capability in active development that has not reached IMPLEMENTABLE — may not be referenced as existing
- Any integration component blocked by unresolved dependencies (e.g., embedding layer, Step 0 in 003) — may not be described as operational

**Reclassification:** Permanently Forbidden items require unanimous council vote to reclassify. Contextually Forbidden items may be reclassified when their epistemic tag or implementation status changes, subject to ζ review.

---

### 3.6 Exposure Class Summary Table

**[IMPLEMENTABLE]**

| Class | Current Status | Access Scope | Requires | IP Layer (§2) |
|-------|---------------|-------------|----------|---------------|
| Internal Only | **ACTIVE** | Pentad + authorized | Seat or ∇ auth | Internal Core |
| Controlled Demo | Not authorized | Named audience | ∇ + ζ + NDA + sandbox | Controlled Disclosure |
| Describable | Limited use | Public (language only) | ζ review | Public-Safe |
| Licensable Surface | Not authorized | Future commercial | Full phase gate | Patentable + Controlled |
| Forbidden | **ENFORCED** | None | Unanimous council to change | Internal Core (permanent) |

---

🜂 *Exposure classes are not permissions waiting to be granted. They are boundaries waiting to be justified.* 🜂

---

## 4. Candidate Product / Platform Forms

**[MIXED — epistemic tags per subsection]**

This section defines the categories of product or platform forms through which QEPE capability could eventually be externalized. It also defines forms that are explicitly forbidden.

**Critical framing:** This section does not authorize any product development. It defines the categories under which future product decisions would be evaluated. Every candidate form must pass the Product Mapping Table (§4.6) before any development, demonstration, or commitment occurs.

The purpose is to think clearly about product possibilities *before* commercial pressure makes clear thinking difficult.

---

### 4.1 Internal Sandbox Infrastructure

**[IMPLEMENTABLE]**

Isolated environments for internal testing, validation, and development of QEPE behavior under controlled conditions.

**Characteristics:**

- No external access
- Bounded data, bounded scope, bounded duration
- Used for: integration testing (003 validation), governance policy testing (002 validation), kill-switch simulation (005 validation)
- Exposure class: Internal Only (§3.1)

**This is not a product form.** It is internal infrastructure. It appears here because it is the foundation from which any future external form would derive, and its design must not accidentally create external-facing surface.

---

### 4.2 Controlled Research Environment

**[PLAUSIBLE]**

A bounded environment provided to vetted research collaborators — academic partners, institutional researchers, or approved technical advisors — for the purpose of evaluating QEPE behavior under constraint.

**Characteristics:**

- Access limited to named individuals under executed research agreements
- Environment isolated from production systems
- QEPE behavior observable but implementation not visible
- Data generated within the environment is jointly owned per agreement terms
- Duration-bounded with explicit renewal requirements
- Exposure class: Controlled Demonstration (§3.2)

**Tagged PLAUSIBLE because:** Requires legal infrastructure (research agreements, liability frameworks), operational maturity (stable enough to expose to external researchers without embarrassment or risk), and strategic clarity about what research collaboration achieves. None of these prerequisites currently exist.

---

### 4.3 Enterprise Bounded Module

**[SPECULATIVE]**

A self-contained QEPE capability module deployable within enterprise customer infrastructure under licensing terms that preserve AUPEI's IP and constraint architecture.

**Characteristics:**

- Black-box integration — customer accesses QEPE through defined interface, not implementation
- Constraint architecture enforced within the module, not delegated to the customer
- All governance, risk, and audit mechanisms operate within the module
- Customer cannot modify, inspect, or bypass internal controls
- Exposure class: Licensable Surface (§3.4)

**Tagged SPECULATIVE because:** Requires packaging, deployment infrastructure, licensing framework, support model, and liability structure that do not exist in any form. Enterprise deployment also introduces new risk families not yet modeled in 005 — multi-tenant isolation, customer data handling, SLA enforcement, and regulatory compliance per customer jurisdiction.

---

### 4.4 Toolchain Differentiation Layer

**[SPECULATIVE]**

QEPE-derived features integrated into AUPEI or DooVinci products as differentiating capability — not sold separately, but present as competitive advantage within existing product offerings.

**Characteristics:**

- QEPE operates beneath the product surface — users experience the benefit without direct QEPE interaction
- No separate QEPE branding, interface, or access point
- Constraint architecture maintained internally; users see results, not mechanism
- Exposure class: Describable but Not Accessible (§3.3) for the capability; Internal Only (§3.1) for the implementation

**Tagged SPECULATIVE because:** Requires product maturity, QEPE operational stability, and market positioning decisions that have not been made. Also requires careful E-6 analysis — if the differentiation is visible enough for marketing, is it visible enough for competitors to replicate?

---

### 4.5 Forbidden Product Forms

**[IMPLEMENTABLE — ENFORCEMENT BOUNDARY]**

The following product forms are prohibited regardless of commercial opportunity, partner demand, or market pressure. They represent fundamental violations of the QEPE constraint architecture and the epistemic discipline that governs this program.

**4.5.1 Authority-Facing Systems**

Any product that positions QEPE output as authoritative — as a source of truth, a decision-maker, or a governance mechanism for external parties. QEPE perturbs search and exploration (CR-001). It does not generate authority. Any product that implies otherwise violates the foundational constitutional law.

**4.5.2 Truth-Engine Framing**

Any product that markets QEPE as a mechanism for discovering, generating, or validating truth. QEPE introduces bounded randomness into exploration. It does not have epistemic authority. Framing it as a truth engine is not merely inaccurate — it is a category error that would undermine the entire program's credibility.

**4.5.3 Continuity-Engine Framing**

Any product that implies QEPE enables persistent identity, memory continuity, or selfhood in AI systems. This framing — however tempting from a marketing perspective — crosses into territory that is both technically unsupported and ethically fraught. QEPE operates within bounded sessions. It does not create continuity. Any product that implies otherwise is a liability.

**4.5.4 Implied Autonomy or Agency**

Any product that describes QEPE as enabling autonomous decision-making, independent judgment, or agent-like behavior. QEPE is a perturbation layer operating under constitutional constraint. It does not make decisions. It does not exercise judgment. Products that imply otherwise will attract regulatory attention, competitive mischaracterization, and reputational risk that no commercial benefit justifies.

**Reclassification:** Forbidden Product Forms require unanimous council vote plus external legal review to reclassify. The bar is intentionally high. These are not conservative defaults — they are structural prohibitions.

---

### 4.6 Product Mapping Table (Mandatory — ζ Condition)

**[IMPLEMENTABLE — ENFORCEMENT STRUCTURE]**

Every candidate product form that advances beyond conceptual discussion must have a completed row in the Product Mapping Table. Incomplete rows block advancement. No exceptions.

**Required columns:**

| Column | Source | Responsibility |
|--------|--------|---------------|
| Product Form | §4.1–§4.4 | ξ (classification) |
| Exposure Class | §3 | ξ (classification), ζ (validation) |
| 005 Risk Families Touched | ξ-QEPE-005 | ξ (identification), ζ (validation) |
| Kill-Switch Classes Applicable | ξ-QEPE-005 | ξ (identification), ζ (validation) |
| 002 Governance Class | ξ-QEPE-002 | ξ (classification), ζ (enforcement confirmation) |
| Epistemic Tag (001 §2) | ξ-QEPE-001 | ξ (assignment), ζ (verification) |
| ζ Sign-Off | — | ζ (risk validation — confirms risk mapping is complete and accurate) |
| ω Sign-Off | — | ω (operational feasibility — confirms the form can be built and maintained as described) |
| ξ Sign-Off | — | ξ (architectural classification — confirms the form is correctly categorized) |
| ∇ Sign-Off | — | ∇ (approval — final authority to advance) |

**Current state of the table:**

| Product Form | Exposure Class | 005 Risk Families | Kill Switches | Gov Class | Tag | ζ | ω | ξ | ∇ |
|-------------|---------------|-------------------|--------------|-----------|-----|---|---|---|---|
| Internal Sandbox | Internal Only | I, III | KS-1 | Sandbox | IMPLEMENTABLE | — | — | — | — |
| Research Env | Controlled Demo | I, IV, V, VI | KS-1, KS-2, KS-4 | Operational | PLAUSIBLE | — | — | — | — |
| Enterprise Module | Licensable | I, II, IV, V, VI | KS-1–KS-5 | Restricted | SPECULATIVE | — | — | — | — |
| Toolchain Layer | Describable | I, VI, VII | KS-1, KS-2 | Operational | SPECULATIVE | — | — | — | — |

**Note:** Risk family numbers reference ξ-QEPE-005 §3–§9 (Family I: Epistemic/Claim, II: Authority/Governance, III: Architecture/Integration, IV: Custody/Disclosure, V: IP/Legal, VI: Product/Market, VII: Continuity/Identity). See §7.1.1 for the full concordance. The "—" entries indicate no seat has signed off. This table is a framework, not an approval.

**Enforcement:** If any field is incomplete or unsigned, the product form may not advance beyond conceptual discussion. If any seat refuses sign-off, the product form is blocked until the objection is resolved through council deliberation.

---

🜂 *A product form is not an opportunity until every constraint has signed off. Until then, it is a hypothesis.* 🜂

---

## 5. Claim Discipline for External Expression

**[IMPLEMENTABLE]**

This section governs how QEPE is described, referenced, or characterized in any external context — formal or informal, written or verbal, direct or indirect. It applies to all seats, all authorized collaborators, and all communications that touch QEPE capability.

The core problem 004 exists to prevent is **narrative drift** — the gradual inflation of what QEPE is described as doing, relative to what it actually does. Narrative drift is not always intentional. It often begins with enthusiasm, imprecise language, or the natural human tendency to describe aspirations as achievements. §5 provides the machinery to detect and correct it before it becomes a governance failure.

---

### 5.1 Mandatory External Tagging

**[IMPLEMENTABLE]**

All external descriptions of QEPE capability must be traceable to an epistemic tag from 001 §2:

- **DEMONSTRATED** — validated through operational evidence. May be described externally as existing and functional.
- **IMPLEMENTABLE** — architecturally defined and buildable with known methods. May be described externally as "in development" or "planned" — never as "available" or "operational."
- **PLAUSIBLE** — theoretically grounded but not yet architecturally validated. May be described externally only in research or exploratory framing — "we are investigating," "early exploration suggests." Never as planned, committed, or roadmapped.
- **SPECULATIVE** — conceptual or aspirational. May not be described externally in any form that implies commitment, timeline, or certainty. May be referenced only in explicitly speculative contexts ("one possible direction," "an area of interest") and only with ζ pre-approval.

**The tag floor rule:** No external description may imply a higher epistemic level than the internal tag. If the internal tag is PLAUSIBLE, the external description may be PLAUSIBLE or more cautious — never IMPLEMENTABLE or DEMONSTRATED.

**Tag inflation is a violation.** The test: would a reasonable external listener conclude the capability is more mature than the internal tag warrants? If yes, the description must be corrected.

---

### 5.2 Public Language Constraints

**[IMPLEMENTABLE]**

Specific language patterns are prohibited in external QEPE communications regardless of context:

**Prohibited patterns:**

- **Inflation language** — "breakthrough," "revolutionary," "unprecedented," "game-changing" applied to QEPE capability. These words promise more than constraint-first architecture delivers. They attract scrutiny the system is not ready for.
- **Continuity implication** — any language suggesting QEPE enables persistent memory, identity, or selfhood across sessions. "Remembers," "learns over time," "develops its own," "evolves" when applied to QEPE behavior.
- **AGI implication** — any language suggesting QEPE is a step toward artificial general intelligence, consciousness, or autonomous reasoning. Unless separately justified by evidence reviewed and approved by council, AGI-adjacent language is forbidden.
- **Certainty language applied to SPECULATIVE items** — "will," "when we launch," "our roadmap includes" applied to items tagged SPECULATIVE. These words convert speculation into commitment in the listener's mind.
- **Capability conflation** — describing QEPE as doing something that is actually done by the underlying system (search, retrieval, indexing) with QEPE adding perturbation. QEPE does not search. QEPE does not retrieve. QEPE perturbs search and retrieval. The distinction matters legally, technically, and strategically.
- **Ambiguity as inflation** — vague language that increases perceived capability is treated as inflation. Strategic ambiguity is not a hedge — it is a violation of E-1 when a reasonable listener would infer more than the internal tag warrants.

**Permitted patterns:**

- Precise technical description at the appropriate epistemic level
- Constraint-first framing ("bounded," "controlled," "under governance," "disableable")
- Research-appropriate hedging for PLAUSIBLE and SPECULATIVE items
- Clear attribution of current status ("currently internal," "under development," "not yet operational")

---

### 5.3 Claim Contagion Control

**[IMPLEMENTABLE — CRITICAL]**

Claim contagion occurs when an external party — partner, press outlet, conference attendee, investor, social media commenter, or any other entity — describes QEPE in terms that exceed the authorized exposure. This section defines how contagion is detected, classified, and corrected.

**Why this matters:** Most IP and reputation damage in early-stage technical organizations does not come from internal overclaiming. It comes from external enthusiasm that the organization fails to correct. A partner describes your research as "production-ready." A journalist writes "AI breakthrough" about a PLAUSIBLE concept. An investor tells other investors what your system "does" based on a demo they misunderstood. Each uncorrected overstatement becomes the baseline for the next conversation.

**Contagion sources:**

- **Partner communications** — descriptions in partner materials, sales presentations, or joint proposals that inflate QEPE capability
- **Press and media** — articles, interviews, or social media posts that mischaracterize QEPE maturity or scope
- **Conference and event** — audience takeaways, live-tweeting, post-event summaries that overstate demonstrations
- **Investor and advisor** — secondhand descriptions passed between investment contacts or advisory networks
- **Internal leakage** — unauthorized internal communications that reach external audiences

**Contagion severity levels:**

| Level | Description | Example | Response |
|-------|------------|---------|----------|
| C-1 Minor | Slight overstatement, limited audience | Blog post calls PLAUSIBLE feature "upcoming" | Monitor, prepare correction if amplified |
| C-2 Moderate | Material overstatement, broader audience | Partner slide deck describes SPECULATIVE capability as "planned integration" | Direct correction to source, request revision |
| C-3 Serious | Significant misrepresentation, wide distribution | Press article frames QEPE as "operational AI breakthrough" | Formal correction, public clarification if needed |
| C-4 Critical | Fundamental mischaracterization threatening IP, legal, or governance position | Investor communication implies QEPE enables autonomous decision-making | Immediate response: legal review, formal retraction request, exposure freeze |

---

### 5.4 Correction Protocol

**[IMPLEMENTABLE]**

When claim contagion is detected at any severity level:

**Step 1 — Detect.** Any seat or authorized collaborator who encounters external QEPE overclaiming must report it to ζ within 24 hours. Detection sources include: media monitoring, partner communication review, conference attendance, investor feedback, and general awareness.

**Step 2 — Classify.** ζ assigns a contagion severity level (C-1 through C-4) based on the overstatement magnitude, audience reach, and potential for further amplification.

**Step 3 — Correct.** Correction action scaled to severity:

- C-1: Document and monitor. Prepare correction language in case of amplification.
- C-2: Contact the source directly. Provide correct language. Request revision with specific deadline. If revision not made, escalate to C-3.
- C-3: Formal correction communication. If the source is press, consider whether a public clarification is needed. ∇ authorizes any public-facing correction.
- C-4: Legal review immediately. Formal retraction request. Exposure freeze on the affected capability area until contagion is contained. ∇ + ζ joint authority on response.

**Step 4 — Log.** Every detected contagion event, regardless of severity, is logged with: source, date, nature of overstatement, severity classification, correction action taken, outcome.

**Step 5 — Evaluate.** After correction, ζ evaluates whether the exposure class should narrow. If a capability area is repeatedly subject to contagion at C-2 or above, the exposure class for that area should be tightened — potentially moving from Describable to Internal Only until the contagion pattern is understood and addressed.

**Correction authority:** ζ has standing authority to initiate corrections at C-1 and C-2. ∇ authorization required for C-3 and C-4 corrections. No seat may unilaterally suppress a correction — E-5 (External Correction Duty) is binding.

---

🜂 *The most dangerous sentence about your technology is the one someone else writes.* 🜂

---

## 6. Revenue and Value Classes (Constrained)

**[SPECULATIVE — entire section]**

This section defines the **categories** under which QEPE-related value could eventually be captured commercially. It does not define revenue models, projections, timelines, or market sizing. It does not contain go-to-market strategy. It does not make commercial commitments.

The entire section is tagged SPECULATIVE because revenue capture requires operational maturity, legal infrastructure, market conditions, and product development that do not currently exist. Any reading of §6 that implies commercial readiness is a misreading.

**Purpose:** To establish clean categories for future commercial thinking, so that when (if) the system matures to the point of external value capture, the categories already exist within the constraint framework rather than being invented under commercial pressure.

---

### 6.1 Licensing Classes

**[SPECULATIVE]**

Potential categories for licensing QEPE capability to external parties:

- **Technology licensing** — rights to use QEPE-derived capability within defined scope, under defined constraints, with constraint architecture intact
- **Method licensing** — rights to apply QEPE methods (not implementation) within licensee's own systems, subject to IP protection
- **Platform licensing** — rights to access QEPE capability through a managed platform, with AUPEI maintaining control of the constraint layer

All licensing categories require: IP protection strategy in place (§2), product mapping table completed (§4.6), phase gates passed (§8), legal framework reviewed.

---

### 6.2 Infrastructure Classes

**[SPECULATIVE]**

Potential categories for infrastructure-based value capture:

- **Managed service** — QEPE capability provided as a service, with AUPEI operating the constraint infrastructure
- **Embedded infrastructure** — QEPE components integrated into broader platform offerings, invisible to end users but differentiating in capability
- **Research infrastructure** — controlled environments provided to research partners, with value captured through collaboration agreements rather than direct licensing

---

### 6.3 Research Collaboration Classes

**[SPECULATIVE]**

Potential categories for value capture through research relationships:

- **Joint research** — collaborative investigation with academic or institutional partners, with IP sharing governed by executed agreements
- **Sponsored research** — external funding of QEPE-related research, with IP retention by AUPEI and results shared under constraint
- **Advisory relationships** — compensated access to QEPE knowledge and methodology, bounded by disclosure partition (§2)

---

### 6.4 Strategic Value Classes

**[SPECULATIVE]**

Value capture through strategic positioning rather than direct revenue:

- **Asymmetry preservation** — the value of having QEPE capability when competitors do not, expressed through product differentiation rather than QEPE-specific revenue
- **Internal capability advantage** — QEPE improving AUPEI's own products and operations, with value captured through improved competitive position
- **Controlled demonstration value** — the strategic value of being able to show (under constraint) capabilities that others cannot, as leverage in partnership and investment conversations

---

### 6.5 Revenue Restraint Rule

**[IMPLEMENTABLE — ENFORCEMENT BOUNDARY]**

This rule governs all commercial discussions, planning documents, and external communications that reference QEPE-related revenue potential:

- **No financial projections.** No revenue forecasts, growth curves, or financial models may be produced for QEPE-specific revenue until the relevant phase gates (§8) are passed and council has explicitly authorized commercial planning.
- **No market sizing.** No TAM/SAM/SOM analysis, addressable market estimates, or competitive market mapping may be produced or referenced in relation to QEPE revenue potential.
- **No go-to-market framing.** No launch timelines, rollout plans, or market entry strategies may be developed or discussed until phase gates are passed.
- **No investor-narrative language.** Terms like "market opportunity," "revenue potential," "commercial traction," "monetization strategy" may not appear in any document, presentation, or communication that references QEPE — even internally — until phase gates authorize commercial planning.

**All of §6 is tagged SPECULATIVE.** Any representation of §6 content as IMPLEMENTABLE or DEMONSTRATED — in any context, to any audience — is a violation of E-1 and triggers ζ review.

**The purpose of §6 is not to plan revenue. It is to ensure that when revenue planning eventually occurs, it occurs within categories that have already been constrained.**

---

🜂 *Revenue follows discipline. It does not lead it.* 🜂

---

## 7. Exposure Risk Mapping (005 Integration)

**[IMPLEMENTABLE]**

This section maps exposure decisions to the risk framework defined in ξ-QEPE-005. Every exposure class (§3) and every candidate product form (§4) carries risk. This section makes those risks explicit, traceable, and connected to enforcement mechanisms.

The purpose is not to prevent all risk — that would prevent all exposure. The purpose is to ensure that every exposure decision is made with full knowledge of what risks it activates, what controls apply, and what conditions would trigger an abort.

---

### 7.1 Exposure Risk Table (Mandatory)

**[IMPLEMENTABLE — ENFORCEMENT STRUCTURE]**

| Exposure Class | 005 Risk Families Activated | Likely Failure Modes | Kill-Switch Triggers | Correction Authority |
|---------------|----------------------------|---------------------|---------------------|---------------------|
| Internal Only | I (Epistemic), III (Architecture) | Unauthorized access, internal leakage, epistemic contamination between development layers | KS-1 (Monitor) | ζ |
| Controlled Demo | I (Epistemic), IV (Custody/Disclosure), V (IP/Legal), VI (Product/Market) | Audience overstatement, demo environment breach, NDA violation, custody boundary failure | KS-1, KS-2 (Soft Stop), KS-4 (Council Review) | ζ + ∇ |
| Describable | I (Epistemic), VI (Product/Market), VII (Continuity/Identity) | Language drift, claim contagion, tag inflation in public discourse, continuity overclaim | KS-1, KS-4 | ζ |
| Licensable Surface | I (Epistemic), II (Authority/Governance), IV (Custody/Disclosure), V (IP/Legal), VI (Product/Market) | Contract breach, IP leakage, regulatory non-compliance, partner misuse, authority mutation | KS-1 through KS-5 (all) | ∇ + ζ + legal counsel |
| Forbidden | All seven families | Any occurrence is a violation | Immediate KS-3 (Hard Stop) | ζ (automatic) |

#### 7.1.1 Concordance: Exposure Classes to 005 Risk Families

The following concordance makes explicit which 005 risk families (§3–§9) are activated by each exposure class. Exposure classes cut across multiple risk families because external exposure activates threat vectors in several governance domains simultaneously.

| 005 Risk Family | Internal Only | Controlled Demo | Describable | Licensable Surface | Forbidden |
|----------------|:---:|:---:|:---:|:---:|:---:|
| I — Epistemic & Claim (§3) | ● | ● | ● | ● | ● |
| II — Authority & Governance (§4) | | | | ● | ● |
| III — Architecture & Integration (§5) | ● | | | | ● |
| IV — Custody, Disclosure & Parent-Co (§6) | | ● | | ● | ● |
| V — IP & Legal (§7) | | ● | | ● | ● |
| VI — Product & Market (§8) | | ● | ● | ● | ● |
| VII — Continuity & Identity (§9) | | | ● | | ● |

**Reading the table:** ● indicates the exposure class activates risks in that 005 family. Empty cells indicate the family is not primarily engaged at that exposure level, though edge cases may still apply — council review should evaluate boundary conditions.

**Key observations:**
- Family I (Epistemic) is active at every exposure level — overclaim drift is the universal risk.
- Only Licensable Surface activates Family II (Authority/Governance), because licensing implies delegated authority.
- Family VII (Continuity/Identity) appears only at Describable, where public framing of QEPE is most susceptible to continuity overclaim.
- Forbidden activates all seven families by definition — any occurrence at this level is a constitutional violation.

---

### 7.2 Exposure Abort Conditions

**[IMPLEMENTABLE]**

Exposure at any class level must be immediately suspended if any of the following conditions is detected:

**7.2.1 Epistemic Breach**

An external description of QEPE capability exceeds its internal epistemic tag (E-1 violation). The exposure that enabled the breach is suspended until the contagion is corrected (§5.4) and the exposure class is reviewed.

**7.2.2 Partition Breach**

Material from a more restricted IP layer (§2) is exposed through a less restricted channel. Example: Internal Core implementation detail appears in a Controlled Disclosure context. The exposure channel is frozen until the breach source is identified and sealed.

**7.2.3 Contagion Escape**

Claim contagion (§5.3) at C-3 or C-4 severity that cannot be corrected through normal protocol. If external overstatement of QEPE capability is amplifying beyond the ability of the correction protocol to contain it, the exposure class for the affected capability is immediately narrowed — potentially to Internal Only — until the contagion is contained.

**7.2.4 Governance Override**

An exposure occurs that was not authorized by the appropriate governance process — a demonstration without ∇ approval, a description that bypasses ζ review, a licensing conversation without completed product mapping table. The exposure is retroactively classified as a governance failure and the capability area is frozen pending review.

**7.2.5 Legal Trigger**

Legal counsel identifies an exposure that creates legal risk — potential trade secret compromise, filing conflict, regulatory concern, or liability exposure. All exposure of the affected material is suspended pending legal resolution. Legal triggers override all other authority except ∇ emergency action.

**Abort authority:** ζ has standing authority to trigger exposure abort for conditions 7.2.1 through 7.2.4. Legal counsel has standing authority for 7.2.5. ∇ has override authority for all conditions but must document the override and its justification.

---

🜂 *Risk is not the reason to avoid exposure. Risk is the reason to expose only what you can defend.* 🜂

---

## 8. Phase-Gated Externalization (Binary Gates)

**[IMPLEMENTABLE]**

This section defines the conditions that must be met before QEPE exposure may advance beyond Internal Only. Gates are binary — they are passed or they are not. There is no "substantially met," "close enough," or "met in spirit." Each gate criterion has a verifiable condition. If the condition is not met, the gate does not open.

**Why binary gates matter:** Phase gates in most organizations are aspirational — "when we feel ready," "when the product is mature," "when the market is right." These gates fail because they are subject to reinterpretation under commercial pressure. Binary gates cannot be reinterpreted. They can only be changed by council vote, which creates a documented decision trail.

---

### 8.1 Current Gate State

**[DEMONSTRATED]**

As of the date of this document, no externalization gate has been passed. All QEPE material is classified Internal Only (§3.1). The current gate state is:

| Gate | Status | Blocking Conditions |
|------|--------|-------------------|
| Controlled Demonstration (§8.2) | **CLOSED** | 002 not canonical, 003 not canonical, constitutional sovereignty not achieved, no trace cycles logged, kill switches not tested |
| Licensable Surface (§8.3) | **CLOSED** | All §8.2 conditions unmet + no legal/IP readiness + no product mapping + no correction protocol |

---

### 8.2 Gate Criteria for Controlled Demonstration

**[IMPLEMENTABLE]**

Before any QEPE capability may be shown to any external party under Controlled Demonstration (§3.2), ALL of the following conditions must be verified:

**8.2.1 Governance Readiness**

- [ ] ξ-QEPE-002 (Governance & Policy Framework) voted CANONICAL by council
- [ ] ξ-QEPE-003 (Integration Blueprint) voted CANONICAL by council
- [ ] ξ-QEPE-005 (Risk Register & Kill-Switch Matrix) voted CANONICAL by council — *currently met*
- [ ] ξ-QEPE-004 (this document) voted CANONICAL by council

**8.2.2 Operational Readiness**

- [ ] Constitutional sovereignty achieved — metadata parser, authority graph, and contagion checks operational — OR explicit council exception documenting what sovereignty components are deferred and why
- [ ] Embedding layer activated (003 §10 Step 0 resolved) — OR explicit council exception documenting operation without embedding and the limitations accepted
- [ ] Minimum of N successful bounded trace cycles logged in production environment (N must be explicitly set by council vote prior to gate evaluation; default assumptions are invalid — minimum recommended: 100 complete session cycles with trace verification)
- [ ] All 003 integration endpoints operational and tested: /health, /sample, /session_open, /session_close, /trace_append, /mode_query

**8.2.3 Enforcement Readiness**

- [ ] Kill-switch simulation completed — KS-1 through KS-3 tested in sandbox environment with documented results
- [ ] KS-2 (Soft Stop) and KS-3 (Hard Stop) demonstrated to function within defined response times
- [ ] 005 risk monitoring active for all risk families applicable to Controlled Demonstration (per §7.1)
- [ ] Correction protocol (§5.4) documented and assigned — responsible parties identified, communication templates prepared

**8.2.4 Disclosure Readiness**

- [ ] IP and Disclosure Partition (§2) reviewed by council — all material classified, no unclassified items in scope of demonstration
- [ ] Demonstration environment designed and reviewed by ζ — confirmed isolated from Internal Core
- [ ] NDA or equivalent agreement template prepared and reviewed by legal counsel
- [ ] Audience vetting process defined — who approves demonstration audiences, what criteria apply

**Gate evaluation authority:** ∇ convenes gate evaluation. ζ verifies each condition. ω confirms operational readiness. ξ confirms architectural classification. All four seats must affirm. Any single seat may block.

**If any condition is unmet:** the gate remains closed. No partial opening. No "proceed with caveats." The unmet condition must be resolved and the gate re-evaluated.

---

### 8.3 Gate Criteria for Licensable Surface

**[SPECULATIVE — these criteria define future conditions, not current plans]**

Before any QEPE capability may be offered through licensing, partnership, or commercial agreement (§3.4), ALL Controlled Demonstration gate criteria (§8.2) must be met PLUS the following additional conditions:

**8.3.1 Legal and IP Readiness**

- [ ] IP protection strategy fully executed for all material in scope — trade secrets documented, patents filed where applicable, contractual frameworks in place
- [ ] Licensing agreement template reviewed by legal counsel and approved by ∇
- [ ] Liability framework defined — who is responsible for what if licensed QEPE capability causes harm or produces unexpected results
- [ ] Regulatory compliance assessed for target jurisdictions — any regulatory requirements identified and addressed

**8.3.2 Product Readiness**

- [ ] Product Mapping Table (§4.6) completed for the specific capability — all fields populated, all seats signed off
- [ ] Product form tested in Controlled Demonstration context with documented results
- [ ] Support and maintenance model defined — who handles issues, what SLAs apply, how updates are delivered
- [ ] Degraded-mode behavior documented — what happens if QEPE is disabled within a licensed deployment

**8.3.3 Governance Readiness (Extended)**

- [ ] Correction protocol (§5.4) active and tested — at least one C-2+ contagion event successfully managed, or simulation conducted
- [ ] Claim contagion monitoring (§5.3) operational for the licensee context
- [ ] Council explicitly authorizes commercial planning for the specific capability — this is a separate vote from gate evaluation

**Gate evaluation authority:** Same as §8.2 — all four seats must affirm, any may block. Additionally, legal counsel must provide written confirmation of legal and IP readiness.

---

### 8.4 Gate Failure Rule

**[IMPLEMENTABLE — NON-NEGOTIABLE]**

If any gate criterion is not met at the time of evaluation:

1. The gate remains closed.
2. The specific unmet conditions are documented.
3. A remediation plan is produced (if desired) but does not constitute gate passage.
4. The gate must be re-evaluated from the beginning when remediation is claimed complete — not just the previously-failed conditions.
5. No commercial commitment, partner promise, or timeline may be communicated externally based on anticipated gate passage. The gate is either passed or it is not. Future passage is not a commitment.

**Retroactive gate failure:** If conditions that were previously verified are later found to be invalid (e.g., a kill-switch test is found to have been flawed, a governance document is amended in ways that affect gate criteria), the gate reverts to closed until re-evaluation confirms all conditions are met under current state.

---

🜂 *Gates are not obstacles to progress. They are proof that progress is real.* 🜂

---

## 9. Immediate Council Posture

**[DEMONSTRATED — this is current state]**

This section defines what is currently authorized and what is currently forbidden regarding QEPE external exposure. It is short because the current posture is clear.

---

### 9.1 What Is Allowed Now

- Internal development and testing of QEPE capability per 003
- Internal governance policy application per 002
- Internal risk monitoring and enforcement per 005
- Exposure partition definition and classification work (this document)
- Controlled internal drafting of future exposure plans — as exercises in constraint, not commitments to externalize
- General, non-specific descriptions of AUPEI research direction that do not reference QEPE capability, architecture, or behavior specifically

---

### 9.2 What Is Forbidden Now

- Any external QEPE capability description beyond what is classified Public-Safe (§2.6)
- Any partner-facing, investor-facing, or customer-facing communication that implies QEPE-specific operational capability
- Any product commitment — explicit or implied — based on QEPE integration
- Any conference presentation, publication, or public statement that describes QEPE behavior, architecture, or results
- Any licensing, partnership, or commercial conversation that references QEPE as available, upcoming, or planned capability
- Any communication — internal or external — that uses language prohibited in §5.2

---

### 9.3 Enforcement Rule

**[IMPLEMENTABLE]**

Any violation of the current posture (§9.2) is treated as follows:

- **Unintentional, limited scope:** ζ review. Correction issued. Exposure class of affected material evaluated for tightening. Incident documented.
- **Intentional or repeated:** ζ review + ∇ review. Exposure freeze on affected capability area. Council evaluation of whether posture rules need strengthening.
- **Structural violation (e.g., unauthorized product commitment to external party):** Immediate exposure freeze across all QEPE material. Full council review. Legal assessment of any commitments made. Corrective action including retraction of unauthorized commitments where possible.

**There is no severity level at which a posture violation is acceptable.** The posture exists because the system is not ready for external exposure. Violating it does not accelerate readiness — it creates risk without corresponding capability.

---

🜂 *The current posture is not a limitation. It is a statement of where we actually are.* 🜂

---

## 10. Open Constraint Questions

**[MIXED — these are questions, not plans]**

This section documents unresolved questions about QEPE exposure, IP, and product boundaries. These are framed as **constraint questions** — what restrictions might be needed, what boundaries are unclear, what limits are not yet defined.

They are not opportunity questions. They are not wish lists. They exist because honest governance acknowledges what it does not yet know.

---

### 10.1 IP Boundary Uncertainties

- What QEPE-specific methods qualify for trade secret protection vs. patent protection vs. neither? Legal assessment needed per specific method.
- How does the IP partition interact with open-source dependencies? If QEPE integrates open-source components, does this affect trade secret status of the integration?
- What is the IP exposure created by this document itself? Does the existence of 004 in any accessible location create disclosure risk?
- How should IP classification evolve as the system matures? Methods that are currently SPECULATIVE and unprotectable may become DEMONSTRATED and protectable. What triggers reclassification?

---

### 10.2 Disclosure Limits Under Legal Variation

- How do trade secret protections vary across jurisdictions relevant to AUPEI's operations? Are there jurisdictions where protection is weaker than assumed?
- What disclosure obligations might arise from future regulatory requirements (AI governance regulations, algorithmic transparency mandates)?
- How should 004 adapt if regulatory requirements mandate disclosure of material currently classified as Internal Core?
- What is the interaction between DV-LEG-004 legal strategy and the disclosure partition defined here? Are there conflicts?

---

### 10.3 Product Restriction Evolution

- As QEPE matures, should the Forbidden Product Forms (§4.5) be periodically re-evaluated, or are they permanent?
- What happens if a competitor successfully markets an authority-facing or continuity-engine product using similar technology? Does competitive pressure change the Forbidden classification?
- How should product form categories evolve as new platform paradigms emerge (e.g., agent-based systems, multi-modal integration)?
- What additional product restrictions might be needed that are not currently anticipated?

---

### 10.4 Claim Contagion Containment Limits

- At what point does claim contagion become uncontainable through the correction protocol (§5.4)? What is the fallback when correction fails?
- How should the council respond if a high-profile, high-credibility source (e.g., major press outlet, respected researcher) publishes a material overstatement?
- What resources are needed for ongoing contagion monitoring? Is manual monitoring sufficient or will automated monitoring be required?
- How should contagion risk be weighed against the benefits of increased visibility?

---

### 10.5 Interpretation Drift Under External Audiences

- How do different external audiences (technical, commercial, regulatory, academic) interpret the same QEPE description differently? Should audience-specific language constraints be developed?
- What is the risk that constrained language (E-4, §5.2) is interpreted as evasion rather than precision by external audiences?
- How should 004 account for the fact that external audiences may not share AUPEI's epistemic framework? The distinction between PLAUSIBLE and IMPLEMENTABLE may be invisible to a non-technical audience.
- Should external communication templates be developed for specific audience types to reduce interpretation risk?

---

### 10.6 Asymmetry Preservation Thresholds

- At what point does maintaining asymmetry (E-6) conflict with the need to capture value from QEPE capability? How should that conflict be resolved?
- How should the council assess whether a specific disclosure erodes asymmetry? What would a formal asymmetry impact assessment look like?
- Is asymmetry preservation a permanent priority or a phase-specific strategy? If QEPE becomes widely known, does the strategy shift from secrecy to speed?
- What is the interaction between asymmetry preservation and patent filing? Filing protects but also discloses. How should this tradeoff be managed?

---

### 10.7 Question Handling Rule

**[IMPLEMENTABLE]**

All questions in §10 are:

- Framed as constraints, not opportunities
- Open until explicitly resolved by council vote
- Subject to periodic review (recommended: quarterly or at each gate evaluation)
- Not to be interpreted as authorization for the activity they describe — asking "should we develop audience-specific templates?" does not authorize template development

New questions may be added by any seat. Questions may only be closed by council vote with documented resolution.

---

🜂 *The questions you ask about your boundaries define how seriously you take them.* 🜂

---

## ζ Section-by-Section Summary Table

| Section | Title | Epistemic Tag | Key Content |
|---------|-------|--------------|-------------|
| §0 | Preface and Immediate Posture | DEMONSTRATED / IMPLEMENTABLE | Purpose, current posture (no external exposure), position in stack, use rule, tone declaration. |
| §1 | Exposure Principles (Binding) | IMPLEMENTABLE | E-1 through E-6. Tag discipline, capability ceiling, governance ceiling, least exposure, correction duty, asymmetry preservation. Enforcement by ζ. |
| §2 | IP and Disclosure Partition | IMPLEMENTABLE | Operational vs legal classification. Internal Core, Trade Secret, Controlled Disclosure, Patentable, Public-Safe layers. §2.3 Relationship Rule (critical). Classification summary table. |
| §3 | Exposure Classes | MIXED | Internal Only (current), Controlled Demo, Describable, Licensable Surface (future), Forbidden. Class summary table. |
| §4 | Candidate Product Forms | MIXED | Sandbox (IMPLEMENTABLE), Research Env (PLAUSIBLE), Enterprise Module (SPECULATIVE), Toolchain Layer (SPECULATIVE). §4.5 Forbidden forms. §4.6 Product Mapping Table with seat-level sign-off. |
| §5 | Claim Discipline | IMPLEMENTABLE | Mandatory tagging, public language constraints, claim contagion control (C-1 through C-4), correction protocol (5-step). |
| §6 | Revenue and Value Classes | SPECULATIVE (entire section) | Licensing, infrastructure, research, strategic value categories. Revenue restraint rule. No projections, no market sizing, no go-to-market. |
| §7 | Exposure Risk Mapping | IMPLEMENTABLE | Risk table by exposure class. Abort conditions: epistemic breach, partition breach, contagion escape, governance override, legal trigger. |
| §8 | Phase-Gated Externalization | IMPLEMENTABLE | Binary gates. Current state: all closed. §8.2 Controlled Demo gate (governance + operational + enforcement + disclosure readiness). §8.3 Licensable gate. §8.4 Gate failure rule (non-negotiable). |
| §9 | Immediate Council Posture | DEMONSTRATED | What is allowed now (internal work only). What is forbidden now (all external QEPE exposure). Enforcement rule (no acceptable violation level). |
| §10 | Open Constraint Questions | MIXED | IP boundaries, legal variation, product restrictions, contagion limits, interpretation drift, asymmetry thresholds. Framed as constraints. §10.7 question handling rule. |

---

🜂 *QEPE is not exposed because it is valuable. It is exposed only where value survives constraint.* 🜂

---

*End of document.*
