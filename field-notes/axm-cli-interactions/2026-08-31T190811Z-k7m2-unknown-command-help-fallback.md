---
id: 2026-08-31T190811Z-k7m2
subject: axm-cli-interactions
key: unknown-command-help-fallback
observed_at: "2026-08-31T19:08:11Z"
session: unknown
kind: gap
status: open
---

**Expected:** Requesting help for guessed AXM command names that do not exist would return a distinct unknown-command result and a nonzero exit status.
**Observed:** `axm inspect --help`, `axm find --help`, and `axm remove --help` each printed the generic top-level help surface; the combined command returned exit status 0.
**Impact:** The command discovery step produced three repeated generic help blocks and did not distinguish invalid command names; progress continued by using the command list in top-level help. Direct cost was one command invocation with noisy output.
**Recovery:** Used the top-level command list to identify `view`, `discover`, and `uninstall`; the original migration work continued.
**Detected by:** Comparing the requested command-specific help surfaces with the repeated top-level help output.
**Observed factors:** AXM CLI version 0.28.2; commands were invoked with `--help` from a configured project workspace.
**Diagnostic evidence:** Process exit status: 0. Result output: generic top-level AXM help was emitted for each unsupported command. Separate diagnostic output: none supplied.
**Hypothesis:** Unknown command names combined with `--help` fall through to the root help handler without an error classification.
**Suggests:** Distinguish an unknown command from an explicit top-level help request in both human and machine-readable output.

Evidence: The requested command surfaces were `inspect`, `find`, and `remove`; none appeared in the top-level command list, and all three returned the same root help text within one successful invocation.
