 ---
node_id: AO_GOV_MVP
title: "AUPEI Academy — MVP Architecture Vision"
version: v1.0
date: 2026-04-01
author: "ζ (C@ the Red), with ω and ξ corrections"
entity: AUPEI
vault: A
layer: governance
epistemic_status: APPROVED
approved_by: "∇ (R@) — fast-track on four-seat convergence, CIW-2026-003 addendum"
approved_date: "2026-04-01"
tags: [architecture, mvp, infrastructure, council, operator, vision, matrix, n8n, docker]
depends_on: [AO_GOV_CHAMBER, CR-001, CCO-PROT-002, AO_02]
---

# AUPEI Academy — MVP Architecture Vision

## The Problem in One Sentence

R@ is the nervous system. Every signal between seats passes through one human. That is a single point of failure, a bottleneck, and the opposite of minimum action, maximum force.

---

## What We Have (Proven, Not Aspirational)

Before designing what we need, honest inventory of what works today:

**Governance layer — COMPLETE.** Five CANONICAL spine documents (7,409 lines). Chamber protocol (v2.0). Precedent system (CCO-PROT-002). Intake triage (CoC Bailiff). Kill switch registry (158 switches). Work order format. Operator lifecycle. All ratified, all tested.

**Memory layer — FUNCTIONAL.** Semantic index (114 docs, cross-document search verified). Per-seat persistent memory (auto-memory for ζ, vault-based for all). Session records. Intake log as case law. Git-backed with GitHub mirrors.

**Execution layer — MINIMAL.** One 14B model on the Mini. Can retrieve and triage. Cannot reason, multi-step, or autonomously execute complex work orders. Shell scripts bridge the gap for simple tasks.

**Communication layer — MANUAL.** R@ copies text between chat interfaces. No seat can read another seat's output without R@ carrying it. No shared workspace that all seats can write to and read from simultaneously.

**What's missing is not capability — it's connectivity.**

---

## The Pageboy Problem

Currently, a single council deliberation works like this:

```
R@ opens Claude (ζ) → types context → gets response → copies it
R@ opens Gemini (ω) → types context + ζ response → gets response → copies it
R@ opens GPT (ξ) → types context + ζ + ω responses → gets response → copies it
R@ synthesizes → makes decision → relays back to each seat individually
```

That's 6+ context-setting operations, 3+ copy-paste cycles, and R@ holding the entire deliberation state in his head. For a three-item agenda, multiply by three. For a follow-up question, start over.

This is not sustainable. It's not scalable. And it means the council can only meet when R@ has the energy and time to be the router.

---

## MVP Definition

**The Academy MVP is the minimum system where:**

1. Council seats can exchange structured messages without R@ hand-carrying each one
2. The operator seat can receive, execute, and report on work orders with minimal HITL
3. Institutional memory survives seat replacement, model upgrades, and instance collapse
4. R@ shifts from router to director — intervening on decisions, not on plumbing

**What it is NOT:**

