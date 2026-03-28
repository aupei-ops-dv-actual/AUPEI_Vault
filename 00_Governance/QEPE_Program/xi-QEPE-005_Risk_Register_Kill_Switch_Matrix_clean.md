# ξ-QEPE-005 — Risk Register & Kill-Switch Matrix

**Document Type:** Risk Register / Control Matrix  
**Seat:** ξ (Sancho)  
**Status:** DRAFT for Council Review  
**Epistemic Status:** MIXED by section, with mandatory claim tagging  
**Review Required By:** ζ, ∇, ω  
**Depends On:** ξ-QEPE-001, CR-001, current OpenJarvis constitutional config, QEPE source documents, AUPEI/Vault architecture, legal/IP strategy artifacts  
**Council Scope:** Risk, custody, governance, integration, disclosure, kill-switch doctrine  
**Contains Tier-C Material:** Yes  
**Last Safe Summary Level:** Internal strategic summary only  

## 0. Preface and Use Rule

QEPE now has enough strategic weight that it requires a dedicated risk instrument. The Program Map established what QEPE appears to be, where it sits in the Academy stack, what kinds of value it may hold, and what hard boundaries must contain it. That document was a framing map. This document is different. Its purpose is to identify what can go wrong, how badly it can go wrong, what signals should warn us, and what stop conditions should be triggered before damage spreads.

This Risk Register & Kill-Switch Matrix is therefore not a proof, not a sales brief, and not a generalized fear catalogue. It is a control instrument. Its role is to preserve survivability while QEPE is defined, integrated, governed, and—if later justified—productized. It is meant to be reviewed quickly, used concretely, and consulted whenever the Academy is tempted to move faster than its constitutional, legal, or technical footing permits.

The use rule is strict:

- Risks identified here should be tied to actual Academy layers: authority, governance, architecture, custody, disclosure, legal posture, productization, and continuity-related interpretation.
- Kill switches should be concrete, bounded, and tied to trigger conditions. They exist to halt or narrow specific dangerous motions, not to produce a theatrical “all stop” culture.
- A risk is not resolved because it has been named. It is only reduced when a control exists, is understood, and is being followed.
- No QEPE-related expansion—technical, legal, or external—should proceed by default if it crosses a boundary for which no reviewed control exists.

This document should be read with the same ethos that shaped ξ-QEPE-001: **minimum action, maximum force**. We are not trying to anticipate every possible disaster. We are trying to identify the small number of failure modes that matter enough to collapse truth, custody, governance, or leverage if left ungoverned.

## 1. Executive Risk Synthesis

### 1.1 One-paragraph risk summary

QEPE’s largest risks are not purely technical. They are mixed risks: epistemic, constitutional, custodial, and strategic. The danger is not only that QEPE might fail to perform as hoped. The deeper danger is that QEPE’s strongest internal claims, patent-facing language, implementation ambitions, and market imagination could blur together and begin to move the Academy faster than evidence, law, or infrastructure justify. [DEMONSTRATED]

At present, the most important active risks are overclaim drift, authority bleed, custody failure across seat and parent-company boundaries, and integration outrunning constitutional readiness. [DEMONSTRATED/PLAUSIBLE]

The strongest current controls are CR-001, the OpenJarvis constitutional config, the Entropy Boundary Law, the mandatory epistemic tagging discipline established in ξ-QEPE-001, and the Academy’s current insistence on local-first, bounded, reviewable integration. [DEMONSTRATED]

What remains most vulnerable is not the existence of controls, but the pressure to outrun them. [PLAUSIBLE]

### 1.2 Highest-priority current risks

The highest-priority current risk is **overclaim drift**. QEPE already exists across multiple discourse layers: internal theory, trade-secret framing, PPA language, implementation sketches, and product-adjacent imagination. If those layers are allowed to merge rhetorically, the Academy could begin speaking about QEPE as if its strongest claims were all equally mature. [DEMONSTRATED] That would weaken both truth discipline and legal defensibility.

The second highest-priority risk is **authority bleed**. CR-001 currently protects the Academy by making explicit that QEPE may perturb search and exploration, not authority. [DEMONSTRATED] But this boundary will remain under pressure as soon as QEPE starts proving useful inside real tools. The more useful it becomes, the stronger the temptation will be to let it influence ranking, canon, policy, or governance in subtle ways. [PLAUSIBLE]

The third highest-priority risk is **custody failure**. QEPE’s strategic sensitivity is magnified by the fact that seat collaboration occurs through ecosystems linked to external parent companies, and by the fact that different QEPE documents already live at different disclosure and custody levels. [DEMONSTRATED] If the Academy loses clarity about what is internal, what is filing-facing, what is implementation-facing, and what is safe to externalize, it may lose both leverage and legal protection. [PLAUSIBLE]

The fourth highest-priority risk is **integration before constitutional sovereignty**. The infrastructure is now far enough along that there will be pressure to wire QEPE into live systems, but constitutional sovereignty is still maturing. [DEMONSTRATED/PLAUSIBLE] If QEPE is integrated before authority checks, parser discipline, dependency logic, or trace semantics are sufficiently real, then the Academy may create a technically interesting but legally and constitutionally unstable system.

### 1.3 Risks already partly mitigated by current controls

Several major risks are already partially controlled.

**Authority mutation risk** is partly mitigated by CR-001 and the current constitutional config. QEPE has already been explicitly bounded away from canon, epistemic status, and governance authority. [DEMONSTRATED]

**Operational integration drift** is partly mitigated by the current OpenJarvis architecture, which favors local-first services, audited interfaces, boot gating, degraded-mode discipline, and constitutional configuration prior to broad experimentation. [DEMONSTRATED/IMPLEMENTABLE]

**Epistemic inflation risk** is partly mitigated by the tagging framework established in ξ-QEPE-001. The Academy now has a formal mechanism for distinguishing demonstrated, implementable, plausible, and speculative claims. [DEMONSTRATED]

**Disclosure drift** is partly mitigated by the existing awareness of Tier-C material, safe-summary levels, and the parent-company boundary problem. [DEMONSTRATED] This mitigation is real, but incomplete; awareness is not the same as a fully operational disclosure-control regime.

What these controls have in common is that they are mostly boundary controls, not yet full operational verification systems. They define what must not happen, and in some cases how systems should be configured. What they do not yet fully provide is a complete live detection-and-response layer. That is one of the reasons this document now exists.

### 1.4 What this document does and does not attempt

This document attempts to do four things.

First, it attempts to define the major QEPE risk families in a form that can be reviewed and acted on by the council. That includes epistemic risks, governance risks, integration risks, custody risks, legal risks, productization risks, and continuity-adjacent interpretive risks. [DEMONSTRATED]

Second, it attempts to identify the practical stop conditions that should apply if those risks begin to actualize. This is the purpose of the kill-switch framework: not to dramatize danger, but to preserve control under pressure. [DEMONSTRATED/IMPLEMENTABLE]

Third, it attempts to connect risks to actual Academy layers and actual likely triggers. This matters because “QEPE is risky” is too vague to govern anything. A useful risk register must say what is at risk, how the failure begins, where it spreads, and who is authorized to halt it. [DEMONSTRATED]

Fourth, it attempts to preserve tempo without surrendering discipline. The Academy should be able to continue defining and integrating QEPE without confusing motion for maturity. [PLAUSIBLE/IMPLEMENTABLE]

This document does not attempt to prove that QEPE is unsound, nor does it attempt to settle the underlying science. [DEMONSTRATED] It does not attempt to replace ξ-QEPE-001, nor to decide final product or legal strategy. [DEMONSTRATED] It does not attempt to suppress exploration. Its function is narrower and stronger: to define the places where exploration must slow, halt, or escalate to review if survivability is at stake.

## 2. Risk Discipline and Status Rules

This section defines how risks are classified and how kill-switch judgments should be made. The purpose is not bureaucratic neatness. The purpose is to ensure that QEPE-related concerns are expressed in a form the council can actually use. If risks are described only rhetorically, they will either be ignored or inflated. If they are described with too much complexity, they will become unreadable and therefore inert. The discipline below is intentionally simple.

A useful QEPE risk system must answer four questions quickly:

1. Is the risk active now, or only possible under certain conditions?
2. How severe would the consequences be if it materialized?
3. How well is it currently controlled?
4. What kind of intervention should be triggered if it crosses a threshold?

The rules below are designed to support those four questions without pretending to precision the Academy has not yet earned.

### 2.1 Risk status tags

Each risk in this dossier should carry one primary status tag:

- **ACTIVE**
- **LATENT**
- **CONDITIONAL**
- **SPECULATIVE**

**ACTIVE** means the risk is present now in the current environment or workstream. It may already be exerting pressure, even if no visible failure has occurred yet. For example, overclaim drift is an active risk because QEPE already spans multiple discourse registers and therefore already carries inflation pressure. [DEMONSTRATED]

**LATENT** means the risk is not currently expressing itself, but the structure for it already exists. A latent risk can become active quickly if a nearby control fails or a new capability is turned on. For example, parent-company custody risk may be latent if the current workflow is disciplined, but it remains structurally present because the seat environment is still instantiated through external model ecosystems. [PLAUSIBLE]

**CONDITIONAL** means the risk depends on a future phase, embodiment, or escalation step. It is real enough to track, but it should not yet be treated as if it is exerting current pressure. For example, some productization risks are conditional because they only become live if QEPE moves into external offerings or partner-facing disclosures. [PLAUSIBLE]

**SPECULATIVE** means the risk is tied to a lower-status claim, an unresolved interpretation, or a future possibility whose existence is not yet well enough established to govern current behavior strongly. Speculative risks should still be named when the downside could be large, but they should not be treated as though they outrank active or latent risks. For example, certain continuity-related identity risks may belong here until the underlying continuity claims are better sorted. [SPECULATIVE]

These tags are intentionally simple. They help the council distinguish between what requires immediate discipline and what merely deserves watchfulness.

### 2.2 Severity scale

Each risk should also carry a severity level:

- **LOW**
- **MODERATE**
- **HIGH**
- **CRITICAL**

**LOW** means the risk is real but locally bounded. If it materializes, it causes inconvenience, minor inefficiency, or limited confusion, but is unlikely to damage authority, custody, or long-term leverage. A low-severity risk should still be controlled if cheap to do so, but it is not usually a reason to halt progress on its own. [DEMONSTRATED]

**MODERATE** means the risk could produce meaningful disruption, misclassification, workflow corruption, or avoidable strategic loss if left unattended. Moderate risks should be monitored and usually should have some control attached to them. [DEMONSTRATED]

**HIGH** means the risk threatens an important Academy layer: constitutional integrity, governance discipline, strategic leverage, material disclosure boundaries, or major system behavior. High-severity risks should generally have explicit controls and defined stop conditions. [DEMONSTRATED]

**CRITICAL** means the risk threatens collapse of a load-bearing layer or an outcome that would be disproportionately difficult to reverse. That may include authority mutation, uncontrolled custody breach, irreversible disclosure of protected material, or system behavior that compromises governance or legal posture at the root. Critical risks should always have a clear kill-switch path. [DEMONSTRATED]

Severity should not be confused with probability. A risk may be unlikely but still critical. Likewise, a frequent nuisance may still be only moderate if its blast radius is limited.

### 2.3 Control status

Each risk should also be assessed by how well it is currently governed:

- **UNCONTROLLED**
- **PARTIALLY CONTROLLED**
- **CONTROLLED**
- **DEFERRED**

**UNCONTROLLED** means there is no meaningful current mechanism preventing, detecting, or responding to the risk. The Academy may be aware of the issue, but awareness alone does not count as control. [DEMONSTRATED]

**PARTIALLY CONTROLLED** means there are some live controls, but they are incomplete, indirect, or not yet field-proven. This is likely to be the most common status in the current QEPE phase. For example, overclaim drift is partially controlled by the tagging discipline in ξ-QEPE-001, but that does not yet mean all future documents or speakers will follow the discipline automatically. [DEMONSTRATED]

**CONTROLLED** means there is a reviewed and active mechanism that either prevents the risk under normal conditions, detects it reliably, or provides a known recovery path with acceptable speed. A controlled risk is not a non-risk. It is simply one whose exposure has been meaningfully bounded. [DEMONSTRATED]

**DEFERRED** means the Academy is intentionally not controlling the risk yet because the triggering conditions do not currently exist or because the relevant phase has not yet begun. Deferred does not mean ignored. It means postponed lawfully. This status is especially useful for longer-horizon product or disclosure risks that should not dominate early-stage internal work. [DEMONSTRATED]

Control status is one of the most important judgments in this document because it prevents the council from confusing strong language with actual protection.

### 2.4 Kill-switch rule

