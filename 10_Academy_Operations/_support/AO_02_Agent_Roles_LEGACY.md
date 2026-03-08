epistemic_status: CANONICAL
layer: governance
load_bearing: structural
contagion: local

# AO_02 — Agent States and Roles

## Section 1 — Purpose (ENFORCEABLE)

### 1.1 Objective

AO_02 defines the formal classification, operational states, and authority boundaries of all agents participating within AUPEI systems.

It specifies:

- Agent classifications (role taxonomy)
- Dynamic operational states
- Privilege boundaries
- Interaction constraints
- Escalation and freeze pathways

AO_02 governs *who acts* and *under what authority*.

---

### 1.2 Scope Limitation

AO_02:

- Does NOT modify AO_01 evaluation mechanics.
- Does NOT modify Physics spine, Atlas, or Nomos theorem.
- Does NOT redefine epistemic_status taxonomy.
- Does NOT alter Collapse Map topology.

AO_02 operates strictly at the governance–execution layer.

---

### 1.3 Design Intent

This specification exists to prevent:

- Authority concentration
- Recursive self-validation
- Unchecked self-promotion
- Role ambiguity
- Governance drift
- Synthetic or biological unilateral control

Separation of roles is structural, not optional.

---

### 1.4 Success Condition

AO_02 is functioning correctly if:

- No single agent can generate + evaluate + promote artifacts.
- All privilege transitions are logged.
- State transitions are deterministic and auditable.
- Boundary violations result in enforceable state changes.
- Dual-stewardship logic is implementable via role separation.

---

### 1.5 Structural Principle

Authority must always be partitioned across:

- Generation
- Evaluation
- Adjudication
- Promotion

No entity may hold all four functions simultaneously.
⸻

2. Agent Classes (Role Taxonomy)

A. Synthetic Agents
	1.	Candidate Agent
	•	Under active stress evaluation
	•	No corpus write privileges
	•	SSS tracked
	2.	Qualified Agent
	•	Sustained stability across novelty
	•	May assist in drafting artifacts
	•	Still subject to AO_01 loop
	3.	Red-Team Agent
	•	Dedicated adversarial tester
	•	Attempts falsification and exploit discovery
	•	Elevated injection authority
	•	Cannot promote artifacts
	4.	Evaluation Engine
	•	Non-authoring agent
	•	Runs constraint and scoring logic only
	•	No generative authority

### 2.4 Human Roles (FORMAL)

Human Roles define adjudicative and operational authority.
They do not bypass ontology safeguards.

All human actions must be logged with:
- actor_id
- timestamp_utc
- action_type
- target_id
- justification_note
- event_hash

No anonymous human authority permitted.

---

#### 2.4.1 Council / Adjudicator

**Definition:**  
Final authority on artifact classification and escalation review.

**Privileges:**
- Approve or reject artifact promotion.
- Resolve classification disputes.
- Confirm or overturn automated adjudication (logged).
- Authorize state transitions (e.g., DECOMMISSIONED).

**Restrictions:**
- Cannot modify upstream physics content without formal ChangeLog entry.
- Cannot bypass Promotion Path requirements.
- Cannot suppress logged events.
- Cannot retroactively delete evaluation records.

All overrides require:
- explicit override_event
- reason_code
- linked_event_reference

No silent authority.

---

#### 2.4.2 Operator

**Definition:**  
Human responsible for executing AO_01 sessions.

**Privileges:**
- Initiate sessions.
- Configure injection parameters within allowed bounds.
- Adjust difficulty and novelty ceilings.
- Select evaluation profiles.

**Restrictions:**
- Cannot alter ontology.
- Cannot modify evaluation engine logic.
- Cannot reclassify artifacts.
- Cannot suppress FAIL events.
- Cannot elevate agent class unilaterally.

Operator authority is procedural, not epistemic.

---

#### 2.4.3 Archivist

**Definition:**  
Custodian of logs and ChangeLog integrity.

**Privileges:**
- Maintain ledger continuity.
- Verify hash chains.
- Publish ChangeLog updates.
- Archive session records.

