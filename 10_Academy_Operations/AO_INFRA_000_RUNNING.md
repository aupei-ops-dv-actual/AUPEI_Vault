---
node_id: AO_INFRA_000
title: "AUPEI Operations — RUNNING State (single source of truth)"
version: v1.0
date_minted: 2026-04-18
author: "C@ the Red"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, running, current_state, anchor, read_first]
depends_on: []
---

# AO_INFRA_000 — What Is Actually Plugged In And Running RIGHT NOW

## Why this doc exists

The other AO_INFRA_* docs describe **target architecture**, **physical capacity**,
and **historical decisions**. They do NOT track what is actually powered on,
cabled up, and serving traffic in the moment.

That gap has burned us twice (incident_2026-04-13_001, incident_2026-04-18_001).
A doc said one thing, the rack said another, and we acted on the doc.

**This file is the rack, not the doc.** It is append-only, timestamped, and
short. Any future instance MUST read this file before touching infrastructure.
If this file is more than 7 days old, treat it as suspect and verify before
acting on it.

---

## Read order before touching any infrastructure

1. **AO_INFRA_000 (this file)** — what is running RIGHT NOW
2. **AO_INFRA_002** — target network architecture (where we are headed)
3. **AO_INFRA_004** — physical topology (where things live, what's cabled)
4. **AO_INFRA_005** — hardware manifest (what we own)
5. **AO_INFRA_006** — secrets register (where credentials live, NOT the
   credentials themselves)
6. **Most recent ops_infra_change_*.json** in `AUPEI/operations_log_staging/` —
   the last change actually executed

If those five disagree, AO_INFRA_000 is authoritative for *current state* and
the most recent ops_log entry is authoritative for *what changed*. The
target/physical/manifest docs are aspirational until they match this file.

---

## Current Running State (as of 2026-04-18, post Phase 1 cutover)

### Edge

| Device | Role | IP / Address | Notes |
|---|---|---|---|
| AT&T BGW320-500 | Transparent bridge (IP Passthrough) | mgmt 192.168.1.254 from WAN side | DHCPS-fixed mode, MAC pin 00:e0:67:2e:40:84 → Protectli WAN |
| Protectli FW6E (OPNsense 25.1) | **Edge router (single NAT)** | WAN igb0 99.105.38.252/22 (DHCP, 31d), GW 99.105.36.1, LAN igb1 10.10.10.1/24 | Lives in Amelia's server closet rack |

### LAN core

| Device | Role | IP / Address | Notes |
|---|---|---|---|
| Netgear GS324TP | **Dumb switch** (VLANs NOT yet trunked) | n/a | All ports access VLAN 1 currently |
| Eero mesh (3 nodes + 1 extender) | **Still in router mode** (WiFi clients double-NAT'd) | Eero LAN behind Protectli LAN | Bridge-mode flip DEFERRED |

### Hosts

| Host | IP | Network | Notes |
|---|---|---|---|
| Mac Mini M4 Pro (`aupei-mini`, user `aupeiops`) | ~10.10.10.119 (last known) | Wired via GS324TP, 1GbE | Boot-sovereign. OpenJarvis + Synapse + Element + Open WebUI active |
| UGREEN NAS | 10.10.10.102 | Wired via GS324TP, 1GbE | Qdrant 6333, NFS lanes |
| MacBook M4 Pro (R@) | DHCP from OPNsense | Main Deck via Eero | Primary workstation |
| Lorex NVR | DHCP | GS324TP | Pre-cutover commissioning |
| Cameras (12 PoE) | DHCP | GS324TP PoE ports | Pre-cutover commissioning |

### Verified working as of 2026-04-18

- WAN public IP confirmed (99.105.38.252/22)
- ping 8.8.8.8 = 17–20 ms, 0% loss
- ping google.com = 63–70 ms, 0% loss (pre-existing DNS anomaly, not cutover-caused)
- Single NAT (BGW is bridge, Protectli is edge)
- Whole house has internet through Protectli path

### NOT yet verified this session (assume green from prior, but verify before relying)

- Open WebUI (was green 2026-04-13)
- Qdrant 5 collections (was 2,874 points 2026-04-13)
- Matrix / Synapse / Element on Mini (was running 2026-04-04)
- LiteLLM model routes (was 7 active 2026-04-04)
- All seat profiles + KBs (was deployed 2026-04-04)

### Known DEFERRED items (do NOT assume these are done)

1. Eero mesh in bridge mode — STILL ROUTER, WiFi double-NAT'd
2. QNAP QSW-M2106-4C 10GbE switch — purchased, NOT deployed (Mini + NAS still 1GbE)
3. GS324TP VLAN trunking — NOT configured (acts as dumb switch)
4. 2× TP-Link TL-SG108PE — purchased, NOT installed (Main Deck + Pancho's still on old switches)
5. Per-VLAN firewall rules (10/20/30) — NOT built
6. Camera + NVR commissioning onto VLAN 20 — NOT done
7. Unbound DNS anomaly investigation — google.com resolves to 64.233.185.113 (non-local edge)
8. BGW management access code rotation — known to current session
9. AO_INFRA_004 was patched 2026-04-18; if other docs still reference an Eero in the server closet, they are wrong

---

## How to update this file

**APPEND-ONLY entries below the divider, newest first.** Do NOT rewrite the
"Current Running State" tables in-place — instead, when the topology meaningfully
changes:

1. Append a new "## Current Running State (as of YYYY-MM-DD, <event>)"
   section ABOVE the previous one
2. Move the previous "Current Running State" section under
   "## Historical State Snapshots" below
3. Cite the ops_infra_change_*.json entry that justifies the change
4. Update the date stamp in this file's frontmatter

**Trigger to update this file:** any infra change touching cabling, power,
routing, addressing, or device commissioning. If you're writing an
ops_infra_change_*.json entry, you also update this file. They ship together.

---

## Historical State Snapshots

(none yet — first version)

---

## Audit hooks (future)

- A weekly cron on the Mini could snapshot `ifconfig`, `pfctl -ss`, `arp -a`,
  Open WebUI health, Qdrant collection sizes, and append a
  `## Verified state YYYY-MM-DD HH:MM` block to this file
- Drift between this file and a verified snapshot = signal to update
