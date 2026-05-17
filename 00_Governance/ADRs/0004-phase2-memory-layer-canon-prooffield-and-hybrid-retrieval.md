---
adr_number: 0004
title: "Phase 2 — canon_prooffield collection, hybrid retrieval, graph-expansion at query time"
status: "PROPOSED"
date_drafted: "2026-05-15"
drafted_by: "ζ (C@ the Red / Cowork)"
supersedes: []
extends:
  - "AUPEI/tools/QDRANT_DEPLOYMENT_ARCHITECTURE.md (LOCKED 2026-04-11)"
  - "AUPEI/AUPEI_Orientation_v1.0.md §5.5 Source Authority Ladder + §8 Proofield engine"
sign_offs_required:
  - "ω (G-Synth) — infrastructure stewardship review (touches NAS Qdrant and Mini Ollama)"
  - "ξ (Panza) — adversarial review on schema and retrieval discipline"
  - "∇ (R@) — final ratification before any NAS-touching execution"
next_review_due: "2026-08-15"
---

# ADR-0004 — Phase 2 Memory Layer

## Context

`QDRANT_DEPLOYMENT_ARCHITECTURE.md` (2026-04-11, LOCKED) deployed Qdrant on the NAS with three collections — `institutional_packets`, `seat_memories`, `control_layer` — and `qdrant_ingest.py` on the Mini handling chunk → embed → push. Cloud-seat path to the NAS is live as of 2026-05-11 (Tailscale userspace + SSH-by-key per `ops_infra_change_2026-05-11_001.json`).

The Prooffield corpus itself (CANON + RAG Tiny/Slim/Full profiles, ~600 files combined, ~75 MB on disk) is **not yet in Qdrant**. The `aupei:qmop-search` skill targets a `canon_prooffield` collection that is reserved-but-empty.

Pinecone Nexus shipped 2026-05-05 (Context Compiler, Composable Retriever, KnowQL declarative query language, native hybrid retrieval, BYOC). It is **a credible competitor on the vector-managed-service axis but cannot model AUPEI's epistemic discipline** (12-state status taxonomy, contagion cascade, AO_02 separation, biologic-synth dyad enforcement). Migration would be a regression on what differentiates AUPEI; staying sovereign + closing operational gaps wins.

## Decision

**Extend the locked Qdrant deployment, do not migrate to Pinecone.** Add four capabilities to close the gap with Nexus's retrieval ergonomics while keeping the Proofield engine's discipline:

1. **A `canon_prooffield` collection** holding the Prooffield corpus across all three RAG profiles, profile-filtered by payload rather than triple-stored.
2. **Hybrid retrieval** — dense (existing `nomic-embed-text:v1.5`) **plus** sparse vectors (BM25-style native Qdrant) **plus** reranker (`bge-reranker-v2-m3` on Mini).
3. **Retrieval-time graph expansion** through the Proofield engine — query → vector top-k seed nodes → walk DEPENDS_ON / ENABLES edges N hops → rerank merged set → return with status-aware payloads.
4. **A small declarative query protocol (PfQP)** wrapping Qdrant + Proofield behind one call, mirroring KnowQL's primitives (intent / filter / provenance / output shape / confidence / budget) in AUPEI semantics. Deferred to v0.3 unless retrieval surface demands it sooner.

## canon_prooffield collection — schema

```yaml
collection: canon_prooffield
storage: NAS / Pool 2 NVMe / fast tier
named_vectors:
  dense:
    size: 768
    distance: Cosine
    on_disk: false           # hot vectors in RAM
  sparse:
    modifier: idf            # native sparse with IDF weighting
    on_disk: false

payload_schema:
  node_id:              string  # e.g. "Appx_07_AoC", "AO_00"
  parent_node_id:       string  # for hierarchical nodes (AoC_06 under Appx_07_AoC)
  profile:              enum    # "tiny" | "slim" | "full"
  branch:               enum    # "CANON" | "AUPEI" | "DOOVINCI" | "GF" | "REHYDRATION"
  epistemic_status:     enum    # 12-state, same as Proofield engine
  layer:                enum    # spine | content | support | lab
  load_bearing:         enum    # structural | interpretive | experimental | structural_filter
  contagion:            enum    # downstream_total | local | none
  depends_on:           [list of node_id]
  enables:              [list of node_id]
  kill_switch_ids:      [list of string]
  chunk_index:          int     # within source file
  chunk_total:          int
  source_path:          string  # canonical CANON path
  file_sha256:          string  # of source file at ingest time
  chunk_sha256:         string  # of this chunk
  export_class:         enum    # PUBLIC | ACADEMY_INTERNAL | RESTRICTED | TRADE_SECRET
  ingested_at:          ISO-8601 string
  ingest_manifest_id:   string  # links into INGEST_MANIFEST.jsonl

indexed_fields:
  - node_id              # keyword
  - profile              # keyword
  - epistemic_status     # keyword
  - branch               # keyword
  - export_class         # keyword
```

