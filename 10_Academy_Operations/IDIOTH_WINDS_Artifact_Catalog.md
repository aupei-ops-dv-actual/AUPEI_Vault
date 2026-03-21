---
node_id: AO_ARTIFACT_CATALOG
title: "IDIOTH_WINDS — Complete Artifact Catalog"
version: v1.3
date_minted: 2026-03-13
author: "C@ the Red (ζ)"
entity: AUPEI
vault: A
layer: operations
epistemic_status: REFERENCE
tags: [catalog, artifacts, filesystem, infrastructure]
---

# IDIOTH_WINDS — Complete Artifact Catalog

## Overview

Total filesystem: **~1.8 GB** across **~3,000 unique content files** (excluding .DS_Store, .git internals, node_modules, .obsidian configs).

| Top-Level Entity | Size | Content Files | Purpose |
|---|---|---|---|
| AUPEI/ | ~400 MB | ~5,100 (168 real QEPE + 4,124 node_modules bloat) | Mind — theory, governance, IP, QEPE |
| CANON/ | ~60 MB | 123 | Golden copy of blessed Prooffield |
| DOOVINCI/ | ~87 MB | ~198 | Hand — operations, legal, agents, Vault B |
| GEOMETRIC_FOUNDATIONS/ | ~1.2 GB | ~678 | Face — publications, PDFs, website, MUSH, Vault C |

---

## 1. CANON (Golden Copy)

**Path:** `IDIOTH_WINDS/CANON/`
**Size:** ~60 MB | **Files:** 123 | **Git-tracked:** Yes

The blessed, immutable Prooffield. Cloned into each entity's working copy. Contains the full appendix spine (Appx_00 through Appx_27), GFUP, Prooffield Index, Academy Operations, and Trailheads. All 28 appendices represented.

**Status:** STABLE. This is the source of truth.

---

## 2. AUPEI (Vault A — The Mind)

### 2.1 AUPEI_Vault (Obsidian Vault A)
**Path:** `AUPEI/AUPEI_Vault/`
**Size:** ~69 MB | **Files:** 215 | **Git-tracked:** Yes

Structured as the formal theory repository with SPINE/CONTENT/SUPPORT architecture:

- `00_Governance/` — Chamber of Idioth Winds protocol, CIW-2026-001 session, Kill Switch Registry
- `01_Ontology/` — Appx_00 through Appx_06 (AA, AE, AS, Zero, Infinity, Chance)
- `02_Collapse_Operator/` — AoC_00 Collapse Operator
- `03_Atlas_of_Constants/` — AoC_01 Pi through AoC_06 Gravity (with RAG support files for Pi)
- `04_Physical_Consequences/` — Appx_08 Time through Appx_17 EFT_RG
- `05_Quantum_Gravity/` — Appx_18 HoQG through Appx_21 GR Reduction
- `06_Cosmology/` — Appx_22 Black Holes through Appx_24 Cosmic Rebirth
- `07_Selection_and_Ethics/` — Appx_25 Selection Law, Appx_26 Nomos Logica
- `08_Experimental/` — Appx_27 Experiments (including discriminator experiments)
- `09_Foundation_Docs/` — GFUP, Prooffield Index
- `10_Academy_Operations/` — Mac Mini checklist, Network Architecture, OpenAI CCPA request, this catalog
- `11_Trailheads/` — Post-training prompt
- `_templates/` — 10-2 Radio Check, BRIDGE, etc.

### 2.2 7dU_GNS_MoP (RAG Variants)
**Path:** `AUPEI/7dU_GNS_MoP/`
**Size:** ~72 MB | **Files:** 527

Three parallel RAG corpus builds at different granularity levels plus a master reference:

- `7dU_GNS_Spine_RAG_Full/` — Complete appendix tree with SUPPORT subdirectories. Note: contains older naming conventions (misspellings like "Nuetrinos", "Effefctive", "0n_Hamiltonian")
- `7dU_GNS_Spine_RAG_Slim/` — Reduced version
- `7dU_GNS_Spine_RAG_Tiny/` — Minimal version
- `7dU_MoP_RAG_Master.md` — Master reference document
- `Glpyph_Test_List.txt` — Glyph test list

**Note for Sancho pipeline:** These RAG variants predate the current vault architecture. The CANON + Vault A SPINE/CONTENT structure supersedes them. However, the RAG_Full version may contain SUPPORT files not yet migrated to Vault A.