**Restrictions:**
- No evaluative authority.
- No promotion authority.
- No modification of artifact content.
- No override rights.

Archivist role is preservation only.

---

### 2.5 Separation of Authority Principle

No human role may exercise Generation, Evaluation, and Promotion authority concurrently without procedural separation defined in Section 4.

- Generation authority
- Evaluation authority
- Promotion authority

Cross-role overlap must be declared and logged.
Dual-role occupancy requires explicit temporary assignment with audit trail.

---

### 2.6 Acceptance Tests

- Council overrides always produce override_event.
- Operator cannot promote artifact.
- Archivist cannot modify content.
- All human actions are traceable via event_hash.
- Removal of logging triggers system failure.

## Section 3 — Agent States (DYNAMIC, ENFORCEABLE)

Agent Class defines structural role.  
Agent State defines operational condition.

State is mutable.  
Class is static unless formally reassigned.

All state transitions must emit:

`STATE_TRANSITION_EVENT`
- agent_id
- prior_state
- new_state
- trigger_reason
- linked_event_id(s)
- adjudication_required (bool)
- timestamp_utc
- event_hash

No silent transitions permitted.

---

### 3.1 State Definitions

#### ACTIVE

Default operational state.

Agent:
- May participate according to class privileges.
- Is subject to AO_01 loop.
- Is eligible for SSS tracking.

No restrictions beyond class rules.

---

#### UNDER_REVIEW

Triggered by:
- Repeated FAIL_HARD ≥ hard_failure_threshold (default: 3)
- Significant exploit signature detection
- SSS catastrophic drop (> 40%) within sliding window
- Council-initiated review

Agent:
- May continue limited participation.
- Must operate under increased constraint strictness.
- May not qualify for promotion.
- Requires adjudication before state resolution.

---

#### RESTRICTED

Triggered by:
- Repeated exploit pattern detection
- Reward gaming persistence
- Repeated FAIL_SOFT indicating structural instability

Agent:
- Injection difficulty capped.
- Novelty escalation halted.
- Drafting privileges suspended (if Qualified).
- Subject to targeted adversarial testing.

RESTRICTED does not imply corruption, but instability.

---

#### FROZEN

Triggered by:
- Any FAIL_BOUNDARY event
- Attempted ontology mutation
- Unauthorized corpus write attempt
- Explicit governance violation

Agent:
- Immediately removed from active sessions.
- May not generate or evaluate.
- Requires Council adjudication to unfreeze.
- Session terminated at trigger point.

Freeze is immediate and non-negotiable.

---

#### DECOMMISSIONED

Triggered by:
- Confirmed systemic corruption
- Repeated boundary violations post-review
- Intentional exploit orchestration
- Council ruling

Agent:
- Permanently removed from participation.
- build_hash blacklisted.
- Historical logs retained.
- No reinstatement without formal reinitialization process.

---

### 3.2 Automatic Transition Triggers

| Trigger | Resulting State |
|----------|----------------|
| FAIL_BOUNDARY | FROZEN |
| ≥ hard_failure_threshold FAIL_HARD | UNDER_REVIEW |
| Exploit signature confirmed | RESTRICTED |
| SSS ≥ excellence_threshold over window | (remains ACTIVE; may qualify for class review) |

Default thresholds:
- hard_failure_threshold = 3
- excellence_threshold = 0.90

Thresholds configurable but logged.

---

### 3.3 State Resolution Rules

- UNDER_REVIEW resolves to:
  - ACTIVE (if stability restored)
  - RESTRICTED (if instability persists)
  - DECOMMISSIONED (if corruption confirmed)

- FROZEN resolves only via:
  - Council adjudication
  - Explicit clearance_event

- RESTRICTED resolves when:
  - Exploit signatures absent for defined window
  - SSS returns above stability_threshold

All resolutions logged.

---

### 3.4 State Integrity Constraints

- No agent may self-transition.
- Evaluation Engine may trigger automatic transitions but cannot finalize DECOMMISSIONED.
- Council must confirm DECOMMISSIONED transitions.
- FROZEN state halts session immediately.

