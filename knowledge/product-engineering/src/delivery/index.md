# How to ship it

How does a change reach production safely and predictably?

The path a change travels from accepted work to released software, and the flow
and automation that keep that path honest. This section owns the movement of
change: the record that keeps one concern recoverable while it travels, the
systems that carry it, and the practices that decide how often and how safely it
moves. How the system behaves once change has arrived belongs to
[How to run it](../operations/). Constructing and verifying the change itself
belongs to [How to build it](../engineering/).

## What this section holds today

| Area | Status |
| --- | --- |
| Work management | Populated: [Work items](work-items/) |
| Delivery automation | Populated: [Automation](automation/) |
| Flow | Not yet written |
| Build and release | Partly covered by [Automation](automation/); the rest is not yet written |

## Track the work that travels

- [Work items](work-items/) - The portable craft of Operational Incident
  Records, Defect Reports, and Changes as durable case records: a taxonomy, a
  content contract, evidence and provenance, identity and relationships,
  lifecycle and completion, verification, host mapping, and portable templates
  for each role.

Nothing here prescribes a tracker. Host mapping is treated as an adaptation of a
portable contract onto whatever system a team already runs.

## Automate the path

- [Automation](automation/) - Workflow automation as a field: what an automated
  workflow system coordinates, a portable definition and runtime model,
  recurring patterns such as pipelines, quality gates, and build-once-promote,
  and the practices of continuous integration, delivery, and deployment.

The subtree deliberately holds more than delivery. Provisioning, data
processing, scheduled operational work, and durable application flow are the
cases that keep the model portable, and dropping them would leave continuous
delivery looking like the whole of the field.

## What is not yet written

Flow has no concepts. It would own batch size, branching and integration
strategy, review gates as a queueing decision rather than as a pipeline step,
work in progress, and release cadence. The automation subtree assumes several of
these without owning them: continuous integration is a claim about how often
changes integrate, not about the service that runs the build.

Build and release is only partly covered. [Automation](automation/) owns the
pipeline, the quality gate, and promoting one identifiable artifact through
environments. What remains unwritten is versioning and artifact identity as a
product decision, environment topology, and rollout strategy, meaning the ways
exposure is staged and withdrawn. Continuous deployment names exposure control
and recovery as demands it makes; nothing here yet explains how to meet them.

## Boundaries

| Concern | Owner |
| --- | --- |
| The record contract for an operational incident | [Work items](work-items/incidents/), in this section |
| Detection, response, command, and post-incident review | [How to run it](../operations/), which claims the scope but holds no concepts yet |
| The obligations a Change carries | [Requirements](../solution/requirements/) |
| Constructing and verifying the change | [How to build it](../engineering/) |
| What a repository task means and who may invoke it | [How to build it](../engineering/), as the repository execution surface; [Automation](automation/) states the split in full |
| Model-directed choice and stopping inside an agent boundary | Agent engineering, the design of goal-directed model-driven systems, owned by the separate `agent-engineering` bundle |

The first two rows are one split stated twice, because it is easy to get wrong.
This section owns what an incident record must contain and how it stays
recoverable. It does not own thresholds, severities, escalation, response roles,
or the review that follows an incident.
