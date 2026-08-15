---
subject: axm-cli-interactions
key: user-lockfile-v3-unreadable
date: 2026-08-15
kind: blocked
status: open
---

**Expected:** `axm list --deprecated --scope user --json` should inspect the
user-scope inventory or provide a supported migration action for older managed
state.
**Actual:** The command failed validation because the user-scope lockfile has
`lockfileVersion: 3`, while the installed CLI expected version 4.
**Gap:** The read-only inventory command cannot load or guide migration of an
older AXM-managed user scope.
**Suggests:** Detect the prior lockfile version and return a safe, explicit
migration command before rejecting the inventory request.

Evidence: In this workspace on 2026-08-15, AXM 0.27.5 returned
`LockfileDecodeError` with `lockfileVersion: Expected 4`; the first line of
the user-scope `.axm/axm-lock.yaml` was `lockfileVersion: 3`.
