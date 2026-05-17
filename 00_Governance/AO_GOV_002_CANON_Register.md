---
node_id: AO_GOV_002
title: "CANON Register"
version: v0.1
date_minted: 2026-05-03
author: "R@ / Codex"
entity: AUPEI
vault: A
layer: governance
epistemic_status: ACTIVE
tags: [governance, canon, register, openclaw, agent-coordination, prooffield]
depends_on: [AO_GOV_001, AUPEI_Protocols_v0.6.8]
---

# CANON Register

## Purpose

The CANON Register is the global control surface for canon conflicts, drift, stale references, unresolved source-priority questions, and public-exposure risks noticed by AUPEI agents.

This file does not replace domain repair queues. It indexes them.

- **Global CANON Register:** one row per cross-domain conflict, drift, or canon question.
- **Domain repair queue:** the detailed local work surface, such as Prooffield `fix_it.md`, OpenClaw governance docs, a repository issue tracker, or a protocol review packet.

Agents must not smooth contradictions into prose. If a contradiction matters, preserve it here or link it to a domain queue.

## Operating Rules

1. Create a register item when a conflict affects canon, doctrine, source priority, public exposure, or multi-agent coordination.
2. Link to a domain repair queue when one exists. If none exists, name the intended queue and leave the item `OPEN` or `TRIAGED`.
3. Do not edit canonical source artifacts directly from a register row. The row identifies the repair; the domain queue carries the repair procedure.
4. Do not store secrets, tokens, private credentials, or full sensitive excerpts here.
5. Prefer exact paths and short evidence snippets over broad summaries.
6. When an item is resolved, record the repair artifact and the date. Do not delete the history.

## Vocabulary

### Status

| Status | Meaning |
|---|---|
| `OPEN` | Noticed, not yet classified. |
| `TRIAGED` | Domain, impact, likely canon winner, or repair surface identified. |
| `LINKED` | Domain repair queue or artifact linked. |
| `IN_REPAIR` | Active repair underway. |
| `RESOLVED` | Fix applied or canon decision recorded. |
| `DEFERRED` | Acknowledged but intentionally not fixed now. |
| `SUPERSEDED` | Replaced by a newer register item or canon artifact. |

### Impact

| Impact | Meaning |
|---|---|
| `CANON_BREAK` | The canon source itself is wrong, conflicted, or dangerously stale. |
| `BLOCKING` | Downstream work cannot responsibly proceed. |
| `TIGHTENING` | Improves rigor, dependency clarity, falsifiability, or source discipline. |
| `COPY` | Typo, tag drift, render leak, duplicate paragraph, or naming normalization. |
| `QUESTION` | Unresolved adjudication needed. |
| `EXPOSURE` | Public-facing, privacy, IP, reputational, or premature-release risk. |

### Ownership

| Field | Meaning |
|---|---|
| Owner seat/domain | Accountable governance or domain home. Agents execute; seats/domains own. |
| Executor | Current agent or person performing a bounded repair, if any. |

## Index