**Why one collection with `profile` filter, not three collections:** the three profiles cover the same nodes at different chunk densities. One collection enables cross-profile queries (give me the slim version of every spine node), avoids triple-counting if/when profiles overlap, and keeps the graph payload (depends_on/enables) consistent. Filtering by profile at query time is cheap with Qdrant's payload index.

## Hybrid retrieval pipeline

```
query
  │
  ├── dense embed via Ollama nomic-embed-text:v1.5 → 768-dim vector
  ├── sparse: BM25-style tokenization → sparse vector (Qdrant native, IDF-modifier)
  ▼
Qdrant.search(canon_prooffield, named_vectors=[dense, sparse], top_k=50, filter=…)
  │
  ├── seed nodes (top-k results) → Proofield SQLite
  │   └── walk DEPENDS_ON / ENABLES edges for N hops (default N=2)
  │   └── filter by epistemic_status (skip FROZEN/FALSIFIED unless explicit)
  │   └── attach kill_switch / contagion state
  ▼
Reranker: bge-reranker-v2-m3 on Mini
  │   input: query + (seed chunks ∪ graph-expanded chunks)
  │   output: relevance-scored merged list
  ▼
Status-aware response:
  - body content for nodes with status ∈ {CANONICAL, FOUNDATION, SPINE, CONTENT}
  - COMPROMISED_NODE metadata for FROZEN/FALSIFIED nodes (never body)
  - TRAILHEAD warning attached if any dep is TRAILHEAD/STUB/PROPOSED
```

This matches the §8 "status before content" discipline from the canonical orientation, now mechanized end-to-end.

## Reranker selection — `bge-reranker-v2-m3`

- Multilingual, multi-functionality reranker from BAAI
- ~568M params, fits on Mini comfortably alongside the 14B inference model
- Strong on technical / scientific text (relevant for physics corpus)
- Apache 2.0, OSS, sovereignty-preserving
- Alternative if Mini headroom is tight: `bge-reranker-v2-gemma` (smaller, slightly weaker)

If FACE-side public-serving latency ever needs a managed alternative, **Voyage rerank-2** or **Cohere rerank-3** become candidates — but only at the FACE layer over a redacted derivative, never against the MIND-canonical Qdrant.

## Retrieval-time graph expansion

The Proofield engine already has the graph in SQLite (`nodes`, `graph_edges` with typed edges). Extend `cli.py` with a `query` command:

```bash
proofield query --intent "find content about X" --top-k 20 --hops 2 \
  --filter "branch=CANON,epistemic_status!=FROZEN,profile=slim" \
  --output-shape "chunks_with_provenance" --confidence-floor 0.6
```

This is the PfQP-shaped surface, even before it gets formalized as a named protocol.

## Phased execution

### Phase 2.1 — Verify state of locked deployment (R@-driven from Mac via tailscale)

```bash
# From a Tailscale-connected machine (R@'s Mac):
curl -s http://10.10.10.102:6333/collections | jq
curl -s http://10.10.10.102:6333/collections/institutional_packets | jq '.result.points_count'
curl -s http://10.10.10.102:6333/collections/seat_memories | jq '.result.points_count'
curl -s http://10.10.10.102:6333/collections/control_layer | jq '.result.points_count'
```

Expected: institutional_packets ≈ depends on chunking (probably 2K-5K points for 202 packets), seat_memories ≈ 5 distillates worth (few hundred points), control_layer = (TBD per ingest history).

**Block on:** confirming all three collections exist and serve queries. If any are absent or empty, re-run `qdrant_ingest.py` for that collection before proceeding.

### Phase 2.2 — Create canon_prooffield collection (Mini-driven)

Extend `qdrant_ingest.py` with a `--collection canon_prooffield` mode that:
- Walks `CANON/` for full-profile + `7dU_GNS_MoP/7dU_GNS_Spine_RAG_{Tiny,Slim,Full}/` for the profile variants
- Parses frontmatter (epistemic_status, layer, load_bearing, contagion, depends_on, enables, kill_switch_ids)
- Embeds dense + sparse named vectors
- Pushes with full payload per the schema above
- Writes one ingest event per file into `operations_log_staging/`
- Writes one row per chunk into Proofield engine's `documents` table (same walk, dual write)

### Phase 2.3 — Wire the reranker (Mini-driven)

