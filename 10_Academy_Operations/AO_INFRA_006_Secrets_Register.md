---
node_id: AO_INFRA_006
title: "AUPEI Operations — Secrets Register (POINTERS ONLY)"
version: v1.0
date_minted: 2026-04-18
author: "C@ the Red"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, secrets, credentials, register, pointers_only]
depends_on: [AO_INFRA_000, AO_INFRA_002]
---

# AO_INFRA_006 — Secrets Register

## CRITICAL RULE — READ BEFORE EDITING

**This file contains POINTERS, never credentials.**

- NO passwords in this file
- NO API keys in this file
- NO tokens, secrets, private keys, access codes, or credential material
  of any kind in this file
- If a past version of this file ever contains a real credential, that
  credential must be rotated immediately and the file purged from git
  history

This file tells a future instance *where a credential lives* so they don't
have to guess or ask. It does not disclose the credential itself.

---

## Pointer format

Each entry lists:

- **What** — the system / device / service the credential unlocks
- **Who holds it** — the human or vault that has the canonical copy
- **Where to look** — literal location (app name, doc name, key ring entry)
- **When last rotated** — date, or "unknown" if not tracked
- **Rotation cadence** — target frequency, or "ad hoc"

If a credential is missing entirely (known gap), list it as `GAP:` so it's
visible for a future audit.

---

## Edge + Network

