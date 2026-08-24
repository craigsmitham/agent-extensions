---
id: 2026-08-24T214918Z-e89d
subject: axm-cli-interactions
key: registry-find-command-absent
observed_at: "2026-08-24T21:49:18Z"
session: sess-38b0b6
kind: workaround
status: open
---

**Expected:** `axm find <FQN> --json` would return published registry metadata; the AXM skill describes registry work using “find/discover” language.
**Observed:** Both parallel `axm find` invocations returned `Unknown subcommand "find" for "axm"` and suggested `lint`. `axm search --help` then displayed the generic command catalog, where the applicable exact-package command is named `view`.
**Impact:** Publication verification was delayed by one command-help lookup after two failed read-only invocations; elapsed time was not measured.
**Recovery:** The generic command catalog identified `axm view`; verification continued with that command.
**Detected by:** Structured CLI error output from the two `axm find` invocations.
**Observed factors:** AXM was invoked from the public agent-extensions workspace for `@craigsmitham/rules/field-notes` and `@craigsmitham/knowledge/field-notes`; both invocations used `--json`.
**Diagnostic evidence:** CLI error code `usage`; process exit status unavailable — output was not retained; request or correlation ID not supplied; attempt count 2; retry stopped after the same error affected both package identities.
**Hypothesis:** The skill’s operation vocabulary does not make the CLI mapping from “find” to `discover` or `view` explicit.
**Suggests:** Name the exact lookup command for a known FQN in AXM-facing guidance.

Evidence: Both package lookups emitted the same `usage` error, and the subsequent command catalog listed `discover` for finding extensions and `view` for published extension metadata.
