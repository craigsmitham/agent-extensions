---
id: 2026-08-16T020502Z-b4t
subject: axm-cli-interactions
key: publish-compat-warning-ignores-same-run-pack
observed_at: "2026-08-16T02:04:30Z"
session: 6faf0876-0105-4599-bf75-e87b41b17574
kind: gap
status: open
---

**Expected:** Publishing a knowledge bundle and, in the same admitted set, the
pack whose dependency range was widened to accept it would not report a range
incompatibility, since the pack version being published declares the accepting
range.
**Observed:** `axm publish @craigsmitham/knowledge/software-engineering
@craigsmitham/packs/software-engineering` printed both as admitted in dependency
order 0 and 1, published both, and also printed `▲
@craigsmitham/packs/software-engineering declares
@craigsmitham/knowledge/software-engineering at range "^0.2.0", which does not
include the published version 0.3.0. Compatibility review is needed.` The
on-disk `pack.json` declares `"^0.3.0"`; `"^0.2.0"` is the range from the
previously published pack 0.1.2. The `Next:` suggestion advised publishing an
updated pack version, which the same command had just done.
**Impact:** Two extra verification commands to confirm the released pack was
correct rather than to act on the warning. No rework; both packages published as
intended.
**Recovery:** Re-read the on-disk `pack.json` and confirmed `"^0.3.0"`, then
`axm view @craigsmitham/packs/software-engineering --json` confirmed 0.2.0 as
latest. Treated the warning as stale and continued.
**Detected by:** The warning contradicting the pack manifest edit made earlier
in the same session.
**Observed factors:** Both packages were named in one `axm publish` invocation.
The immediately preceding `axm publish --preview --json` reported `"findings":
[]` and `blocked: 0` for the same selection. Publish output reported `✔
Published 2 extensions`. Attempts to inspect the published pack with `axm view
<fqn> 0.2.0` and `axm view <fqn>@0.2.0` both returned `not_found`.
**Hypothesis:** The compatibility check compares the newly published bundle
version against the last published pack manifest rather than against the pack
manifest admitted in the same run.
**Suggests:** unknown.

Evidence: publish output lines `@craigsmitham/knowledge/software-engineering@0.3.0
— publish; dependency order 0` and `@craigsmitham/packs/software-engineering@0.2.0
— publish; dependency order 1` immediately preceding the `▲` warning quoting
range `"^0.2.0"`; `pack.json` line
`"@craigsmitham/knowledge/software-engineering": "^0.3.0"`.
