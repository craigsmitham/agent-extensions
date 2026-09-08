---
name: spot-spew
description: >
  Find avoidable maintenance burden from custom implementations of non-core
  needs or non-idiomatic use of adopted software, infrastructure, and tools.
  Identify opportunities to replace custom machinery or simplify necessary
  code using established capabilities and patterns. Not for style-only review.
---

# Spot Spew

Inspect the requested codebase or subject for worthwhile opportunities to
remove unnecessary code or simplify necessary code.

Consider two kinds of opportunity:

- **Capability substitution:** replace custom implementations of non-core needs
  with capabilities already available in adopted dependencies, services, or
  configuration.
- **Idiomatic simplification:** implement required behavior using the adopted
  tool's established abstractions, extension points, and lifecycle. This can
  apply to core or non-core code; a unique domain obligation does not require
  unconventional framework machinery.

For each opportunity:

- Establish the required behavior, governing obligations, and constraints.
  For capability substitution, explain why the need is non-core.
- Identify the custom or unconventional implementation and its concrete burden,
  such as duplicated state, extra coordination, fragile lifecycle handling, or
  harder testing and upgrades.
- Verify alternatives against installed versions, official documentation, and
  relevant first-party examples. Local repository conventions alone do not
  establish that an approach is idiomatic.
- Compare retaining the code with replacement or simplification: behavior
  coverage, migration effort, remaining complexity, costs, and constraints.

Report the strongest opportunities first. For each, cite code locations
and capability or idiom evidence; explain what could disappear or become
simpler, material tradeoffs, and unresolved questions.

Non-core or unconventional code is not inherently waste. Treat a departure
from convention as a signal to investigate, not a finding by itself. Preserve
justified departures when the conventional approach cannot satisfy the actual
obligation or would add burden. Recommend change only when evidence supports a
net reduction in burden; do not recommend changes solely for stylistic
conformity. Distinguish verified findings from candidates; report when none
qualify.

Assessment only: do not modify code or create work items.
