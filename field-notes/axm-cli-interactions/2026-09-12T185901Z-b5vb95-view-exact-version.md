---
id: 2026-09-12T185901Z-b5vb95
subject: axm-cli-interactions
key: view-exact-version
observed_at: "2026-09-12T18:59:02Z"
session: session_01WpCARpDukUjyTm4cVPnusT
kind: workaround
status: open
---

**Expected:** `axm view @craigsmitham/skills/docs@0.4.0 --json` would show that exact published version, matching the `<fqn>@<version>` form `axm install` accepts.
**Observed:** Returned `ok: false`, `code: not_found` for `skills/docs@0.4.0`, `skills/okf@0.1.9`, and `packs/docs@0.7.0`, seconds after all three published. The same handles without `@version` returned `ok: true` with `latest.version` matching. `axm view --help` shows no version selector; a version is a positional `[<field>]` instead.
**Impact:** A misleading not-found immediately after publish; one extra readback round. Elapsed time not measured.
**Outcome:** Readback confirmed via unversioned view.
**Recovery:** Dropped the `@version` suffix and checked `latest.version` and `versions`.
**Detected by:** `axm view --json` result during post-publish verification.
**Observed factors:** axm 0.29.4; registry agentxm; recurrence of the same key already noted earlier today.
**Diagnostic evidence:** code `not_found`; suggestion "Sign in if this extension is private." (`axm login`).
**Hypothesis:** `view` treats `@version` as part of the name rather than rejecting it or resolving it.
**Suggests:** Accept `<fqn>@<version>` in `view`, or reject it with a usage error pointing to the field form.
