---
node_id: AO_INFRA_000
title: "AUPEI Operations — RUNNING State (single source of truth)"
version: v1.1
date_minted: 2026-04-18
date_last_update: 2026-05-11
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

**Orientation waiver — 2026-05-03:** R@ accepted the 2026-04-18 running-state
snapshot as sufficient for orientation and non-mutating planning through
**2026-05-10**. This is not a fresh infrastructure verification and does not
authorize cabling, routing, firewall, addressing, service, or commissioning
changes without live checks.

**Update — 2026-05-11:** Fresh service-layer commissioning verified live
this session (Tailscale on NAS, cloud-seat reachability, UGOS sshd). Edge
and LAN-core physical layer NOT re-verified — that snapshot is still
2026-04-18 (now 23 days old, >7d staleness threshold; flag if relied upon
for cabling/routing/addressing changes).

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

## Current Running State (as of 2026-05-11, post tailnet-NAS commissioning)

### Physical / edge / LAN core / hosts

Unchanged from the 2026-04-18 snapshot (now in Historical State Snapshots
below). Edge router, LAN core, and host IPs are NOT re-verified this session —
service-layer changes only. If you need fresh edge/LAN truth, run live checks
before relying on those tables.

### NEW — Tailnet overlay (Tailscale AUPEI tailnet)

