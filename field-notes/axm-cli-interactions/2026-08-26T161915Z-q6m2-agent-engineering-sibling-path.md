---
id: 2026-08-26T161915Z-q6m2
subject: axm-cli-interactions
key: agent-engineering-sibling-path
observed_at: "2026-08-26T16:19:15Z"
session: unknown
kind: gap
status: open
---

**Expected:** After AXM resolved the active project scope, the Agent Skill
authoring guidance directed required sibling reads through
`.axm/extensions/@agentxm/`.
**Observed:** The directed `.axm/extensions/@agentxm/` paths were absent in the
project workspace; AXM reported a compatible `0.28.1` workspace with no lint
findings, while the installed sibling packages are present under
`agent_extensions/agentxm/@agentxm/`.
**Impact:** Required authoring-reference discovery needed an additional bounded
path check before semantic work could continue.
**Recovery:** Use the project canonical installed-package root reported by the
workspace layout, `agent_extensions/agentxm/@agentxm/`, for the required
read-only sibling references; the original task remains in progress.
**Detected by:** `test -f` and `rg --files` returned no
`.axm/extensions/@agentxm/knowledge/agent-engineering/src` path after successful
AXM preflight.
**Observed factors:** `axm --version` returned `0.28.1`; `axm lint --json`
reported `ok: true`, compatible AXM skill and CLI versions, zero findings, and
exit category `clean`.
**Hypothesis:** Project-installed sibling packages use a canonical repository
root different from the fixed path stated by the authoring guidance.

Evidence: The absent directed path and the successful AXM compatibility and
lint results were observed in the same project workspace before any semantic
edit.
