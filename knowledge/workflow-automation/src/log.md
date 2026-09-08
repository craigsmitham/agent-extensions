# Workflow Automation Update Log

## 2026-09-08

* **Practice boundaries**: Finished the 2026-08-21 split by removing the
  deployment/release/exposure vocabulary and the "not universally preferable"
  argument duplicated between [Continuous
  deployment](practices/continuous-deployment-explainer.md) and [Continuous
  integration, delivery, and
  deployment](practices/continuous-integration-delivery-and-deployment.md). The
  reference now solely owns the comparative vocabulary; the explainer solely
  owns adoption rationale, and each links to the other.
* **Discovery**: Added `Related` sections to [Agents and agentic
  workflows](agents-and-agentic-workflows.md) and the practice-comparison
  reference, which were the only concepts offering a search reader no route
  onward.
* **Index**: Merged the two single-entry groups in the root index into one
  `Patterns and practices` group.

## 2026-08-21

* **Practice boundaries**: Added [Continuous integration, delivery, and
  deployment](practices/continuous-integration-delivery-and-deployment.md) as
  the comparative authority for the three practices and removed the duplicated
  delivery-versus-deployment section from the focused delivery explainer.

## 2026-08-14

* **Agent boundary**: Distinguished deterministic automation, LLM workflows,
  agents, and agents contained within workflows; retained schedules,
  dependencies, durable progress, retries, cancellation, and compensation in
  workflow automation.

## 2026-08-08

* **Creation**: Established the workflow automation model, vendor mappings,
  initial patterns (pipeline, quality gate, build once and promote), and initial
  practices (continuous integration, continuous delivery, continuous
  deployment).
