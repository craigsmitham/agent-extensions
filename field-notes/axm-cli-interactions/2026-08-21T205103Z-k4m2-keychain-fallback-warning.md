---
id: 2026-08-21T205103Z-k4m2
subject: axm-cli-interactions
key: keychain-fallback-warning
observed_at: "2026-08-21T20:51:03Z"
session: unknown
kind: gap
status: open
---

**Expected:** `axm list --json` would return installed-extension state without an environment warning during a read-only workspace inspection.
**Observed:** AXM emitted `OS keychain unavailable; using restricted credential file.` before returning a successful result.
**Impact:** The result remained usable, but the warning added an unexpected diagnostic that required distinguishing a benign fallback from a task-affecting failure; elapsed cost was not measured.
**Recovery:** No recovery was required; the command completed successfully and the documentation task continued.
**Detected by:** The NDJSON diagnostics emitted by `axm list --json`.
**Observed factors:** The command ran in the project workspace through a non-interactive Codex shell; AXM returned `ok: true` and 48 extension entries.
**Hypothesis:** unknown

Evidence: `axm list --json` emitted the warning and then a successful result document in the same invocation.