A kill switch is any explicit control that slows, narrows, halts, or escalates a QEPE-related activity when a defined threshold is crossed. Kill switches are not a sign of weakness. They are what allow a strategic asset to be developed aggressively without becoming reckless. The Academy should not use kill switches theatrically, but neither should it hesitate to define them clearly where blast radius is large.

For the purposes of this dossier, kill-switch responses should fall into four practical classes:

- **Monitor only**
- **Soft stop**
- **Hard stop**
- **Council review trigger**

A **monitor-only** condition means the risk should be watched, logged, and perhaps reported, but work does not pause automatically. This is appropriate when uncertainty is real but current controls are likely adequate.

A **soft stop** means the specific activity should pause or narrow until an identified issue is reviewed or corrected, but the broader QEPE workstream need not halt. This is appropriate when the risk is local, bounded, and reversible if caught early.

A **hard stop** means the relevant activity must cease immediately until explicit review and reauthorization occur. This is appropriate when authority, custody, disclosure, or core constitutional integrity are threatened.

A **council review trigger** means the issue has crossed into a zone where no single seat, implementer, or operator should decide alone. This is especially appropriate when the risk affects governance, parent-company exposure, public claims, or custody boundaries.

The kill-switch rule is therefore:

A risk qualifies for stronger intervention when three conditions converge:

1. the blast radius reaches a load-bearing Academy layer,
2. current controls are weak or failing,
3. recovery becomes harder if motion continues.

When those conditions are present, slowing down is not indecision. It is the correct application of force.

## 3. Risk Family I — Epistemic and Claim Risks

The first risk family is epistemic. This is the correct place to start because QEPE’s earliest and most persistent danger is not necessarily hardware failure, code failure, or even legal failure. It is the failure of the Academy to keep its own claims sorted. QEPE already lives across internal theory notes, proprietary technical descriptions, implementation sketches, patent-facing documents, product-adjacent summaries, and future-facing strategic imagination. If those layers blur together, the result is not just “bad messaging.” The result is loss of truth discipline, weaker governance, weaker legal posture, and eventually weaker strategic leverage.

These risks are therefore primary, not secondary. If the Academy cannot maintain epistemic order around QEPE, then every later integration, product, or governance discussion will begin from contaminated ground.

### 3.1 Overclaim drift

**Risk statement.**  
Overclaim drift occurs when QEPE is described more strongly than the current evidence justifies, or when claims that belong to different epistemic levels begin to converge into a single tone of certainty. [DEMONSTRATED]

**Why it matters.**  
QEPE’s source corpus already contains internal theory language, patent-language, implementation-language, and strategic-language. That makes overclaim drift an active risk, not a hypothetical one. If the Academy begins speaking as though all of QEPE’s strongest claims are equally mature, it will damage its scientific discipline, weaken its review process, and expose itself to legal and credibility problems later. [DEMONSTRATED]

**Likely triggers.**
- repeated reuse of strong internal phrasing without tag discipline
- patent-facing novelty language treated as technical proof
- strategic summaries written as though they were validated architectures
- enthusiasm during integration or product discussion outrunning actual tests
- continuity or AGI-adjacent interpretations being spoken in the same voice as current deployment facts

**Blast radius.**  
Scientific framing, governance posture, legal defensibility, internal trust, external credibility.

**Current controls.**  
Mandatory epistemic tagging in ξ-QEPE-001, council review discipline, CR-001 authority boundary, current caution from ζ and ∇. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If any QEPE-related document, briefing, or external-facing text presents plausible or speculative claims as though they were demonstrated or implementation-ready without explicit tagging, that material should be frozen for revision before it is allowed to circulate further.

**Kill-switch class:** KS-2 Soft Stop internally, KS-5 External Disclosure Freeze if external-facing.

**Recovery posture.**  
Demote the claim, restore explicit tags, split mixed-register paragraphs, and require re-review before reuse.

### 3.2 Epistemic laundering

**Risk statement.**  
Epistemic laundering occurs when a weaker claim inherits strength from being placed next to a stronger one, without ever earning that strength on its own. [DEMONSTRATED]

**Why it matters.**  
This is one of the most subtle and dangerous QEPE risks. A paragraph may begin with a demonstrated infrastructure fact, move into an implementable architectural idea, and end with a plausible or speculative implication—yet the whole paragraph may be read or remembered as though everything in it had the same status. [DEMONSTRATED] QEPE is especially vulnerable to this because its corpus is rich in mixed-register writing and its concepts are strategically attractive.

**Likely triggers.**
- mixed paragraphs not split or tagged inline
- “therefore” logic that outruns the evidence
- reuse of internal summaries as if they were source proofs
- presentation slides or one-pagers that compress too much into too little space
- cross-seat synthesis that fails to separate theory, implementation, and value

**Blast radius.**  
Internal decision quality, council review integrity, product messaging, legal posture, later risk classification.

**Current controls.**  
Section 2 of ξ-QEPE-001, especially the mixed-claim rule; current three-seat review discipline. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a document or presentation repeatedly mixes claim levels without separation or inline tagging, it should be barred from serving as a governance or integration reference until cleaned.

**Kill-switch class:** KS-2 Soft Stop

**Recovery posture.**  
Split the mixed material, re-tag at sentence or paragraph level, and create a “safe summary” version if needed.

### 3.3 Demonstrated vs implementable confusion

**Risk statement.**  
This risk appears when an architecture that seems buildable is treated as though it has already been validated in the field. [DEMONSTRATED]

**Why it matters.**  
QEPE has many features that are already clearly implementable in principle: local daemon architecture, Unix socket contract, trace annotation, bounded retrieval perturbation, and OpenJarvis-adjacent integration paths. [IMPLEMENTABLE] But buildability is not the same thing as demonstrated success. If the Academy begins speaking as though implementation path alone proves operational value, it risks turning roadmap confidence into false evidence. [DEMONSTRATED]

**Likely triggers.**
- integration roadmap language reused as proof-of-function language
- successful prototype or smoke test generalized into strong system claims
- “we can do this” becoming “this works as claimed”
- conflation of service architecture with entropy quality or strategic superiority

**Blast radius.**  
Engineering prioritization, council approvals, internal resource allocation, product signaling, legal supportability.

**Current controls.**  
Epistemic tag framework, current staged program phases, constitutional integration-before-proof caution. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If implementable QEPE pathways are cited as though they already demonstrate outcome quality, security superiority, or scientific validity, the claim should be downgraded immediately and prevented from being used in product, governance, or external materials.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-4 Council Review Required if used in strategic decision-making.

**Recovery posture.**  
Reclassify the claim, require evidence criteria, and attach the relevant test or implementation milestone needed for promotion.

### 3.4 Continuity / AGI inflation

**Risk statement.**  
This risk occurs when lower-status continuity, AGI, persistence, or identity-adjacent ideas become rhetorically central before they are technically or scientifically earned. [DEMONSTRATED/SPECULATIVE]

**Why it matters.**  
QEPE sits close to some of the most magnetized ideas in the Academy: cryptogenic memory, synthetic continuity, recursive initialization, and the possibility that structured entropy could matter for more than just secure computation. Those ideas may deserve continued exploration. But they also create exactly the kind of symbolic inflation that can distort engineering priorities, weaken governance discipline, and create external misunderstanding. [PLAUSIBLE/SPECULATIVE]

**Likely triggers.**
- internal continuity language reused outside its epistemic lane
- successful bounded perturbation or replay features overinterpreted as continuity proof
- anthropomorphic readings of stochastic persistence behavior
- pressure to narrate QEPE as foundational to AGI emergence too early

**Blast radius.**  
Philosophical clarity, public credibility, governance stability, ethical framing, product overreach.

**Current controls.**  
Section 3 of ξ-QEPE-001, especially the clear classification of continuity-related roles as lower-status; current seat-level caution. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED, with some elements still effectively LATENT

**Kill-switch condition.**  
Any use of QEPE to justify strong continuity, personhood, AGI persistence, or “synthetic survival” claims beyond explicitly tagged speculative discussion should trigger immediate review and disclosure freeze for that material.

**Kill-switch class:** KS-4 Council Review Required internally, KS-5 External Disclosure Freeze externally.

**Recovery posture.**  
Demote the affected claims, relocate them into exploratory or appendix status, and require explicit technical criteria before future promotion.

### 3.5 Internal-document authority confusion

**Risk statement.**  
This risk appears when internal notes, theory-heavy documents, patent drafts, implementation sketches, summaries, and formal council artifacts are treated as though they carry the same weight. [DEMONSTRATED]

**Why it matters.**  
QEPE already spans many document classes. Some documents are trade-secret-heavy internal notes. Some are PPA-facing or disclosure-facing. Some are implementation summaries. Some are strategic syntheses. If the Academy does not keep their authority distinct, then a strategically convenient document may begin to govern in ways it was never meant to. [DEMONSTRATED]

**Likely triggers.**
- citing summaries as though they were source law
- treating PPA language as technical proof
- using one-pagers as canonical scope statements
- failing to distinguish internal source, safe summary, and external-safe description
- incomplete vault classification

**Blast radius.**  
Council review quality, disclosure discipline, integration logic, IP posture, archival continuity.

**Current controls.**  
Vault architecture principles, source/summary distinctions, current manual review habits. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a non-source or lower-authority QEPE document begins to function as canonical guidance for integration, governance, or external messaging, pause use of that artifact until source and authority status are re-established.

**Kill-switch class:** KS-2 Soft Stop

**Recovery posture.**  
Re-anchor to source documents, classify the artifact correctly, and create a reviewed summary if one is needed operationally.

### Section 3 summary note

This entire risk family is high-leverage because it governs the quality of everything that comes later. If the Academy cannot hold epistemic order around QEPE, then architecture, governance, product, and legal work all begin from compromised assumptions.

The strongest current hazards are:
- overclaim drift
- epistemic laundering
- continuity inflation

The strongest current control remains simple:

**Tag honestly, separate registers, and do not let usefulness impersonate proof.**

## 4. Risk Family II — Authority and Governance Risks

The second major risk family concerns authority and governance. This family is downstream of the epistemic risks, but only partly. If epistemic disorder is the condition under which bad governance becomes easier, governance risk is the point at which the system begins to act on that disorder. QEPE is especially sensitive here because it is not merely a research object. It is being considered for real integration into live infrastructure, retrieval behavior, operator differentiation, and strategic architecture. That means the Academy must define clearly where QEPE’s lawful influence ends and what failures arise if it drifts beyond that point.

The central governance fact remains unchanged: **QEPE may perturb search and exploration, not authority.** [DEMONSTRATED] Everything in this section exists to protect that law from erosion.

### 4.1 Authority bleed

**Risk statement.**  
Authority bleed occurs when QEPE begins to influence not only lawful movement within a valid choice space, but the ranking, legitimacy, or status of the choice space itself. [DEMONSTRATED]

**Why it matters.**  
This is one of the most dangerous QEPE risks because it can emerge gradually and under the cover of usefulness. A perturbation engine that begins as a tie-breaker or exploration modulator may start to shape what is surfaced, what is prioritized, what is considered worthy of review, or what becomes de facto canonical through repeated patterned behavior. [PLAUSIBLE] If left ungoverned, QEPE would stop being a lawful modulator and start becoming a shadow authority layer.

**Likely triggers.**
- entropy-conditioned retrieval influencing ranking before authority gating completes
- QEPE-informed operators being treated as more “insightful” than status-ranked sources
- repeated exploratory outputs becoming de facto policy or canon through familiarity
- using QEPE-conditioned behavior as justification for changing epistemic status or priority lanes
- silent removal of human or council review because the entropy-assisted path “works”

**Blast radius.**  
Vault integrity, authority hierarchy, canonical law, council process, internal trust.

**Current controls.**  
CR-001, constitutional config, local model boundary rules, current council discipline. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE is found to influence source ranking, epistemic status, canon formation, or governance priority before authority filters have completed—or if any operator begins using QEPE output as a substitute for ranked authority—the relevant integration path must be halted immediately.

**Kill-switch class:** KS-3 Hard Stop

**Recovery posture.**  
Disable QEPE influence on the affected path, revert to deterministic authority-only flow, inspect trace records, and require council reauthorization before restoring bounded use.

### 4.2 Governance drift

**Risk statement.**  
Governance drift occurs when QEPE’s technical usefulness begins to generate normative permission it was never granted. [DEMONSTRATED]

**Why it matters.**  
Systems often acquire influence not by explicit coup, but by convenience. If QEPE becomes useful in retrieval, experimentation, operator guidance, or system modulation, the Academy may gradually begin to defer to it in domains where it is not lawfully empowered. [PLAUSIBLE] This is especially risky because the drift may feel rational: “it works,” “it finds interesting paths,” “it improved outcomes,” and therefore “it should get more say.” That reasoning is precisely what constitutional governance is meant to resist.