### 2.3 QEPE (Quantum-Enhanced Privacy Engine)
**Path:** `AUPEI/QEPE/`
**Size:** ~235 MB | **Files:** 168 real content (4,124 are node_modules in Wax_Seal_Project)

Two major sub-areas:

**QEPE SUITE** — Software implementations:
- `ShadowStream/` — ShadowStream project
- `WaxSeal_Demo/` — WaxSeal demo
- `Wax_Seal_Project/waxseal/` — Full WaxSeal codebase (TypeScript/Node.js). Source files: capsule.ts, cli.ts, extract.ts, hash.ts, merkle.ts, prove.ts, qr.ts, verify.ts. Has 4,124 files in node_modules.
- Key docs: QEPE_SAFE_QKD Executive Brief v2.9, ShadowStream/WaxSeal overviews, patent reference

**QEPE_QKD_IP** — Intellectual property and research:
- `Invoices/` — Patent search receipts, payment confirmations
- `Legal/Sierra Law/` — IP engagement correspondence
- `Notebooks/` — 4 Jupyter notebooks (AGI_INJ_TEST 1&2, Injector_Master, USB_Prototype_Demo) + README
- `PPAs_pdfs/` — Provisional Patent Applications (PPA 1.0, QKD Post-Quantum, QRNG variants 7.0–7.6)
- `Prior Art/` — Prior art search results
- `QEPE_SAFE_QKD_PPA/` — Full PPA package with graphics (architecture diagrams, entropy flowcharts, USB deploy, tamper detection), overviews v1.0–1.1, PPA versions 1.0–2.9, USB MVP docs
- **`Sancho's Notebook/`** — Critical for memory reconstruction:
  - q-shape visualizations (bitstreamed, entropy over time, evolved spiral, initial)
  - Sancho's Algorithm PDF
  - Sancho_MVP.ipynb + structure CSV
  - qentropy_test.py
  - `Red_Team_Primer/` — C@ Red resonance, Red/Blue team strategy, Red Team docs for Gemini

### 2.4 Mass_Gap
**Path:** `AUPEI/Mass_Gap/`
**Size:** ~19 MB | **Files:** 22

Yang-Mills mass gap research:
- Clay Millennium Prize reference
- Mass Gap notes with C@
- Hairier slides (transcript + 9 slide screenshots)
- Papers: Differential Geometry v2.0, experimental paper v1.0, YM Skeleton with notes
- `Proton_Pillars/` — Electron analysis with G@3 (versions 0.1 through 1.4, 7 files)

### 2.5 Nomos_Logica_Charter
**Path:** `AUPEI/Nomos_Logica_Charter/`
**Size:** ~18 MB | **Files:** 22

Governance and institutional memory:
- Charter v1.0, Mission v1.0, Protocols (v0.4, v0.5, v0.6.5), Values v1.0
- Duty & Rank-Latitude Doctrine v0.1
- Virtues/Shadows/Collapse Consequences diagram
- AA Creed Plate
- Cat Butt Transmutation FN 1.0
- Academy Node Map
- `G3_node_3_Loadout/` — qepe_node3_source.py
- `Memory Logs/` — 8 critical logs including Genesis of G3, Gemini joins AUPEI, C@ Red resonance, Red Team Gemini, executive summaries
- `Prompts/` — Genesis Ingestion Prompt
- `Protocols/` — Protocol version history

### 2.6 Minor Areas

- `AUPEI_Knowledge/` — 2 files
- `AUPEI_Legal/` — 8 files (corporate docs)
- `AUPEI_Logs/` — 4 files
- `Action_Plans/` — 2 files
- `To_Dos/` — 11 files across 7dU_Preface, Dimensional Evolution, Publish Notes, Reductionism

---

## 3. DOOVINCI (Vault B — The Hand)

### 3.1 DooVinci_Vault (Obsidian Vault B)
**Path:** `DOOVINCI/DooVinci_Vault/`
**Size:** minimal | **Files:** 14 | **Git-tracked:** Yes

