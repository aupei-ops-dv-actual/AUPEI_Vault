---
node_id: AO_INFRA_004
title: "AUPEI Operations — Physical Network Topology"
version: v1.0
date_minted: 2026-03-17
author: "C@ the Red"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, network, physical, topology, power]
depends_on: [AO_INFRA_002, AO_INFRA_003]
---

# Physical Network Topology

## Design Mandate

The AUPEI network infrastructure must run 24/7 off-grid autonomously.
Power, compute, storage, security, and connectivity — all on Amelia's floor,
all solar-backed, all surviving a grid outage or flood indefinitely.

---

## CURRENT STATE — 2026-04-18 (Phase 1 cutover complete)

Read this before assuming any "Pre-cutover / Post-cutover" marker below
reflects what is actually plugged in right now. The "Logical Overlay on
Physical" section is the TARGET state, not all of it has been built yet.

**DONE (Phase 1, this session):**
- Protectli FW6E physically relocated from desk → Amelia's server closet rack
- Cabling: BGW320 LAN → Protectli igb0 (WAN); Protectli igb1 (LAN) → GS324TP
- BGW320 IP Passthrough fixed (MAC was pinned to wrong device); WAN now lands
  on public AT&T IP. Single NAT. BGW is a transparent bridge.
- Whole house online via Protectli (cameras, NVR, Mini, NAS, MacBook, Eeros)

**STILL PENDING (deferred to later sessions):**
- Eero mesh is STILL in router mode → WiFi clients are double-NATted
  (Protectli → Eero NAT). Bridge-mode flip not yet performed.
- QNAP QSW-M2106-4C purchased, NOT deployed. Mini + NAS still on 1GbE.
- GS324TP acts as a dumb switch; VLAN trunking not yet configured.
- 2× TP-Link TL-SG108PE purchased, NOT installed. Old switches still in
  Main Deck and Pancho's.
- Per-VLAN firewall rules (10/20/30) not yet built.
- Camera/NVR re-commissioning onto VLAN 20 not yet done.

**Reference incident: ops_infra_change_2026-04-18_001.json**

---

## Power Infrastructure (Solved)

```
Solar Arrays → 3× EcoFlow Delta Pro 3 (+ 3 extra batteries)
                    │ ≈24 kWh total capacity
                    │
                    └──→ EcoFlow Smart Panel 2 (Amelia's floor)
                         Independent sub-panel
                         ├── Protectli FW6E       (~15W)
                         ├── Mac Mini M4 Pro      (~40W)
                         ├── UGREEN NAS           (~40W peak)
                         ├── QNAP desk switch     (~15W)
                         ├── GS324TP + PoE cams   (~130W peak)
                         ├── Lorex NVR            (~30W)
                         ├── BGW320 gateway       (~15W)
                         └── Eero node            (~10W)
                         ─────────────────────────
                         Total: ≈295W peak
                         Runtime on 24kWh: ≈81 hours (no sun)
                         With Sacramento solar: indefinite

Backup: Generator + Grid power (for cloudy days, heavy loads)
```

---

## Physical Layout — Floor by Floor

### Amelia's Floor (2nd Floor / Attic) — THE NERVE CENTER

Everything critical lives here. Own power. Own fiber. All cameras home here.

