---
id: 2026-08-27T200645Z-h6q2
subject: axm-cli-interactions
key: new-preview-existing-settings-created
observed_at: "2026-08-27T20:06:45Z"
session: z7c2p1
kind: gap
status: open
---

**Expected:** The `axm skills new shape --owner @craigsmitham --preview --json` plan would classify the existing `axm.json` target as updated rather than created.
**Observed:** The preview identified `skills/shape/skill.json`, `skills/shape/src/SKILL.md`, and `axm.json` under targets with `change: "created"`, although `axm.json` already existed and contained configured workspace state.
**Impact:** The preview could not be relied on by itself to distinguish creation of new package files from modification of existing workspace desired state; one extra read of `axm.json` was required before apply.
**Recovery:** Confirmed the existing `axm.json` contents directly and retained the preview candidate for bounded application review.
**Detected by:** Comparing the structured preview target classification with the observed filesystem.
**Observed factors:** AXM 0.28.1; candidate `77e8e5edacff3f809ea42d8dd77029d2644e0579196fec4f2fa6b75f28af308e`; plan outcome `previewed`; process exit status `0`; `axm.json` was present before apply.
**Diagnostic evidence:** Primary result target: `{ "path": "axm.json", "change": "created" }`; diagnostic output: none supplied.
**Hypothesis:** The new-skill plan may use `created` for every file represented in a creation unit rather than expressing the path-local filesystem transition.
**Suggests:** Report the actual path-level transition for shared workspace files independently from the enclosing unit's creation state.

Evidence: The existing `axm.json` was readable immediately after the preview and already declared the workspace owner, agents, skills, knowledge bundles, and packs.
