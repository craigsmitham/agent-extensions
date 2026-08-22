---
id: 2026-08-22T003439Z-p5n6
subject: axm-cli-interactions
key: publish-partial-upload-failures
observed_at: "2026-08-22T00:34:39Z"
session: s-k7p3
kind: workaround
status: open
---

**Expected:** An exact publication set admitted by authoritative preview would
publish every pending extension or fail before any upload.
**Observed:** The live publish uploaded six new versions, then reported four
registry-internal upload failures and one deadline timeout; two dependent packs
were blocked while nineteen existing versions remained verified.
**Impact:** The release became partially published and required an idempotent
re-preflight and retry of seven unresolved identities; elapsed time was not
measured.
**Recovery:** Re-preflighted only failed and dependency-blocked identities with
`--on-existing verify` before retrying, so any late successful upload would be
verified rather than overwritten.
**Detected by:** Inspecting the structured publish result after the exact
32-extension upload command completed.
**Observed factors:** The exact preview had reported `publicationStatus:
admitted`, 13 pending uploads, 19 verified existing versions, and no findings.
**Hypothesis:** Unknown; the registry returned generic internal errors for four
requests and one configured-deadline timeout.

Evidence: the live result reported `published: 6`, `alreadyPublished: 19`,
`failed: 5`, and `blocked: 2`; no local content changed during publication.
