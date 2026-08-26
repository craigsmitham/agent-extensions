---
id: 2026-08-26T130055Z-k4m2
subject: axm-cli-interactions
key: authoring-knowledge-scope-path
observed_at: "2026-08-26T13:00:55Z"
session: unknown
kind: workaround
status: open
---

**Expected:** The installed `author-agent-skill` instructions said the active AXM scope would expose the required agent-engineering sibling under `.axm/extensions/@agentxm/knowledge/agent-engineering/src/`.
**Observed:** In this project workspace, reads from that path failed with exit status 1 and `No such file or directory`; `axm help skills` identified project acquired packages under `agent_extensions/`, where the required sibling was present.
**Impact:** The authoring workflow required one additional scope-resolution step before its required guidance could be read; elapsed impact was not measured.
**Recovery:** Continued with the AXM-documented project canonical path `agent_extensions/agentxm/@agentxm/knowledge/agent-engineering/src/`; the original task remained in progress.
**Detected by:** Required guidance reads failed after a clean `axm lint --json` preflight.
**Observed factors:** AXM CLI 0.28.1; project workspace; `axm lint --json` reported compatible skill and CLI versions with no findings.
**Diagnostic evidence:** Guidance read command exit status 1; diagnostic output was `open: No such file or directory` for each requested `.axm/extensions/...` file.
**Hypothesis:** The authoring instruction names a user-scope canonical layout without accounting for the project-scope acquired-package layout documented by AXM.
**Suggests:** Resolve the active canonical sibling path through AXM state before prescribing a fixed `.axm/extensions/` prefix.

Evidence: `axm help skills` states that project acquired skills use `./agent_extensions/...`, and the required agent-engineering files were directly present under that project path.
