# Behavioral evaluation cases

Run each prompt in a fresh agent context with the skill and the Gen Stack
pack's knowledge bundles. Do not provide the expected output or assertions to
the test agent. `evals.json` is the machine-readable authority.

The cases cover Defect Report evidence and hypotheses, source-request need
versus solution, bounded proposed and authorized Change Specifications, a
structural Architecture change, a quality-only change, a Bugfix Specification,
an Architecture-document correction without a concrete system Bug, a changing
Incident Record, a brief-only rewrite, and refusal to turn unbounded intake
directly into a Specification or implementation tasks. They also cover faithful
preservation of supplied design and delivery context, absence of invented
context, and linked cross-cutting Design. Provenance cases cover a delayed
Sentry investigation-to-Linear handoff, individually traceable source
occurrences, explicit unavailable evidence, a non-monitoring defect without
irrelevant monitoring fields, persisted-item readback that lost a source link,
and a research summary that must not replace the authoritative source pointer.
Gen Stack cases cover a failed Evaluation that intentionally repeats an
authoritative Requirement, provisional Requirement impact at source intake, an
implementation-only Change Specification whose existing Evaluations must be
rerun, and routing between tracker work and canonical Gen Stack concept
authoring.

The suite passes when the selected artifact matches its lifecycle, facts and
unknowns remain honest, supplied context is retained at its actual authority
state, the brief is derived from the body, every material source remains
traceable or explicitly unavailable, persisted readback is checked, and no
product, Requirement, design, priority, or delivery decision is invented.