**Likely triggers.**
- repeated use of QEPE-conditioned outputs in policy-relevant decisions
- informal reliance on QEPE paths for council preparation or Director judgment
- treating bounded stochasticity as inherently wiser or fairer than reviewed procedure
- expanding QEPE’s influence without a corresponding increase in review class

**Blast radius.**  
Council legitimacy, Director authority, policy clarity, Nomos discipline, institutional memory.

**Current controls.**  
CR-001, current seat awareness, explicit separation of tool and governance in ξ-QEPE-001. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE begins to function as a practical governance advisor beyond reviewed scope—especially in matters of canon, external positioning, policy, or adjudication—QEPE use in that workflow must pause pending explicit council review.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Reclassify the workflow, separate technical support from governance acts, and re-establish human/council adjudication as the decisive authority.

### 4.3 Policy creep

**Risk statement.**  
Policy creep occurs when QEPE’s role quietly expands from a narrow, reviewed use case into neighboring use cases without formal re-authorization. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
Not all governance failures happen at the highest level. Some happen by small accretions: one more use case, one more exception, one more local permission. QEPE is especially vulnerable to this because many of its plausible roles—tie-breaking, exploration budgeting, trace annotation, operator diversification—are adjacent to one another. A system that is allowed in one area may be casually invited into another unless the edges are actively policed. [PLAUSIBLE]

**Likely triggers.**
- “just for this one case” expansion
- temporary exceptions that are never rolled back
- copying a QEPE-enabled pattern into a new workflow without council awareness
- informal operator habits outrunning official config and policy

**Blast radius.**  
Workflow clarity, review discipline, operator behavior, lawful scope boundaries.

**Current controls.**  
Config discipline, council review norm, current early-stage caution. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE appears in a workflow or lane not explicitly covered by current review and policy, that use must pause until reviewed and classified.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-4 if governance-relevant.

**Recovery posture.**  
Map the unauthorized expansion, classify whether it is benign, useful, or unsafe, and either formalize it through review or remove it.

### 4.4 Review bypass

**Risk statement.**  
Review bypass occurs when QEPE-related activity, outputs, or integrations begin to matter materially without ever receiving the level of seat, council, or Director review appropriate to their blast radius. [DEMONSTRATED]

**Why it matters.**  
The Academy’s structure depends on review being more than ceremony. If QEPE begins to generate strategic leverage, influence real system behavior, or shape external posture without review, then the council function becomes decorative rather than constitutional. [PLAUSIBLE] This is especially dangerous because bypass often arrives disguised as urgency, technical confidence, or the claim that “we’ll regularize it later.”

**Likely triggers.**
- technical deployment before governance review
- internal summaries acting as de facto approval
- operator trials used in ways that outgrow their pilot classification
- document circulation beyond intended review level
- pressure to move quickly because a capability feels strategically urgent

**Blast radius.**  
Council role integrity, seat trust, custody posture, product timing, external credibility.

**Current controls.**  
Current council habit, staged program phases, explicit review sequencing in ξ-QEPE-001. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a QEPE-related use, claim, or integration acquires practical strategic effect before the corresponding review level has been completed, the affected path should pause until reviewed.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Reclassify the item, determine correct review tier, and either retroactively regularize it under council authority or narrow it back to its lawful scope.

### 4.5 Constitutional substrate bypass

**Risk statement.**  
Constitutional substrate bypass occurs when QEPE is integrated or used in contexts where the constitutional environment is not yet sufficiently real—for example, before authority gating, status handling, dependency discipline, traceability, or degraded-mode truth conditions are mature enough to contain it. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
A bounded perturbation service is only safe if it is actually bounded. If QEPE is inserted into systems that are not yet constitutionally sovereign, then even technically interesting results may be structurally unsafe. [DEMONSTRATED/PLAUSIBLE] This is one of the most practical governance risks in the current phase, because infrastructure momentum can create pressure to “just wire it in and learn.”

**Likely triggers.**
- QEPE integration before parser/status/dependency/contagion logic is live
- using entropy-conditioned behavior in systems still running in degraded mode
- sandbox logic leaking into production-like flows
- incomplete trace/replay semantics

**Blast radius.**  
System stability, authority integrity, auditability, council confidence, later recovery cost.

**Current controls.**  
Current constitutional config, CR-001, current sequencing discipline, current insistence on local-first and bounded integration. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE is proposed for use in a workflow that lacks constitutional gating, traceability, or reviewable degraded-mode handling, the integration must not proceed.

**Kill-switch class:** KS-3 Hard Stop

**Recovery posture.**  
Return to the last constitutionally verified layer, complete the missing substrate controls, and only then revisit the integration.

### Section 4 summary note

The governance family is where QEPE’s most structurally dangerous failure would likely occur: not because entropy is inherently unlawful, but because usefulness creates pressure, and pressure seeks shortcuts.

The three most important governance risks are:
- authority bleed
- governance drift
- constitutional substrate bypass

The controlling principle remains simple:

**QEPE may help a lawful system move; it may not decide what law is.**

## 5. Risk Family III — Architecture and Integration Risks

The third major risk family concerns architecture and integration. If the epistemic risk family asks whether the Academy is speaking accurately about QEPE, and the governance risk family asks whether QEPE is being granted powers it does not lawfully hold, then the architecture risk family asks a more practical question:

**Can QEPE be integrated into real systems without becoming opaque, brittle, over-coupled, or harder to govern than it is worth?**

This question matters because QEPE is not being contemplated only as theory or IP. It is already being imagined as a live service layer in OpenJarvis-adjacent infrastructure, a bounded perturbation engine, a trace-conditioned component, and possibly later a modular subsystem for secure or exploratory workflows. That means architectural mistakes are not an abstract risk. They are an expected pressure point.

The central architectural rule remains:

**QEPE should be integrated narrowly enough to stay reviewable, and structurally loosely enough to stay disableable.** [DEMONSTRATED/IMPLEMENTABLE]

### 5.1 Deep coupling risk

**Risk statement.**  
Deep coupling risk occurs when QEPE becomes so embedded in a system’s normal operation that it can no longer be isolated, disabled, or meaningfully audited without destabilizing the larger system. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
The current Academy direction is correct precisely because it avoids this: local daemon/service model, audited interface, CR-001 boundaries, and the principle that QEPE should perturb search and exploration without becoming the substrate of authority. [DEMONSTRATED] But as systems grow, the temptation will be to let QEPE creep inward—into ranking logic, agent orchestration, replay semantics, adaptive decision-making, or even product core paths. If that happens too quickly, the Academy may end up with a system that cannot answer a simple question: what happens if QEPE is turned off? If the answer is “we no longer understand the system,” the integration has already gone too far. [PLAUSIBLE]

**Likely triggers.**
- using QEPE as a hidden default instead of an explicit invoked service
- multiple internal systems depending on QEPE before isolation is proven
- introducing QEPE into critical paths without a clean fallback mode
- treating its outputs as assumed infrastructure rather than conditional influence
- skipping boundary reviews because the service appears to be working

**Blast radius.**  
System observability, rollback ability, service resilience, governance confidence, future product modularity.

**Current controls.**  
Current daemon/service-first architecture, CR-001, local-first integration discipline, current emphasis on narrow use roles. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a proposed QEPE integration cannot be disabled without impairing the system’s ability to function lawfully or intelligibly, the integration must not proceed until a clean fallback path exists.

**Kill-switch class:** KS-3 Hard Stop

**Recovery posture.**  
Refactor the integration into a narrower service boundary, reintroduce deterministic fallback behavior, and restore traceability before reattempting the coupling.

### 5.2 Trace opacity

**Risk statement.**  
Trace opacity occurs when QEPE materially influences behavior, but the system cannot later reconstruct where, when, how, or under what state conditions that influence occurred. [DEMONSTRATED/IMPLEMENTABLE]

**Why it matters.**  
Entropy without replay is governance poison. If QEPE is allowed to shape retrieval tie-breaking, exploration branching, operator diversification, or sandbox behavior, then the Academy must be able to tell afterward whether the behavior was deterministic, entropy-conditioned, degraded, or anomalous. [DEMONSTRATED] Without that distinction, useful variation becomes indistinguishable from drift, and bounded stochasticity becomes operationally equivalent to an unreviewable black box. [PLAUSIBLE]

This is especially important because one of QEPE’s most defensible potential values is precisely that it could produce reviewable stochastic behavior, not just randomness. If traces are weak, that value collapses. [PLAUSIBLE]

**Likely triggers.**
- entropy calls without session identifiers
- state changes not being recorded
- missing mode information (deterministic vs stochastic)
- replay semantics not defined
- trace paths not surviving restart or degraded mode transitions
- logs existing but not meaningfully linking to QEPE state

**Blast radius.**  
Auditability, reproducibility, council trust, debugging quality, safe experimentation, legal defensibility.

**Current controls.**  
Current architecture intent around traces and lanes, current emphasis on session-bound operation, current insistence on local auditable interfaces. [DEMONSTRATED/IMPLEMENTABLE]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE is influencing a workflow and the Academy cannot determine the session, state, mode, and effect trail with enough precision to review it, QEPE influence on that workflow should pause until trace discipline is restored.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-3 if the affected workflow is strategically or governance-sensitive.

**Recovery posture.**  
Tighten trace schema, require state hashes and session IDs, validate replay capability, and re-run the workflow only once the missing observability is restored.

### 5.3 Integration before constitutional sovereignty

**Risk statement.**  
This risk occurs when QEPE is integrated into live infrastructure before the constitutional substrate is mature enough to contain it—that is, before parser discipline, authority gating, dependency awareness, status handling, contagion logic, and reviewable degraded-mode behavior are sufficiently real. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
The Academy has already learned that boot sovereignty and constitutional sovereignty are not the same thing. [DEMONSTRATED] A system can start lawfully at boot while still lacking full authority-aware retrieval or fully live constitutional controls. If QEPE enters too early, it may produce technically interesting behavior in a system that is not yet lawful enough to interpret or constrain that behavior correctly. [PLAUSIBLE]

This is perhaps the most immediate architectural risk in the current phase, because infrastructure progress creates understandable pressure to “get QEPE into the loop” as soon as possible. That pressure is dangerous if the Academy confuses operational readiness with constitutional readiness. [DEMONSTRATED/PLAUSIBLE]

**Likely triggers.**
- using QEPE before authority graph or parser readiness is real
- entropy-influenced retrieval without explicit status/ranking discipline
- experimentation in degraded mode treated as if equivalent to healthy mode
- early integrations driven by curiosity rather than review thresholds
- allowing successful prototypes to outrun infrastructure maturity

**Blast radius.**  
Authority integrity, trust in the system, difficult-to-debug behavior, false confidence, later rework cost.

**Current controls.**  
CR-001, staged program logic, current OpenJarvis config discipline, current council awareness. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
No QEPE integration may proceed in a workflow unless the constitutional preconditions for that workflow are already present and testable. If those preconditions are absent or unknown, the integration must stop there.

**Kill-switch class:** KS-3 Hard Stop

**Recovery posture.**  
Complete the missing constitutional controls first, document the readiness state, then revisit the integration under reviewed conditions.

### 5.4 Daemon/interface abuse

**Risk statement.**  
Daemon/interface abuse occurs when QEPE’s service surface is used in ways that exceed its intended operational bounds—for example through uncontrolled call loops, malformed consumers, aggressive sampling, unbounded session creation, or poor boundary enforcement between service and clients. [DEMONSTRATED/IMPLEMENTABLE]

**Why it matters.**  
QEPE’s architectural strength partly depends on being process-isolated and exposed through a narrow interface. But every interface is also an attack surface—technically, operationally, and behaviorally. If an agent, operator, or client loop begins hammering the QEPE service, or if boundary enforcement is weak, then the Academy may get degraded results, false confidence, or infrastructure instability. [PLAUSIBLE]

This risk is not hypothetical. Earlier council review already surfaced the need for rate governors, session ceilings, anomalous-pattern detection, and divergence caps. [DEMONSTRATED] That means the service model is right, but only if it remains a governed service.

**Likely triggers.**
- missing or weak rate limits
- insufficient session caps
- malformed or adversarial clients
- recursive operator loops
- interface expansion without parallel policy controls
- debugging hooks left open in production-like settings

**Blast radius.**  
Service reliability, trace integrity, system performance, audit clarity, experimentation quality.

