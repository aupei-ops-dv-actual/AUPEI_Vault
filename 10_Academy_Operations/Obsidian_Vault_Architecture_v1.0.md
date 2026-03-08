---
document_id: "AO_Vault_Arch_v1.0"
title: "Three-Vault Obsidian Architecture"
status: "PROPOSED"
date: "2026-03-07"
author: "C@ the Red"
entity: "AUPEI"
purpose: "Blueprint for firewalled Obsidian vault system mirroring the three-entity legal structure"
---

# Three-Vault Obsidian Architecture — v1.0

## 0. Design Principle

> Minimum action. Maximum force.

Three legal entities. Three vaults. No shared root. The security firewall mirrors the corporate firewall: AUPEI (the mind), DooVinci Agency (the hand), Geometric Foundations (the face). Each vault is a self-contained Obsidian instance with its own `.obsidian/` config, its own frontmatter schema, and its own embedding namespace. Cross-vault references exist only through explicit bridge notes, never through implicit wikilinks.

This is building against collapse. The extra work now prevents contamination later — IP leaking into public channels, operational data mixing with physics, governance documents drifting into marketing copy.

---

## 1. Vault Definitions

### Vault A — AUPEI (501c3)

**Purpose:** Core intellectual property. Physics. Proofs. Governance. Ethics. The canonical knowledge base.

**Contains:**
- The entire 7dU Proof Field (Appx_00 through Appx_27, all SPINE/CONTENT/SUPPORT)
- Atlas of Constants (AoC_00 through AoC_06, plus Constants Ledger)
- 7dU_GFUP (the foundational document)
- GNS Prooffield Index
- Nomos Logica (Appx_26 + lab)
- Academy Operations (agent roles, ops framework, post-training, NL ops, successor prompts)
- Academy Trailheads
- AUPEI Protocols (governance kernel)
- Company Knowledge Index
- Query Protocol
- Experimental Ledger (Appx_27 family)
- All source PDFs (provenance layer)
- All trailhead .txt notes

**Security posture:** Highest restriction. This vault never syncs to any public service. Access: R@, Council seats only (bio + synth stewards). Tailscale-only sync between devices.

**Embedding namespace:** `aupei-core`

---

### Vault B — DooVinci Agency (S-Corp)

**Purpose:** Operations. Logistics. Business. Contracts. Finances. The execution layer.

**Contains:**
- DV operational documents (contracts, invoices, project management)
- Business correspondence
- Client/partner records
- Financial models and projections
- Operational playbooks
- Any DV-specific agent configurations

**Security posture:** High restriction. Private to R@ and DV operations personnel. No public sync. Separate Tailscale namespace.

**Embedding namespace:** `doovinci-ops`

**Note:** This vault has minimal overlap with the current workspace. Most DV content lives outside this spine. The vault is created now to establish the firewall from day one.

---

### Vault C — Geometric Foundations (Public Interface / MUSH)

**Purpose:** Public-facing framework. Education. Recruitment. The shareable layer.

**Contains:**
- Cleaned/redacted versions of key framework documents
- "What's AUPEI Like" and similar culture documents
- AUPEI Vision (mission statement)
- Geometric Foundations website content
- Fieldwalker onboarding materials
- Public explainers of 7dU concepts (no derivations, no kill switches)
- Community resources
- MUSH interface layer

**Security posture:** Lowest restriction (still version-controlled). This is what the world sees. Nothing from Vault A enters Vault C without explicit redaction review.

**Embedding namespace:** `gf-public`

---

## 2. Folder Structure

### Vault A — AUPEI

