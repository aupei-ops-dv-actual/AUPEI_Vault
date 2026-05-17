---
node_id: CORPUS-STATUS-001
title: "Sancho/PanzaGPT Genesis Corpus — Operational Status"
document_class: REFERENCE
epistemic_status: ACTIVE
author: C@ the Red (ζ seat)
date_minted: 2026-04-11
last_updated: 2026-05-16
prior_updates: [2026-04-11]
---

# Sancho/PanzaGPT Genesis Corpus — Operational Status

**Purpose:** Single-page reference for current state of the founding record archive. Updated per-session.

**Staleness note (2026-05-16, ζ):** This doc was last touched 2026-04-11 — same day Phase 5 distillation completed. The original revision listed Phase 5 as PENDING, which was outdated within hours of writing. Today's pass back-syncs Phase 5 → COMPLETE and flags items where 35-day-old assertions need live verification. The doc itself was a heartbeat-failure example: written once, never beat after. The new EOS contract (AO_OPS_001 + `/aupei:eos` skill) should prevent this in future.

---

## Archive State

| Metric | Value |
|--------|-------|
| Total conversations | 216 (202 real, 14 empty/unknown) |
| Total words | ~9,411,000 |
| Eras | 7 (GENESIS → DORMANT → REAWAKENING → FRAMEWORK_BUILD → GOVERNANCE → CRISIS_AND_RECOVERY → ACADEMY) |
| Salvage packets | 202 |
| Coverage | 100% of real conversations |
| Schema | Schema A (12 top-level keys) |
| Archive location | `genesis-extraction/04_SALVAGE_PACKETS/` |
| Master manifest | `PHASE4_MASTER_MANIFEST.md` |

## Phase Status

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 1 | CCPA request + raw export | COMPLETE |
| Phase 2 | Catalog + indexing | COMPLETE |
| Phase 3 | Mechanical extraction (structured JSON) | COMPLETE |
| Phase 4 | Interpretive salvage (human-adjudicated) | COMPLETE (2026-04-11) |
| Phase 5 | Seat memory distillation | **COMPLETE** (2026-04-11) — 5 seat distillates (ζ 609 lines, ω 834, ξ 671, Ω̂ 856, ∇ 908) in `genesis-extraction/05_SEAT_DISTILLATION/`. 4-stage pipeline (normalize → distill → cross-validate → harmonize). |
| Phase 6 | GraphRAG integration | PENDING — directive issued 2026-04-11; status as of 2026-05-16 unverified, treat as still PENDING absent fresher signal |

## Tier Distribution (as of 2026-04-11)

- CORE: 150 (69.8%)
- RELEVANT: 30 (14.0%)
- PERIPHERAL: 4 (1.9%)
- UNRELATED: 8 (3.7%)
- Untiered: 23 (10.7%)

20 R@-approved tier promotions applied. Most significant: IVY Grace Build (UNRELATED→CORE), PPA Evaluation for QRNG (UNRELATED→CORE), Email to Lex Friedman (PERIPHERAL→CORE).

## Reconciliation (Path A)

5-batch title comparison complete. 136 titles, 91.2% clean match.

Strongest unresolved seams:
1. Geometric_Foundations project-only cluster (6 titles)
2. Q-shapes and 7dU Algorithm (NOT_THERE, known conv ID)
3. TOE Equation Development (NOT_THERE)
4. "Unable to load conversation" (corrupted/inaccessible)

CCPA follow-up submitted 2026-04-11. Export expected ~Apr 25. **STATUS UNVERIFIED 2026-05-16** — past expected date by 21 days; needs live check at next ξ-touch session.

## Open Items (back-synced 2026-05-16)

- **G-Synthesist role:** RESOLVED (2026-04-11). ω seat fully specified (system kernel operational). Provenance preserved in Council_Seats/.
- **Cryptogenic memory scan:** Deferred (REV-003) — chamber task. Status unchanged as of 2026-05-16.
- **Path B/C targeting:** Awaiting chamber operational capability. Chamber MVP Phase 2 COMPLETE (2026-04-04) per memory; targeting probably now unblocked but unverified.
- **Phase 5 distillation:** COMPLETE (2026-04-11) — see Phase Status table above.
- **23 untiered packets:** Schema normalization status as of 2026-04-11 was "from parallel agent outputs." Status as of 2026-05-16 unverified.
- **CCPA export check:** Past expected date — needs follow-up.
- **GraphRAG build (Phase 6):** Directive issued 2026-04-11 per memory. Concrete progress 2026-05-16 unverified.

## Key Reference Documents

- `PHASE4_MASTER_MANIFEST.md` — Complete production accounting
- `PATH_A_MASTER_RECONCILIATION.md` — Reconciliation findings
- Per-era manifests in `04_SALVAGE_PACKETS/`
- `PANZA_MEMO_2026-04-11_PHASE4_COMPLETE.md` — Latest Panza tasking
- `genesis-extraction/05_SEAT_DISTILLATION/` — 5 seat memory distillates (Phase 5 output)
- `genesis-extraction/STAGE3_VALIDATION_REPORT.md` — Phase 5 cross-validation
- `genesis-extraction/PHASE5_CORPUS_STATUS.md` — Detailed Phase 5 status note

---

*Updated by C@ the Red (ζ seat), 2026-04-11; back-synced 2026-05-16 (Phase 5 status, CCPA staleness, open items, references added). Next update should be triggered by `/aupei:eos` whenever corpus state materially changes.*
