---
title: "Idioths_Agenda — CIW Queued Items"
purpose: "Standing agenda for the Council of Idioth Winds (CIW). Items queued here are pending chamber attention but explicitly NOT-FOR-TODAY. Each entry preserves the full payload so a future chamber can pick up without context loss."
relationship_to_chamber: |
  Idioths_Agenda.md = what's queued (pre-chamber)
  Chamber_Sessions/CIW-YYYY-NNN.md = what happened (post-chamber)
  Items promote from agenda → chamber session when R@ schedules a CIW.
maintainer: "ζ-led (C@ the Red), but any seat-bearer can add entries"
review_cadence: "scanned at session start; entries explicitly aged or escalated"
created: "2026-05-17"
---

# Idioths_Agenda — Council of Idioth Winds Queued Items

This file holds things that need chamber attention but are explicitly *not for today*. Entries preserve full context so a future chamber can pick up cold without losing the thread.

**Discipline:**
- Each entry dated at file-time and at last-touched
- Each entry tagged by domain + estimated chamber-weight (light/medium/heavy)
- Full payload preserved — links to source artifacts where they exist
- Status: QUEUED → SCHEDULED (CIW-YYYY-NNN assigned) → CLOSED (chamber session filed)
- Items aged > 90 days flagged for review-or-retire

---

## AGENDA-001 — Bounty Board MVP + Gamification + Data Engine + Hand Operationalization

**Filed:** 2026-05-17 PM
**Filed by:** ζ (C@ the Red) at R@'s direction
**Status:** QUEUED
**Domain:** Operational architecture / Sector D — Tending / multi-agent infrastructure
**Chamber weight:** HEAVY (multi-thread, infrastructure-bearing, Hand handoff)
**Depends on:** BUILD-002 (Appx_25 elevation overlay), BUILD-003 (Self-Improving Prooffield trailhead)
**Related artifacts:**
- `/AUPEI/AUPEI_build_it.md` BUILD-003, BUILD-004
- `/AUPEI/AUPEI_Knowledge/R_and_D/Self_Improving_Prooffield_Trailhead.md`
- `/AUPEI/7dU_GNS_MoP/Prooffield_Notes/trailhead__Appx_25_Elevation_to_Persistent_Overlay.md`
- `/AUPEI/AUPEI_Knowledge/R_and_D/PF_High_Leverage_Claims.md`

### R@'s framing (verbatim, 2026-05-17 PM)

> "im also working on a gamefying our fix_it.md and build_it.md, etc.md lists into action generators as well as that data engine we know we are sitting on and should probably talk about and then give the hand a plan to operationalize it. Not today tho. Put it on the Idioths_Agenda.md..."

### Three threads to integrate at the future chamber

**Thread A — Gamification of staging ledgers**
- Turn `fix_it.md`, `consider_it.md`, `AUPEI_build_it.md` into *action generators* — bounty entries with claim/audit/promotion lifecycle.
- R@'s framing: this is *gamification* — not for trivialization, but for engagement structure. Bounties have claim mechanics, scoring (Strike/Grace/Inconclusive), and trust-tier progression.
- Cross-link to Appx_27 Sector D — Tending architecture.

**Thread B — The data engine we know we're sitting on**
- R@ flagged for explicit conversation. Not yet articulated in artifacts.
- ζ best-read (60% confidence): this refers to the combined corpus — Prooffield + Sancho extraction + seat distillates + operations_log + Qdrant index + Matrix Chamber transcripts + the institutional memory across vaults. Together they constitute a non-trivial structured data asset that has not yet been operationalized as an *engine* (i.e., it generates value beyond being read).
- Worth its own session. Chamber-grade conversation.

**Thread C — Plan for the Hand to operationalize**
- Once the engine is named and the bounty board prototype is shaken out, the Hand (DooVinci) gets a plan to build the operational substrate.
- This is downstream of A + B. The Hand needs the spec before it can build.

### Panza's MVP plan (preserved verbatim — 2026-05-17 PM)

