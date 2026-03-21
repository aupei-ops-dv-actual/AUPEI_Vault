---
node_id: AO_INFRA_003
title: "Sunday Provisioning Runbook — Mac Mini & Protectli FW6E"
version: v1.0
date_minted: 2026-03-15
author: "C@ the Red"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, provisioning, mac-mini, opnsense, protectli]
depends_on: [AO_INFRA_002]
---

# Sunday Provisioning Runbook
## Block 1: Mac Mini (M4 Pro) · Block 2: Protectli FW6E (Bench Only)

**Date:** 2026-03-15 (Sunday)
**Operator:** R@
**Support:** C@ the Red

---

## Pre-Flight Checklist

- [ ] Portable monitor (UPERFECT 18.5") — USB-C cable + power cable
- [ ] Bluetooth keyboard + mouse (or wired USB-C)
- [ ] Mac Mini power cable
- [ ] Protectli FW6E + power adapter
- [ ] USB flash drive (8GB+) for OPNsense installer
- [ ] Ethernet cables (×2 minimum — one for Mini, one for Protectli bench test)
- [ ] Second monitor or same portable for Protectli (VGA/HDMI — check Protectli ports)
- [ ] M4 Pro MacBook (for downloading ISOs, Tailscale admin, and C@ support)

---

## BLOCK 1 — Mac Mini Provisioning

**Location:** Amelia's Floor (upstairs server room / workstation area)
**Time estimate:** 45-60 minutes

### 1.1 Physical Setup

1. **Position the Mini** at its permanent desk location on Amelia's floor
2. **Connect UPERFECT monitor:**
   - USB-C to USB-C (preferred — carries video + power to monitor)
   - If Mini's USB-C ports are all Thunderbolt 5, any of the 3 rear TB5 ports work
   - Alternative: HDMI cable to the Mini's HDMI port
3. **Connect ethernet** to existing network (temporary — flat network for now)
   - The Mini has 10GbE built in. Use the RJ45 port on the back
   - It'll get a DHCP address from whatever's serving now (BGW320 or Eero)
4. **Connect power, boot**
5. **Pair Bluetooth keyboard + mouse** (or connect wired USB)

### 1.2 macOS Initial Setup

Walk through the macOS Setup Assistant:

- **Language/Region:** English (US)
- **Accessibility:** Skip for now
- **Network:** Should auto-detect wired ethernet
- **Sign in with Apple ID:** Use R@'s primary Apple ID
  - Enable iCloud Drive, Find My Mac
  - iCloud Keychain: Yes (for credential sync)
- **Computer Name:** `AUPEI-Mini` (or `aupei-mini` — we'll reference this in Tailscale)
- **Create local admin account:**
  - Full name: whatever
  - Account name: `ratops` (or R@'s preference)
  - Strong password — store in keychain
- **Enable FileVault:** YES — full disk encryption is non-negotiable for ops hardware
- **Enable Location Services:** Your call, but recommended for Find My
- **Skip Screen Time, Siri** for now

### 1.3 System Configuration

Once at the desktop:

```
# Open Terminal (Cmd+Space → "Terminal")

# 1. Set hostname properly
sudo scutil --set ComputerName "AUPEI-Mini"
sudo scutil --set HostName "aupei-mini"
sudo scutil --set LocalHostName "aupei-mini"

# 2. Show hidden files in Finder
defaults write com.apple.finder AppleShowAllFiles YES
killall Finder

# 3. Enable SSH (for Tailscale SSH fallback and local access)
sudo systemsetup -setremotelogin on

# 4. Disable sleep when on power
sudo pmset -c sleep 0
sudo pmset -c disksleep 0
sudo pmset -c displaysleep 15

# 5. Enable auto-restart after power failure
sudo pmset -a autorestart 1

# 6. Check 10GbE link status
networksetup -listallhardwareports
# Look for "Ethernet" with speed reported
# Verify link with:
ifconfig en0  # (or whichever is the 10GbE port)
```

### 1.4 Install Core Stack

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH (Apple Silicon)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

# Core tools
brew install git wget curl htop tree jq

# Tailscale (standalone — not App Store version)
brew install --cask tailscale

# Docker via OrbStack (much better than Docker Desktop on Apple Silicon)
brew install --cask orbstack

# Syncthing (for IDIOTH_WINDS mirror to NAS when it arrives)
brew install syncthing
# Don't start yet — configure when NAS is ready

# Obsidian (for Vault D / ξ Sandbox when ready)
brew install --cask obsidian

# VS Code (optional but useful for remote dev)
brew install --cask visual-studio-code

# Python (for future local model work)
brew install python@3.12

# Node.js (for future MUSH/web work)
brew install node
```

### 1.5 Tailscale Setup

```bash
# Open Tailscale app (it installs as a menu bar app)
# Or from CLI:
open /Applications/Tailscale.app

# In the menu bar:
# 1. Click Tailscale icon → Log in
# 2. Authenticate with R@'s Tailscale account
#    (create one at login.tailscale.com if needed — free tier covers 100 devices)
# 3. The Mini gets a 100.x.x.x Tailscale IP

# Enable Tailscale SSH (run in Terminal):
# Go to Tailscale admin console → Settings → SSH
# Add an ACL rule allowing SSH access
```

**Then on the M4 Pro MacBook:**

```bash
# If not already installed:
brew install --cask tailscale
# Log in with same Tailscale account
# Both machines now see each other on the Tailnet

# Test connectivity from M4:
ping aupei-mini  # (MagicDNS name)
# or
ping 100.x.x.x  # (Mini's Tailscale IP shown in admin console)

# Test Screen Sharing from M4:
# Finder → Go → Connect to Server → vnc://aupei-mini
```

### 1.6 Verify & Snapshot

- [ ] Mini boots cleanly, FileVault enabled
- [ ] Wired ethernet connected (check with `ifconfig`)
- [ ] Homebrew installed and working (`brew --version`)
- [ ] Tailscale connected, M4 ↔ Mini ping works
- [ ] Screen Sharing from M4 to Mini works over Tailscale
- [ ] SSH from M4 to Mini works: `ssh ratops@aupei-mini`
- [ ] Mini set to never sleep on AC power
- [ ] Auto-restart after power failure enabled

**Block 1 complete. Mini is live, reachable, and ready for Vault D build later.**

---

## BLOCK 2 — Protectli FW6E Bench Provisioning

**Location:** Amelia's floor desk (bench setup — NOT in live network)
**Time estimate:** 60-90 minutes

> **IMPORTANT:** The FW6E does NOT go into the live network today.
> Without the managed switches (arriving mid-week), inserting the Protectli
> would mean the whole house runs through it on a flat network — defeating
> the purpose and risking an outage if config isn't right.
>
> Today we: install OPNsense, configure interfaces, define VLANs, set
> firewall rules, enable Suricata — all on the bench. When switches arrive,
> we do a single clean cutover.

### 2.0 Know Your FW6E

The Protectli FW6E has **6 Intel i211 Gigabit Ethernet ports** and typically:
- Intel Core i5 (6th/7th gen depending on variant)
- 8-16GB RAM (check what yours shipped with)
- Internal mSATA or M.2 SSD
- VGA + HDMI output
- 2× USB 3.0
- AES-NI support (critical for VPN/encryption performance)
- Fanless

**Check your specific variant's RAM and storage.** If it's 8GB, that's fine for our setup with Suricata. 16GB is better but not blocking.

### 2.1 Prepare OPNsense Installer

**On the M4 Pro MacBook:**

```bash
# 1. Download OPNsense (amd64, vga image for USB boot)
# Go to: https://opnsense.org/download/
# Select:
#   Architecture: amd64
#   Image type: vga (for console/monitor install)
#   Mirror: closest to Sacramento
# Download the .img.bz2 file

# 2. Decompress
cd ~/Downloads
bunzip2 OPNsense-*.img.bz2

# 3. Flash to USB drive
# Insert USB drive, find its device name:
diskutil list
# Look for your USB drive (e.g., /dev/disk4)

# CAREFUL — this erases the USB drive:
diskutil unmountDisk /dev/disk4
sudo dd if=OPNsense-*.img of=/dev/rdisk4 bs=4m
# Wait for completion (no progress bar — be patient, ~2-5 min)
# Then:
diskutil eject /dev/disk4
```

### 2.2 Install OPNsense to Protectli

1. **Connect portable monitor** to Protectli (HDMI or VGA)
2. **Connect USB keyboard** (not Bluetooth — BIOS/boot won't see BT)
3. **Insert OPNsense USB drive**
4. **Power on Protectli**
5. **Enter BIOS** (usually DEL or F2 at POST)
   - Verify AES-NI is enabled (should be by default)
   - Set boot order: USB first
   - Save and exit
6. **Boot from USB** — OPNsense live environment loads
7. **Login:** `installer` / `opnsense`
8. **Run installer:**
   - Select keymap (US)
   - Select "Install (ZFS)" if SSD is large enough, or "Install (UFS)" for simpler setup
   - Select the internal SSD as target (NOT the USB drive)
   - Confirm — installer writes to SSD
9. **Remove USB drive when prompted, reboot**

### 2.3 Initial OPNsense Configuration (Console)

After reboot, OPNsense presents a console menu. Login: `root` / `opnsense`

**Interface Assignment:**

The FW6E has 6 ports. OPNsense will detect them as `igb0` through `igb5`. You need to figure out which physical port maps to which interface name.

```
# At the console menu, select option 1: Assign interfaces

# When asked about VLANs: YES (we'll set them up)
# When asked about WAN: select igb0 (Port 1 — leftmost usually)
# When asked about LAN: select igb1 (Port 2)
# Optional interfaces: skip for now — we'll use VLANs on LAN

# If unsure which port is which:
# Plug ethernet into one port at a time
# The console shows link-up/link-down events
# Label the ports with tape as you identify them
```

**Set LAN IP (for bench access):**

```
# Select option 2: Set interface IP address
# Choose LAN (igb1)
# Set IPv4: 10.10.10.1
# Subnet: 24 (255.255.255.0)
# Enable DHCP on LAN: YES
# DHCP range: 10.10.10.100 — 10.10.10.199
```

### 2.4 Web GUI Configuration

1. **Connect M4 MacBook directly to Protectli Port 2 (LAN) with ethernet cable**
   - Or use a USB-C ethernet adapter if needed
   - Your Mac should get a DHCP address in the 10.10.10.x range
2. **Open browser:** `https://10.10.10.1`
   - Accept the self-signed cert warning
   - Login: `root` / `opnsense`
3. **Run the Setup Wizard:**
   - Hostname: `protectli`
   - Domain: `aupei.local`
   - DNS: Leave default for now (we'll switch to Unbound later)
   - Time zone: America/Los_Angeles
   - WAN: DHCP (will get public IP via passthrough later)
   - LAN: Already set to 10.10.10.1/24
   - Change root password to something strong — store securely

### 2.5 Create VLANs

**Interfaces → Other Types → VLAN:**

| VLAN Tag | Parent Interface | Description |
|----------|-----------------|-------------|
| 10 | igb1 (LAN) | OPS_TRUSTED |
| 20 | igb1 (LAN) | IOT_UNTRUSTED |
| 30 | igb1 (LAN) | GUEST_ISOLATED |

> NOTE: We're creating VLANs on the LAN parent interface. When the managed
> switches arrive, the LAN port trunks all three VLANs to the switch, and
> the switch assigns ports to VLANs. For now on bench, we just define them.

**Interfaces → Assignments → Assign each VLAN:**

- VLAN 10 → Name: `OPS` → Enable → IPv4: 10.10.10.1/24 → DHCP: 10.10.10.100-199
- VLAN 20 → Name: `IOT` → Enable → IPv4: 10.20.20.1/24 → DHCP: 10.20.20.100-199
- VLAN 30 → Name: `GUEST` → Enable → IPv4: 10.30.30.1/24 → DHCP: 10.30.30.100-199

### 2.6 Firewall Rules

**Firewall → Rules → [each interface]:**

**OPS (VLAN 10) — Trusted:**
```
Pass | IPv4+6 | * | OPS net | * | * | * | # Full access out
Pass | IPv4   | * | OPS net | * | IOT net | 80,443,554 | # Camera viewing (HTTP, HTTPS, RTSP)
```

**IOT (VLAN 20) — Restricted:**
```
Block | IPv4 | * | IOT net | * | OPS net | * | # NO access to ops
Block | IPv4 | * | IOT net | * | GUEST net | * | # NO access to guest
Pass  | IPv4 | * | IOT net | * | * | * | # Internet access (for cloud cams, streaming)
```
> Note: The block rules must be ABOVE the pass rule (rules evaluated top-down)

**GUEST (VLAN 30) — Internet Only:**
```
Block | IPv4 | * | GUEST net | * | 10.0.0.0/8 | * | # Block ALL private ranges
Pass  | IPv4 | * | GUEST net | * | * | * | # Internet only
```

**WAN — Default deny inbound (already set by OPNsense defaults)**

### 2.7 DNS — Unbound

**Services → Unbound DNS → General:**
- Enable: ✓
- Listen port: 53
- Network interfaces: All (LAN, OPS, IOT, GUEST)
- DNSSEC: Enable
- Register DHCP leases: ✓ (so you can reach devices by name)

This gives every VLAN a local recursive DNS resolver. No more leaking DNS queries to AT&T or Google.

### 2.8 Suricata IDS

**Services → Intrusion Detection → Administration:**
- Enable: ✓
- IPS mode: OFF for now (detect only — we'll tune first)
- Interfaces: WAN
- Pattern matcher: Hyperscan (fastest, uses AES-NI)
- **Download rulesets:**
  - ET Open (emerging threats)
  - Abuse.ch SSL Blacklist
  - Feodo Tracker

**Services → Intrusion Detection → Schedule:**
- Enable automatic rule updates: ✓
- Every 6 hours

> Suricata stays in IDS mode (alert-only) until after the full network cutover.
> We'll tune false positives for a week, then switch to IPS (block mode).

### 2.9 Additional Hardening

```
# System → Settings → Administration:
- Disable HTTP redirect (HTTPS only): ✓
- TCP port: 8443 (move off default 443)
- Disable console login password: NO (keep it)
- Enable Secure Shell: ✓ (for emergency access)

# System → Firmware → Plugins — Install:
- os-theme-cicada (optional — dark theme, easier on the eyes)

# Firewall → Settings → Advanced:
- Clear invalid DF bits: ✓
- Enable firewall state scrubbing: ✓
```

### 2.10 Bench Verification

- [ ] OPNsense installed and boots from internal SSD
- [ ] Web GUI accessible at https://10.10.10.1
- [ ] Root password changed from default
- [ ] VLANs 10, 20, 30 created and assigned
- [ ] Firewall rules defined for each VLAN
- [ ] Unbound DNS enabled
- [ ] Suricata IDS enabled (detect mode) with rulesets downloaded
- [ ] SSH enabled for emergency access
- [ ] Hostname set to `protectli.aupei.local`

**Block 2 complete. Protectli is configured and ready. Stays on the bench until switches arrive.**

---

## What We're NOT Doing Today

| Task | Why Not | When |
|------|---------|------|
| BGW320 IP Passthrough | Need switches first for clean cutover | Mid-week |
| Moving devices to VLANs | Need switches to assign ports | Mid-week |
| Eero bridge mode | Would kill WiFi mid-transition | Mid-week cutover |
| NAS assembly | Drives arriving Tuesday | Mid-week |
| Protectli in live network | No switches = flat network through firewall = pointless | Mid-week |

---

## Mid-Week Cutover Sequence (Preview)

When the 2× TP-Link TL-SG108PE + 1× QNAP QSW-M2106-4C + UGREEN NAS arrive:

1. **Pre-stage switches** — configure VLANs on all three new switches + GS324TP
2. **Assemble NAS** — install 4× IronWolf Pro 8TB, RAID 5, basic config
3. **Protectli goes live** — WAN port to BGW320 (IP Passthrough), LAN trunk to GS324TP in Amelia's rack
4. **Configure GS324TP** (Amelia's rack) — trunk port to Protectli, trunk port to QNAP desk switch, VLAN 20 access ports for cameras, PoE for future expansion
5. **Floor run from GS324TP → QNAP QSW-M2106-4C** (Amelia's desk/workstation area) — single trunked cable across attic
6. **Connect Mini to QNAP desk switch** on VLAN 10 access port (10GbE)
7. **Connect NAS to QNAP desk switch** on VLAN 10 access port (10GbE)
8. **Run ethernet to Main Deck** — connect TP-Link TL-SG108PE #1, trunk from GS324TP or Protectli
9. **Run ethernet to Poncho's floor** — connect TP-Link TL-SG108PE #2, trunk from above
10. **Configure BGW320 IP Passthrough** → Protectli takes public IP
11. **Eero to bridge mode** — connect to appropriate VLAN per floor
12. **Verify all VLANs** — test isolation, internet access, cross-VLAN camera viewing
13. **Enable Suricata IPS** after 1 week of IDS tuning

---

## Hardware Reference

| Device | Specs | Role | VLAN | Location |
|--------|-------|------|------|----------|
| Mac Mini | M4 Pro, 64GB, 2TB, 10GbE | Tier 1 Ops / Vault D | 10 | Amelia's |
| M4 Pro MacBook | R@'s workstation | Primary ops | 10 | Mobile |
| Protectli FW6E | 6-port GbE, OPNsense | Firewall/router | — | Amelia's |
| UGREEN DXP4800 Pro | i3-1315U, 8GB DDR5, 4-bay | Tier 3 NAS | 10 | Amelia's |
| 4× IronWolf Pro 8TB | ST8000NT001 | RAID 5 (~24TB usable) | — | In NAS |
| QNAP QSW-M2106-4C | 2.5G+10G managed switch | Desk switch | Trunk | Amelia's |
| TP-Link TL-SG108PE ×2 | 8-port managed PoE | Floor switches | Trunk | Poncho's + Main Deck |
| Netgear GS324TP | 24-port managed PoE+ | Camera/IoT switch | 20 | Amelia's |
| Eero mesh (×4) | WiFi coverage | WiFi AP (bridge mode) | 30 | All floors |

---

## Notes

- **FW6E vs VP2420:** AO_INFRA_002 recommended VP2420. R@ has FW6E — this is
  actually better hardware (6 ports vs 4, Intel Core i5 vs Celeron N5105).
  More than adequate. The extra ports give us flexibility (could dedicate a port
  per VLAN instead of trunking, though trunking is cleaner).
- **GS324TP already managed:** This is a win. The existing 24-port PoE switch
  for cameras already supports VLANs. We trunk VLAN 20 to it mid-week and all
  cameras land on the IoT VLAN without changing a single cable.
- **10GbE Mini ↔ NAS:** The QNAP QSW-M2106-4C has 4× combo 10GbE ports. Mini
  and NAS both have 10GbE. They'll talk at wire speed through the desk switch.
  This matters for Time Machine backups and IDIOTH_WINDS sync.
- **Amelia's floor split topology:** GS324TP lives in the server room rack
  (with Protectli, BGW320, cameras). QNAP desk switch lives at the workstation
  area (with Mini, NAS). Single trunked floor run connects them across the
  attic. QNAP was deliberately chosen as PoE to allow future camera expansion
  on the workstation side without additional floor runs.
