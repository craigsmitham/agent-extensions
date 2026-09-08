---
type: Explanation
title: Operational Incident Records
description: Explains how one living record coordinates impact, response, restoration, recovery, communication, closure, and independently owned follow-up.
tags: [incident, operational-incident, service-impact, response, restoration, recovery, closure, follow-up, pe-delivery]
generated: { by: claude/opus-5, at: 2026-09-08T00:00:00Z }
---

# Operational Incident Records

An **Operational Incident Record** is one of the three portable work-item
roles defined in the
[Software work-item taxonomy](../software-work-item-taxonomy.md): the durable
living work item for one current or imminent operational-impact case that meets
the consuming organization's coordinated-response threshold. It keeps impact,
current control, objectives, responsibilities, decisions, actions,
communications, chronology, handoffs, exit conditions, and follow-up
recoverable.

## One incident, several states

Operational states change independently:

- impact may begin, change scope, or end;
- a service may be restored before recovery is complete;
- response command may transfer while technical work continues;
- monitoring may continue after mitigation;
- the incident record may close while corrective Changes, review, or recovery
  remain open.

A single host status cannot prove all of these transitions.

## Command and responsibility

Command is a responsibility for maintaining shared situational awareness,
objectives, decisions, and coordination. It is not necessarily a job title or
the person performing mitigation. Record delegated operational,
communications, investigation, and handoff responsibilities using the local
response model.

## Neighboring work

The Incident Record does not need root cause or permanent correction to serve
live response. Preserve related observations, Defect Reports, Changes,
post-incident review, recovery, and follow-up as independently owned records or
artifacts. Link them explicitly without copying their state or closing them
automatically.

## Who owns what

Thresholds, severities, escalation, response roles, communications, and closure
authority have two owners, and the two are not in competition.

| Owner | What it owns |
| --- | --- |
| The consuming organization's incident policy | The local values: the threshold that opens a record, the severity scale, the named roles, the escalation paths, and who may close |
| [How to run it](../../../operations/) | The portable craft behind those values: how severity is reasoned about, how command and communication are run, what ends a response, and what a post-incident review does with the result. That section holds the scope claim; none of the craft is written yet |

This subtree owns neither. It supplies the record contract: what the record must
show about impact, severity, control, objectives, chronology, closure, and
follow-up so that the response stays recoverable after it ends. A guide here may
say that severity and its evidence basis must appear in the record and stay
current. It may not say how a responder should arrive at a severity, run
command, or decide to escalate.
