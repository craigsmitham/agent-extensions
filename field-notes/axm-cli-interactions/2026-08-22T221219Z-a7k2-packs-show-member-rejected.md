---
id: 2026-08-22T221219Z-a7k2
subject: axm-cli-interactions
key: packs-show-member-rejected
observed_at: "2026-08-22T22:12:19Z"
session: audit-4f9c
kind: gap
status: open
---

**Expected:** `axm packs show <extension>` would accept the audited skill identity, as stated by `axm help packs`.
**Observed:** `axm packs show @craigsmitham/skills/author-architecture-docs --json` exited 9 with `Expected a pack identity`.
**Impact:** One read-only command failed and the audit required one additional query using the known pack identity.
**Recovery:** Query the declared `@craigsmitham/packs/software-architecture` pack directly; the audit continued.
**Detected by:** The CLI validation envelope and nonzero exit status.
**Observed factors:** AXM CLI 0.27.15; project scope; workspace lint clean; command used the canonical member FQN.
**Hypothesis:** The help text and command validator disagree about whether `packs show` accepts member extensions.
**Suggests:** Align the command behavior or usage text for member-to-pack inspection.

Evidence: `axm help packs` says “Use axm packs show <extension>”; the member query returned code `validation`, detail `Expected a pack identity: @craigsmitham/skills/author-architecture-docs`.