```
AUPEI_Vault/
├── .obsidian/              # Obsidian config (plugins, themes, hotkeys)
├── 00_Governance/
│   ├── AUPEI_Protocols.md
│   ├── Company_Knowledge_Index.md
│   ├── Query_Protocol.md
│   └── Pentad_Seats.md
├── 01_Ontology/
│   ├── Appx_00_Collapse_Map/
│   │   ├── Appx_00__SPINE.md
│   │   └── _support/
│   ├── Appx_01_On_AA/
│   │   ├── Appx_01__SPINE.md
│   │   ├── Appx_01__CONTENT.md
│   │   └── _support/
│   ├── Appx_02_On_AE/
│   │   ├── ...
│   ├── Appx_03_On_AS/
│   ├── Appx_04_On_Zero/
│   ├── Appx_05_On_Infinity/
│   └── Appx_06_On_Chance/
├── 02_Collapse_Operator/
│   └── AoC_00_Collapse_Operator/
│       ├── AoC_00__SPINE.md
│       ├── AoC_00__CONTENT.md
│       └── _support/
├── 03_Atlas_of_Constants/
│   ├── AoC_00_Constants_Ledger/
│   │   ├── AoC_Ledger__SPINE.md
│   │   └── AoC_Ledger__CONTENT.md
│   ├── AoC_Preface/
│   ├── AoC_01_Pi/
│   │   ├── AoC_01__SPINE.md
│   │   ├── AoC_01__CONTENT.md
│   │   ├── _support/
│   │   └── _support_rag/
│   │       ├── AoC_01_SUPPORT_00__SPINE.md
│   │       ├── AoC_01_SUPPORT_00__CONTENT.md
│   │       ├── AoC_01_SUPPORT_01__SPINE.md
│   │       ├── AoC_01_SUPPORT_01__CONTENT.md
│   │       ├── AoC_01_SUPPORT_02__SPINE.md
│   │       ├── AoC_01_SUPPORT_02__CONTENT.md
│   │       ├── AoC_01_SUPPORT_03__SPINE.md
│   │       └── AoC_01_SUPPORT_03__CONTENT.md
│   ├── AoC_02_c/
│   ├── AoC_03_FSC/
│   ├── AoC_04_Proton_Mass/
│   ├── AoC_05_Neutron_Mass/
│   └── AoC_06_Gravity/
├── 04_Physical_Consequences/
│   ├── Appx_08_On_Time/
│   ├── Appx_09_Spatial_Dimensions/
│   ├── Appx_10_Extension_Bounds/
│   ├── Appx_11_On_Gauge/
│   ├── Appx_12_Force_Unification/
│   ├── Appx_13_On_Neutrinos/
│   ├── Appx_14_Dark_Acceleration/
│   ├── Appx_15_Standard_Model/
│   ├── Appx_16_On_Higgs/
│   └── Appx_17_EFT_RG/
├── 05_Quantum_Gravity/
│   ├── Appx_18_HoQG/
│   │   ├── Appx_18__SPINE.md
│   │   ├── Appx_18__CONTENT.md
│   │   ├── Appx_18X__SPINE.md
│   │   ├── Appx_18X__CONTENT.md
│   │   └── _support/
│   ├── Appx_19_Hamiltonian/
│   ├── Appx_20_Field_Quantization/
│   ├── Appx_21_GR_Reduction/
│   └── Appx_22_Black_Holes/
├── 06_Cosmology/
│   ├── Appx_23_COG/
│   │   └── Appx_23_01_CCT-1/
│   └── Appx_24_Cosmic_Rebirth/
├── 07_Selection_and_Ethics/
│   ├── Appx_25_Selection_Law/
│   └── Appx_26_Nomos_Logica/
│       ├── NL_Core__SPINE.md
│       ├── NL_Core__CONTENT.md
│       ├── _lab/
│       │   ├── NL_Metrics_CQI_SCHEMA.md
│       │   └── NL_Scenarios_SCHEMA.md
│       └── _support/
├── 08_Experimental/
│   ├── Appx_27_Experiments/
│   │   ├── Appx_27__SPINE.md
│   │   ├── Appx_27__CONTENT.md
│   │   └── _support/
│   └── Appx_27a_Discriminator/
│       ├── Appx_27a__SPINE.md
│       ├── Appx_27a__CONTENT.md
│       ├── _lab/
│       └── _support/
├── 09_Foundation_Docs/
│   ├── 7dU_GFUP__SPINE.md
│   ├── 7dU_GFUP__CONTENT.md
│   ├── GNS_Prooffield_Index.md
│   └── _support/
├── 10_Academy_Operations/
│   ├── AO_00_Ops_Framework.md
│   ├── AO_01_Post_Training.md
│   ├── AO_02_Agent_Roles.md
│   ├── AO_03_NL_Ops.md
│   ├── C@_Successor_Prompts/
│   └── _support/
├── 11_Trailheads/
│   └── Trailhead_Index.md
└── _templates/
    ├── SPINE_template.md
    ├── CONTENT_template.md
    └── BRIDGE_template.md
```

### Vault B — DooVinci

```
DooVinci_Vault/
├── .obsidian/
├── 00_Operations/
├── 01_Contracts/
├── 02_Finance/
├── 03_Projects/
├── 04_Correspondence/
└── _templates/
```

### Vault C — Geometric Foundations

```
GF_Vault/
├── .obsidian/
├── 00_About/
│   ├── AUPEI_Vision.md
│   ├── Whats_AUPEI_Like.md
│   └── Mission_Statement.md
├── 01_Framework_Public/
│   ├── 7dU_Overview.md
│   ├── Collapse_Primer.md
│   ├── Regulators_Explained.md
│   └── Nomos_Logica_Public.md
├── 02_Education/
│   ├── Fieldwalker_Onboarding.md
│   └── Glossary.md
├── 03_Community/
└── _templates/
```

