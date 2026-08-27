---
id: 2026-08-27T223558Z-v8r3
subject: axm-cli-interactions
key: evaluator-workspace-discovery
observed_at: "2026-08-27T22:35:58Z"
session: s-v8r3
kind: workaround
status: open
---

**Expected:** The repository-required workspace-wide `agent-skill-eval.mjs
validate --json` invocation should discover workspace-authored Agent Skill
packages.
**Observed:** The validator exited with code 2, returned `ok: false`, discovered
no packages, and required `--package` explicitly.
**Impact:** Validation could not proceed as one workspace-wide operation and
required separate explicit invocations for each affected package.
**Recovery:** Run validation once per affected canonical skill package with an
explicit `--package skills/<name>` argument.
**Detected by:** The validator's structured result and process exit status.
**Observed factors:** Node.js 24.13.1; project AXM lint was clean immediately
after the failure; canonical affected packages are under `skills/`.
**Diagnostic evidence:** Result fields: `ok: false`, `packages: []`; finding:
`No workspace-authored Agent Skill packages were discovered; pass --package
explicitly.`; exit status `2`.
**Hypothesis:** unknown

Evidence: The documented command was run from the repository root and returned
the structured failure above before any behavioral trial or generated run was
created.