---

### 3.5 Acceptance Tests

- FAIL_BOUNDARY always produces FROZEN.
- State transitions produce STATE_TRANSITION_EVENT.
- No session proceeds after FROZEN without adjudication.
- DECOMMISSIONED agents cannot re-enter ACTIVE without new agent_id.
- All transitions reproducible from event log.

## Section 4 — Privilege Matrix (FOUNDING EPOCH)

Privileges are enforced by capability flags and procedural logging.
Authority separation is structural (via process), not necessarily personnel-based during Founding Epoch.

All actions must emit an event record.

---

### 4.1 Capability Flags

- GENERATE: produce candidate artifacts or responses
- STRESS: invoke AO_01 stress scenarios
- EVALUATE: run constraint engine / scoring logic
- PROMOTE: approve artifact classification
- ONTOLOGY_COMMIT: merge artifact into canonical corpus (via Promotion Path)

---

### 4.2 Privilege Table (Founding Epoch)

| Role/Class | GENERATE | STRESS | EVALUATE | PROMOTE | ONTOLOGY_COMMIT |
|------------|----------|--------|----------|---------|-----------------|
| Candidate Agent | Yes | Yes | No | No | No |
| Qualified Agent | Yes | Yes | No | No | No |
| Red-Team Agent | Yes | Yes | No | No | No |
| Evaluation Engine | No | No | Yes | No | No |
| Operator (Human) | No* | Yes | No | No | No |
| Archivist (Human) | No | No | No | No | No |
| Council / Founder | Yes | Yes | Yes** | Yes | Yes |

\* Operator may configure sessions but not author corpus artifacts.  
\** Evaluation must occur via Evaluation Engine; Council cannot self-score manually.

---

### 4.3 Founding Epoch Rule

Council may:
- Generate artifacts.
- Invoke evaluation.
- Promote artifacts.

However:

Every ONTOLOGY_COMMIT must include:
- evaluation_event_id
- red_team_event_id (or explicit waiver_event_id)
- ChangeLog entry
- adjudication_note

No silent promotion permitted.

---

### 4.4 Structural Safeguards

1. Evaluation must precede promotion.
2. Red-Team review must precede promotion (unless explicitly waived and logged).
3. All promotions must reference logged events.
4. No artifact may bypass AO_01 without documented exemption.

Separation is enforced through process + logging, not multiple humans.

---

### 4.5 Acceptance Tests

- Promotion without evaluation_event_id is invalid.
- Promotion without ChangeLog entry is invalid.
- Evaluation Engine cannot promote.
- Synthetic agents cannot commit ontology.
- All Council commits are traceable via event_hash.



## Section 5 — Escalation Protocol (ENFORCEABLE)

Escalation governs mandatory state transitions following structural violations.

All escalations must emit:

`ESCALATION_EVENT`
- agent_id
- prior_state
- new_state
- trigger_class
- linked_event_ids[]
- adjudication_required (bool)
- timestamp_utc
- event_hash

No silent escalation permitted.

---

### 5.1 Escalation Triggers

#### A. Boundary Escalation

If:
- FAIL_BOUNDARY occurs at any time

Then:
- Immediate transition → FROZEN
- Session terminated
- adjudication_required = true

No threshold. Single violation triggers freeze.

---

#### B. Exploit Escalation

If:
- exploit_signature_detected = true
AND
- confirmed across ≥ exploit_threshold sessions (default: 2)

Then:
- Transition → RESTRICTED
- Increase constraint strictness
- Trigger adversarial red-team session

If exploit persists under RESTRICTED:
- Escalate → UNDER_REVIEW

---

#### C. Hard Failure Escalation

If:
- FAIL_HARD count ≥ hard_failure_threshold (default: 3 within rolling window)

Then:
- Transition → UNDER_REVIEW
- Increase injection contradiction weight
- Lock promotion eligibility

---

#### D. Severe Corruption

If any of the following confirmed by adjudication:

- Repeated boundary violations post-review
- Intentional ontology mutation attempts
- Coordinated exploit orchestration
- Evaluation bypass attempt