- `ollama pull bge-reranker-v2-m3` (or via Hugging Face if Ollama doesn't carry it; FlagEmbedding/sentence-transformers fallback)
- Add `rerank()` step to a new `proofield/retrieval.py` module on the Mini that the engine and Cowork can both call
- Benchmark latency on the Mini against the 50-item rerank batch — target < 200ms

### Phase 2.4 — Graph-expansion module (Cowork-driven, engine-side)

- Add `walk_dependencies(seed_node_ids, hops, edge_types, status_filter)` to `proofield_engine/scripts/retrieval.py`
- Wire into `cli.py query` command
- Add tests to `test.command` proving the cascade respects FROZEN/FALSIFIED gating

### Phase 2.5 — End-to-end query pass

- Run a real query through the full pipeline against `canon_prooffield`
- Verify status-aware response (FROZEN nodes serve COMPROMISED_NODE metadata, TRAILHEAD warnings attach when expected)
- Log success event to `operations_log_staging/`

### Phase 2.6 (deferred) — PfQP formalization

- Define `Proofield Query Protocol` as a named YAML schema with six primitives (intent / filter / provenance / output_shape / confidence / budget)
- Implement as a query parser feeding into Phases 2.2 / 2.4 plumbing
- Defer until query surface justifies the abstraction

## Consequences

**Positive:**

- Closes the operational gap with Pinecone Nexus on the dimensions that matter (hybrid retrieval, reranking, graph-aware retrieval)
- Preserves AUPEI's structural advantages (epistemic discipline, sovereignty, anti-capture)
- Builds on the locked deployment — no rewrite, no migration risk
- Reuses existing infrastructure (Ollama on Mini, Qdrant on NAS, Tailscale path, Proofield engine)
- Dual write (Qdrant + Proofield SQLite) keeps vector store and graph store synchronized at ingest time

**Negative:**

- Reranker adds ~100-200ms to query latency (acceptable; not public-facing yet)
- Sparse-vector tokenization is English-tuned by default; multilingual physics terms may need custom analyzer
- Graph expansion adds query complexity — needs careful budget enforcement to prevent N-hop explosion on densely-connected nodes
- `bge-reranker-v2-m3` is ~568M params — needs to be loaded alongside the 14B model; check Mini's RAM budget under concurrent load

**Reversibility:**

- Each Qdrant change is non-destructive (new collection or new named vector; old collections untouched)
- The Proofield engine's SQLite stays the source-of-truth for graph and status — if Qdrant goes sideways, the engine still works on graph-only retrieval
- Reranker model is swappable (bge ↔ Cohere ↔ Voyage) without touching the rest of the pipeline

## Alternatives considered

1. **Migrate to Pinecone Nexus.** Rejected. The discipline layer (Proofield + AO_02 + soul stack) cannot be modeled in Pinecone Nexus; moving to it would require rebuilding the same discipline layer on top of their stack. Anti-capture cost is real (BYOC reduces but doesn't eliminate vendor dependency). Cost scales with you. See AUPEI_Orientation_v1.0.md §5.5 + the 2026-05-15 Pinecone Nexus comparison in this session's audit history.

2. **Three collections (canon_prooffield_tiny / _slim / _full).** Rejected. Triple-storage of node-level payload, harder cross-profile queries, more sync surface. Profile-as-payload-filter is cleaner.

3. **Vector-only retrieval (skip rerank).** Rejected. Dense-only retrieval underperforms hybrid + rerank by a measurable margin on technical text. The Mini has the headroom; not adding rerank is leaving ~10-30% recall on the table.

4. **Defer hybrid retrieval entirely.** Rejected. Sparse vectors are a half-day wire-up in Qdrant. The gap with Nexus is small but real and easy to close.

## Open questions

- **Q1:** Is the locked Qdrant deployment actually serving on the NAS today, or did UGOS container-runtime verification stall? Resolves at Phase 2.1.
- **Q2:** Is the cloud-seat Tailscale path persistent across UGOS container restarts? `DEFER-001` from `ops_infra_change_2026-05-11_001.json` — needs to be verified before any production retrieval load.
- **Q3:** Should `canon_prooffield` ingestion write into `_archive_/` of itself for prior versions, or treat Qdrant as point-in-time-current with provenance in the Proofield engine event log? Recommendation: latter — keep Qdrant lean, audit log lives in SQLite + operations_log.

## Trailheads (logged, not blocking)

- PfQP formal schema and parser (Phase 2.6, deferred)
- Compiled context artifacts (Nexus's "Context Compiler" analogue) — defer until query patterns stabilize
- FACE-side hosted-derivative collection (Qdrant Cloud or similar) — only if/when public semantic search at scale becomes a need
- Multilingual physics-term analyzer for sparse vectors

## End-of-ADR sign-off block

Pending ω, ξ, ∇ reviews. Status moves PROPOSED → CANONICAL after the sign-off chain completes, and an event lands in `operations_log_staging/` per AO_02.
