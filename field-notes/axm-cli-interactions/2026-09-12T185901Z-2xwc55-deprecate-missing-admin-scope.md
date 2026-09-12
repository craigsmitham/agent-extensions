---
id: 2026-09-12T185901Z-2xwc55
subject: axm-cli-interactions
key: deprecate-missing-admin-scope
observed_at: "2026-09-12T18:59:02Z"
session: session_01WpCARpDukUjyTm4cVPnusT
kind: blocked
status: open
---

**Expected:** `axm deprecate <old> --replacement <new> --message ...` would record deprecation guidance, since the same login had just published `@craigsmitham/skills/docs@0.4.0`, `@craigsmitham/skills/okf@0.1.9`, and `@craigsmitham/packs/docs@0.7.0` successfully.
**Observed:** Both calls (`@craigsmitham/skills/author-docs` → `docs`, `@craigsmitham/skills/author-okf` → `okf`) failed with `forbidden`: "Missing required scope: extensions:admin." The failing request was the preliminary GET of `/v1/extensions/<fqn>/deprecation`. The `--json` result's nested `message` field contained a serialized Effect `HttpClientResponse` object (function source text, circular markers) instead of a readable message. No suggestion or recovery command named the scope or how to obtain it.
**Impact:** Deprecation step of a rename could not complete; old identities remain undeprecated (`deprecation: null` on readback). Required handing a manual re-login step back to the user. Retries: 0.
**Outcome:** Blocked; publish, commit, and push completed.
**Recovery:** not yet — likely `axm login --scope extensions:admin` followed by rerunning the deprecations.
**Detected by:** `axm deprecate --json --non-interactive` result.
**Observed factors:** axm 0.29.4; registry agentxm; session already authenticated with publish rights; 403 on a read of deprecation state before any write.
**Diagnostic evidence:** code `forbidden`; tag `ExtensionsGetDeprecation403`; HTTP 403; suggestions: not supplied.
**Hypothesis:** The default login grant omits `extensions:admin`, and deprecate requires it even for the pre-read.
**Suggests:** Emit a recovery suggestion naming `axm login --scope extensions:admin`, and keep serialized client objects out of the JSON `message`.
