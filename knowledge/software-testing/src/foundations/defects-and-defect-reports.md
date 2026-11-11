---
type: Explanation
title: Defects and Defect Reports
description: Explains how observations, failures, Defects, Defect Reports, investigation, correction, verification, and closure remain distinct.
tags: [defect, defect-report, bug, failure, observation, expectation, diagnosis, correction, verification, software-testing]
generated: { by: codex/gpt-6, at: 2026-11-11T20:13:01Z }
sources:
- id: prior-recording-defect-reports
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-testing/src/defects/recording-defect-reports.md
  title: Recording Defect Reports
- id: prior-triaging-defect-reports
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-testing/src/defects/triaging-defect-reports.md
  title: Triaging Defect Reports
- id: prior-linking-defects-to-corrective-changes
  resource: https://github.com/craigsmitham/agent-extensions/blob/333fc2fe7f67b0520f456efdb107e0730d04e069/knowledge/software-testing/src/defects/linking-defects-to-corrective-changes.md
  title: Linking Defects to corrective Changes
---

# Defects and Defect Reports

An **observation** records something perceived under stated conditions. A
**failure** is an observed inability to perform as required or intended. A
**Defect** is a deficiency in a system or work product relative to an
applicable expectation or intended use. A **Defect Report** is the durable work
item that preserves evidence suggesting one or more Defects may exist.

These concepts do not imply one another automatically. An anomaly may have a
valid explanation. A static finding may establish a Defect without a witnessed
runtime failure. One failure may result from several Defects, and one Defect may
produce several occurrences.

## Expectation and discrepancy

A useful report identifies the relevant expectation or intended use and the
observed discrepancy. The expectation may come from a specification, contract,
decision, policy, documented behavior, supported use, or other recognized
source. If it is uncertain, record the candidate expectation and its authority
rather than manufacturing a definitive requirement.

## Report maturity

The report may mature from received concern, through supported discrepancy and
investigation, to an authorized disposition. That maturity is separate from
priority, assignment, correction, verification, and closure. A tracker label
such as `bug` cannot prove diagnosis.

## Correction and closure

Investigation reduces uncertainty. Correction changes a defective work product
or compensates for an unacceptable effect. Verification gathers bounded
evidence about stated conditions. Closure records an authorized lifecycle
decision. A report can be closed as duplicate, not reproducible under stated
conditions, accepted risk, out of scope, or remediated; those dispositions have
different meanings and evidence needs.

## Evidence and disposition

One report preserves one independently managed discrepancy. Related occurrences
retain separate identities when their impact, evidence, communication, or
closure requires it. A record includes the applicable expectation, observed
result, revision and environment, inputs and trigger, impact, and uncertainty;
the [Defect Report template](../defects/defect-report-template.md) supplies the fallback
presentation.

Reproduction steps are valuable when established and safe, but not universally
required. Static findings, logs, measurements, screenshots, or unavailable
material can be relevant evidence. Preserve provenance and limitations, including
workaround risks. Sensitive evidence belongs in a governed channel with a safe
public synopsis. Severity and priority remain separately authorized metadata.

Triage establishes an attributable classification or explicit unknown,
relationship decisions, and next route. It does not automatically diagnose
root cause, set priority, authorize correction, or close a report. Applicability
depends on the actual version, environment, configuration, and supported use;
title similarity is insufficient evidence for a duplicate decision.

## Corrective Changes

A Change is classified as Bugfix only when evidence establishes a Defect and
its authorized purpose is correction or acceptable compensation. Investigation,
monitoring, risk acceptance, and deferment alone do not establish that purpose.

The report remains an independently recoverable evidence record. The separate
Change links the Defects or reports it remediates and states the corrected or
compensated condition, included and excluded cases, constraints, regression
risks, and acceptance conditions. The applicable expectation remains linked to
its authority. Mixed work shares a Change only when outcome, authority,
delivery, and verification form a coherent boundary.

The Change records delivery and verification. Each report retains its own
disposition and closure policy: a delivered Bugfix does not automatically verify
or close every report, and a closed report does not prove delivery.