---
okf_version: "0.2"
---
# Engineering environment

Engineering tools, repository interfaces, workflows, and environments.

This bundle contains existing material migrated from product-engineering. Coverage is partial.


Shared definitions and guidance are supplied by `@craigsmitham/knowledge/software-engineering-foundations`, included in this discipline’s pack.

Companion readings in other discipline bundles are optional. Resolve a named concept by its bundle identity and concept ID with `axm knowledge concepts get`.

- [Adopting a repository task interface](adopting-a-repository-task-interface.md) — Use when converting the task-interface principles into an actual repository change; a twelve-step design or repair sequence, the local binding that records runner-specific decisions, the signals that show whether the interface helped, and a worked example of collapsing four validation inventories into one.
- [Designing a coherent repository task interface](repository-task-interface.md) — Use when repository tasks, scripts, launchers, wrappers, or CI paths compete, or when placing new repeatable work; name the competing-semantics problem, the outcomes one task interface must deliver, and the portable vocabulary that the contract, invocation, and adoption guides build on.
- [Resolved task contract principles](resolved-task-contract-principles.md) — Use when deciding what a single repository task means — who owns it, what it guarantees from a clean shell, which dependencies it declares, and when a cache replay still answers the caller's question; the five principles that define a canonical resolved contract.
- [Task invocation and conformance principles](task-invocation-and-conformance-principles.md) — Use when wrappers, aliases, hooks, agents, or CI steps have accumulated around a repository's tasks; the five principles that bound each entrypoint's role, keep one membership authority per workflow, hold actors to canonical semantics, and check resolved rather than declared behavior.
