---
node_id: AO_INFRA_005
title: "AUPEI Operations — Hardware Manifest"
version: v1.0
date_minted: 2026-03-25
author: "C@ the Red"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, hardware, manifest, inventory]
depends_on: [AO_INFRA_003, AO_INFRA_004]
---

# Hardware Manifest — AUPEI Academy Infrastructure

**Last updated:** 2026-03-25
**Owner entity:** DooVinci Agency (S-Corp) — all hardware is DooVinci property
**Canonical copy:** Vault A (this file). Vault B has operational copy. Vault C has bridge reference.

---

## Compute

### Mac Mini (Server) — "the Mini"

| Field | Value |
|-------|-------|
| **Role** | Primary server. OpenJarvis host. Always-on infrastructure. |
| **Chip** | Apple M4 Pro |
| **CPU** | 14-core (10 performance + 4 efficiency) |
| **GPU** | 20-core Apple GPU (Metal acceleration) |
| **Neural Engine** | 16-core |
| **Unified Memory** | 64 GB |
| **Internal Storage** | 2 TB SSD |
| **Ethernet** | 10 Gigabit Ethernet (built-in) |
| **Ports (Front)** | 2× USB-C, 3.5mm headphone jack |
| **Ports (Back)** | 3× Thunderbolt 5, HDMI, 10GbE RJ45, power |
| **Network Connection** | **Pre-cutover:** 1GbE → Netgear GS105E. **Post-cutover:** 10GbE → QNAP QSW-M2106-4C |
| **VLAN** | 10 (OPS_TRUSTED), 10.10.10.x |
| **Hostname** | aupei-mini |
| **Location** | Amelia's Floor, workstation area |
| **Power** | EcoFlow Smart Panel 2 (solar-backed) |
| **Software Bundle** | Pro Apps Bundle for Education (not preinstalled) |
| **macOS Services** | Ollama, OpenJarvis (planned), launchd, Time Machine to NAS |

**NOTE:** This is a DIFFERENT machine from R@'s M4 Pro MacBook Pro (laptop). Both have M4 Pro chips. "The Mini" = server. "The M4" = MacBook.

---

### M4 Pro MacBook Pro (Laptop) — "the M4" / "the powerbook"

| Field | Value |
|-------|-------|
| **Role** | R@'s primary workstation. Portable. NOT the server. |
| **Chip** | Apple M4 Pro |
| **Location** | Mobile (Main Deck when home) |
| **Network** | VLAN 10 (wired via USB-C adapter or WiFi) |
| **Relation to Mini** | Separate machine. Does NOT host OpenJarvis. |

---

## Storage

### UGREEN DXP4800 Pro NAS — "AUPEI-NAS"

| Field | Value |
|-------|-------|
| **Role** | Network-attached storage. Vaults, archives, backups, media, fast tier. |
| **Hostname** | AUPEI-NAS (restored after RAM upgrade reset) |
| **IP** | 10.10.10.102 (DHCP reservation from Protectli) |
| **Network Connection** | **Pre-cutover:** 1GbE → Netgear GS105E. **Post-cutover:** 10GbE → QNAP QSW-M2106-4C (same switch as Mini) |
| **OS** | UGOS |
| **RAM** | 64 GB DDR5 (2× 32GB Crucial DDR5 5600MT/s) |
| **Management** | https://10.10.10.102:9443 |

#### Storage Pool 1 — Bulk Storage

| Field | Value |
|-------|-------|
| **RAID** | RAID 5 |
| **Drives** | 4× Seagate IronWolf Pro 8TB |
| **Filesystem** | btrfs |
| **Usable Capacity** | 21.7 TB |
| **Shares** | CANON, AUPEI_Archive, DooVinci_Archive, GF_Archive, Backups, Media_AUPEI, Media_Personal |
| **Use** | Vaults, git mirrors, Time Machine backups, archives, media |

#### Storage Pool 2 — Academy Fast Tier

| Field | Value |
|-------|-------|
| **RAID** | RAID 1 (mirror) |
| **Drives** | 2× Samsung 990 Pro 4TB NVMe |
| **Filesystem** | btrfs |
| **Usable Capacity** | 3.6 TB |
| **Volume Name** | Academy Fast — OpenJarvis, QEPE, Agent Runtime |
| **Planned Lanes** | `/jarvis/index`, `/jarvis/sqlite`, `/jarvis/traces`, `/qepe/session_traces`, `/qepe/qshape_state`, `/qepe/replay`, `/ops/agent_logs` |
| **Use** | OpenJarvis runtime data, QEPE session traces, Q-shape state, operator logs |

---

## Network

> **DEPLOYMENT NOTE (2026-03-25):** The network below describes both PRE-CUTOVER (current) and POST-CUTOVER (planned) states. Pre-cutover, the Eeros sit between ATT and the Protectli WAN, and all devices connect through the GS105E at 1GbE. The GS324TP, QNAP 10GbE switch, and floor switches are purchased but NOT yet deployed. Unbound DNS is NOT configured — Mini uses 1.1.1.1 / 8.8.8.8 temporarily.

### Netgear GS105E — Current Desk Switch (PRE-CUTOVER)

