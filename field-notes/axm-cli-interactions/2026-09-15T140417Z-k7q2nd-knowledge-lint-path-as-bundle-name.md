---
id: 2026-09-15T140417Z-k7q2nd
subject: axm-cli-interactions
key: knowledge-lint-path-as-bundle-name
observed_at: "2026-09-15T14:04:17Z"
session: abec0f7a-f800-472e-b094-4c5478a4fba9
kind: workaround
status: open
---

**Expected:** `axm knowledge lint knowledge/product-engineering` would validate the locally authored bundle at that directory, since the argument was an existing path containing `knowledge.json`.
**Observed:** The command printed `✖ Knowledge bundle "knowledge/product-engineering" is not installed (not_found)`. The positional argument is an installed bundle name; local directories require `--path`. The error did not mention `--path`.
**Impact:** One extra help lookup and rerun before validation; not measured in time.
**Outcome:** `axm knowledge lint --path ./knowledge/product-engineering` reported "Knowledge validation passed for 1 bundle".
**Recovery:** Read `axm knowledge lint --help` and reran with `--path`.
**Detected by:** Human-readable CLI output while validating a documentation change.
**Observed factors:** axm 0.29.4 (update 0.31.1 available); argument contained a slash and resolved to an existing directory; project scope default.
**Diagnostic evidence:** code `not_found`; exit status unavailable — output was piped through `tail`; suggestions: not supplied.
**Hypothesis:** unknown
**Suggests:** When the bundle argument resolves to a local directory, suggest `--path <dir>` in the not_found result.

Evidence: first command and message above; successful rerun with `--path` in the same session.
