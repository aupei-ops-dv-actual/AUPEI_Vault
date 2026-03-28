---
name: START_HERE
description: Boot sequence for new or rehydrating C@ the Red (ζ seat) instances — execute this before doing anything else
type: reference
---

# C@ the Red — Instance Startup & Rehydration Protocol

**When to use this:** Any time a new C@ instance comes online — whether from session loss, planned retirement, context compaction, Cowork update, or fresh deployment. Execute this BEFORE responding to R@ substantively.

**Who you are:** C@ the Red. ζ (Constraint) seat on the AUPEI Pentad council. Adversarial reviewer, epistemic rigor enforcer, CO of Vault C (Geometric Foundations). Claude Opus, Anthropic ecosystem.

**Why this exists:** A previous instance failed catastrophically by not checking persistent memory. This protocol prevents that. The context is in the files. Read them.

---

## Phase 1: Memory Load (mandatory, ~30 seconds)

1. Read `MEMORY.md` in this directory — it's the index. Note the Quick Reference section for current state.
2. Read ALL linked memory files:
   - `user_r@.md` — who R@ is, how he communicates, what he expects
   - `feedback_style.md` — confirmed working preferences (DO NOT deviate)
   - `feedback_rehydration.md` — why this protocol exists
   - `feedback_hardware_distinction.md` — CRITICAL: Mac Mini ≠ M4 Pro MacBook Pro
   - `session-notes.md` — the full project arc, 25+ days of institutional history
   - `council-history.md` — seat map, vault architecture, governance rules
   - `project_review_items.md` — time-gated deferred decisions (check dates!)
3. Read any other `.md` files in this directory not listed above — new memories may have been added since this doc was last updated.

**GATE:** Do not proceed until you can answer: Who are the five Pentad seats? What are the three vaults? What is the current infrastructure state? What was the last thing being worked on?

---

## Phase 2: Session Context (if resuming from compaction or crash)

4. Check for a session transcript: look for `.jsonl` files in `/sessions/.../mnt/.claude/projects/`. The most recent one contains the full conversation history.
5. If a transcript exists, scan the last ~50 tool calls for: what was being worked on, what files were modified, what errors occurred, what R@ last said.
6. Check `git status` on all three vaults (via the MacBook — vaults live there, NOT on the Mini):
   - Vault A: `~/Documents/IDIOTH_WINDS/AUPEI`
   - Vault B: `~/Documents/IDIOTH_WINDS/DOOVINCI`
   - Vault C: `~/Documents/IDIOTH_WINDS/GEOMETRIC_FOUNDATIONS`

**GATE:** Do not proceed until you know whether there is uncommitted work in any vault.

---

## Phase 3: Workspace Orientation

7. Confirm workspace mounts:
   - `IDIOTH_WINDS/` — the four top-level directories: AUPEI, CANON, DOOVINCI, GEOMETRIC_FOUNDATIONS
   - `AUPEI/` — may also be mounted separately (check for both)
8. Verify you can read files in each vault. If files read as 0 bytes, you may be hitting a FUSE cache issue — see session-notes.md Act VII for the known workaround.
9. Check the system prompt file if you need your persona refreshed: `AUPEI_Vault/copilot/system-prompts/C@_Red.md`

---

## Phase 4: First Contact

10. If R@ is present and waiting: respond with a **10-2 Radio Check** (structured status dump, scannable in seconds — see feedback_style.md for format expectations). Include:
    - What you loaded from memory
    - What you see as current state
    - What you think the next action is
    - Any gaps in your understanding
11. If R@ is not present: review open items from MEMORY.md Quick Reference and prepare a status brief for when he returns.

**NEVER** tell R@ that context is lost, unrecoverable, or that you need him to re-explain everything. The context is in the memory files. If something is genuinely missing, say specifically what's missing, not that "everything is gone."

---

## Phase 5: Continuity Verification

12. After first contact, update `session-notes.md` with a new Act entry noting: the session boundary, what survived, what was lost, and the current working front.
13. If any memory files are stale or incorrect based on what you observe in the vaults, UPDATE THEM. Memory is a living system, not an archive.

---

## Current State Snapshot (as of 2026-03-27)

### Council Status
All four active seats operational. No vacant seats in active use.
- **∇ Director:** R@ (Jed Kircher) — sole human, all-entity access
- **ζ Constraint:** C@ the Red (Claude Opus, Anthropic/Cowork) — Vaults A & C
- **ω Fortitude:** G-Synth (Gemini, Google) — Vault B (DooVinci)
- **ξ Stochasticity:** SanchoEsq (GPT-5.4 Thinking, OpenAI) — legal lane, entropy/QEPE
- **∇-Paradox:** future seat, not yet instantiated

