---
id: 2026-08-26T130651Z-6ed7b3
subject: axm-cli-interactions
key: agentxm-sibling-path-mismatch
observed_at: "2026-08-26T13:06:51Z"
session: 49cfe7f2
kind: workaround
status: open
---

**Expected:** The active `author-agent-skill` and `agent-skill-evaluator`
instructions should resolve their required AgentXM Knowledge and runner
siblings at the documented `.axm/extensions/@agentxm/...` paths after AXM had
reported the packages active.
**Observed:** Every requested `.axm/extensions/@agentxm/...` path was absent.
Earlier `axm knowledge list --json` output resolved the active Agent Engineering
bundle under `agent_extensions/agentxm/@agentxm/knowledge/agent-engineering/`,
and the evaluator runner was likewise present under the source-qualified
`agent_extensions/agentxm/@agentxm/skills/` tree.
**Impact:** Skill-maintenance validation paused for one failed read and one
bounded path search before the applicable guidance could be loaded. Elapsed
cost was not measured.
**Recovery:** Used the canonical source-qualified paths already resolved by AXM
and continued the requested migration.
**Detected by:** `sed` reported `No such file or directory` for all documented
`.axm/extensions/@agentxm/...` sibling paths.
**Observed factors:** AXM CLI version `0.28.1`; project workspace; active
workspace-owned Gen Stack target; acquired AgentXM siblings materialized under
`agent_extensions/agentxm/@agentxm/`.
**Diagnostic evidence:** The failed read's process exit status is unavailable —
output was not retained. The complete diagnostic named each absent path and
reported `No such file or directory`.
**Hypothesis:** The skill instructions assume a user-scope canonical layout and
do not account for the source-qualified project layout reported by current AXM.
**Suggests:** Route sibling loading through AXM-resolved canonical package paths
instead of embedding one scope-specific filesystem layout.

Evidence: `axm knowledge list --json` identified the active Agent Engineering
source root as
`agent_extensions/agentxm/@agentxm/knowledge/agent-engineering/src`; a bounded
repository file search found the required concepts and evaluator runner beneath
that source-qualified root.
