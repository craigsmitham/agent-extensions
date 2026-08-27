---
id: 2026-08-27T233106Z-r6t4
subject: axm-cli-interactions
key: evaluator-workspace-discovery
observed_at: "2026-08-27T23:31:06Z"
session: s-r6t4
kind: workaround
status: open
---

**Expected:** The repository-required workspace-wide
`agent-skill-eval.mjs validate` invocation would discover workspace-authored
Agent Skill packages.
**Observed:** The validator exited with code 2, discovered no packages, and
required `--package` explicitly.
**Impact:** Validation required separate explicit invocations for each affected
canonical skill package.
**Recovery:** Run validation once per affected package with
`--package skills/<name>`.
**Detected by:** The validator's result and process exit status.
**Observed factors:** Node.js 22.23.1; AXM 0.28.1; the command ran from the
project workspace root.
**Diagnostic evidence:** Finding: `No workspace-authored Agent Skill packages
were discovered; pass --package explicitly.`; exit status `2`.
**Hypothesis:** unknown

Evidence: Explicit validation of `skills/sync-change`, `skills/gen-stack`, and
`skills/plan` subsequently discovered and validated each package.
