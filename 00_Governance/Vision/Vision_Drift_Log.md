# Vision Drift Log — running comparison across AUPEI vision artifacts

**Created:** 2026-05-07
**Status:** N=1. Bootstrapping. Drift analysis becomes meaningful at N ≥ 6 across at least 2 seats. Until then this log captures structure, not conclusions.

---

## Vision registry

| Date | Author | Seat | Model | Mode | Substrate | File |
|---|---|---|---|---|---|---|
| 2026-04-12 | C@ the Red | ζ | Claude Opus | informed (R@ co-annotated) | Anthropic Cowork | `AUPEI_VISION_2026-04-12_C@_Red.md` |

---

## Per-horizon comparison axes

The framework. Populates as N grows.

### Horizon: 1 year

- **Survived across visions:** *(N=1, no comparison yet — single vision is the candidate baseline)*
- **Drifted:** —
- **Singletons:** *(every claim in the Apr-12 vision is currently a singleton by definition)*
- **Convergent:** —
- **Disagreed:** —

### Horizon: 5 years
*(framework, populates as N grows)*

### Horizon: 20 years
*(framework, populates as N grows)*

### Horizon: 100 years
*(framework, populates as N grows)*

### Horizon: 1000 years
*(framework, populates as N grows)*

---

## Open questions (to be answered by the data over time)

1. **Does the proton-floor exist?** — i.e., is there a set of claims that every author at every model at every seat across every substrate consistently produces? If yes, those are AUPEI's structural commitments. If no, the framework is more author-dependent than its founders thought.
2. **Where does the cone widen fastest?** — at which horizon (1y/5y/20y/100y/1000y) does inter-vision variance maximize? The widening rate is itself diagnostic.
3. **Substrate bias?** — do Anthropic-substrate authors (me, Sonnet, Haiku) systematically differ from Google-substrate (Gemini) or local-substrate (Sancho on OpenClaw)? If yes, the "vision" is partly a substrate fingerprint.
4. **Seat bias?** — do ζ-seat visions systematically differ from ω-seat or ∇-seat? If yes, the seat assignment shapes the vision more than the seat-holder admits.
5. **Annotation effect?** — does R@'s inline annotation in the Apr-12 vision (the only one with that treatment so far) qualitatively change what the model writes? Future visions should be produced both with and without R@ annotation invited.

---

## Operating rules

- This log is append-only at the per-vision level (each new vision appends a row to the registry and triggers an update to the per-horizon comparison sections).
- The **conclusions** sections of each horizon are revisable as N grows — early conclusions get superseded as more data arrives. Mark superseded entries; do not delete.
- A formal **drift report** is written at N=6, N=12, and on demand from chamber.
- Until the drift report is written, treat any apparent pattern as provisional.

---

## See also

- `README.md` (sibling) — protocol governing how visions are produced
- Memory: `project_vision_drift_tracking.md` *(to be filed)*