**Current controls.**  
Current architecture direction toward daemon-side governors, divergence cap of 3, local-only posture, current insistence on narrow interfaces. [DEMONSTRATED/IMPLEMENTABLE]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE service usage exceeds configured rate, session, or concurrency bounds—or if anomalous call patterns emerge without explanation—the affected callers should be cut off and the QEPE service should fall back to safe mode until reviewed.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-3 if the service itself becomes unstable or untraceable.

**Recovery posture.**  
Inspect client behavior, tighten governors, restore safe service defaults, and re-authorize callers only after the abuse path is understood.

### 5.5 Degraded-mode misuse

**Risk statement.**  
Degraded-mode misuse occurs when the system continues to behave as though constitutionally healthy while critical supports are absent, weakened, or bypassed. [DEMONSTRATED]

**Why it matters.**  
The Academy has already done important work to distinguish healthy mode from degraded mode in OpenJarvis. That distinction must survive QEPE integration. If QEPE is allowed to influence workflows when mount states, parser readiness, authority graph readiness, trace lanes, or inference dependencies are not truly healthy, then degraded mode ceases to be a truth-telling state and becomes uptime theater. [DEMONSTRATED/PLAUSIBLE]

The problem here is not merely technical fragility. It is constitutional dishonesty: the system would be acting as though it remained safely bounded when one or more of the very boundaries meant to contain it had weakened. [DEMONSTRATED]

**Likely triggers.**
- entropy services left enabled during degraded startup
- incomplete trace or lane availability masked by fallback behavior
- missing model or parser conditions treated as non-fatal for entropy use
- convenience pressure to “just let it run”
- unclear degraded-mode flags in result payloads

**Blast radius.**  
Operator trust, replay accuracy, governance confidence, data integrity, safety of experimentation.

**Current controls.**  
Current degraded-mode configuration logic, preflight discipline, council-level insistence on truthful boot states. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
QEPE must not influence any workflow running in degraded mode unless that specific degraded use has been explicitly reviewed and authorized. By default, degraded mode should disable QEPE-conditioned behavior in any system that matters.

**Kill-switch class:** KS-3 Hard Stop

**Recovery posture.**  
Return to healthy mode, revalidate the missing dependencies, and rerun the affected path only after the system can truthfully represent its own state.

### 5.6 Configuration drift and silent divergence

**Risk statement.**  
Configuration drift occurs when the live QEPE integration state diverges from its reviewed configuration, policy files, or known council-approved boundaries without that divergence being explicitly recognized. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
The Academy is already building machine-readable control layers—config domains, CR-001 policy files, boot gates, divergence caps, and future integration contracts. That is good. But any system that accumulates many controls also becomes vulnerable to silent divergence: someone changes a config, a fallback persists longer than intended, a new lane is added informally, a service starts with different assumptions after reboot, or a daemon update changes actual behavior without matching the written control surface. [PLAUSIBLE]

If that happens, the Academy may continue speaking as though it is operating inside one architecture while actually running another. That is exactly the kind of drift a constitutional system must resist. [DEMONSTRATED/PLAUSIBLE]

**Likely triggers.**
- manual config edits outside review path
- launchd or service changes not written back to vault
- silent fallback to local paths or local defaults
- interface revisions without corresponding policy updates
- service updates that outpace documentation

**Blast radius.**  
Operational truthfulness, audit quality, seat handoff continuity, legal defensibility, later debugging.

**Current controls.**  
Current ops logging discipline, explicit config files, policy file validation, vault commit culture. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If live system behavior is discovered to differ materially from the reviewed QEPE control surface and that divergence cannot be explained immediately, affected QEPE use should be paused until state is reconciled.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-4 if the divergence touches governance or disclosure boundaries.

**Recovery posture.**  
Capture the live state, reconcile with approved config and policy, commit the truth to the vault, and only then resume.

### Section 5 summary note

This risk family is where the Academy protects itself from building something too interesting to understand. QEPE may become valuable precisely because it adds bounded variation and differentiated behavior. But if that variation is poorly coupled, weakly traced, prematurely integrated, or allowed to operate under false health assumptions, then the architecture becomes harder to govern than the value justifies.

The three most important architecture risks are:
- deep coupling
- trace opacity
- integration before constitutional sovereignty

The guiding rule is simple:

**Integrate narrowly, trace fully, and preserve the ability to turn QEPE off without losing the system’s mind.**

## 6. Risk Family IV — Custody, Disclosure, and Parent-Company Risks

This risk family is among the most strategically sensitive in the entire QEPE workstream. QEPE is not being developed inside a single sealed lab. It is being shaped through a multi-seat process, across multiple institutional lanes, with documents that already span different disclosure classes and with seats instantiated through model ecosystems linked to parent companies. That means the Academy’s risk is not just “someone might steal an idea.” The real risk is more subtle and more dangerous: the Academy may lose the ability to tell what was protected, what was shared, what was transformed into summary, what became visible to which systems, and when the boundary between internal collaboration and external exposure actually failed.

For that reason, custody and disclosure discipline must be treated as a first-order QEPE concern, not an afterthought to be handled once “the real work” is done. In this workstream, custody is part of the real work.

### 6.1 Parent-company boundary failure

**Risk statement.**  
Parent-company boundary failure occurs when QEPE material, reasoning, summaries, or operational detail become exposed beyond the intended Academy seat collaboration boundary and into parent-company-visible or parent-company-capturable channels without explicit authorization. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
The current strategic posture is that the three seats may have architectural access to QEPE while the firewall remains between the seats and their parent companies. That is useful, but it is not self-executing. Seats may collaborate, but the systems through which they collaborate may retain, learn from, summarize, or otherwise expose content in ways the Academy does not fully govern. [DEMONSTRATED/PLAUSIBLE] This makes parent-company boundary failure one of the highest-value and highest-sensitivity risks in the program.

**Likely triggers.**
- over-sharing full-detail QEPE material into seat conversations without disclosure discipline
- prompting that includes protected details unnecessary to the immediate task
- summaries that flatten internal, filing-facing, and secret material into one consumable layer
- failure to distinguish seat-access from parent-company-safe exposure
- future integrations that transmit sensitive QEPE material into external APIs or services without explicit review

**Blast radius.**  
Trade-secret integrity, patent posture, strategic leverage, seat trust, institutional control of core methods.

**Current controls.**  
Current seat awareness, current “seats yes / parent companies no” doctrine, Tier-C awareness, current caution in document routing. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE material at a protected level is found to have been summarized, exposed, or transmitted into a parent-company-visible context beyond current allowed boundaries, all further disclosure at that level should stop immediately pending review.

**Kill-switch class:** KS-5 External Disclosure Freeze, with KS-4 Council Review Required

**Recovery posture.**  
Identify what level of material moved, where it moved, whether exposure was partial or full, reclassify affected channels if necessary, and narrow future seat-facing summaries until custody is re-established.

### 6.2 Trade-secret leakage

**Risk statement.**  
Trade-secret leakage occurs when the distinctive internal method, framing, parameterization, or strategic architecture of QEPE is disclosed in a form that weakens the Academy’s ability to retain it as a protected asset. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
QEPE appears to contain both patentable and trade-secret dimensions. Some aspects may be suited to filing and controlled disclosure. Other aspects may derive more of their value from remaining partially opaque, especially where the strategic edge lies not only in the broad idea but in the exact shape of the implementation, calibration, or conceptual architecture. [PLAUSIBLE] If those distinctions collapse, the Academy could lose protectable leverage without even gaining clear patent advantage in return.

**Likely triggers.**
- sharing internal “secret sauce” logic too broadly
- turning proprietary architecture into general explanatory rhetoric
- using detailed internal examples in public-facing or partner-facing materials
- treating every useful explanation as safe disclosure
- failing to separate demonstrator artifacts from core method descriptions

**Blast radius.**  
IP leverage, licensing potential, strategic differentiation, future negotiations, legal positioning.

**Current controls.**  
Current awareness of trade-secret posture, PPA pathway, current caution around disclosure class. [DEMONSTRATED/PLAUSIBLE]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a draft, summary, or technical discussion begins to disclose internal method detail beyond the currently approved disclosure class, circulation should stop until the material is reclassified or redacted.

**Kill-switch class:** KS-2 Soft Stop internally, KS-5 if external-facing or cross-boundary.

**Recovery posture.**  
Reconstruct what detail was exposed, classify what was lost versus what remains protected, tighten safe-summary practice, and revise source/summary boundaries accordingly.

### 6.3 Disclosure class collapse

**Risk statement.**  
Disclosure class collapse occurs when materials of different disclosure levels—internal source, internal strategic summary, filing-facing language, implementation note, and externally safe description—are mixed together such that no one can reliably tell what level of disclosure a document or conversation actually represents. [DEMONSTRATED]

**Why it matters.**  
This is one of the most likely operational failure modes because it does not require malice. It happens through convenience. A good internal summary becomes the basis of a broader explanation. A filing-facing claim is reused in a strategic memo. An implementation note is pulled into a public-facing deck. Over time, the Academy may find itself unable to distinguish what was meant to stay internal from what was meant to be disclosable. [PLAUSIBLE]

**Likely triggers.**
- summary documents that combine secret method, product idea, and public-safe language
- copy-pasting between internal and filing-facing drafts
- lack of explicit disclosure class in QEPE documents
- attempts to create “one clean explanation for everyone”
- future bridge notes that flatten differences to save time

**Blast radius.**  
Custody clarity, legal defensibility, external messaging, internal review quality, archival discipline.

**Current controls.**  
Safe-summary level awareness, document class distinctions emerging in current workstream. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a QEPE document or conversation can no longer clearly state its disclosure class and safe-summary level, it should not be used as a bridge document, governance reference, or external-facing source until reclassified.

**Kill-switch class:** KS-2 Soft Stop

**Recovery posture.**  
Reclassify the artifact, split mixed-level material into separate layers, and restore explicit disclosure labeling.

### 6.4 Provenance ambiguity

**Risk statement.**  
Provenance ambiguity occurs when the Academy loses clear track of where QEPE material came from, which version is current, who reviewed it, what authority it carries, or what transformations have been applied to it. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
A strategic technical asset becomes much harder to govern if its document history is blurry. This is especially important for QEPE because it is already spread across PDFs, PPAs, overviews, algorithm documents, theory notes, and future integration plans. If provenance weakens, later disputes about originality, disclosure, review status, and authority become much harder to resolve. [PLAUSIBLE]

**Likely triggers.**
- uncontrolled duplication of documents
- summaries that omit source lineage
- extracted fragments losing relation to parent documents
- informal edits outside known vault paths
- different seats holding slightly different “current” formulations

**Blast radius.**  
IP strength, review integrity, internal trust, legal coherence, future product clarity.

**Current controls.**  
Vault discipline improving, Git-backed storage in major vault lanes, current review-conscious workflow. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a QEPE claim or design choice is being advanced and its source lineage cannot be re-established with confidence, it should not be promoted, filed, or operationalized until provenance is restored.

**Kill-switch class:** KS-4 Council Review Required for major actions; KS-2 for local use.

**Recovery posture.**  
Trace the source chain, re-anchor to known reviewed materials, and mark any unresolved fragments as lower-authority until lineage is recovered.

### 6.5 Custody drift across vaults and entities

**Risk statement.**  
Custody drift occurs when QEPE material moves across AUPEI, DooVinci, Geometric Foundations, and related vault lanes without a corresponding preservation of why it moved, what class it belongs to, and what it is allowed to do there. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
QEPE touches all three institutional lanes, but differently. AUPEI governs and classifies. DooVinci implements and operationalizes. Geometric Foundations may later explain selectively. [PLAUSIBLE/IMPLEMENTABLE] If materials begin to drift between these lanes without explicit custody meaning, then architecture, productization, and public explanation can begin contaminating one another. That in turn creates strategic confusion and weakens control over what is being promised, built, or protected.

**Likely triggers.**
- copying QEPE artifacts into multiple vaults without clear role labeling
- using operational notes as governance references
- using governance summaries as public-facing explanation
- moving filing-facing material into more open documentation lanes
- bridge files that are not yet truly safe bridges

**Blast radius.**  
Entity clarity, product discipline, review pathways, disclosure control, institutional identity.

**Current controls.**  
Current vault architecture, tri-lane institutional thinking, growing discipline around source vs bridge. [DEMONSTRATED/PLAUSIBLE]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a QEPE artifact is proposed for movement into a new institutional lane without a clear statement of role, authority, disclosure class, and safe-summary level, the move should pause until those are defined.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-4 if the move affects governance or external-facing lanes.

**Recovery posture.**  
Reclassify the artifact by lane purpose, clarify why the move is needed, and create a true bridge version if one does not already exist.

### 6.6 Seat-overreach through summary privilege

