---
id: 2026-09-12T190100Z-m5v9pi
subject: axm-cli-interactions
key: deprecate-replacement-not-found
observed_at: "2026-09-12T19:01:00Z"
session: session_01WpCARpDukUjyTm4cVPnusT
kind: blocked
status: open
---

**Expected:** With `extensions:admin` granted, `axm deprecate @craigsmitham/skills/author-docs --replacement @craigsmitham/skills/docs --message ...` (and the same for `author-okf` → `okf`) would record deprecation with a structured replacement, because both replacements are published and public.
**Observed:** Both calls exited 3 with `not_found`: "The replacement extension was not found." The same session's `axm view @craigsmitham/skills/docs visibility` and `axm view @craigsmitham/skills/okf visibility` returned `public`, and unversioned `axm view` showed `latest.version` 0.4.0 and 0.1.9. The problem `instance` was `/v1/extensions/@craigsmitham/skill/author-docs/deprecation` (singular `skill`); the earlier 403 pre-read used `/v1/extensions/%40craigsmitham/skills/author-docs/deprecation` (plural). As before, the JSON nested `message` contained a serialized Effect response object.
**Impact:** Deprecation of both renamed skills could not complete; readback still shows `deprecation: null`. Retries: 0 for this error.
**Outcome:** Blocked; returned to user for a decision.
**Recovery:** not yet
**Detected by:** `axm deprecate --json --non-interactive` result.
**Observed factors:** axm 0.29.4; registry agentxm; replacements published about 5 minutes earlier; session re-authenticated via device code with only `extensions:admin` scope; OS keychain unavailable warning at login.
**Diagnostic evidence:** exit 3; code `not_found`; problem code `extension_not_found`; tag `ExtensionsPutDeprecation404`; HTTP 404; problem type `https://registry.agentxm.ai/problems/extension_not_found`; suggestions: not supplied.
**Hypothesis:** unknown — possibly a type-segment mismatch (singular vs plural) when the replacement FQN is resolved server-side.