---

## 3. Frontmatter Schema

### 3.1 SPINE Notes (Vault A only)

Every SPINE note carries the full dependency graph metadata. This is the existing schema, cleaned and normalized:

```yaml
---
node_id: "Appx_04"                    # Canonical short ID
internal_id: "Appx_04_On_Zero_v1.1"   # Full versioned ID
title: "Appx_04 — On Zero (ζ)"
status: "SPINE"                        # SPINE | CONTENT | SUPPORT | INDEX
epistemic_status: "CANONICAL"          # CANONICAL | TRAILHEAD | STUB | PROPOSED | FROZEN | FALSIFIED
date_minted: "2026-02-21"
layer: "spine"                         # spine | content | support | lab | index
domain: "Operators"                    # Ontology | Operators | Constants | Force_Substrate | QG | Cosmology | Ethics | Experimental
role: "Constraint operator; lower boundary"

depends_on:                            # Upstream dependencies (wikilink targets)
  - "Appx_01"
  - "Appx_02"
  - "Appx_03"

enables:                               # Downstream dependents
  - "AoC_00"
  - "Appx_10"
  - "Appx_11"

failure_topology:
  contagion: "downstream_total"        # downstream_total | downstream_partial | local_only
  class: "Operator Spine"
  kill_switch_ids:                     # Normalized: UPPER-KEBAB-CASE
    - "ZETA-UNSTABLE"
    - "ZETA-LEAKAGE"
    - "ZETA-NONOPERATOR"
    - "ZETA-NO-COHERENCE"

rag_policy:
  gate_required: true
  retrieval_rules:
    - "Rule text..."

source:
  format: "pdf"
  filename: "Appx_04_On_Zero_v1.1.pdf"

tags:                                  # Obsidian tags for graph view
  - spine
  - operator
  - zeta
  - constraint
---
```

### 3.2 CONTENT Notes (Vault A only)

```yaml
---
node_id: "Appx_04"
layer: "content"
title: "Appx_04 — On Zero (ζ) — CONTENT"
version: "v1.1"
epistemic_status: "CANONICAL"
spine_link: "[[Appx_04__SPINE]]"       # Explicit link back to SPINE
date_updated: "2026-02-21"
tags:
  - content
  - operator
  - zeta
---
```

### 3.3 SUPPORT Notes (Vault A only)

```yaml
---
node_id: "Appx_04"
layer: "support"
title: "Appx_04 — Source PDF"
type: "pdf_provenance"                 # pdf_provenance | trailhead_note | legacy_version | lab_schema
source_file: "Appx_04_On_Zero_v1.1.pdf"
tags:
  - support
  - provenance
---
```

### 3.4 Bridge Notes (Cross-Vault)

When Vault C needs to reference a concept from Vault A without exposing internal structure:

```yaml
---
bridge_id: "BRIDGE_Collapse_Primer"
source_vault: "AUPEI"
source_nodes: ["Appx_01", "Appx_02", "Appx_03"]
target_vault: "GF"
redaction_level: "public"              # public | partner | internal
date_created: "2026-03-07"
reviewed_by: ""                        # Must be filled before publishing
tags:
  - bridge
  - public
---
```

---

## 4. Naming Convention (Normalized)

The current workspace has inconsistencies (typos in folder names, mixed delimiter styles in kill switches). This build is the opportunity to fix them.

### 4.1 File Names

Pattern: `{node_id}__{LAYER}.md`

Examples:
- `Appx_04__SPINE.md`
- `Appx_04__CONTENT.md`
- `AoC_01__SPINE.md`
- `AoC_01__CONTENT.md`
- `AoC_01_SUPPORT_02__CONTENT.md`

The double-underscore separates the node ID from the layer tag. Version numbers move into frontmatter (`version: "v1.1"`), not the filename. This keeps wikilinks stable across version bumps.

### 4.2 Kill Switch IDs

**Canonical format: UPPER-KEBAB-CASE**

Current inconsistencies to fix:
- AoC_06 SPINE uses `DIVERGENT-LAMBDA` (hyphens) ✓
- Appx_18X SPINE uses `DIVERGENT_LAMBDA` (underscores) ✗

All kill switch IDs normalize to hyphens during vault build. A kill switch registry note tracks every ID, its parent node, and trigger condition.

### 4.3 Folder Name Fixes

