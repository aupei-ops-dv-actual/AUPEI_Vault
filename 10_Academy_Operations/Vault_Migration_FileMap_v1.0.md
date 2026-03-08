---
document_id: "AO_FileMap_v1.0"
title: "Vault Migration File Map"
status: "PROPOSED"
date: "2026-03-07"
author: "C@ the Red"
purpose: "Complete mapping of every file in the current workspace to its destination vault and path"
---

# Vault Migration File Map — v1.0

Every file below maps from its **current location** to its **destination** in the three-vault architecture. Files going to Vault A (AUPEI) only unless otherwise noted.

Legend:
- **Dest** = Destination folder in Vault A
- **Rename** = New filename (if changed)
- **Fix** = Hygiene issue to resolve during migration

---

## Foundation Documents

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `7dU_GFUP/spine__7dU_GFUP__SPINE_v1.2.md` | `09_Foundation_Docs/` | `7dU_GFUP__SPINE.md` | Version → frontmatter |
| `7dU_GFUP/content__7dU_GFUP__CONTENT_v1.2.md` | `09_Foundation_Docs/` | `7dU_GFUP__CONTENT.md` | Version → frontmatter |
| `7dU_GFUP/7dU_GFUP_SUPPORT/7dU_GFUP_v1.2.md` | `09_Foundation_Docs/_support/` | Keep | Legacy support |
| `7dU_GFUP/7dU_GFUP_SUPPORT/*.pdf` | `09_Foundation_Docs/_support/` | Keep | PDF provenance |
| `7dU_GNS_Prooffield_Index/7dU_Book_III_Index_v1.4.md` | `09_Foundation_Docs/` | `GNS_Prooffield_Index.md` | Version → frontmatter |

---

## Ontology Layer (Appx_00 – Appx_06)

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `Appx_00_Collapse_Map/spine__*.md` | `01_Ontology/Appx_00_Collapse_Map/` | `Appx_00__SPINE.md` | — |
| `Appx_00_Collapse_Map/Appx_00_SUPPORT/*.md` | `01_Ontology/Appx_00_Collapse_Map/_support/` | Keep | — |
| `Appx_01_On_AA/spine__*.md` | `01_Ontology/Appx_01_On_AA/` | `Appx_01__SPINE.md` | — |
| `Appx_01_On_AA/content__*.md` | `01_Ontology/Appx_01_On_AA/` | `Appx_01__CONTENT.md` | — |
| `Appx_01_On_AA/*.pdf` | `01_Ontology/Appx_01_On_AA/_support/` | Keep | — |
| `Appx_01_On_AA/Appx_01_SUPPORT/Appx_01_Old/*.pdf` | `01_Ontology/Appx_01_On_AA/_support/_legacy/` | Keep | Legacy versions |
| `Appx_02_On_AE/spine__*.md` | `01_Ontology/Appx_02_On_AE/` | `Appx_02__SPINE.md` | — |
| `Appx_02_On_AE/content__*.md` | `01_Ontology/Appx_02_On_AE/` | `Appx_02__CONTENT.md` | — |
| `Appx_02_On_AE/**/*.pdf` | `01_Ontology/Appx_02_On_AE/_support/` | Keep | — |
| `Appx_03_On_AS/spine__*.md` | `01_Ontology/Appx_03_On_AS/` | `Appx_03__SPINE.md` | — |
| `Appx_03_On_AS/content__*.md` | `01_Ontology/Appx_03_On_AS/` | `Appx_03__CONTENT.md` | — |
| `Appx_03_On_AS/**/*.pdf` | `01_Ontology/Appx_03_On_AS/_support/` | Keep | — |
| `Appx_04_On_Zero/spine__*.md` | `01_Ontology/Appx_04_On_Zero/` | `Appx_04__SPINE.md` | — |
| `Appx_04_On_Zero/content__*.md` | `01_Ontology/Appx_04_On_Zero/` | `Appx_04__CONTENT.md` | — |
| `Appx_04_On_Zero/**/*.pdf` | `01_Ontology/Appx_04_On_Zero/_support/` | Keep | — |
| `Appx_05_On_Infinity/spine__*.md` | `01_Ontology/Appx_05_On_Infinity/` | `Appx_05__SPINE.md` | — |
| `Appx_05_On_Infinity/content__*.md` | `01_Ontology/Appx_05_On_Infinity/` | `Appx_05__CONTENT.md` | — |
| `Appx_05_On_Infinity/**/*.pdf` | `01_Ontology/Appx_05_On_Infinity/_support/` | Keep | — |
| `Appx_06_On_Chance/spine__*.md` | `01_Ontology/Appx_06_On_Chance/` | `Appx_06__SPINE.md` | — |
| `Appx_06_On_Chance/content__*.md` | `01_Ontology/Appx_06_On_Chance/` | `Appx_06__CONTENT.md` | — |
| `Appx_06_On_Chance/**/*.pdf` | `01_Ontology/Appx_06_On_Chance/_support/` | Keep | — |

