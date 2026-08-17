---
id: 2026-08-17T190513Z-5b4b
subject: axm-cli-interactions
key: cli-skill-version-drift
observed_at: "2026-08-17T19:05:13Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm lint --strict --json` would validate the workspace with the installed official AXM skill compatible with the running CLI.
**Observed:** Lint reported `workspace/axm-skill-compatible`: AXM CLI `0.27.8` is outside the installed official AXM skill range `0.27.7`.
**Impact:** Strict workspace validation could not evaluate the retirement change cleanly; one unrelated compatibility error remained.
**Recovery:** Continued with targeted checks and left the AXM installation unchanged because updating it was outside this task.
**Detected by:** `axm lint --strict --json`.
**Observed factors:** The running CLI identified itself as `0.27.8`; `.axm/extensions/@agentxm/skills/axm/SKILL.md` declares `axm.sh/cli-version-range: "0.27.7"`.
**Hypothesis:** The CLI was upgraded without reconciling the bundled AXM skill.

Evidence: The lint result contained one `workspace/axm-skill-compatible` error with the observed CLI and skill versions.