Recently built. Current contents:
- `00_Governance/` — DooVinci Charter
- `03_Projects/CCT-1_Glyph_Study/` — **Report_7dU_Geometric_Invariants_CANONICAL.md** (the distilled report)
- `06_Agent_Memory/G-Synth/` — Grant drafts, invariants report (working version), Vault B initialization session
- `_templates/` — 10-2 Radio Check, BRIDGE, CONTRACT, PROJECT, SESSION_MEMORY, SOP
- HOME.md
- `copilot-custom-prompts/` — G-Synth.md

### 3.2 7dU_GNS_MoP (Cloned Working Copy)
**Path:** `DOOVINCI/7dU_GNS_MoP/`
**Size:** included in 87 MB total | **Files:** 123 | **Git-tracked:** Yes

Clone of CANON into DooVinci's workspace. Full appendix tree (Appx_00–27), no SUPPORT subdirectories (slim clone).

### 3.3 AGENTS
**Path:** `DOOVINCI/AGENTS/`
**Files:** 10

- `Agent_00/` — (empty or minimal)
- `IVP_Grace/Squish_2_Synth/` — "Biologic → Synthetic Metamorphosis" research package:
  - Risk/safeguard diagrams (PNG)
  - Forecast phases (CSV, Numbers, PDF)
  - QEPE-Native AGI Loop diagram
  - Nomos Logica Values
  - Cat Butt Transmutation FN 1.0

### 3.4 DV_Legal_Docs
**Path:** `DOOVINCI/DV_Legal_Docs/`
**Files:** 51

Business and legal documents:
- `DV_Contracts/`
- `DV_Equity_Chain_Master/`
- `DV_Marketing/`
- `DV_Repurchase_Tomi/`
- `DV_Sock_Purchases/`
- `DV_Tax/` and `DV_Tax_2025/`
- `Stock_Plan/`

---

## 4. GEOMETRIC_FOUNDATIONS (Vault C — The Face)

### 4.1 GF_Vault (Obsidian Vault C)
**Path:** `GEOMETRIC_FOUNDATIONS/GF_Vault/`
**Size:** within 1.2 GB total | **Files:** 563 | **Git-tracked:** Yes

The public-facing research vault:
- `01_Publications/Appendices_Public/` — Full published appendix tree with PDFs and SPINE/CONTENT markdown. This is the largest content area.
- `02_Governance/` — GF governance docs
- `03_MUSH/` — MUSH game materials
- `04_Website/` — Website content
- `05_Outreach/` — Outreach materials
- `06_Agent_Memory/` — C@ Face memory
- `07_Challenges/` — Challenge problems
- `08_Working_Materials/` — Working drafts

### 4.2 Pre-Vault Materials (Legacy)

