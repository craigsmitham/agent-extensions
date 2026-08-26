---
id: 2026-08-26T150518Z-j4n8
subject: axm-cli-interactions
key: agent-engineering-sibling-path
observed_at: "2026-08-26T15:05:18Z"
session: codex-v8m2
kind: workaround
status: open
---

**Expected:** The `author-agent-skill` workflow said its coupled Agent Engineering knowledge sibling would be available from the active AXM scope root at `.axm/extensions/@agentxm/knowledge/agent-engineering/src/`.
**Observed:** Reading the required revision guidance at that path failed because the path did not exist; the same files were present under `agent_extensions/agentxm/@agentxm/knowledge/agent-engineering/src/`.
**Impact:** Skill-authoring preflight required one failed read and one bounded repository search before the required guidance could be loaded; elapsed impact was not measured.
**Recovery:** Used the project-canonical acquired-package path reported by the workspace layout; the original documentation cleanup remained in progress.
**Detected by:** `sed` failed while loading the required Agent Engineering revision guidance.
**Observed factors:** AXM CLI version 0.28.1; project workspace; `axm lint --json` had reported no findings; canonical acquired packages were stored under `agent_extensions/agentxm/`.
**Diagnostic evidence:** The read command exited 2 with `sed: .axm/extensions/@agentxm/knowledge/agent-engineering/src/skills/maintenance-and-evolution.md: No such file or directory`.
**Hypothesis:** The authoring workflow documents a user-scope sibling path but does not account for AXM's project-scope source-qualified canonical path.

Evidence: The exact expected and recovered paths, AXM version, lint state, exit status, and diagnostic are preserved above.
