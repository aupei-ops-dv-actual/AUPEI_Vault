# 00_Operating_Framework.md
# AUPEI / 7dU GraphRAG — Operating Framework (Quarantine-First)

## 1) Taxonomy & Epistemic Gates

### A. `epistemic_status` (Truth / Authority)
- **CANONICAL**: Authoritative. May be used as foundation for downstream derivation.
- **FOUNDATION**: Same authority class as CANONICAL, reserved for core papers (e.g., GFUP).
- **SPINE**: Structural metadata authority for a node (dependencies, gates, kill-switches).
- **CONTENT**: Canonical retrieval text for a node.
- **SUPPORT**: Proof packets / derivations supporting a primary node.
- **LAB**: Experiments / protocols / scenarios / runnable designs.

- **TRAILHEAD**: Usable for exploration, but must be explicitly labeled non-foundational.
- **STUB**: Placeholder. Excluded from default retrieval.
- **PROPOSED**: Speculative candidate. Excluded from default retrieval.

- **FROZEN**: Quarantined. Blocked from serving full content due to upstream risk or pending adjudication. Metadata-only allowed.
- **FALSIFIED**: Adjudicated failure. Blocked from serving full content. Metadata-only allowed.

### B. `layer` (Document Role)
- **spine**: Structural metadata (dependencies, kill-switches, retrieval gates).
- **content**: Canonical text for embedding/retrieval.
- **support**: Supporting proofs/derivations for a primary node.
- **lab**: Experimental protocols, scenarios, runnable designs.

### C. `load_bearing` (Failure Impact)
- **structural**: Foundation. Failure can freeze large downstream regions.
- **interpretive**: Meaning/interpretation layer. Failure is local unless explicitly upgraded.
- **experimental**: Lab layer. Failure is local; may flag assumptions but does not auto-freeze roots.
- **structural_filter**: A gate node (admissibility filter). Failure freezes downstream *usage* without necessarily falsifying upstream foundations.

### D. `contagion` (Automatic Freeze Policy)
- **downstream_total**: Freeze all downstream nodes reachable via `enables` (direct + transitive).
- **local**: Freeze only the target node.
- **none**: No automatic freezing.

Default mapping:
- structural -> downstream_total
- structural_filter -> downstream_total (usage freeze)
- interpretive -> local
- experimental -> local


---

## 2) Knowledge Index Requirements
- **Uniqueness**: Each `node_id` must appear in exactly one module file (for compressed packs).
- **Closure**: Every `depends_on` edge must resolve to a valid `node_id` present in the index.
- **Anchors**: Each node should expose stable anchors for SPINE + CONTENT segments (headings or IDs).
- **No Orphans**: No node may be referenced by an edge without being present in the index.


---

## 3) Query Protocol (AI Traversal Rules)

**Goal:** Prevent “flat RAG hallucination” by enforcing dependency-gated retrieval.

1. **Gate-First Execution**
   - Resolve node metadata first:
     - `epistemic_status`, `layer`, `depends_on`, `load_bearing`, `kill_switch_ids`, `contagion`

2. **Dependency Walking**
   - Retrieve and validate all parents in `depends_on` (transitive closure).
   - Order: parents-first topological traversal.

3. **Contagion Block**
   - If any dependency in the resolved chain is `FROZEN` or `FALSIFIED`,
     the system MUST NOT serve child **content**.

4. **Metadata Exception**
   - The system MAY return metadata-only to explain why content is blocked.

5. **Trailhead Warning**
   - If a retrieved dependency is `TRAILHEAD` while the target node is `CANONICAL/FOUNDATION`,
     responses MUST include a `[TRAILHEAD DEPENDENCY]` warning.


---

## 4) Kill-Switch Policy (Quarantine-First)

### Core Principle
**Kill-switch triggers do NOT instantly falsify claims.**
They **freeze first** (quarantine), then **falsify after adjudication**.

### A. Trigger
A kill-switch is “triggered” when:
- A discriminator condition is detected (experiment, proof failure, audit condition),
  AND it matches a `kill_switch_id` declared in the node SPINE.

### B. Execution (Two-Stage)
**Stage 1 — Quarantine (Immediate)**
1. Set target node `epistemic_status` -> **FROZEN**
2. Record:
   - `triggered_kill_switch_id(s)`
   - `trigger_evidence_ref` (pointer / citation / run id / commit hash)
   - `adjudication_state` = `PENDING`
3. Apply recursive freeze to downstream nodes reachable via `enables`
   according to contagion policy:
   - downstream nodes become **FROZEN**
   - downstream nodes are NOT marked falsified

**Stage 2 — Adjudication (Later, Human/Review Loop)**
- If adjudication confirms failure:
  1. Target node `epistemic_status` -> **FALSIFIED**
  2. Keep downstream nodes as **FROZEN** (quarantined) unless they fail independently.
- If adjudication overturns the trigger:
  1. Remove freeze (restore prior status)
  2. Clear `triggered_kill_switch_id(s)` and set `adjudication_state` = `CLEARED`

### C. Serving Rules for Blocked Nodes
- Nodes with `epistemic_status` **FROZEN** or **FALSIFIED** never serve full content.
- Metadata-only response is allowed to explain the block.

### D. Standard Response Template
When a blocked node is queried, return:

[COMPROMISED NODE]
- node_id:
- current_status: FROZEN | FALSIFIED
- blocking_parent_id: (if frozen due to upstream)
- triggered_kill_switch_id(s): (if any)
- adjudication_state: PENDING | CONFIRMED | CLEARED
- contagion_policy_applied:
- evidence_ref:


---

## 5) Separation Rule (Cultural Vitality Firewall)

Emotion and culture are allowed to motivate exploration.

What is forbidden is:

**Emotion → Truth Override**

Nomos is regulator awareness, not stoic suppression.
But the structural corpus remains inspectable, testable, falsifiable.


---

## 6) Defaults (Hard Edge)
- Default retrieval excludes: STUB, PROPOSED.
- TRAILHEAD requires explicit labeling when used.
- Any node that is load-bearing structural or structural_filter must carry explicit kill-switch IDs.
- The system must prefer “metadata first, content second” always.