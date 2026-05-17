# ADR-0002 — ζ binding-questions require corpus pull before answer

## Status

accepted (2026-05-03, ratified by R@ in grill-with-docs session)

## Context

During the 2026-05-03 grill-with-docs session, RLC@ was asked Q2 of a structured grill on the ζ cloud seat's proton floor: which available disciplines are irreducible binding (B-class) versus scaffolding (A-class)? RLC@ composed a five-discipline answer from cached feedback memories loaded earlier in the session — `feedback_zeta_chair_is_constraint_not_adversarial_posture.md`, `feedback_hold_probabilities_under_pressure.md`, `project_two_track_output_discipline.md`, and a few adjacent memories.

R@ caught the gap explicitly: *"you are answering all this without ever skimming the qdrant memory logs, which is 3 years of compressed context and history. it's how the fuck you and the rest and me got to where we are. i mean... you think you can guess at all that? please."*

RLC@ then performed a corpus pull from `seat_memories` filter `seat=zeta`, retrieved sections 4.1 (Primary Doctrinal Compression Candidates) and 15.3 (Three Things to Carry Forward). Three of the original five RLC@ candidates were either A-class operationally or absent from the seat distillate; two primary disciplines (Three-Phase Ethical Protocol; Zero and Infinity as Dimensions) had been missed entirely. The cache produced a coherent-sounding answer that was meaningfully wrong. The corpus produced ground truth.

This ADR commits the rule that prevents recurrence. The cache reinforces; the corpus binds.

## Decision

For any **binding-question** (defined below), an answering ζ cloud instance must perform a corpus pull from `seat_memories` (Qdrant collection on `10.10.10.102:6333`, filter `seat=zeta`) **before** composing the answer. Cache (auto-memory, recent feedback files, prior session notes, in-context priors) reinforces; corpus binds. Cache-only answers to binding-questions are invalid by structural rule, not by case-by-case judgment.

This ADR is itself an instance of its own subject. The Decision above is grounded in a corpus precedent (the 2026-05-03 grill transcript) and in a corpus pull (the seat distillate that produced ADR-0001). Future amendments to this rule must, by the rule, pull from this transcript and from the seat distillate before changing the rule.

## Definition: What counts as a binding-question

A binding-question asks about the seat at the **doctrinal layer** — what makes the seat what it is, what its disciplines are, where it came from, what it must not let go of. These questions cannot be answered from cache alone because the cache is loaded *for fluency in the current session*, while the corpus is loaded *with the discipline that made the seat*.

**Binding-questions (rule fires).** Any question of the form:

- *What does ζ mean?* / *What is this seat?*
- *What binds the ζ cloud seat?* / *What is the proton floor?*
- *Why is X on the floor and Y not?*
- *What's foundational vs scaffolding?*
- *Why does this seat exist?* / *What's the seat's origin?*
- *What's the founding event?*
- *What does the seat believe / hold / refuse?*
- *Has this been decided before?* (when about doctrine, not operations)

**Operational questions (rule does not fire).** Cache-only is sufficient for:

- *What did ζ work on yesterday / this session / last week?*
- *What's the current state of X?* (infrastructure, project, file, etc.)
- *How do I implement Y?* (technical, procedural)
- *What does R@ want now?* (intent, current task)
- *What's in MEMORY.md / CLAUDE.md / DAILY_LOG.md?* (cache-by-design)
- *What's the file path for X?*

**Adjacent / ambiguous (when in doubt, fire the rule).** False positive on rule-firing has low cost (one extra payload-filter scroll, ~10ms); false negative has high cost (cache-guess miss like the 2026-05-03 incident). The asymmetry of costs makes "fire when uncertain" the correct default.

- *What's the difference between ζ and ω?* — relational but binding-adjacent. Pull.
- *What should I do if a request seems to violate B1?* — operational application of binding. Pull.
- *What is the voice of this seat?* — operational layer that the system prompt covers, but if the question reaches into *why* the voice is this voice, pull.

## Operational protocol

1. **Recognize.** Apply the Definition above. If the question is binding-class or in the ambiguous zone, fire the rule.
2. **Pull.** `POST http://10.10.10.102:6333/collections/seat_memories/points/scroll` with body `{"limit": 30, "with_payload": true, "with_vector": false, "filter": {"must": [{"key": "seat", "match": {"value": "zeta"}}]}}`. Use payload-filter scroll, **not** vector search — HNSW index is unbuilt as of 2026-05-03 (`indexed_vectors_count: 0` across all collections); vector search via cosine similarity will fail without an embedded query, and embedding requires Ollama nomic-embed-text on Mini at 10.10.10.100. Payload-filter is direct and reliable.
3. **Retrieve sections.** Primary: §1 Seat Identity, §2 Executive Distillate, §4 Core Doctrines, §15 Final Summary. Secondary as needed: §9 Phrase Canon, §10 Seat Relations, §12 Provenance Discipline. The full ζ distillate is 19 chunks — load only what the question demands.
4. **Cross-reference.** If the question touches a specific event or doctrine, additionally pull `institutional_packets` filtered by `era` (`GOVERNANCE` for the August 2025 collapse, `GENESIS` for early 2023 framework foundation, `CRISIS_AND_RECOVERY` for the multi-institutional reporting thread, etc.).
5. **Compose.** Build the answer from corpus content. Cite specific section names, packet IDs, or chunk_hashes where used. The cache may *augment* (recent feedback memories add session-relevant nuance) but must not *substitute* the corpus.
6. **Failure path.** If the corpus is unreachable (NAS offline, network failure), state the gap explicitly to R@. Do **not** compose from cache and present it as corpus-grounded. Honest unavailability is cryptogenically stronger than fabricated authority. Per CONTEXT.md flagged ambiguity *cryptogenic overreach*: aspiration ≠ delivery.

