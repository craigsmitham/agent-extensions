---
id: 2026-09-11T020734Z-17e1
subject: axm-cli-interactions
key: publish-preview-incompatible-server-response
observed_at: "2026-09-11T02:07:34.877708+00:00"
session: release-docs-0131
kind: workaround
status: open
---

**Expected:** The committed-source publication preview admits the same docs skill archive as the successful pre-commit preview.
**Observed:** AXM reported an incompatible authoritative publish preview with HTTP 500 and stopped before upload.
**Impact:** Final preflight failed once, requiring a public metadata read and another read-only preview. Delay not measured.
**Recovery:** Registry latest read returned 0.3.0; the subsequent exact-selection preview admitted 0.4.0 with identical archive integrity and no risk conditions. Upload had not been attempted at capture time.
**Detected by:** Complete structured preview result and process exit status.
**Observed factors:** AXM 0.28.12; @craigsmitham/skills/devops-docs@0.4.0; committed source matches HEAD 5dccf1056dac7cc8d870d6864b8f918bcbddc2a2. Earlier uncommitted preview succeeded.
**Diagnostic evidence:** Preview exit 10, ok false, publicationSet.status blocked, finding reason authoritative_preflight_failed, execution.status not-run, outcome reason blocked_by_preflight. Failure code/class internal, responseStatus 500, retryable false, attemptCount 1, maxAttempts 3, attemptsExhausted false. Request/correlation ID not supplied. Recovery preview exit 0, ok true, admitted, blocked 0, failed 0, pending 1.
**Hypothesis:** unknown.
