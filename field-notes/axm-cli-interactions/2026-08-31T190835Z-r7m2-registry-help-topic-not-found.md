---
id: 2026-08-31T190835Z-r7m2
subject: axm-cli-interactions
key: registry-help-topic-not-found
observed_at: "2026-08-31T19:08:35Z"
session: q8v4n2
kind: workaround
status: open
---

**Expected:** AXM help would expose a registry topic that identified the command for reading published extension metadata.
**Observed:** `axm help registry` failed because `registry` is not a help topic and directed the caller to `axm help`.
**Impact:** One unsuccessful read-only help lookup and two additional discovery steps were required before the registry read command was found; elapsed cost was not measured.
**Recovery:** `axm help` exposed the command catalog, and `axm view --help` identified the published-metadata command. The task completed.
**Detected by:** The retained command result and nonzero process status.
**Observed factors:** AXM CLI version 0.28.2; project workspace; read-only registry discovery.
**Diagnostic evidence:** Exit status 3; classification `not_found`; message `Unknown help topic or command path 'registry'.`; recovery guidance `axm help`.
**Hypothesis:** The CLI organizes registry reads under the `view` command without a registry help topic.

Evidence: The original failure result retained its exit status, stable classification, message, and recovery guidance; `axm view --help` subsequently returned exit status 0.
