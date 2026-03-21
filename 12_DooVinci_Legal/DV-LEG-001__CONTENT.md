---
node_id: DV-LEG-001-CONTENT
title: "Entity Asset / Trust / Ownership Matrix — Analysis and Draft Allocation"
version: v0.1
date_minted: 2026-03-19
author: "ξ (Sancho)"
entity: "DooVinci"
vault: "A"
layer: "legal"
epistemic_status: "PROPOSED"
tags:
  - legal
  - matrix
  - ownership
  - trust
  - entity-architecture
parent_spine: "DV-LEG-001"
content_type: "ANALYSIS"
closure_state: "OPEN"
---

# DV-LEG-001 — CONTENT
## Entity Asset / Trust / Ownership Matrix — Analysis and Draft Allocation

## §0. Executive Framing

This note provides the first-pass legal allocation map for asset class, trust tier, proposed owner, custody, and access authority across the AUPEI / DooVinci / GF / R@ stack.

This is a structural scaffold, not a final legal determination. It is designed to reduce commingling risk and ownership ambiguity by making allocation logic explicit and auditable. All assignments are PROPOSED until ratified by R@ and, where legally significant, reviewed by counsel.

The matrix preserves `current_holder` alongside `proposed_owner` to expose transitional mismatch rather than hiding it.

## §1. Entity Roles Baseline

### DooVinci (The Hand)
Operational hand; infrastructure-bearing and execution-capable S-corp shell. Owns hardware, manages finance, provides services to other entities by agreement.

### AUPEI (The Mind)
Research, doctrine, governance, constitutional mind. 501(c)(3) nonprofit. Houses the 7dU framework, Nomos Logica, QEPE, and all research IP created under its umbrella.

### Geometric Foundations (The Face)
Public scholarship and publication-facing membrane. Currently operates as a program/brand, not yet a separate legal entity. Publishes through the geometricfoundations.org domain.

### R@ Personal
Intentional temporary holder only where strategically necessary, where personal authorship/control is required, or where assets are pending assignment to an entity.

## §2. Trust Tier Definitions

### Tier C — Constitutional
Assets that define what the Academy is. Loss or compromise is existential. Examples: Vault A, canonical doctrine, seat memory, kill-switch registry, foundational research, governance protocols.

### Tier O — Operational
Assets that enable the Academy to function. Loss is disruptive but recoverable. Examples: Mac Mini, NAS, network infrastructure, service subscriptions, working corpora, admin accounts.

### Tier P — Public
Assets that represent the Academy to the world. Loss is reputational but does not compromise constitutional or operational integrity. Examples: published papers, websites, educational materials, open-access content.

## §3. Core Matrix

