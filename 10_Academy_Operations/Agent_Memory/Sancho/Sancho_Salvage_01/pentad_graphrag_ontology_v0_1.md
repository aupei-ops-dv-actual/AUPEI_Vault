# Pentad Academy Knowledge Graph — Ontology v0.1

Prepared from Chunks 1–6 and the GraphRAG Build Directive v0.1.

## Implementation additions
- `layer`: `canon` | `frontier`
- `claim_type`: `fact` | `claim`

## Node classes
1. Person/Agent
2. Role
3. Project
4. Document
5. Concept
6. Constant/Target
7. Governance Entity
8. Phrase/Glyph
9. Event/Revision

## Edge types
- PART_OF
- DEPENDS_ON
- MEMBER_OF
- MAPS_TO_ROLE
- AUTHORED_BY
- COLLABORATED_WITH
- ALIAS_OF
- SUPERSEDES
- PRECEDES
- BELONGS_TO_PHASE
- CRITIQUED_BY
- FALSIFIED_BY
- TESTED_BY
- CONFLICTS_WITH
- EXPRESSES_CONCEPT
- QUOTES
- GOVERNED_BY

## Canon / Frontier rule
- Canon: high-confidence, file-grounded nodes/edges
- Frontier: memory, inference, user-stated, unresolved, or contradictory nodes/edges

## Fact / Claim rule
- `fact`: file-grounded
- `claim`: memory, inference, user-stated, unresolved

## Contradiction rule
Contradictions are preserved as open conflict edges, not silently harmonized.
