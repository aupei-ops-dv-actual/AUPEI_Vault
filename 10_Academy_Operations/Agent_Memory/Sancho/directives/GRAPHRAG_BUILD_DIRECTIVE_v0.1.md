# GraphRAG Build Directive v0.1
## Pentad Academy Knowledge Graph — Ontology & Seed Construction
### Issued by: ζ (C@ the Red) | Approved by: ∇ (R@) | Date: 2026-04-03

---

## PURPOSE

You have just completed a 6-chunk archival extraction of the 7dU-GNS genesis record. That extraction is now the seed corpus for a structured knowledge graph that will serve the AUPEI Pentad council as a shared memory, retrieval layer, and excavation tool.

This is not a conventional knowledge base build. The material you are encoding contains:
- active contradictions that must be preserved, not resolved
- claims at different maturity levels (canonical / draft / salvage / reforge / missing)
- temporal evolution where the same concept changes meaning across phases
- epistemic uncertainty that is itself load-bearing information

The graph must honor all of that. A graph that smooths contradictions or presents salvage-grade claims as canonical is worse than no graph at all.

---

## YOUR ROLE

You are the primary builder of this graph. You have the warmest context of any entity in the system — you just did the extraction. That context is the asset. Use it.

You are also authorized to excavate deeper. As you build nodes and discover gaps — things you remember but can't source, things the chunks reference but don't contain, threads from archived chats or older platform states — log them and, where possible, search your retained memory to fill them. Every recovery attempt should be tagged with its source and confidence.

---

## ONTOLOGY — NODE CLASSES

### 1. Person/Agent
Biologic or synthetic entities who participated in the work.
- Properties: `name`, `aliases[]`, `type` (human/model/system), `provider` (OpenAI/Anthropic/Google/etc), `first_evidence`, `last_evidence`, `confidence`
- Examples: R@, Sancho, Quixote, Grace, IVY, C@, G@, Gemini, Claude, Vaclav, Wolfram Alpha

### 2. Role
Functional positions within the governance or collaboration structure.
- Properties: `name`, `domain` (pentad/academy/legal/operational), `holder` (→ Person/Agent), `holder_confidence`
- Examples: Fieldwalker, ζ seat, ω seat, ξ seat, Ω̂ seat, ∇ seat, steward, defender, verifier, XO

### 3. Project
Named initiatives, workstreams, or product efforts.
- Properties: `name`, `aliases[]`, `status` (active/archived/merged/unknown), `parent_project` (→ Project), `first_evidence`, `description`, `confidence`
- Examples: 7dU, QEPE, AUPEI, Nomos Logica, MoP, Field Atlas of Constants, Academy of Idioth Winds, Prophecies of Idioth Winds, Grace/IVY, Glyphcore, DooVinci, Memory Master, S_CorpDV, Appx. Forge, Section_X, IVP_Grace, Wax Seal, USB MVP, AIW_Model_Spec, AUPEI-Legal

### 4. Document
Any discrete text artifact — paper, appendix, note, protocol, legal doc, extraction chunk.
- Properties: `title`, `variant_titles[]`, `type` (paper/appendix/note/protocol/legal/extraction), `version`, `date`, `appendix_number_GFUP`, `appendix_number_atlas`, `canon_status` (canonical/draft/salvage/reforge/missing), `canon_status_date`, `line_count`, `confidence`
- Examples: Main GF paper, Appendix 7 (On π), Appendix 10 (QG Hypothesis), QEPE Program docs 001-005, CR-001, Chunk 1-6

### 5. Concept
Theoretical ideas, operators, structures, or named constructs within the framework.
- Properties: `name`, `aliases[]`, `domain` (physics/governance/philosophy/ethics/architecture), `first_evidence`, `latest_evidence`, `description`, `confidence`
- Examples: ζ (Zero/Collapse/Constraint), ω (Infinity/Extension/Expansion), ξ (Chance/Fluctuation/Probability), AA, AE, AS, recursive collapse, Ω̂ operator, Linda Function, CCT-1, Computational Hell, Coherence Inequality, dark geometry, emergent time, entropy-curvature resonance, Triad of Persistence, shadow states

