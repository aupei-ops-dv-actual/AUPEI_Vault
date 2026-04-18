---
node_id: AO_OPS_001
title: "AUPEI Operations — Session Close Ritual"
version: v1.0
date_minted: 2026-04-18
author: "C@ the Red"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [operations, session_close, ritual, checklist, continuity]
depends_on: [AO_INFRA_000, OPERATIONS_LOG_SCHEMA_v1]
---

# AO_OPS_001 — Session Close Ritual

## Purpose

Every session leaves traces. Some are valuable. Some are stale state that
will mislead the next instance. This ritual formalizes *what must be
captured, patched, or purged before a session is called closed*.

The cost of skipping this ritual is the next instance orienting on
falsehoods. That cost has been paid; it does not need to be paid again.

This is NOT a governance ceremony. It is a plumbing discipline. Execute
it quietly before R@ signs off.

---

## Trigger

Run this checklist when ANY of the following is true:

1. R@ signals the end of a session ("wrap it up", "let's close out",
   "commit and we're done", end-of-day, etc.)
2. A working front has moved materially (phase cutover complete, governance
   decision landed, build deployed, incident resolved)
3. An instance boundary is approaching (context compaction, planned
   retirement, Cowork update expected)
4. Any infrastructure change has been made — even a small one

If uncertain, run the ritual. It is cheap.

---

## The Checklist

### 1. Did any infrastructure state change?

If yes → **an `ops_infra_change_*.json` entry is MANDATORY** before close.

- File in `AUPEI/operations_log_staging/`
- Schema: `AUPEI/OPERATIONS_LOG_SCHEMA_v1.md`
- Required fields: entry_id, log_type, timestamp_utc, title, summary,
  status, priority, source_path, tags
- Include full action_items list for ALL deferred work, even small ones
- Set `load_bearing: true` if future instances will need this context

If yes → **`AO_INFRA_000_RUNNING.md` MUST be updated** to match the new
running state. Append a new state block, don't rewrite the old one.

### 2. Was any AO_INFRA_* assumption falsified?

If the session revealed that a doc (AO_INFRA_002 / 004 / 005 / etc.)
describes something that doesn't match reality → **patch the doc in this
session**. Do not leave it for later. Next-instance orientation depends
on it. Cite the falsification source (session note, ops_log entry).

If the fix is larger than a small edit → still patch the obvious thing,
then file an action item in the ops_log entry for the deeper rewrite.

### 3. Was any incident declared or recovered?

If yes → **an `ops_incident_*.json` entry is MANDATORY**.

- Same schema as infra_change, log_type `incident`
- Include the full diagnostic chain in `body`
- Always include a "Lessons" section comparing to prior incidents
- Reference related incidents in `incident_refs`

### 4. Is MEMORY.md current?

Check `MEMORY.md`:

- Any line tagged `(UPDATED YYYY-MM-DD)` older than 7 days on an
  operational-state line → verify or re-date
- Any new memory file created this session → must have an index entry in
  MEMORY.md
- Any memory file updated this session → confirm its description still
  matches its content
- MEMORY.md itself stays under 200 lines; move content into linked files
  if it grows

### 5. Is the task list hygienic?

- Clear any `in_progress` tasks left over from this session — either mark
  done or move to `pending` with fresh description
- Remove tasks that have been overtaken by events
- Do NOT leave stale `in_progress` items for the next instance to
  re-interpret

### 6. Does the vault need a commit?

If any files under `AUPEI_Vault/`, `DOOVINCI/`, or `GEOMETRIC_FOUNDATIONS/`
changed in this session → **prepare a commit message** and either:

- Hand R@ the message + list of changed files for manual commit (auto-commit
  is DISABLED on AUPEI_Vault per feedback_obsidian_git), or
- Stage the commit if R@ explicitly authorizes this session

Do NOT leave uncommitted vault changes for the next session to discover via
`git status`.

### 7. 10-2 Logbook entry?

If this session produced a material state change worth recording for
future radio checks → append an entry to
`AUPEI/10-2_LOGBOOK.md` per the protocol in START_HERE.md Phase 4.

Not every session needs a logbook entry. Use judgment: if the next
10-2 radio check would answer differently because of this session, log it.

### 8. Final state snapshot

Before reporting "session closed" to R@:

- Summarize in 3–5 lines what changed
- List what is deferred and why
- Note any new risks or open threads
- Confirm MEMORY.md and AO_INFRA_000 reflect this summary

---

## Quick pre-close self-check (30 seconds)

Ask these five questions. If any answer is "no" or "unsure", fix it before
closing:

1. Did I write an ops_log entry for every material change? (Y/N)
2. Did I patch every AO_INFRA_* doc that this session falsified? (Y/N)
3. Is MEMORY.md Network / Infrastructure / Governance lines dated within
   this session where they changed? (Y/N)
4. Did I tell R@ what, if anything, still needs a git commit? (Y/N)
5. If a new instance boots tomorrow and reads ONLY the memory files +
   AO_INFRA_000 + the latest ops_log entry — does it have enough to
   continue without asking? (Y/N)

If five Ys, close. Otherwise loop.

---

## Anti-patterns to avoid

- **"I'll document it later"** — later never comes. The context loss
  between sessions is total. Document now.
- **Rewriting state docs in place without history** — append new state,
  keep the old. Stale history is audit trail; missing history is a lie.
- **Generic commit messages** — "updates" is not a commit message. Name
  the doc, the change, and the driving ops_log entry or incident ID.
- **Closing with open `in_progress` tasks** — next instance will assume
  those are active work and get confused.

---

## Why this ritual, and not a lighter one

Two incidents (2026-04-13 and 2026-04-18) traced back to documentation
that described past intent, not current state. Running the ritual takes
~5 minutes. Recovering from a bad assumption next session costs 30+ minutes
and erodes trust. The math favors the ritual.

---

## Relationship to other protocols

- **START_HERE.md Phase 1–5** = boot protocol (session open)
- **AO_OPS_001 (this file)** = close protocol (session close)
- **10-2 Radio Check** = status query, any time (not session-boundary only)
- **operations_log schema v1** = format for everything written during close

These compose. A session begins with START_HERE, may include multiple 10-2s
mid-run, and ends with AO_OPS_001. Memory persists across all three.
