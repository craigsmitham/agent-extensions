---
id: 2026-08-22T220219Z-q7m2
subject: axm-cli-interactions
key: packs-show-rejects-member
observed_at: "2026-08-22T22:02:19Z"
session: a8f3c1
kind: gap
status: open
---

**Expected:** `axm packs show @craigsmitham/skills/setup-architecture-docs --json` should show the pack relationship because current `axm help packs` says `axm packs show <extension>` compares membership state.
**Observed:** AXM returned a validation error: `Expected a pack identity: @craigsmitham/skills/setup-architecture-docs`.
**Impact:** One documented read-only inspection attempt produced unusable output and required a different query; elapsed delay was not measured.
**Recovery:** Query the known software-architecture pack identity and inspect its declared dependencies; the audit continued.
**Detected by:** Comparing the command result with the immediately preceding current CLI help output.
**Observed factors:** AXM CLI 0.27.15; project scope; workspace lint was clean; the target skill is a configured member of a workspace-authored pack.
**Hypothesis:** The help uses `extension` to mean a pack extension, while the command accepts only pack identities.

Evidence: `axm help packs` states “Use `axm packs show <extension>`”; the member identity command exited with the validation error above.
