---
id: 2026-08-26T200422Z-r4k7
subject: axm-cli-interactions
key: inspect-help-falls-back-to-root-help
observed_at: "2026-08-26T20:04:22Z"
session: s-r4k7
kind: gap
status: open
---

**Expected:** `axm inspect --help` would either describe an inspection command or report that the command does not exist while resolving canonical package ownership.
**Observed:** AXM 0.28.1 exited successfully and displayed the generic root help without identifying `inspect` as unsupported.
**Impact:** Package-state discovery required one additional command, `axm list --json`; no task output was blocked.
**Recovery:** Used the structured workspace inventory from `axm list --json` and continued.
**Detected by:** The returned usage contained only root commands and no `inspect` command details.
**Observed factors:** Project workspace was valid, `axm lint --json` was clean, and the CLI/skill compatibility status was compatible.
**Diagnostic evidence:** Command `axm inspect --help`; exit status `0`; CLI version `0.28.1`; output surface was generic root help.
**Hypothesis:** Unknown subcommands followed by `--help` may currently fall through to root help.

Evidence: The successful exit and generic command listing were observed directly before the structured inventory recovery command.