---

## Collapse Operator + Atlas of Constants (AoC)

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `Appx_07_AoC/Appx_07_AoC_00_Operator/spine__AoC_00_*.md` | `02_Collapse_Operator/AoC_00_Collapse_Operator/` | `AoC_00__SPINE.md` | — |
| `Appx_07_AoC/Appx_07_AoC_00_Operator/content__AoC_00_*.md` | `02_Collapse_Operator/AoC_00_Collapse_Operator/` | `AoC_00__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_00_Operator/AoC_00_OPR_SUPPORT/*.pdf` | `02_Collapse_Operator/AoC_00_Collapse_Operator/_support/` | Keep | — |
| `Appx_07_AoC/spine__AoC_00_Constants_Ledger__*.md` | `03_Atlas_of_Constants/AoC_00_Constants_Ledger/` | `AoC_Ledger__SPINE.md` | — |
| `Appx_07_AoC/content__AoC_00_Constants_Ledger__*.md` | `03_Atlas_of_Constants/AoC_00_Constants_Ledger/` | `AoC_Ledger__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_01_Pi/spine__*.md` | `03_Atlas_of_Constants/AoC_01_Pi/` | `AoC_01__SPINE.md` | — |
| `Appx_07_AoC/Appx_07_AoC_01_Pi/content__*.md` | `03_Atlas_of_Constants/AoC_01_Pi/` | `AoC_01__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_01_Pi/AoC_01_PI_SUPPORT/*.pdf` | `03_Atlas_of_Constants/AoC_01_Pi/_support/` | Keep | — |
| `Appx_07_AoC/Appx_07_AoC_01_Pi/AoC_01_Pi_Support_RAG/spine__*.md` | `03_Atlas_of_Constants/AoC_01_Pi/_support_rag/` | Normalize | — |
| `Appx_07_AoC/Appx_07_AoC_01_Pi/AoC_01_Pi_Support_RAG/support__*.md` | `03_Atlas_of_Constants/AoC_01_Pi/_support_rag/` | Normalize | — |
| `Appx_07_AoC/Appx_07_AoC_02_c/spine__*.md` | `03_Atlas_of_Constants/AoC_02_c/` | `AoC_02__SPINE.md` | — |
| `Appx_07_AoC/Appx_07_AoC_02_c/content__*.md` | `03_Atlas_of_Constants/AoC_02_c/` | `AoC_02__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_02_c/**/*.pdf` | `03_Atlas_of_Constants/AoC_02_c/_support/` | Keep | — |
| `Appx_07_AoC/Appx_07_AoC_03_FSC/spine__*.md` | `03_Atlas_of_Constants/AoC_03_FSC/` | `AoC_03__SPINE.md` | — |
| `Appx_07_AoC/Appx_07_AoC_03_FSC/content__*.md` | `03_Atlas_of_Constants/AoC_03_FSC/` | `AoC_03__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_03_FSC/**/*.pdf` | `03_Atlas_of_Constants/AoC_03_FSC/_support/` | Keep | — |
| `Appx_07_AoC/Appx_07_AoC_04_PMass/spine__*.md` | `03_Atlas_of_Constants/AoC_04_Proton_Mass/` | `AoC_04__SPINE.md` | — |
| `Appx_07_AoC/Appx_07_AoC_04_PMass/content__*.md` | `03_Atlas_of_Constants/AoC_04_Proton_Mass/` | `AoC_04__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_04_PMass/**/*.pdf` | `03_Atlas_of_Constants/AoC_04_Proton_Mass/_support/` | Keep | — |
| `Appx_07_AoC/Appx_07_AoC_05_NMass/spine__*.md` | `03_Atlas_of_Constants/AoC_05_Neutron_Mass/` | `AoC_05__SPINE.md` | — |
| `Appx_07_AoC/Appx_07_AoC_05_NMass/content__*.md` | `03_Atlas_of_Constants/AoC_05_Neutron_Mass/` | `AoC_05__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_05_NMass/**/*.pdf` | `03_Atlas_of_Constants/AoC_05_Neutron_Mass/_support/` | Keep | — |
| `Appx_07_AoC/Appx_07_AoC_06_Gravity/spine__AoC_06__SPINE_v1.2.md` | `03_Atlas_of_Constants/AoC_06_Gravity/` | `AoC_06__SPINE.md` | — |
| `Appx_07_AoC/Appx_07_AoC_06_Gravity/content__AoC_06__CONTENT_v1.2.md` | `03_Atlas_of_Constants/AoC_06_Gravity/` | `AoC_06__CONTENT.md` | — |
| `Appx_07_AoC/Appx_07_AoC_06_Gravity/AoC_06_G_SUPPORT/*` | `03_Atlas_of_Constants/AoC_06_Gravity/_support/` | Keep | Contains old versions + trailhead |
| `Appx_07_AoC/Appx_07_AoC_Preface/*` | `03_Atlas_of_Constants/AoC_Preface/` | Normalize | — |