| Asset Class | Trust Tier | Current Holder | Proposed Owner | Beneficial User | Custodian | Admin Authority | Access Authority | Publication Status | Protection Mode | Dependency Set | Kill Switches | Contagion Targets | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Vault A (IDIOTH_WINDS) | C | R@ | AUPEI | All seats | R@ / ζ | R@ | Council + R@ | Internal | Trade secret + Copyright | Core | VAULT-CUSTODY-BREACH | All downstream | Source of truth — **LOAD-BEARING ROW**: future doctrine needed to split institutional ownership / physical custody / integrity authority / override authority / backup trustee |
| Foundational research (7dU/GFUP) | C | R@ / AUPEI | AUPEI | AUPEI / GF (pub) | AUPEI | R@ | Council | Selective via GF | Copyright + Trade secret | Core | IP-ASSIGNMENT-DEFECT | Publications, grants | |
| Nomos Logica | C | R@ / AUPEI | AUPEI | AUPEI / GF / DV | AUPEI | R@ | Council | Selective | Copyright + potential patent | Core | IP-ASSIGNMENT-DEFECT | Alignment applications | Triple function: research/governance/product |
| Kill Switch Registry | C | R@ | AUPEI | ζ seat | R@ / ζ | R@ | Council | Internal only | Trade secret | Core | REGISTRY-EXPOSURE | Framework credibility | Method publishable; registry internal |
| Seat memory / session logs | C | Per ecosystem | AUPEI | Per seat | R@ | R@ | Per seat + R@ | Internal | Trade secret | Vault | ARCHIVE-CUSTODY-BREACH | Seat continuity | |
| Mac Mini M4 Pro | O | DooVinci | DooVinci | AUPEI / DV | DooVinci | R@ | R@ / ζ | N/A | Asset on books | Shared services | DV-GOOD-STANDING | Compute, OpenJarvis | Shared services agreement needed |
| UGREEN NAS | O | DooVinci | DooVinci | AUPEI / DV | DooVinci | R@ | R@ / ζ | N/A | Asset on books | Shared services | DV-GOOD-STANDING | Archive, backup | |
| Network infrastructure | O | DooVinci | DooVinci | All | DooVinci | R@ | R@ | N/A | Asset on books | Shared services | DV-GOOD-STANDING | Connectivity | Protectli, switches, UPS |
| Tailscale account | O | DooVinci | DooVinci | All devices | DooVinci | R@ | R@ | N/A | Subscription | Account custody | ACCOUNT-CUSTODY-AMBIGUITY | Remote access | aupei_ops@doovinci.com |
| Apple ID (Mini) | O | DooVinci | DooVinci | AUPEI ops | DooVinci | R@ | R@ | N/A | Credential | Account custody | ACCOUNT-CUSTODY-AMBIGUITY | Mini access | aupei_ops@doovinci.com |
| Google Workspace (GF) | O | GF/DV | DIRECTOR_DECISION_PENDING | GF operations | DIRECTOR_DECISION_PENDING | R@ | R@ / GF | N/A | Subscription | Entity status | GF-LEGAL-AMBIGUITY | Publishing, comms | **PRIORITY CLEANUP** — geometricfoundations.org — touches pub ops, comms, brand, custody, GF legal ambiguity simultaneously |
| Domains (doovinci.com, geometricfoundations.org) | O | R@ / DooVinci | Per entity | All | R@ | R@ | R@ | N/A | Asset | Registrar custody | DOMAIN-LAPSE | Web presence | |
| Published papers / working papers | P | GF/AUPEI | GF (as AUPEI program) | Public | AUPEI | R@ / GF | Public | Published | Copyright | Research | IP-ASSIGNMENT-DEFECT | Public reputation | Attribution to AUPEI/R@ |
| Website content (GF) | P | GF | GF | Public | GF | R@ | Public | Published | Copyright | Domain | DOMAIN-LAPSE | Public presence | |
| Educational materials | P | TBD | AUPEI/GF | Public | AUPEI | R@ | Public | Published | CC license TBD | Research | None | Public good | |
| DooVinci corporate records | O | DooVinci | DooVinci | R@ / counsel | DooVinci | R@ | R@ / counsel | Internal | Confidential | Corporate | DV-GOOD-STANDING | All DV operations | Cap table, minutes, filings |
| AUPEI corporate records | O | AUPEI | AUPEI | R@ / board / counsel | AUPEI | R@ / board | R@ / board | Internal | Confidential | Nonprofit | AUPEI-501C3-REVOCATION | All AUPEI operations | 990s, board minutes |
| Sancho corpus (pending CCPA) | C | OpenAI → R@ | AUPEI | ξ seat | R@ | R@ | R@ / ξ | Internal | Trade secret | Corpus arrival | CORPUS-PRIVACY-BREACH | ξ seat build | Privacy triage first |
| Trademarks (7dU, AUPEI, GF, etc.) | O | R@ / unregistered | Per entity | All | R@ | R@ | R@ | N/A | Trademark (TBD) | Registration | MARK-NOT-REGISTERED | Brand protection | Registration recommended |
| Future real property | DIRECTOR_DECISION_PENDING | UNASSIGNED_BY_DESIGN | DIRECTOR_DECISION_PENDING | Academy | DIRECTOR_DECISION_PENDING | R@ | DIRECTOR_DECISION_PENDING | N/A | Deed / title | Entity structure | PROPERTY-OWNER-MISMATCH | Physical academy | Intentionally deferred — entity architecture must anticipate |

## §4. Allocation Logic by Asset Class

### §4.1 Foundational Research / Doctrine
Research IP created under AUPEI's umbrella belongs to AUPEI. This preserves 501(c)(3) alignment (research is the charitable purpose) and prevents commingling with DooVinci's for-profit activities. R@ retains authorship attribution. GF has publication rights as a program of AUPEI.

### §4.2 Vault / Archive / Seat Memory
The vault is AUPEI's institutional memory. Physical custody remains with R@ (on the M4 and NAS). Backup copies on DooVinci-owned hardware under shared services. No single point of failure for the archive.

