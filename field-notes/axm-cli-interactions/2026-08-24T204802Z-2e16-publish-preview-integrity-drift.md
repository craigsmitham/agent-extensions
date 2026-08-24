---
id: 2026-08-24T204802Z-2e16
subject: axm-cli-interactions
key: publish-preview-integrity-drift
observed_at: "2026-08-24T20:48:02Z"
session: 2E16E51B-DF14-4C75-811E-079918D2A447
kind: workaround
status: open
---

**Expected:** `axm publish --preview --json --non-interactive` would verify published versions and prepare every new authored version for upload.
**Observed:** The preview reported immutable-version integrity drift for `@craigsmitham/knowledge/effect-v4@0.5.0` and atomically blocked five otherwise pending releases.
**Impact:** Publication was delayed by one failed preview, one version-bump preview and application, and one repeated catalog preview.
**Recovery:** `axm version @craigsmitham/knowledge/effect-v4 patch` advanced the bundle to `0.5.1`; the repeated preview completed with six pending releases and no failures.
**Detected by:** The publish preview returned `ok: false`, `failed: 1`, and the `integrity_drift` reason.
**Observed factors:** The workspace was authenticated as `@craigsmitham`; the initial bulk selection contained 33 authored extensions, 27 verified existing versions, five blocked entries, and one failed entry.
**Hypothesis:** The authored bundle changed after version `0.5.0` had already been published.

Evidence: AXM named `@craigsmitham/knowledge/effect-v4@0.5.0` as the immutable version with integrity drift. Its version preview reported exactly `0.5.0 -> 0.5.1`, and the subsequent publish preview reported `ok: true`, 27 already published, six pending, and no blocked or failed entries.
