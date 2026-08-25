---
id: 2026-08-25T212914Z-q5n8
subject: axm-cli-interactions
key: explicit-login-scopes-replaced-session-grants
observed_at: "2026-08-25T21:29:14Z"
session: s8f2n
kind: workaround
status: open
---

**Expected:** Authorizing the missing Registry scope during one release workflow would add that capability without removing scopes already needed by later publish and lifecycle steps.
**Observed:** Each `axm login --scope ...` request established only the explicitly requested scopes. Authorizing `extensions:publish:new` allowed the first package identity but then blocked version publication; authorizing both publish scopes allowed publication but then blocked deprecation; adding `extensions:admin` still caused the replacement pack to be concealed as not found because `extensions:read` was absent.
**Impact:** The release required four browser authorization rounds and three failed Registry preflights or lifecycle attempts before one combined scope set supported the full workflow.
**Recovery:** Reauthenticated with `extensions:read`, `extensions:publish:new`, `extensions:publish:version`, and `extensions:admin` together, then successfully created both deprecation records with an available replacement.
**Detected by:** Structured Registry responses from publish and deprecate commands.
**Observed factors:** AXM CLI `0.28.0`; one session publishing a new package identity, new versions, and deprecation guidance; explicit `--scope` flags; public replacement pack already readable through `axm view` before the concealed-not-found response.
**Diagnostic evidence:** New-package preview initially returned `authoritative_preflight_failed`; the eight-version preview returned the same failure after the first scoped login; deprecation returned HTTP `403`, code `forbidden`, required scope `extensions:admin`, and granted scopes `extensions:publish:new` plus `extensions:publish:version`; the next deprecation returned HTTP `404`, code `extension_not_found`, until `extensions:read` was included. No failed deprecation attempt changed Registry state.
**Hypothesis:** Explicit OAuth scopes replace the saved grant set, while command recovery suggestions name only the immediately missing scope and do not preserve the scopes required by the end-to-end release workflow.
**Suggests:** Make scoped reauthentication additive by default, or have recovery guidance include the current grants plus the missing scope and disclose when a concealed not-found result can mean missing read permission.

Evidence: The final combined authorization immediately enabled both warning-only deprecations to reference `@craigsmitham/packs/gen-stack` without changing package content or visibility.
