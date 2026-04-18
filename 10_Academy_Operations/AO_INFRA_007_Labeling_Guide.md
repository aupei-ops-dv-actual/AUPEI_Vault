---
node_id: AO_INFRA_007
title: "AUPEI Operations — Physical Labeling Guide"
version: v1.0
date_minted: 2026-04-18
author: "C@ the Red"
entity: AUPEI
vault: A
layer: operations
epistemic_status: ACTIVE
tags: [infrastructure, physical, labeling, hardware, documentation]
depends_on: [AO_INFRA_004, AO_INFRA_005]
---

# AO_INFRA_007 — Physical Labeling Guide

## Why this matters

A doc says "Eero #2 is on Main Deck wired to Amelia's port 3 of GS324TP".
A future R@ (or a contractor, or an emergency responder) is standing in
front of three identical Eeros on Main Deck. None of them are labeled.
The doc is correct and useless at the same time.

Physical labels turn documentation into operable knowledge. They cost
~$30 in label tape and 2 hours of work, and they save hours of
"which one was it?" every time we touch the rack.

This guide is the standard. Apply it to existing devices in the next
on-site session, and to new devices at install time going forward.

---

## Materials

- **Label printer:** Brother P-touch or similar (R@'s call)
- **Tape:** 12mm white-on-clear or black-on-white, laminated, indoor
- **Backup:** Sharpie + masking tape for emergencies

Avoid hand-written paper labels for permanent equipment. They fade,
peel, and lose authority.

---

## Label content standard

Every infrastructure device gets a label with these fields:

```
DEVICE_ID   (canonical name from AO_INFRA_005 manifest)
ROLE         (one line: what it does)
ADDR         (IP if static, "DHCP" if not)
CABLES       (key uplink — "→ Amelia GS324TP p3")
DATE         (install / last revision)
```

**Maximum 5 lines.** If it doesn't fit, the device name is too verbose.

---

## Naming convention

Mirror the AO_INFRA_002 / 005 naming. Examples:

| Device | Label DEVICE_ID |
|---|---|
| Protectli FW6E | `EDGE_PROTECTLI` |
| BGW320-500 | `WAN_BGW320` |
| Netgear GS324TP | `CORE_GS324TP` |
| TP-Link SG108PE on Main Deck | `SWITCH_MAIN_DECK` |
| TP-Link SG108PE on Pancho's | `SWITCH_PANCHOS` |
| QNAP QSW-M2106-4C | `WORKSTATION_QSW` |
| Eero (Main Deck primary) | `EERO_MAIN_1` |
| Eero (Main Deck secondary) | `EERO_MAIN_2` |
| Eero (Main Deck extender) | `EERO_MAIN_X` |
| Eero (Pancho's) | `EERO_PANCHOS` |
| Mac Mini | `HOST_MINI` |
| UGREEN NAS | `HOST_NAS` |
| Lorex NVR | `NVR_LOREX` |
| EcoFlow Delta Pro 3 (×3) | `PWR_EFDP3_A`, `_B`, `_C` |
| EcoFlow Smart Panel 2 | `PWR_SMARTPANEL` |

Use ALL_CAPS, no spaces, role-prefix for grouping. Length ≤16 chars where
possible.

---

## Per-device label specifications

### Edge / Network Core (Amelia's Server Closet)

#### `EDGE_PROTECTLI` (Protectli FW6E)
```
EDGE_PROTECTLI
OPNsense edge router (single NAT)
WAN igb0: 99.105.38.252/22 (DHCP)
LAN igb1: 10.10.10.1/24
2026-04-18
```
Place on top face of chassis.

#### `WAN_BGW320` (AT&T BGW320-500)
```
WAN_BGW320
AT&T fiber GW (transparent bridge)
Mgmt: 192.168.1.254
Pinned to EDGE_PROTECTLI MAC
2026-04-18
```

#### `CORE_GS324TP` (Netgear GS324TP)
```
CORE_GS324TP
24-port PoE switch (LAN core)
Trunk in: p1 ← EDGE_PROTECTLI
Cameras: p5-16, NVR p17
2026-XX-XX (update at VLAN cut)
```

### Switches (per-port labels)

For multi-port switches, also label EACH USED PORT with a small flag
indicating what's connected:

GS324TP example port labels:
- `p1: ← PROTECTLI igb1`
- `p2: → WORKSTATION_QSW (trunk)`
- `p3: → SWITCH_MAIN_DECK`
- `p4: → SWITCH_PANCHOS`
- `p5–16: PoE cameras`
- `p17: NVR_LOREX`

TP-Link SG108PE port labels match the AO_INFRA_004 port table.

### Eeros

Each Eero gets a label on top:
```
EERO_MAIN_1
Mesh master, wired
Uplink: SWITCH_MAIN_DECK p5
2026-XX-XX
```

The Eero app names should match these IDs (rename in app to match
physical label).

### Hosts

Mini and NAS get small labels on a non-vent surface:
```
HOST_MINI
aupei-mini (M4 Pro 64GB)
LAN: ~10.10.10.119
Boot-sovereign (OpenJarvis)
```

```
HOST_NAS
UGREEN NAS
LAN: 10.10.10.102
NFS lanes + Qdrant 6333
```

### Power

Each EcoFlow Delta Pro 3 gets a letter suffix and circuit assignment:
```
PWR_EFDP3_A
EcoFlow Delta Pro 3 (Battery A)
Capacity: ~6 kWh
Feeds: PWR_SMARTPANEL
```

### Cabling

Every cat6 run between rooms gets a flag at BOTH ends:
- `→ AMELIA SVR CLOSET` (at Main Deck end)
- `→ MAIN DECK` (at Amelia end)
- `→ PANCHOS` and `→ MAIN DECK` for that run

Avoid relying on color alone. Color helps; printed text wins.

### Power cords

For any device whose unplugging would be disruptive (Mini, NAS, Protectli,
NVR, BGW), wrap a small flag at the plug end:
```
DO NOT UNPLUG
HOST_MINI — boot-sovereign
```

---

## Application sequence (suggested)

When a future on-site session has time for labeling:

1. Print all labels for current AO_INFRA_004 devices using this guide
2. Start with the rack in Amelia's server closet (highest density, highest
   confusion risk)
3. Label devices first, then port flags, then cable ends
4. Walk to Main Deck, then Pancho's
5. Update Eero app names to match physical labels
6. Take a photo of each labeled device, store under
   `AUPEI_Vault/10_Academy_Operations/photos/2026-MM-DD_labeling/`
7. Append a short ops_log entry (`log_type: "infra_change"`) recording
   the labeling pass

---

## Maintenance

- When a device is replaced → remove the old label and apply a new one in
  the same session
- When an IP changes → re-print and re-apply
- When a cable is moved → re-flag both ends in the same session
- Labels older than 18 months should be inspected for legibility

---

## Anti-patterns

- **Sharpie on chassis** — looks ugly, hard to update, may damage finish
- **Numeric-only labels** ("Switch 1") — meaningless without an external
  legend doc that nobody reads
- **Labels on bottoms/backs only** — you have to lift / move the device to
  read them; defeats the purpose
- **Encoded labels** ("X-1-A") — require decoding; just use the canonical
  name from AO_INFRA_005

---

## Related docs

- `AO_INFRA_004_Physical_Topology.md` — what's where
- `AO_INFRA_005_Hardware_Manifest.md` — canonical device IDs
- `AO_INFRA_000_RUNNING.md` — current state, address tables
