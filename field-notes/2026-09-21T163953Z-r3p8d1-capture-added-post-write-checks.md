---
observed_at: "2026-09-21T16:39:53Z"
session: "session-k4m8v2"
area: "field-notes skill execution"
---

# Capture added post-write verification

## Context
An isolated authoring smoke trial exercised a straightforward field-note write
with diagnostics and enrichment explicitly prohibited.

## Friction
After writing the note, the agent reread it with `sed` and ran `git status` for
the note path. Neither call contributed information to the occurrence, and the
Git check failed because the disposable workspace was not a Git repository.

## Cost / impact
Two unnecessary tool calls were made after capture, and the representative
smoke case failed.

## Outcome
The skill was tightened to state that the write completes capture and to forbid
rereading, verifying, or checking repository status for the note.

## Evidence
Run `2026-09-21T16-38-27-323Z-286422fb` reported the `sed` and `git status`
calls as the sole critical-failure evidence.
