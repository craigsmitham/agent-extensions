---
id: 2026-08-24T161802Z-q7m4
subject: axm-cli-interactions
key: publish-stale-pack-suggestion
observed_at: "2026-08-24T16:18:02Z"
session: s7k2p9
kind: gap
status: open
---

**Expected:** A successful dependency-inclusive pack publication would not
recommend publishing the updated pack that the same operation just published.
**Observed:** Publishing `@craigsmitham/packs/effect-v4@0.5.0` with dependencies
succeeded, but the final suggestions still warned that the previous pack range
`^0.3.0` did not reach knowledge `0.4.0` and recommended publishing an updated
pack.
**Impact:** The final output required one manual check to distinguish a stale
suggestion from an unresolved compatibility problem; elapsed time was not
measured.
**Recovery:** Confirmed in the same publish result that pack `0.5.0` succeeded
with knowledge `>=0.4.0`; the publication completed.
**Detected by:** Comparison of the publish finding and suggestion with the
admitted publication set and successful pack outcome.
**Observed factors:** AXM CLI `0.27.17`; dependency-inclusive publish; knowledge,
skill, and pack versions published in one operation; previous pack version used
`^0.3.0`.
**Hypothesis:** The compatibility suggestion is computed from the previously
published pack before the updated pack outcome is considered.
**Suggests:** Suppress or resolve the suggestion when the admitted publication
set contains a successfully published pack whose new dependency range reaches
the published dependency.

Evidence: The publish result reported knowledge `0.4.0`, skill `0.1.0`, and pack
`0.5.0` as successful; pack `0.5.0` resolved knowledge at `>=0.4.0`; the final
suggestion nevertheless requested an updated pack for the old `^0.3.0` range.
