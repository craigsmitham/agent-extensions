---
id: 2026-09-08T144320Z-fShT
subject: axm-cli-interactions
key: versioned-fqn-selector-rejected
observed_at: "2026-09-08T14:43:20Z"
session: session_01FoDZXZVV1Gh4KYPifShTCn
kind: gap
status: open
---

**Expected:** After publishing, the AXM skill directs an "exact-version
Registry readback", so `axm publish --preview --on-existing verify` was given
version-pinned selectors
`@craigsmitham/knowledge/software-engineering@2.8.0` and
`@craigsmitham/packs/software-engineering@2.3.0`.
**Observed:** The command exited 9 with
`{"ok":false,"code":"validation","detail":"Invalid fully qualified name:
@craigsmitham/knowledge/software-engineering@2.8.0"}` and the suggestion "Use
the 3-segment format:
@handle/(skills|mcps|subagents|rules|hooks|knowledge|packs)/name". The
selector grammar has no version segment, so a readback cannot name the version
it verifies; it verifies whatever version the local manifest currently
declares.
**Impact:** One rejected command and one rerun with unversioned selectors
before the digest verification could be completed. No mutation was affected;
the publish had already succeeded.
**Recovery:** Reran with unversioned selectors. `--on-existing verify`
resolved 2.8.0 and 2.3.0 from the authored manifests and reported
`version_already_published` / `success` for both, which is the intended
digest-match no-op. Task completed.
**Detected by:** Non-zero exit status and the structured `validation` error in
the JSON result.
**Observed factors:** axm 0.28.11; axm skill 0.28.1 (bundled
@agentxm/skills/axm@0.28.1); registry `agentxm`; project scope; both packages
workspace-authored.
**Diagnostic evidence:** exit status 9; `code: validation`; cause tag
`FqnInvalidError`; affected selectors
`@craigsmitham/knowledge/software-engineering@2.8.0` and
`@craigsmitham/packs/software-engineering@2.3.0`; retryability: not supplied;
suggested recovery: 3-segment FQN format.
**Hypothesis:** FQN parsing is shared across commands and deliberately
version-free, while publish takes its version from the authored manifest; the
skill's "exact-version readback" wording does not map onto any selector
syntax.
**Suggests:** Either accept and validate a version suffix on publish
selectors, or have the skill describe the readback as verifying the authored
manifest version and checking that version in the result.