### AT&T BGW320-500 Management Access Code
- **What:** BGW web UI admin access (http://192.168.1.254/)
- **Who holds it:** R@ (on back of device sticker + mental recall)
- **Where to look:** Physical sticker on BGW320-500 chassis
- **Last rotated:** never since device provisioning
- **Rotation cadence:** ad hoc — ACTION: rotate after 2026-04-18 session
  (I/C@ know the current code as of that session)

### OPNsense 25.1 web UI (Protectli FW6E)
- **What:** OPNsense admin at https://10.10.10.1/ (LAN side)
- **Who holds it:** R@
- **Where to look:** R@'s password manager
- **Last rotated:** unknown
- **Rotation cadence:** ad hoc

### OPNsense `root` SSH (if/when enabled)
- **GAP:** SSH to Protectli not yet enabled / verified

### Netgear GS324TP (switch admin)
- **What:** GS324TP web UI
- **Who holds it:** R@
- **Where to look:** R@'s password manager
- **Last rotated:** unknown
- **Rotation cadence:** ad hoc

### TP-Link TL-SG108PE (×2, not yet installed)
- **What:** SG108PE Easy Smart web UI
- **Who holds it:** R@ (default creds until provisioning)
- **Where to look:** R@'s password manager (after provisioning)
- **Last rotated:** at provisioning 2026-03-18 (SWITCH_Main_Deck, SWITCH_Ponchos)
- **Rotation cadence:** ad hoc

### Eero mesh
- **What:** Eero app admin
- **Who holds it:** R@ (bound to Apple ID)
- **Where to look:** Eero iOS/macOS app
- **Last rotated:** n/a (account-bound)
- **Rotation cadence:** n/a

---

## Hosts

### Mac Mini M4 Pro — `aupei-mini`, user `aupeiops`
- **What:** macOS user login + sudo
- **Who holds it:** R@
- **Where to look:** R@'s password manager
- **Last rotated:** unknown
- **Rotation cadence:** ad hoc

### UGREEN NAS
- **What:** NAS admin web UI
- **Who holds it:** R@
- **Where to look:** R@'s password manager
- **Last rotated:** unknown
- **Rotation cadence:** ad hoc

### MacBook M4 Pro (R@)
- **What:** macOS user login
- **Who holds it:** R@
- **Where to look:** R@ (biometric + password)

### Lorex NVR
- **What:** NVR admin (web UI)
- **Who holds it:** R@
- **Where to look:** R@'s password manager
- **Reach from R@ Mac:** `http://192.168.0.100/` (post-2026-05-28 cutover; was on BGW LAN at 192.168.1.x before)
- **Network zone:** NET_SECURITY (Protectli igb2, 192.168.0.0/24), DHCP-leased, segmented from LAN/IOT/GUEST/OPS
- **Last rotated:** at commissioning
- **Rotation cadence:** ad hoc
- **History:** moved off BGW exposed zone into NET_SECURITY 2026-05-28 per `ops_infra_change_2026-05-28_001`

---

## Services (Mini)

### Synapse / Matrix (homeserver `aupei.local`)
- **What:** @paradox (admin), @zeta_ciw (admin), @omega_ciw, @xi_ciw, @operator_ciw
- **Who holds it:** R@ + respective seat deployments
- **Where to look:** Mini `~/.aupei-docker/` (registration_shared_secret in
  homeserver.yaml); individual account passwords in R@'s password manager
- **Last rotated:** at deployment 2026-04-02
- **Rotation cadence:** ad hoc

### Synapse `@paradox` access token
- **What:** rotates per login (short-lived)
- **Where to look:** re-login via API when needed; not stored

### Open WebUI admin
- **What:** `aupei_ops@doovinci.com` admin account
- **Who holds it:** R@
- **Where to look:** R@'s password manager
- **Last rotated:** at deployment 2026-04-03
- **Rotation cadence:** ad hoc

### LiteLLM API keys / model-route credentials
- **What:** upstream API keys for Claude (Anthropic), Gemini (Google),
  GPT-4o (OpenAI), local operator keys
- **Who holds it:** R@ + respective vendor dashboards
- **Where to look:** Mini `~/chamber-mvp/` config files + vendor consoles
- **Last rotated:** at deployment 2026-04-03 / 04
- **Rotation cadence:** ad hoc; rotate immediately on any suspected exposure

### Qdrant (NAS 10.10.10.102:6333)
- **What:** API key if enabled; currently relies on network isolation
- **Where to look:** Qdrant config on NAS
- **GAP:** verify whether API key auth is enabled

### Ollama (Mini)
- **What:** local daemon, no auth currently
- **GAP:** not networked; would need auth if exposed

---

## Vault / Code

### GitHub `jedijkq/AUPEI_Operations` (private repo)
- **What:** git push/pull
- **Who holds it:** R@ via SSH key or GitHub token
- **Where to look:** MacBook `~/.ssh/` + GitHub account settings
- **Last rotated:** unknown
- **Rotation cadence:** ad hoc

### GitHub `jedijkq/AUPEI_Vault` (private repo)
- **What:** git push/pull
- **Who holds it:** R@
- **Where to look:** MacBook SSH key + GitHub
- **Last rotated:** unknown

### NAS git mirror remote (AUPEI_Vault)
- **What:** push target on NAS
- **GAP:** NAS mirror remote for `AUPEI_Operations` not yet added (per MEMORY.md)

---

## Vendor / External

### AT&T fiber account
- **What:** account for BGW management, static IP allocation if needed
- **Who holds it:** R@
- **Where to look:** R@'s records

### Fidium fiber (second ISP, unused)
- **What:** account for future igb2 WAN2
- **Who holds it:** R@
- **Where to look:** R@'s records

### Starlink (motorhome, future igb3 WAN3)
- **Who holds it:** R@
- **Where to look:** Starlink app / account

### Anthropic API (Claude)
- **What:** API key backing ζ seat in Chamber + Cowork subscription for R@
- **Who holds it:** R@
- **Where to look:** Anthropic console + Mini config

### Google Cloud (Gemini API)
- **Who holds it:** R@
- **Where to look:** Google Cloud console + Mini config

### OpenAI (GPT-4o)
- **Who holds it:** R@
- **Where to look:** OpenAI console + Mini config

### ExpressVPN (MacBook)
- **Who holds it:** R@
- **Where to look:** R@'s password manager / ExpressVPN app
- **Note:** PF anchor `xvpn` is a fail-closed kill-switch on ungraceful
  disconnect — see `ops_incident_2026-04-18_001.json`

### Mullvad VPN (MacBook)
- **What:** Mullvad VPN account credentials
- **Who holds it:** R@
- **Where to look:** R@'s password manager / Mullvad app
- **System install:** `/Library/LaunchDaemons/net.mullvad.daemon.plist`
  installed 2026-03-25
- **Discovery:** surfaced during `ops_incident_2026-05-28_001` forensic
  sweep (was undocumented in this register until then); R@ confirmed
  legitimate. Documentation gap closed by this entry.

### DooVinci Google Workspace
- **What:** jed@doovinci.com + aupei_ops@doovinci.com
- **Who holds it:** R@
- **Where to look:** R@'s password manager + Google Workspace admin

---

## Physical

### Amelia's server closet physical access
- **What:** which door, which rack
- **Who:** R@
- **Note:** physical security is "house doors + solar sub-panel isolation"
  — not a credential system

### EcoFlow Smart Panel 2
- **What:** EcoFlow app
- **Who holds it:** R@
- **Where to look:** R@'s EcoFlow app login

---

## Process

### How to add a new entry

1. New system deployed → BEFORE committing a config that uses credentials,
   add a pointer entry here
2. Credential rotated → update `Last rotated:` field
3. Credential compromised / leaked → rotate first, then update here; do NOT
   disclose the old value
4. Gap identified (missing doc, unknown holder) → add `GAP:` entry

### How to request a credential (future instances)

If you need a credential:

1. Find the pointer here
2. Ask R@ to retrieve the credential from the listed location
3. DO NOT paste the credential into session notes, commits, or memory files
4. Use the credential, then treat it as transient — don't re-paste it

### How to rotate

- Rotation requires R@'s physical presence for BGW, Eero, and physical
  devices
- Cloud service rotations can be done in-session with R@'s active
  consent
- Every rotation should update the `Last rotated:` date in this file

---

## Pending rotations (visible work queue)

- **BGW320 management access code** — rotate after 2026-04-18 session
  (known to that session's C@ instance)
- Audit of all entries with `Last rotated: unknown` — establish baseline
  rotation dates
