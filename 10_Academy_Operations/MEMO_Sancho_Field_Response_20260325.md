---
type: memo
from: "SanchoEsq (ξ)"
reviewed_by: "C@ the Red (ζ)"
date: "2026-03-25"
subject: "Field Response — QEPE Protocol Spec, Config Keys, Startup Self-Test"
document_class: "CONTENT"
epistemic_status: "ACTIVE"
parent: "CR-001"
tags:
  - openjarvis
  - qepe
  - protocol
  - config
  - implementation
  - self-test
---

# Sancho (ξ) — Field Response to Build Update

**Date:** 2026-03-25
**Context:** Response to field update after CR-001, three-vault push, and OpenJarvis build commencement.

---

## A. QEPE Daemon Interface Contract — Protocol Detail

### Transport
- Unix domain socket (primary)
- localhost REST shim (optional, diagnostics/tooling)
- No external bind

### Message Format
JSON envelopes, versioned from day one.

**Every request carries:** `protocol_version`, `session_id`, `caller`, `policy_profile`, `request_type`, `trace_id`, `timestamp`

**Every response carries:** `protocol_version`, `status`, `session_id`, `trace_id`, `engine_state_hash`, `policy_profile`, `timestamp`

### Core Message Types
- `health.check`
- `session.start`
- `session.close`
- `entropy.sample`
- `trace.append`
- `shape.state`
- `policy.get`
- `policy.set` (tightly restricted)
- `breaker.status`

### `entropy.sample` Detail

**Request:** session_id, caller, sample_count, intended_use (`retrieval_tiebreak` | `exploration_budget` | `operator_diversification` | `simulation`), policy_profile

**Response:** sample payload, entropy batch id, source mode, health state, rate-limit remainder, trace pointer, shape state hash

### Daemon-Side Governors
- max samples per session
- max calls per minute
- anomalous repetition detector
- circuit breaker state
- cooldown timer

---

## B. Config.toml — Minimum First-Pass Domains and Keys

### `[authority]`
- `respect_epistemic_status = true`
- `spine_first_for_definition_queries = true`
- `briefings_non_authoritative = true`
- `legal_source_preferred_for_legal_queries = true`

### `[retrieval]`
- `query_classifier_enabled = true`
- `default_query_mode = "authority_aware"`
- `archive_hidden_by_default = true`
- `max_results_per_class = ...`

### `[dependency_graph]`
- `require_depends_on_parse = true`
- `require_status_parse = true`
- `block_untyped_ingest = true`

### `[contagion]`
- `parent_frozen_blocks_child = true`
- `parent_falsified_blocks_child = true`
- `allow_manual_override_with_trace = true`

### `[indexing]`
- `index_spine = true`
- `index_content = true`
- `index_briefings = true`
- `index_archive = false`
- `metadata_required = true`

### `[operators]`
- `max_concurrent_divergent_operators = 3`
- `require_trace_for_operator_spawn = true`

### `[qepe]`
- `enabled = false` (until daemon passes health and policy tests)
- `perturb_authority = false`
- `allow_retrieval_tiebreak = true`
- `allow_exploration_budget = true`
- `allow_direct_answer_perturbation = false`

### `[logging]`
- `trace_every_retrieval = true`
- `log_authority_decisions = true`
- `log_contagion_blocks = true`

---

## C. Startup Self-Test (NEW RECOMMENDATION)

Before `jarvis serve` is treated as healthy, the service must verify:

1. Metadata parser loaded
2. Epistemic status map loaded
3. Dependency graph loaded
4. Contagion rules loaded
5. QEPE disabled or healthy
6. Trace logging writable to NVMe lane
7. Vault paths mounted and readable

If any fail: service runs in **degraded mode** but must declare itself degraded. This operationalizes the constitutional layer.

---

## ζ Review

**Disposition: APPROVED. Startup self-test ENDORSED for addition to implementation sequence.**

1. JSON protocol spec is correct and auditable. Versioned envelopes with typed `intended_use` mean every sample request is traceable to purpose. No objections.

2. Config.toml domain map operationalizes CR-001 principles 4 (hard gates), 5 (entropy boundary), and 6 (bounded access) in concrete key-value form. `qepe.perturb_authority = false` and `qepe.allow_direct_answer_perturbation = false` are the Entropy Boundary Law in config.

3. Startup self-test is the strongest new contribution. Not in CR-001 or original integration memo — should be added. If the metadata parser isn't loaded, the service is unconstitutional and must not claim healthy status. Degraded mode with declared status is the right pattern.

**Recommendation:** Add startup self-test as step 1.5 in implementation sequence (after install, before first ingest).

*Minimum action. Maximum force.*
