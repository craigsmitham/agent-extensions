---
type: Explanation
title: Incident policy and records
description: The existing boundary between local incident policy, response practice, and the durable incident record.
tags:
- software-operations
status: draft
generated:
  by: codex/gpt-6
  at: '2026-11-11T18:36:09Z'
sources:
- id: migration-source
  resource: https://github.com/craigsmitham/agent-extensions/blob/c56a54cb5cdb2c14c0d71801709c2b38968c99dd/knowledge/product-engineering/src/delivery/work-items/incidents/index.md
  title: Existing product-engineering material before the discipline migration
---

# Incident policy and records

Thresholds, severities, escalation, response roles, communications, and closure
authority have two owners, and the two are not in competition.

| Owner | What it owns |
| --- | --- |
| The consuming organization's incident policy | The local values: the threshold that opens a record, the severity scale, the named roles, the escalation paths, and who may close |
| [Software operations](../index.md) | The portable craft behind those values: how severity is reasoned about, how command and communication are run, what ends a response, and what a post-incident review does with the result. Applied response guidance remains a placeholder |

This subtree owns neither. It supplies the record contract: what the record must
show about impact, severity, control, objectives, chronology, closure, and
follow-up. A guide here may say that severity and its evidence basis must appear
in the record and stay current. It may not say how a responder should arrive at
a severity, run command, or decide to escalate.