```
┌─────────────────────────────────────────────────────────────────┐
│                    AMELIA'S FLOOR                                │
│                                                                  │
│  ┌──── SERVER CLOSET ────────────┐    cat6 ceiling    ┌─── WORKSTATION ───┐
│  │                                │    ═══════════>    │                    │
│  │  ATT Fiber (BGW320-500)       │                     │  Mac Mini M4 Pro  │
│  │  Fidium Fiber (unused-future) │    (can run 2nd     │  UGREEN NAS       │
│  │  Protectli FW6E               │     cat6 if needed) │  QNAP QSW-M2106  │
│  │  Netgear GS324TP (24p PoE)   │                     │   └─10GbE to Mini │
│  │  Lorex NVR                    │                     │   └─10GbE to NAS  │
│  │  weBoost cell booster         │                     │                    │
│  │  5× coax (antenna TV)        │                     └────────────────────┘
│  │  (no Eero upstairs)           │
│  │                                │
│  │  ← 12 camera PoE runs home   │
│  │     here to GS324TP          │
│  │     (room for 24 total)      │
│  │                                │
│  └──┬──────────┬─────────────────┘
│     │          │
│     │ cat6     │ cat6 + unused fiber trunk
│     │          │
└─────┼──────────┼────────────────────────────────────────────────┘
      │          │
      ↓          ↓
┌─────────────────────────────────────────────────────────────────┐
│                    MAIN DECK (Ground Floor)                      │
│                                                                  │
│  R@'s M4 Pro MacBook (primary workstation)                      │
│  TP-Link TL-SG108PE #1 (managed PoE)                           │
│  Eero #1 (hardwired from Amelia's — Main)                       │
│  Eero #2 (cat6 wired from Amelia's)                             │
│  Eero #3 (WiFi extender — backyard, wall outlet)                │
│  Printer                                                         │
│                                                                  │
│     │ cat6 (from Poncho's)                                       │
│     │                                                            │
└─────┼────────────────────────────────────────────────────────────┘
      │
      ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PONCHO'S FLOOR (Basement)                     │
│                                                                  │
│  TP-Link TL-SG108PE #2 (managed PoE)                           │
│  Eero (wired from Amelia's)                                      │
│  PS5                                                             │
│  Music player                                                    │
│  LG Google TV                                                    │
│  AV rack (media center)                                          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Existing Cable Infrastructure

| Run | From | To | Type | Status |
|-----|------|----|------|--------|
| 1 | Amelia's server closet | Amelia's workstation | Cat6 (ceiling) | Active — trunk for QNAP |
| 2 | Amelia's server closet | Main Deck | Cat6 | Active — feeds Eero #1 |
| 3 | Amelia's server closet | Main Deck | Cat6 | Active — feeds Eero #2 |
| 4 | Amelia's server closet | Poncho's | Cat6 | Active — feeds Poncho's Eero |
| 5 | Amelia's server closet | Lower floors | Fiber trunk | Unused — future |
| 6 | Poncho's | Main Deck | Cat6 | Available |
| 7 | Amelia's server closet | Amelia's workstation | Cat6 (potential) | Can be run if needed |

---

## Logical Overlay on Physical

### At Cutover:

**Amelia's Server Closet:**
- BGW320 (IP Passthrough) → Protectli WAN port (igb0)
- Protectli LAN port (igb1) → GS324TP (trunk: VLANs 10, 20, 30)
- GS324TP Port assignments:
  - Port 1: Trunk from Protectli (all VLANs)
  - Port 2: Trunk to QNAP workstation (cat6 ceiling run, all VLANs)
  - Port 3: Trunk to Main Deck (cat6, TP-Link #1)
  - Port 4: Trunk to Poncho's (cat6, TP-Link #2)
  - Ports 5-16: VLAN 20 access (cameras, PoE)
  - Port 17: VLAN 20 access (Lorex NVR)
  - Port 18: VLAN 20 access (Eero — or VLAN 30 for guest)
  - Ports 19-24: Reserved/future

**Amelia's Workstation (across attic via cat6 trunk):**
- QNAP QSW-M2106-4C receives trunk from GS324TP
  - 10GbE Port: Mac Mini (VLAN 10 access)
  - 10GbE Port: NAS (VLAN 10 access)
  - 2.5GbE Ports: Future cameras, PoE devices (VLAN 20)

**Main Deck — SWITCH_Main_Deck (10.10.10.201):**
- TP-Link TL-SG108PE #1, configured 2026-03-18
  - Port 1 (PoE): Tagged trunk (VLANs 10, 20, 30) — PVID 1 — spare/future uplink
  - Port 2 (PoE): VLAN 1 untagged — PVID 1 — spare (future PoE camera)
  - Port 3 (PoE): VLAN 20 untagged — PVID 20 — Sony Bravia
  - Port 4 (PoE): VLAN 20 untagged — PVID 20 — PS5
  - Port 5: VLAN 10 untagged — PVID 10 — Eero mesh node
  - Port 6: Tagged trunk (VLANs 10, 20, 30) — PVID 1 — cat6 downlink to Poncho's
  - Port 7: VLAN 10 untagged — PVID 10 — desk switch → M4/printer
  - Port 8: Tagged trunk (VLANs 10, 20, 30) + VLAN 1 untagged — PVID 1 — uplink to Protectli/GS324TP

**Poncho's Floor — SWITCH_Ponchos (10.10.10.202):**
- TP-Link TL-SG108PE #2, configured 2026-03-18
  - Port 1 (PoE): VLAN 1 untagged — PVID 1 — spare (future PoE camera)
  - Port 2 (PoE): VLAN 1 untagged — PVID 1 — spare (future PoE camera)
  - Port 3 (PoE): VLAN 1 untagged — PVID 1 — spare (future PoE camera)
  - Port 4 (PoE): VLAN 1 untagged — PVID 1 — spare (future PoE camera)
  - Port 5: VLAN 20 untagged — PVID 20 — Sony Bravia
  - Port 6: VLAN 20 untagged — PVID 20 — PS5
  - Port 7: VLAN 10 untagged — PVID 10 — Eero mesh node
  - Port 8: Tagged trunk (VLANs 10, 20, 30) + VLAN 1 untagged — PVID 1 — uplink to Main Deck

---

## Future Expansion Notes

- **Fidium fiber:** Second ISP into Amelia's. OPNsense supports multi-WAN
  failover natively. ATT + Fidium = redundant internet. Plug Fidium into
  Protectli igb2, configure as WAN2 with failover gateway group. Zero
  additional hardware needed.
- **Starlink:** Currently on the motorhome. Future bolt-on to Protectli
  igb3 as WAN3. Triple-redundant internet.
- **Camera expansion:** GS324TP has room for 12 more cameras (24 total).
  QNAP desk switch adds PoE for cameras on the workstation side of attic.
- **Second cat6 to workstation:** Run it if we want redundancy or a
  dedicated management VLAN trunk separate from data. Not blocking now.
- **MUSH server / DMZ:** Protectli has igb2-igb5 unused. VLAN 40 (DMZ)
  can be added for public-facing services when ready.
