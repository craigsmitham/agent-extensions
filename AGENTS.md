# Public agent extensions

- Treat every artifact and metadata field as public. Do not author, commit, or
  document personal or private information; use synthetic examples and fixtures.
- When authoring documentation in a knowledge bundle, follow the
  [docs knowledge bundle](knowledge/docs/src/index.md).
- Keep concepts and guidance coherent across extensions. Resolve contradictory
  terminology or claims before publishing.
- When choosing or changing a package license, apply
  [Licensing public extensions](docs/licensing.md) and preserve published and
  third-party obligations explicitly.

## Extension authoring versus adoption

This repository authors and distributes extension frameworks. The presence of
a skill, subagent, pack, rule, hook, or knowledge bundle here does not mean the
repository adopts that extension's operating model.

Treat an extension being discussed or changed as the subject of authoring,
maintenance, evaluation, or audit, not as an invoked workflow. Use the
artifact-appropriate authoring and evaluation guidance. Do not require an
extension's domain artifacts merely because work concerns that extension's
sources.

Apply an extension's operating model to repository work only when the user
explicitly asks to execute that workflow or repository instructions separately
declare its adoption. Its sources may still be consulted as subject-matter
authority when maintaining the extension.

## Agent Skill evaluation artifacts

For every workspace-authored Agent Skill, keep the versioned evaluation
contract and cases under `skills/<name>/evals/`.
Keep fixtures, graders, and harness inputs there only when they are stable
source. Write routine generated runs under ignored `.work/evals/`; promote only
the minimal decision evidence that must ship with the package.

Validate all authored suites with
`node agent_extensions/agentxm/@agentxm/skills/agent-skill-evaluator/src/scripts/agent-skill-eval.mjs validate`.
Treat routing and activated execution as separate stages, bind evidence to
exact target, suite, runner, adapter, environment, and provenance identities,
and preserve `unknown` and `harness-error` rather than converting missing
evidence into a pass. Version a skill when its evaluation source changes;
evaluation evidence is not audit or release approval.

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
<!-- axm:start v=1 region=rules ext=@agentxm/rules/instructions -->
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
