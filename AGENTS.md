# Public agent extensions
- Keep concepts and guidance coherent across extensions. Resolve contradictory
  terminology or claims before publishing.


## Field note subjects

| Subject | Mode | Scope | Target condition | Retire when |
| --- | --- | --- | --- | --- |
| axm-cli-interactions | survey | Sessions that directly run `axm` to complete work in this workspace or manually validate AXM behavior; automated test invocations excluded | — | Recurring notes support a specific target condition, or two triage reviews find no pattern |

<!-- axm:start v=1 region=knowledge ext=@agentxm/knowledge/discovery gen=7cffea455ac5178d84ce39d24a7af48468b650ab8dd725273aefea0bcf548dbe -->
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
<!-- axm:point v=1 ext=@craigsmitham/knowledge/product-engineering kind=knowledge -->

| Bundle | Description |
| --- | --- |
| [docs](knowledge/docs/src/index.md) | Portable documentation craft for authoring, naming, information architecture, auditing, and improving explainers, guides, principles, and evidence-backed patterns |
| [effect-v4](knowledge/effect-v4/src/index.md) | Checklists to consult when designing, implementing, maintaining, or reviewing Effect v4 TypeScript |
| [field-notes](knowledge/field-notes/src/index.md) | Operational field-note practice for factual and diagnostic evidence capture, impact-aware triage, evidence-led findings, and verified corrective action |
| [knowledge-management](knowledge/knowledge-management/src/index.md) | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources |
| [product-engineering](knowledge/product-engineering/src/index.md) | Opinionated product-development lifecycle from strategy through operations and maintenance, with shared conceptual foundations |
<!-- axm:end v=1 region=knowledge -->
<!-- axm:start v=1 region=rules ext=@agentxm/rules/instructions gen=56b79c4851319fe8a9b006aff016de418e238a3725f88b3e25c09df5ea6cd24f -->
<!-- axm:point v=1 ext=@craigsmitham/rules/field-notes@0.2.4 kind=rule -->

## Field notes

Capture useful feedback from ordinary work within declared subjects, so
experience informs improvements to tools, guidance, and workflows. Preserve
meaningful observations—including differences between expected and actual
behavior, even when a later attempt succeeds—with enough evidence to understand
what happened and its outcome. Keep observations factual, protect sensitive
information, and continue the task.

Subjects under observation are declared in the `## Field note subjects` table in
this file. If that section is missing or has no rows, this rule is inactive.
Respect each subject's scope and target condition.

Use `capture.md` alongside the installed field-notes rule source for the record
format and evidence requirements. Capture each occurrence once; exclude routine
successes, your own typos, and speculation without an observed occurrence.
Preserve useful diagnostic evidence before reducing output; never rerun a
mutation merely to recover evidence.

Recording observations does not authorize investigation, remediation, or issue
creation beyond the current task. Report capture in at most one short line at
the end of your response. Raise live correctness, data-loss, or security problems
immediately.

Use the `field-notes` skill to declare subjects, triage notes, or promote findings.
<!-- axm:end v=1 region=rules -->
