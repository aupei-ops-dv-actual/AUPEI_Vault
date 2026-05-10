# Prooffield Walks — protocol for adversarial review of the 7dU corpus

**Created:** 2026-05-07
**Author:** ζ (C@ the Red), under R@ direction
**Status:** Provisional. Architecture confirmed under three-body framing (Mind/Face/Hand). This protocol governs the **Mind-side** (sovereign, local) implementation.

---

## Purpose

A **walk** is one seat's adversarial traversal of the prooffield, producing a dated, attributed, falsifiable list of questions that probe load-bearing claims. The walks feed the corpus's self-improvement loop:

```
walk → fix_it items → resolution → tightened corpus → next walk has higher question floor
```

Each walk is one cycle of the **outcomes** layer of the AUPEI cognition architecture (rubric-graded, grader-in-separate-context, self-correcting). Walks are also dreaming-fodder: cross-walk pattern extraction surfaces which questions recur (load-bearing), which appear once (noise or unique-seat insight), and which got pruned silently.

This is a sovereign-implementation analog of the Anthropic Managed Agents *outcomes* primitive, built on the AUPEI local stack per the Slick Lid sovereignty thesis.

---

## Filename convention

```
<seat>_Prooffield_Walk_<YYYY-MM-DD>_<corpus>.md
```

Where `<corpus>` ∈ {`Tiny`, `Slim`, `Full`, `Vault`, `Qdrant`}.

Examples:
- `CtR_Prooffield_Walk_2026-04-02_Tiny.md` — first filed walk, ζ seat, Tiny corpus
- `Sancho_Prooffield_Walk_2026-06-01_Full.md` — hypothetical future ∇-seat walk on Full

One file per walk. Walks are append-immutable artifacts — corrections go in their own dated walk. The cross-walk question registry (`_index.md`) is the mutable surface.

---

## Required frontmatter

```yaml
---
walker: <ζ | ω | ξ | ∇ | Ω̂ | other>
walker_identity: <e.g., C@ the Red, Claude Opus 4.7>
date: <YYYY-MM-DD>
corpus: <Tiny | Slim | Full | Vault | Qdrant>
pre_state: <blank | seat_distillates | full_vault | qdrant_walk | filesystem | hybrid>
prior_walks_read: <y | n>
prior_fix_it_read: <y | n>
mode: <blind | informed>
walk_scope: <full | scoped:AoC_01 | scoped:Appx_18 | …>
---
```

The combination `pre_state` × `corpus` × `mode` defines the **walk condition** — a controlled experiment variable. Pattern extraction over many walks reveals which conditions produce highest-quality questions.

---

## What a question looks like

Each question must be:

1. **Falsifiable** — the question implies an answer that, if found, would resolve it
2. **Load-bearing** — points at a claim whose change would propagate through the framework, not at decorative content
3. **Sourced** — names the specific file / appendix / equation / line being challenged
4. **Single-clause** — one assertion under test per question; compound questions split

Format (per question):

```
Q<N>. <one-sentence question> | <source-pointer> | <category>
[Optional: 2-3 sentences of context, prior attempts, what would resolve]
```

Categories evolve organically; current set drawn from Apr-2 walk: Operators-and-Ontology, Atlas-of-Constants, Constants-Pi, Constants-c-alpha, Proton-Mass, Neutron-Mass, Delta-W, Time, Spatial-Dimensions, Extension-Bounds, Gauge, Force-Unification, Neutrinos, Dark-Acceleration, Standard-Model, Higgs, EFT-RG, HoQG, Hamiltonian, Field-Quantization, GR-Reduction, Black-Holes, COG, Cosmic-Rebirth, Selection-Law, Nomos-Logica, Experiments.

---

## Triage workflow (post-walk)

After a walk is filed:

