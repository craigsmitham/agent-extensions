---
id: 2026-08-24T162523Z-k7m2
subject: axm-cli-interactions
key: packs-show-extension-identity
observed_at: "2026-08-24T16:25:23Z"
session: c8f4a2
kind: gap
status: open
---

**Expected:** `axm packs show <extension>` would accept the audited skill identity, as described by `axm help packs` and the active audit workflow.
**Observed:** `axm packs show @craigsmitham/skills/craft-effect-v4 --json` exited with a validation error: `Expected a pack identity`.
**Impact:** Pack relationship inspection required one additional command path; elapsed delay was not measured.
**Recovery:** Inspect the declared recommended pack directly and compare its manifest membership; the audit continued.
**Detected by:** The command returned the fixed `ok: false` validation envelope.
**Observed factors:** AXM CLI 0.27.17; project workspace; audited skill declares `@craigsmitham/packs/effect-v4` in `recommendedPacks`.
**Hypothesis:** The help text and command argument contract use different meanings of `<extension>`.

Evidence: `axm help packs` says “Use axm packs show <extension>”; the skill FQN was rejected specifically because it was not a pack identity.