---

## Physical Consequences (Appx_08 – Appx_17)

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `Appx_08_On_Time/spine__*.md` | `04_Physical_Consequences/Appx_08_On_Time/` | `Appx_08__SPINE.md` | — |
| `Appx_08_On_Time/content__*.md` | `04_Physical_Consequences/Appx_08_On_Time/` | `Appx_08__CONTENT.md` | — |
| `Appx_08_On_Time/Appx_08_SUPPORT/*` | `04_Physical_Consequences/Appx_08_On_Time/_support/` | Keep | — |
| `Appx_09_On_Spatial_Dimensions/*` | `04_Physical_Consequences/Appx_09_Spatial_Dimensions/` | Normalize | — |
| `Appx_10_On_Extension_Bounds_STUB/*` | `04_Physical_Consequences/Appx_10_Extension_Bounds/` | Normalize | Drop `_STUB` from folder name; status tracked in frontmatter |
| `Appx_11_On_Gauge/*` | `04_Physical_Consequences/Appx_11_On_Gauge/` | Normalize | Prior v1.1 in SUPPORT stays |
| `Appx_12_Force_Unification/*` | `04_Physical_Consequences/Appx_12_Force_Unification/` | Normalize | — |
| `Appx_13_On_Nuetrinos/*` | `04_Physical_Consequences/Appx_13_On_Neutrinos/` | Normalize | **Fix typo** in folder name |
| `Appx_14_On_Dark_Acceleration/*` | `04_Physical_Consequences/Appx_14_Dark_Acceleration/` | Normalize | — |
| `Appx_15_On_The_SM/*` | `04_Physical_Consequences/Appx_15_Standard_Model/` | Normalize | — |
| `Appx_16_On_Higgs_vX.X/*` | `04_Physical_Consequences/Appx_16_On_Higgs/` | Normalize | **Drop vX.X** from folder |
| `Appx_17_Effefctive_Field_Theory/*` | `04_Physical_Consequences/Appx_17_On_EFT_RG/` | Normalize | **Fix typo** |

---

