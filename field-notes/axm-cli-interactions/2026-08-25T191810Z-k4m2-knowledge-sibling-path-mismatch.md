---
id: 2026-08-25T191810Z-k4m2
subject: axm-cli-interactions
key: knowledge-sibling-path-mismatch
observed_at: "2026-08-25T19:18:10Z"
session: unknown
kind: workaround
status: open
---

**Expected:** The author-agent-skill instructions said the installed agent-engineering sibling was available under `.axm/extensions/@agentxm/`.
**Observed:** Every required file lookup under that path failed with `No such file or directory`; the installed sibling was under `agent_extensions/agentxm/@agentxm/`.
**Impact:** One failed read attempt and one repository search were needed before the required guidance could be opened.
**Recovery:** Located the same named resources under `agent_extensions/agentxm/@agentxm/` and continued the task.
**Detected by:** `wc` failed for each instructed path.
**Observed factors:** AXM CLI help completed successfully; the workspace contains acquired extension material under `agent_extensions/`.
**Diagnostic evidence:** Failed command exit code was `1`; each path reported `open: No such file or directory`.
**Hypothesis:** The skill describes a canonical path convention that differs from this workspace's installed materialization path.

Evidence: The instructed `.axm/extensions/@agentxm/...` paths were absent, while `rg --files` found all requested resources under `agent_extensions/agentxm/@agentxm/...`.
