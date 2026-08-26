---
id: 2026-08-26T140523Z-k3m7
subject: axm-cli-interactions
key: evaluator-workspace-discovery
observed_at: "2026-08-26T14:05:23Z"
session: 01a03e53
kind: workaround
status: open
---

**Expected:** Running the repository-mandated `agent-skill-eval.mjs validate`
command without `--package` from the active AXM workspace would discover and
validate every workspace-authored Agent Skill, as stated by the runner
documentation.

**Observed:** The command returned exit code `2`, an empty `packages` array,
and the finding `No workspace-authored Agent Skill packages were discovered;
pass --package explicitly.`

**Impact:** Workspace-wide evaluation-source validation did not run. This work
required one explicit validation command per changed skill package.

**Recovery:** Validate `skills/author-docs`, `skills/author-okf`, and
`skills/audit-docs` separately with `--package`; task completion remained
possible.

**Detected by:** Complete structured JSON output and process exit status from
the repository-mandated validator command.

**Observed factors:** AXM CLI `0.28.1`; evaluator package
`@agentxm/skills/agent-skill-evaluator@0.2.2` installed and enabled; command ran
from the project workspace root; `axm lint --json` had returned a clean,
compatible workspace result.

**Diagnostic evidence:** Exit code `2`; result `ok: false`; `packages: []`;
one discovery finding; no evaluation run workspace was created.

**Hypothesis:** unknown

Evidence: The runner documentation says package omission validates every
workspace-authored Agent Skill, while the observed command discovered none in
a workspace where `axm list --json` reported the changed workspace-authored
skills installed and enabled.
