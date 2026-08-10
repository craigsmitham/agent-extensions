---
subject: axm-cli
key: version-authority-diverges
date: 2026-08-09
kind: gap
status: open
---

**Expected:** The active AXM CLI, its installed skill guidance, and the CI
validation pin would expose one current version authority or an explicit
compatibility policy.
**Actual:** `axm --version` reported `0.26.0`, the installed AXM skill metadata
declared CLI version `0.25.8`, and `.github/workflows/public-safety.yml` installed
`axm.sh@0.25.7`.
**Gap:** A maintainer cannot tell from the existing routes which release should
govern local guidance and public-package validation.
**Suggests:** Define the intended version authority and update path, then make
the skill metadata and CI pin derive from or verify against it.

Evidence: `axm --version`,
`.axm/extensions/@agentxm/skills/axm/src/SKILL.md`, and
`.github/workflows/public-safety.yml` inspected on 2026-08-09.
