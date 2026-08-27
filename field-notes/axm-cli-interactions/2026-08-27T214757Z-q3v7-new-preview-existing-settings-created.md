---
id: 2026-08-27T214757Z-q3v7
subject: axm-cli-interactions
key: new-preview-existing-settings-created
observed_at: "2026-08-27T21:47:57Z"
session: 01a04517-ce35-7b83-bb62-dc80444f257a
kind: gap
status: open
---

**Expected:** The `axm skills new quick-change --preview --yes --json` plan would classify the existing `axm.json` target as updated rather than created.
**Observed:** The preview reported `axm.json` with `change: "created"`, although the file existed and already contained workspace desired state.
**Impact:** The preview's path-level change label could not distinguish new package files from an edit to existing workspace state; the file had to be checked separately before application.
**Recovery:** Confirmed the existing `axm.json` before applying any mutation and continued using the preview only for its bounded target inventory.
**Detected by:** Comparing the structured preview with the observed filesystem and previously read workspace configuration.
**Observed factors:** AXM 0.28.1; candidate `596578b1788715dbf2be672ed07f929434e1bf8334a24246b760592998c987db`; outcome `previewed`; process exit status `0`; no diagnostic output was supplied.
**Diagnostic evidence:** Primary result target: `{ "path": "axm.json", "change": "created" }`; diagnostic output: none supplied.
**Hypothesis:** The plan may apply the enclosing creation unit's change classification to every target rather than report each path's filesystem transition.
**Suggests:** Report existing shared workspace files as updated while retaining the creation state for new package files.

Evidence: `axm.json` was present before the preview and contained configured agents, skills, knowledge bundles, and packs.
