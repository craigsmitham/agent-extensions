---
id: 2026-09-08T231500Z-q8m2
subject: axm-cli-interactions
key: login-scope-ignored-when-session-valid
observed_at: "2026-09-08T23:15:00Z"
session: 1e63a258-cc0a-4526-8328-b9d202a20020
kind: gap
status: open
---

**Expected:** `axm login --scope extensions:admin`, the exact recovery command
the CLI itself emitted as a structured suggestion alongside a `forbidden` /
`Missing required scope: extensions:admin` failure, to obtain that scope.
**Observed:** the command exited successfully with `Already logged in to
registry.agentxm.ai as @craigsmitham.` and performed no sign-in. A following
`axm whoami --json` reported the unchanged scope set
`["extensions:publish:new","extensions:publish:version"]` and the unchanged
`expiresAt` 2026-09-09T12:36:36.908Z, confirming no new credential was issued.
The requested `--scope` was neither honored nor reported as ignored.
**Impact:** the suggested recovery did not restore progress; the blocked
registry deprecation of two identities remained blocked. Two extra commands
(the no-op login, plus a `whoami` to detect that it was a no-op) and one
`axm login --help` read were needed to find `--yes` as the actual route. The
success exit status would have masked the no-op had the scope not been
re-checked.
**Recovery:** not yet applied. `axm login --help` documents `--yes` as "Start a
new sign-in without prompting when a valid session already exists", so
`axm login --yes --scope extensions:admin` is the apparent route; it requires
interactive browser approval and was handed to the operator.
**Detected by:** comparing `axm whoami --json` scopes and `expiresAt` before
and after the login command; the login command's own output claimed success.
**Observed factors:** axm 0.28.11 (0.28.12 available); credentialType
`session`, valid and unexpired at the time of the call; the suggestion
originated from the CLI's own `{"type":"suggestion", ...,
"cmd":"axm login --scope extensions:admin"}` event on the prior failure.
**Diagnostic evidence:** login exit status 0; no error code or warning emitted;
scopes before `["extensions:publish:new","extensions:publish:version"]`, scopes
after identical; `expiresAt` identical across both `whoami` calls; retryability
not supplied. No authorization material was retained.
**Hypothesis:** `login` short-circuits on any valid existing session before
comparing the requested `--scope` set against the granted set, so a scope
upgrade is indistinguishable from a redundant login.
**Suggests:** either honor `--scope` by re-authenticating when the requested
scopes are not a subset of the granted ones, or warn that `--scope` was ignored
and name `--yes`; emitting a suggestion whose command cannot take effect in the
state that produced it is the specific gap.

Evidence: the suggested command was run by the operator in this session's
shell, immediately after the `ExtensionsGetDeprecation403` failure recorded in
2026-09-08T230500Z-k3v7, against
`/Users/craig/Code/craigsmitham/agent-extensions` on axm 0.28.11.