| Node | Tailnet IP | MagicDNS | Mode | Status |
|---|---|---|---|---|
| `aupei-nas` | 100.85.5.109 | aupei-nas.taile22fd1.ts.net | Docker container on UGREEN NAS (image tailscale/tailscale:latest, privileged + host network, state volume /volume1/docker/tailscale-state, auto-restart on) | Online (2026-05-11) |
| `cloud-seat-cowork` | 100.114.119.105 | n/a | Ephemeral, userspace-networking, sandbox-side per cowork session | Online during sessions; auto-cleaned when sandbox dies (key is reusable, not ephemeral-mode in admin) |
| `ivy-idioth-vector-prime` | 100.93.3.65 | (R@'s MBP, native Tailscale) | macOS native | R@'s primary |
| `aupei-mini`, `ipad-mini-6th-gen-wificellular`, `pixel-9-pro` | (various 100.x) | n/a | OFFLINE > 22 days | Cold, not in use |
| (DERP relay used) | derp-2 (sfo) | — | — | Healthy; NAS↔sandbox actually direct-pathed via STUN via 10.10.10.102:42955, ~5ms |

### NEW — Service commissioning on NAS

| Service | Where | Listen | Notes |
|---|---|---|---|
| UGOS sshd | NAS host | 0.0.0.0:22 (LAN + tailnet via serve) | Enabled this session; pre-existed but was OFF by default |
| `tailscale serve` proxy | inside `tailscale-aupei-nas` container | tailnet:22 → tcp://localhost:22 | Required because Tailscale runs in userspace mode in UGOS Docker; without serve, host sshd is unreachable from tailnet. State volume mount means serve config SHOULD persist across container restart (untested — DEFER-001 in ops_infra_change_2026-05-11_001.json) |
| Tailscale auth key | (in 1Password and reference_cloud_seat_ssh_key.md memory) | n/a | Reusable, 90-day expiry ~2026-08-08; rotate by ~2026-08-01 |
| `aupei_ops` user (NAS) | uid 1000, gid 10 (`admin` group) | n/a | Home redirected from `/home/aupei_ops` (read-only base layer, unwritable) to `/volume1/homes/aupei_ops` via `/etc/passwd` patch; home now real with `.ssh/authorized_keys` 700/600 |
| Cloud-seat SSH key | private in cowork memory, public in `~aupei_ops/.ssh/authorized_keys` on NAS | n/a | ed25519, fingerprint `SHA256:m5RqO80+emkFUP3u7a3VrCsxUTUEn7R7aNSPKQk4jqU` |

### Verified working as of 2026-05-11

- Tailscale Docker container up on NAS, registered as `aupei-nas` at 100.85.5.109
- `tailscale ping` cloud-seat-cowork → aupei-nas: 5 ms direct-path, no DERP needed
- SSH from R@'s Mac to aupei_ops@100.85.5.109 (password auth): success
- SSH from cowork sandbox to aupei_ops@100.85.5.109 (key auth via `tailscale nc` ProxyCommand): success, lands at /volume1/homes/aupei_ops
- Cloud-seat session-onboarding ritual documented in `reference_cloud_seat_ssh_key.md` (cowork memory dir)
- ops_infra_change_2026-05-11_001.json filed in `AUPEI/operations_log_staging/`

### NOT yet verified this session (assume green from prior, but verify before relying)

- Open WebUI, Qdrant, Matrix/Synapse/Element on Mini, LiteLLM, seat KBs (last green 2026-04-04 to 2026-04-13)
- Edge/LAN physical layer (last verified 2026-04-18, now >3 weeks stale)
- The cleanup actions R@ took in Tailscale admin (offline ghost `aupei-nas (100.77.236.32)` deletion + `aupei-nas-1 → aupei-nas` rename) — verify MagicDNS resolves 100.85.5.109 next session

### Known DEFERRED items added this session

1. **DEFER-001:** Verify `tailscale serve --tcp=22` survives container cold restart (~70% it does via state volume; polish to declarative via TS_SERVE_CONFIG)
2. **DEFER-002:** Verify `/etc/passwd` survives NAS reboot (~30% UGOS regenerates from config DB; need rc.local/systemd hook if it does)
3. **DEFER-003:** Update git `nas` remote on AUPEI_Vault to SSH-via-tailnet form (replace filesystem-mount remote with `aupei_ops@100.85.5.109:/path/to/bare.git`)
4. **DEFER-004:** Tailscale auth key rotation (~2026-08-01, before 2026-08-08 expiry)
5. **DEFER-005:** Mirror this setup for `gf_ops` admin (Face's path in)
6. **DEFER-006:** Write AO_INFRA_RUNBOOK_003 — Cloud-seat session-onboarding ritual (formalize current notes)
7. **DEFER-007:** Confirm Tailscale admin cleanup done (ghost node deleted, rename applied, MagicDNS resolves)

### Known DEFERRED items still carried from 2026-04-18

(unchanged — see Historical State Snapshots below for full list)

1. Eero mesh in bridge mode — STILL ROUTER, WiFi double-NAT'd
2. QNAP QSW-M2106-4C 10GbE switch — purchased, NOT deployed
3. GS324TP VLAN trunking — NOT configured
4. 2× TP-Link TL-SG108PE — purchased, NOT installed
5. Per-VLAN firewall rules (10/20/30) — NOT built
6. Camera + NVR commissioning onto VLAN 20 — NOT done
7. Unbound DNS anomaly investigation
8. BGW management access code rotation
9. AO_INFRA_004 patches (Eero-in-closet misstatement etc.)

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

### 2026-04-18 — post Phase 1 network cutover

Justified by: `ops_infra_change_2026-04-18_001.json`. This was the
running state from 2026-04-18 until 2026-05-11, when tailnet/SSH service
commissioning was layered on top. Physical layer (edge/LAN/host IPs)
is still presumed unchanged at the 2026-05-11 update unless someone
runs fresh live checks.

#### Edge

| Device | Role | IP / Address | Notes |
|---|---|---|---|
| AT&T BGW320-500 | Transparent bridge (IP Passthrough) | mgmt 192.168.1.254 from WAN side | DHCPS-fixed mode, MAC pin 00:e0:67:2e:40:84 → Protectli WAN |
| Protectli FW6E (OPNsense 25.1) | **Edge router (single NAT)** | WAN igb0 99.105.38.252/22 (DHCP, 31d), GW 99.105.36.1, LAN igb1 10.10.10.1/24 | Lives in Amelia's server closet rack |

#### LAN core

| Device | Role | IP / Address | Notes |
|---|---|---|---|
| Netgear GS324TP | **Dumb switch** (VLANs NOT yet trunked) | n/a | All ports access VLAN 1 currently |
| Eero mesh (3 nodes + 1 extender) | **Still in router mode** (WiFi clients double-NAT'd) | Eero LAN behind Protectli LAN | Bridge-mode flip DEFERRED |

#### Hosts

| Host | IP | Network | Notes |
|---|---|---|---|
| Mac Mini M4 Pro (`aupei-mini`, user `aupeiops`) | ~10.10.10.119 (last known) | Wired via GS324TP, 1GbE | Boot-sovereign. OpenJarvis + Synapse + Element + Open WebUI active |
| UGREEN NAS | 10.10.10.102 | Wired via GS324TP, 1GbE | Qdrant 6333, NFS lanes |
| MacBook M4 Pro (R@) | DHCP from OPNsense | Main Deck via Eero | Primary workstation |
| Lorex NVR | DHCP | GS324TP | Pre-cutover commissioning |
| Cameras (12 PoE) | DHCP | GS324TP PoE ports | Pre-cutover commissioning |

#### Verified working as of 2026-04-18

- WAN public IP confirmed (99.105.38.252/22)
- ping 8.8.8.8 = 17–20 ms, 0% loss
- ping google.com = 63–70 ms, 0% loss (pre-existing DNS anomaly, not cutover-caused)
- Single NAT (BGW is bridge, Protectli is edge)
- Whole house has internet through Protectli path

#### NOT yet verified at 2026-04-18 close (assume green from prior, but verify before relying)

- Open WebUI (was green 2026-04-13)
- Qdrant 5 collections (was 2,874 points 2026-04-13)
- Matrix / Synapse / Element on Mini (was running 2026-04-04)
- LiteLLM model routes (was 7 active 2026-04-04)
- All seat profiles + KBs (was deployed 2026-04-04)

#### Known DEFERRED items at 2026-04-18 close

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

## Audit hooks (future)

- A weekly cron on the Mini could snapshot `ifconfig`, `pfctl -ss`, `arp -a`,
  Open WebUI health, Qdrant collection sizes, and append a
  `## Verified state YYYY-MM-DD HH:MM` block to this file
- Drift between this file and a verified snapshot = signal to update
