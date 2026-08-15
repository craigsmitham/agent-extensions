---
id: 2026-08-15T234104Z-k7p
subject: axm-cli-interactions
key: registry-upload-internal-error-blocks-pack
observed_at: "2026-08-15T23:41:04Z"
session: s-a7m4
kind: blocked
status: open
---

**Expected:** The admitted four-package publication set would publish together
after its clean preview.
**Observed:** The rule and knowledge packages published, the skill upload failed
with an internal registry error, and the pack was blocked by that failed
dependency.
**Impact:** The release became partial and required another AXM publication
attempt; elapsed time was not measured.
**Recovery:** AXM supplied an exact continuation command that verifies the two
published versions and retries the incomplete members; the release was not yet
complete when observed.
**Detected by:** The structured `axm publish` result reported two successes, one
failed upload, one blocked dependency, and `ok: false`.
**Observed factors:** The same explicit four-package selection passed preview;
all packages were version 0.2.0 and the pack resolved its three dependencies to
0.2.0 before upload.
**Hypothesis:** unknown

Evidence: The failed outcome used reason `upload_failed` with an internal error
for the skill, and the pack outcome used reason `blocked_by_dependency`.