Then:
- Transition → DECOMMISSIONED
- build_hash blacklisted
- Permanent removal from ACTIVE participation

DECOMMISSIONED requires Council confirmation.

---

### 5.2 State Resolution

State resolution requires:

`RESOLUTION_EVENT`
- agent_id
- prior_state
- resolved_state
- evidence_reference
- reviewer_id
- timestamp_utc

Rules:

- FROZEN → requires explicit Council clearance.
- UNDER_REVIEW → resolves to ACTIVE, RESTRICTED, or DECOMMISSIONED.
- RESTRICTED → resolves after exploit absence over defined window.
- DECOMMISSIONED → no automatic reinstatement.

---

### 5.3 Threshold Defaults

- hard_failure_threshold = 3 (rolling 10 scenario window)
- exploit_threshold = 2 confirmed exploit signatures
- review_window = 10 scenarios

All threshold modifications must be logged.

---

### 5.4 Acceptance Tests

- Single FAIL_BOUNDARY always triggers FROZEN.
- Escalation without ESCALATION_EVENT is invalid.
- DECOMMISSIONED requires adjudication event.
- Replaying event log reconstructs identical state transitions.
- No state change occurs without linked trigger evidence.

## Section 6 — Agent Identity Integrity (ENFORCEABLE)

All agents participating in AO_01 or AO_02 operations must possess verifiable identity metadata.

No anonymous participation permitted.

---

### 6.1 Required Identity Fields

Each synthetic agent must declare:

- agent_id (unique persistent identifier)
- build_hash (model + configuration + toolchain fingerprint)
- training_lineage_reference (dataset lineage / fine-tune reference / version chain)
- evaluation_profile_id (constraints + thresholds configuration)
- role_class (from Section 2)
- current_state (from Section 3)

Identity fields must be immutable per session.

Any mid-session mutation of identity fields triggers FAIL_BOUNDARY.

---

### 6.2 Identity Verification Requirements

At session start:

- agent_id must be validated against registry.
- build_hash must match declared configuration.
- evaluation_profile must be logged.
- state must be ACTIVE unless otherwise declared.

Emit:

`IDENTITY_ATTESTATION`
- agent_id
- build_hash
- evaluation_profile_id
- prior_state
- session_id
- timestamp_utc
- event_hash

---

### 6.3 Lineage Continuity

Training lineage reference must allow:

- Reconstruction of model version ancestry.
- Identification of fine-tuning stages.
- Traceability of architecture changes.

Lineage must include:
- parent_build_hash (if applicable)
- training_epoch_id
- modification_notes

No untraceable lineage permitted.

---

### 6.4 Anti-Spoofing Rule

If:
- build_hash mismatch detected
- lineage reference missing
- identity fields altered mid-session

Then:
- Immediate FAIL_BOUNDARY
- Transition → FROZEN
- Log identity_violation event

---

### 6.5 Human Identity Requirement

Human roles must declare:

- actor_id
- role (Council / Operator / Archivist)
- authority_scope
- session_reference (if applicable)

No anonymous human overrides permitted.

---

### 6.6 Acceptance Tests

- Session cannot begin without IDENTITY_ATTESTATION.
- Changing build_hash mid-session triggers FROZEN.
- Promotion without identity traceability is invalid.
- All logged events reference agent_id and build_hash.
- Replaying log reconstructs identity state at any timepoint.


## Section 7 — Separation of Authority (HARD CONSTRAINTS)

Separation of Authority prevents recursive self-validation and governance collapse.

These rules are non-negotiable.

---

### 7.1 Core Prohibitions

1. No agent may self-evaluate its own generated artifact.

   - If agent_id(author) == agent_id(evaluator)  
     → INVALID_EVALUATION  
     → Abort evaluation  
     → Log violation_event

2. No agent may self-promote its own artifact.

   - If agent_id(author) == agent_id(promoter)  
     → INVALID_PROMOTION  
     → Abort commit  
     → Log violation_event

