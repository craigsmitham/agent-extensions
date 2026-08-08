---
subject: axm-cli
key: public-safety-unpublished-warning
date: 2026-08-08
kind: gap
status: open
---

**Expected:** `scripts/check-public-safety.sh` would validate an unpublished package change before publication, as required by the repository publishing gate.
**Actual:** The check exited 1 solely because `axm lint` reported `workspace/authored-content-unpublished` for the changed skill.
**Gap:** An expected pre-publication state is treated as a failing safety condition, so the mandated pre-publication check cannot pass while a package change awaits publication.
**Suggests:** Make this advisory non-fatal in the public-safety check while preserving it in ordinary lint output.

Evidence: `scripts/check-public-safety.sh` exited 1 after `axm lint` reported one warning and no errors for `.axm/extensions/@craigsmitham/skills/field-notes`; the warning instructed publishing the working version.
