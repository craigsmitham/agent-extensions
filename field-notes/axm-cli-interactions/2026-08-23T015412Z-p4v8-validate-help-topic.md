---
id: 2026-08-23T015412Z-p4v8
subject: axm-cli-interactions
key: validate-help-topic
observed_at: "2026-08-23T01:54:12Z"
session: 01a02bf6-359b-7132-a0d8-40903b3e1337
kind: gap
status: open
---

**Expected:** `axm help validate` would describe an AXM validation command for
checking changed extension manifests after synchronization.
**Observed:** AXM reported that `validate` is an unknown help topic or command
path and suggested listing the general help topics.
**Impact:** One help query was unusable; elapsed delay was not measured.
**Recovery:** Use the clean `axm sync --preview` result for workspace
materialization and the extension-specific OKF, profile, and evaluation-suite
validators for the changed artifacts.
**Detected by:** The CLI returned a structured `not_found` help response.
**Observed factors:** The workspace sync preview and apply both succeeded, and
the requested work changed knowledge, skill, and pack manifests.
**Hypothesis:** AXM has no general `validate` command in this installed version.
**Suggests:** Document the intended manifest-validation route, or expose it
through a discoverable help topic.

Evidence: `axm help validate` returned `Unknown help topic or command path
'validate'` with code `not_found`.
