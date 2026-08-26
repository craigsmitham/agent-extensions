---
id: 2026-08-26T201437Z-v7c1
subject: axm-cli-interactions
key: help-topics-fall-back-to-root
observed_at: "2026-08-26T20:14:37Z"
session: 01a03fac-c065-7e42-823f-754f600dfd49
kind: workaround
status: open
---

**Expected:** The installed AXM skill directs callers to type- or operation-
specific live help, so `axm help skill` or `axm help inspect` should identify
the relevant surface or its replacement.
**Observed:** Both help topics exited 3 with `not_found`; `axm inspect --help`
instead exited 0 but displayed root help because `inspect` is not a command.
**Impact:** Canonical skill-source resolution required two failed help lookups
and a misleading successful fallback before using the plural `skills` surface.
**Recovery:** Continue with the root-advertised `axm help skills` and
`axm skills --help` commands; task not yet complete.
**Detected by:** Complete exit status and output from the three bounded help
commands.
**Observed factors:** AXM CLI version 0.28.1; workspace lint was clean and
compatible. No mutation was attempted.
**Diagnostic evidence:** `axm help skill` and `axm help inspect` each exited 3
with reason `not_found`; `axm inspect --help` exited 0 and returned root usage.
**Hypothesis:** Help lookup does not normalize singular type names or reject an
unknown command before the global `--help` handler displays root help.

Evidence: The recorded commands and exit statuses show the lookup and fallback
behavior in this session.
