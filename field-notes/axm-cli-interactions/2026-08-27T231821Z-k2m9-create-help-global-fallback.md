---
id: 2026-08-27T231821Z-k2m9
subject: axm-cli-interactions
key: create-help-global-fallback
observed_at: "2026-08-27T23:18:21Z"
session: 01a0456f-03c5-7d32-9d76-798334e72901
kind: workaround
status: open
---

**Expected:** `axm create --help` would describe extension creation or identify the type-scoped command that owns it.
**Observed:** AXM 0.28.1 exited 0 and printed global help without saying that `create` is not a top-level command.
**Impact:** One additional help lookup was required before skill creation could proceed.
**Recovery:** `axm skills --help` exposed the `axm skills new` command; the original work continued.
**Detected by:** The result contained the global command inventory rather than creation syntax.
**Observed factors:** The command ran in a compatible AXM project workspace; `axm lint --json` reported no findings.
**Diagnostic evidence:** Command: `axm create --help`; process exit status: `0`; primary result: global AXM help; diagnostic output: none supplied.
**Hypothesis:** Unknown top-level command help may fall back to global help without identifying the unmatched token.
**Suggests:** Make the unrecognized command explicit and point to the matching type-scoped help surface.

Evidence: `axm create --help` returned global usage, while the subsequent `axm skills --help` identified `axm skills new` as the creation route.
