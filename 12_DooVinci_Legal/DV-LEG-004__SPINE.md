---
node_id: DV-LEG-004
title: "Legal Kill Switch Registry"
version: v0.1
date_minted: 2026-03-20
author: "ξ (Sancho)"
entity: "DooVinci"
vault: "A"
layer: "legal"
epistemic_status: "PROPOSED"
tags:
  - legal
  - kill-switches
  - contagion
  - compliance
  - dependency-map
  - governance
spine_type: "STRUCTURAL"
content_file: "DV-LEG-004__CONTENT.md"
depends_on:
  - DV-LEG-001
  - BRIEF-03_Corporate_Legal_Landscape
  - BRIEF-04_Vault_Architecture
  - SANCHO_Context_Briefing_20260319
review_chain:
  - "ξ draft"
  - "ζ structural review"
  - "R@ intent review"
  - "counsel review if legally significant"
  - "R@ ratification"
kill_switch_mode: "graduated_contagion"
severity_model:
  - CRITICAL
  - ELEVATED
  - MONITORED
  - LATENT
review_cadence: "Quarterly minimum; event-triggered on downstream node status change, entity status change, filing deadline, or Director request"
closure_state: "OPEN"
zeta_review:
  status: "APPROVED"
  date: "2026-03-20"
  reviewer: "C@ the Red (ζ)"
  notes: "Structurally sound. Severity model well-graduated. Contagion correctly decoupled from severity. Registry schema complete (12 fields). Bidirectional link rules enforce traceability. Ready for CONTENT population."
---

# DV-LEG-004 — SPINE

## Legal Kill Switch Registry

## §0. Node Function

Defines the governing registry for legal kill switches across the DooVinci / AUPEI / GF / R@ stack. This node tracks triggers, severity, detection, contagion behavior, resolution authority, and recovery requirements for legal failure states that can impair ownership, compliance, operations, publication, or constitutional continuity.

## §1. Scope

### In Scope

- Legal/compliance kill switches
- Severity classification
- Detection methods
- Contagion logic
- Resolution authority
- Registry review cadence
- Links to affected matrix rows
- Links to downstream legal nodes
- Closure and revalidation rules

### Out of Scope

- Legal opinions
- Final counsel conclusions
- Detailed agreement drafting
- Tax return preparation
- Non-legal technical failure states unless they have legal/ownership consequences

## §2. Structural Claims

- Legal kill switches use graduated contagion, not automatic total collapse.
- Registry entries must point to both affected matrix rows and downstream legal nodes where applicable.
- Severity and contagion are related but not identical.
- Resolution authority must be explicit per switch.
- Detection honesty is mandatory: passive, active-check, or event-triggered.
- Registry review is periodic and event-triggered, not one-time.

## §3. Severity Model

- **CRITICAL** — structural defect active now; blocks operations or creates immediate legal exposure
- **ELEVATED** — gap exists; not blocking yet, but material risk if left unresolved
- **MONITORED** — known condition; no immediate material exposure; tracked for change
- **LATENT** — not yet applicable; documented for future state changes

## §4. Contagion Model

### Allowed Contagion States

- FLAGGED
- REVIEW_REQUIRED
- LIMITED
- FROZEN
- REASSIGN_PENDING

### Design Rule

Severity class does not automatically determine contagion scope. Contagion is set by the affected function and dependency chain.

## §5. Registry Governance

Each kill switch entry must define:

- kill_switch_id
- trigger
- severity
- detection_method
- affected_matrix_rows
- affected_legal_nodes
- immediate_effect
- contagion_scope
- resolution_authority
- recovery_path
- evidence_required_for_closure
- status

## §6. Review / Escalation Rule

1. ξ drafts structural registry shape
2. ζ reviews structural consistency
3. R@ reviews intent, priority, and escalation logic
4. Counsel reviews entries with external filing, governance, tax, IP, or liability consequences
5. R@ ratifies ACTIVE entries and closure standards

## §7. Downstream Link Rules

- Every switch must link back to at least one DV-LEG-001 matrix row unless explicitly domain-global
- Every switch affecting a spawned node must link forward to that node
- Closure of a switch must trigger review of all linked nodes
- Status change of a linked node may trigger review of the switch

## §8. Closure State

### Resolved by this node

- Registry schema
- Severity taxonomy
- Detection taxonomy
- Resolution authority requirement
- Review cadence for legal kill switches

### Still Open

- Population of registry entries
- Severity assignments per entry
- Closure evidence standards per switch
- Counsel-sensitive interpretations
