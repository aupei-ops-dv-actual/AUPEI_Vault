---
atlas_id: "7dU_GraphRAG_Content"
node_id: "AoC_00"
internal_id: "AoC_00_Constants_Ledger_v1.1"
title: "AoC_00 — Constants Ledger (Master Index)"
status: "CONTENT"
date_minted: "2026-02-21"
layer: "content"
domain: "Atlas of Constants"
---

# AoC_00 — Constants Ledger (Master Index)

This ledger is the authoritative map for constants in the AoC container.

**Rule:** Any constant query must consult AoC_00 first to:
1) resolve canonical ID + aliases  
2) check node status (CANONICAL / TRAILHEAD / DISPUTED / etc.)  
3) enforce dependency gates  
4) identify falsifier hooks (Appx_27 lanes)  

---

## Ledger Fields (Schema)

- **constant_id**: stable identifier for GraphRAG routing (AoC_##)
- **symbol**: conventional symbol where applicable
- **aliases**: allowed query names / synonyms
- **status**: TRAILHEAD | SUPPORT | CANONICAL | DERIVED | PREDICTED | DISPUTED | DEPRECATED
- **primary_node**: canonical AoC node to retrieve for answers
- **depends_on**: gating nodes required before serving content
- **falsifier_hooks**: where to test / discriminate (Appx_27 lanes or test families)
- **notes**: short, constitutional constraints (“do not overclaim”, “requires Selection Law first”, etc.)

---

## Constants Table (Seed Set)

### AoC_01 — π (Pi)
- **symbol:** π
- **aliases:** ["pi", "Pi", "circle constant", "ratio circumference diameter"]
- **status:** CANONICAL
- **primary_node:** AoC_01
- **support_nodes:** ["AoC_01_PI_SUPPORT_00", "AoC_01_PI_SUPPORT_01", "AoC_01_PI_SUPPORT_02", "AoC_01_PI_SUPPORT_03"]
- **depends_on:** ["Appx_01", "Appx_02"]  # ontology gates; avoid free-floating numerology
- **falsifier_hooks:** ["Appx_27 (Sector A: analytic/numerical cross-checks)"]
- **notes:** "Treat π as a geometric law anchor; support packets carry analytic/radial/numerical derivations."

---

### AoC_02 — c (Speed of Light)
- **symbol:** c
- **aliases:** ["speed of light", "lightspeed", "c0"]
- **status:** TRAILHEAD
- **primary_node:** AoC_02
- **depends_on:** ["Appx_08", "Appx_09"]  # time + spatial dimensions typically gate c
- **falsifier_hooks:** ["Appx_27 (Sector A/B: timing, propagation, cosmological distance ladders)"]
- **notes:** "If content is not yet canonicalized in AoC, do not overclaim; route to trailhead and proposed tests."

---

### AoC_03 — α (Fine-Structure Constant ≈ 1/137)
- **symbol:** α
- **aliases:** ["fine structure constant", "alpha", "1/137", "137", "FSC", "FSC_137"]
- **status:** CANONICAL
- **primary_node:** AoC_03
- **depends_on:** ["AoC_01", "Appx_04", "Appx_06"]  # π + bounds/chance often appear in derivations
- **falsifier_hooks:** ["Appx_27 (Sector A: spectroscopy precision; atomic structure residuals)"]
- **notes:** "Treat α-derivation claims as load-bearing; cite support packets when invoked."

---

### AoC_04 — Proton Mass
- **symbol:** m_p
- **aliases:** ["proton mass", "mp", "m_p"]
- **status:** CANONICAL
- **primary_node:** AoC_04
- **depends_on:** ["Appx_25", "AoC_03"]  # Selection Law gate + α context
- **falsifier_hooks:** ["Appx_27 (Sector A: particle/atomic residuals); Appx_27a (if gravity-threshold coupling is invoked)"]
- **notes:** "Do not serve proton-mass explanation without Selection Law gate; falsification is contagious downstream."

---

### AoC_05 — Neutron Mass
- **symbol:** m_n
- **aliases:** ["neutron mass", "mn", "m_n"]
- **status:** CANONICAL
- **primary_node:** AoC_05
- **depends_on:** ["Appx_25", "AoC_04"]  # Selection Law gate + proton reference
- **falsifier_hooks:** ["Appx_27 (Sector A: nuclear residuals / mass splitting); Appx_27a (only if gravity coupling is claimed relevant)"]
- **notes:** "Neutron-proton splitting should remain tightly gated; avoid speculative leaps without test hooks."

---

### AoC_06 — G (Gravity Constant / On Gravity)
- **symbol:** G
- **aliases:** ["gravitational constant", "Newton's constant", "big G", "G_N"]
- **status:** TRAILHEAD
- **primary_node:** AoC_06
- **depends_on:** ["Appx_21", "Appx_22"]  # GR reduction + black holes are typical gravity gates
- **falsifier_hooks:** ["Appx_27a (primary lane: gravity threshold discriminator)", "Appx_27 (Sector B: macro tests)"]
- **notes:** "Gravity is currently treated as trailhead; do not present as closed-form without linking to Appx_27a lane logic."

---

## Alias Discipline (Non-Negotiable)

If a query term is not listed under **aliases**, the assistant should:
- treat it as unknown or ambiguous
- propose adding it to AoC_00 after verification
- avoid silently mapping it to a nearby constant

This prevents constant-ID drift and keeps GraphRAG truthful.

---

## Revision Protocol

When any AoC node is updated:
- update **status**
- update **depends_on** gates if needed
- add or revise **falsifier_hooks**
- append a one-line change note in the primary node (not here)

AoC_00 is the routing truth table.

---

## ChangeLog — Constant Promotion Ledger

This section records formal status changes of constants within the AoC framework.

Each entry must include:
- Date (YYYY-MM-DD)
- Constant ID (e.g., AoC_03)
- Previous Status (e.g., TRAILHEAD, SUPPORT)
- New Status (e.g., CANONICAL, DERIVED, DISPUTED)
- Justification reference (Appendix or Experiment Lane)
- Decision authority (e.g., Ledger vote, Experiment 27a result)

---

### Entries

(Reserved)


---

## Navigation

**SPINE:** [[AoC_Ledger__SPINE|AoC_00 SPINE]]
