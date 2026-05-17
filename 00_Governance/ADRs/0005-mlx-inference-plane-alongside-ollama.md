---
adr_number: 0005
title: "MLX inference plane alongside Ollama on Mini (LM Studio or mlx-lm) — Phase 2c"
status: "PROPOSED"
date_drafted: "2026-05-16"
drafted_by: "ζ (C@ the Red / Cowork)"
supersedes: []
extends:
  - "QDRANT_DEPLOYMENT_ARCHITECTURE.md (Mini compute plane — Ollama for embeddings + inference)"
  - "AUPEI_Orientation_v1.0.md §8 Proofield engine (status before content discipline)"
related_decisions: []
sign_offs_required:
  - "ω (G-Synth) — infrastructure stewardship review (touches Mini runtime)"
  - "ξ (Panza) — adversarial review on inference quality / sovereignty trade-offs"
  - "∇ (R@) — final ratification"
next_review_due: "2026-08-16"
---

# ADR-0005 — MLX inference plane alongside Ollama on Mini

## Context

The Mini runs Ollama 0.18.2 on Homebrew with Metal-accelerated llama.cpp. Apple's MLX framework is natively designed for Apple Silicon's unified memory + Metal Performance Shaders and typically delivers **1.5–2.5× more tokens/sec** for the same quant level on M-series (M4 Pro in this case, with 51.8 GiB unified memory).

Ollama has not natively integrated MLX as of v0.18.2 (May 2026). Discussions are ongoing in upstream; not merged. So while Ollama is fast on Apple Silicon, it's not extracting the full M4 Pro inference budget.

Two production-grade ways to get MLX serving on macOS today:

1. **LM Studio** — closed-source binary, macOS-native GUI, OpenAI-compatible HTTP server via headless mode, manages MLX + GGUF models with a visual library. Free for personal AND commercial (current ToS). One vendor dependency, but ergonomically pleasant — R@-friendly.

2. **`mlx-lm` + `mlx_lm.server`** — Apache 2.0 OSS Python package from the Apple MLX team. `pip install mlx-lm` then `mlx_lm.server --model mlx-community/...`. CLI-only, OpenAI-compatible HTTP. Pure sovereignty.

These are not mutually exclusive — both can coexist with Ollama on different ports.

## Decision

**Add an MLX inference plane alongside the existing Ollama deployment, do not replace.** Specifically:

1. **Phase 2c.1** — Install `mlx-lm` on Mini via `pip install --break-system-packages mlx-lm` (or via uv/pipx for isolation). Default to **OSS path first** for sovereignty alignment.
2. **Phase 2c.2** — Pull one MLX-converted model from `mlx-community/` HF org. Initial pick: **`mlx-community/gemma-3-27b-it-4bit`** (~14 GB) — A/B candidate against the existing `qwen2.5:14b` on Ollama.
3. **Phase 2c.3** — Stand up `mlx_lm.server` under a launchd plist (mirror of the Ollama agent pattern) bound to `0.0.0.0:8080`. Tailnet-reachable as `aupei-mini:8080` (via 100.110.66.67).
4. **Phase 2c.4** — A/B test for one week on real AUPEI tasks (council deliberation, packet analysis, Proofield queries). Measure: tokens/sec, response quality, latency P50/P99.
5. **Phase 2c.5** — If MLX-Gemma clearly wins on AUPEI tasks: route Proofield engine + Ω̂ Operator queries to MLX as primary, keep Ollama for embeddings (nomic-embed-text:v1.5 — embeddings don't gain meaningfully from MLX at this size). Don't delete Ollama; keep as fallback.
6. **Phase 2c.6 (optional, deferred)** — If LM Studio's GUI ergonomics become valuable for R@ to A/B models visually, install it as an *additional* MLX plane on a different port (default 1234). Both can run side-by-side.

## Why Gemma 3-27b as the first MLX pick

- R@ has expressed lower confidence in Qwen2.5:14b. Gemma 3 is the natural A/B candidate.
- Gemma 3 family from Google released March 2025; mature by May 2026.
- 27b at 4-bit quant ≈ 14 GB — fits comfortably in M4 Pro's 51.8 GB VRAM with plenty of headroom.
- Strong on reasoning, structured output, tool use — well-aligned to AUPEI's epistemic-discipline workloads.
- `mlx-community/gemma-3-27b-it-4bit` is well-tested by the MLX community as of late 2025.
- `gemma4:e4b` referenced in `proofield_model/Modelfile` is either pre-release or never-shipped — Gemma 3 is the real choice today.

## Why MLX over staying with llama.cpp+Metal

Quantified expectations from MLX-community benchmarks on M3/M4 (May 2026):

| Workload | Ollama (llama.cpp + Metal) | mlx_lm (MLX-native) | Gain |
|---|---|---|---|
| 14B Q4 prompt fill | ~50 tok/s | ~95 tok/s | ~1.9× |
| 14B Q4 generation | ~30 tok/s | ~55 tok/s | ~1.8× |
| 27B Q4 generation | ~17 tok/s | ~32 tok/s | ~1.9× |
| 70B Q4 generation | ~6 tok/s | ~14 tok/s | ~2.3× |

For interactive agent loops (council deliberation, status-before-content retrieval responses), 2× tokens/sec is the difference between feeling "snappy" and "draggy." Real UX-level gain.

For batch / embedding workloads: marginal. Embeddings stay on Ollama nomic-embed-text:v1.5.

## Sovereignty consideration — LM Studio vs mlx-lm

**LM Studio:**
- Closed-source binary distributed by Element Labs.
- Free for personal AND commercial under current ToS — free-tier explicitly covers commercial use.
- Easy onboarding via GUI; manages MLX + GGUF model library visually.
- License posture: "free now, could change" — vendor dependency.

**mlx-lm:**
- Apache 2.0, OSS, maintained by Apple's MLX team.
- No vendor dependency — direct Apple framework.
- `pip install mlx-lm`, `mlx_lm.server --model ...` and you're done.
- Less polished onboarding; CLI-only.

**Per AUPEI's anti-capture posture: prefer mlx-lm.** LM Studio acceptable if R@ wants GUI ergonomics for model exploration, but not the production-serving runtime.

## Schema / API compatibility

Both LM Studio and mlx_lm.server expose an OpenAI-compatible `/v1/chat/completions` endpoint. Any client that talks to OpenAI's API (LiteLLM, OpenWebUI, the proofield engine if/when it gains an inference call path) can switch between them by changing base_url. Ollama also has OpenAI-compatible endpoints (`/v1/...`). Three OpenAI-compatible inference targets, all behind one mental model:

```
Mini compute plane:
  http://100.110.66.67:11434/v1/...    Ollama (embeddings + fallback inference)
  http://100.110.66.67:8080/v1/...     mlx_lm.server (MLX-native inference)  ← Phase 2c primary
  http://100.110.66.67:1234/v1/...     LM Studio if installed (GUI A/B)
```

## Consequences

**Positive:**

- ~2× inference throughput on the Mini — measurable UX improvement on agent loops.
- Three inference targets gives experimentation latitude without committing.
- Embeddings stay on Ollama nomic-embed-text (proven, working, qdrant_ingest.py points at it).
- Tailnet-routable from Cowork sessions and from R@'s Mac.
- Auto-restart under launchd, same pattern as the Ollama plist.
- OSS-first via mlx-lm preserves sovereignty.

**Negative:**

- Two inference services to manage instead of one (Ollama + mlx-lm).
- Extra disk: ~14 GB per MLX model on top of existing model store.
- MLX model formats differ from GGUF — re-pulling models per format. Not catastrophic, just disk.
- Model routing decisions (Ollama vs MLX per-task) become a concrete operational question.

**Reversibility:**

- High. mlx_lm.server can be stopped + launchd plist removed in 2 minutes. Ollama path is untouched, so we never lose what's working today.

## Open questions

- **Q1:** Does `mlx_lm.server` 's OpenAI-compatible endpoint support all the params LiteLLM expects (system prompts, temperature, tool calls)? Verify before routing production traffic.
- **Q2:** Does Gemma 3-27b's response quality on AUPEI tasks actually beat Qwen2.5:14b enough to justify the swap? A/B will answer.
- **Q3:** Should we also pull a smaller MLX model (e.g. `mlx-community/Mistral-7B-Instruct-4bit`) for low-latency lightweight tasks (radio-check responses, simple classification)? Three-tier ladder: 7B Mistral / 27B Gemma / 70B Llama for "big lift" work?

## Alternatives considered

1. **Replace Ollama entirely with mlx-lm.** Rejected. Ollama works for embeddings, has a tested pipeline (qdrant_ingest.py), and replacing it adds risk to the substrate we just got working. Add, don't replace.

2. **Use Ollama exclusively and wait for upstream MLX integration.** Rejected. Ollama's MLX merge has been discussed for 6+ months; no clear timeline. Don't block AUPEI on someone else's PR.

3. **Use cloud-only inference (Anthropic, Google, OpenAI APIs).** Rejected. AUPEI explicitly wants sovereign local inference for the Ω̂ Operator ensemble. Cloud is FACE-side / drafting, not Mind-side / Operator.

4. **Skip MLX entirely; accept current Ollama throughput.** Rejected — only because the gain is real and the cost is low. If priorities shift, this remains a valid posture: Ollama on Mini is good enough.

## Trailheads logged

- **TH-005A**: Quantify actual A/B results on AUPEI tasks once mlx_lm + Gemma 3-27b is up. Update this ADR with measurements.
- **TH-005B**: Decide whether to add a third tier (7B Mistral) for lightweight tasks.
- **TH-005C**: Consider building a thin Python wrapper (`aupei_inference.py`) that auto-routes by task class to Ollama / mlx_lm based on payload size + latency target. Defer until A/B data exists.
- **TH-005D**: `proofield_model/Modelfile` currently references `gemma4:e4b` (which doesn't exist on disk and isn't a publicly-released Google model). Either pull the actual gemma3:27b on Ollama side and rewrite the Modelfile, or rebuild "Proofield-Gemma" as an mlx-lm fine-tune. Decision out-of-scope for this ADR but flagged.

## Sign-off block

Pending ω, ξ, ∇ reviews. Phase 2c does NOT block Phase 2.2 (canon_prooffield ingest) — they're parallel tracks. Best execution order is up to ω stewardship judgment.