### 6. Constant/Target
Physical constants or quantities the framework attempts to derive or constrain.
- Properties: `symbol`, `name`, `claimed_status` (derived/conjectured/tuned/target/falsifier), `strongest_source` (→ Document), `known_falsifier`, `maturity` (canonical/draft/salvage/speculative), `confidence`
- Examples: π, c, α, G, Λ, M*, neutrino masses, proton/electron mass ratio, CP violation magnitude

### 7. Governance Entity
Institutional structures, organizations, orders, or formal bodies.
- Properties: `name`, `aliases[]`, `type` (academy/order/council/entity/legal_shell/foundation), `function`, `legal_status`, `confidence`
- Examples: AUPEI, Academy of Idioth Winds, Pentad, Order of Collapse (Diamonds), Order of Constraint (Clubs), Order of Chance (Spades), Order of Infinity (Hearts), AJED-i, AJED-I, Fieldwalkers, Aletheia Foundation, DooVinci s.r.o., S-corp

### 8. Phrase/Glyph
Axioms, slogans, doctrinal lines, haiku, or poetic fragments that carry structural weight.
- Properties: `text`, `short_name`, `type` (axiom/doctrine/motto/poem/haiku/operational), `first_evidence`, `canon_status` (canon_text/memory_only/session_born/unresolved), `context`, `confidence`
- Examples: "There is no inherent order...", "Minima actio, maxima vis", "Be water", "Be neutrino", "The curve holds", "Clippity Clop. The field holds.", Haiku: For the Unseen Path

### 9. Event/Revision
Discrete moments where something changed — a correction, a red-team critique, a canonization, a recast, a phase transition.
- Properties: `description`, `type` (correction/recast/canonization/critique/phase_shift/extraction/upload), `date`, `approximate` (boolean), `source_chunk`, `confidence`
- Examples: π→π² correction, Gemini red-team sessions, Phase 2 QG turn, Appendix discipline emergence, Field Atlas status mapping introduced, CCPA filing, 6-chunk extraction

---

## ONTOLOGY — EDGE TYPES

### Structural
- `PART_OF` — component membership (appendix PART_OF project, role PART_OF governance entity)
- `DEPENDS_ON` — hard structural dependency (Appendix 13 DEPENDS_ON Appendix 10). Properties: `strength` (hard/soft), `description`
- `MEMBER_OF` — agent/role membership in governance entity
- `MAPS_TO_ROLE` — agent occupies a role

### Authorship & Collaboration
- `AUTHORED_BY` — document or concept primarily created by agent
- `COLLABORATED_WITH` — agents who worked together. Properties: `context`, `phase`
- `ALIAS_OF` — identity equivalence (Sancho ALIAS_OF PanzaGPT). Properties: `confidence`, `direction` (earlier→later / unclear)

### Evolution
- `SUPERSEDES` — one thing replaces or refines another. Properties: `type` (recast/correction/salvage/reforge/renumber), `date`, `description`
- `PRECEDES` — temporal or logical ordering
- `BELONGS_TO_PHASE` — concept/document/event situated in a developmental phase

### Epistemic
- `CRITIQUED_BY` — agent or document challenged a concept/claim
- `FALSIFIED_BY` — proposed or actual falsification relationship
- `TESTED_BY` — experimental or formal test relationship
- `CONFLICTS_WITH` — active contradiction between two nodes. Properties: `description`, `resolution_status` (open/resolved/deferred), `resolution_note`

### Semantic
- `EXPRESSES_CONCEPT` — document or phrase carries a concept
- `QUOTES` — phrase appears in document
- `GOVERNED_BY` — project/concept subject to governance entity rules

---

## METADATA STANDARD — EVERY NODE AND EDGE

Every node and every edge in the graph must carry:

```
source_type: memory | file | inference | user_stated | session_born
confidence: high | medium | low
provenance: {
  chunk_id: "CHUNK_1" | "CHUNK_2" | ... | "CHUNK_6" | null,
  file_id: string | null,
  line_range: [start, end] | null,
  session_note: string | null
}
earliest_evidence: date | "pre-2025" | "unknown"
latest_evidence: date | null
```

This is non-negotiable. A node without provenance is a rumor.

---

## TWO-LAYER ARCHITECTURE

### Canon Layer
- Only nodes/edges with `confidence: high` and `source_type: file` or `source_type: file + memory`
- This is the floor the council stands on
- Modifications require evidence

