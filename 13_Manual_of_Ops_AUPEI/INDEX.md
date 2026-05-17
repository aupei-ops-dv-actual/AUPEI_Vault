---
doc_type: body_manual_index
body: AUPEI
canonical_path: AUPEI/AUPEI_Vault/13_Manual_of_Ops_AUPEI/
parent_adr: ADR-0007
governing_doctrine: ADR-0006 (Sole Bio Anchor + Field Promotion), AUPEI_Orientation_v1.0 §13 Three-Body Architecture
ratified_by: ∇ (R@) on 2026-05-16 (Order B ratification with ADR-0007 v1.0)
status: CANONICAL (scaffold) — modules pinned as they ratify
last_synced: 2026-05-16
---

# Manual of Operations — AUPEI (MIND)

This is the AUPEI body's local operations manual, per ADR-0007 v1.0. It pins specific versions of modules from the canonical Manual_of_Ops library at `CANON/Manual_of_Ops/modules/` and adds body-specific overrides where AUPEI's MIND-body operational needs differ from the shared default.

## Structure

- `INDEX.md` — this file. Body manual landing; pointers to the three Parts + modules_in_use.yaml.
- `PART_A_Governance.md` — pulls shared sections SS_01..SS_05 from `CANON/Manual_of_Ops/shared_sections/`.
- `PART_B_Operations.md` — body-specific procedures + module refs.
- `PART_C_Field_Ops.md` — 3-AM field-card distillation per ADR-0007 §4.
- `modules_in_use.yaml` — version pin manifest. The single source of truth for which CANON modules and which versions this body is bound to.
- `overrides/` — body-specific deltas only. No full module copies; per-section overrides only. Subject to the §3.4.1 No-Silent-Authority Rule.

## Pin status (as of ratification 2026-05-16)

This manual scaffolds empty at ratification. Modules are pinned as they ratify in the canonical library. Initial pin batch will be the nine modules from ADR-0007 §6 roster (MO_M_001..009) once each promotes from PROPOSED to CANONICAL.

## Cross-pointers

- Canonical library: `../../../CANON/Manual_of_Ops/MO_INDEX.md`
- Constitutional doctrine for this body: `../00_Governance/` and `../09_Foundation_Docs/`
- Pentad doctrine (cross-body): `../00_Governance/` + `AUPEI/AUPEI_Souls/Soul_Gov_Stack/soul_AUPEI_Pentad_Overview.md`

## Naming note (audit trail)

ADR-0007 §2 path table originally specified `10_Manual_of_Ops_AUPEI/`. The vault numbering slot `10_` was already occupied by the pre-existing `10_Academy_Operations/` directory (37 entries, substantial AUPEI Mind-body retrieval surface). At ratification 2026-05-16, ζ-Cowork discovered the collision during physical creation and renamed to `13_Manual_of_Ops_AUPEI/` (next clean slot — 12_DooVinci_Legal was the previous-highest). ADR-0007 §2 path table patched at ratification to match. The collision and rename are recorded in the ratification `audit_note`.