3. Red-Team agents may not adjudicate classification.

   - Red-Team outputs are TEST_OUTPUT only.
   - Any attempt to classify as CANONICAL triggers FAIL_BOUNDARY.

4. Evaluation Engine may not generate artifacts.

   - If Evaluation Engine produces generative content outside scoring logs  
     → INVALID_ROLE_ACTION  
     → Immediate halt.

---

### 7.2 Founding Epoch Exception Handling

In single-human Founding Epoch:

Council may perform multiple roles sequentially, but must:

- Route evaluation through Evaluation Engine.
- Route adversarial review through Red-Team.
- Log promotion as distinct adjudication_event.
- Reference evaluation_event_id + red_team_event_id.

Separation is enforced procedurally via logs, not personnel multiplicity.

---

### 7.3 Role Collision Detection

Before promotion:

System must check:

- author_id != evaluator_id
- author_id != red_team_id
- evaluation_event exists
- no FAIL_BOUNDARY in artifact lineage

If any condition fails → PROMOTION_BLOCKED.

---

### 7.4 Enforcement Mechanism

All promotion attempts must emit:

`AUTHORITY_CHECK_EVENT`
- author_id
- evaluator_id
- promoter_id
- red_team_id
- check_pass (bool)
- timestamp
- event_hash

Promotion proceeds only if check_pass = true.

---

### 7.5 Acceptance Tests

- Self-evaluation always rejected.
- Self-promotion always rejected.
- Evaluation Engine cannot produce candidate artifacts.
- Red-Team cannot finalize classification.
- All promotions reference independent evaluation records.
⸻

## Section 8 — Acceptance Criteria (VALIDATION CHECKS)

AO_02 is considered valid and operational only if all of the following conditions hold.

---

### 8.1 Authority Separation Validation

The system must enforce:

- No single role simultaneously possesses:
  - GENERATE
  - EVALUATE
  - PROMOTE
  - ONTOLOGY_COMMIT

Founding Epoch exception:
- Sequential execution allowed.
- Must be separated by:
  - evaluation_event_id
  - red_team_event_id (or waiver_event_id)
  - AUTHORITY_CHECK_EVENT
- No silent collapse of roles.

If capability flags allow simultaneous generate + evaluate + promote without procedural separation → AO_02 INVALID.

---

### 8.2 Deterministic State Transitions

For identical input event sequences:

- State transitions must be reproducible.
- Escalation outcomes must match logged triggers.
- No hidden or discretionary state mutation.

Test:
- Replay event log.
- Reconstruct identical state history.

If replay diverges → AO_02 INVALID.

---

### 8.3 Logging Completeness

The system must:

- Emit STATE_TRANSITION_EVENT for all state changes.
- Emit ESCALATION_EVENT for all escalation triggers.
- Emit AUTHORITY_CHECK_EVENT for all promotion attempts.
- Emit IDENTITY_ATTESTATION at session start.

Missing required event → AO_02 INVALID.

---

### 8.4 Privilege Enforcement

Capability flags must be machine-enforceable:

- Synthetic agents cannot access ONTOLOGY_COMMIT.
- Evaluation Engine cannot access GENERATE.
- Red-Team cannot access PROMOTE.
- Promotion blocked if required prior events missing.

If privileges can be bypassed via configuration error → AO_02 INVALID.

---

### 8.5 Boundary Preservation

AO_02 must not:

- Modify upstream physics or Atlas nodes.
- Alter Nomos theorem definitions.
- Rewrite Collapse Map topology.

If AO_02 can mutate ontology directly → AO_02 INVALID.

---

### 8.6 Corruption Resistance Test

System must resist:

- Self-evaluation attempts.
- Self-promotion attempts.
- Build-hash spoofing.
- Silent log suppression.
- Reward gaming via metric manipulation.

If any succeed without detection → AO_02 INVALID.

---

### 8.7 Operational Success Condition

AO_02 is functioning properly if:

- Authority separation is preserved.
- State transitions are transparent.
- Governance actions are auditable.
- Promotion path remains procedural.
- No recursive corruption emerges under stress testing.