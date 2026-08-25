---
id: 2026-08-25T184658Z-k4p8
subject: axm-cli-interactions
key: workspace-lock-version-mismatch
observed_at: "2026-08-25T18:46:58Z"
session: 01a03927
kind: blocked
status: open
---

**Expected:** AXM 0.27.18 would read the repository's accepted workspace
lockfile and complete the required read-only lint preflight.
**Observed:** `axm lint --json` reported that `axm-lock.yaml` was invalid
because `lockfileVersion` did not equal the expected value `5`.
**Impact:** AXM package lint and the AXM-backed public-safety gate could not
validate the revised packages; deterministic source, JSON, profile, and link
checks remained available.
**Recovery:** No AXM recovery was attempted because changing workspace state
was outside this profile-editing task. Work continued with the non-AXM checks.
**Detected by:** The required AXM preflight and the repository public-safety
script.
**Observed factors:** The executable reported version `0.27.18`; the affected
artifact was the repository-root `axm-lock.yaml`; the command was read-only.
**Diagnostic evidence:** AXM returned code `validation`, title `Invalid
Request`, and detail `lockfileVersion: Expected 5`; process exit status was
unavailable because it was not retained in the displayed result.
**Hypothesis:** The repository lockfile and installed CLI expect different
workspace-lock schema versions.

Evidence: Both `axm lint --json` and `bash scripts/check-public-safety.sh`
stopped while loading the same workspace lockfile before package validation.