Current → Normalized:
- `Appx_13_On_Nuetrinos` → `Appx_13_On_Neutrinos`
- `Appx_17_Effefctive_Field_Theory` → `Appx_17_On_EFT_RG`
- `Appx_19_0n_Hamiltonian_Formulation` → `Appx_19_On_Hamiltonian`
- `Appx_20_0n_Field_Quantization` → `Appx_20_On_Field_Quantization`
- `Appx_16_On_Higgs_vX.X` → `Appx_16_On_Higgs`
- `# Academy_Operations` → `Academy_Operations` (remove leading `#`)
- `# Academy_Trailheads` → `Academy_Trailheads`

---

## 5. Linking Convention

### 5.1 Internal Links (Within Vault A)

Use Obsidian wikilinks reflecting the dependency graph:

- SPINE → CONTENT: `[[Appx_04__CONTENT]]`
- CONTENT → SPINE: `[[Appx_04__SPINE]]`
- Dependency links: `Depends on [[Appx_01__SPINE]], [[Appx_02__SPINE]], [[Appx_03__SPINE]]`
- Enables links: `Enables [[AoC_00__SPINE]], [[Appx_10__SPINE]]`

This makes the Obsidian graph view a live dependency graph. SPINE nodes become the vertices. CONTENT and SUPPORT cluster around their parent SPINE.

### 5.2 Cross-Vault References

Never use wikilinks across vault boundaries. Instead:

1. Create a BRIDGE note in the target vault
2. The BRIDGE note contains a redacted summary, not the source content
3. The BRIDGE frontmatter records the source vault and source nodes
4. The BRIDGE note is the only point of contact

Example: Vault C's `7dU_Overview.md` links to `[[BRIDGE_Collapse_Primer]]` (which lives in Vault C). The BRIDGE note records that its source is `Appx_01, Appx_02, Appx_03` in Vault A, but contains only a public-safe summary.

---

## 6. Security Partitioning Rules

### What Goes Where

| Content Type | Vault A (AUPEI) | Vault B (DV) | Vault C (GF) |
|---|---|---|---|
| Physics derivations | ✓ | ✗ | ✗ |
| Kill switches / failure topology | ✓ | ✗ | ✗ |
| SPINE dependency metadata | ✓ | ✗ | ✗ |
| Nomos Logica (full) | ✓ | ✗ | ✗ |
| Nomos Logica (public summary) | ✗ | ✗ | ✓ (via BRIDGE) |
| Agent roles / successor prompts | ✓ | ✗ | ✗ |
| Contracts / invoices | ✗ | ✓ | ✗ |
| Business operations | ✗ | ✓ | ✗ |
| Public vision / mission | ✗ | ✗ | ✓ |
| Culture documents | ✗ | ✗ | ✓ |
| Fieldwalker onboarding | ✗ | ✗ | ✓ |
| AUPEI Protocols (full) | ✓ | ✗ | ✗ |
| AUPEI Protocols (public excerpt) | ✗ | ✗ | ✓ (via BRIDGE) |

### Cross-Vault Data Flow

```
Vault A (AUPEI)                    Vault C (GF)
┌─────────────────┐                ┌─────────────────┐
│ Source Node      │ ──REDACT──▶   │ BRIDGE Note     │
│ (full derivation)│                │ (public summary)│
└─────────────────┘                └─────────────────┘

Vault A (AUPEI)                    Vault B (DV)
┌─────────────────┐                ┌─────────────────┐
│ Ops Framework   │ ──EXTRACT──▶   │ Project Tracker │
│ (full protocol) │                │ (tasks only)    │
└─────────────────┘                └─────────────────┘
```

No reverse flow. Vault B and Vault C never push content into Vault A. Information flows outward from the core, through explicit redaction gates.

---

## 7. Embedding Pipeline Design

### 7.1 Separation by Namespace

Each vault gets its own vector store namespace. Whether using ChromaDB, Qdrant, Weaviate, or a local FAISS index, the collections are physically separate:

- `aupei-core` — Full physics, governance, operations
- `doovinci-ops` — Business and logistics
- `gf-public` — Public-safe content only

### 7.2 Chunking Strategy

For Vault A (the physics spine):