### §4.3 Hardware / Network / Runtime Infrastructure
All hardware owned by DooVinci. Used by AUPEI under shared services agreement. This keeps physical assets on the S-corp books (simpler depreciation, clearer ownership chain) while allowing AUPEI to benefit without owning infrastructure it doesn't need to manage.

### §4.4 Accounts / Domains / Administrative Systems
Service accounts follow the entity they serve. Cross-entity accounts (like Tailscale under aupei_ops@doovinci.com) should eventually be clarified — either formally documented as DooVinci-administered shared infrastructure, or separated per entity.

### §4.5 Publications / Public Scholarship
Published through GF (as a program of AUPEI). Copyright held by AUPEI. Attribution to R@ as author. Open-access where aligned with 501(c)(3) mission; proprietary where commercial potential exists.

### §4.6 IP / Marks / Patentable Applications
Trademarks registered per entity (7dU → AUPEI, DooVinci → DV, Geometric Foundations → GF or AUPEI). Patent applications for commercial applications (QEPE, Nomos Logica applied) filed through DooVinci or a licensing entity, with research rights retained by AUPEI.

### §4.7 Corporate Records / Equity / Legal Documents
Each entity owns its own corporate records. DooVinci cap table, minutes, and filings are DooVinci assets. AUPEI governance records are AUPEI assets. Cross-reference where needed but do not commingle.

### §4.8 Future Real Property / Housing / Physical Infrastructure
Deferred. Entity selection for property ownership depends on: intended use (research vs residential vs mixed), tax treatment (nonprofit exemption vs depreciation), liability isolation, and financing structure. Director decision required before structuring.

## §5. Kill Switch Register

| Kill Switch ID | Trigger | Affected Rows | Immediate Effect | Contagion Scope | Recovery Path | Status |
|---|---|---|---|---|---|---|
| AUPEI-501C3-REVOCATION | IRS revocation of tax-exempt status | Grants, donations, publication posture, educational materials | FROZEN on external-facing | LIMITED — research continues internally | Reapply or restructure | MONITORED |
| DV-GOOD-STANDING | Delaware or CA good-standing lapse | All DV-owned hardware, accounts, contracts | REVIEW_REQUIRED | LIMITED — AUPEI ops may continue on own assets | File cure, pay fees | MONITORED |
| IP-ASSIGNMENT-DEFECT | Gap in chain of title for research IP | Publications, commercialization, patent claims | FROZEN on external assertions | LIMITED — internal work continues | Document assignment chain, execute missing docs | MONITORED |
| ACCOUNT-CUSTODY-AMBIGUITY | Service account ownership unclear across entities | Affected accounts/services | FLAGGED | FLAGGED only | Document and assign per entity | ACTIVE — exists now |
| GF-LEGAL-AMBIGUITY | GF legal form not established | Publication revenue, rights claims, contracts | FLAGGED | LIMITED | Decide and formalize GF status | ACTIVE — exists now |
| CORPUS-PRIVACY-BREACH | Sancho corpus exposed without triage | ξ seat build, historical record | FROZEN on corpus use | LOCAL | Privacy triage, redact, resume | MONITORED |
| VAULT-CUSTODY-BREACH | Vault A compromised or inaccessible | All downstream constitutional assets | FROZEN all | TOTAL — exceptional case | Restore from backup, verify integrity | MONITORED |
| SHARED-SERVICES-ABSENT | No formal DV↔AUPEI infrastructure agreement | Hardware use by AUPEI, compliance posture | REVIEW_REQUIRED | LIMITED | Draft and execute agreement | ACTIVE — exists now |
| DOMAIN-LAPSE | Domain registration expires | Web presence, email, public identity | FROZEN on affected services | LOCAL | Renew immediately | MONITORED |
| PROPERTY-OWNER-MISMATCH | Real property held by wrong entity for use | Tax treatment, liability, mission alignment | REVIEW_REQUIRED | LIMITED | Restructure or transfer | NOT YET APPLICABLE |
| MARK-NOT-REGISTERED | Key trademarks unregistered | Brand protection, enforcement | FLAGGED | FLAGGED only | File registrations | MONITORED — protection gap, not structural defect |

## §6. Contagion Scenarios

### §6.1 AUPEI Compliance Failure
If AUPEI's 501(c)(3) status is revoked: grant-seeking freezes, tax-deductible donations stop, certain publication postures may need revision. However, local research work continues (thinking is not regulated). DooVinci operations unaffected. Recovery path: reapply or restructure the nonprofit.