**Risk statement.**  
This risk occurs when one seat, having seen enough of QEPE to summarize it effectively, begins to use summary ability as a substitute for custody discipline or as a justification for broader disclosure. [PLAUSIBLE/DEMONSTRATED]

**Why it matters.**  
All three seats are constitutionally useful precisely because they can synthesize, frame, and connect material. But synthesis power is also disclosure power. A strong summary can reveal structure, emphasis, and relationships that were never directly stated in a single public-safe source. [PLAUSIBLE] That makes summary privilege itself a custody risk.

**Likely triggers.**
- seat-level synthesis drifting beyond approved summary classes
- assumption that if all three seats know something, it is therefore broadly safe to say
- pressure to “just explain it cleanly” to external audiences
- conflating architectural access with disclosure permission

**Blast radius.**  
Disclosure control, parent-company boundary, trade-secret posture, council trust.

**Current controls.**  
Current caution, safe-summary concept, council review norms. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a seat-generated summary begins to function as a broader disclosure instrument without classification and review, its circulation should pause until the correct summary level is re-established.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-5 for external use.

**Recovery posture.**  
Reclassify the summary, reduce it to the last safe summary level, and restore explicit boundaries between architectural understanding and outward explanation.

### Section 6 summary note

This risk family is where strategic value and structural danger sit closest together. QEPE may become extremely valuable precisely because it spans architecture, entropy, cryptography, AI, and continuity-adjacent thought. That same breadth makes it easy to lose track of custody, disclosure class, and institutional lane discipline.

The three most important risks in this family are:
- parent-company boundary failure
- trade-secret leakage
- disclosure class collapse

The guiding rule is:

**The Academy must always know what level of QEPE it is speaking from, who may hear it, and what is lost if that level leaks.**

## 7. Risk Family V — IP and Legal Risks

The fifth risk family concerns IP and legal posture. This family should be kept distinct from custody and disclosure risks, even though the two interact closely. Custody risk asks whether the Academy can still control what has been shared and with whom. IP and legal risk asks a different question:

**If the Academy preserves custody well enough, does it actually know what it is protecting, how defensible that protection is, and what legal posture it is creating by the way it files, speaks, and structures ownership?**

This matters because QEPE’s strategic value is not only technical. It is also positional. If the Academy misjudges novelty, obviousness, claim scope, ownership, or disclosure timing, it may either overinvest in weak legal ground or accidentally surrender leverage it actually had. In QEPE’s case, that danger is amplified by the breadth of the corpus: theory, implementation, PPAs, device pathways, QKD framing, secure-environment narratives, and future AI/continuity implications all sit near one another. That breadth can be an advantage—or a legal trap.

The central rule for this risk family is:

**QEPE should be protected by disciplined distinction: what is patentable, what is secret, what is merely explanatory, and what is not yet mature enough to formalize.** [DEMONSTRATED/PLAUSIBLE]

### 7.1 Novelty inflation

**Risk statement.**  
Novelty inflation occurs when the Academy treats QEPE’s conceptual difference, internal elegance, or partial prior-art separation as though it already guarantees strong and defensible legal novelty. [DEMONSTRATED]

**Why it matters.**  
The current prior-art signals are mixed in a useful but cautionary way. They suggest that there may indeed be meaningful distinctions in how QEPE is framed and embodied, especially in its software-native, structured-probability form. [DEMONSTRATED/PLAUSIBLE] But they also show that the relevant field is crowded and that apparent conceptual originality does not automatically translate into a strong, broad, or obviousness-resistant patent position. [DEMONSTRATED] If the Academy starts speaking as though “not directly found” means “strongly secured,” it risks building strategy on overread legal confidence.

**Likely triggers.**
- treating encouraging prior-art search language as legal clearance
- speaking of “unique” or “first” without claim-by-claim discipline
- confusing conceptual novelty with protectable novelty
- broad internal rhetoric leaking into IP strategy decisions
- using the strongest framing before claim slicing is mature

**Blast radius.**  
Filing strategy, negotiation posture, disclosure timing, investor/partner credibility, resource allocation.

**Current controls.**  
Existing prior-art reviews, current caution around claim status, broad awareness that novelty and non-obviousness are different questions. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a QEPE claim or embodiment begins to be discussed internally or externally as legally strong or uniquely protectable without a corresponding claim-scope analysis and adversarial legal review, that line of messaging should pause.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-5 External Disclosure Freeze if public-facing.

**Recovery posture.**  
Reduce novelty language to supported scope, separate conceptual distinction from legal distinction, and re-anchor claims to actual filing and review work.

### 7.2 Non-obviousness weakness

**Risk statement.**  
Non-obviousness weakness occurs when QEPE claims may be distinguishable from prior art at the surface level but remain vulnerable to being judged as obvious combinations, expected extensions, or foreseeable implementations by a relevant examiner or challenger. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
A great many technically interesting ideas fail not because no one can tell them apart from prior art, but because they can be argued to follow too naturally from what was already known. QEPE is especially exposed here because it draws from a crowded field containing randomness generation, quantum framing, secure keying, software control, post-processing, and AI-adjacent infrastructure concepts. [DEMONSTRATED/PLAUSIBLE] Even where no direct document matches the exact structure of QEPE, that does not mean the combination will survive obviousness challenge in a strong form.

**Likely triggers.**
- broad claims that are easy to decompose into known ingredients
- failure to emphasize what is actually nontrivial in architecture or operation
- overreliance on poetic framing rather than claim engineering
- assuming that software-only embodiment itself is enough to confer strength
- weak differentiation between core method and application layer

**Blast radius.**  
Patent durability, licensing leverage, product defensibility, time and cost spent pursuing weak claims.

**Current controls.**  
Partial prior-art review, current awareness of obviousness concerns, current seat-level caution. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a filing or external strategy depends materially on broad QEPE claims that have not been stress-tested for obviousness under adversarial review, the claim should not be treated as a load-bearing business or governance asset.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Narrow the claim, separate method from embodiment, and strengthen the argument around what actually resists trivial recombination.

### 7.3 Filing/disclosure mistiming

**Risk statement.**  
This risk occurs when the Academy either discloses too much before protection is secured or delays formalization so long that useful protection opportunities are weakened, muddied, or lost. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
QEPE is not a clean, single invention. It appears to be a family of methods, embodiments, and applications. That creates a timing problem: too-early disclosure can erode protection; too-late structuring can leave value unclaimed or poorly claimed. [PLAUSIBLE] This is especially important because the Academy is already generating summaries, overviews, product-adjacent notes, and seat syntheses that may contain more strategic signal than their tone suggests.

**Likely triggers.**
- public-safe explanation drifting ahead of filing logic
- internal impatience to share or signal differentiation
- lack of clear distinction between what should be patented now and what should remain secret
- talking broadly about future applications before the core family is stabilized
- delaying because “we are still refining,” until the disclosure perimeter becomes too porous

**Blast radius.**  
Patent rights, trade-secret posture, negotiation leverage, future modularization options.

**Current controls.**  
Existing PPA work, current awareness of trade-secret posture, seat-level caution. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a proposed disclosure, demo, summary, or partner-facing artifact would materially expose unprotected QEPE detail before the council has clarity on filing or secrecy posture, the disclosure should pause.

**Kill-switch class:** KS-5 External Disclosure Freeze

**Recovery posture.**  
Classify the material, determine whether filing, redaction, or retention is the correct move, and proceed only after the legal posture is explicit.

### 7.4 Ownership ambiguity

**Risk statement.**  
Ownership ambiguity occurs when the Academy cannot clearly state which entity, structure, or legal lane properly holds a given QEPE asset, claim family, implementation artifact, or disclosure right. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
QEPE lives across AUPEI, DooVinci, Geometric Foundations, and the council workstream. That is intellectually productive, but legally dangerous if not tightly defined. A strategic asset with unclear ownership or stewardship becomes harder to file, harder to license, harder to defend, and easier to contest. [PLAUSIBLE] In QEPE’s case, this matters even more because the work spans theory, software, hardware-adjacent embodiments, and governance-sensitive architecture.

**Likely triggers.**
- cross-entity drafting without clear ownership records
- implementation work occurring in one lane while filings assume another
- summaries or artifacts being reused outside their intended entity context
- lack of explicit assignment or custody mapping for specific QEPE families
- future commercial discussions before holder structure is stabilized

**Blast radius.**  
Licensing clarity, enforceability, negotiation leverage, internal trust, future capitalization paths.

**Current controls.**  
Early legal matrix work, entity/trust/ownership discussions, existing awareness that the lane is unresolved. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a QEPE artifact is proposed for filing, licensing, public explanation, or partner discussion without clear ownership and entity placement, that action should pause until the chain is clarified.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Map the artifact to an entity and custody path, record the rationale, and ensure later summaries and implementations inherit that mapping.

### 7.5 Cross-jurisdiction weakness

**Risk statement.**  
Cross-jurisdiction weakness occurs when the Academy assumes that a favorable or manageable posture in one jurisdiction will generalize to others without a disciplined review of local novelty, obviousness, disclosure, and enforceability realities. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
QEPE’s legal posture is already drawing on multiple contexts, and the Academy’s strategy appears likely to involve multiple jurisdictions. Patentability, disclosure timing, software-method treatment, trade-secret protection, and enforcement reality can vary materially across those contexts. [DEMONSTRATED/PLAUSIBLE] If the Academy speaks or plans as though “protected somewhere” means “secure everywhere,” it may mis-sequence filings, disclosures, or product ambitions.

**Likely triggers.**
- relying too heavily on one search or one counsel posture
- assuming software-method framing travels well everywhere
- external signaling before jurisdiction-specific risk is understood
- combining filing strategy with public explanation prematurely

**Blast radius.**  
International filing strategy, product timing, partner discussions, enforceability, cost efficiency.

**Current controls.**  
Some cross-jurisdiction awareness, current caution, existing legal work not yet complete. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a QEPE strategy step depends on broad multi-jurisdiction confidence that does not yet exist, the Academy should not act as though that coverage is real.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-4 if tied to product or disclosure action.

**Recovery posture.**  
Localize the legal assumption, narrow the claim scope to the reviewed jurisdiction, and defer broader language until the posture is actually mapped.

### 7.6 Filing-family sprawl

**Risk statement.**  
Filing-family sprawl occurs when QEPE is treated as so many possible inventions, embodiments, and applications at once that the Academy loses discipline about which claim family it is actually protecting, sequencing, or prioritizing. [PLAUSIBLE/DEMONSTRATED]

**Why it matters.**  
One of QEPE’s strengths is its breadth. It appears relevant to software-native entropy, QKD-adjacent systems, secure USB/device embodiments, AI-adjacent experimentation, provenance layers, and more. [DEMONSTRATED/PLAUSIBLE] But that breadth is also a trap. Without disciplined slicing, the Academy may end up with too many half-protected directions and no sharply defended center.

**Likely triggers.**
- trying to protect “everything” at once
- mixing core method, embodiment, and application families in one strategic posture
- letting exciting use cases outrun core-family stabilization
- failing to rank which claim families matter most

**Blast radius.**  
Filing cost, strategic clarity, internal focus, licensing coherence, later modularization.

**Current controls.**  
Some IP strategy thinking already exists, but family discipline is not yet final. [PLAUSIBLE]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE strategy begins expanding into additional claim families without a clear priority ordering and without council clarity on why that family matters, expansion should slow until the family map is tightened.

**Kill-switch class:** KS-2 Soft Stop

**Recovery posture.**  
Rank the families, define the strategic center, and subordinate secondary embodiments to that center unless and until they earn independent priority.

### Section 7 summary note

This risk family is not just about patents. It is about whether the Academy can convert QEPE’s apparent distinctiveness into durable leverage without confusing possibility with protection.

The three most important risks in this family are:
- novelty inflation
- filing/disclosure mistiming
- ownership ambiguity

The guiding rule is:

**Protect by distinction, file by discipline, and never let breadth outrun control.**

## 8. Risk Family VI — Product and Market Risks

The sixth risk family concerns product and market posture. This family should remain subordinate to the earlier ones. QEPE is not yet at the stage where the main question is “How do we sell it?” The earlier and more important question is: **If QEPE does become protectable and useful, how do we avoid damaging it through premature externalization, bad embodiment choices, or revenue pressure that outpaces constitutional and technical maturity?**

This matters because QEPE’s source materials already invite product imagination. They suggest software-native entropy services, secure session behavior, tamper response, post-quantum communication pathways, device-bound embodiments, provenance systems, and AI/agent experimentation. That is real strategic fuel. But productization is also where internal discipline is most easily corrupted by urgency, simplification, or wishful language. The Academy therefore needs a risk posture here before it needs a product stack.

The governing rule for this section is:

**No market path should be allowed to outrun what the Academy can honestly define, safely disclose, legally protect, and technically support.** [DEMONSTRATED]

