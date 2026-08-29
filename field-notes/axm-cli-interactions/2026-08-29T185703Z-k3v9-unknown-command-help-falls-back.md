---
id: 2026-08-29T185703Z-k3v9
subject: axm-cli-interactions
key: unknown-command-help-falls-back
observed_at: "2026-08-29T18:57:03Z"
session: c4m7p2
kind: workaround
status: open
---

**Expected:** Asking for help on an unavailable AXM command would identify the command as unavailable, allowing the published-metadata readback command to be selected directly.
**Observed:** Both `axm find --help` and `axm info --help` printed generic top-level AXM help without an unknown-command diagnostic. The top-level command list identified `axm view` as the published-metadata command.
**Impact:** Two unsuccessful help lookups were required before the exact registry readback surface was found; elapsed cost was not measured.
**Recovery:** `axm view --help` returned the expected command-specific help with exit status 0, and planning continued.
**Detected by:** The returned help lacked the requested command name and matched the top-level command catalog.
**Observed factors:** AXM CLI version 0.28.2; both unavailable help requests were made in one parallel read-only tool call.
**Diagnostic evidence:** Exit statuses for the two unavailable-command requests are unavailable because the wrapper output did not retain them; both outputs began with the generic AXM banner and command catalog. Recovery command exit status: 0.
**Hypothesis:** The CLI routes unknown commands with `--help` to top-level help without a distinct diagnostic.

Evidence: The generic output listed `view` as “View published extension metadata”; `axm view --help` then returned usage `axm view [flags] <extension> [<field>]`.