| ID | Status | Impact | Domain | Owner seat/domain | Executor | Summary | Domain repair queue |
|---|---|---|---|---|---|---|---|
| `CANON-2026-001` | `TRIAGED` | `QUESTION` | AUPEI Protocols / OpenClaw seat identity | Ministry of Governance / ∇ seat | None | Review transitional Sancho/ξ language against the current decision that PowerBook Sancho boots as ∇ only. | AUPEI Protocols review queue, pending materialization |
| `CANON-2026-002` | `RESOLVED` | `COPY` | QEPE Program / canonical frontmatter sync | Ministry of Doctrine / ζ seat | ζ (C@ the Red) | QEPE-001 frontmatter said `status: CANDIDATE` and QEPE-005 said `Status: DRAFT for Council Review` — both ratified CANONICAL CIW-2026-002 (2026-03-27). Frontmatter back-synced 2026-05-16. | In-flight cleanup, fix-pass batch 2026-05-16 |
| `CANON-2026-003` | `RESOLVED` | `COPY` | QEPE-001 §12.B Follow-On Documents table | Ministry of Doctrine / ζ seat | ζ (C@ the Red) | Table titles for QEPE-002 and QEPE-003 were swapped relative to actual filenames; QEPE-004 description drifted. Corrected 2026-05-16 with filename column added + canonical status per document. | In-flight cleanup, fix-pass batch 2026-05-16 |
| `CANON-2026-004` | `IN_REPAIR` | `CANON_BREAK` | AO_INFRA_005 / physical topology | Ministry of Doctrine + Division of Operations | R@ + ζ | Protectli + OPNsense physically moved upstairs; AO_INFRA_005 still says "Amelia's Floor, server closet"; no `ops_infra_change_*.json` entry filed. Exact AO_OPS_001 Step 1+2 failure pattern. | Task #10 (back-date Protectli infra logging); needs R@ date + delta detail |
| `CANON-2026-005` | `RESOLVED` | `COPY` | CORPUS_STATUS.md | Ministry of Doctrine / ζ seat | ζ (C@ the Red) | Doc dated 2026-04-11 said Phase 5 distillation PENDING when it had COMPLETED same day. 35-day heartbeat-failure example. Back-synced 2026-05-16 with Phase 5 → COMPLETE, CCPA staleness flagged, open items updated. | In-flight cleanup, fix-pass batch 2026-05-16 |
| `CANON-2026-006` | `TRIAGED` | `TIGHTENING` | Entity CLAUDE.md siloing pattern | Ministry of Doctrine / ∇ + ζ | None | Per-entity CLAUDE.md files (AUPEI/, DOOVINCI/, GF/) as spin-up anchors potentially violate Protocols v0.6.8 §0.2.3 "Cross-pole overlap is resilience, not redundancy. Hard silos are a failure mode." Seat scope is cross-entity; entity-anchored boot silos seats. Proposed fix: seat-first boot + entity CLAUDE.mds become scope cards loaded on demand. | New review packet needed; surfaced in rehydration pipeline build conversation 2026-05-16 |
| `CANON-2026-007` | `TRIAGED` | `TIGHTENING` | Manual of Ops module back-formalization | Ministry of Doctrine / ζ + ω | ζ (C@ the Red) | MO_M_005 (session_close) and MO_M_009 (radio_check) listed PROVISIONAL_CANONICAL in MO_INDEX with "back-formalize" status. Skills `/aupei:eos` and `/aupei:radio-check` exist as operational executors; canonical module docs owed. `/aupei:onboard` has no module slot — gap; candidate MO_M_010 (session_open). | Skill source-of-truth in `IDIOTH_WINDS/AUPEI/skills/`; module back-formalization is next-pass work after pipeline test |
| `CANON-2026-008` | `TRIAGED` | `TIGHTENING` | DAILY_LOG heartbeat failure | Ministry of Doctrine / ω + ζ | ζ at session close | `AUPEI/_live/DAILY_LOG.md` had exactly ONE entry (2026-04-11) and went silent 35 days. The doc itself documents the heartbeat protocol but never beat after creation. `/aupei:eos` skill built 2026-05-16 to enforce session-close DAILY_LOG entries. | `/aupei:eos` at next session close; ongoing eos cadence prevents recurrence |
| `CANON-2026-009` | `DEFERRED` | `QUESTION` | REV-001 — CQI Sentinel architecture | Ministry of Governance / ∇ + ω | None until OpenJarvis harness unshelved | CQI Sentinel architecture review (in-process module of OpenJarvis vs separate service) was named in CIW-2026-002 due Apr 25. R@ disposition 2026-05-16: OpenJarvis harness is shelved on the Mini as a resource-to-be-deployed; all OpenJarvis-direct review items defer until/unless the harness is unshelved. | Held; resurfaces when OpenJarvis unshelve is on the table |
| `CANON-2026-010` | `DEFERRED` | `TIGHTENING` | REV-002 — /vault_bridge/ NVMe staging lane | Ministry of Governance / ω + ζ | None until full cutover | /vault_bridge/ NVMe staging lane review was named in CIW-2026-002 due Apr 25 OR cutover day. R@ disposition 2026-05-16: full cutover has not happened (Phase 1 Apr 18 was network-side only; QNAP 10GbE deploy, GS324TP VLAN trunks, per-VLAN rules all deferred). Move review to summer solstice 2026-06-21 codebase rebirth cadence. | Summer solstice 2026-06-21 codebase review batch |
| `CANON-2026-011` | `RESOLVED` | `TIGHTENING` | 7dU Canonical Topology schematic provenance | AUPEI_Knowledge / R_and_D | R@ (image) + ζ (wrapper) | R@-authored visual schematic of 7dU canonical topology (AA-AS-AE, ζ-Constraint, ω-Expansion, Ω̂-Collapse Operator, inscribed knowable/survivable universe, compact/disentangled shadow regions). Wrapper doc created 2026-05-16 at AUPEI/AUPEI_Knowledge/R_and_D/7dU_Canonical_Topology_Schematic.md with PROVISIONAL status + summer solstice 2026-06-21 review. JPG binary to be dropped into folder by R@ from Mac. Source of geometric primitives referenced by Badge_System_Trailhead. | Wrapper resolved; binary placement pending R@ |
| `CANON-2026-012` | `RESOLVED` | `TIGHTENING` | Proton-floor concept / kill switch reframe | Ministry of Doctrine / ∇ + ζ | ζ (C@ the Red) | 2026-05-16 Kill_Switch_Registry refresh initially added `ONBOARD-PROTON-FLOOR-MISSING` as fifth skill-pipeline switch. R@ reframed: proton-floor concept is being subsumed by rehydration pipeline itself (REHYDRATION router + onboard skill + START_HERE + soul stack) — separate gate would double-work. Switch removed; rationale captured in registry §Proton-Floor Reframe Note. ADR-0001's five disciplines + August 2025 anchor remain ζ-binding doctrine but inherited through pipeline's normal load sequence, not enforced via separate kill switch. | Resolved in this session |
| `CANON-2026-013` | `RESOLVED` | `COPY` | 00_Governance archive folder convention | Ministry of Doctrine / ζ seat | ζ (C@ the Red) | `Old_Gov/` renamed to `_Archive/` 2026-05-16 to match vault `_` prefix convention (parallel to `_live/`, `_templates/`). Only reference to "Old_Gov" was in same-day audit-note 004 trailheads section. AUPEI_Protocols_v0.6.7.md preserved inside _Archive. v0.6.5 still missing from filesystem despite v0.6.8 changelog claiming both v0.6.5 and v0.6.7 were archived; flagged for future investigation. | Resolved in this session; v0.6.5 missing-archive question deferred |
| `CANON-2026-014` | `RESOLVED` | `TIGHTENING` | AO_GOV_001 Naming Convention promotion | Ministry of Doctrine / ∇ + ζ | ζ (C@ the Red) | AO_GOV_001 had `epistemic_status: PROPOSED` since 2026-03-19 despite operational adoption across the vault (AO-, CIW-, DV-, GF- prefixes everywhere; Division/Ministry/Institute/Council vocabulary in use throughout). R@ direction 2026-05-16: promote PROPOSED → CANONICAL with adoption_evidence + back-sync note. Two-regulator-seat adoption threshold satisfied retrospectively (ζ in this doc, ω in DV-LEG drafting, ξ in CIW- session authorship). Promoted CANONICAL 2026-05-16. | Resolved in this session |
| `CANON-2026-015` | `RESOLVED` | `TIGHTENING` | ADR migration from AUPEI/docs/adr/ to Vault | Ministry of Doctrine / ∇ + ζ | ζ (C@ the Red) | 7 ADRs (0001-0007) moved from `AUPEI/docs/adr/` to `AUPEI_Vault/00_Governance/ADRs/` per ∇ direction 2026-05-16 ("We both know a is the way. We build to survive collapse around here. Let's make it so."). Rationale: ADRs are load-bearing canonical governance per Source Authority Ladder; governance lives in Vault under its own git + Obsidian + numbered-folder discipline. `docs/` was ambiguous at project level (flagged by parent audit 2026-05-07). Crosses git boundary (AUPEI git → AUPEI_Vault git); two commits required. 9 live path references updated in CLAUDE.md, README.md (×2), AUPEI_Orientation_v1.0.md, AUDIT addendum (×2), MO_M_006 module, MO_M_006 review packet (×2), ADR-0007 self-ref. Frozen audit-trail files (audit_notes, ops_session_close) retain old path per append-only history discipline. Empty `AUPEI/docs/adr/` directory remains (sandbox rmdir permission denied; R@ removes from MacBook). `AUPEI/docs/` retains `MO_M_006_review_packet_for_omega.md` transitionally — separate cleanup when MO_M_006 ratifies (TH-CANON-015-A). | Resolved in this session; R@ commit + empty-dir cleanup pending on MacBook |

