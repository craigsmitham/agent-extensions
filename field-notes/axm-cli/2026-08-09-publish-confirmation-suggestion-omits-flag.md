---
subject: axm-cli
key: publish-confirmation-suggestion-omits-flag
date: 2026-08-09
kind: gap
status: open
---

**Expected:** When non-interactive publication requires an explicit
confirmation flag, the error would name the supported flag needed to continue.
**Actual:** `axm publish --authored --owner @craigsmitham --on-existing verify
--json` exited 2 with "Interactive prompt required: Apply changes?" and
suggested passing "the value via a flag" without naming `--yes`.
**Gap:** The failure identifies the confirmation requirement but makes an
automation caller search command help to discover the actionable syntax.
**Suggests:** Name `--yes` in the error suggestion and include a ready-to-run
retry command.

Evidence: the publish command exited 2 on 2026-08-09; `axm publish --help`
subsequently showed `--yes, -y` as the non-interactive confirmation flag.