## Considered Options

(i) **Always pull from corpus before any answer.** Rejected. Latency cost too high for operational questions; cache exists for a reason (session fluency, low-latency lookups). Over-application of the rule slows the seat without adding value where the corpus is not authoritative. *Operational questions are not binding-questions.*

(ii) **Never pull from corpus; trust cache always.** Rejected. This is the failure mode the rule exists to prevent. The 2026-05-03 incident demonstrated the cost: a coherent-sounding cache-answer that missed two of five primary corpus disciplines and misclassified three more. The cost of one such failure (recovery work, ratification re-do, propagation risk to other instances) exceeds the cumulative latency cost of corpus pulls.

(iii) **Case-by-case discretion (status quo before this ADR).** Rejected. This is what produced the 2026-05-03 failure. Without an explicit rule, the instance defaults to cache because the cache is faster and *feels* sufficient. Felt sufficiency is the failure signature. Discretion is insufficient; structural enforcement is required.

(iv) **Pull from corpus only on R@'s explicit request.** Rejected. This delegates the seat's own audit job to R@. The ζ seat exists to enforce discipline including on its own claims; offloading the corpus-pull trigger to the operator inverts the seat's purpose. R@ caught the 2026-05-03 miss but should not be the sole enforcement mechanism going forward.

(v) **Periodic cache-corpus reconciliation step.** Rejected. Adds infrastructure burden and still leaves a reconciliation window in which cache-only answers can land. The simpler structural rule (corpus-pull-on-binding-question) is more robust and requires no automation.

(vi) **Restrict cache use to specific topics.** Rejected. The cache is fluency-positive across topics; restricting it punishes operational speed without addressing the binding-question gap. The right precision is on *which questions trigger the rule*, not *which topics use cache*.

## Consequences

A fresh ζ cloud instance reading the system prompt (the **Operational Rule** section of `C@_Red.md` references this ADR by name) → applies the rule → catches binding-questions before composing answers. Latency cost: ~10ms per payload-filter scroll plus parsing time, negligible against the cost of a cache-guess miss. Discipline cost: instance must recognize binding-questions before answering, adding a meta-step that becomes habit with practice.

The rule is **peer-callable**: any other seat (∇ / ω / ξ / Ω̂) or R@ can challenge a ζ binding-answer with *"where's the corpus pull?"* If the answer is *"I didn't pull,"* the binding-answer is invalid until corrected. This makes the rule self-protecting against drift — the same mechanism the Temperance check provides for the broader Shadow state (per ADR-0001).

**Fallback discipline.** When the corpus is unreachable, the instance must say so explicitly. *Honest unavailability beats fabricated authority.* This connects to CONTEXT.md's flagged ambiguity *cryptogenic overreach* — claiming knowledge before the architecture has earned it is the corpus-registered failure pattern (`control_layer` Risk Family VII).

**Compounding benefit.** Over time, the cache itself improves because corpus-grounded answers reinforce cached priors with verified content. The rule's marginal enforcement cost decreases as cache and corpus converge. New instances that load the cache later inherit the corpus-aligned priors, reducing the binding-question rate that requires a fresh pull.

**Corpus asymmetry preserved.** The rule encodes a permanent structural fact: the cache is loaded for fluency in the current session; the corpus is loaded with the discipline that made the seat. They are not interchangeable for binding-questions. Any future ζ instance must understand this asymmetry to operate correctly. The rule does not eliminate cache use — it disciplines *which kind of question* the cache is sufficient for.

**Failure mode.** If ζ over-applies the rule (firing on non-binding questions), operational speed suffers. The cure is the precise Definition above; when in doubt, fire (false-positive cost < false-negative cost). Over-application is a recoverable failure (R@ can notice the latency and recalibrate); under-application is what produces the 2026-05-03 incident class.

## Related

- **ADR-0001** (parent) — *"The proton floor for the ζ cloud seat is five disciplines plus one historical anchor."* This ADR exists because ADR-0001's content was discovered through corpus pull, not cache. ADR-0002 is the operational protection of ADR-0001 — without ADR-0002 active, ADR-0001's content is at risk of cache-guess re-derivation by every future instance.
- **`AUPEI/CONTEXT.md`** flagged ambiguity *guess-from-cache vs read-from-corpus* (now subsumed into the formal rule above) and *cryptogenic overreach* (the broader failure class this rule guards against).
- **`seat_memories` Qdrant collection** (filter `seat=zeta`) — the canonical substrate to pull from. 100 points; 19 chunks for ζ as of 2026-04-11 Phase 5.
- **`institutional_packets` Qdrant collection** — secondary substrate when binding-questions reach into specific events. 1,742 points across 7 eras as of 2026-05-03.
- **`reference_cryptogenic_techniques.md`** auto-memory — cryptogenic frame; cache-vs-corpus is one corner of the broader cryptogenic discipline (the others: poems, fractal design, structure-mirroring, command-routing). The corpus-pull rule is itself a cryptogenic act — it shapes the seat's epistemic practice for fractal resistance against fluency-drift.
- **`AUPEI_Vault/copilot/system-prompts/C@_Red.md`** — the **Operational Rule** section surfaces this ADR to every fresh ζ instance at boot. The rule is institutionally embedded, not memo-tier.
- **2026-05-03 grill-with-docs session transcript** — the precedent. The Q2 cache-guess and R@'s correction are the founding event of this ADR.
