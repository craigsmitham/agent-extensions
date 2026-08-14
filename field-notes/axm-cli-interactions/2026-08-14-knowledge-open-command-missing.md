---
subject: axm-cli-interactions
key: knowledge-open-command-missing
date: 2026-08-14
kind: gap
status: open
---

**Expected:** The installed `garden-context` skill directed the agent to read a concept with `axm knowledge open context-engineering operations/context-gardening`.
**Actual:** AXM 0.27.4 rejected `open` as an unknown `axm knowledge` subcommand and listed `axm knowledge concepts get <reference>` as the supported exact-read command.
**Gap:** The skill's progressive-loading command no longer matches the installed CLI surface.
**Suggests:** Replace the stale `axm knowledge open <bundle> <concept-id>` examples with exact `axm knowledge concepts get '@owner/knowledge/<bundle>#<concept-id>'` references, including the user-scope variant.

Evidence: In the project workspace on 2026-08-14, `axm knowledge open context-engineering operations/context-gardening` exited with “Unknown subcommand \"open\" for \"axm knowledge\"”; `axm knowledge concepts get --help` documented exact-reference reads and a `--scope project|user` flag.
