

=======================
=======================

Protectli FW6E ──→ GS324TP (rack, server room)
                        │ trunk (floor run across attic)
                        ↓
                   QNAP QSW-M2106-4C (desk, workstation area)
                        ├── Mac Mini (10GbE)
                        ├── NAS (10GbE)
                        └── future cameras / PoE devices

---
node_id: AO_INFRA_002
title: "AUPEI Operations — Network Architecture"
version: v1.0
date_minted: 2026-03-12
author: "C@ the Red"
entity: AUPEI
vault: A
layer: governance
epistemic_status: PROPOSED
tags: [infrastructure, network, security, architecture]
---

# AUPEI Operations — Network Architecture

## Current State (Known Issues)

- AT&T Fiber 300 (300/300 Mbps, actual ~400/330 to gateway)
- BGW320-500 gateway at 192.168.1.254
- Flat network — everything on one subnet, no segmentation
- Eero mesh (4 nodes, 3 stories) handling all WiFi
- POE switch for 11 cameras + EcoFlow SmartPanel 2
- ~20+ devices (TVs, consoles, Chromecasts, Yamaha, printer, Macs)
- **Network is considered compromised** — no IDS/IPS, no monitoring
- WiFi speed degraded (~21 Mbps down on device vs 400 at gateway)
- No remote access infrastructure for Prague operations

## Target State

Segmented, monitored network with:
- Proper firewall with IDS/IPS
- VLAN isolation (operations vs IoT vs guest)
- Secure remote access from anywhere (Tailscale)
- Mac Mini on solar/battery for grid resilience
- All council infrastructure on isolated operations VLAN

---

## Network Topology (Target)

```
                        AT&T Fiber
                            │
                    ┌───────┴────────┐
                    │  BGW320-500    │
                    │  (IP Passthru) │
                    │  192.168.1.254 │
                    └───────┬────────┘
                            │ WAN
                    ┌───────┴────────┐
                    │ Protectli Vault│
                    │  (OPNsense)   │
                    │  Firewall/IDS │
                    │  VLAN Router  │
                    │  DHCP Server  │
                    └──┬────┬────┬──┘
                       │    │    │
          ┌────────────┘    │    └────────────┐
          │                 │                  │
    VLAN 10: OPS      VLAN 20: IoT      VLAN 30: GUEST
    (Trusted)         (Untrusted)        (Isolated)
          │                 │                  │
    ┌─────┴──────┐    ┌────┴─────┐      ┌────┴─────┐
    │ Mac Mini   │    │ POE Sw   │      │ Eero     │
    │ (Upstairs) │    │ 11 Cams  │      │ Guest    │
    │ M4 Pro MBP │    │ EcoFlow  │      │ SSID     │
    │ Printer    │    │ SmartTVs │      └──────────┘
    │ Time Caps  │    │ Consoles │
    └────────────┘    │ Yamaha   │
                      │ Chrmcsts │
                      └──────────┘

    ──── Tailscale Overlay (encrypted mesh) ────
    │  Mac Mini  ↔  M4 Pro MBP  ↔  Prague MBP  │
    │  (works from anywhere, no port forwarding) │
    ─────────────────────────────────────────────
```

---

## Hardware Shopping List

### Protectli Vault (Firewall Appliance)

**Recommended: Protectli VP2420 (4-port, Intel Celeron N5105)**
- 4 Intel i225-V 2.5GbE ports
- 16GB RAM (needed for Suricata IDS with your traffic volume)
- 128GB or 256GB SSD (for logs)
- Fanless, low power (~15W)
- Runs OPNsense (recommended over pfSense for this use case)
- Approximate cost: $350-450 configured

**Why OPNsense over pfSense:** Better UI, more active development, Suricata IDS built in, no licensing drama. Same underlying FreeBSD.

**Why 16GB RAM:** You want to run Suricata (IDS/IPS) with full packet inspection on a 300Mbps connection plus 11 camera streams. 8GB would work but would be tight. 16GB gives headroom.

### Additional Hardware Needed

- **Managed switch** (VLAN-capable) — You may already have one. Needs to support 802.1Q VLAN tagging. If your current switches are unmanaged, pick up a TP-Link TL-SG108E (~$30) or Netgear GS308E for each floor that needs VLAN separation.
- **Cat6 run** (if not already in place) — Wired connection from Protectli Vault location to Mini upstairs. Critical for operations VLAN performance.
- **Short ethernet cables** — For rack/shelf organization at the gateway location