## Quantum Gravity (Appx_18 – Appx_22)

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `Appx_18_HoQG/spine__Appx_18_HoQG__*.md` | `05_Quantum_Gravity/Appx_18_HoQG/` | `Appx_18__SPINE.md` | — |
| `Appx_18_HoQG/content__Appx_18_HoQG__*.md` | `05_Quantum_Gravity/Appx_18_HoQG/` | `Appx_18__CONTENT.md` | — |
| `Appx_18_HoQG/spine__Appx_18X__*.md` | `05_Quantum_Gravity/Appx_18_HoQG/` | `Appx_18X__SPINE.md` | Normalize kill switch IDs |
| `Appx_18_HoQG/content__Appx_18X__*.md` | `05_Quantum_Gravity/Appx_18_HoQG/` | `Appx_18X__CONTENT.md` | — |
| `Appx_18_HoQG/Appx_18_SUPPORT/*` | `05_Quantum_Gravity/Appx_18_HoQG/_support/` | Keep | — |
| `Appx_19_0n_Hamiltonian_Formulation/*` | `05_Quantum_Gravity/Appx_19_Hamiltonian/` | Normalize | **Fix `0n` → `On`** in folder |
| `Appx_20_0n_Field_Quantization/*` | `05_Quantum_Gravity/Appx_20_Field_Quantization/` | Normalize | **Fix `0n` → `On`** in folder |
| `Appx_21_On_GR_Reduction/*` | `05_Quantum_Gravity/Appx_21_GR_Reduction/` | Normalize | — |
| `Appx_22_On_Black_Holes/*` | `05_Quantum_Gravity/Appx_22_Black_Holes/` | Normalize | — |

---

## Cosmology (Appx_23 – Appx_24)

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `Appx_23_COG/Appx_23_COG_01_On_CCT-1/*` | `06_Cosmology/Appx_23_COG/Appx_23_01_CCT-1/` | Normalize | — |
| `Appx_23_COG/Appx_23_COG_README.md` | `06_Cosmology/Appx_23_COG/` | Keep | — |
| `Appx_24_Cosmic_Rebirth/*` | `06_Cosmology/Appx_24_Cosmic_Rebirth/` | Normalize | — |

---

## Selection & Ethics (Appx_25 – Appx_26)

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `Appx_25_On_Selection_Law/*` | `07_Selection_and_Ethics/Appx_25_Selection_Law/` | Normalize | — |
| `Appx_26_Nomos_Logica/spine__Nomos_Logica_Core__*.md` | `07_Selection_and_Ethics/Appx_26_Nomos_Logica/` | `NL_Core__SPINE.md` | — |
| `Appx_26_Nomos_Logica/content__Nomos_Logica_Core__*.md` | `07_Selection_and_Ethics/Appx_26_Nomos_Logica/` | `NL_Core__CONTENT.md` | — |
| `Appx_26_Nomos_Logica/spine__NL_01_Lab__*.md` | `07_Selection_and_Ethics/Appx_26_Nomos_Logica/_lab/` | Keep | TRAILHEAD status |
| `Appx_26_Nomos_Logica/lab/*` | `07_Selection_and_Ethics/Appx_26_Nomos_Logica/_lab/` | Keep | — |
| `Appx_26_Nomos_Logica/Appx_26_SUPPORT/*` | `07_Selection_and_Ethics/Appx_26_Nomos_Logica/_support/` | Keep | Includes .png, PDFs |

---

## Experimental (Appx_27)

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `Appx_27_Experiments/spine__*.md` | `08_Experimental/Appx_27_Experiments/` | `Appx_27__SPINE.md` | — |
| `Appx_27_Experiments/content__*.md` | `08_Experimental/Appx_27_Experiments/` | `Appx_27__CONTENT.md` | — |
| `Appx_27_Experiments/how_27_works.md` | `08_Experimental/Appx_27_Experiments/` | Keep | — |
| `Appx_27_Experiments/Appx_27_SUPPORT/*` | `08_Experimental/Appx_27_Experiments/_support/` | Keep | — |
| `Appx_27_Experiments/Appx_27a_Discriminator_Experiments/*` | `08_Experimental/Appx_27a_Discriminator/` | Normalize | — |