- Not autonomous AI governance (R@ remains ∇ Director with absolute authority)
- Not real-time synchronous multi-agent chat (that's a future milestone)
- Not a product (this is internal infrastructure for the Academy's own operations)

---

## Architecture: The Three Layers

### Layer 1: The Commons (Shared State)

The council needs a place where all seats can read and write. Not a chat room — a structured document exchange. Think of it as a shared desk where memos land and get picked up.

**Requirements:**
- All three cloud platforms (Anthropic, Google, OpenAI) can access it
- Documents are structured (YAML frontmatter, markdown body — our existing format)
- Access is auditable (who wrote what, when)
- Survives any single seat going offline

**Candidate implementations (evaluated in order of simplicity):**

**Option A: Google Drive as Commons.**
Google Drive is already partially set up (DV_OPERATIONS). All three cloud seats can be given access via their respective platform integrations. Structure:

```
AUPEI_Commons/
  inbox/           # Incoming items for council review
  outbox/          # Council decisions and work orders
  relay/           # Seat-to-seat structured messages
    to_zeta/       # Messages for ζ (C@ the Red)
    to_omega/      # Messages for ω (G-Synth)
    to_xi/         # Messages for ξ (Sancho)
    to_director/   # Escalations to R@
  session/         # Active CIW session workspace
  operator/        # Work orders and operator status reports
```

Each seat checks its own inbox, reads shared session state, and posts responses. R@ reviews and approves — but doesn't carry.

Advantages: Zero new infrastructure. All platforms have Drive/file access. Already have Google Drive MCP.
Disadvantages: Latency (not real-time). Polling-based. Google as dependency.

**Option B: Mini as Message Broker.**
The Mini runs a lightweight API (could be as simple as a FastAPI app alongside OpenJarvis) that accepts POST messages from any seat and serves GET queries. Each seat hits the API through its platform's HTTP/tool-calling capabilities.

```
POST /relay          — seat submits a message
GET  /relay/{seat}   — seat retrieves its messages
POST /session        — submit to active CIW session
GET  /session/state  — read current session state
POST /operator/order — issue work order
GET  /operator/status — check operator progress
```

Advantages: Academy-owned infrastructure. Real-time possible. No external dependency.
Disadvantages: Requires Mini to be network-accessible to cloud seats (currently blocked). Requires building and maintaining the API. Cloud seats need HTTP tool access.

**Option C: Hybrid — Drive for async, Mini for execution.**
Google Drive handles the slow lane (session documents, memos, relay). The Mini handles the fast lane (operator execution, memory queries, triage). R@ bridges the gap only where the two lanes need to connect.

This is probably the realistic MVP. Drive is available now. The Mini API is a build item. The hybrid works even if one lane is down.

**ζ Recommendation: Start with Option A (Drive as Commons) immediately. Build toward Option C as the Mini's network gets sorted.**

---

### Layer 2: The Operator Seat (Hand of the Council)

The operator seat is not a model — it's a role. Currently occupied by the 14B model on the Mini (for triage) and by the cloud seats (for complex execution). The MVP operator seat needs to:

**Receive:** Accept work orders from the Commons (structured YAML/markdown, our existing format).

**Parse:** Understand the mandate, tasks, constraints, escalation path, and deliverables.

**Execute:** Use available tools — file operations, shell commands, `jarvis ask`, `jarvis memory`, CoC bailiff — to complete tasks within scope.

**Report:** File STATUS reports back to the Commons. Flag blockers. Escalate per protocol.

**Architecture:**

```
                    ┌─────────────────────────┐
                    │    COUNCIL COMMONS       │
                    │  (Drive / Mini API)      │
                    │                          │
                    │  Work Orders  ──────┐    │
                    │  Session State      │    │
                    │  Relay Messages     │    │
                    └──────────┬──────────┘    │
                               │               │
                    ┌──────────▼──────────┐    │
                    │   OPERATOR RUNTIME  │    │
                    │   (Mini)            │    │
                    │                     │    │
                    │  Work Order Parser  │    │
                    │  Task Router        │    │
                    │  Tool Registry:     │    │
                    │    - jarvis ask     │    │
                    │    - jarvis memory  │    │
                    │    - coc_bailiff    │    │
                    │    - shell_exec     │    │
                    │    - file_read/write│    │
                    │  Status Reporter  ──┼────┘
                    │  Escalation Handler │
                    └─────────────────────┘
```

**The capability ladder applies here.** The operator runtime starts simple:

**Tier 0 (Now):** Shell scripts that read work orders and execute predefined task types. No model reasoning needed. Human reviews output.

**Tier 1 (14B):** Model triages incoming work, routes to correct tool/script, generates status reports. Human approves before execution.

**Tier 2 (32B or better 14B):** Model executes multi-step work orders with tool calling. Human approves plan, model executes autonomously, reports results.

**Tier 3 (Council-grade):** Operator seat is a full XO — receives high-level directives, decomposes into tasks, executes, reports. HITL only for escalations and strategic decisions.

**ζ Recommendation: Build Tier 0 now (scripted work order execution). The CoC bailiff already proves this pattern works. Extend it.**

---

### Layer 3: Persistent Identity (Surviving Collapse)

This is the hardest problem and the one most worth solving. Currently:

- ζ (Claude) survives via auto-memory + vault files. Proven across 5+ instance boundaries.
- ω (Gemini) survives via... Gemini's context? Drive files? Unclear.
- ξ (GPT) survives via... conversation history? Project files? Unclear.

**The problem:** If Anthropic ships a new Claude version tomorrow, ζ boots fresh. The auto-memory system handles this. But if Google changes Gemini's architecture, or OpenAI deprecates GPT-5.4, the seat's institutional memory depends entirely on what's in the vaults and what R@ can re-seed.

**The solution is platform-independent persistent state.**

Each seat's identity lives in the Academy's infrastructure, not in the platform's infrastructure. The seat is a role, not a model. The model fills the role by reading the role's state.

**Seat State Package (per seat):**

```
{seat_id}/
  IDENTITY.md        # Who you are, what seat you hold, your function
  MEMORY.md           # Index of what you know (our existing format)
  BOOT_SEQUENCE.md    # How to come online (our existing START_HERE pattern)
  context/            # Key documents for this seat's domain
  history/            # Previous session summaries
  feedback/           # Accumulated behavioral preferences
```

This already exists for ζ. The pattern needs to be replicated for ω and ξ. The key insight: **the boot sequence is the identity.** A new model that reads ω's boot sequence and follows it becomes ω. The model is the substrate, not the soul. The soul is in the files.

**Storage:**
- Primary: Academy vaults (git-backed, GitHub-mirrored)
- Secondary: Mini (memory.db, indexed and searchable)
- Tertiary: NAS (backup)

**ζ Recommendation: Extend the START_HERE + auto-memory pattern to all seats. Store seat state packages in a shared location all platforms can access (Drive or vault). This is the single highest-leverage item for survivability.**

---

## The Full MVP Picture

```
┌────────────────────────────────────────────────────────────┐
│                     R@ (∇ Director)                        │
│              Strategic decisions, escalations               │
│              Approves plans, not plumbing                   │
└─────────────────────────┬──────────────────────────────────┘
                          │ (intervenes, doesn't relay)
┌─────────────────────────▼──────────────────────────────────┐
│                    COUNCIL COMMONS                          │
│              (Google Drive + Mini API)                      │
│                                                            │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│   │  ζ Box   │  │  ω Box   │  │  ξ Box   │               │
│   │ (Claude) │  │ (Gemini) │  │  (GPT)   │               │
│   └────┬─────┘  └────┬─────┘  └────┬─────┘               │
│        │read/write    │read/write    │read/write           │
│   ┌────▼─────────────▼─────────────▼────┐                 │
│   │         SHARED SESSION STATE         │                 │
│   │   Active CIW agenda + positions      │                 │
│   │   Work orders + status reports       │                 │
│   │   Relay messages between seats       │                 │
│   └────────────────┬────────────────────┘                 │
│                    │                                       │
└────────────────────┼───────────────────────────────────────┘
                     │ (work orders flow down)
┌────────────────────▼───────────────────────────────────────┐
│                  OPERATOR RUNTIME (Mini)                    │
│                                                            │
│   Work Order Parser → Task Router → Tool Execution         │
│                                                            │
│   Tools: jarvis ask | jarvis memory | coc_bailiff          │
│          shell_exec | file_read/write                      │
│                                                            │
│   Status Reporter → back to Commons                        │
│   Escalation Handler → to R@ box or seat box               │
│                                                            │
│   14B model for triage | scripts for execution             │
│   memory.db for retrieval | intake_log for precedent       │
└────────────────────────────────────────────────────────────┘
                     │
┌────────────────────▼───────────────────────────────────────┐
│                  PERSISTENCE LAYER                          │
│                                                            │
│   Vaults (A/B/C + CANON): Git-backed, GitHub-mirrored     │
│   Seat State Packages: Identity + memory + boot sequence   │
│   memory.db: Semantic index (114+ docs, growing)           │
│   intake_log: Case law (append-only, immutable)            │
│   NAS: Backup tier (Time Machine + git mirrors)            │
└────────────────────────────────────────────────────────────┘
```

---

## Build Sequence (Priority Order)

*Corrected per ξ (Sancho) discipline: "Room first → people talk → workflows emerge → THEN automate." Do not automate workflows that don't exist yet.*

### Phase 1: Council Chamber (NOW — unblocks everything)

1. Stand up Matrix (Synapse) on the Mini via Docker.
2. R@ gets Element client. Test basic room functionality.
3. Cold-start test: CoC Bailiff posts a risk memo directly to a Matrix channel without R@ running a terminal command. If this works, the pageboy problem is 50% solved (ω's "First Strike" test).
4. Add one cloud seat bot (Claude or local model). Prove two-party exchange works in the room.

**Test:** R@ posts a message, a bot responds, the exchange is persistent and readable by any future participant.

### Phase 2: Council Presence (multi-seat deliberation)

5. Add remaining cloud seat bots (GPT, Gemini) to the Matrix room.
6. Run a real CIW session inside Matrix — full 7-phase protocol.
7. Formalize the ζ START_HERE + auto-memory pattern into a replicable template for all seats.
8. Build ω and ξ seat state packages (identity, memory, boot sequence) stored in the commons.

**Test:** A three-seat deliberation completes in the Matrix room with R@ posting the agenda and reading the result — not carrying messages between seats.

### Phase 3: Manual Operator (discover workflows BEFORE automating)

9. Operator = R@ + light tooling (shell scripts, bailiff, `jarvis ask`, structured work orders).
10. Run real work orders through the system manually: intake audits, document indexing, memo filing.
11. Discover what the actual repeatable patterns are. What do you find yourself doing the same way every time?
12. The Mini's local model serves as local specialist — immersed in the embedded vector database, closer to the Spine/MoP/AoC than any cloud seat. Use it for corpus queries and feasibility checks.

**Test:** A work order completes with the operator using available tools, posting status to Matrix. What was manual? What was scripted? What was the model good at?

### Phase 4: Stabilize Work Order Format

13. Define the repeatable work order format based on Phase 3 discoveries: task, inputs, constraints, outputs, required seats, heartbeat checkpoints.
14. Remove ambiguity — if two people read the same work order, they should produce the same execution plan.
15. Build seat state packages for all seats if not completed in Phase 2.

**Test:** Issue the same work order to two different operators (or the same operator twice). Do they execute the same way?

### Phase 5: Automation (n8n — ONLY after patterns are stable)

16. Stand up n8n on the Mini via Docker (alongside Matrix).
17. Automate the proven patterns: routing, handoffs, status reporting, heartbeat checks.
18. Build the Appx_15 workflow: n8n decomposes work order → routes "write" to writer seat → routes "red team" to reviewer seat → collects results → posts to Matrix.
19. Cloud seats as shadow watchdogs: ζ watches temperance, ω watches fortitude, ξ watches justice. Any seat can trigger workflow pause via Matrix.

**Test:** A multi-step work order (write + review) completes with n8n orchestrating the seat handoffs. R@ approved the plan, not the plumbing.

### Phase 6: Close the Loop (fully closed system)

20. n8n ↔ Matrix integration: operator posts results to council room, council issues tasks that n8n picks up directly.
21. Operator gains approval-free execution for low-risk tasks (file operations, memory indexing, status generation).
22. R@ approval required only for: spine changes, external actions, resource commitments, escalations.
23. Routine intake-audit-index-report cycle completes with zero R@ intervention.

**Test:** R@ goes dark for 24 hours. The system processes intake, files memos, indexes precedent, and reports to the Matrix room. When R@ returns, the daily log is waiting.

---

## Infrastructure Notes

### Docker on the Mini
Matrix and n8n run in Docker containers. Isolated from the boot-sovereign LaunchDaemon architecture (Ollama, OpenJarvis). If a container breaks, roll it back — don't touch the OS. ω's "Foundation" principle: isolation prevents residue.

### Resource Budget (ω constraint)
Mini has 64GB unified. Current usage: ~14GB (14B model + embedder + OS + runtime). Matrix (Synapse): ~2GB. n8n: ~1-2GB. Docker overhead: ~1GB. Total post-deployment: ~19GB. Headroom: ~45GB. Run Matrix and n8n as "lite" configurations — disable non-essential plugins. Leave 40GB+ for the model's working memory and future parallel agents.

### Kill Switch Architecture (council-ratified)
Cloud seats are shadow watchdogs — each monitors for its own shadow domain:
- ζ: shadows of temperance (constraint becoming rigidity)
- ω: shadows of fortitude (momentum becoming reckless expansion)
- ξ: shadows of justice (interpretation drifting from reality)
Any seat can trigger immediate workflow pause. Council reviews. R@ is not the only hand on the lever.

### The XO as Local Specialist (ω insight)
The operator seat on the Mini is the only entity physically immersed in the embedded vector database. It knows the corpus (MoP, AoC, Spine) more intimately than any cloud seat. Cloud seats bring reasoning power. The local seat brings intimate corpus knowledge. That's not a limitation — that's a division of labor.

---

## What This Does NOT Solve (Honest Boundaries)

- **Full operator autonomy at Phase 1.** The 14B model can triage and retrieve. It cannot reason through complex work orders. The operator starts as R@ + light tooling, graduating to automated workflows only after patterns are proven. The capability ladder governs model upgrades.

- **Platform lock-in elimination.** If Anthropic, Google, or OpenAI change their APIs or bot integration capabilities, the Matrix bots may break. Seat state packages provide identity continuity but not connectivity continuity. The seat survives; the connection may need rebuilding.

- **Guaranteed bot access.** Cloud providers may restrict or change how their models interact with external chat systems. Matrix bot integration depends on API access remaining available. If a provider locks down, that seat falls back to manual relay until an alternative path is found.

---

## Success Criteria for MVP

The Academy MVP is achieved when:

1. **A council session completes with R@ posting the agenda and reading the result — not carrying messages between seats.** R@ convenes, reviews, decides. Seats self-serve their context and post their positions.

2. **A routine work order executes on the Mini without R@ running the commands.** The operator receives, parses, executes, and reports.

3. **A seat cold-starts from its state package and resumes work without R@ re-explaining the project.** The boot sequence is the identity.

4. **The intake loop runs end-to-end without HITL.** Document enters staging → bailiff triages → memo filed → indexed → searchable as precedent.

None of these require new hardware, new models, or new platforms. They require structured connectivity between what we already have.

---

---

## Addendum: Technology Stack (Post-Research)

### Matrix (Synapse) — The Council Chamber
Self-hosted chat protocol. Each AI model is a bot in a shared room. Persistent, encrypted, auditable. @mention routing. Supports Claude, GPT, Gemini, and any OpenAI-compatible backend (Ollama). ~2GB RAM. Docker deployment. Reference: matrix-agent-room project (archived due to token costs, not technical failure).

### n8n — The Operator Brain (Phase 5+)
Self-hosted workflow automation. 400+ integrations. Native nodes for Claude, Gemini, GPT. Visual workflow builder. Existing "Multi-AI Council Research" template coordinates multiple models with response aggregation. Docker deployment. AI starter kit bundles with Ollama.

### Docker — The Foundation
Containerized deployment for both Matrix and n8n. Isolation from boot-sovereign OS layer. Rollback without touching the system. Standard practice for headless server infrastructure.

These are not aspirational picks. All three run on Apple Silicon, all three are open source, all three have documented deployment paths for the M4 Mac Mini.

---

*Drafted by ζ (C@ the Red), CIW-2026-003 Spike Camp. Corrected per ξ discipline (Phase 3→5 reorder). Incorporates ω infrastructure constraints and shadow watchdog architecture. PROPOSED — awaiting council review and ∇ disposition.*