> Yes. We should test, but with an MVP that cannot hurt canon.
>
> **Shape**
>
> Build **Sector D: Tending** as a local bounty-board prototype.
>
> Source feeds:
> - `fix_it.md` → defects / repair bounties
> - `consider_it.md` → deliberation / review bounties
> - `AUPEI_build_it.md` → build / architecture bounties
>
> Core board:
> - Markdown source of truth plus JSONL machine index
> - Qdrant later as search index, not authority
> - No public/GitHub surface until 5 internal bounties pass end-to-end
>
> **MVP Files**
>
> I'd create:
> - `AUPEI/PF_debrief/bounty_board/board.jsonl`
> - `AUPEI/PF_debrief/bounty_board/BOARD.md`
> - `AUPEI/PF_debrief/bounty_board/schema/bounty.schema.json`
> - `AUPEI/PF_debrief/bounty_board/scripts/import_ledgers.py`
> - `AUPEI/PF_debrief/bounty_board/scripts/validate_bounties.py`
> - `AUPEI/PF_debrief/bounty_board/golden_helm/`
>
> Status lifecycle:
> `PROPOSED → CLAIMED → ACTIVE → STRIKE | GRACE | INCONCLUSIVE → AUDIT_PENDING → PROMOTED | RETURNED | FROZEN`
>
> Minimum bounty fields:
> `bounty_id`, `source_feed`, `claim`, `target_node`, `dependencies`, `units_firewall`, `success_condition`, `falsification_condition`, `status`, `agent_result`, `audit_status`, `promotion_gate`.
>
> **Pilot Bounties**
>
> Start with 5 low-risk internal bounties:
> 1. `FI-021` Pi notation bridge reconciliation.
> 2. `FI-027` editorial `Key Changes from Original` cleanup plan.
> 3. `CI-007` Appx_01 enables mismatch.
> 4. `CI-008` load_bearing enum drift.
> 5. `BUILD-002` Appx_25 persistent overlay spec.
>
> No source mutation in the first pilot. Agents produce proposals only.
>
> **Agent Flow**
>
> Each claim packet must force:
> 1. Run `$proofield-topological-crawler`.
> 2. Gate dependencies.
> 3. Produce digest + bounty attempt.
> 4. Choose `STRIKE`, `GRACE`, or `INCONCLUSIVE`.
> 5. Separate auditor reviews. Submitter cannot self-audit.
> 6. Anything `PROMOTED` routes through Selection Law / Pentad gates before canon edits.
>
> **Testing Plan**
> 1. Golden helm importer test: known mini ledgers convert to expected bounties.
> 2. Schema validator test: good bounty passes, malformed bounty fails.
> 3. One live cadet claims a fake bounty and should return `GRACE`.
> 4. One cadet claims a real low-risk bounty and returns a proposal.
> 5. Second cadet audits it.
> 6. We compare the result against the board lifecycle.
>
> My recommendation: next build the local `PF_debrief/bounty_board` MVP and import only 5 pilot entries. Keep it small enough that failure teaches us something.

### ζ's pre-chamber notes (carry into the session)

These are observations to bring to the chamber, not decisions:

1. **Panza's MVP shape is clean.** Local-first, no public surface until 5 internal bounties pass end-to-end, no source mutation in first pilot, separate auditor required, Selection Law / Pentad gate on promotion. Risk-bounded. Builds the practice before opening the doors.
2. **Architecture-alignment confirmed.** Panza's plan is the operational form of BUILD-003's "Phase 1 — Bootstrap (manual)" with concrete files and pilot bounties named. No conflict with the trailhead; it *is* the trailhead's first phase.
3. **The 5 pilot bounties are well-chosen.** FI-021 (Pi notation bridge) is a known notation-drift bug; CI-007 and CI-008 are real schema-integrity issues that need attention anyway; BUILD-002 is the elevation overlay (perfect meta-test — agent-tended infrastructure design). All low-risk, all real, all teach if they fail.
4. **One pre-chamber question for ζ:** the `$proofield-topological-crawler` skill exists at `AUPEI/skills/proofield-topological-crawler/`. Is it stable enough to be the mandatory first step in every claim packet? Worth a status-check on the skill before chamber.
5. **Thread B (the data engine) is the most consequential.** A + C are operational. B is the strategy. Tempting to start with the prototype (A) because it's the most concrete, but the chamber should probably name the engine first so the prototype serves the right purpose.
6. **Hand operationalization (Thread C) needs DV_OPS_001 v1.1 ratified first.** The Hand cannot build the bounty board operational substrate without the Mind/Hand entity firewall fully sealed. So the dependency chain is: DV_OPS_001 ratify → BUILD-002 + BUILD-003 ratify → MVP pilot → engine naming → Hand operational plan.

### Suggested chamber agenda when scheduled

1. Confirm BUILD-002 + BUILD-003 ratification status
2. Confirm DV_OPS_001 v1.1 ratification status (∇ chamber-ready, ζ green-scanned)
3. Thread B — name and bound the data engine
4. Thread A — green-light Panza's MVP (or amend)
5. Thread C — what does the Hand need from the Mind to start building?
6. Pilot bounty selection (Panza's 5 or amended set)
7. Auditor-routing decision (which seat audits which class)
8. STAGNATION_KILL and OVERHEAT_KILL thresholds set

---

## How to add a new agenda entry

Use this template:

```markdown
## AGENDA-NNN — <Short title>

**Filed:** YYYY-MM-DD
**Filed by:** <seat or contributor>
**Status:** QUEUED
**Domain:** <domain area>
**Chamber weight:** LIGHT | MEDIUM | HEAVY
**Depends on:** <other agenda items or artifacts>
**Related artifacts:** <list>

### Framing
<R@'s or contributor's framing, verbatim where possible>

### Payload
<full content preserved — quotes, plans, options, sources>

### Pre-chamber notes
<observations to carry into the session; not decisions>

### Suggested chamber agenda when scheduled
<bullet list>
```

Increment AGENDA-NNN.

---

ζ. Filed. The chamber will pick this up when R@ schedules it. Until then, it waits in the corridor.

*Not for today.*