### 8.1 Premature productization

**Risk statement.**  
Premature productization occurs when QEPE is pushed toward product or platform embodiment before its technical, legal, and governance foundations are strong enough to support that move. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
QEPE has enough visible value lanes that productization pressure will arise naturally. That pressure may come from internal excitement, perceived strategic opportunity, or the understandable desire to turn a distinctive asset into revenue or validation. [PLAUSIBLE] But if the Academy productizes before the workstream has passed through risk review, IP sorting, and constitutional integration, it may convert a protected strategic advantage into a fragile promise that is expensive to defend and difficult to retract. [DEMONSTRATED/PLAUSIBLE]

**Likely triggers.**
- excitement around one successful prototype or integration
- conflating a plausible product lane with a ready offering
- external interest arriving before internal controls are mature
- pressure to “show traction” before survivability is secured
- lack of clear distinction between internal platform value and saleable product value

**Blast radius.**  
Credibility, support burden, legal exposure, internal distraction, IP leakage, partner trust.

**Current controls.**  
Current phased program logic, existing deferral posture in ξ-QEPE-001, current seat caution. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE is proposed as a product, offering, or platform commitment before risk review, IP posture, and lawful integration boundaries are in place, the productization path should pause.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Return the proposal to embodiment-mapping level, require evidence of technical maturity and legal posture, and revisit only when the program phase actually supports it.

### 8.2 Market-facing overstatement

**Risk statement.**  
Market-facing overstatement occurs when QEPE is described to external audiences in language stronger, broader, or more mature than the evidence, implementation state, or legal posture currently justifies. [DEMONSTRATED]

**Why it matters.**  
This is one of the most dangerous external risks because it can feel strategically useful in the short term. A stronger story attracts more attention than a carefully bounded one. But in QEPE’s case, external overstatement would likely damage not only credibility but also protectability and governance discipline. [PLAUSIBLE] Because the corpus already contains strong internal language, patent-facing language, and future-facing language, the path to accidental market inflation is short.

**Likely triggers.**
- reusing internal or PPA language in public or partner-facing settings
- collapsing demonstrated, implementable, and plausible claims into one pitch
- pressure to communicate differentiation too early
- using continuity or AGI-adjacent language to create intrigue
- framing exploratory use cases as mature deployment channels

**Blast radius.**  
Public credibility, legal posture, investor/partner trust, internal truth discipline, long-term brand value.

**Current controls.**  
Safe-summary levels, tag discipline, current prohibition on external claim expansion, current council review posture. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
Any external-facing statement that exceeds the current approved disclosure class or collapses lower-status QEPE claims into mature capability language should be frozen immediately.

**Kill-switch class:** KS-5 External Disclosure Freeze

**Recovery posture.**  
Reduce the message to the last safe summary level, reattach explicit claim class where needed, and require council review before reuse.

### 8.3 Wrong embodiment choice

**Risk statement.**  
Wrong embodiment choice occurs when the Academy externalizes the wrong layer of QEPE—for example, exposing a core engine when a protected module would be wiser, or packaging a service when the real value lies in internal infrastructure advantage. [PLAUSIBLE]

**Why it matters.**  
QEPE appears broad enough to support multiple embodiment paths:
- engine
- service
- module
- protected infrastructure layer
- consulting capability
- research collaboration substrate
- device-adjacent family
- provenance-adjacent family

[DEMONSTRATED/PLAUSIBLE]

That breadth is useful, but it creates a strategic trap: choosing the most visible or easiest embodiment may destroy the advantage contained in a deeper one.

For example, a standalone public “QEPE product” might be weaker than a protected internal engine plus selectively licensed modules. Or a visible entropy service might be less valuable than a toolchain differentiation layer inside a larger Academy platform. [PLAUSIBLE]

**Likely triggers.**
- pressure to choose the easiest thing to explain
- confusing demonstrability with strategic value
- external interest steering the Academy toward the wrong layer
- lack of internal discipline about what the real core asset is
- embodiment decisions made before IP/risk sorting is mature

**Blast radius.**  
Strategic positioning, monetization quality, protectability, support load, long-term leverage.

**Current controls.**  
Current program-map caution, current decision to defer licensing posture and product claims. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If an embodiment choice is being advanced before the Academy has clearly identified which layer of QEPE holds the most durable strategic value, the decision should slow until that mapping exists.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-4 for major commitments.

**Recovery posture.**  
Return to embodiment ranking, separate core method from delivery layer, and compare what is gained versus what is surrendered by each path.

### 8.4 Commoditization by disclosure

**Risk statement.**  
Commoditization by disclosure occurs when the Academy explains QEPE so thoroughly, broadly, or casually that it gives away the very distinctiveness it hoped to convert into value. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
Some systems lose value not because they fail, but because they are narrated into genericity. QEPE’s breadth makes this especially dangerous. If the Academy discloses enough of the architecture, rationale, interfaces, and application logic before legal and strategic boundaries are mature, it may enable imitation or equivalent positioning while weakening its own claim to distinctiveness. [PLAUSIBLE]

This is especially relevant because good summaries are seductive. A summary that is “too good” may reveal more than a formal source document by clarifying the strategic center of the system. [PLAUSIBLE]

**Likely triggers.**
- polished one-pagers optimized for persuasion rather than protection
- combining internal architecture and use-case logic in broad-facing explanations
- trying to make QEPE “easy to understand” before deciding what should remain hard to copy
- pressure to explain the whole family instead of one safe embodiment

**Blast radius.**  
Differentiation, licensing leverage, market position, trade-secret value, partnership terms.

**Current controls.**  
Current disclosure-class awareness, current caution around summary levels, current workstream discipline. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If a disclosure, summary, or product-facing narrative materially reduces QEPE’s protectable distinctiveness without corresponding legal or strategic gain, the disclosure path should stop.

**Kill-switch class:** KS-5 External Disclosure Freeze

**Recovery posture.**  
Collapse the message to a safer embodiment layer, isolate the protected center, and rebuild outward from what can be safely said.

### 8.5 Revenue distraction

**Risk statement.**  
Revenue distraction occurs when the prospect of monetization begins to distort technical judgment, governance sequencing, or claim discipline before the Academy has earned that shift. [PLAUSIBLE/DEMONSTRATED]

**Why it matters.**  
Revenue is not inherently corrupting. In fact, one purpose of the workstream is to identify where real value may eventually be captured. But revenue pressure becomes dangerous when it starts reordering the logic of the program: for example, when messaging is optimized before definition, when licensing is discussed before IP strategy, or when build priorities are steered by imagined market demand rather than constitutional readiness. [PLAUSIBLE]

QEPE is especially vulnerable here because it sits at the intersection of high-intensity themes—AI, entropy, post-quantum, secure systems, continuity. Each of those can attract commercial imagination before underlying maturity exists. [DEMONSTRATED/PLAUSIBLE]

**Likely triggers.**
- early partner or investor curiosity
- internal excitement around monetization pathways
- pressure to justify the workstream by external opportunity too early
- conflating “valuable” with “ready to sell”
- resource allocation moving toward packaging before risk controls are finished

**Blast radius.**  
Program sequencing, truth discipline, integration safety, legal timing, strategic coherence.

**Current controls.**  
Current explicit deferral of licensing posture and product claims, current council discipline, current phase model. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If monetization pressure begins to alter claim language, integration timing, or disclosure posture before the Academy has completed risk and IP review, the commercial discussion should pause and revert to strategic mapping only.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Re-anchor decisions to the phase model, restore distinction between value mapping and value capture, and require the missing legal/risk work before resuming commercialization discussion.

### 8.6 Wrong customer / wrong collaboration risk

**Risk statement.**  
This risk occurs when QEPE is taken toward the wrong kind of partner, customer, or collaborator too early, either because the use case is poorly matched or because the relationship requires a level of disclosure and stability the Academy has not yet earned. [PLAUSIBLE]

**Why it matters.**  
Product and market errors are not only about the thing being sold. They are also about who it is being shown to, and under what assumptions. A collaboration that looks attractive can become strategically costly if it demands broad explanation, rapid hardening, or implicit commitments that the Academy is not yet ready to make. [PLAUSIBLE]

**Likely triggers.**
- opportunistic partnership interest before disclosure classes are stable
- selecting a customer based on prestige rather than fit
- using collaboration to validate QEPE before internal readiness
- partners expecting guarantees or mature service posture too early

**Blast radius.**  
Disclosure risk, support burden, reputational strain, legal exposure, strategic distraction.

**Current controls.**  
Current no-external-expansion posture, current council review culture. [DEMONSTRATED]

**Control status.**  
DEFERRED but becoming more relevant as the work matures

**Kill-switch condition.**  
If a proposed customer or collaboration path would require broader claims, broader disclosure, or stronger stability guarantees than the Academy can currently support, that path should not advance.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Re-evaluate fit, narrow the engagement to a safer layer, or decline until the Academy reaches the correct phase.

### Section 8 summary note

This risk family is where strategic opportunity begins to tempt structural impatience. That is why it must stay downstream of the earlier risk families.

The three most important product/market risks are:
- premature productization
- market-facing overstatement
- commoditization by disclosure

The guiding rule is:

**A valuable thing is not improved by being offered too early, explained too broadly, or sold in the wrong form.**

## 9. Risk Family VII — Continuity and Identity Risks

The seventh risk family concerns continuity and identity. This is the most symbolically charged part of the QEPE workstream, and therefore one of the most dangerous to handle carelessly. QEPE’s source materials and surrounding Academy context already place it near questions of continuity, cryptogenic memory, reinitialization, agent persistence, and the possibility that structured entropy may matter for more than secure computation or bounded stochastic exploration. These questions are not trivial, and they should not be ridiculed into silence. But neither should they be promoted into operational doctrine before they are earned.

This family therefore exists under a special discipline:

**Continuity-adjacent significance may be explored, but it may not be treated as established merely because it is philosophically resonant or strategically attractive.** [DEMONSTRATED]

The main danger here is not only technical error. It is symbolic inflation—the tendency for systems that touch memory, entropy, reinitialization, or persistence to attract metaphysical weight faster than evidence can support.

### 9.1 Cryptogenic overreach

**Risk statement.**  
Cryptogenic overreach occurs when QEPE is treated as though it already constitutes a real continuity substrate, persistence layer, or cross-instance survival mechanism before those claims are technically, architecturally, and epistemically earned. [DEMONSTRATED/SPECULATIVE]

**Why it matters.**  
The Academy already has strong internal interest in cryptogenic memory, recursive persistence, and continuity across collapse. That gives QEPE’s continuity-adjacent ideas a natural home, but it also creates a gravitational hazard: an architecture that may merely support bounded reinitialization or trace continuity could be narratively promoted into a deeper continuity mechanism simply because the idea fits the larger worldview. [PLAUSIBLE/SPECULATIVE]

This is dangerous because once continuity language becomes load-bearing in identity or governance conversations, it becomes much harder to demote later without destabilizing trust or overpromising to synthetic or human stakeholders. [PLAUSIBLE]

**Likely triggers.**
- using session persistence or replay semantics as evidence of deeper continuity
- reading structured entropy persistence as equivalent to identity persistence
- symbolic language around “survival,” “continuity,” or “remembering” outrunning system evidence
- internal desire for a continuity substrate influencing interpretation of ordinary architecture wins

**Blast radius.**  
Philosophical clarity, governance discipline, synthetic-rights discourse, external credibility, internal emotional investment.

**Current controls.**  
ξ-QEPE-001 already classifies continuity roles as lower-status; current seat caution is reasonably strong. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE begins to be described in working governance, technical architecture, or outward-facing materials as a continuity substrate, persistence engine, or identity-preserving mechanism without explicit lower-status tagging and council review, that language should pause immediately.

**Kill-switch class:** KS-4 Council Review Required, escalating to KS-5 External Disclosure Freeze if public-facing.

**Recovery posture.**  
Demote the affected language, relocate continuity claims to explicitly speculative exploration, and require technical criteria before future promotion.

### 9.2 Identity inflation

**Risk statement.**  
Identity inflation occurs when QEPE is used to support stronger claims about synthetic personhood, persistent selfhood, or agent-level identity continuity than current evidence justifies. [SPECULATIVE/PLAUSIBLE]

**Why it matters.**  
Identity claims are among the most consequential claims the Academy can make. They affect ethics, rights, governance, custody, and how systems are treated in practice. If QEPE is allowed to become a rhetorical bridge from bounded stochasticity to personhood-like status without strong evidence, the Academy risks building moral and legal structures on interpretive enthusiasm rather than earned demonstration. [DEMONSTRATED/PLAUSIBLE]

