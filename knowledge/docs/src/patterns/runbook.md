---
type: Pattern
title: Runbook
description: For a bounded operational task with an established procedure, specify repeatable execution with explicit conditions, verification, recovery, and escalation.
tags:
- docs
- runbook
- operations
- maintenance
- incident-response
- verification
- automation
- documentation-pattern
- pattern
- authoring
status: stable
sources:
- id: aws-runbooks
  resource: https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html
  title: AWS — Use runbooks to perform procedures
- id: aws-runbook-branching
  resource: https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-action-branch.html
  title: AWS — Run conditional automation steps
- id: diataxis-how-to
  resource: https://diataxis.fr/how-to-guides/
  title: Diátaxis — How-to guides
generated:
  by: codex/gpt-6
  at: '2026-11-11T17:40:43Z'
---

# Runbook

For a bounded operational task with an established procedure, **specify
repeatable execution with explicit conditions, verification, recovery, and
escalation**.

This pattern describes the reusable document design. A local runbook realizes
it for a particular operational task, with its own evidence and ownership.

## Purpose

An operational task recurs and its desired outcome is known. It may be planned
work, such as deployment, onboarding, or maintenance, or a mitigation selected
during an incident. The reader has the required skills but may be unfamiliar
with this procedure. Accurate execution matters regardless of whether the work
is urgent.

## Design tradeoffs

- **Efficiency versus safety** — readers need to finish promptly while checking
  consequential actions.
- **Precision versus variation** — supported environments and inputs may require
  different steps toward the same outcome.
- **Completeness versus cognitive load** — readers need execution detail without
  unrelated background.
- **Human judgment versus automation** — reliable steps can be automated, while
  remaining decisions and responsibility must be explicit.
- **Current accuracy versus maintenance cost** — system changes can make a
  command, threshold, or prerequisite stale.

To document a procedure and rehearse its failure path, follow
[How to write a runbook](../guides/writing-a-runbook.md).

## When to use

Use a runbook when:

- a bounded task and its desired outcome are known;
- an established procedure covers the supported conditions;
- repeatability, handoff, or operational risk justifies maintaining it; and
- execution and its results can be verified.

## When not to use

- The primary job is assessing a situation and deciding how to respond — use
  [Playbook](playbook.md), then invoke runbooks for selected tasks.
- No established procedure covers the task or current conditions — investigate
  or escalate before claiming a repeatable path.
- The reader is learning the system from zero — provide a tutorial separately.
- The material is only a system inventory — use reference documentation.
- Competent users need only prompts for known actions or a bounded check — use
  a [Checklist](checklist.md), linking procedural detail where needed.

## Terminology

For why checks and branches belong to one bounded task, see
[What a runbook lets an operator repeat](../explainers/runbook.md).

A runbook owns repeatable execution of a bounded task. Explicit branching,
parameterization, multiple participating roles, and automation can all serve
that job. Linearity and the absence of judgment are not defining requirements.
AWS Systems Manager runbooks, for example, support conditional steps based on
inputs or earlier results.[^aws-runbook-branching]

A runbook may stand alone or support several playbooks. Its entry condition can
be a direct task request; incident diagnosis is not a prerequisite for routine
work. See [Playbook](playbook.md#terminology) for the broader terminology
and how the two forms relate.

## Illustrative example

**Roll back checkout deployment** is a runbook supporting the
[checkout response playbook](playbook.md#illustrative-example). Once rollback
is selected, the runbook specifies:

- **Applicability and prerequisites:** the target deployment, approved prior
  version, operator access, and compatibility checks that determine whether
  rollback is available.
- **Execution:** the deployment mechanism, exact local commands and parameters,
  and documented branches for supported deployment states.
- **Verification:** confirmation that the intended version is serving and that
  the required health checks pass.
- **Recovery and handoff:** conditions for stopping, recovery options if the
  deployment fails, and escalation when no supported path remains.

The runbook can complete its deployment task while customer errors persist;
its completion report returns that observation to the playbook for reassessment.
It may also be used during a planned rollback without any incident playbook.
This synthetic outline illustrates the documentation boundary. A usable local
runbook would supply the actual commands, thresholds, and recovery details.

## Sources and examples

- **AWS operational guidance** describes runbooks for specific outcomes,
  including onboarding and deployments, with permissions, error handling,
  ownership, validation, maintenance, and increasing automation. This supports
  routine work as well as incident mitigation.[^aws-runbooks]
- **AWS Systems Manager** implements branching within executable runbooks,
  including choosing steps by operating system. This is a concrete counterexample
  to defining all runbooks as linear text procedures.[^aws-runbook-branching]
- **Diátaxis how-to guidance** supports practical, goal-oriented steps and
  handling real-world variation. It supplies the underlying documentation craft,
  rather than a definition of the playbook/runbook distinction.[^diataxis-how-to]

The bounded-task formulation is this bundle's convention. These sources support
its execution concerns without making the terminology universal.

## Related

- [Playbook](playbook.md) — guides assessment and coordinated response, and may
  invoke a runbook for a selected task.
- [How-to guide](how-to.md) — supplies the underlying procedure craft.
- [Checklist](checklist.md) — supports bounded execution prompts, verification,
  or readiness decisions within or alongside the procedure.
- [Reference](reference.md) — owns inventories and exact
  system facts that a runbook can link instead of duplicating.

[^aws-runbooks]: AWS — Use runbooks to perform procedures.
[^aws-runbook-branching]: AWS — Run conditional automation steps.
[^diataxis-how-to]: Diátaxis — How-to guides.
