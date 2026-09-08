---
type: Guide
title: Analyzing requirement impact
description: Traces a proposed requirement change through sources, dependents, realization, verification, validation, and operations. Use when a requirement change is proposed and its reach across dependents and existing evidence is not yet known.
tags: [impact-analysis, change, traceability, evidence, dependency, pe-solution]
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Analyzing requirement impact

Impact analysis begins with the exact proposed semantic change and follows
typed relationships in both directions.

Consider:

- source needs, goals, rules, decisions, and stakeholder commitments;
- parent, refined, allocated, dependent, conflicting, and sibling requirements;
- terminology, models, interfaces, data, designs, code, configuration, and operations;
- assessments, fixtures, evidence, monitoring, and acceptance claims;
- delivery plans, migrations, releases, support, documentation, and training;
- external obligations, security, safety, privacy, accessibility, and other
  relevant qualities.

For each affected item, record why it may be affected, evidence inspected,
owner, proposed response, and remaining uncertainty. Search is discovery
evidence, not proof that no unlinked dependents exist.

Scale breadth to consequence and coupling. Report the declared search boundary
and inaccessible or missing sources.
