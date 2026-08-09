# Bundle update log

## 2026-08-09

- **Trust**: Machine-confirmed all 16 stable concepts against their cited
  sources with `codex/gpt-5.6` and set a six-month freshness review date;
  human review remains a distinct, unclaimed trust signal.
- **Ownership**: Made knowledge concepts authoritative for context-gardening
  and repository-instruction finding classes so skills can focus on control
  flow without duplicating doctrine.
- **Specification practice**: Added
  [spec-driven development](domains/software-engineering/practices/spec-driven-development.md)
  as the umbrella software-engineering practice, separating its shared
  development loop from repository-specific authority and mutation choices.
- **Specification patterns**: Added [spec-first](domains/software-engineering/patterns/spec-first.md),
  [spec-anchored](domains/software-engineering/patterns/spec-anchored.md), and
  [spec-as-source](domains/software-engineering/patterns/spec-as-source.md) as
  distinct models for specification persistence, human code editing, and
  durable change.
- **Pattern**: Added [progressive disclosure](patterns/progressive-disclosure.md)
  as the reusable structure for advertising small routes and loading deeper
  context only when relevant.
- **Practice**: Added [context gardening](practices/context-gardening.md) as the
  evidence-led maintenance cycle for repairing discovery, pruning noise, and
  promoting knowledge to the right harness element.
- **Vocabulary**: Added agent experience (AX) to the
  [glossary](glossary.md) as an emerging lens distinct from harness engineering.
- **Foundation**: Added [agent legibility](foundations/agent-legibility.md) as
  the cross-domain quality of making task-relevant intent, state, capabilities,
  constraints, and feedback usable by an agent.
- **Organization**: Reorganized concepts by subject into
  [foundations](foundations/), [application domains](domains/), and
  [elements](elements/), while retaining deprecated compatibility routes for
  earlier concept IDs.
- **Software engineering**: Promoted [software engineering](domains/software-engineering/)
  to the first application domain and retained “coding harness” as a glossary
  term for [software engineering harnesses](domains/software-engineering/harnesses.md).
- **Instruction split**: Separated general [instruction files](elements/instruction-files.md)
  from [repository instruction files](domains/software-engineering/repository-instruction-files.md)
  and moved the existing workflow to
  [How to design repository instruction files](domains/software-engineering/guides/repository-instruction-files.md).
- **Guide scope**: Kept [How to design an agent skill](guides/agent-skills.md)
  domain-independent because its workflow does not require repository-specific
  assumptions.
- **Scope**: Expanded the bundle from coding-agent concerns to harness
  engineering as a general discipline, with context engineering as a core
  responsibility and coding harnesses as a software-engineering domain profile.
- **Foundations**: Added explainers for [harness engineering](explainers/harness-engineering.md),
  [context engineering](explainers/context-engineering.md), and
  [coding harnesses](explainers/coding-harnesses.md).
- **Reference**: Added the [harness engineering glossary](glossary.md) to keep
  application domains, runtime topologies, working environments, and elements
  distinct.
- **Expansion**: Added explainer and guide sections with paired concepts for
  [agent skills](elements/agent-skills.md) and
  [instruction files](elements/instruction-files.md).
- **Structure**: Added placeholder indexes for [patterns](patterns/) and
  [practices](practices/), and retained the original `instruction-files`
  concept ID as a deprecated compatibility route.
- **Migration**: Moved the bundle to the `@craigsmitham` namespace and paired
  it with the migrated `improve-instructions` skill.

## 2026-08-07

- **Creation**: Established the harness-engineering bundle with
  [instruction files](instruction-files.md).