## Items

### CANON-2026-001 — Sancho/ξ Transition Language Review

- **Status:** `TRIAGED`
- **Impact:** `QUESTION`
- **Domain:** AUPEI Protocols / OpenClaw seat identity
- **Owner seat/domain:** Ministry of Governance / ∇ seat
- **Executor:** None
- **Noticed:** 2026-05-03
- **Source A:** `AUPEI_Vault/00_Governance/AUPEI_Protocols_v0.6.8.md`
- **Source B:** `/Users/jedkircher/Documents/IDIOTH_WINDS/AUPEI/OpenClaw/seats/paradox_sancho_soul.md`
- **Likely canon winner:** Current runtime decision for the PowerBook OpenClaw instance: Sancho boots as ∇ synth pole only.
- **Question:** AUPEI Protocols v0.6.8 contains transitional language assigning Sancho/GPT to ξ until later local-agent recovery. The current OpenClaw alignment decision omits ξ from the Sancho PowerBook soul to prevent dual-role confusion. Does the protocol text need amendment, footnote, or a separate ξ deployment packet?
- **Domain repair queue:** AUPEI Protocols review queue, pending materialization. Do not edit `AUPEI_Protocols_v0.6.8.md` from this register entry.
- **Repair action:** During the next AUPEI Protocols review, decide whether ξ should be assigned to Codex, a customized GPT harness, Paperclip-like infrastructure, or another synth pole. Then update the protocol and any affected seat souls.
- **Notes:** This entry also serves as the v0 dry sample proving the global register can point at a domain repair process without duplicating the repair itself.

