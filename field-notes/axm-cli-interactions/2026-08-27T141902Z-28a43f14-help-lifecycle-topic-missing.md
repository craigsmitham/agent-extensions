---
id: 2026-08-27T141902Z-28a43f14
subject: axm-cli-interactions
key: help-lifecycle-topic-missing
observed_at: "2026-08-27T14:19:02Z"
session: 28a43f14
kind: gap
status: open
---

**Expected:** `axm help lifecycle` should orient a read-only assessment of extension lifecycle state because AXM owns extension lifecycle operations.
**Observed:** AXM returned `Unknown help topic or command path 'lifecycle'. (not_found)` and directed the user to `axm help`; lifecycle operations instead appear as separate top-level commands.
**Impact:** The assessment required one failed help lookup and one additional help lookup before reaching the relevant `deprecate` and `list` command help.
**Recovery:** `axm --help`, `axm deprecate --help`, and `axm list --help` restored progress; the original assessment continued.
**Detected by:** Direct CLI invocation during lifecycle discovery.
**Observed factors:** AXM CLI version `0.28.1`; project workspace lint was clean and skill compatibility was reported as compatible.
**Diagnostic evidence:** Command: `axm help lifecycle`; process exit status: `1`; error class: `not_found`; recovery command supplied by AXM: `axm help`.
**Hypothesis:** Lifecycle commands are discoverable individually but lack a grouped conceptual help topic.

Evidence: On AXM `0.28.1`, the lifecycle-oriented help path failed while top-level help listed `yank`, `unyank`, `deprecate`, and `undeprecate` as independent commands.
