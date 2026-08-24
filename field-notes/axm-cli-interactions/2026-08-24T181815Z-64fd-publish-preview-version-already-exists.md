---
id: 2026-08-24T181815Z-64fd
subject: axm-cli-interactions
key: publish-preview-version-already-exists
observed_at: "2026-08-24T18:18:15Z"
session: unknown
kind: gap
status: open
---

**Expected:** Previewing the two versions produced by the current work would
construct publication candidates without uploading them.
**Observed:** The explicit preview stopped during selection because both
versions were already published.
**Impact:** One preview failed before archive construction; no upload occurred,
and one documented verification step was added to the work.
**Recovery:** Proceed with `--on-existing verify` to compare the authored
archives with the immutable registry releases; task completion is pending.
**Detected by:** `axm publish ... --preview --json --non-interactive` returned
exit code 6 with `version_exists` for both selected extensions.
**Observed factors:** The selection contained exactly the authored work-item
skill and software-engineering knowledge bundle; the registry identity was
authenticated; unrelated authored extensions were excluded.
**Hypothesis:** The versions were published by another interaction after their
local version increments.

Evidence: The preview selected two extensions, published zero, failed two, and
reported that skill version `0.1.7` and knowledge version `1.0.1` already exist.
