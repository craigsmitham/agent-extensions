# Public agent extensions
- Keep concepts and guidance coherent across extensions. Resolve contradictory
  terminology or claims before publishing.


<!-- axm:start v=1 region=knowledge ext=@agentxm/knowledge/discovery gen=4df15866eba8537bbdcd1a321ef25e6a32648413a5675e107adccffb5ccad366 -->
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
<!-- axm:start v=1 region=rules ext=@agentxm/rules/instructions gen=8db614040e03a64811017c2de20616e59f1d491f5da07337af060204d3c76018 -->
<!-- axm:point v=1 ext=@craigsmitham/rules/field-notes@1.0.0 kind=rule -->

## Field notes

Record meaningful friction encountered during the task, including failures,
confusing guidance, avoidable rework, missing capabilities, and workarounds—even
when the work succeeds. Use the `field-notes` skill to capture each occurrence
once, then continue the task.

Use only evidence and context already available. Do not investigate, perform
additional analysis, or generate hypotheses or recommendations for the note.
Skip routine steps, expected diagnostic failures, and isolated typing mistakes.
Capture does not expand the task's authority.
<!-- axm:end v=1 region=rules -->
