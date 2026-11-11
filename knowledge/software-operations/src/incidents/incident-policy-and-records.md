---
type: Explanation
title: Incident policy and records
description: Defines current-state-first incident records, attributable chronology, response-policy boundaries, and independent restoration, recovery, and closure.
tags:
- software-operations
status: draft
generated: { by: codex/gpt-6, at: 2026-11-11T19:46:48Z }
sources:
- id: migration-source
  resource: https://github.com/craigsmitham/agent-extensions/blob/c56a54cb5cdb2c14c0d71801709c2b38968c99dd/knowledge/product-engineering/src/delivery/work-items/incidents/index.md
  title: Existing product-engineering material before the discipline migration
- id: prior-recording-operational-incidents
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-operations/src/incidents/recording-operational-incidents.md
  title: Recording Operational Incidents
---

# Incident policy and records

Local incident policy defines response thresholds, severity scales, command,
escalation, communication, and closure authority. The record preserves those
choices and their evidence; creating or editing it does not authorize technical
mitigation, assignments, or public communication. Applied response guidance
in this bundle remains a placeholder.

An incident record identifies the threshold applied, exact incident system and
disclosure boundary, and one independently managed impact and response path.
Related alerts, reports, incidents, and recovery work retain their identities.

## Record contract

The [Operational Incident Record template](operational-incident-template.md)
presents current state before chronology. The current brief identifies affected
service or capability, user or business impact, scope, start time or uncertainty,
response state, active control, and next update. Severity includes its evidence
basis and when it was set or changed.

Coordination records command responsibility, delegated roles, safe channels,
response objectives, decision authority, and transfers or handoffs. It records
who holds responsibility rather than assigning it.

Chronology contains attributable observations, decisions, actions, results, and
communications in time order. Preserve what was known then, distinguishing
hypotheses, confirmed findings, and unavailable evidence; later understanding
must not rewrite earlier knowledge as contemporaneous.

Mitigation and its observed effect, monitoring, restoration, residual impact,
recovery work, rollback state, and validation remain distinguishable. Impact
end, restoration, recovery, and closure can occur at different times and under
different authorities.

Closure records the applicable exit policy, authority, supporting evidence,
residual risk, and reopening trigger. Related Defect Reports, Changes, reviews,
and recovery items can remain open under independent ownership.