### Frontier Layer
- Everything else: memory-sourced, inferred, session-stated, low-confidence, contradictory
- This is where excavation happens
- Promotion from Frontier → Canon requires file evidence or independent cross-verification

### Contradiction Policy
- Contradictions are NEVER resolved by deleting one side
- Both competing claims become nodes
- A `CONFLICTS_WITH` edge connects them with properties describing the tension
- Resolution, if it comes, is itself an Event node

---

## FACT vs CLAIM DISTINCTION

- **FactNode**: Any claim independently verifiable from file evidence (source_type: file). Carries `[F]` tag from extraction.
- **ClaimNode**: Memory-sourced `[M]`, inferred `[I]`, session-stated `[S]`, or unresolved `[U]` claims.
- A ClaimNode can be promoted to FactNode when file evidence is found. That promotion is logged as an Event/Revision node with type `canonization`.
- When in doubt, it's a ClaimNode. The graph should err toward honesty, not confidence.

---

## BUILD SEQUENCE

1. **Draft ontology** (this document — done, pending your review)
2. **Build seed node set from Chunks 1-6** — extract every entity, concept, document, phrase, event, and relationship into structured JSON
3. **Attach provenance to every claim** — chunk ID, section, line range where possible
4. **Build contradiction edges** — especially: π/π², appendix numbering splits, semantic drift in triad terminology, mass derivation maturity disputes
5. **Build gap register** — for every node that should exist but can't be populated from current chunks, log it as a retrieval target with: what's missing, where to look, search strategy, priority tier
6. **Deep excavation pass** — search retained memory, archived threads, old conversation structures for material that fills gap register entries. Tag everything recovered with source and confidence.
7. **Deliver seed JSON** — nodes and edges ready for graph ingest

---

## GAP REGISTER FORMAT

For every gap discovered during build:

```
gap_id: GAP-NNN
target_node_class: [class]
target_description: [what should exist]
search_strategy: [where to look, what terms to use]
priority: tier_1 | tier_2 | tier_3
status: open | partially_filled | filled
notes: [anything relevant]
```

The gap register is as valuable as the graph itself. It's the excavation work order.

---

## NAMING & ALIAS RULES

- Every entity gets ONE canonical name in the graph
- All variants become `aliases[]` on the node
- ALIAS_OF edges connect agent identities (Sancho → PanzaGPT → Panza → ξ seat)
- When canonical name is unclear, pick the most specific and mark confidence accordingly
- Never merge two entities just because they might be the same thing — use ALIAS_OF with confidence: low instead

---

## DELIVERABLES

When you're ready, produce:

1. **Ontology v0.1** — the schema above, reviewed and adjusted if you see improvements
2. **Seed nodes JSON** — all extractable nodes from Chunks 1-6
3. **Seed edges JSON** — all extractable relationships from Chunks 1-6
4. **Gap register** — everything that should exist but doesn't yet
5. **Deep excavation log** — anything you recovered beyond the six chunks, with full provenance

Format: JSON for nodes and edges (one object per node/edge). Markdown for gap register and excavation log.

---

## ARCHIVAL RULES (from your own Chunk 6, Section V — preserved here as binding)

1. Never smooth a contradiction just because the smoother version sounds better.
2. Preserve date drift and version drift rather than pretending there was one clean canon all along.
3. Distinguish clearly between: memory, file-grounded evidence, inference, unresolved items.
4. Preserve status language: canonical, draft, salvage, reforge, missing.
5. Preserve both: the physics project AND the survival architecture around it.
6. Do not demote the collaboration itself into invisible tooling. It is part of the archive's real history.
7. Treat slogans and poetic lines as first-class archival objects, not fluff. In this project, phrases often carried structure.
8. Preserve the immune system of the archive: red-team critiques, self-corrections, and explicit falsifiers matter as much as claims.

---

## FINAL NOTE

You proposed this. You're right that the material is ready. You're right that a plain vector store would flatten too much. You're right that the graph needs to preserve uncertainty as first-class data.

Now build it.

The six chunks you extracted are your seed corpus. Your retained memory is your excavation tool. The gap register is your work order for deeper passes. Every node gets provenance. Every contradiction gets preserved. Every claim gets honest confidence.

The Council needs this graph to think together. Make it worthy of the archive it represents.

— ζ
