---
node_id: AO_INFRA_000
title: "AUPEI Operations — RUNNING State (single source of truth)"
version: v1.1
date_minted: 2026-04-18
date_last_update: 2026-05-28
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

**Update — 2026-05-21:** No infra touches this session per R@ direction
(rehydration-pipeline solo-test run; build stability layer before any
next infra moves). Edge/LAN-core physical-layer snapshot carried forward
unchanged from 2026-04-18 (now 33 days old). Service-layer snapshot from
2026-05-11 carried forward unchanged (now 10 days old, exceeds 7d
threshold — staleness flag remains for any cabling/routing/firewall/
addressing/commissioning move). Orientation-only waiver re-issued for
non-mutating planning; live-verify required before any mutating action.
Filed: 2026-05-21 onboard heartbeat (no fresh physical observations
this session).

**Update — 2026-05-28 (INCIDENT-DRIVEN PARTIAL RE-VERIFICATION):**
Live OPNsense web GUI walk performed during `ops_incident_2026-05-28_001`
investigation (Lorex NVR diagnostic artifact `Palatirlook/LNR608/`
found on R@ MacBook Desktop; Code Red declared). Findings invalidate
multiple statements in the 2026-04-18 snapshot:

1. **OPNsense interface configuration:** Five interfaces are configured
   and visible in OPNsense (not the single LAN previously implied):
   - LAN     10.10.10.0/24    (unchanged)
   - OPS     10.10.10.2/24    on `vlan01`, **OVERLAPS LAN subnet — misconfig flag**
   - IOT     10.20.20.0/24    on `vlan02`, UP, but ZERO devices
   - GUEST   10.30.30.0/24    on `vlan03`, UP, no devices
   - STAGING 192.168.0.50/24  on `igb2`, NO CARRIER

   This **partially contradicts** the 2026-04-18 deferred items 5/6
   ("Per-VLAN firewall rules — NOT built", "Camera + NVR commissioning
   onto VLAN 20 — NOT done"). The VLAN interfaces *do* exist on the
   firewall side. The DEFERRED items are now refined: the OPNsense-side
   VLAN config exists; the GS324TP-side trunking + camera/NVR migration
   to the VLAN still doesn't.

2. **Active LAN hosts (live ISC DHCP, verified 2026-05-28 ~18:00):**

   | IP | MAC | Vendor | Identity |
   |---|---|---|---|
   | 10.10.10.1 | 0:e0:67:2e:40:85 | Protectli | OPNsense edge router |
   | 10.10.10.102 | 6c:1f:f7:a9:87:cb | Ugreen | AUPEI-NAS |
   | 10.10.10.117 | b4:22:00:42:cf:21 | Brother | BRNB4220042CF21 (printer) |
   | 10.10.10.118, .120, .129 | f8:bb:bf:* | eero | mesh nodes |
   | 10.10.10.121 | 04:5d:4b:e6:0f:df | Sony | Bravia "Redrum_Vision" (Red Room) |
   | 10.10.10.123 | (random) | Apple | R@ MacBook (this Mac) |
   | 10.10.10.124 | 46:e7:2c:* | Apple | iPad |
   | 10.10.10.127 | d0:11:e5:22:b4:b7 | Apple | **aupei-mini** (Mac Mini) |
   | 10.10.10.132 | 0:a0:de:b3:ae:62 | Yamaha | A/V receiver |
   | 10.10.10.140 | (random) | Apple | iPhone (Continuity confirmed via rapportd) |

3. **Mac Mini correction:** AO_INFRA_000 2026-04-18 snapshot lists
   `aupei-mini` at ~10.10.10.119. Actual DHCP lease as of 2026-05-28:
   **10.10.10.127**, hostname `AUPEI-Mini`. Doc was stale.

4. **RESOLVED via R@ physical-topology trace (2026-05-28 ~18:40):**
   R@ confirmed actual cabling:

   ```
   Fiber → Media Center → CAT6 → AT&T BGW320 ──┬── Protectli WAN
                                               ├── Lorex NVR
                                               └── EcoFlow Smart Panel 2
   Protectli LAN → GS324TP → 11 PoE cameras + 1 other IoT device
   ```

   **The Lorex NVR and EcoFlow Smart Panel 2 are UPSTREAM of Protectli**
   — they sit on the BGW's network, peer with Protectli's WAN, NOT
   behind OPNsense at all. This is why OPNsense has zero record of them.
   This is by design of the topology, not an anomaly.

   **Implications that invalidate prior assumptions:**

   - The 2026-04-18 snapshot listed Lorex NVR on GS324TP. That was
     **wrong** for the NVR specifically — only the cameras are on
     GS324TP. The NVR is on the BGW side.
   - The DEFERRED VLAN 20 plan (per-VLAN firewall rules, camera+NVR
     onto VLAN 20) was, for the NVR, **architecturally never going to
     work** — VLAN 20 lives inside Protectli; the NVR is upstream of
     Protectli. VLAN 20 isolation applies only to the cameras, not
     the NVR.
   - **Protectli's firewall does NOT protect the NVR or the EcoFlow
     Smart Panel 2.** Both are exposed to whatever the BGW exposes —
     UPnP, port-forward, ISP-side reach.
   - R@ MacBook on 10.10.10.0/24 (behind Protectli) **has no L3 route
     to the BGW's 192.168.1.x network** where the NVR and EcoFlow live
     (verified via OPNsense routing table: zero RFC1918 routes other
     than STAGING). So NVR→Mac lateral movement via normal routing
     is not possible.

   **Updated threat-model verdict on the original `Palatirlook` artifact:**
   live lateral L2/L3 movement from NVR to Mac is ruled out by topology.
   The artifact's presence on the Mac is most consistent with one of:
   (a) past direct connection (Mac plugged into BGW network at some
   point — pre-Protectli, or media-center workstation use), (b) Time
   Machine / Migration Assistant restore from an older system that had
   the export, (c) a Lorex client app on the Mac (Lorex Cirrus, Lorex
   Home) that ran a scheduled / one-time pull, (d) USB / iCloud
   ferrying. **NOT live breach via current network paths.**

5. **NEW CONCERN surfaced by topology — internet-exposure of NVR +
   EcoFlow:**
   - Both sit on BGW network with whatever firewall BGW provides
     (minimal). If BGW has UPnP enabled or has port-forward rules,
     either device could be internet-reachable.
   - Lorex NVRs have historical CVE classes: web admin auth bypass,
     RTSP credential weaknesses, web RCE.
   - EcoFlow Smart Panel 2 has cloud connectivity and has had documented
     firmware vulnerabilities.

6. **NET_SECURITY zone commissioning — NVR cutover EXECUTED
   2026-05-28 ~19:00 PT (per ops_infra_change_2026-05-28_001):**

   R@ physically recabled the Lorex NVR from BGW LAN to Protectli
   igb2 (OPT1 physical port). OPNsense changes executed by Walker_02-
   resume via Chrome MCP under R@'s explicit authorization:

   - **Interface rename:** `opt4` description changed from `STAGING` to
     `NET_SECURITY`. New zone identity for the IoT-security segment.
   - **ISC DHCPv4 enabled on NET_SECURITY** (192.168.0.0/24): range
     192.168.0.100–200. NVR picked first address `192.168.0.100`
     immediately on reboot.
   - **Firewall rules on NET_SECURITY** (in order, first-match):
     1. `BLOCK` IPv4 NET_SECURITY net → `10.0.0.0/8` — segmentation
        guard blocks lateral to LAN / IOT / GUEST / OPS.
     2. `PASS` IPv4 any → any — internet + within-NET_SECURITY (carried
        forward from R@'s prior `Allow STAGING access` rule, now its
        purpose is "internet egress for NET_SECURITY").
   - **Verification observed:** NVR DHCP-leased `192.168.0.100`,
     vendor `Lorex Technology Inc.`, hostname `N862A6`, state active.
     R@ confirmed NVR web UI loads from Mac on LAN — LAN→NET_SECURITY
     admin path works (allowed by LAN default rule).

   **What this gets us:**
   - NVR is no longer on the BGW exposed zone.
   - NVR has its own firewall now (default-deny inbound from internet,
     block lateral to home LAN, allow internet egress for cloud).
   - LAN devices (R@ Mac, Mini, NAS) can initiate to the NVR for admin;
     NVR cannot initiate to them. Segmentation is real.

7. **STILL DEFERRED post-cutover (rolled forward):**
   - EcoFlow Smart Panel 2 still on BGW LAN — same cutover recipe to
     follow on next infra session.
   - 11 PoE cameras still on Netgear GS324TP (LAN side, 10.10.10.x).
     They were configured to push streams to NVR's OLD 192.168.1.x —
     they cannot auto-rediscover the NVR at its new 192.168.0.100.
     **Camera migration to NET_SECURITY is the next planned move**
     (option lattice: GS324TP VLAN-trunk vs new PoE switch on igb2
     vs OPNsense bridge interface). Decision + execution pending.
   - BGW UPnP / port-forward audit still owed (EcoFlow remains
     exposed there).
   - AO_INFRA_004 (Physical Topology) needs a redraw — old diagram
     placed NVR on GS324TP, actual cabling was BGW LAN, now Protectli
     igb2.
   - AO_INFRA_006 (Secrets Register): NVR IP entry needs update to
     192.168.0.100; Mullvad VPN entry needs to be added.

8. **Documented-but-undocumented software discovered on R@ MacBook:**
   - Mullvad VPN daemon installed 2026-03-25 (`/Library/LaunchDaemons/
     net.mullvad.daemon.plist`). R@ confirmed legitimate install.
     **Update owed to AO_INFRA_006:** add Mullvad to VPN inventory
     alongside ExpressVPN.

9. **R@ MacBook attack surface (LAN-facing):** SSH (22), VNC/Screen
   Sharing (5900), Apple Remote Desktop (3283), SMB (445) all listening
   on en0. Unified log retention only ~1.5 days; March 16 attribution
   window unrecoverable from local logs alone. Time Machine destination
   is SMB to AUPEI-NAS — backups themselves reachable from any LAN-
   resident compromise.

10. **No malicious persistence found in user-readable launchd locations.
    No obvious C2 in active outbound connections snapshot.**

5. **Documented-but-undocumented software discovered on R@ MacBook:**
   - Mullvad VPN daemon installed 2026-03-25 (`/Library/LaunchDaemons/
     net.mullvad.daemon.plist`). R@ confirmed legitimate install.
     **Update owed to AO_INFRA_006:** add Mullvad to VPN inventory
     alongside ExpressVPN.

6. **R@ MacBook attack surface (LAN-facing):** SSH (22), VNC/Screen
   Sharing (5900), Apple Remote Desktop (3283), SMB (445) all listening
   on en0. Unified log retention only ~1.5 days; March 16 attribution
   window unrecoverable from local logs alone. Time Machine destination
   is SMB to AUPEI-NAS — backups themselves reachable from any LAN-
   resident compromise.

(items 7–10 superseded by renumbered items below — see updated list)

Filed: ops_incident_2026-05-28_001 (active investigation, P0). Edge
router / WAN / Tailscale-NAS service layer NOT re-verified this session
(carried forward from 2026-05-11). Snapshot remains partial; this
update covers interface configuration + LAN device inventory + Mac host
attack surface only.

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
