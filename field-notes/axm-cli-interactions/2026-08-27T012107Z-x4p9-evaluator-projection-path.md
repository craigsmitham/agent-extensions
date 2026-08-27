---
id: 2026-08-27T012107Z-x4p9
subject: axm-cli-interactions
key: evaluator-projection-path
observed_at: "2026-08-27T01:21:07Z"
session: sess-k7m2
kind: workaround
status: open
---

**Expected:** The enabled evaluator's runner-selection reference said its runner
guide was available at
`.axm/extensions/@agentxm/skills/agent-skill-evaluator/src/references/runner.md`.
**Observed:** Reading that path failed because it was absent; the same guide was
present at the workspace's canonical AgentXM package path.
**Impact:** Verification required one failed read and one repository file
search before the authoring smoke workflow could continue.
**Recovery:** Read
`agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator/src/references/runner.md`;
the original task continued.
**Detected by:** `sed` failed while following the selected runner instructions.
**Observed factors:** AXM reported
`@agentxm/skills/agent-skill-evaluator` installed and enabled at version
`0.2.2`; the repository contains the canonical AgentXM package source but not
the documented `.axm/extensions` projection.
**Diagnostic evidence:** Read command exit status `1`; diagnostic was “No such
file or directory.”
**Hypothesis:** This workspace exposes the implicit package through its
canonical source without materializing the documented projection path.
**Suggests:** Let runner selection resolve and report the usable canonical or
projected reference path for the active AXM workspace layout.

Evidence: AXM `list --json` reported the evaluator installed and enabled; an
`rg --files` lookup found the runner guide only under the canonical AgentXM
package source.
