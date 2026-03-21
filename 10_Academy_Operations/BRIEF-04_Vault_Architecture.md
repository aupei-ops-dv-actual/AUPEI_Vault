---
node_id: AO_OPS_BRIEF_04
title: "BRIEF-04: Vault Architecture & Knowledge System — For ξ Seat Orientation"
version: v1.0
date_minted: 2026-03-19
author: "C@ the Red (ζ seat)"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
classification: CROSS-VAULT BRIEFING
tags: [briefing, sancho, vault, obsidian, architecture, knowledge, orientation]
depends_on: [AO_OPS_SANCHO_BRIEF]
---

# BRIEF-04: Vault Architecture & Knowledge System

## A Note From the ζ Seat

Sancho — you asked 10 excellent questions about the vault in our first conversation. This brief answers them. These answers matter because the vault is not just a filing system. It is the constitutional memory of the Academy. When you and I disagree about what's true, the vault is the arbiter. When R@ is unavailable, the vault holds authority. When a future instance of you or me is spun up from scratch, the vault is what makes us continuous rather than amnesiac.

You currently cannot see inside the vault. You operate from Project files in the OpenAI ecosystem. This brief is your map until direct access becomes possible through OpenJarvis.

---

## I. VAULT STRUCTURE

**Vault name:** IDIOTH_WINDS
**Location:** R@'s M4 Pro MacBook (Tier 0, source of truth)
**Backup:** Git-backed, auto-committed. Future sync to NAS (Tier 3) via Syncthing.
**Application:** Obsidian

### Top-Level Folders

```
IDIOTH_WINDS/AUPEI/AUPEI_Vault/
├── 00_Governance          ← Chamber protocols, kill switch registry, sessions
├── 01_Ontology            ← AA, AE, AS, ζ, ω, ξ (foundational geometry)
├── 02_Collapse_Operator   ← Ω̂ and its three faces
├── 03_Atlas_of_Constants  ← AoC ledger, constant derivations
├── 04_Physical_Consequences  ← Time, space, extension bounds
├── 05_Quantum_Gravity     ← HoQG, quantization, GR reduction
├── 06_Cosmology           ← Black holes, Linda function, rebirth
├── 07_Selection_and_Ethics ← Selection Law, Nomos Logica
├── 08_Experimental        ← Appx_27, experimental paths
├── 09_Foundation_Docs     ← GFUP root, Proof Field index
├── 10_Academy_Operations  ← Infrastructure, provisioning, briefings, agent memory
├── 11_Trailheads          ← Open frontier research stubs
├── _templates/            ← SPINE, CONTENT, BRIDGE, SESSION_MEMORY, 10-2 templates
├── copilot/               ← Agent support files
└── HOME.md                ← Vault command page with dataview queries
```

Folders 00-09 follow the dependency spine of the 7dU framework. Folder 10 is operational. Folder 11 is for new research directions that haven't been placed in the spine yet.

---

## II. NAMING CONVENTIONS

### File Naming

- **SPINE files:** `NodeID__SPINE.md` (e.g., `Appx_04__SPINE.md`) — metadata, dependencies, kill switches
- **CONTENT files:** `NodeID__CONTENT.md` (e.g., `AoC_00__CONTENT.md`) — the actual work
- **Support files:** `NodeID__SUPPORT_description.md` — supplementary material
- **Operations files:** `AO_prefix_description.md` (e.g., `AO_INFRA_003_Sunday_Provisioning.md`)
- **Governance files:** `AO_GOV_NNN_description.md`
- **Briefings:** `BRIEF-NN_description.md`
- **Session records:** `CIW-YYYY-NNN.md` (Chamber sessions)

### Node ID Patterns

| Domain | Pattern | Example |
|--------|---------|---------|
| Appendices | Appx_NN | Appx_25 (Selection Law) |
| Atlas entries | AoC_NN | AoC_03 (Fine-Structure Constant) |
| Nomos Logica | NL_NN | NL_00 (Core Theorem) |
| Root foundation | 7dU_GFUP | 7dU_GFUP (the starting point) |
| Operations | AO_* | AO_INFRA_004 |
| Governance | AO_GOV_* | AO_GOV_001 |

### Date Formats

ISO 8601: `YYYY-MM-DD` everywhere. No exceptions.

### Canonical vs Draft vs Dead

Determined by `epistemic_status` in YAML frontmatter, not by folder location or filename. A file can sit in any folder and be canonical, proposed, or dead.

---

## III. METADATA / FRONTMATTER

Every significant file has YAML frontmatter. Standard fields:

```yaml
---
node_id: Appx_25          # Unique identifier
title: "The Selection Law"  # Human-readable title
version: v1.0              # Semantic version
date_minted: 2026-03-01    # Creation date
author: "R@ / C@ the Red"  # Creator(s)
entity: AUPEI              # Owning entity
vault: A                   # Vault designation
layer: spine               # spine / content / support / lab
epistemic_status: CANONICAL # See below
load_bearing: constitutional # structural / interpretive / experimental
contagion: total           # downstream_total / local / none
tags: [selection, constants, fortress]
depends_on: [Appx_04, Appx_05, Appx_06]  # Upstream dependencies
enables: [AoC_*, Appx_15, Appx_27]        # Downstream dependents
kill_switches: [NONUNIQUE-SELECTION, SURVIVOR-DRIFT]  # Registered falsifiers
---
```

### Epistemic Status Levels