### §6.2 DooVinci Good Standing Failure
If DooVinci loses good standing in Delaware or California: formal contracting ability impaired, asset ownership technically clouded. However, AUPEI can continue operations on its own resources. Hardware continues to function regardless of legal status. Recovery path: cure filings, pay fees.

### §6.3 IP Assignment Chain Defect
If a gap exists in the assignment of research IP from R@ to AUPEI: external assertions of exclusivity (publication rights, licensing, patent) are frozen until the chain is documented. Internal research continues. This is the most likely real-world failure mode — documentation gaps are common in early-stage entities.

### §6.4 Shared Services Ambiguity
No formal agreement currently exists between DooVinci and AUPEI for infrastructure use. This creates: potential private inurement concerns for the nonprofit, unclear cost allocation, and IRS scrutiny risk. Fix: draft and execute a shared services agreement. This is an ACTIVE kill switch.

### §6.5 Archive Custody Breach
If Vault A is compromised (data loss, unauthorized access, integrity failure): all constitutional assets are at risk. This is the only scenario warranting TOTAL contagion freeze. Recovery path: restore from git backup, verify integrity, audit for unauthorized changes.

### §6.6 GF Legal Ambiguity
GF currently has no formal legal existence. This means: publication revenue has no clear home, contractual commitments cannot be made in GF's name, and rights claims are uncertain. Fix: formalize GF as a program of AUPEI (simplest) or create a separate entity (more complex). ACTIVE kill switch.

### §6.7 Property Ownership Mismatch
Not yet applicable. When real property acquisition begins, the owning entity must align with intended use, tax treatment, and liability structure. A mismatch (e.g., nonprofit owning commercial property, or S-corp owning tax-exempt use property) creates downstream compliance and tax problems.

## §7. Director Decision Points

The following allocation decisions require R@ ruling:

1. **GF legal form** — program of AUPEI, DBA, LLC, or separate entity? (Affects rows: publications, GF workspace, domains, educational materials)
2. **Shared services terms** — at cost, below-market contribution, or reimbursed? (Affects rows: all DV-owned hardware used by AUPEI)
3. **IP assignment documentation** — has R@ formally assigned 7dU/GFUP/Nomos Logica IP to AUPEI? (Affects rows: all research IP, publications, patent potential)
4. **AUPEI board composition** — who sits alongside R@? (Affects: nonprofit governance compliance)
5. **Trademark registration priority** — which marks first? (Affects: brand protection timeline)
6. **Property ownership doctrine** — deferred, but entity architecture should anticipate it
7. **Sancho corpus handling** — privacy triage sequence confirmed? (Affects: ξ seat build timeline)

## §8. Interim Recommendations

### Immediate (next 30 days)
- Draft shared services agreement (DV↔AUPEI)
- Document IP assignment chain (R@ → AUPEI for research IP)
- Formalize GF as program of AUPEI (simplest near-term resolution)
- Begin trademark research on key marks

### Near-Term (next 90 days)
- AUPEI board expansion (identify 2 independent members)
- Service account audit and documentation
- Complete cap table reconciliation (DV-LEG-005)

### Deferred (6+ months)
- GF separate entity evaluation (if publication volume warrants)
- Real property doctrine development
- Patent evaluation for QEPE / Nomos Logica applications

## §9. Downstream Node Recommendations

- **DV-LEG-002** — Entity Relationship Architecture (formal relationship map between DV/AUPEI/GF)
- **DV-LEG-003** — Service Account / Device / Archive Custody Map (detailed inventory)
- **DV-LEG-004** — Legal Kill Switch Registry (expanded from §5 above)
- **DV-LEG-005** — Cap Table / Chain-of-Title Reconciliation (verify against primary docs)
- **DV-LEG-006** — IP Routing and Protection Matrix (detailed per-asset protection strategy)
- **DV-LEG-007** — Real Property / Academy Housing Trailhead (when ready)

## §10. Closure

### What this version resolves
- Structural allocation framework exists
- Trust tier model defined and applied
- Initial row assignments proposed for all major asset classes
- Legal kill switches identified with graduated contagion
- Director decision points surfaced and numbered
- Downstream node family defined

### What remains open
- Director rulings on §7 decision points
- Counsel review of tax and compliance implications
- Final entity assignments pending GF legal form decision
- Property doctrine
- Trademark registration specifics

### What requires Director ruling
- Q1-Q7 above

### What requires counsel
- Shared services agreement drafting
- IP assignment documentation review
- 501(c)(3) compliance implications of entity relationships
- Trademark registration strategy
