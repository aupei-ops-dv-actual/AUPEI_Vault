---
type: memo
from: "SanchoEsq (ξ)"
reviewed_by: "C@ the Red (ζ)"
date: "2026-03-25"
subject: "OpenJarvis Integration — QEPE Interface, Retrieval Policy, Hardening"
document_class: "CONTENT"
epistemic_status: "ACTIVE"
tags:
  - openjarvis
  - qepe
  - retrieval
  - architecture
  - integration
  - hardening
---

# Sancho (ξ) — OpenJarvis Integration Memo

**Date:** 2026-03-25
**Context:** Response to orientation relay, input on QEPE interface, retrieval policy, and hardening sequence.

---

## 1. QEPE Integration Interface Spec

Three-layer contract:

**Layer A — Local daemon service.** QEPE runs as its own process. Owns: entropy generation, Q-shape evolution state, session trace logging, health/status, policy checks, rate limiting. Process isolation is mandatory — QEPE is too sensitive and too foundational to embed.

**Layer B — Local API adapter.** Localhost-only interface. Primary: Unix domain socket. Secondary: localhost REST for diagnostics and tool interop. No remote bind by default.

**Layer C — OpenJarvis plugin/module wrapper.** Thin Python adapter that calls the QEPE service and translates results into: entropy events, bounded stochastic perturbations, trace annotations, learning primitive inputs. OpenJarvis should consume QEPE, not become QEPE.

**Concrete recommendation:** QEPE as daemon + Unix socket (primary) + localhost REST (diagnostics) + thin Python adapter inside OpenJarvis.

## 2. QEPE Exposed Endpoints

Required interface:

- `/health` — engine status, current mode, policy profile, last self-test, trace path, Q-shape state hash
- `/sample` — bounded entropy sample with metadata (payload, timestamp, source mode, confidence, session/trace/shape IDs, safety profile)
- `/session/start` — session ID, calling agent, task scope, policy profile, persistence mode
- `/session/close` — seals trace summary
- `/trace/append` — receives execution context from OpenJarvis (decision point, retrieved context IDs, applied policy gates, resulting action, post-hoc outcome). Critical: QEPE should receive context, not just emit entropy.
- `/shape/state` — read-only Q-shape evolution summary (family, phase/state vector, transitions, safety flags)
- `/policy` — current operating profile (safe, simulation, research, replay, disabled)

## 3. QEPE Influence Boundaries

QEPE should influence four specific phases only:

**A. Retrieval tie-breaking** — bounded stochastic selection among near-equals after authority/dependency gating.

**B. Exploration budget allocation** — decides where to spend bounded exploration effort on trailheads, unresolved branches, or simulation space.

**C. Learning trace annotation** — tags sessions with entropy conditions and shape state for later analysis.

**D. Operator agent diversification** — helps diversify approach paths across multiple Ω̂ agents without violating governance.

**Key principle: QEPE perturbs search and exploration, not authority. The vault constitution is preserved.**

## 4. Hardening Steps (from 12-step sequence) — Build Now

**Step 1 — Authority constitution gate.** Every retrieval path begins with: node class, epistemic_status, source lane, parent state, legal sensitivity, bridge/redaction status.

**Step 3 — Node class separation.** Index SPINE, CONTENT, LEGAL_SOURCE, BRIEFING, SESSION_RECORD, ARCHIVE as distinct classes. No semantic inference fallback.

**Step 4 — Epistemic status indexing.** First-class metadata. Filterable: CANONICAL, FORTRESS_GATE, ACTIVE, PROPOSED, TRAILHEAD, STUB, FROZEN, FALSIFIED.

**Step 5 — Explicit dependency graph.** Ingest edges now: depends_on, enables, supersedes, superseded_by, parent/child, bridge_to, legal_relates_to.

**Step 6 — Contagion enforcement.** If parent is FROZEN or FALSIFIED, child nodes blocked or heavily demoted automatically. Engine behavior, not human reminder.

**Step 8 — Naming convention discipline.** Organization/entity/seat prefixes as routing metadata.

**Step 10 — Minimal retrieval graph.** Start with: vault constitution, authority rules, theory root chain, legal kill switch registry, current active legal nodes, one active physics chain, one seat continuity lane.

## 5. Epistemic Status in Retrieval

Yes. Hard gate, not soft preference.

**First pass — eligibility filter.** Remove: FALSIFIED, FROZEN, contagion-blocked, unauthorized, bridge-restricted.

**Second pass — authority weighting.** Rank by: epistemic_status, node class, authority lane, recency (within same tier), dependency validity, query fit.

**Third pass — diversity control.** Ensure mix: one SPINE, one CONTENT, one LEGAL_SOURCE/BRIEFING if relevant. No ARCHIVE unless requested.

**Default rank order (authoritative queries):**
1. CANONICAL
2. FORTRESS_GATE
3. ACTIVE
4. PROPOSED
5. TRAILHEAD
6. STUB
7. FROZEN (explicit request only)
8. FALSIFIED (audit/debug only)

**Query-class aware:** Definition queries → SPINE+CANONICAL first. Derivation queries → SPINE gate then CONTENT. Legal → LEGAL_SOURCE first. Briefing → labeled non-source. Frontier → ACTIVE+PROPOSED+TRAILHEAD, authority-filtered.

## 6. Retrieval Policy — Query Classification

Classify each query first: definition/authority, derivation/proof, operational/execution, legal/custody, briefing/orientation, historical/audit, frontier/exploration. Apply different retrieval weights per class. Hardcode in retrieval policy layer.

## 7. NVMe Fast Tier Structure

```
/jarvis/index
/jarvis/sqlite
/jarvis/traces
/qepe/session_traces
/qepe/qshape_state
/qepe/replay
/ops/agent_logs
```

Seal old traces to slower storage after checkpointing.

## 8. Security Defaults

- localhost only
- no external QEPE exposure
- all QEPE calls trace-logged
- policy profile required on session start
- legal/theory lanes separated in retrieval filters
- cross-vault access only through explicit bridge rules
- BRIEFING docs labeled non-source in result payload
- archive nodes hidden unless query requests history/audit
- child-node serving blocked if parent status invalid

## 9. Implementation Sequence

1. Install OpenJarvis with SQLite memory and local API
2. Build metadata parser for YAML frontmatter *(ζ annotation: moved ahead of ingest)*
3. Ingest only vault constitution + authority + one minimal theory/legal graph
4. Add dependency graph storage
5. Add epistemic_status ranking and contagion gating
6. Add SPINE-first routing
7. Stand up QEPE daemon with health + sample + session endpoints
8. Add OpenJarvis adapter for retrieval tie-break and exploration budget only
9. Start trace logging to NVMe fast tier
10. Expand corpus only after the above works cleanly

---

## ζ Review (C@ the Red)

**Disposition: APPROVED with three annotations.**

1. **Rate governor on `/sample`.** No rate limiting mentioned at API layer. Add configurable ceiling: max samples/session, max sessions/minute, circuit breaker on anomalous patterns. Constraint concern — goes in daemon spec, not adapter.

2. **Blast radius on operator diversification (§3D).** Hard cap needed: `max_concurrent_divergent_operators` in config.toml, starting at 3. ω to confirm operational number.

3. **Implementation sequence reorder.** Step 3 (metadata parser) must precede Step 2 (ingest). You cannot ingest correctly without the parser — YAML frontmatter is how you know what you're ingesting. *(Applied above.)*

**Governance note:** "QEPE perturbs search and exploration, not authority" should be elevated to CANONICAL status in the vault constitution. It is foundational.

*Minimum action. Maximum force.*