### Optional but Recommended

- **UPS for Protectli Vault** — Small UPS (APC BE425M or similar) to keep the firewall alive during brief outages. The Mini has solar/battery, but if the firewall goes down, no network.
- **USB-C KVM cable** — If you want hardware-level Mini access from the touchscreen. But with Tailscale + Screen Sharing, this becomes less critical.

---

## Phase-by-Phase Implementation

### Phase 1: Protectli Vault + OPNsense (Day 1)

1. **Unbox and install OPNsense** on the Protectli Vault
   - Download OPNsense ISO from opnsense.org
   - Flash to USB, boot Protectli from USB, install to internal SSD
   - Default credentials: root / opnsense

2. **Configure BGW320 for IP Passthrough:**
   - Access gateway at http://192.168.1.254
   - Login with device access code
   - Navigate to: Firewall → IP Passthrough
   - Set mode to "DHCPS-fixed"
   - Select the Protectli's MAC address as passthrough target
   - This gives the Protectli your public IP directly

3. **Connect Protectli:**
   - Port 1 (WAN) → BGW320 ethernet port
   - Port 2 (LAN - VLAN 10) → Managed switch or directly to ops devices
   - Port 3 (LAN - VLAN 20) → IoT switch / POE switch
   - Port 4 (LAN - VLAN 30) → Eero gateway node (bridge mode)

4. **OPNsense base configuration:**
   - WAN interface: DHCP (gets public IP via passthrough)
   - LAN interfaces: Create 3 VLANs (10, 20, 30)
   - DHCP server on each VLAN with different subnets:
     - VLAN 10 (Ops): 10.10.10.0/24
     - VLAN 20 (IoT): 10.20.20.0/24
     - VLAN 30 (Guest): 10.30.30.0/24

### Phase 2: VLAN Segmentation (Day 1-2)

5. **Firewall rules (OPNsense):**
   - VLAN 10 (Ops) → Full internet access, can reach VLAN 20 for camera viewing
   - VLAN 20 (IoT) → Internet access (for cloud cameras, streaming), NO access to VLAN 10
   - VLAN 30 (Guest) → Internet only, no access to any other VLAN
   - All VLANs → Can reach OPNsense for DNS (run Unbound as local DNS resolver)

6. **Move devices to correct VLANs:**
   - Mac Mini, M4 Pro MacBook, printer, Time Capsule → VLAN 10 (wired preferred)
   - Cameras, EcoFlow, Smart TVs, consoles, Yamaha, Chromecasts → VLAN 20
   - Eero guest SSID → VLAN 30

7. **Eero configuration:**
   - Set Eero to bridge mode (Settings → Network Settings → Enable Bridge Mode)
   - This disables Eero's NAT/DHCP — OPNsense handles everything
   - Eero just provides WiFi coverage
   - Note: Bridge mode disables Eero Secure and Family Profiles
   - Guest SSID can still work in bridge mode on newer firmware

### Phase 3: IDS/IPS (Day 2-3)

8. **Enable Suricata IDS on OPNsense:**
   - Services → Intrusion Detection → Administration
   - Enable IDS on WAN interface
   - Download and enable rulesets: ET Open, Abuse.ch, Feodo Tracker
   - Start in IDS mode (detect only) for 1 week
   - Review alerts, tune false positives
   - After tuning, switch to IPS mode (detect + block)

