---
id: 2026-08-27T200541Z-n4k8
subject: axm-cli-interactions
key: create-help-global-fallback
observed_at: "2026-08-27T20:05:41Z"
session: z7c2p1
kind: workaround
status: open
---

**Expected:** `axm create --help` would either describe the extension-creation surface or report that creation is available through a type-scoped command.
**Observed:** AXM 0.28.1 exited 0 and printed the global help surface, with no explicit indication that `create` is not a top-level command.
**Impact:** One additional help lookup was required before the skill-creation workflow could continue.
**Recovery:** Continued with `axm skills --help` to locate the type-scoped creation command; the original task remained able to proceed.
**Detected by:** The returned usage text listed the global command surface rather than creation syntax.
**Observed factors:** The command ran in an AXM project workspace with CLI 0.28.1; `axm lint --json` had reported compatible AXM skill and CLI versions with no findings.
**Diagnostic evidence:** Command: `axm create --help`; process exit status: `0`; primary result: global AXM usage and command list; diagnostic output: none supplied.
**Hypothesis:** Unknown-command help may intentionally fall back to global help without identifying the unmatched token.
**Suggests:** Make an unrecognized top-level command explicit and point to the relevant type-scoped help when a close command family exists.

Evidence: The captured command returned the global help banner and command inventory rather than syntax for creating an extension or an unknown-command diagnostic.
