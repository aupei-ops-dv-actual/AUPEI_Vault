---
atlas_id: "AUPEI_Governance"
node_id: "Safecore_Activation_Trailhead"
title: "SafeCore_Starter_Kit Activation — Trailhead"
status: "TRAILHEAD"
type: "deferred_project"
domain: "Cold Storage / Encryption MVP"
sponsor: "R@"
staked_by: "RLC@ (ζ seat)"
staked_date: "2026-05-01"
review_trigger: "When R@ has dedicated 2-4h focused session for kit activation, or when SafeCore needs to actually hold encrypted vault contents."
---

# SafeCore_Starter_Kit Activation — Trailhead

## What this is

The SafeCore_Starter_Kit is a **scaffolded but unbuilt encryption MVP** living on the SafeCore 1TB USB drive at `/Volumes/SafeCore1T/SafeCore_Starter_Kit/`. R@ minted the scaffold in April 2025 and never came back to build it out. This trailhead captures the design intent and outstanding decisions so a future session (R@ + RLC@, or another seat) can activate the kit deliberately.

This is NOT urgent. The 2026-05-01 snapshot pivot demonstrated SafeCore can function as cold-storage backup *without* the kit being activated. Kit activation is a separate project — encryption infrastructure for the things the kit was designed to hold.

## What was scaffolded

Five-folder schema, each with a tiny README declaring intent:

