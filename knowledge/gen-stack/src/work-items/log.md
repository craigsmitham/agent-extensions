# Software engineering update log

## 2026-08-26

- **Change Specifications**: Replaced request-centered work-item guidance with
  [Change specifications and delivery
  work](change-specifications-and-delivery-work.md) and [Writing change
  specifications](writing-change-specifications.md); raw requests remain
  Signals or source evidence until a candidate system or Architecture change
  has a recognizable boundary and explicit authority state.
- **Bugs and corrective work**: Added an explainer and authoring guide for
  Bugfix Specifications, defined the boundary from Defects, Defect reports,
  and Bugs, required separate identities so corrective work cannot erase the
  originating report's Signal and Provenance, and distinguished
  observation-facing Defect-report titles from correction-facing Bugfix
  titles.

## 2026-08-25

- **Gen Stack composition**: Made the Gen Stack pack the recommended entry
  point and connected work-item guidance to its single authoritative
  Requirement-impact analysis rather than duplicating that classification in
  every artifact guide.

## 2026-08-24

- **Originating evidence**: Strengthened defect-report provenance so multiple
  occurrences remain individually traceable and monitoring-sourced reports
  retain canonical occurrence identifiers and controlled-access links without
  copying unsafe raw evidence.

## 2026-08-21

- **Operational incidents**: Distinguished impact, service, response,
  understanding, and follow-up state; expanded the live-record guide with
  safe channels, response surfaces, scalable roles, objectives, actions,
  communications, acknowledged handoffs, exit criteria, closure validation,
  and progressive coordination and transition fields.
- **Defect reports**: Reframed defect guidance around reported anomalies,
  static and dynamic evidence, classification, resolution, verification, and
  safe progressive intake; renamed the explainer to [Failures, defects, and
  defect reports](failures-defects-and-defect-reports.md) and the
  guide to [Recording defect reports](recording-defect-reports.md).
- **Source requests**: Reframed request intake around attributable source
  occurrences, normalized analysis, Requirements, and delivery authority. The
  later Change Specification guidance now preserves that material as source
  context without treating raw intake as a first-class change work item.
- **Scope**: Removed software architecture guidance so this bundle now focuses
  on evidence-timed design change and context-rich software work items.

## 2026-08-20

- **Architecture docs**: Added scale-neutral capability, feature, surface,
  domain-context, C4 structural, strategic-evolution, and architecture-doc
  organization guidance for progressive, explicitly related architecture
  views.
- **Work items**: Added [Preserving design and delivery context in software
  work items](preserving-design-and-delivery-context.md), connected
  it to Defect Report and Change Specification authoring, and clarified that brief limits
  never justify trimming supplied technical context.

## 2026-08-15

- **Architecture documentation**: Added the candidate Just Enough Architecture
  Docs pattern and Applying Just Enough Gen Stack guide for
  preserving durable functional, quality, and structural meaning without a
  parallel prose specification.
- **Quality concerns**: Added quality-characteristic guidance to connect
  quality vocabulary to contextual requirements, scenarios,
  architecture significance, and proportionate evidence.
- **Work items**: Added the cross-cutting pair [Work item titles and
  summaries](work-item-titles-and-summaries.md) and [Titling and
  summarizing work items](titling-and-summarizing-work-items.md),
  and gave each type-specific guide a `Summary` section, a pointer from its
  titling step, and a final-check bullet.
- **Work items**: Added paired explainers and guides for operational incident
  records, software Defect Reports, and change work under
  [Software work items](index.md).
- **Principles and patterns**: Reframed
  [YAGNI](../principles/yagni-and-speculative-complexity.md) as a principle
  of timing, optionality, and deferred commitment, and added
  [Tidy First](../patterns/tidy-first.md) as its related just-in-time
  structural-change pattern.
- **Expansion**: Broadened invariant guidance beyond architectural guardrails
  and added a paired invariant-authoring guide.
- **Creation**: Established the bundle with architecture guidance and
  [YAGNI and speculative complexity](../principles/yagni-and-speculative-complexity.md).
