---
id: 2026-08-27T233343Z-t5q8
subject: axm-cli-interactions
key: keychain-fallback
observed_at: "2026-08-27T23:33:43Z"
session: s-t5q8
kind: gap
status: open
---

**Expected:** Read-only AXM inventory and publish-preview preflight would use
available local state without credential-store diagnostics.
**Observed:** `axm list --json` and publish previews completed but warned that
the OS keychain was unavailable and a restricted credential file was used.
**Impact:** Results remained usable; the structured stream carried unrelated
credential noise and no retry was needed.
**Recovery:** Accept AXM's restricted-file fallback and use the successful final
result.
**Detected by:** Warning events in the structured command stream.
**Observed factors:** AXM 0.28.1; project workspace; read-only inventory and
preview operations; successful result states.
**Diagnostic evidence:** Warning: `OS keychain unavailable; using restricted
credential file.`
**Hypothesis:** unknown

Evidence: Extension inventory and archive preflight completed despite the
warning; no credential value or private content was exposed.
