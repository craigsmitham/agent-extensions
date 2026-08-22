---
id: 2026-08-22T232752Z-v3p9
subject: axm-cli-interactions
key: packs-show-member-rejected
observed_at: "2026-08-22T23:27:52Z"
session: codex-v3p9
kind: gap
status: open
---

**Expected:** `axm packs show <extension>` would accept the skill identity, as stated by the installed AXM skill and `axm help packs`.
**Observed:** `axm packs show @craigsmitham/skills/maintain-architecture-docs --json` exited 9 with `Expected a pack identity`.
**Impact:** Pack membership inspection required one failed command and a follow-up using the known pack identity.
**Recovery:** Use the software-architecture pack identity directly; the original naming assessment continued.
**Detected by:** The CLI validation error from the documented command form.
**Observed factors:** AXM CLI and installed AXM skill both report version 0.27.15; workspace lint was clean.
**Hypothesis:** The help and skill describe member-oriented lookup that the current command parser does not implement.
**Suggests:** Align `packs show` help and parser behavior for extension-member lookup.

Evidence: The command, argument, exit code 9, validation message, and matching CLI/skill versions are recorded above.
