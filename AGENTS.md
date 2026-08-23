# Public agent extensions

- Treat every artifact and metadata field as public. Do not author, commit, or
  document personal or private information; use synthetic examples and fixtures.
- When authoring documentation in a knowledge bundle, follow the
  [docs knowledge bundle](.axm/extensions/@craigsmitham/knowledge/docs/src/index.md).
- Keep concepts and guidance coherent across extensions. Resolve contradictory
  terminology or claims before publishing.
- When choosing or changing a package license, apply
  [Licensing public extensions](docs/licensing.md) and preserve published and
  third-party obligations explicitly.

## Agent Skill evaluation artifacts

For every workspace-authored Agent Skill, keep the versioned evaluation
contract and cases under `.axm/extensions/@craigsmitham/skills/<name>/evals/`.
Keep fixtures, graders, and harness inputs there only when they are stable
source. Write routine generated runs under ignored `.work/evals/`; promote only
the minimal decision evidence that must ship with the package.

Validate all authored suites with
`node .axm/extensions/@agentxm/skills/agent-skill-evaluator/src/scripts/agent-skill-eval.mjs validate`.
Treat routing and activated execution as separate stages, bind evidence to
exact target, suite, runner, adapter, environment, and provenance identities,
and preserve `unknown` and `harness-error` rather than converting missing
evidence into a pass. Version a skill when its evaluation source changes;
evaluation evidence is not audit or release approval.

## Field note subjects

| Subject | Mode | Scope | Target condition | Retire when |
| --- | --- | --- | --- | --- |
| axm-cli-interactions | survey | Sessions that directly run `axm` to complete work in this workspace or manually validate AXM behavior; automated test invocations excluded | — | Recurring notes support a specific target condition, or two triage reviews find no pattern |

<!-- axm:start v=1 region=knowledge ext=@agentxm/knowledge/discovery -->
## Knowledge Bundles

### @agentxm

| Bundle | Description |
| --- | --- |
| [agent-engineering](.axm/extensions/@agentxm/knowledge/agent-engineering/src/index.md) | End-to-end design of goal-directed AI agent systems: agent behavior, multi-agent coordination, prompts, context, harness, skills, evaluation, trust, and operations |

### @craigsmitham

| Bundle | Description |
| --- | --- |
| [docs](.axm/extensions/@craigsmitham/knowledge/docs/src/index.md) | Portable documentation craft for authoring, naming, information architecture, auditing, and improving explainers, guides, principles, and evidence-backed patterns |
| [effect-v4](.axm/extensions/@craigsmitham/knowledge/effect-v4/src/index.md) | Opinionated Effect v4 guides for data modeling, services and layers, failure, lifetimes, concurrency, platform integration, and verification |
| [field-notes](.axm/extensions/@craigsmitham/knowledge/field-notes/src/index.md) | Operational field-note practice for factual capture, impact-aware triage, evidence-led findings, and verified corrective action |
| [knowledge-management](.axm/extensions/@craigsmitham/knowledge/knowledge-management/src/index.md) | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources |
| [product-management](.axm/extensions/@craigsmitham/knowledge/product-management/src/index.md) | Product management principles for outcomes, product risks, empowered teams, discovery, delivery, evidence, and product strategy |
| [software-architecture](.axm/extensions/@craigsmitham/knowledge/software-architecture/src/index.md) | Human-first software architecture guidance and the required OKF profile for system context, decisions, constraints, product quality requirements, boundaries, and selected views |
| [software-engineering](.axm/extensions/@craigsmitham/knowledge/software-engineering/src/index.md) | Software engineering guidance for evidence-timed design change and context-rich work items for incidents, defects, and feature delivery |
| [strategy](.axm/extensions/@craigsmitham/knowledge/strategy/src/index.md) | Strategy as coherent choices about participation and advantage, supported by capabilities, value creation, and evidence |
| [workflow-automation](.axm/extensions/@craigsmitham/knowledge/workflow-automation/src/index.md) | Platform-agnostic understanding of workflow automation through a common model, vendor mappings, recurring patterns, and established integration and delivery practices |
<!-- axm:end v=1 region=knowledge -->
<!-- axm:start v=1 region=rules ext=@agentxm/rules/instructions -->
<!-- axm:point v=1 ext=@craigsmitham/rules/use-effect-v4@0.1.0 kind=rule -->

## Use Effect v4

When working with Effect, use Effect v4 APIs and conventions. Do not use Effect
v3 APIs or carry v3 patterns forward; verify ambiguous guidance against current
v4 sources.

<!-- axm:point v=1 ext=@craigsmitham/rules/yagni@0.1.1 kind=rule -->

## YAGNI

Before adding capability, structure, process, or scope for future use, consult
the [YAGNI principle](.axm/extensions/@craigsmitham/knowledge/software-engineering/src/design-and-change/yagni-and-speculative-complexity.md).
Defer the commitment unless it serves a current feature, constraint, invariant,
or concrete risk. If delay would close an option that is costly to recover,
take only the cheapest safe action that preserves it.

<!-- axm:point v=1 ext=@craigsmitham/rules/tidy-first@0.1.1 kind=rule -->

## Tidy First

When current structure materially increases the difficulty or risk of an
authorized software behavior change, consult the [Tidy First
pattern](.axm/extensions/@craigsmitham/knowledge/software-engineering/src/design-and-change/tidy-first.md).
Choose first, after, later, or never. If tidying first, make only the smallest
behavior-preserving change that makes the authorized change easier.

<!-- axm:point v=1 ext=@craigsmitham/rules/field-notes@0.2.0 kind=rule -->

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

### How to record

On the first qualifying incident in a session, read the
[capture instructions](.axm/extensions/@craigsmitham/rules/field-notes/src/capture.md).
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