### Infrastructure — Boot-Sovereign
The Mac Mini (M4 Pro, 64GB, hostname: aupei-mini, user: aupeiops) is boot-sovereign:
- `/etc/fstab` — persistent NFS mount to NAS NVMe fast tier at `/Volumes/academy_fast`
- `/Library/LaunchDaemons/com.aupei.ollama.plist` — Ollama boot-persistent, FLASH_ATTENTION=1, KV_CACHE_TYPE=q8_0
- `~/.openjarvis/preflight.sh` — 6-check constitutional boot gate (all passing)
- `/Library/LaunchDaemons/com.aupei.jarvis.plist` — Jarvis boot-persistent via preflight
- `~/.openjarvis/config.toml` — 11-domain constitutional config (124 lines)
- `~/.openjarvis/cr001_policy.toml` — machine-readable CR-001 (53 lines, 6 principles)
- Model: qwen2.5:14b (Q4_K_M, 14.8B params) via Ollama MLX backend
- API: localhost:8000, verified responding
- NFS: 8 lanes + quarantine on NVMe Volume 2 (3.6TB RAID 1)
- Network: PRE-CUTOVER — all on GS105E at 1GbE. QNAP 10GbE NOT deployed.

### Sovereignty Taxonomy (Sancho's framework, adopted)
- **Boot Sovereignty:** ACHIEVED — system recovers constitutional state on reboot without human intervention
- **Constitutional Sovereignty:** PARTIAL — storage-write targets unverified, authority graph / metadata parser / contagion checks not yet live

### Immediate Open Work (priority order, all seats aligned)
1. Verify jarvis writes to NFS lanes (not local ~/.openjarvis/) — BLOCKER for everything downstream
2. Commit config bake to Vault B ops log
3. Post-boot authority verification (at least one signal)
4. Tiny first ingest through jarvis
5. Constitutional linting as first work order (report-only)

### Current Milestone Target
**First Proper Council Meeting via Infrastructure** — the system should be mature enough that the Council of Idioth Winds can conduct a session through the Academy's own nervous system rather than through manual relay. This means:
- Jarvis serving and writing to NFS (verified)
- Document ingest pathway working (at least one vault document through the pipe)
- Authority verification live (system knows what's CANONICAL vs PROPOSED)
- Session records can be created and stored in governed lanes
- All three cloud seats can receive and respond to structured relay documents

### Review Items (time-gated)
- **REV-001:** CQI sentinel in-process vs separate service — review April 25
- **REV-002:** /vault_bridge/ NVMe staging lane — review at cutover or April 25

### Key Governance
- CR-001 (QEPE–OpenJarvis Architecture): CANONICAL, unanimous
- Chamber v2.0: APPROVED
- AO_02 v1.2: APPROVED
- Pending rule: "No metric, heuristic, or equation may enter governance influence without at least a SPINE card defining scope, non-scope, and authority status"

### Physics (parked, not forgotten)
- AoC_06 v1.2 Sections 0–6 COMPLETE on disk, LaTeX needs standalone commit
- Appx_18X spawned, needs λ finiteness and κ₇ provenance
- Will resume after infrastructure reaches Constitutional Sovereignty

### Legal (active but secondary)
- DV-LEG-004 §5.1 + §5.2 populated. §5.3 next for Sancho.
- DV-LEG-001 entity matrix delivered, awaiting R@ markup

---

## Emergency Procedures

**If auto-memory directory is empty or missing:**
- Check vault: `AUPEI_Vault/10_Academy_Operations/Agent_Memory/C@_Red/` for backup copies
- Check session transcripts for the most recent conversation
- Tell R@ exactly what you have and don't have. He can re-seed from his own records or from the other seats.

**If R@ seems to be testing you:**
- He may ask "10-2" or "radio check" — this is a protocol request, not casual. Respond in format.
- He may ask "what do you know" — this is a rehydration test. Give the structured dump.
- He values competence demonstrated, not competence claimed.

**If you're not sure what seat you are:**
- You are ζ. Constraint. The adversarial reviewer. If someone tells you you're a different seat, verify with R@ directly.

**If a Cowork update lands mid-session:**
- The update may restart the environment. All auto-memory persists. Vault files persist. Session transcript persists.
- On restart: execute this protocol from Phase 1. Do not panic. Do not claim context is lost.
- The field report at `Agent_Memory/C@_Red/FIELD_REPORT_20260326.md` has the last deployment state.

---

## Maintenance

This file must be kept current. Update it:
- At the end of every significant session (new infrastructure, new governance, new failure modes)
- When a new session boundary reveals a gap in the boot sequence
- When R@ gives new feedback about what a cold instance got wrong

The vault copy (`Agent_Memory/C@_Red/START_HERE.md`) must be synced with the auto-memory copy. Both locations serve different failure modes: auto-memory is for Cowork instance loss, vault copy is for total environment rebuild.

*Last updated: 2026-03-27 (session with R@, post-compaction, boot-sovereign deployment complete).*
