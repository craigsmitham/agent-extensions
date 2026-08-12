---
subject: axm-cli-interactions
key: knowledge-lint-frontmatter-unlocated
date: 2026-08-12
kind: gap
status: open
---

**Expected:** `axm knowledge lint` rejects a concept for "invalid YAML
frontmatter", so the finding should name the offending key, line, or parser
error well enough to fix without guessing.
**Actual:** the error was `docs/playbook-explainer.md: playbook-explainer.md
contains invalid YAML frontmatter.` and nothing more — no line, column, key, or
underlying parser message, and no `Next` hint. The repeated filename is the
only locator.
**Gap:** the cause was an unquoted `description` scalar containing `: ` (`a
genre, not a type: a situation-selected...`), which YAML reads as a mapping.
Nothing in the output pointed at the description field or at quoting, so the
fix came from inspecting the two new files against the ten existing concepts
whose descriptions happen to contain no colon.
**Suggests:** surface the underlying YAML parser error (line/column and
message) on this finding, or at minimum name the key that failed to parse.

Evidence: AXM CLI 0.26.6, skill 0.26.6, workspace
`/Users/craig/Code/craigsmitham/agent-extensions`. Command
`axm knowledge lint --path ./.axm/extensions/@craigsmitham/knowledge/docs`
exited 1 with two such lines (`playbook-explainer.md`, `runbook-explainer.md`),
both newly authored with the same colon pattern in `description`. Quoting both
description values made the same command pass with no warnings. `--json` output
was not inspected on this run, so whether it carries richer cause is unknown.