| Field | Value |
|-------|-------|
| **Role** | Temporary desk switch. All OPS devices at 1GbE. |
| **Ports** | 5× Gigabit |
| **Location** | Amelia's Floor, workstation area |
| **Uplink** | Protectli LAN (igb1) |
| **Downlinks** | Mac Mini, NAS, M4 Pro MacBook Pro |
| **Status** | **ACTIVE** — will be replaced by QNAP + GS324TP at cutover |

### Protectli FW6E — Firewall/Router

| Field | Value |
|-------|-------|
| **Role** | Firewall, VLAN router, DHCP, DNS, IDS |
| **OS** | OPNsense 25.1 |
| **CPU** | Intel i7 (6-port model, recertified) |
| **RAM** | 16 GB DDR4 |
| **Storage** | 128 GB Transcend MSA230 mSATA SSD |
| **Ports** | 6× Intel i225-V 2.5GbE (igb0–igb5) |
| **WAN** | igb0 → **Pre-cutover:** Eeros → ATT. **Post-cutover:** BGW320 (IP passthrough) |
| **LAN** | igb1 → **Pre-cutover:** GS105E. **Post-cutover:** GS324TP trunk |
| **VLANs** | 10 (OPS_TRUSTED: 10.10.10.0/24), 20 (IOT: 10.20.20.0/24), 30 (GUEST: 10.30.30.0/24) |
| **Services** | **Pre-cutover:** DHCP only, DNS not serving (Unbound unconfigured). **Post-cutover:** Unbound DNS (recursive), Suricata IDS (detect mode), DHCP per VLAN |
| **Location** | Amelia's Floor, server closet |
| **Power** | EcoFlow Smart Panel 2 |

### Netgear GS324TP — Rack Switch (POST-CUTOVER)

| Field | Value |
|-------|-------|
| **Role** | Core distribution switch. Trunk to all floors. |
| **Ports** | 24× PoE+ Gigabit |
| **Location** | Amelia's Floor, server closet |
| **Uplink** | Protectli igb1 (trunk: VLANs 10, 20, 30) |
| **Downlinks** | Trunk to QNAP desk switch (cat6 ceiling run), trunks to Main Deck and Poncho's floor, camera PoE ports |
| **Status** | **PURCHASED, NOT DEPLOYED** |

### QNAP QSW-M2106-4C — Desk Switch (POST-CUTOVER)

| Field | Value |
|-------|-------|
| **Role** | 10GbE aggregation for Mini + NAS |
| **Ports** | 4× 10GbE combo (SFP+/RJ45), 6× 2.5GbE |
| **Location** | Amelia's Floor, workstation area |
| **Uplink** | Trunk from GS324TP (cat6 across attic ceiling) |
| **10GbE Port 1** | Mac Mini |
| **10GbE Port 2** | NAS |
| **Note** | Mini↔NAS traffic stays on this switch at 10Gig. Never touches GbE backbone. |
| **Status** | **PURCHASED, NOT DEPLOYED** |

### TP-Link TL-SG108PE ×2 — Floor Switches

| Field | Value |
|-------|-------|
| **#1 Location** | Main Deck (10.10.10.201) |
| **#2 Location** | Poncho's Floor (10.10.10.202) |
| **Ports** | 8× Gigabit (4× PoE) each |
| **Role** | VLAN access for floor devices |

### ATT BGW320-500 — Gateway

| Field | Value |
|-------|-------|
| **Role** | ISP gateway, IP passthrough to Protectli |
| **Service** | ATT Fiber 300 (actual ~400/330 Mbps) |
| **IP** | 192.168.1.254 (management only after passthrough) |
| **WiFi** | Disabled (Eero handles WiFi) |

### Eero Mesh — WiFi

| Field | Value |
|-------|-------|
| **Nodes** | 4 (Amelia's, Main ×2, Backyard) |
| **Mode** | Bridge (no NAT/DHCP — OPNsense handles) |
| **Role** | WiFi coverage only |

---

## Power

### EcoFlow Delta Pro 3 System

| Field | Value |
|-------|-------|
| **Units** | 3× Delta Pro 3 + 3× extra batteries |
| **Total Capacity** | ~24 kWh |
| **Distribution** | EcoFlow Smart Panel 2 (Amelia's Floor sub-panel) |
| **Critical Load** | Mini (~40W) + Protectli (~15W) + NAS (~40W) + QNAP switch (~15W) + Eero (~10W) ≈ 120W |
| **Full Load** | + GS324TP + PoE cams + NVR ≈ 295W peak |
| **Runtime (no sun)** | ~81 hours (full load), ~200 hours (critical only) |
| **With Solar** | Indefinite (Sacramento climate) |

### Fidium Fiber (Future)

| Field | Value |
|-------|-------|
| **Status** | Terminated in server closet, unused |
| **Role** | Future WAN2 failover via Protectli igb2 |

---

## Peripherals

| Device | Location | Notes |
|--------|----------|-------|
| UPERFECT 18.5" portable monitor | Amelia's workstation | USB-C to Mini for local access |
| Bluetooth keyboard + mouse | Amelia's workstation | Mini peripherals |
| Lorex NVR | Server closet | 12 cameras via GS324TP PoE |
| weBoost cell booster | Server closet | Cell coverage for Amelia's floor |

---

*This manifest is the canonical hardware record for the AUPEI Academy infrastructure. Update this file when hardware changes. Vault B (DooVinci) holds the operational copy. Vault C (GF) holds a bridge reference.*
