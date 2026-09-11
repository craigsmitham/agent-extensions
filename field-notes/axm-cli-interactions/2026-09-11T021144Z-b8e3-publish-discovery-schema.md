---
id: 2026-09-11T021144Z-b8e3
subject: axm-cli-interactions
key: publish-discovery-schema
observed_at: "2026-09-11T02:11:44Z"
session: devops-fallback-a7f2
kind: blocked
status: open
---

**Expected:** Exact-package publication preview produces a reviewable archive candidate.
**Observed:** `axm publish @craigsmitham/skills/devops-docs --preview --json` fails during candidate selection with "Remote discovery response does not match expected schema".
**Impact:** Preview provides no archive; publication cannot proceed. One preview failed.
**Recovery:** Unresolved at capture; checking the installed CLI release status.
**Detected by:** Release preflight.
**Observed factors:** AXM 0.28.12; agentxm registry; one authored skill selected, local version 0.4.1.
**Diagnostic evidence:** Process exit=10; ok=false; publicationSet.status=unavailable; execution.status=not-run; action=error; phase=selection; reason=candidate_invalid; cause.code=internal; class=internal; retryable=false; attemptCount=1; maxAttempts=3; attemptsExhausted=false; responseStatus=500. Request ID and recovery command not supplied.
**Hypothesis:** unknown
