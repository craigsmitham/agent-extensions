---
id: 2026-09-08T230500Z-k3v7
subject: axm-cli-interactions
key: deprecate-requires-undocumented-admin-scope
observed_at: "2026-09-08T23:05:00Z"
session: 1e63a258-cc0a-4526-8328-b9d202a20020
kind: blocked
status: open
---

**Expected:** `axm deprecate @craigsmitham/skills/engineer-requirements
--replacement ... --message ...` to apply, having preflighted with `axm whoami`
which reported an authenticated `@craigsmitham` session against
`https://registry.agentxm.ai` with scopes `extensions:publish:new` and
`extensions:publish:version`. Neither `axm deprecate --help` nor `axm help`
names a scope requirement for the command.
**Observed:** exit non-zero with `code: "forbidden"`, detail `Missing required
scope: extensions:admin.` The failure surfaced on the *read* leg — `GET
/v1/extensions/@craigsmitham/skills/engineer-requirements/deprecation`, HTTP
403 — before any mutation was attempted.
**Impact:** the registry half of a pack/skill retirement could not be completed
in-session; deprecation of two published identities
(`@craigsmitham/skills/engineer-requirements`,
`@craigsmitham/packs/requirements-engineering`) was deferred to an interactive
login the operator must run. One command attempt, no retry. Local removal was
unaffected and completed.
**Recovery:** not attempted in-session. The CLI emitted a structured
suggestion: `axm login --scope extensions:admin`. Task completed apart from the
registry mutation.
**Detected by:** non-zero exit and the `forbidden` JSON error envelope from the
first `axm deprecate` invocation.
**Observed factors:** axm 0.28.11 (0.28.12 available); credentialType
`session`, `expiresAt` 2026-09-09T12:36:36.908Z; `resourceRestrictions.extensions`
null; `axm lint --json` reported `axmSkillCompatibility.status: "compatible"`.
**Diagnostic evidence:** error code `forbidden`; problem type
`https://registry.agentxm.ai/problems/forbidden`; HTTP status 403; instance
`/v1/extensions/@craigsmitham/skills/engineer-requirements/deprecation`;
`details.requiredScope: "extensions:admin"`; `details.grantedScopes:
["extensions:publish:new","extensions:publish:version"]`; error tag
`ExtensionsGetDeprecation403`; retryability not supplied; attempt count 1.
**Hypothesis:** `login` issues a publish-oriented scope set by default, and
lifecycle-administration commands (`deprecate`, and plausibly `yank`,
`visibility`) require a scope that is not requested at login time nor declared
in per-command help.
**Suggests:** name the required scope in `axm deprecate --help` and in the
`publish` help topic, or have `axm whoami` flag which lifecycle commands the
current scope set cannot perform.

Evidence: `axm whoami --json` and `axm deprecate ... --json --non-interactive`
were run consecutively in the same shell against
`/Users/craig/Code/craigsmitham/agent-extensions` on axm 0.28.11. No
authorization material was retained.