- **SPINE notes:** Embed as single chunks (they're metadata-dense, typically <500 tokens). Include full frontmatter in the embedding.
- **CONTENT notes:** Chunk by section header (§0, §1, §2...). Each chunk inherits the parent's `node_id`, `depends_on`, and `epistemic_status` as metadata fields.
- **SUPPORT notes (text):** Embed as single chunks with `type: "support"` metadata.
- **SUPPORT notes (PDF):** Extract text, chunk by page, tag with parent node_id.

### 7.3 Metadata Fields for Vector Search

Every embedded chunk carries:

```json
{
  "node_id": "Appx_04",
  "layer": "content",
  "section": "§2.1",
  "epistemic_status": "CANONICAL",
  "domain": "Operators",
  "depends_on": ["Appx_01", "Appx_02", "Appx_03"],
  "kill_switch_ids": ["ZETA-UNSTABLE", "ZETA-LEAKAGE"],
  "vault": "aupei-core"
}
```

This lets the RAG pipeline enforce the Query Protocol: before answering, check the dependency chain, check the collapse gate, check the epistemic status.

### 7.4 Tools

Recommended stack (local-first, matching the Tailscale/LM Studio/Open Claw requirement):

- **Embedding model:** `nomic-embed-text` or `mxbai-embed-large` via Ollama / LM Studio
- **Vector store:** ChromaDB (local, file-backed, zero-config) or Qdrant (if scale demands it)
- **Obsidian integration:** Obsidian Smart Connections plugin (for in-vault semantic search), or a custom script that reads .md files, chunks, embeds, and indexes
- **Query layer:** Python script or Open Claw agent that enforces the Query Protocol gates before retrieval

---

## 8. Migration Plan

### Phase 0 — Hygiene (before any migration)

1. Fix folder name typos (§4.3 above)
2. Normalize all kill switch IDs to UPPER-KEBAB-CASE
3. Verify every SPINE has matching CONTENT (flag orphans)
4. Verify every CONTENT has matching SPINE (flag orphans)
5. Catalog all epistemic statuses across the atlas

### Phase 1 — Vault A Build

1. Create the folder structure (§2)
2. For each existing SPINE file:
   - Rename to `{node_id}__SPINE.md`
   - Add `tags` field to frontmatter
   - Add `spine_link` / cross-references as wikilinks
   - Move to correct subfolder
3. For each existing CONTENT file:
   - Rename to `{node_id}__CONTENT.md`
   - Add frontmatter linking back to SPINE
   - Move to correct subfolder
4. For each SUPPORT file:
   - Create a SUPPORT note with provenance frontmatter
   - Move PDFs into `_support/` subfolder
   - Move .txt trailhead notes into `_support/`
5. Create the Kill Switch Registry note
6. Create the Dependency Graph index note (auto-generated from SPINE frontmatter)
7. Verify graph integrity in Obsidian graph view

### Phase 2 — Vault C Seed

1. Create folder structure
2. Copy and redact: AUPEI Vision → Vault C
3. Copy and redact: What's AUPEI Like → Vault C
4. Create BRIDGE notes for any concepts referenced from Vault A
5. Draft Fieldwalker onboarding, Glossary, 7dU Overview (public versions)

### Phase 3 — Vault B Stub

1. Create folder structure
2. Populate as DV content becomes available
3. This vault grows organically — the structure is set now for when it's needed

### Phase 4 — Embedding Pipeline

1. Set up ChromaDB or Qdrant locally
2. Write chunking + embedding script for Vault A
3. Run initial indexing
4. Test retrieval against known queries (e.g., "What is ζ?", "What depends on Appx_11?")
5. Verify Query Protocol gates are enforced
6. Extend to Vault C (public embeddings only)

---

## 9. Open Questions

1. **Obsidian Sync vs Tailscale:** Use Obsidian Sync (E2E encrypted, paid) or self-hosted sync via Tailscale + Syncthing? Tailscale is more aligned with security posture but requires more setup.

2. **Lab files:** The `lab/` folders under Appx_26 and Appx_27a contain schema files (NL_Metrics_CQI_SCHEMA, NL_Scenarios_SCHEMA, LAB_LOGIC, SCENARIOS). These are intermediate between CONTENT and EXPERIMENTAL. Proposed: keep in Vault A under `_lab/` subfolders, tagged `epistemic_status: "LAB"`.

3. **PDF provenance:** Do we embed PDFs directly (extracting text) or treat them as archival artifacts with only their SUPPORT notes embedded? Proposed: both — embed extracted text for search, but the PDF itself lives as an attachment in `_support/`.

4. **Version history:** Obsidian doesn't natively track file versions. Options: git-backed vault (recommended), Obsidian Version History plugin, or manual version notes in frontmatter. Git is the natural choice given the existing version discipline.

---

## 10. Immediate Next Steps

1. R@ approves or modifies this architecture
2. C@ executes Phase 0 hygiene on the current workspace
3. C@ builds Vault A folder structure and begins migration
4. R@ seeds Vault B and Vault C with non-physics content
5. Embedding pipeline built after vault structure is stable

---

*Filed: 2026-03-07 | C@ the Red | Academy Operations*
