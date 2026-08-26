---
id: 2026-08-26T201414Z-q2m8
subject: axm-cli-interactions
key: agent-engineering-direct-sibling-missing
observed_at: "2026-08-26T20:14:14Z"
session: 01a03fac-c065-7e42-823f-754f600dfd49
kind: gap
status: open
---

**Expected:** The installed `author-agent-skill` instructions require revision
guidance under the direct
`.axm/extensions/@agentxm/knowledge/agent-engineering/src/` sibling at the
active AXM scope root.
**Observed:** `rg` reported that the required `.axm/extensions` knowledge and
evaluation sibling paths do not exist in this project workspace.
**Impact:** Agent Skill authoring is delayed until canonical AXM state resolves
whether an eligible direct sibling is available; the knowledge-bundle portion
of the task can continue independently.
**Recovery:** Pending AXM canonical-state inspection; task not yet complete.
**Detected by:** A bounded `rg --files` lookup for the exact required guidance
and runner-selection paths.
**Observed factors:** AXM CLI version 0.28.1 and workspace lint compatibility
were clean immediately before the lookup. The missing-path lookup was read-only.
**Diagnostic evidence:** `rg` exited 2 and reported both direct `.axm/extensions`
paths as absent.
**Hypothesis:** The project may retain the packages in a canonical acquired
extension location that is not projected to the direct sibling paths required
by the authoring instructions.

Evidence: The exact required direct paths were absent during this session;
canonical package resolution had not yet been inspected.