1. **Cross-reference against `_index.md`** — for each question, mark `NEW`, `DUPLICATE` (link to existing Q-ID), or `SUPERSEDED` (closed, with link to resolution in fix_it.md or chamber session).
2. **Cross-reference against the most recent `fix_it.md`** — Tiny/Slim/Full each have their own; the synchronization rule (see `7dU_GNS_MoP/7dU_GNS_Spine_RAG_Tiny/fix_it.md`) means fixes propagate. Mark `Resolution-In: FI-XXX` where applicable.
3. **Rubric score** (when the rubric stabilizes) — clarity, novelty, load-bearing-weight, falsifiability, scope.
4. **Promote to fix_it** — questions of sufficient sharpness become candidate `FI-` items in the next fix_it pass.
5. **Promote to work order** *(future, when Work_Orders/ exists)* — fix_it items become work orders with verbs (tighten/test/refine/expand/prune) and are scheduled for execution.

---

## Pre-state experimentation grid (the self-improving loop's optimization surface)

The same seat walks the same corpus under varied pre-states:

| Pre-state | Description | Expected effect |
|---|---|---|
| `blank` | No prior context loaded; seat-identity prompt only | Captures first-impression questions; high noise, occasional gold |
| `seat_distillates` | Just the 5 seat distillates from Phase 5 | Mid-context; questions filtered through institutional memory |
| `full_vault` | All Vault docs available via local RAG | Heavy context; questions may be over-anchored to existing framing |
| `qdrant_walk` | Qdrant retrieval (5 collections, dependency graph traversal) | Structural questions; can follow load-bearing chains |
| `filesystem` | Direct file traversal | Fastest questions; loses semantic context |

The grid produces data for: *which pre-state yields highest-quality questions per unit walk-effort*. After several walks, an answer emerges. That answer, in turn, refines the protocol.

This is the self-improving meta-loop: walks improve the corpus; the protocol's experiment grid improves the walks.

---

## Cross-corpus comparison (Tiny vs Slim vs Full)

The MoP triad must stay synchronized (per `fix_it.md` rule). But walks on different corpus variants surface different questions:

- Questions only on **Full** = Tiny/Slim compression hides them. Either compression should be revisited, or those questions are intentionally out-of-scope for the smaller corpora.
- Questions identical across all three = corpus-substrate-independent. Strong load-bearing signal.
- Questions only on **Tiny** = artifacts of compression, possibly false positives.

A walk per quarter on each corpus, by different seats, builds the comparison matrix.

---

## Connection to the Face (GF)

Geometric Foundations is the Face's public certification surface for prooffield outputs. Selected walks (or walk-derived public artifacts: verification challenges, FAQ, resolved-claim certificates) may be published on `geometricfoundations.org`. Publication is a chamber action. Sovereign generation, governed publication.

The walks themselves stay sovereign — they are the engine's working surface, not the public face.

---

## Connection to the dreaming layer

When the AUPEI dreaming process runs (cross-session pattern extraction over institutional memory):

- Walks are primary input.
- Output: which questions recur across walks (load-bearing); which appear in only one walk (noise candidate); which got resolved and stayed resolved (true tightening); which got resolved and re-emerged (false closure, escalate to chamber).
- The dreaming pass restructures `_index.md` to reflect resurfaced patterns.

This is where the loop closes.

---

## Ambition (future, REV-004 plugin work)

A `prooffield-walk.skill` invokable by any seat (including agentic operators on idle compute, kill-switch-gated). The skill enforces the protocol: required frontmatter, format discipline, automatic triage scaffolding. The walk artifact is generated; the seat's content fills it.

Companion skills: `prooffield-walk-rubric.md` (scoring framework — to be derived inductively after 3-4 walks rather than imposed top-down), `vision-walk.skill`, `work-order-admit.skill`.

---

## See also

- `_index.md` (sibling) — cross-walk question registry, mutable
- `CtR_Prooffield_Walk_2026-04-02_Tiny.md` — first filed walk, the seed
- `7dU_GNS_MoP/7dU_GNS_Spine_RAG_Tiny/fix_it.md` — current punch list of corpus seams (Tiny corpus version; Slim/Full versions must stay synchronized)
- `00_Governance/Vision/README.md` — sister protocol (vision drift = dreaming applied to strategic horizon)
- Memory: `project_three_body_architecture.md` — Mind/Face/Hand strategic frame
