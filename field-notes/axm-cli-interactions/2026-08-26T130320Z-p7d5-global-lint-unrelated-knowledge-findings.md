---
id: 2026-08-26T130320Z-p7d5
subject: axm-cli-interactions
key: global-lint-unrelated-knowledge-findings
observed_at: "2026-08-26T13:03:20Z"
session: unknown
kind: gap
status: open
---

**Expected:** The required post-edit `axm lint --json` check would provide actionable validation of the changed `@craigsmitham/skills/research` package.
**Observed:** The global lint exited 1 with 264 findings from unrelated `knowledge/gen-stack` content; a structured filter found no finding whose path contained `skills/research`.
**Impact:** The global exit status could not serve as a clean pass/fail signal for the Research revision; one additional package-scoped verification path was required.
**Recovery:** Preserved the global failure and continued with explicit Research package inspection and evaluation-source validation; the original task remained in progress.
**Detected by:** Post-edit AXM lint and a follow-up structured result filter.
**Observed factors:** AXM CLI 0.28.1; compatibility status `compatible`; summary: 8 errors, 256 warnings, 0 infos; Research-path findings: 0.
**Diagnostic evidence:** `axm lint --json --quiet` process exit status 1; result `ok: false`; `exitCategory: errors`.
**Hypothesis:** Concurrent or unrelated Knowledge bundle changes made the workspace-wide lint outcome unsuitable as a target-specific signal.
**Suggests:** Provide or document a package-scoped lint surface for bounded extension authoring checks.

Evidence: The structured lint result contained no finding with a path under `skills/research`, while its complete summary attributed 264 findings to the workspace result.
