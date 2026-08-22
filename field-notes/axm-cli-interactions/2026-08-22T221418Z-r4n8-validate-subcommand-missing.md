---
id: 2026-08-22T221418Z-r4n8
subject: axm-cli-interactions
key: validate-subcommand-missing
observed_at: "2026-08-22T22:14:18Z"
session: a8f3c1
kind: workaround
status: open
---

**Expected:** AXM would expose a `validate` subcommand for a workspace extension after the evaluator-specific source validation completed.
**Observed:** `axm validate @craigsmitham/skills/setup-architecture-docs --json` returned a usage error stating that `validate` is an unknown subcommand.
**Impact:** One read-only validation attempt produced unusable output and required using the documented AXM inspection or lint surface; elapsed delay was not measured.
**Recovery:** Retain the successful evaluator validation and use only commands listed by current AXM help for remaining package checks; remediation continued.
**Detected by:** The AXM CLI error envelope and nonzero exit status.
**Observed factors:** AXM CLI 0.27.15; project scope; the Agent Skill evaluator validation had already passed; the command was a guessed convenience surface rather than one shown by current help.
**Hypothesis:** AXM separates extension inspection and linting from the evaluator's versioned-suite validation.

Evidence: AXM returned code `usage` with detail `Unknown subcommand "validate" for "axm"`.
