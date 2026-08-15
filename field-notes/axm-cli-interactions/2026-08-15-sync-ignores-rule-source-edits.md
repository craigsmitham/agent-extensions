---
subject: axm-cli-interactions
key: sync-ignores-rule-source-edits
date: 2026-08-15
kind: gap
status: open
---

**Expected:** After editing the canonical `src/RULE.md` bodies of two
workspace-authored, enabled rules, `axm sync --preview` would report and `axm
sync` would render the revised bodies into the managed rules region.
**Actual:** Scoped sync previews reported both rules up to date; workspace sync
updated only Knowledge discovery; the managed rules region retained each
rule's original scaffold placeholder.
**Gap:** Sync did not recognize canonical body drift for enabled,
workspace-authored rules even though rule installation guidance says sync
recomputes the complete managed rules block.
**Suggests:** Include workspace-authored rule body content in sync drift
detection and rendering, or document the command that refreshes enabled rule
projections after authoring edits.

Evidence: `axm lint --details` returned no findings; scoped previews for
`@craigsmitham/rules/yagni` and `@craigsmitham/rules/tidy-first` were no-ops;
workspace preview and apply reported only an `AGENTS.md` Knowledge discovery
update; afterward `AGENTS.md` still contained “Describe the behavior this rule
asks agents to follow” for both rules while each canonical `src/RULE.md`
contained its completed guidance.