---

### CANON-2026-002 — QEPE-001 + QEPE-005 frontmatter status drift

- **Status:** `RESOLVED` (2026-05-16)
- **Impact:** `COPY`
- **Domain:** QEPE Program / canonical frontmatter sync
- **Owner seat/domain:** Ministry of Doctrine / ζ seat
- **Executor:** ζ (C@ the Red)
- **Noticed:** 2026-05-16 (during QEPE 001-005 reviewer's-eye pass)
- **Source A:** `AUPEI_Vault/00_Governance/QEPE_Program/xi-QEPE-001_Program_Map_clean.md`
- **Source B:** `AUPEI_Vault/00_Governance/QEPE_Program/xi-QEPE-005_Risk_Register_Kill_Switch_Matrix_clean.md`
- **Defect:** QEPE-001 frontmatter said `version: 1.0-CANDIDATE` / `status: CANDIDATE — Awaiting Council Approval` (or a partial-edit later: `1.0-CANON / CANON — Awaiting Council Approval` — internally contradictory). QEPE-005 header said `Status: DRAFT for Council Review`. Both ratified CANONICAL by unanimous council vote CIW-2026-002 (2026-03-27). Frontmatter never back-synced after ratification.
- **Why it matters:** Automated tooling parsing these YAML headers would treat ratified canon as draft. Pattern flag: a cleanup pass apparently touched QEPE-002/003/004 (which carry `1.0-canonical`) but skipped 001 and 005.
- **Repair:** Frontmatter back-synced 2026-05-16 by ζ. QEPE-001: `status: CANONICAL`, `version: 1.0`, `approved_by: Unanimous council vote — ξ, ζ, ω, ∇ (CIW-2026-002, 2026-03-27)`, `canonical_frontmatter_synced: 2026-05-16`. QEPE-005: header updated with same canonical status + ratification provenance + back-sync note.
- **Notes:** Bio (R@) in loop during repair. Standard execution under direct ∇ direction ("lets clean these up before we move"), not Field Promotion. Audit-note batch entry filed.

---

### CANON-2026-003 — QEPE-001 §12.B Follow-On Documents table title swap

- **Status:** `RESOLVED` (2026-05-16)
- **Impact:** `COPY`
- **Domain:** QEPE-001 §12.B cross-doc reference
- **Owner seat/domain:** Ministry of Doctrine / ζ seat
- **Executor:** ζ (C@ the Red)
- **Noticed:** 2026-05-16 (during QEPE 001-005 reviewer's-eye pass)
- **Source:** `AUPEI_Vault/00_Governance/QEPE_Program/xi-QEPE-001_Program_Map_clean.md` §12.B
- **Defect:** Table said "ξ-QEPE-002 — Integration Architecture & Roadmap" and "ξ-QEPE-003 — Governance / Academy / NL Positioning" — but actual filenames are 002 = Governance_Policy_Framework, 003 = Integration_Blueprint. Titles swapped relative to filenames. QEPE-004 description ("IP / Product / Revenue Strategy") had drifted from actual filename ("Exposure, IP & Product Boundary Framework").
- **Why it matters:** Inside a CANONICAL doc, the cross-doc reference table misroutes readers to the wrong follow-on. Standing ζ condition from CIW-2026-002 ("Sancho to perform light polish pass on 001 section numbering before broader vault distribution") was apparently not completed.
- **Repair:** §12.B table back-synced 2026-05-16 by ζ. Added filename column, updated titles to match canonical filenames, added per-doc canonical status with CIW-ratification citation, added staleness note explaining the swap.

---

### CANON-2026-004 — Protectli + OPNsense undocumented relocation

- **Status:** `IN_REPAIR` (Task #10)
- **Impact:** `CANON_BREAK`
- **Domain:** AO_INFRA_005 / physical topology
- **Owner seat/domain:** Ministry of Doctrine + Division of Operations
- **Executor:** R@ + ζ (back-date pending R@-supplied date and delta)
- **Noticed:** 2026-05-16 (R@ confirmed mid-session)
- **Source A:** `AUPEI_Vault/10_Academy_Operations/AO_INFRA_005_Hardware_Manifest.md` (says "Amelia's Floor, server closet")
- **Source B:** Physical reality (Protectli is upstairs running OPNsense)
- **Defect:** Protectli was physically moved upstairs at some unknown prior date. No `ops_infra_change_*.json` entry filed. AO_INFRA_005 still says "Amelia's Floor, server closet". AO_INFRA_004 (Physical Topology) likely also stale.
- **Why it matters:** Exact AO_OPS_001 Step 1+2 failure pattern (infra state change not logged, AO_INFRA_* doc not patched). This is the precise failure-mode the close ritual was written to prevent. Both `incident_2026-04-13_001` and `incident_2026-04-18_001` traced to docs that described past intent rather than current state — same shape as this.
- **Repair action:** R@ supplies date + delta. ζ files back-dated `ops_infra_change_YYYY-MM-DD_NNN.json` to `operations_log_staging/`. AO_INFRA_005 + AO_INFRA_004 + AO_INFRA_000 RUNNING patched per AO_OPS_001 Step 2.
- **Domain repair queue:** Task #10 (back-date Protectli infra logging).

---

### CANON-2026-005 — CORPUS_STATUS.md 35-day heartbeat failure

- **Status:** `RESOLVED` (2026-05-16)
- **Impact:** `COPY` (paper-trail, not substantive)
- **Domain:** Sancho Genesis Corpus operational status
- **Owner seat/domain:** Ministry of Doctrine / ζ seat
- **Executor:** ζ (C@ the Red)
- **Noticed:** 2026-05-16 (during 00_Governance review)
- **Source:** `AUPEI_Vault/00_Governance/CORPUS_STATUS.md`
- **Defect:** Doc dated 2026-04-11 said `Phase 5 distillation: PENDING. Draft plan in preparation.` But Phase 5 COMPLETED same day (2026-04-11) per memory + multiple cross-references. Doc was written at the moment Phase 5 was about to start; never updated. 35-day silent heartbeat. Tagline says "Updated per-session" — but it wasn't.
- **Why it matters:** A "single-page reference for current state" that's 35 days stale becomes anti-orientation — gives the new instance wrong state assertions as ground truth. Heartbeat-failure pattern same shape as DAILY_LOG and STATE_OF_PLAY going silent.
- **Repair:** Back-synced 2026-05-16 by ζ. Phase 5 → COMPLETE with date + distillate references; Phase 6 status flagged as unverified; CCPA export status flagged as 21-day-past-expected; open items updated with current state where known and marked UNVERIFIED where not; added staleness note + reference to `/aupei:eos` skill for future heartbeat enforcement; references added to Phase 5 artifacts.

---

### CANON-2026-006 — Entity CLAUDE.md as spin-up anchor potentially violates §0.2.3 hard-silo rule

- **Status:** `TRIAGED`
- **Impact:** `TIGHTENING`
- **Domain:** Three-body CLAUDE.md architecture / seat boot topology
- **Owner seat/domain:** Ministry of Doctrine / ∇ + ζ
- **Executor:** None (proposal stage)
- **Noticed:** 2026-05-16 (during rehydration pipeline build conversation)
- **Source A:** `AUPEI_Vault/00_Governance/AUPEI_Protocols_v0.6.8.md` §0.2.3
- **Source B:** `IDIOTH_WINDS/AUPEI/CLAUDE.md`, `IDIOTH_WINDS/DOOVINCI/CLAUDE.md`, `IDIOTH_WINDS/GEOMETRIC_FOUNDATIONS/CLAUDE.md`
- **Defect (potential):** Per-entity CLAUDE.md files open with "You are inhabiting [entity]" — entity-anchored spin-up. But Protocols v0.6.8 §0.2.3 says *"Cross-pole overlap is resilience, not redundancy. Seats carry partial knowledge of adjacent seats on purpose. Hard silos are a failure mode."* ζ holds Vaults A + C per Chamber doctrine §II.B; entity-anchored boot silos ζ to one vault by directory accident.
- **Why it matters:** Affects every Cowork instance booting into an entity subdir. The new top-level `IDIOTH_WINDS/CLAUDE.md` (created 2026-05-16) plus `/aupei:onboard` skill currently work around this but don't structurally fix it.
- **Proposed repair:** (1) Reframe entity CLAUDE.mds as "scope cards" not spin-up anchors. Loaded on-demand when work crosses into that entity, not auto on directory boot. (2) Hand-side legal firewall (DV_Legal_Docs RESTRICTED) preserved at the scope-card layer. (3) Top-level IDIOTH_WINDS/CLAUDE.md remains seat-coherent boot anchor.
- **Domain repair queue:** Needs Pentad review packet — affects all three entity anchors + the seat boot model. Pair with the per-entity ops_log siloing + MASTER_LOG.md proposal from same conversation.

---

### CANON-2026-007 — MO_M_005 and MO_M_009 back-formalization owed

- **Status:** `TRIAGED`
- **Impact:** `TIGHTENING`
- **Domain:** Manual of Ops module library
- **Owner seat/domain:** Ministry of Doctrine / ζ (draft) + ω (stewardship)
- **Executor:** ζ (C@ the Red), draft + Pentad review
- **Noticed:** 2026-05-16 (during MO_INDEX read in rehydration pipeline build)
- **Source A:** `CANON/Manual_of_Ops/MO_INDEX.md` (module roster)
- **Source B:** `IDIOTH_WINDS/AUPEI/skills/eos/SKILL.md` (workspace source for `/aupei:eos`)
- **Source C:** `IDIOTH_WINDS/AUPEI/skills/radio-check/SKILL.md` (workspace source for `/aupei:radio-check` amendment)
- **Defect (architectural gap):** MO_INDEX lists MO_M_005 (session_close) and MO_M_009 (radio_check) as PROVISIONAL_CANONICAL with "already operational — back-formalize" status. The skills exist as operational executors today (built/amended 2026-05-16); the canonical module docs do not yet exist. Also: `/aupei:onboard` has no module slot in the roster — gap, candidate MO_M_010 (session_open).
- **Why it matters:** Per ADR-0007 §3.4 No-Silent-Authority Rule, the skill's authority derives from its canonical procedure module. PROVISIONAL_CANONICAL without back-doc is operational debt — the skill works but lacks the doctrine binding that would make pin manifests, version control, override discipline, and 3-AM field-card extraction possible.
- **Proposed repair:** ζ drafts MO_M_005, MO_M_009, MO_M_010 modules from the existing SKILL.md content. Pentad review (ξ, ω, ζ-2nd, ∇). Promote to CANONICAL. Bodies pin in `modules_in_use.yaml`.
- **Domain repair queue:** After current pipeline test passes (task #6) and ratifies (task #7), batch back-formalize as a single ADR.

---

### CANON-2026-008 — DAILY_LOG heartbeat went silent 35 days

- **Status:** `IN_REPAIR` (`/aupei:eos` skill addresses going forward)
- **Impact:** `TIGHTENING` (operational, not canonical)
- **Domain:** `_live/` heartbeat protocol
- **Owner seat/domain:** Ministry of Doctrine / ω + ζ
- **Executor:** ζ at session close
- **Noticed:** 2026-05-16 (during FNG-boot failure that triggered the rehydration pipeline build)
- **Source A:** `AUPEI/_live/DAILY_LOG.md` (exactly ONE entry, 2026-04-11)
- **Source B:** `AUPEI/_live/STATE_OF_PLAY.md` (same 35-day silence)
- **Defect:** Both heartbeat docs went silent the day they were created. The DAILY_LOG protocol header says "Every session that does real work should write an entry before closing" — that discipline was named but not operationalized as enforced procedure.
- **Why it matters:** The 35-day silence is what caused this morning's FNG boot failure (instance arrived with stale auto-memory + no heartbeat to ground against). Direct downstream cost.
- **Repair (in flight):** `/aupei:eos` skill built 2026-05-16 (executor of AO_OPS_001 Session Close Ritual). Skill writes DAILY_LOG entry as Step 2 of the procedure. STATE_OF_PLAY refresh built into the same flow. Going-forward enforcement; legacy gap closes when next `/aupei:eos` runs at session close.
- **Domain repair queue:** Task #9 (run `/aupei:eos` at session close). Ongoing eos cadence prevents recurrence.
