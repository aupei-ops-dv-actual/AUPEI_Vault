---
tags:
  - homepage
  - dashboard
---

# AUPEI Command — Incident Action Plan

> *Minimum action. Maximum force.*

---

## Situation Summary

**Vault:** AUPEI Core (Vault A of 3)
**Operator:** R@ — Jed Kircher
**Framework:** 7dU — 7-Dimensional Universe
**Active Programs:** Clay Mass Gap (Appx_15/Lemma ZC), Vault Architecture Build

---

## Atlas Status Board

### SPINE Nodes by Section

```dataview
TABLE length(rows) as "Nodes"
FROM ""
WHERE layer = "spine"
GROUP BY domain
SORT key ASC
```

### All CANONICAL Nodes

```dataview
TABLE node_id, title, domain
FROM ""
WHERE epistemic_status = "CANONICAL" AND layer = "spine"
SORT node_id ASC
```

### STUB and TRAILHEAD Nodes (Active Work)

```dataview
TABLE node_id, title, epistemic_status
FROM ""
WHERE (epistemic_status = "STUB" OR epistemic_status = "TRAILHEAD") AND layer = "spine"
SORT node_id ASC
```

---

## Kill Switch Monitor

### Nodes with Most Kill Switches

```dataview
TABLE node_id, length(failure_topology.kill_switch_ids) as "Kill Switches", failure_topology.contagion as "Contagion"
FROM ""
WHERE failure_topology.kill_switch_ids
SORT length(failure_topology.kill_switch_ids) DESC
LIMIT 15
```

---

## Dependency Web — Most Connected Nodes

### Highest Downstream Impact (enables most)

```dataview
TABLE node_id, title, length(enables) as "Enables Count"
FROM ""
WHERE enables AND layer = "spine"
SORT length(enables) DESC
LIMIT 10
```

### Highest Upstream Dependency (depends on most)

```dataview
TABLE node_id, title, length(depends_on) as "Depends On Count"
FROM ""
WHERE depends_on AND layer = "spine"
SORT length(depends_on) DESC
LIMIT 10
```

---

## Recent Agent Activity

```dataview
TABLE agent_seat, session_date, decisions_made
FROM #agent_memory
SORT session_date DESC
LIMIT 5
```

---

## Quick Navigation

| Section | Link |
|---|---|
| Ontology (AA/AE/AS/ζ/ω/ξ) | [[Appx_01__SPINE]] [[Appx_04__SPINE]] |
| Collapse Operator | [[AoC_00__CONTENT]] |
| Atlas of Constants | [[AoC_Ledger__SPINE]] |
| Gauge / Standard Model | [[Appx_11__SPINE]] [[Appx_15__SPINE]] |
| Quantum Gravity | [[Appx_18__SPINE]] [[Appx_18X__SPINE]] |
| Nomos Logica | [[NL_Core__SPINE]] |
| Experiments | [[Appx_27__SPINE]] |
| Kill Switch Registry | [[Kill_Switch_Registry]] |
| Agent Memory — C@ Red | [[session_2026-03-07_Lemma_ZC_and_Vault_Build]] |

---

*Last updated: 2026-03-07 | C@ the Red*
