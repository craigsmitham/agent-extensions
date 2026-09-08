# Automation

This subtree owns workflow automation as a field: systems that coordinate a
triggered body of work toward an intended outcome, the recurring structural
arrangements those systems take, and the established ways of working they
enable. Continuous integration, continuous delivery, and continuous deployment
are the practices in that field most relevant to [How to ship it](../), and they
are why the field is held here. They are not the edge of the field. The same
model also covers provisioning, data processing, scheduled operational work, and
durable application flow, and those profiles stay in scope because dropping them
would leave the model without the cases that make it portable.

Concepts here explain what these systems and practices are. Goal-oriented
procedures may be added separately as guides when they are warranted.

Every concept sits directly in this folder. Pattern and practice are knowledge
forms, and [the overview](../../overview.md) keeps knowledge form as a facet
carried in tags rather than as a folder, so the headings below group the
concepts without giving any of them a second address.

## Foundations

* [Workflow automation](workflow-automation-explainer.md) - What automated
  workflow systems coordinate, which use cases belong to the field, and how
  workflows, patterns, and practices relate.
* [Workflow model](workflow-model-explainer.md) - A portable definition/runtime
  taxonomy for workflow automation and mappings to the object models of major
  platforms.
* [Agents and agentic workflows](agents-and-agentic-workflows.md) - Distinguishes
  deterministic automation, LLM workflows, agents, and agents contained within
  durable workflows by who controls execution.

## Patterns

Recurring arrangements of workflow elements. A pattern applies within a context,
resolves competing forces, and has consequences rather than being a universal
rule.

* [Pipeline](pipeline-explainer.md) - How a pipeline progresses a change or
  input through dependent work toward an outcome while accumulating evidence
  and confidence.
* [Quality gate](quality-gate-explainer.md) - How a gate controls workflow
  progression with an explicit decision based on evidence, policy, or
  approval.
* [Build once and promote](build-once-promote-explainer.md) - Why delivery
  workflows should produce one identifiable artifact and advance that same
  artifact through validation and target environments.

## Practices

Established ways of working that automation supports but does not, by itself,
establish. A practice is recognized by how changes flow over time, not by a
vendor feature, workflow name, or trigger.

* [Continuous integration, delivery, and deployment](continuous-integration-delivery-and-deployment.md) - Distinguishes continuous integration, continuous delivery, and continuous deployment by the change-flow commitment, evidence, and release decision each practice owns.
* [Continuous integration](continuous-integration-explainer.md) - Why
  continuous integration is the practice of integrating small changes
  frequently and verifying each integration, not merely running a CI service.
* [Continuous delivery](continuous-delivery-explainer.md) - How continuous
  delivery keeps changes releasable through reliable automation while leaving
  release timing as a deliberate decision.
* [Continuous deployment](continuous-deployment-explainer.md) - How continuous
  deployment automatically releases every qualifying change and what that
  demands from validation, exposure, observability, and recovery.

## Dated concepts here

Two concepts in this subtree carry a `stale_after` date, and they are the only
dated concepts in the bundle. Both rest on material that moves faster than the
craft around it, and the date is the obligation that keeps them honest.

| Concept | Date | What to do when it arrives |
| --- | --- | --- |
| [Workflow model](workflow-model-explainer.md) | 2027-02-08 | Recheck the cited platform documentation, then either refresh the mapping table and move the date, or delete the table and keep the portable model |
| [Agents and agentic workflows](agents-and-agentic-workflows.md) | 2027-02-14 | Recheck the cited vendor guidance on agent and workflow forms, then confirm or revise the control-path distinction it draws |

The mapping table in [Workflow model](workflow-model-explainer.md) is the one
place this bundle names vendors at length. It is comparative rather than
prescriptive: it exists to show that vendor nouns do not form one portable
hierarchy, which is the claim the portable model rests on. [The
overview](../../overview.md) permits it under a currency contract and states the
conditions it must keep meeting. Nothing else in this subtree depends on the
table being current, so an unmaintained mapping can be removed without taking
the model with it.

## Boundaries

| Concern | Owner |
| --- | --- |
| Definition, execution, and durable lifecycle of automated workflows | This subtree |
| What a repository task means and who may invoke it | [How to build it](../../engineering/), as the repository execution surface |
| Constructing and verifying the change a workflow carries | [How to build it](../../engineering/) |
| Behavior of the system after a change has arrived | [How to run it](../../operations/) |
| Model-directed choice, replanning, and stopping inside an agent boundary | Agent engineering, the design of goal-directed model-driven systems, owned by the separate `agent-engineering` bundle |

The second row is the line between a repository's execution surface and delivery
automation, and it is easy to blur because a pipeline step and a developer's
terminal often invoke the same command. The execution surface owns what a task
means and who may invoke it. Delivery automation owns when a workflow runs it
and what happens to the result. A workflow that redefines what a check means,
rather than calling the task that already defines it, has crossed into the other
section's territory and produced a second definition of the same check.

The last row is drawn deliberately rather than left implicit. [Agents and
agentic workflows](agents-and-agentic-workflows.md) states which parts of an
agent-containing system this subtree owns and which parts it does not, so that
delivery automation does not quietly absorb agent design.
