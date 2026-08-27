---
id: 2026-08-26T232655Z-b7n3
subject: axm-cli-interactions
key: inspect-find-help-fallback
observed_at: "2026-08-26T23:26:55Z"
session: w3p9
kind: gap
status: open
---

**Expected:** Asking for help on unavailable `inspect` and `find` commands would identify them as unavailable and direct Registry metadata reads to the supported command.
**Observed:** Both `axm inspect --help` and `axm find --help` exited successfully and printed generic root help; the command list revealed `view` as the Registry metadata surface.
**Impact:** Exact-version readback required one additional help lookup; elapsed delay was not measured.
**Recovery:** Use `axm view --help` and the supported exact-version selectors.
**Detected by:** Command output differed from the requested help subjects.
**Observed factors:** AXM CLI 0.28.1; project workspace; both unavailable command names were passed with `--help`.
**Diagnostic evidence:** Combined command exit status `0`; both outputs showed root `USAGE axm <command> [flags]`; no unknown-command error or suggestion was emitted; `view` appeared under the `EXTENSIONS` command list.
**Hypothesis:** Unknown help subjects fall back to root help without surfacing that fallback.

Evidence: Two distinct unavailable command names produced the same successful root-help output instead of subject-specific help or an error.