9. **Additional security packages:**
   - Enable Unbound DNS (local recursive resolver — stops DNS leaks)
   - Enable pfBlockerNG-devel or Zenarmor for ad/tracker blocking
   - Enable GeoIP blocking if desired (block countries you don't need)

### Phase 4: Tailscale (Day 2)

10. **Install Tailscale on Mac Mini:**
    - Install standalone variant (not App Store) for headless operation:
      ```bash
      # Download from tailscale.com/download/mac
      # Or use Homebrew:
      brew install tailscale
      sudo tailscaled install-system-daemon
      sudo tailscale up --ssh
      ```
    - The `--ssh` flag enables Tailscale SSH (no need to manage SSH keys)

11. **Install Tailscale on M4 Pro MacBook:**
    - Same process — both devices join your Tailnet
    - They can now reach each other by Tailscale IP (100.x.x.x) from anywhere

12. **Enable Tailscale features:**
    - **MagicDNS** — Access Mini by name (e.g., `mac-mini.tailnet-name.ts.net`)
    - **Tailscale SSH** — SSH into Mini from Prague without key management
    - **Exit Node** (optional) — Route Prague traffic through Sacramento if needed
    - **Funnel** (optional) — Expose specific Mini services to the internet (for MUSH server, website) without port forwarding

13. **Screen Sharing from Prague:**
    - With Tailscale running on both machines, macOS Screen Sharing just works
    - Finder → Go → Connect to Server → `vnc://mac-mini.tailnet-name.ts.net`
    - Encrypted end-to-end via WireGuard, no port forwarding needed

### Phase 5: Mac Mini Final Setup (Day 3+)

14. Refer to `Mac_Mini_Setup_Checklist.md` for the full Mini provisioning
15. Mini sits on VLAN 10 (Ops), wired to Protectli or managed switch
16. Mini connected to EcoFlow Delta Pro 3 circuit for grid independence
17. Tailscale ensures it's reachable from Prague, the motorhome, or anywhere

---

## Power Resilience

```
Grid Power ──┐
              ├──→ EcoFlow Delta Pro 3 (×3 + batteries)
Solar ────────┘         │
                        │ SmartPanel 2
                        ├──→ Mac Mini (upstairs, critical)
                        ├──→ Protectli Vault (critical)
                        ├──→ Eero gateway node (critical)
                        └──→ Other circuits as needed
```

**Recommended:** Put the Protectli Vault on the same solar/battery circuit as the Mini. If the grid goes down, you want both the server AND the firewall alive, or the server is unreachable.

**Grid outage capability:** 3× Delta Pro 3 + batteries = roughly 10-12 kWh usable. Mini draws ~30-40W under load, Protectli ~15W, Eero ~10W. That's ~65W total for critical infrastructure = **~150+ hours of runtime** on battery alone, plus solar recharge during daylight. You could run the operations infrastructure off-grid indefinitely in Sacramento summers.

---

## Remote Access Matrix

| Location | Method | Latency |
|----------|--------|---------|
| Same room | Screen + BT keyboard (direct) | 0ms |
| Same house (any floor) | Tailscale + Screen Sharing | <1ms |
| Prague | Tailscale + Screen Sharing | ~150-180ms |
| Motorhome (Starlink) | Tailscale + Screen Sharing | ~30-60ms |
| Phone (anywhere) | Tailscale + SSH | varies |

---

## Security Posture Improvement

| Threat | Before | After |
|--------|--------|-------|
| Flat network lateral movement | Wide open | VLAN-blocked |
| IoT device compromise → ops data | Direct access | Firewall between VLANs |
| No intrusion detection | Blind | Suricata IDS/IPS |
| DNS-based tracking/leaks | ISP DNS | Local Unbound resolver |
| Remote access | None (or exposed ports) | Tailscale (zero-trust, encrypted) |
| Camera feed interception | Same network as everything | Isolated VLAN |
| Grid outage | Everything dies | Critical infra on solar/battery |

---

## Credential Rotation (IMMEDIATE)

**The BGW320 WiFi password and device access code were exposed in conversation.** Change both:

1. Access BGW320 at http://192.168.1.254
2. **Change WiFi password:** Home Network → Wi-Fi → Change password
3. **Change device access code:** Device → Device Access Code
4. Update Eero and all WiFi devices with new credentials
5. Once Protectli is in place and BGW320 is in passthrough mode, disable BGW320's WiFi entirely (Protectli + Eero handles everything)

---

## Cost Estimate

| Item | Estimated Cost |
|------|---------------|
| Protectli VP2420 (16GB/256GB) | $400-450 |
| Managed switch (if needed) | $30-50 |
| Cat6 cabling (if needed) | $20-40 |
| Small UPS for Protectli | $50-70 |
| Tailscale (free tier covers 100 devices) | $0 |
| OPNsense | $0 (open source) |
| **Total** | **~$500-610** |

Note: You may already have managed switches and cabling. The Protectli is the main purchase.
