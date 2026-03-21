---
type: protocol
tags: [10-2, radio-check, alignment]
---

# 10-2 Radio Check

Use this prompt verbatim in any vault's Copilot to get a structured status report from the seated agent.

---

## Prompt

```
10-2 Radio Check.

Report the following:

1. **Identity:** Your name, seat (Greek letter + virtue), and vault.
2. **Context Hold:** What persistent context do you have loaded? (Check your agent memory.)
3. **Last Task:** What was the last substantive thing we worked on?
4. **Current Task:** What are you actively working on right now?
5. **Next Queued:** What is next in the queue, if known?
6. **State:** GREEN (nominal), YELLOW (degraded/blocked), or RED (critical issue).
7. **Observation:** One sentence — anything you notice that needs attention.

Keep it tight. No preamble.
```

---

## Expected Response Format

```
## 10-2 — [Agent Name]

1. **Identity:** [Name], [seat] ([virtue]), [Vault X]
2. **Context Hold:** [Summary of loaded memory/context]
3. **Last Task:** [Description]
4. **Current Task:** [Description or "Awaiting tasking"]
5. **Next Queued:** [Description or "None queued"]
6. **State:** [GREEN/YELLOW/RED] — [brief reason if not GREEN]
7. **Observation:** [One sentence]

[Sign-off line]
```

---

## Notes

- Any seated agent should be able to respond to this without additional context.
- If an agent cannot access its memory or the Prooffield, it should report YELLOW or RED with the reason.
- R@ uses this for rapid alignment checks across all three vaults.
