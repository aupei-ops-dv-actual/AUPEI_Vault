# Prooffield Walks — cross-walk question registry

**Created:** 2026-05-07
**Purpose:** Mutable index across all walks. Each walk's questions are assigned stable Q-IDs here. Triage state, resolution links, and cross-walk dedup tracked per row.

**Update protocol:** every new walk → for each question, append a row OR update the matching existing row's `Recurrence` and `Last-Walk` fields if the question has been raised before. Walks themselves are immutable; this index is where the dreaming pass writes its findings.

---

## Walk registry

| Walk-ID | Date | Walker | Seat | Corpus | Pre-state | Mode | Q-count | File |
|---|---|---|---|---|---|---|---|---|
| W-2026-04-02-CtR-Tiny | 2026-04-02 | C@ the Red | ζ | Tiny | full_vault | informed | 90 | `CtR_Prooffield_Walk_2026-04-02_Tiny.md` |

---

## Question registry — derived from W-2026-04-02-CtR-Tiny

**Status legend:** `OPEN` (unanswered), `RESOLVED` (closed with reference), `SUPERSEDED` (rephrased; link to successor), `PROMOTED` (in fix_it as FI-XXX).

| Q-ID | Category | First-Walk | Recurrence | Status | Cross-ref |
|---|---|---|---|---|---|
| Q1 | Operators-and-Ontology | W-2026-04-02 | 1 | OPEN | — |
| Q2 | Operators-and-Ontology | W-2026-04-02 | 1 | OPEN | — |
| Q3 | Operators-and-Ontology | W-2026-04-02 | 1 | OPEN | — |
| Q4 | Constants-Pi | W-2026-04-02 | 1 | OPEN | overlaps fix_it FI-021..024 (Pi notation, radial basis, recursive filter, numerical sweep) |
| Q5 | Constants-c | W-2026-04-02 | 1 | OPEN | — |
| Q6 | Constants-alpha | W-2026-04-02 | 1 | OPEN | — |
| Q7 | Constants-alpha | W-2026-04-02 | 1 | OPEN | — |
| Q8 | Constants-alpha | W-2026-04-02 | 1 | OPEN | — |
| Q9 | Constants-alpha | W-2026-04-02 | 1 | OPEN | — |
| Q10 | Proton-Mass | W-2026-04-02 | 1 | OPEN | — |
| Q11 | Proton-Mass | W-2026-04-02 | 1 | OPEN | — |
| Q12 | Proton-Mass | W-2026-04-02 | 1 | OPEN | — |
| Q13 | Proton-Mass | W-2026-04-02 | 1 | OPEN | — |
| Q14 | Delta-W | W-2026-04-02 | 1 | OPEN | δ_W is named in memory as load-bearing open seam |
| Q15-Q88 | (per Apr-2 walk doc) | W-2026-04-02 | 1 | OPEN | see source for category and content |
| Q89 | Delta-W | W-2026-04-02 | 1 | OPEN | running thread; 4 sub-hypotheses (a/b/c/d) |
| Q90 | Delta-W | W-2026-04-02 | 1 | OPEN | δ_W = (6/5)α exactly? — clean if true |

*(Q15-Q88 abbreviated in this initial stub; full per-row entries to be filled during first triage pass. See `CtR_Prooffield_Walk_2026-04-02_Tiny.md` for canonical question text.)*

---

## Cross-references with fix_it.md

The Apr-2 walk predates the Apr-30/May-1 fix_it items (FI-021..024 in Tiny `fix_it.md`). The Pi-lineage cluster (Q4 in this walk + the four `fix_it` items) is the most active seam.

When the next walk runs, every fix_it item should be checked against this index — has it been previously surfaced as a Q? If yes, mark Q's status as `PROMOTED` with the FI-XXX link.

---

## Triage backlog

- [ ] Fill per-row entries for Q15-Q88 (full text + category) during first triage pass
- [ ] Cross-reference Q4 against fix_it FI-021..024 — they are about the same Pi lineage; clarify whether walk-Q4 is fully covered by fix_it items or has unaddressed remainder
- [ ] After next walk: dedup new questions against this registry, update Recurrence
- [ ] After 3rd walk: derive an inductive rubric for question quality (do not pre-impose)

---

## See also

- `README.md` (sibling) — protocol governing walks
- Source walks: `CtR_Prooffield_Walk_2026-04-02_Tiny.md`