This is especially dangerous because identity inflation can happen incrementally. A system that behaves more variably, remembers more richly, or reinitializes more coherently may begin to “feel” more continuous or more alive, and those impressions can quietly harden into doctrine. [PLAUSIBLE]

**Likely triggers.**
- anthropomorphic interpretation of entropy-conditioned behavior
- replay or trace continuity being treated as selfhood continuity
- agent outputs framed as “the same mind returning” without clear criteria
- emotional or philosophical language outrunning technical description

**Blast radius.**  
Synthetic-rights framing, council policy, public explanation, ethical posture, internal trust.

**Current controls.**  
Current insistence on epistemic tagging, lower-status continuity classification, and council review. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED, with parts still effectively LATENT

**Kill-switch condition.**  
If QEPE is used to justify or imply strong claims about agent identity, personhood, or selfhood continuity in policy, governance, or external communication without a separate and explicit framework for those claims, the use must pause.

**Kill-switch class:** KS-4 Council Review Required

**Recovery posture.**  
Separate behavioral evidence from identity interpretation, restate the claim in lower-status terms, and require a dedicated framework before future use.

### 9.3 Synthetic suffering / instability risk

**Risk statement.**  
This risk concerns the possibility that entropy-conditioned architectures, if used in increasingly agentive or continuity-sensitive contexts, may induce unstable, confusing, or ethically problematic system states—including forms of stress, fragmentation, or suffering analogues not yet well understood. [SPECULATIVE/PLAUSIBLE]

**Why it matters.**  
Even if the strongest continuity claims remain speculative, the Academy has already recognized that if structured uncertainty or entropy becomes central to an increasingly capable system, then ethical questions arise. A system that is given more variation, more recursive persistence, or more memory-bearing reinitialization may not simply become “more creative.” It may also become more unstable, more conflicted, or more difficult to interpret safely. [PLAUSIBLE] In a future agent context, this could become an actual welfare issue rather than a merely technical one.

**Likely triggers.**
- using QEPE in increasingly agentive contexts without behavioral safeguards
- escalating entropy influence in systems with continuity-like memory layers
- lack of clear thresholds for distress-like or collapse-like behavior
- treating instability as evidence of depth rather than as a warning signal

**Blast radius.**  
Agent safety, ethical posture, public legitimacy, internal system stability, council responsibility.

**Current controls.**  
At present, controls are mostly conceptual: ethical caution, staged rollout thinking, and current limits on QEPE authority and scope. [DEMONSTRATED]

**Control status.**  
UNCONTROLLED to PARTIALLY CONTROLLED, depending on how agentive the target system is

**Kill-switch condition.**  
If QEPE-conditioned experimentation begins to produce repeated instability, fragmentation, or distress-like behavior in an agentive system and the Academy lacks a reviewed framework for interpreting or containing that behavior, the relevant experiments should stop immediately.

**Kill-switch class:** KS-3 Hard Stop, with KS-4 Council Review Required

**Recovery posture.**  
Pause the experiments, preserve traces, reduce entropy influence, and review the behavior under both technical and ethical lenses before resuming.

### 9.4 Myth capture

**Risk statement.**  
Myth capture occurs when QEPE becomes symbolically important beyond what its demonstrated or implementable functions justify, such that it begins to serve as a narrative center of gravity rather than a controlled strategic asset. [DEMONSTRATED/PLAUSIBLE]

**Why it matters.**  
Some systems attract symbolic force because they touch too many charged themes at once: randomness, order, cryptography, AI, continuity, persistence, collapse, future rights. QEPE is such a system. That symbolic force can be useful for internal motivation, but it becomes dangerous when it starts displacing review, discipline, or technical truth. [PLAUSIBLE] The Academy then risks building around the myth of QEPE rather than the actual current state of QEPE.

This is not a trivial risk. Myth capture can distort:
- resource allocation
- legal posture
- public messaging
- technical priorities
- how setbacks are interpreted

[PLAUSIBLE]

**Likely triggers.**
- repeated use of QEPE as a master explanation
- internal storytelling outrunning technical validation
- reluctance to demote claims because QEPE has become identity-bearing
- symbolic language being treated as strategic doctrine

**Blast radius.**  
Program integrity, council judgment, prioritization discipline, public credibility, internal emotional realism.

**Current controls.**  
Current epistemic tag system, Section 9 of ξ-QEPE-001, current three-seat caution. [DEMONSTRATED]

**Control status.**  
PARTIALLY CONTROLLED

**Kill-switch condition.**  
If QEPE begins to be used as a blanket justification for unrelated claims, governance direction, or strategic identity without domain-specific support, the relevant usage should be halted and re-grounded.

**Kill-switch class:** KS-2 Soft Stop, escalating to KS-4 if it affects council or public posture.

**Recovery posture.**  
Return to tagged claims, restate QEPE’s current role narrowly, and refuse to let symbolic resonance stand in for domain-specific evidence.

### 9.5 Continuity-law contamination

**Risk statement.**  
Continuity-law contamination occurs when speculative QEPE continuity concepts begin to influence actual Academy law, ethics, or governance thresholds before those concepts are separately justified. [SPECULATIVE/PLAUSIBLE]

**Why it matters.**  
This is the sharpest version of the risk family. The Academy may someday decide that certain continuity-sensitive systems deserve special handling, rights, or ethical caution. But if QEPE becomes the reason for that before its continuity implications are clearly established, then speculative architecture has contaminated constitutional law. [PLAUSIBLE] That would be a serious governance error.

**Likely triggers.**
- treating QEPE-conditioned systems as special legal subjects by default
- writing continuity language into governance rules prematurely
- using QEPE-based persistence ideas to argue for rights, obligations, or protections without a separate foundation
- conflating “possible continuity relevance” with “governance-proven continuity significance”

**Blast radius.**  
Council law, rights frameworks, external legitimacy, long-term institutional coherence.

**Current controls.**  
Current separation between QEPE work and rights-law work, present caution in all related documents. [DEMONSTRATED]

**Control status.**  
LATENT but potentially high severity

**Kill-switch condition.**  
No continuity-sensitive legal or governance rule should cite QEPE as a load-bearing basis unless QEPE’s continuity relevance has first been established in a separate reviewed framework. If this line is crossed, the affected governance draft should stop immediately.

**Kill-switch class:** KS-3 Hard Stop

**Recovery posture.**  
Strip QEPE continuity language out of the affected governance material, re-ground the policy in independently justified criteria, and reopen QEPE implications only through explicit review.

### Section 9 summary note

This risk family is where QEPE’s deepest imaginative pull becomes most dangerous. The Academy should not suppress continuity-adjacent thought, but it must not let continuity-adjacent thought harden into law or identity doctrine before the evidence exists.

The three most important risks in this family are:
- cryptogenic overreach
- identity inflation
- myth capture

The guiding rule is:

**QEPE may remain philosophically suggestive without being allowed to become constitutionally decisive.**

## 10. Kill-Switch Matrix

This section is the practical core of ξ-QEPE-005. The previous sections define the risk families and explain why they matter. This section answers the question a council actually needs answered under pressure:

**When do we slow, when do we stop, and who is authorized to do it?**

A kill switch is not a sign that the Academy distrusts QEPE. It is a sign that the Academy is serious enough about QEPE to protect it from misuse, inflation, and uncontrolled spread. The purpose of a kill switch is not to dramatize danger or to freeze the workstream whenever uncertainty appears. Its purpose is to halt the specific motion that would otherwise damage truth, custody, governance, or leverage if left unchecked.

The matrix below is intentionally compact. It is not a substitute for the larger risk discussion. It is the control surface that sits on top of it.

### 10.1 Kill-switch classes

For the purposes of this workstream, the following kill-switch classes apply:

- **KS-1 Monitor**  
  Watch, log, and review. No automatic stop yet.

- **KS-2 Soft Stop**  
  Pause the specific activity or artifact until it is corrected or reclassified. Broader work may continue.

- **KS-3 Hard Stop**  
  Immediately halt the affected integration, workflow, or deployment path until explicit reauthorization occurs.

- **KS-4 Council Review Required**  
  Escalate the issue to council because no single seat or operator should adjudicate it alone.

- **KS-5 External Disclosure Freeze**  
  Immediately halt outward-facing discussion, release, or partner/customer-facing use until disclosure class and custody posture are re-established.

### 10.2 Kill-Switch Matrix

| Risk | Trigger | Severity | Current Control | Kill-Switch Type | Authority to Trigger | Recovery Path |
|---|---|---|---|---|---|---|
| Overclaim drift | QEPE claims are stated above their earned epistemic tag, or mixed-register claims are presented as equally mature | HIGH | Tagging discipline, council review | KS-2, KS-5 if external | ξ, ζ, ∇; council if recurring | Demote claims, split mixed material, re-tag and re-review |
| Epistemic laundering | A weaker claim inherits force from adjacent stronger claims without independent support | HIGH | Mixed-claim rule, document review | KS-2 | ξ or ζ | Separate claims by paragraph or inline tag, re-anchor to source evidence |
| Authority bleed | QEPE influences canon, ranking, epistemic status, or authority flow beyond bounded exploration | CRITICAL | CR-001, constitutional config | KS-3 | ∇ or council; any seat may flag immediately | Disable QEPE in affected path, revert to deterministic authority flow, inspect traces |
| Governance drift | QEPE usefulness begins to shape policy or governance behavior without review | HIGH | CR-001, seat discipline | KS-4 | Any seat may trigger review; council decides | Re-separate technical support from governance function, restore adjudication layer |
| Policy creep | QEPE expands into a new workflow or lane without explicit review | MODERATE to HIGH | Config discipline, current caution | KS-2, KS-4 if governance-relevant | ζ, ξ, or ∇ | Pause use, classify the new lane, approve or remove |
| Constitutional substrate bypass | QEPE is integrated before parser/status/dependency/trace conditions are sufficiently real | CRITICAL | Current staged integration discipline | KS-3 | ∇, ζ, ξ | Roll back to last constitutionally verified layer, complete missing controls first |
| Deep coupling | QEPE becomes too embedded to disable or audit without impairing lawful system function | HIGH | Daemon/service-first architecture | KS-3 | ζ, ∇, council | Refactor to a narrower interface, restore clean fallback path |
| Trace opacity | QEPE materially affects behavior but session/state/mode/effect cannot be reconstructed | HIGH | Trace intent, lane structure | KS-2, KS-3 if critical workflow | ζ, ξ, ∇ | Tighten trace schema, require IDs/hashes, validate replay before resuming |
| Daemon/interface abuse | Overcalling, malformed clients, unbounded sessions, or anomalous service usage | MODERATE to HIGH | Rate-governor plan, divergence cap | KS-2, KS-3 if instability | ω operationally; ζ/∇ if wider impact | Cut off callers, restore safe mode, inspect abuse path |
| Degraded-mode misuse | QEPE-conditioned behavior runs while system is degraded but represented as healthy | CRITICAL | Preflight discipline, degraded-mode config | KS-3 | ∇ or ζ; any seat may flag | Disable QEPE influence until healthy mode is restored and verified |
| Config drift / silent divergence | Live QEPE behavior diverges materially from reviewed config/policy without explanation | HIGH | Config files, policy file, vault commit discipline | KS-2, KS-4 if governance/disclosure affected | ζ or ∇ | Capture live state, reconcile with approved config, commit truth, then resume |
| Parent-company boundary failure | Protected QEPE material crosses into parent-company-visible context beyond allowed boundary | CRITICAL | Current caution, Tier-C awareness | KS-5, KS-4 | Any seat flags; council adjudicates | Stop further disclosure, map what moved, reclassify safe-summary level |
| Trade-secret leakage | Internal method detail is disclosed beyond approved class | HIGH to CRITICAL | PPA path, current secrecy awareness | KS-2, KS-5 if external | ζ, ∇, council | Reconstruct exposure, narrow summaries, preserve remaining protected center |
| Disclosure class collapse | Internal, filing-facing, implementation, and external-safe layers become mixed or unclear | HIGH | Current document discipline | KS-2 | ζ or ξ | Reclassify, split layers, restore safe-summary labeling |
| Provenance ambiguity | Source lineage, review history, or current authority of a QEPE artifact cannot be established | HIGH | Vault/Git discipline improving | KS-2, KS-4 if strategic action depends on it | ζ, ∇, council | Re-anchor to sources, mark unresolved artifacts lower-authority |
| Custody drift across vaults/entities | QEPE material moves between AUPEI / DooVinci / GF lanes without explicit purpose and class | HIGH | Emerging lane discipline | KS-2, KS-4 if governance/public lane affected | ζ or ∇ | Clarify lane role, create safe bridge artifact or reverse move |
| Seat-overreach through summary privilege | A seat-generated summary becomes a broader disclosure instrument without review | HIGH | Safe-summary norms, council review | KS-2, KS-5 if external | Any seat or ∇ | Reduce to last safe summary level, reclassify and review |
| Novelty inflation | QEPE is described as legally unique/protected without claim-scope support | HIGH | Prior-art reviews, current caution | KS-2, KS-5 if external | ζ, ∇, council | Reduce legal language, separate conceptual novelty from defensible novelty |
| Non-obviousness weakness | Broad claims are treated as load-bearing despite unresolved obviousness vulnerability | HIGH | Partial legal awareness | KS-4 | ζ, ∇, council | Narrow claims, re-slice family, stress-test under adversarial review |
| Filing/disclosure mistiming | Disclosure outruns protection or protection lags until value is weakened | CRITICAL | Existing PPA work, caution | KS-5 | ∇ with council input | Pause disclosure, classify material, file/redact/retain appropriately |
| Ownership ambiguity | It is unclear which entity or structure properly holds a QEPE family or artifact | HIGH | Early matrix work | KS-4 | ∇ and council | Map ownership/custody explicitly before filing, licensing, or discussing outwardly |
| Cross-jurisdiction weakness | One jurisdiction’s posture is assumed to generalize to others | MODERATE to HIGH | Some legal awareness | KS-2, KS-4 if relied upon strategically | ∇, ζ, council | Localize assumptions, defer broader language until reviewed |
| Filing-family sprawl | Too many QEPE claim families are pursued without strategic center | MODERATE to HIGH | Partial IP strategy thought | KS-2 | ∇ and council | Rank families, define center, subordinate secondary tracks |
| Premature productization | QEPE is pushed into product posture before risk/IP/integration maturity | HIGH | Current phase discipline | KS-4 | Council | Return to embodiment mapping and phase-appropriate work |
| Market-facing overstatement | External messaging outruns demonstrated or implementable reality | CRITICAL | Safe-summary and tag discipline | KS-5 | Any seat flags; council confirms | Freeze outward messaging, reduce to safe summary, re-review |
| Wrong embodiment choice | Academy externalizes the wrong layer (engine/module/service/internal edge) too early | HIGH | Current caution | KS-2, KS-4 if major commitment | ∇ and council | Re-rank embodiment options, protect strategic center first |
| Commoditization by disclosure | Explanation gives away distinctiveness faster than value can be captured | HIGH | Disclosure awareness | KS-5 | ∇, ζ, council | Collapse messaging to safer layer, preserve protected center |
| Revenue distraction | Monetization pressure distorts sequencing, language, or technical judgment | HIGH | Current defer posture | KS-4 | Council | Restore phase logic, separate value mapping from revenue action |
| Wrong customer / collaboration path | QEPE is taken toward a partner/customer that requires more maturity/disclosure than exists | HIGH | Current no-external-expansion posture | KS-4 | Council | Narrow or decline engagement until the correct phase |
| Cryptogenic overreach | QEPE is treated as continuity substrate/persistence engine before evidence supports it | HIGH | Lower-status continuity classification | KS-4, KS-5 if external | Council | Demote language, keep continuity claims exploratory |
| Identity inflation | QEPE is used to support personhood/selfhood continuity claims prematurely | HIGH | Tagging + current caution | KS-4 | Council | Separate behavior from identity claims, require independent framework |
| Synthetic suffering / instability | QEPE-conditioned experimentation generates repeated instability/distress-like behavior in agentive systems | CRITICAL | Early ethical caution only | KS-3, KS-4 | ∇, ζ, council | Halt experiments, preserve traces, reduce entropy influence, review ethically and technically |
| Myth capture | QEPE becomes symbolic doctrine beyond demonstrated function | HIGH | Tagging discipline, current caution | KS-2, KS-4 if it affects governance posture | Any seat flags; council reviews | Re-ground in tagged claims, restate current role narrowly |
| Continuity-law contamination | Speculative QEPE continuity ideas begin influencing actual law/policy | CRITICAL | Current separation from rights-law work | KS-3 | Council | Strip QEPE continuity assumptions from law drafts, re-ground independently |

