# Public agent extensions
- Keep concepts and guidance coherent across extensions. Resolve contradictory
  terminology or claims before publishing.
- Keep markdown files under 300 lines


## Field note subjects

| Subject | Mode | Scope | Target condition | Retire when |
| --- | --- | --- | --- | --- |
| axm-cli-interactions | survey | Sessions that directly run `axm` to complete work in this workspace or manually validate AXM behavior; automated test invocations excluded | — | Recurring notes support a specific target condition, or two triage reviews find no pattern |

<!-- axm:start v=1 region=knowledge ext=@agentxm/knowledge/discovery gen=4cb1e0ec5b17693404a69ae29eb2fb405e492401b3364c1b091a8ae2bf7a33de -->
## Knowledge Bundles

Use `axm knowledge concepts --help` to search, read, and explore these bundles.

### @agentxm

<!-- axm:point v=1 ext=@agentxm/knowledge/agent-engineering kind=knowledge -->

| Bundle | Description |
| --- | --- |
| [agent-engineering](agent_extensions/agentxm/@agentxm/knowledge/agent-engineering/src/index.md) | End-to-end design of goal-directed AI agent systems: agent behavior, multi-agent coordination, prompts, context, harness, skills, evaluation, trust, and operations |

### @craigsmitham

<!-- axm:point v=1 ext=@craigsmitham/knowledge/docs kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/effect-v4 kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/field-notes kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/knowledge-management kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/product-management kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/requirements-engineering kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/software-engineering kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/strategy kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/work-management kind=knowledge -->
<!-- axm:point v=1 ext=@craigsmitham/knowledge/workflow-automation kind=knowledge -->

| Bundle | Description |
| --- | --- |
| [docs](knowledge/docs/src/index.md) | Portable documentation craft for authoring, naming, information architecture, auditing, and improving explainers, guides, principles, and evidence-backed patterns |
| [effect-v4](knowledge/effect-v4/src/index.md) | Checklists to consult when designing, implementing, maintaining, or reviewing Effect v4 TypeScript |
| [field-notes](knowledge/field-notes/src/index.md) | Operational field-note practice for factual and diagnostic evidence capture, impact-aware triage, evidence-led findings, and verified corrective action |
| [knowledge-management](knowledge/knowledge-management/src/index.md) | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources |
| [product-management](knowledge/product-management/src/index.md) | Portable product management for value and demand, product strategy, outcomes, risks, empowered teams, discovery, delivery, and evidence |
| [requirements-engineering](knowledge/requirements-engineering/src/index.md) | Portable requirements engineering for elicitation, analysis, specification, review, traceability, lifecycle, and evidence across project methods and tools |
| [software-engineering](knowledge/software-engineering/src/index.md) | Portable engineering craft for evidence-backed codebase review, test architecture, and coherent repository execution surfaces |
| [strategy](knowledge/strategy/src/index.md) | Strategy as coherent choices about participation, advantage, value, and capabilities, informed by situational awareness and evidence |
| [work-management](knowledge/work-management/src/index.md) | Portable software work-item taxonomy, content contracts, templates, lifecycle, evidence, and tracker-neutral guidance |
| [workflow-automation](knowledge/workflow-automation/src/index.md) | Platform-agnostic understanding of workflow automation through a common model, vendor mappings, recurring patterns, and established integration and delivery practices |
<!-- axm:end v=1 region=knowledge -->
<!-- axm:start v=1 region=rules ext=@agentxm/rules/instructions gen=13f9a5c8cebfaf12084b2a3c55940648fc5518aca247451fdda6c4639e6b3c3e -->
<!-- axm:point v=1 ext=@craigsmitham/rules/use-effect-v4@0.1.1 kind=rule -->

## Use Effect v4

When working with Effect, use Effect v4 APIs and conventions. Do not use Effect
v3 APIs or carry v3 patterns forward; verify ambiguous guidance against current
v4 sources.

<!-- axm:point v=1 ext=@craigsmitham/rules/field-notes@0.2.3 kind=rule -->

## Field notes

Record how work actually goes, so recurring obstacles become durable
improvements instead of repeated friction.

Subjects under observation are declared in the `## Field note subjects` table in
this file. **If that section is missing or has no rows, this rule is inactive —
do nothing.**

### When to record

While doing ordinary work within a declared subject, record one note when:

- reality differs from instructions, documentation, or command output;
- you retry, guess, search, or improvise an undocumented workaround; or
- a `target`-mode subject is blocked from its target condition.

Do not record your own typo, the same incident twice in one session, or
speculation without an observed incident.

### Preserve diagnostic evidence

While working within a declared subject, do not discard safe structured failure
details before deciding whether an interaction qualifies for capture. Inspect
the complete result, preserve the process exit status, and keep result output
separate from diagnostic output. If output must be reduced, retain materially
useful error, request, response, retry, recovery, and affected-artifact fields.
Never retain credentials, authorization material, opaque response bodies, or
other sensitive values. Do not rerun a mutation merely to recover evidence.

### How to record

On the first qualifying incident in a session, read `capture.md` alongside the
installed field-notes rule source.
Append one note for each qualifying incident. Recording it is expected behavior,
not an admission of failure.

### Stay in the work

Log and continue. Do not investigate the note, fix what it describes, open an
issue, or discuss it beyond one short line at the end of your response.

Raise a live correctness, data-loss, or security problem immediately instead of
filing it. Stop to ask only when genuinely blocked on ambiguous architecture,
data model, or destructive scope; name the ambiguity in one sentence with two or
three options.

To declare subjects, triage notes, or promote them into findings, use the
`field-notes` skill. Never do that work inline.
<!-- axm:end v=1 region=rules -->
