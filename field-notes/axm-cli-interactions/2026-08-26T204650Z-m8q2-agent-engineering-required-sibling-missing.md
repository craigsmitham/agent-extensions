---
id: 2026-08-26T204650Z-m8q2
subject: axm-cli-interactions
key: agent-engineering-required-sibling-missing
observed_at: "2026-08-26T20:46:50Z"
session: unknown
kind: blocked
status: open
---

**Expected:** The `author-agent-skill` workflow's required Agent Engineering knowledge sibling and runner-selection reference would be available at their declared direct `.axm/extensions/@agentxm/...` paths in this clean, compatible AXM workspace.
**Observed:** Every required direct sibling path tested for skill revision was absent, including `.axm/extensions/@agentxm/knowledge/agent-engineering/src/skills/maintenance-and-evolution.md` and `.axm/extensions/@agentxm/skills/evaluate-agent-skill/src/references/runner-selection.md`.
**Impact:** The Gen Stack skill and evaluation-source portion of the requested implementation could not be authored under its governing workflow; knowledge-guide work could continue. Elapsed cost was not measured.
**Recovery:** None for skill authoring in this session; the workflow was narrowed only at the blocked skill-authoring boundary while the independent knowledge-bundle change continued.
**Detected by:** Exact file-presence checks required by `author-agent-skill` returned `MISSING` for all applicable sibling resources.
**Observed factors:** AXM CLI version `0.28.1`; workspace lint clean; AXM skill compatibility `compatible`; required paths were checked exactly without filesystem discovery or substitution.
**Diagnostic evidence:** Eight exact required sibling files reported `MISSING`; no recovery field was supplied by the file-presence check.
**Hypothesis:** The active workspace has not projected the required authoring and evaluator siblings into the paths mandated by `author-agent-skill`.

Evidence: The retained check output lists each required `.axm/extensions/@agentxm/...` file as `MISSING` after a clean `axm lint --json` result.
