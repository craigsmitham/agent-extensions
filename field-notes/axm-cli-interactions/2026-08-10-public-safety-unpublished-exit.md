---
subject: axm-cli-interactions
key: public-safety-unpublished-exit
date: 2026-08-10
kind: gap
status: open
---

**Expected:** `docs/publishing.md` says to run `scripts/check-public-safety.sh`
and resolve every finding before publishing, so a release-ready unpublished
package set should be able to pass that gate before upload.
**Actual:** The script exited 1 solely because the three intended new skills
were unpublished and suggested publishing them to resolve the findings.
**Gap:** The documented pre-publish gate cannot succeed for a first publication
when unpublished-content advisories are treated as failing findings.
**Suggests:** Exempt unpublished-content advisories from the pre-publish safety
exit status, or document them as the one expected release-resolved exception.

Evidence: `scripts/check-public-safety.sh` exited 1 with three
`workspace/authored-content-unpublished` warnings and no other findings.
