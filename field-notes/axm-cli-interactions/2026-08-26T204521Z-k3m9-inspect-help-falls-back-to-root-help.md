---
id: 2026-08-26T204521Z-k3m9
subject: axm-cli-interactions
key: inspect-help-falls-back-to-root-help
observed_at: "2026-08-26T20:45:21Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm inspect --help` would describe an inspection command that could resolve canonical package identity after the AXM skill directed package authors to resolve the target through AXM.
**Observed:** The command exited successfully and printed the generic AXM root help instead of inspection-specific help; no diagnostic identified `inspect` as unsupported.
**Impact:** Package-resolution work required another discovery step; elapsed cost was not measured.
**Recovery:** Progress continued using the documented project-authored roots and the type-specific `axm help knowledge` guidance; the original task remained in progress.
**Detected by:** The output contained the root `USAGE` and command catalog rather than an `inspect` command synopsis.
**Observed factors:** AXM CLI version `0.28.1`; command `axm inspect --help`; process exit status `0`; workspace lint was clean and skill compatibility was `compatible`.
**Diagnostic evidence:** Exit status `0`; no error code, recovery field, or unsupported-command diagnostic was supplied.
**Hypothesis:** The CLI may route an unknown command with `--help` to root help without signaling that fallback.
**Suggests:** Return a typed unknown-command result or visibly label the fallback when command-specific help is unavailable.

Evidence: The retained command result shows `axm inspect --help` produced generic root help headed by `USAGE axm <command> [flags]` and exited `0` under AXM `0.28.1`.
