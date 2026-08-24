---
id: 2026-08-24T180143Z-t9x4
subject: axm-cli-interactions
key: concepts-search-bundle-flag-rejected
observed_at: "2026-08-24T18:01:43Z"
session: temporal-routing-review-t9x4
kind: workaround
status: open
---

**Expected:** After reading `axm knowledge concepts --help`, a bundle selector would allow a search to be limited to `@craigsmitham/effect-v4`.
**Observed:** `axm knowledge concepts search DateTime --bundle @craigsmitham/effect-v4 --json` failed with `Unrecognized flag: --bundle`.
**Impact:** One CLI invocation failed and the knowledge lookup required an additional help command; elapsed delay was not measured.
**Recovery:** `axm knowledge concepts search --help` exposed the supported flags; work continued with an unscoped project search.
**Detected by:** The CLI returned a usage error and exit failure.
**Observed factors:** AXM CLI `0.27.15`; project scope; the parent help listed the `search` subcommand but not its flags.
**Hypothesis:** Bundle-level filtering is not supported by `concepts search`, and the parent help does not make that limitation visible.
**Suggests:** Consider documenting how to narrow a project-wide search to a known bundle, or explicitly state that search has no bundle selector.

Evidence: The rejected command returned `code: usage`, `detail: Unrecognized flag: --bundle in command axm knowledge concepts search`; subcommand help lists only `--limit`, `--cursor`, and `--scope`.