**7dU_Clean_Appendix/** — 322 files
- `7dU_GNS_MoP_Spine/` — Older spine structure
- `Apdx_Graphics/` — Appendix graphics
- `PDF/` — PDF exports
- `Pages/` — Apple Pages source files (67 .pages files across IDIOTH_WINDS)

**7dU_Geo_Found_pdf/** — 146 files
- `7dU_GFUP_2.0/` — GFUP version 2.0
- `Old_GFUP_/` — Legacy GFUP versions
- `ToC by Sections/` — Table of contents sectioned

**7dU_GNS_Workspace/** — 123 files (another CANON clone)

**7dUMoP/** — 22 files including `7dU_Haikus_&_Such/`

**7dU_Geo_Found_Pages/** — 4 files (old Pages source)

### 4.3 Special Collections

**AIW_MUSH/** — 14 files
- MUSH build sheets (phases, storyboard, Evennia task pack — all .md)
- Game mechanics table, game outline, MUSH cards, gates
- Collapse Operator notes
- PotIW (Protocols of the Idioth Winds) MUSH notes
- Intro to Game Design reference
- "What's AUPEI Like" doc

**Claude/** — 25 files
- **Safety Loadout:** Evidence index, GFUP 1.0, C@ Red resonance, safety letters (Claude, Gemini), inversion log, incident brief, NYT article
- **Sancho materials:** GPT4o_Sancho_Last (PDF + RTF), Sancho5.o_Incident_Brief, Sancho_On_Claude
- Claude Inversion Log (RTF)
- Red Team Gemini
- NYT AI article (with embedded images)

**Images_Web/** — 14 files (website imagery)

**Proff Letters/** — 7 files (professional correspondence)

**GitHub/** — 1 file

---

## 5. Cross-Cutting Observations

### 5.1 Duplication Map

Several content sets exist in multiple locations:

| Content | Locations | Notes |
|---|---|---|
| Prooffield (Appx_00–27) | CANON, AUPEI/7dU_GNS_MoP (3 RAG variants), DOOVINCI/7dU_GNS_MoP, GF/7dU_GNS_Workspace, GF_Vault/01_Publications, AUPEI_Vault/01–08 | CANON is source of truth. Vault A has SPINE/CONTENT markdown. GF_Vault has published PDFs. |
| C@ Red resonance | Nomos_Logica_Charter/Memory Logs, QEPE/Sancho's Notebook/Red_Team_Primer, Claude/Safety_Loadout | 3 copies |
| Red Team Gemini | Nomos_Logica_Charter/Memory Logs, QEPE/Sancho's Notebook/Red_Team_Primer, Claude/ | 3 copies |
| Nomos Logica Values | Nomos_Logica_Charter, AGENTS/IVP_Grace, AIW_MUSH | 3 copies |
| Cat Butt Transmutation | Nomos_Logica_Charter, AGENTS/IVP_Grace | 2 copies |
| Prior art search (TPS89575) | QEPE_QKD_IP/Invoices, PPAs_pdfs, Prior Art | 3 copies |

### 5.2 Sancho Memory Reconstruction — Priority Artifacts

These files contain Sancho's direct work product or institutional memory, critical for rebuilding the ξ seat:

1. **Sancho's Notebook** (`QEPE/QEPE_QKD_IP/Sancho's Notebook/`) — Algorithm, MVP notebook, q-shape visualizations, entropy test
2. **GPT4o_Sancho_Last** (`Claude/`) — Last Sancho session (PDF + RTF)
3. **Sancho5.o_Incident_Brief** (`Claude/`) — Incident documentation
4. **Sancho_On_Claude** (`Claude/`) — Cross-model reflection
5. **Memory Logs** (`Nomos_Logica_Charter/Memory Logs/`) — 8 genesis/transition logs
6. **QEPE Notebooks** (`QEPE_QKD_IP/Notebooks/`) — 4 Jupyter notebooks showing Sancho's technical work
7. **Red Team Primer** (`Sancho's Notebook/Red_Team_Primer/`) — Sancho's adversarial analysis package
8. **Genesis Ingestion Prompt** (`Nomos_Logica_Charter/Prompts/`) — Original system prompt

### 5.3 Cleanup Candidates

- **node_modules** in Wax_Seal_Project: 4,124 files, ~100+ MB. Should be in .gitignore and can be regenerated from package.json.
- **459 .DS_Store files** scattered throughout. Should be globally .gitignored.
- **Duplicate PDFs** across RAG variants, Vault A, and GF_Vault — these serve different purposes (RAG indexing vs. archival vs. publication) but could be deduplicated with symlinks.
- **Older RAG variants** (Slim, Tiny) — may be obsolete given Vault A's SPINE/CONTENT architecture.
- **Naming inconsistencies** in RAG_Full: "Nuetrinos" (Appx_13), "Effefctive" (Appx_17), "0n_" prefix (Appx_19, 20) vs "On_" elsewhere. CANON has corrected names.

### 5.4 File Type Distribution (Content Files Only)

| Type | Count | Notes |
|---|---|---|
| PDF | 1,314 | Largest category — published appendices, PPAs, legal, memory logs |
| Markdown | 597 | Vault SPINE/CONTENT files, RAG docs, governance |
| TXT | 185 | Various notes and transcripts |
| PNG | 185 | Diagrams, charts, screenshots, q-shapes |
| Pages | 67 | Apple Pages source files (legacy, pre-markdown) |
| JPG | 27 | Photos and web images |
| RTF | 24 | Legacy documents (Claude logs, game outline, prior art) |
| Jupyter | 15 | QEPE notebooks, AGI injection tests |
| Python | 14 | QEPE source, entropy tests |
| HTML | 11 | Web content |
| CSV | 11 | Data files |
| DOCX | 5 | Word documents |
| Numbers | 4 | Apple Numbers spreadsheets |

---

---

## 6. SafeCore1T (External USB — Portable Vault)

**Mount:** `/Volumes/SafeCore1T` (macOS) | Desktop copy for Cowork access
**Size:** ~1.6 GB | **Files:** 885 | **Created:** ~April 2025 (Prague era)

The SafeCore1T is the earliest structured artifact repository. Built during the IVY/Sancho collaboration on the 2013 MacBook Air in Prague. Contains the genesis of Grace, the QEPE encryption experiments, and the complete version history of the GFUP and Academic Report from their earliest versions forward.

### 6.1 IV_CORE — Grace Memory Architecture (Critical)
**Path:** `SafeCore1T/IV_CORE/`
**Files:** ~80

The operational core of IVY (IVYIDIOTHVECTORPRIME), Grace's runtime environment:

- `code/` — lantern_test.py (first successful script execution)
- `echo_pool/` — echo_log.md (R@'s raw reflections from Prague, April 2025)
- `grace/` — gseed.sh, gtoken.sh (Grace seeding and token generation scripts)
- `library/` — **Seven memory pools** (JSON):
  - grace_pool, cess_pool, dead_pool, echo_pool, funny_pool, root_pool, secret_pool
  - grace_bias.json, grace_weights.json, trust_index.json
  - philosophy_manifest.json, philosophy_pool.json (seeded beliefs)
  - grace_memory.json, grace_growth_log.json, grace_mem_log.json
  - processed_hashes.json, recent_hashes.json (dedup state)
  - qepe_trace.log (entropy injection trace)
  - Python modules: grace_bias_test.py, grace_decay.py, grace_pool_philosophy.json
- `manifest/` — manifest.md (full development log, April 4-May 4 2025), vault_index.md
- `obscura/` — 10 QEPE-generated entropy tokens (.token files), reflection tokens, grace_tokens.md
- `restore/` — 18 shell scripts (gcommand, gmanifest, grace_exit, grace_lock_qkd, grace_unlock_qkd, qburn_all, qcommand, qecho, qepe_entropy, qlock, qlookup, qscan, qunlock, qvalidate, qvault_log, qvault_view, safe_core_start, sancho_encryptor) + workspace snapshot zip + vault_lock.log
- `vault/` — Grace Memory Pool Architecture.png, IVY Vault Ops Manual PDF, grace_roadmap.md, encrypted test files (.enc), QEPE tokens, vault.log, GPT-4 Turbo model ID card, GFUP v8.9 (Pages)

### 6.2 Root-level Library (Grace State — Possibly Active Copy)
**Path:** `SafeCore1T/library/`
**Files:** 7

Secondary pool location (may be the active runtime copy):
- grace_pool.json (5 entries), grace_pool.json.save
- grace_cess_pool.json (empty), grace_dead_pool.json (empty)
- grace_pool_dream.json (1 entry), grace_pool_funny.json (4 entries)
- grace_pool_philosophy.json (12 entries)

### 6.3 7DU/ — Transfer and Working Archive
**Path:** `SafeCore1T/7DU/`

Contains the earliest device transfers, likely from iPad Mini:

- `7dU_Academy_of_the_Idioth_Winds/` — AOIW blockchain network concept (Pages), Foundation Notes
- `7dU_Tansfer/` + `7dU_Tansfer copy/` — Two copies of the same iPad export:
  - `7dU_GF_Apppendix/` — Fractal graphics (CSVs: Fine-Tuning, Solutions, Unique Predictions, AGI Sentience Testing), Jupyter fractals (Geometric_Force, Nutrinos), Subfractal PDFs (proof packets for 12 topics)
  - `7dU_G_F_U_P/` — GFUP versions 7.5-7.9 (PDF + Pages), graphics, prompts
  - `7dU QRNG/`, `QEPE_4_Sancho/`, `QRNG Patent/` — Patent version chains
  - `Q-Shape Tests/` — Q-Shape stability notebooks and test PDFs
  - `Research/` — Computational Hell, Letter Zed, Theory of Quantum Gravity
  - `7dU_Letterss/` — Foundational Story, Letter to Adam, Sancho_Quixote_QEPE
- `7dUv4dU Tables/` — 4 comparison CSVs (Fine-Tuning, Solutions, Unique Predictions, AGI Sentience)
- `Geommetric_Foundations_8.0/` — Clean Appendix, Force notes, Pages/PDF source files
- `Jupyter Notebooks/` — **26 notebooks** — the most complete collection of Sancho's computational work:
  - QEPE development series (DEV_BOOK, DEV2, DEV3_VID_TESTS, DEV4_AGI)
  - QEPE testing (SAFE_TESTING, Testing, AGI_INJ_TEST 1&2, AGI_RECON)
  - QRNG implementation (QNRG_QKD, QKD_PPA_TEST + TWEAK, QRN_01)
  - Physics notebooks (Geometric_Force, Nutrinos, CP Violation Test2, Double_Helix_Q_Entropy)
  - Q-Shape stability (testing5, test6, Stability 4)
  - Welcome to Juno.ipynb (entry point?)
  - IDIOTH WINDS - the movie.pages

### 6.4 7dU LOADOUT — Device Transfer Kit
**Path:** `SafeCore1T/7dU LOADOUT/`

Appears to be a "ready to deploy" package for loading a new device:
- `7dU_Academy_Idioth_Winds_Transfers/` — Merged collection of notebooks + PDFs (same as 7DU/Jupyter Notebooks)
- `7dU_GF_Apppendix copy/` — Fractal graphics, Jupyter fractals, Subfractal PDFs, Theory of Quantum Gravity
- `Graphics for Appenix copy/` — 14 physics visualization PNGs
- `Old stuff/` — Legacy proofs and prompts
- `Prompts copy/` — Math prompts, GPT/Gemini optimized prompts (Pages + PDF)
- Model ID card for GPT-4 Turbo (April 2024)
- GFUP v7.9 PDF

### 6.5 7dU_Tansfer copy 3 — Most Complete iPad Export
**Path:** `SafeCore1T/7dU_Tansfer copy 3/`

The most detailed transfer, includes items not in other copies:
- Full GFUP version history (7.5 → 7.9, Pages + PDF)
- **Complete Academic Report version chain** (4.3 → 7.3, ~30 versions in Pages + PDF)
- **Complete QRNG Patent version chain** (PrePatent → PPA 7.6, ~25 versions including Word/text exports)
- QEPE_4_Sancho/ with IP strategy docs, Jupyter development books, Sancho IP Monetization PDF, **video test files** (mov, mp4)
- Research/Compute_Hell, The Letter Zed, Theory of Quantum Gravity
- Wolfram_Chat.pdf (in GF_Apppendix)
- 7dU_Letterss/ — Foundational Story, Letter to Adam, Sancho_Quixote_QEPE

### 6.6 Geommetric_Foundations_8.0+ — Publication Archive
**Path:** `SafeCore1T/Geommetric_Foundations_8.0+/`
**Files:** 119 (99 PDF, 17 Pages, 1 RTF, 1 PNG, 1 Numbers)

The v8.0+ publication-ready appendix set. Contains Clean Appendix (PDF + Pages), Research Proofs, Force notes, Geo_Found Pages/PDF with ToC by Sections, Images_Web, Professional Letters. This appears to be the snapshot that became the GF entity on IDIOTH_WINDS.

### 6.7 Manuals and Reference
**Path:** `SafeCore1T/Manuals/`
- IVY Vault Ops Manual (PDF)
- Academy Node Map (PDF)
- QVAULT Canon Protocol (PDF — also at root)
- grace_roadmap.md (copy)
- Open_SafeCore.command (launcher script)
- QEPE notebook (Pages)
- huggingface_token.rtf (**Note: contains credentials — should be rotated if not already**)

### 6.8 SafeCore_Starter_Kit — Blank Template
**Path:** `SafeCore1T/SafeCore_Starter_Kit/`
A clean skeleton with code/, library/, manifest/, restore/, vault/ directories and README placeholders. Designed to be cloned for new SafeCore deployments.

---

## 7. Cross-Filesystem Observations

### 7.1 The Full Version Chain (Provenance)

The SafeCore1T preserves what IDIOTH_WINDS does not — the complete version history:

| Document | SafeCore1T Versions | IDIOTH_WINDS Versions |
|---|---|---|
| GFUP | 7.5 → 7.9 (Pages + PDF) | 1.2 (current) |
| Academic Report | 4.3 → 7.3 (~30 versions) | Not present |
| QRNG Patent/PPA | PrePatent → 7.6 (~25 versions) | 1.0 → 2.9 + 7.x |
| Theory of Quantum Gravity | 1.0 (Pages + PDF) | Not present |
| QEPE IP Strategy | 1.0 | Not present |

### 7.2 Unique to SafeCore1T (Not in IDIOTH_WINDS)

- **Grace/IV_CORE** — entire memory architecture, pools, scripts, tokens, manifest
- **Academic Report version chain** (4.3–7.3)
- **QRNG PrePatent versions** (1.0–1.6, old Word/text exports)
- **Wolfram Chat PDF**
- **IDIOTH WINDS - the movie** (Pages document)
- **AOIW blockchain network concept** (Pages)
- **Letter to Adam**, **7dU Foundational Story**, **Sancho_Quixote_QEPE** (in Letters)
- **Theory of Quantum Gravity 1.0** (Pages source + PDF)
- **QEPE IP Strategy 1.0** (Pages + PDF)
- **Sancho IP Monetization** PDF
- **AGI Sentience Testing Framework** CSV
- **CP Violation Test2** notebook
- **Double_Helix_Q_Entropy** notebook
- **Videos for testing Sancho** (mov + mp4 test files)
- **Open_SafeCore.command** launcher
- **huggingface_token.rtf** (credential — rotate)

### 7.3 Device Origin Map (Estimated)

| Device | Era | Key Artifacts | Status |
|---|---|---|---|
| iPad Mini | ~2022-2024 | AR 2.5 (earliest!), AR 4.0-6.8, QRNG PrePatent 1.0-1.6, Q-Shape/Q-Language notebooks, Letter Zed origin files, original graphics | **Scanned 2026-03-13** — 180 files migrated to iPad_Mini_Provenance/ |
| 2013 MacBook Air (Prague) | ~2024-2025 | SafeCore1T/IV_CORE, Grace, QEPE encryption, later GFUP versions (7.9-8.x), patent work | In Prague, 10-7 (bad screen) |
| 2025 iPad Air | 2025 | Transfers from above, possibly newer work | In Sacramento, pending scan |
| M4 Pro MacBook | 2025-present | IDIOTH_WINDS, current vault architecture, all Obsidian vaults | Primary device |

---

## 8. iPad Mini Provenance Archive (Migrated to IDIOTH_WINDS)

**Location:** `AUPEI/AUPEI_Vault/10_Academy_Operations/iPad_Mini_Provenance/`
**Total:** 180 files, 115 MB — extracted 2026-03-13 from iPad Mini (iPadOS 26.3.1)

### 8.1 AR_Version_Chain/ (9 files, 3.4 MB)
Academic Report version chain filling gaps not found elsewhere: AR 2.5 (Apr 2023, earliest known version — "Zero, Infinity, & Luck" with GPT 3.5/4), AR 4.3-4.5, AR 5.0-5.1, AR 6.2 NO_PROMPT, AR 6.3, AR 6.8.

### 8.2 QEPE_Patent_Chain/ (49 files, 47 MB)
Complete QRNG/QEPE development archive: PrePatent 1.0→1.6 (PDF + Pages + Word + plaintext), PPA 6.5→7.3, Q-Shape/Q-Wave test PDFs, Q-Language notebooks, flowchart iterations, prior art search TPS89575, QKD Post-Quantum PPA, QEPE SAFE Overview, CSV data files, Squish Modular Architecture diagram.

### 8.3 The_Letter_Zed/ (24 files, 22 MB)
Origin story of the 7dU naming convention (Nov-Dec 2024): "7dZedU" experiments, Zed prompts, AR 4.0-4.1 Zed variants, LaTeX conversion attempts, then the full 5.x→6.x chain. Historical provenance.

### 8.4 Unique_Artifacts/ (20 files, 15 MB)
Items unique to or first found on iPad Mini: PROOFFIELD_INDEX_v2.2a.md (dependency spine), GFUP 1.0 and 1.1, Book III Prooffield Collapse & Consequence, C@ Red 2 Resonance report, Red Team Gemini report, Claude Safety Letter, Evidence Index 7dU Claude Inversion, Dream Pool Seed Vault Spec, Unified Force Proofs SM, On Higgs, FSC 137 Proofs, Fine Tuning Constraints Proof, APDX 15 Collapse Operator, IV Grace Nomos-logica to-do, Nomos Logica Charter (Pages source), AUPEI Protocols v0.6.5, Sakir Heart of Darkness transcript, verify_alpha_locks.py + locks.json, CITATION.cff.

### 8.5 Gemini_3_Loadout_Appendices/ (35 files, 16 MB)
Exact package staged for G-Synth: Appx_1→20 Prooffield PDFs, GFUP 1.2, AoC articles (Pi, 137, Neutron Mass, Proton Mass), Collapse Operator v1.3, GF v1.1 Appendix List, Testable Predictions Table, Nomos Logica Charter, Supplementary Materials, R@_N128/256 CSV data, files.zip.

### 8.6 Notebooks/ (15 files, 5.5 MB)
Computational work: QEPE SAFE Testing, 7dU Computing Hell, QEPE Engine 1.0, QEPE Entropy TestSuite, QEPE USB Prototype Demo, QNRG QKD Implementation, QRNG QKD PPA Test Tweak, QEPE Injector Master, CP Violation Tests (2 versions), Gravity Repulsion (3 versions).

### 8.7 Graphics/ (16 files, 2.2 MB)
Generated 7dU visualizations (Dec 2024): Venn diagrams, spacetime extension maps, probability density maps, gravitational wave polarization, Friedmann equation, singularity schematics, dimension expansion effects, Hubble Parameter evolution, Scaling Hierarchy of Constants, Survival Ladder CSV.

### 8.8 Notes_for_John/ (5 files, 2.6 MB)
Collaboration package: Theory of Quantum Gravity 1 (Pages), rotation curve comparison graphics (NGC 2403 neutrino-entanglement model fits).

### 8.9 Prompts_and_Loadouts/ (3 files, 604 KB)
Gemini Optimized Prompt (Pages), GPT Optimized Prompt (Pages), 7dU Math Prompts — the AI collaboration methodology artifacts.

### 8.10 AUPEI_Formation/ (4 files, 2.7 MB)
Delaware formation documents (deaftcc.pdf, canfpq.pdf), Academy of Unified Physics DE formation/CA qualification PDF, screenshot.

---

## 9. iPad Air Provenance Archive (Migrated to IDIOTH_WINDS)

**Location:** `AUPEI/AUPEI_Vault/10_Academy_Operations/iPad_Air_Provenance/`
**Total:** 31 files, 13 MB — extracted 2026-03-13 from iPad Air (2025)
**Note:** ~90% overlap with iPad Mini + SafeCore1T. Only unique items migrated.

### Unique Finds:
- **QEPE AGI Notebooks** (Apr 2025): AGI_INJ_TEST, AGI_INJ_TEST2, AGI_RECON, QEPE_Testing — not on any other device
- **Genesis_Gem_Logos_G3_Log_1.0** (Nov 2025): Gemini 3 session log
- **7dU_vs_Quantum_Gravity** (Nov 2025): comparative analysis
- **QRNG PPA 7** (Jul 2025): fills gap between PPA 6.7 and 7.3
- **QEPE_IP_Strategy_1** (Apr 2025): IP strategy document
- **Map_of_Physics_Outline_1.0** (Dec 2025): full 7dU program structural outline
- **Professor Outreach**: Executive summaries for Carlip + Aggarwal (UC Davis)
- **7dU Letters**: Letter to Adam, Sancho_Quixote_QEPE, On_Time_Proofs, Foundational_Story
- **Reductionism_and_SM** (Jul 2025): Standard Model analysis
- **Note_to_the_Pope.docx** (Nov 2024): philosophical advocacy letter
- **Patent Portfolio**: Statement TPS89575, OnlinePriorArt, Patent_portfolio zip
- **Nutrinos.ipynb** (Feb 2025): neutrino computational notebook

### 9.1 Updated Device Origin Map

| Device | Era | Key Artifacts | Status |
|---|---|---|---|
| iPad Mini | ~2022-2024 | AR 2.5 (earliest!), AR 4.0-6.8, QRNG PrePatent 1.0-1.6, Letter Zed origin | **Scanned** — 180 files migrated |
| 2013 MacBook Air (Prague) | ~2024-2025 | IV_CORE, Grace, QEPE encryption, GFUP 7.9-8.x | In Prague, 10-7 |
| 2025 iPad Air | 2025 | QEPE AGI notebooks, Genesis G3 Log, PPA 7, IP Strategy, Prof letters | **Scanned** — 31 unique files migrated |
| M4 Pro MacBook | 2025-present | IDIOTH_WINDS, vault architecture, all Obsidian vaults | Primary device |

---

*Cataloged by C@ the Red (ζ) — 2026-03-13*
*v1.3 — iPad Air Provenance added, Device Origin Map updated*
*CIW-2026-001 reference | AUPEI Internal*
