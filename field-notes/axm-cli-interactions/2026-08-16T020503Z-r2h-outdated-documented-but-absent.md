---
id: 2026-08-16T020503Z-r2h
subject: axm-cli-interactions
key: outdated-documented-but-absent
observed_at: "2026-08-16T01:58:40Z"
session: 6faf0876-0105-4599-bf75-e87b41b17574
kind: gap
status: open
---

**Expected:** `axm outdated` would list extensions with available updates. The
workspace's installed `axm` skill documents it in its quick reference as "Show
extensions with available updates · `axm outdated`".
**Observed:** `axm outdated` printed the general command help, whose command
inventory lists `knowledge, publish, fork, import, adopt, demote, install,
update, uninstall, list, view, visibility, version, yank, unyank, deprecate,
undeprecate, sync, lint, cache, upgrade, login, logout, whoami, token` and does
not include `outdated`. No error text identified the command as unknown.
**Impact:** One wasted command and a discarded output while diagnosing a
separate blocked update. The task continued by other means.
**Recovery:** Abandoned the command and used `axm update --preview --json`
instead.
**Detected by:** Help text appearing where a version listing was expected.
**Observed factors:** AXM CLI 0.27.5 installed via Homebrew, reported up to date
by `axm upgrade`. The `axm` skill is a registry install configured in this
project workspace. A separate attempt to update that skill in the same session
was blocked and did not apply.
**Hypothesis:** The skill's quick reference documents a command that this CLI
version does not implement, and an unrecognized subcommand falls through to
general help rather than an unknown-command error.
**Suggests:** unknown.

Evidence: `axm outdated` output ending in the `LEARN MORE` help section rather
than a listing; skill quick-reference row `| Show extensions with available
updates | `axm outdated` |`.