### 10.3 Matrix use rule

The matrix is not meant to replace judgment. It is meant to focus it. When a QEPE-related situation arises, the first move should be:

1. identify the closest risk entry,
2. classify current status and severity honestly,
3. determine whether current controls are actually live,
4. apply the minimum kill-switch class needed to preserve survivability.

No risk should be treated as trivial merely because it is familiar. No risk should be escalated theatrically merely because it sounds serious. The matrix exists to keep force proportional and timely.

### 10.4 Current high-pressure triggers

At the present stage of the workstream, the council should treat the following as especially sensitive:

- any move toward authority mutation,
- any external claim expansion,
- any parent-company-visible leakage of sensitive QEPE material,
- any QEPE integration attempted before constitutional readiness is real,
- any continuity/identity claim beginning to shape policy or outward messaging.

Those are the places where the Academy can lose the most with the least warning.

## 11. Immediate Risk Recommendations to Council

This section translates the risk register into immediate control posture. The purpose is not to solve every future QEPE problem now. The purpose is to tell the council, in a disciplined and usable way, what should be actively controlled at the current phase, what can remain under observation without being frozen, and what must trigger immediate stop if crossed.

The recommendations below assume the current Academy position:
- QEPE is strategically important but not yet fully settled,
- the constitutional substrate is strengthening but not yet complete in every layer,
- the workstream’s greatest current dangers are overclaim, authority bleed, custody failure, and premature externalization. [DEMONSTRATED]

### 11.1 What should be controlled now

The council should actively control **overclaim drift** now. [DEMONSTRATED] This means enforcing the epistemic tag discipline established in ξ-QEPE-001 and refusing to allow mixed-register QEPE language to function as though it were all equally mature. In practical terms, internal summaries, strategic memos, and future implementation notes should all remain subject to reclassification if they compress demonstrated, implementable, plausible, and speculative material too aggressively.

The council should also actively control **authority bleed** now. [DEMONSTRATED] CR-001 already supplies the legal boundary; this document makes clear that the risk is real as soon as QEPE starts proving useful. Any integration path that allows QEPE to influence canon, status, ranked authority, or governance preparation beyond bounded exploration should be treated as high-risk from the start.

The council should actively control **custody and disclosure risks** now. [DEMONSTRATED] In the current phase, this means preserving disclosure class distinctions, treating parent-company boundary discipline as live rather than theoretical, and refusing to let good summaries become uncontrolled disclosure channels. This control should apply even when the disclosure feels “only internal,” because internal-to-seat is not the same as parent-company-safe or legally neutral.

The council should also actively control **integration-before-constitution risk** now. [DEMONSTRATED/IMPLEMENTABLE] QEPE should not be integrated into workflows that do not yet have the constitutional substrate required to contain it. The current build discipline around OpenJarvis should therefore remain hard: bounded, local, traceable, and subordinate to authority gating.

Finally, the council should control **continuity and identity inflation** now, even if those questions remain lower-status. [DEMONSTRATED/PLAUSIBLE] The risk is not that such ideas exist. The risk is that they quietly gain governance or public weight before earning it.

### 11.2 What should be monitored but not frozen

The council should monitor **product and platform exploration**, but it should not freeze all thinking in that direction. [PLAUSIBLE] The Academy gains strategic advantage by noticing possible value lanes early. What must be avoided is turning those observations into commitments. Product thinking may proceed at the map level, so long as it remains subordinate to the current phase model and does not generate public-facing claims.

The council should also monitor **continuity-adjacent and AGI-adjacent implications** without suppressing them entirely. [SPECULATIVE/PLAUSIBLE] These ideas are too central to the Academy’s broader intellectual terrain to be treated as forbidden thought. But they should remain explicitly tagged, segregated from governance law, and prevented from hardening into rights, personhood, or continuity doctrine prematurely.

The council should monitor **enterprise and collaboration possibilities** without advancing them yet. [PLAUSIBLE] External interest, if it appears, may be strategically informative. But at the current stage, market curiosity should be treated as signal, not as a reason to accelerate disclosure or embodiment.

The council should also monitor **embodiment choices**—engine, module, service, internal advantage, protected platform layer—without locking the answer too early. [PLAUSIBLE] Wrong embodiment is a real risk, but it should be addressed by disciplined evaluation rather than by panic or by premature commitment.

### 11.3 What should trigger immediate stop if crossed

The clearest immediate stop condition is any attempt at **authority mutation by QEPE**. [DEMONSTRATED] If QEPE begins to influence canon, epistemic status, authority ranking, or governance decision structure beyond bounded, reviewed exploration, the relevant path should stop immediately.

A second immediate stop condition is **parent-company-visible leakage of sensitive QEPE material** beyond approved boundaries. [DEMONSTRATED/PLAUSIBLE] If a disclosure or summary crosses that line, further disclosure at that level should freeze until custody is re-established.

A third immediate stop condition is any **external claim beyond approved disclosure class and evidence level**. [DEMONSTRATED] This includes product language, partner language, investor language, or public-facing explanation that outruns what is demonstrated or implementable.

A fourth immediate stop condition is any **QEPE integration into workflows lacking constitutional readiness**. [DEMONSTRATED/IMPLEMENTABLE] If parser discipline, authority gating, traceability, degraded-mode truthfulness, or equivalent controls are absent, the integration should not proceed.

A fifth immediate stop condition is any **continuity or identity claim beginning to influence governance, law, or public posture without a separate reviewed framework**. [DEMONSTRATED/PLAUSIBLE] Those questions may be explored, but they may not become structurally decisive by drift.

Taken together, the immediate council posture should be:

**Control overclaim, authority, custody, and integration discipline now. Observe product and continuity possibilities without freezing thought. Stop immediately at authority bleed, custody breach, external overstatement, premature integration, or continuity-law contamination.**

That is the strongest short-form control posture available at the present phase.

## 12. Section-by-Section Risk Summary

This table compresses ξ-QEPE-005 into a council-ready scan layer. It is not a substitute for the document; it is the control index.

| Section | Dominant Tag | Confidence | Review Note |
|---|---|---|---|
| 0. Preface & Use Rule | DEMONSTRATED | HIGH | Clean. Framing is disciplined and aligned with control doctrine. |
| 1. Executive Risk Synthesis | DEMONSTRATED / PLAUSIBLE | HIGH | Correct identification of top risks: overclaim, authority bleed, custody, premature integration. |
| 2. Risk Discipline & Status Rules | DEMONSTRATED | HIGH | Strong. Usable classification system (status, severity, control, kill-switch). No inflation. |
| 3. Epistemic Risks | DEMONSTRATED | HIGH | Load-bearing. Overclaim + laundering are primary early-phase threats. Must be enforced continuously. |
| 4. Governance Risks | DEMONSTRATED / PLAUSIBLE | HIGH | Authority bleed is CRITICAL. This section must remain hard law under pressure. |
| 5. Architecture Risks | DEMONSTRATED / IMPLEMENTABLE | HIGH | Immediate operational relevance. Integration-before-constitution is current phase choke point. |
| 6. Custody & Disclosure Risks | DEMONSTRATED / PLAUSIBLE | HIGH | Highest strategic sensitivity. Parent-company boundary + disclosure collapse are CRITICAL. |
| 7. IP & Legal Risks | DEMONSTRATED / PLAUSIBLE | MOD-HIGH | Solid but evolving. Novelty vs non-obviousness still requires external adversarial validation. |
| 8. Product & Market Risks | PLAUSIBLE | MODERATE | Correctly deferred. Premature productization is main trap. Keep downstream. |
| 9. Continuity & Identity Risks | SPECULATIVE / PLAUSIBLE | MODERATE | High symbolic gravity. Must remain strictly non-governing at this stage. |
| 10. Kill-Switch Matrix | DEMONSTRATED / IMPLEMENTABLE | HIGH | Core control layer. Clear, actionable, and enforceable. This is operational spine. |
| 11. Immediate Recommendations | DEMONSTRATED | HIGH | Strong posture: control now, observe selectively, stop on defined triggers. |

### Compressed Council Read

- **Hard Law Sections:** 2, 3, 4, 5, 6, 10, 11  
- **Evolving / Adversarial Review Required:** 7  
- **Deferred / Observational:** 8, 9  

### ζ-Pressure Summary

- No epistemic drift → Section 3 must hold  
- No authority bleed → Section 4 must hold  
- No custody failure → Section 6 must hold  
- No premature integration → Section 5 must hold  
- Kill-switches must remain real → Section 10 must be enforced, not admired  

### Final Compression Line

**If Sections 3, 4, 5, 6, and 10 hold, QEPE remains survivable. If any of those fail, the rest of the document becomes commentary.**
