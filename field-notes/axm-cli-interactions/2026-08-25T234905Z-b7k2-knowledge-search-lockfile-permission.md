---
id: 2026-08-25T234905Z-b7k2
subject: axm-cli-interactions
key: knowledge-search-lockfile-permission
observed_at: "2026-08-25T23:49:05Z"
session: s8k2q
kind: workaround
status: open
---

**Expected:** `axm knowledge concepts search "inputs signals" --non-interactive` should search the installed knowledge corpus, as directed by `axm knowledge concepts --help`.
**Observed:** The command exited before returning search results because it could not read the workspace lockfile.
**Impact:** Knowledge discovery through AXM was unavailable for this query; progress required one fallback search over the local source corpus.
**Recovery:** Used `rg` and read the matched Gen Stack source concepts directly; the original documentation question remained answerable.
**Detected by:** The AXM command returned exit status 9 with a validation diagnostic.
**Observed factors:** The command ran from the workspace root with `--non-interactive`; `axm knowledge concepts --help` had succeeded immediately beforehand.
**Diagnostic evidence:** Exit status: `9`. Diagnostic: `Failed to read the workspace lockfile. Fix the file's permissions or restore it from version control, then rerun. (validation)`.
**Hypothesis:** unknown

Evidence: The search command, exit status, diagnostic, preceding successful help invocation, and fallback are retained above.
