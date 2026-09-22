# Public agent extensions
- Keep concepts and guidance coherent across extensions. Resolve contradictory
  terminology or claims before publishing.


<!-- axm:start v=1 region=knowledge ext=@agentxm/knowledge/discovery gen=71e559b75a6ceadb7bf57b773b5bfc34c33b2b883ebe7b1d6049b6f4c6eebffa -->
## Knowledge Bundles

Use `axm knowledge concepts --help` to search, read, and explore these bundles.

### @agentxm

<!-- axm:point v=1 ext=@agentxm/knowledge/agent-engineering kind=knowledge -->

| Bundle | Description |
| --- | --- |
| [agent-engineering](agent_extensions/registry/@agentxm/knowledge/agent-engineering/src/index.md) | End-to-end design of goal-directed AI agent systems: agent behavior, multi-agent coordination, prompts, context, harness, skills, evaluation, trust, and operations |

### @craigsmitham

<!-- axm:point v=1 ext=@craigsmitham/knowledge/docs kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/effect-v4 kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/field-notes kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/knowledge-management kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/product-engineering kind=knowledge -->

| Bundle | Description |
| --- | --- |
| [docs](knowledge/docs/src/index.md) | Portable documentation craft for authoring, naming, information architecture, auditing, and improving explainers, guides, principles, and evidence-backed patterns |
| [effect-v4](knowledge/effect-v4/src/index.md) | Checklists to consult when designing, implementing, maintaining, or reviewing Effect v4 TypeScript |
| [field-notes](knowledge/field-notes/src/index.md) | Operational field-note practice for preserving factual session friction, observed cost or impact, outcomes, and safe evidence for later analysis |
| [knowledge-management](knowledge/knowledge-management/src/index.md) | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources |
| [product-engineering](knowledge/product-engineering/src/index.md) | Opinionated product-development lifecycle from strategy through operations and maintenance, with shared conceptual foundations |
<!-- axm:end v=1 region=knowledge -->
<!-- axm:start v=1 region=rules ext=@agentxm/rules/instructions gen=bd0c1c6fccf2ca4978a9ef9bb8e6c0217df3620e08c7d4ec9e13ab3ef1bd52fb -->
<!-- axm:point v=1 ext=@craigsmitham/rules/field-notes@1.0.1 kind=rule -->

## Field notes

Record meaningful friction encountered during the task, including failures,
confusing guidance, avoidable rework, missing capabilities, and workarounds—even
when the work succeeds. Use the `field-notes` skill to capture each occurrence
once, then continue the task.

Use only evidence and context already available. Do not investigate, perform
additional analysis, or generate hypotheses or recommendations for the note.
Skip routine steps, expected diagnostic failures, and isolated typing mistakes.
Capture does not expand the task's authority.

When committing or delivering authorized task work, include the field notes
created for that work and check that none were left untracked. Keep unrelated
notes out of the change.
<!-- axm:end v=1 region=rules -->