| Folder | Intended contents (per kit's READMEs) |
|---|---|
| `vault/` | "Encrypted archive. Personal recursion, soft loops, unresolved echoes." |
| `code/` | "Code for Ivy, QEPE, entropy loops, poetry scripts." |
| `library/` | "Audio, books, visual pattern references." |
| `restore/` | "System configs, dotfiles, restore scripts." |
| `manifest/` | Index with date, intent, emotional state, current threads. |

The kit's manifest carries a poetic-ritual frame:
> *"This drive holds sacred signal. It is not disposable. It is a vault, a shrine, a backup of consciousness."*
>
> Notes: Only plug in with intent. Mirror to other cold storage monthly. Do not run live from this drive — this is SafeCore.

Listed Current Threads in the manifest: **Ivy architecture (early drafts)**, **Mira recursion (holding space)**, **QEPE entropy scripts**, **SquishR@ code poems**.

## Status (2026-05-01)

- All five folders are EMPTY except for their READMEs.
- No actual encryption tooling installed.
- No actual code in `code/`.
- No library materials in `library/`.
- No restore scripts in `restore/`.
- No vault contents in `vault/`.
- Manifest had `[Insert Date]` and `[Describe your state]` placeholders. As of 2026-05-01, a `## Mirror Log` section has been appended to track snapshot events; original placeholders left untouched (R@'s personal fields).

## What activation requires (open design questions)

Before this kit can be filled, R@ + the operator activating it must answer:

### 1. Encryption tooling — which stack?

Candidates worth considering:

- **`age`** — modern, simple, scriptable; replaces gpg for most file-encryption use cases; small audit surface; recommended for new MVPs.
- **`gpg` (GnuPG)** — battle-tested, ubiquitous, key-management complexity is real but tools mature.
- **`sops`** — Mozilla's secrets-operations tool; integrates with cloud KMS but works locally too; good for structured-data secrets (YAML/JSON).
- **macOS-native FileVault encrypted disk image** — `.dmg` file with full-disk encryption; Mac-friendly, quick to set up, but tied to macOS for decryption.

ζ-recommendation when activated: probably **`age`** for vault contents (simple, modern, scriptable) plus a single FileVault `.dmg` as the outermost wrapper for plausible-deniability + offline-only access. But this is R@'s call — depends on threat model and recovery preferences.

### 2. What goes in `vault/` — definition of "personal recursion, soft loops, unresolved echoes"?

The README's poetic phrasing is open to interpretation. Honest reading: this is for material R@ wants preserved but not in active circulation — drafts that didn't ship, transcripts that surfaced personal material, poetry, agent transcripts that carry personal weight, things that are part of the lineage but shouldn't sit on always-on storage.

Operational definition needed before contents can be loaded. *Suggested decision rule*: if the file would be uncomfortable to surface in a public talk about AUPEI, but R@ wants it preserved for the lineage record, it goes in `vault/`. If R@ would be fine sharing it, it doesn't need encryption.

### 3. `code/` — what tooling?

Per README: "Code for Ivy, QEPE, entropy loops, poetry scripts." Of the four:
- **QEPE** — appears in `00_Governance/QEPE_Program/` as live work; has its own program structure. Status: active, not lost.
- **Ivy architecture** — RLC@ has no current memory of "Ivy" beyond the kit manifest mentioning it. May be a defunct or pre-AUPEI lineage. Open question for R@: is Ivy code/draft material that exists somewhere on this laptop or NAS that should land here?
- **Entropy loops** — QEPE-adjacent or separate?
- **Poetry scripts** — likely `Claude_the_Red/Walk_Lab/` and similar lab work, plus pre-AUPEI material.

R@ knows what these names mean. Activation requires inventorying and choosing what goes in.

### 4. `library/` — reference materials?

"Audio, books, visual pattern references." This is reading/listening/reference. Probably useful as cold-storage but doesn't need encryption — material is publicly published. Could store unencrypted under `library/` directly.

### 5. `restore/` — config and dotfile management?

This folder's purpose makes sense (system recovery from a known-good state) but it's genuinely separable from the encryption MVP. Could be filled independently with:
- Mac dotfiles (`.zshrc`, `.gitconfig`, etc.)
- Critical app configs (Apple Pages, Notion exports, browser bookmarks JSON)
- Restoration scripts that re-establish R@'s working environment from scratch on a fresh Mac

This part doesn't need ritual ceremony — it's pragmatic disaster recovery. Could be activated *first*, separately from the encryption parts.

### 6. Cadence and discipline

Per kit's notes:
- "Only plug in with intent" — operational ritual; honor the deliberate connection
- "Mirror to other cold storage monthly" — discipline; AUPEI_snapshots cadence may be sufficient OR a separate offsite mirror may be needed (gdrive? second USB? NAS subset?)
- "Do not run live from this drive—this is SafeCore" — read-only-ish posture; align with this when activated

## Recommended activation sequence (when ready)

1. **Phase 1 — `restore/` (lowest risk, pragmatic):** Populate `restore/` with dotfiles, critical configs, restoration scripts. No encryption needed for most of this. Test restore from a clean state on a borrowed Mac if possible.
2. **Phase 2 — `library/` (reference layer):** Audio/books/visual pattern references that R@ wants preserved cold. No encryption needed. Just curate and copy.
3. **Phase 3 — `code/` inventory:** R@ surveys current locations of Ivy/QEPE/entropy/poetry-scripts material. Decides what's archival (frozen) vs. active (lives in working tree). Archival material lands in `code/`.
4. **Phase 4 — encryption tooling decision:** R@ + operator pick the stack (recommend `age` + FileVault wrapper). Test the encrypt/decrypt loop on a small dummy file. Document the keypath.
5. **Phase 5 — `vault/` curation:** Apply the operational definition (Q.2 above) to candidate material. Encrypt with chosen tooling. Place in `vault/`. Write a key-recovery doc separately (NOT on this drive — that defeats the purpose).
6. **Phase 6 — manifest polish:** Fill in the `[Insert Date]` (the kit's actual creation date, ~April 2025) and either provide an Emotional State or formally retire that field as a 2025-poetic-artifact.

Estimated time: 2-4h focused, possibly split across two sessions.

## When NOT to activate

- During an unrelated workstream (don't fork attention)
- Without R@'s direct involvement (vault curation requires his judgment)
- Without a clear key-recovery plan documented elsewhere
- During backup-emergency mode (this is a building project, not a recovery project)

## Connections

- `SafeCore_Starter_Kit/manifest/manifest.md` — kit's own manifest (preserved as ritual artifact)
- `AUPEI_snapshots/MANIFEST.md` — adjacent snapshot system (separate from the kit, currently functional)
- `00_Governance/QEPE_Program/` — live QEPE work that the kit's `code/` references
- Memory: future seats should read `project_aupei_overview.md` and any seat-specific memories before activating