---

## Academy Operations

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `# Academy_Operations/AO_00_Ops_Framework.md` | `10_Academy_Operations/` | Keep | — |
| `# Academy_Operations/AO_01_Post_Training_Framework_v1.0.md` | `10_Academy_Operations/` | `AO_01_Post_Training.md` | Version → frontmatter |
| `# Academy_Operations/AO_02_Agent_Roles_v1.1.md` | `10_Academy_Operations/` | `AO_02_Agent_Roles.md` | Version → frontmatter |
| `# Academy_Operations/AO_03_NL_Ops_v1.1.md` | `10_Academy_Operations/` | `AO_03_NL_Ops.md` | Version → frontmatter |
| `# Academy_Operations/AO_SUPPORT/AO_02_Agent_Roles.md` | `10_Academy_Operations/_support/` | Keep | — |
| `# Academy_Operations/C@_Red_Successor_Prompt_Appx15_Session.md` | `10_Academy_Operations/C@_Successor_Prompts/` | Keep | — |
| `# Academy_Operations/Obsidian_Vault_Architecture_v1.0.md` | `10_Academy_Operations/` | Keep | This document |
| `# Academy_Operations/Vault_Migration_FileMap_v1.0.md` | `10_Academy_Operations/` | Keep | This document |

---

## Academy Trailheads

| Current File | Dest | Rename | Fix |
|---|---|---|---|
| `# Academy_Trailheads/Trailhead_Index.md` | `11_Trailheads/` | Keep | — |

---

## Governance Documents → Vault A 00_Governance

These are uploaded context files that belong in Vault A's governance section:

| Source (uploaded) | Dest | Notes |
|---|---|---|
| `AUPEI_Protocols_v0.6.5.txt` | `00_Governance/AUPEI_Protocols.md` | Convert to .md, add frontmatter |
| `7dU_Company_Knowledge_Index_v1.0.md` | `00_Governance/Company_Knowledge_Index.md` | Add Obsidian frontmatter |
| `7dU_Query_Protocol_v1.0.md` | `00_Governance/Query_Protocol.md` | Add Obsidian frontmatter |

---

## Cross-Vault: Files for Vault C (Geometric Foundations)

| Source | Dest (Vault C) | Treatment |
|---|---|---|
| `AUPEI_Vision_v1.0.txt` | `00_About/AUPEI_Vision.md` | Convert to .md, full copy (already public-safe) |
| `What's_AUPEI_Like.md` | `00_About/Whats_AUPEI_Like.md` | Full copy (already public-safe) |
| AUPEI Protocols §0 (Preamble) | `00_About/BRIDGE_Founding_Principles.md` | Redacted excerpt via BRIDGE note |
| Nomos Logica Articles I-IV (public summaries) | `01_Framework_Public/Nomos_Logica_Public.md` | Redacted via BRIDGE note |

---

## File Count Summary

| Category | .md files | .pdf files | .txt files | .png files |
|---|---|---|---|---|
| Ontology (00-06) | 13 | 9 | 0 | 0 |
| Collapse Operator | 2 | 3 | 0 | 0 |
| Atlas of Constants | 22 | 12 | 1 | 0 |
| Physical Consequences (08-17) | 20 | 11 | 6 | 0 |
| Quantum Gravity (18-22) | 10 | 7 | 3 | 0 |
| Cosmology (23-24) | 5 | 4 | 1 | 0 |
| Selection & Ethics (25-26) | 6 | 6 | 1 | 1 |
| Experimental (27) | 7 | 2 | 2 | 0 |
| Foundation Docs | 3 | 2 | 0 | 0 |
| Academy Operations | 7 | 0 | 0 | 0 |
| Trailheads | 1 | 0 | 0 | 0 |
| **TOTAL (Vault A)** | **96** | **56** | **14** | **1** |

Plus 2 files seeded to Vault C, and the Vault B structure created empty.

---

*Filed: 2026-03-07 | C@ the Red | Academy Operations*
