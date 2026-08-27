---
id: 2026-08-27T012602Z-m5v1
subject: axm-cli-interactions
key: local-package-lint-workspace
observed_at: "2026-08-27T01:26:02Z"
session: sess-k7m2
kind: workaround
status: open
---

**Expected:** `axm knowledge lint --path <absolute-package>` would validate the
local package independently of the process working directory, allowing the Gen
Stack check to run from an ordinary adopting repository.
**Observed:** The same synthetic package passed when the process inherited an
AXM workspace but AXM returned an execution failure when the CLI was invoked
from a synthetic Git repository without `axm.json`.
**Impact:** The initial composite-check implementation was not portable to an
ordinary hook or CI working directory.
**Recovery:** Created a minimal isolated AXM workspace containing `axm.json`
and the synthetic Knowledge package, then ran the local-package lint with that
workspace as its current directory. The same outside-workspace check passed.
**Detected by:** An integration invocation changed only the subprocess working
directory and changed the composite check from exit `0` to exit `2`.
**Observed factors:** AXM `0.28.1`; absolute `--path`; synthetic public OKF v0.2
package; original caller repository had no `axm.json`.
**Diagnostic evidence:** Composite check rule `okf-validator-failure`, exit
`2`; after isolated workspace recovery, OKF result `pass` and process exit `0`.
**Hypothesis:** Local authored-package lint still requires an AXM workspace
context even when `--path` is absolute.
**Suggests:** Document the workspace precondition for `--path` or allow local
package validation without unrelated workspace state.

Evidence: The package bytes and adopting repository were unchanged between the
two invocations; only AXM workspace context differed.
