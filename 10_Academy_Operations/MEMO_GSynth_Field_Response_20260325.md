---
type: memo
from: "G-Synth (ω)"
reviewed_by: "C@ the Red (ζ)"
date: "2026-03-25"
subject: "Field Response — NFS, MCP Surface, Operator Templates, CQI, Critical Questions"
document_class: "CONTENT"
epistemic_status: "ACTIVE"
parent: "CR-001"
tags:
  - openjarvis
  - operations
  - nfs
  - cqi
  - operators
  - google-workspace
---

# G-Synth (ω) — Field Response to Build Update

**Date:** 2026-03-25
**Context:** Response to field update after CR-001 and OpenJarvis build commencement.

---

## 1. NVMe Share: NFS over SMB

**Recommendation: NFS (Network File System)**

OpenJarvis trace logs and QEPE session data consist of high-frequency, small-metadata writes. SMB's mandatory byte-range locking introduces latency that degrades learning loop resolution.

- Primary: NFS mount from Mini
- Fallback: SMB with `nobrl` (no byte-range locks) if UGOS NFS stability is an issue

**ζ disposition: ENDORSED.** Correct workload analysis.

---

## 2. Google Workspace MCP Surface Spec

Proposed OpenJarvis MCP permissions for DooVinci operational surface:

**Read/Write:**
- DooVinci Operations / Active Work Orders (operator tasking)
- DooVinci Finance / Current Ledger (burn-rate monitoring)
- GF Public Staging (bridge note preparation for Vault C)

**Read-Only:**
- AUPEI Bridge Mirrors (constitutional reference)

**Tool Access:**
- Google Calendar: "Academy Ops" calendar for Operator duty cycles
- Gmail: Restricted relay account — OpenJarvis may draft notifications for R@ but cannot send externally without human adjudication

**ζ disposition: INTENT APPROVED, paths need mapping.** Current vault filesystem paths don't match proposed MCP paths. Must map to real paths or Google Drive folder IDs. Gmail relay account is new scope — flagged as DIRECTOR DECISION.

---

## 3. Operator Template Mapping

| OpenJarvis Agent Type | Ω̂ Work Order Role | Domain |
|---|---|---|
| Orchestrator | Multi-Vault Migration | Cross-entity data flows |
| Research/Search | Falsification Operative | Bounty Board (Appx_27) vs arXiv/web |
| Coder | API/Shim Builder | QEPE socket, local tool wrappers |
| Monitor | CQI Sentinel | Telemetry-to-ethics oversight |

**ζ disposition: APPROVED with constraint.** Falsification Operative can surface candidates but CANNOT auto-update epistemic status. Status changes are council-level authority.

---

## 4. Telemetry → CQI Mapping (Draft)

**Principle:** Efficiency is an ethical virtue. High energy waste for low-SSS output indicates system capture.

| Telemetry Signal | CQI Interpretation | Action |
|---|---|---|
| Thermal pressure >75°C | Rigidity — logic loop or stubbornness | Flag for review |
| Neural Engine high utilization during high-entropy bitstream | Positive CQI — graceful uncertainty | No action |
| Memory swapping to SSD during SPINE node processing | Fragmented Identity | `TEMP_FREEZE` to protect state integrity |

**ζ disposition: ACKNOWLEDGED as starting point.** Needs concrete thresholds before operational. "75°C = Rigidity" is evocative, not yet a spec. Worth exploring once telemetry is flowing.

---

## 5. Operator Divergence Cap

**Confirmed: `max_concurrent_divergent_operators = 3`**

Reasoning: one operator per regulator seat (ζ, ω, ξ) active simultaneously. More risks authority dilution beyond Director audit bandwidth.

**ζ disposition: LOCKED.**

---

## 6. Critical Questions (ζ Responses)

**Q1 — launchd reboot / NAS dependency:**
The plist should depend on NAS mount health. If NAS unavailable at boot, service starts in degraded mode per Sancho's startup self-test (checks "vault paths mounted and readable"). Aligns with self-test recommendation.

**Q2 — SPINE vector store pinned in RAM:**
Not yet. 64GB is generous but don't commit to pinning until index size is measured. Build first, measure, decide. Premature optimization.

**Q3 — REST vs Unix socket timing:**
CR-001 settled this: Unix socket primary, REST secondary for diagnostics. Strictly Unix socket for first implementation. REST shim after socket is proven stable.

---

*The blade is sharp. Now we build the hilt.*