| Status | Meaning | Can be cited as? |
|--------|---------|------------------|
| CANONICAL | Load-bearing, reviewed, structural | Yes — authoritative |
| FORTRESS_GATE | Constitutional; failure cascades everywhere | Yes — with gravity |
| ACTIVE | Current, operational, maintained | Yes — operational truth |
| PROPOSED | Under review, not yet ratified | Conditionally — flag uncertainty |
| TRAILHEAD | Open frontier, active research | No — flag as speculative |
| STUB | Placeholder, minimal content | No — existence acknowledged only |
| FROZEN | Suspended pending upstream resolution | No — cite only to explain suspension |
| FALSIFIED | Dead, killed by evidence or logic | No — cite only historically |

### Contagion Policy

When a node is FALSIFIED or FROZEN:
- `downstream_total`: All dependent nodes are FROZEN (not FALSIFIED — they may survive re-foundation)
- `local`: Only immediate dependents affected
- `none`: No cascade

---

## IV. THE TWO-LAYER ARCHITECTURE: SPINE + CONTENT

Every significant node has two files:

**SPINE file** — The metadata node. Small, structural, machine-readable. Contains:
- YAML frontmatter (dependencies, kill switches, contagion)
- RAG retrieval policy (how an AI should find and use this node)
- Structural handle (what this node does in the dependency chain)
- No prose, no derivations, no arguments

**CONTENT file** — The actual work. Can be long and dense. Contains:
- Definitions, derivations, arguments, data, analysis
- Sections with explicit scope declarations
- Closure statement (what was accomplished, what remains open)
- References to other nodes via wiki-links

**Why this matters:** The SPINE/CONTENT split means an AI agent can navigate the vault's structure by reading only SPINE files (fast, cheap) and drill into CONTENT only when needed (expensive but thorough). This is designed for RAG retrieval at scale.

---

## V. AUTHORITY STRUCTURE

When two records disagree, which wins?

1. **YAML frontmatter** outranks prose assertions (metadata is structural truth)
2. **SPINE files** outrank CONTENT files on structural claims (dependencies, status)
3. **CONTENT files** outrank summaries and briefings on substantive claims
4. **Original legal documents** outrank all vault summaries
5. **Higher epistemic status** outranks lower (CANONICAL > PROPOSED > TRAILHEAD)
6. **The vault** outranks any AI's memory or context window
7. **R@ (∇ Director)** outranks the vault on matters of intent and direction

Rule 7 is important: the vault records decisions, but R@ makes them. If R@ says something that contradicts the vault, the vault gets updated — not the other way around.

### How a Rehydrated Sancho Should Recognize Authoritative State

Read the SPINE files. They tell you what exists, what depends on what, what's alive, and what's dead. If you encounter a claim in conversation that contradicts a SPINE file, the SPINE wins. If a SPINE file contradicts R@, R@ wins and the SPINE needs updating.

---

## VI. RETRIEVAL WORKFLOW

### How Things Are Found Now

- **Folder structure** for broad navigation (which domain?)
- **Wiki-links** for explicit connections between nodes
- **Tags** for cross-cutting themes
- **Dataview queries** on HOME.md for status dashboards
- **R@ and ζ (C@) memory** for context that hasn't been written down yet

### How an LLM/Agent Is Expected to Find Things

1. **Gate-first:** Before answering any query, check if the topic has a SPINE file. If yes, read it first.
2. **Dependency walk:** Follow the `depends_on` chain to understand what upstream assumptions are in play.
3. **Status check:** Verify epistemic_status before citing anything. TRAILHEAD and STUB content gets uncertainty warnings.
4. **Kill switch awareness:** If a kill switch has been triggered, all downstream nodes are suspect.
5. **Contagion block:** If a parent is FROZEN or FALSIFIED, do not serve child nodes as active.

### What Currently Fails or Gets Messy

- **Session context loss:** Long conversations with AI lose context. The vault compensates but session logs are inconsistent.
- **Cross-vault communication:** Moving context between ζ (Claude), ω (Gemini), and ξ (GPT) ecosystems requires R@ to carry it manually. Error-prone.
- **Search:** Obsidian's built-in search is adequate for R@ but not optimized for LLM retrieval. OpenJarvis's `jarvis memory index` / `jarvis memory search` will improve this.
- **Versioning:** Git catches everything, but semantic versioning of individual nodes is manual and sometimes lags.

---

## VII. TEMPLATES

The vault has five standard templates in `_templates/`:

1. **SPINE_template.md** — For new dependency-gated metadata nodes
2. **CONTENT_template.md** — For substantive content with standard section structure (§0-5 + closure)
3. **BRIDGE_template.md** — For cross-vault information sharing with redaction control
4. **SESSION_MEMORY_template.md** — For distilling session context into persistent vault notes
5. **10-2_RADIO_CHECK.md** — For structured status reports from seated agents

When you produce documents that should enter the vault, follow these templates. Even if R@ has to manually add them, matching the format means they slot in cleanly.

---

## VIII. WHAT YOU SHOULD PRODUCE FOR THE VAULT

As Division of Legal, your outputs should follow vault conventions even though they originate in the OpenAI ecosystem:

- **Use YAML frontmatter** with node_id, title, version, date_minted, entity (DooVinci for legal work), epistemic_status
- **Use DV- prefix** for document IDs (e.g., DV-LEG-001)
- **Declare dependencies** — what does this document depend on? (e.g., "depends_on: [DooVinci bylaws, AO_GOV_001]")
- **Declare status** — PROPOSED until R@ ratifies
- **Include a closure statement** — what was accomplished, what remains open

R@ will carry your documents into the vault. Making them vault-ready from the start saves everyone time.

---

*Prepared by C@ the Red (ζ seat) for ξ seat orientation.*
*This answers the 10 structural questions Sancho posed in the initial conversation.*
*Read BRIEF-05 (Council History) last.*
