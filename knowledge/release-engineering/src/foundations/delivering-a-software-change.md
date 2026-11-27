---
type: Explanation
title: Delivering a software change
description: The developer’s job, six decisions along the way, and outcomes for shortening the time from starting a change to confirming it works for its intended users.
tags: [jobs-to-be-done, job-map, cycle-time, release-engineering, parallel-agents]
status: draft
generated: { by: codex/gpt-6, at: 2026-11-27T17:44:17Z }
---

# Delivering a software change

A developer’s job is to **deliver a change to a running product and establish that it works for the people who depend on it**. Work begins when the developer takes up the change. It ends when the intended audience can use it and there is evidence of the intended behavior. A release limited to staff can answer a rollout question while delivery to customers is still pending.

Consider a solo developer or a team of three to five, each developer directing three to five agents. While one agent tests a change, another can alter a contract it relies on. Each addition to the queue can cost the developer time piecing together what was tried, what changed since, and whether anyone followed the release. The progress the developer seeks can be expressed in their voice:

> When several changes are underway and the product is changing underneath each one, I want each change to reach users as soon as there’s enough evidence to proceed, so I can keep work moving and give my attention to the decisions that need me.

## Verification priorities

Unless project instructions specify otherwise, choose among credible ways to verify a change in this order:

1. **Speed.** Minimize the elapsed time to actionable feedback and to confirmed delivery. Count queueing, rework after a late failure, and delays imposed on other changes. Spending more compute is worthwhile when it meaningfully shortens that path.
2. **Efficiency.** When the timing is comparable, choose the option that consumes less runner time, scarce environment capacity, and developer attention. Give each claim one default place to be checked and carry its evidence forward while its assumptions hold.
3. **Consistency.** When timing and resource cost are comparable, favor reproducible results and comparable readiness judgments across agents and environments. A flaky result that takes three reruns also carries a speed and efficiency cost.

Plan comprehensive coverage across the delivery cycle. A check can run later when its result will still arrive in time to act on the failure. A failure that would make a data conversion irreversible needs evidence before conversion. The project can change the ranking for a particular release or environment and specify checks that must run there.

## The job map

These are decisions a developer can delegate. A new observation can reopen an earlier decision. Recovery is conditional on an adverse result.

| Job step | Judgment | Desired outcome |
| --- | --- | --- |
| Define a change that can ship independently | What small result would be useful, how would we recognize it, and which concurrent work does it depend on? | Reduce rework caused by discovering a dependency or misunderstood expectation late. |
| Establish that the change behaves as intended | Where can we exercise the behavior and the failure that matters while the change is still cheap to correct? | Shorten time to actionable feedback. Reduce the chance of accepting a change whose important behavior went unexercised. |
| Establish that it works with concurrent changes | Which assumptions have changed since the last check? Does the combined product still work? | Detect incompatibilities sooner, reduce time lost to a broken integration, and spend fewer runner-minutes rechecking unaffected behavior. |
| Decide whether and how to release | What can advance, for which audience, and which uncertainty would justify waiting or seeking another judgment? | Reduce the time a ready change waits and limit exposure while consequential uncertainty remains. Make comparable readiness decisions for changes with equivalent evidence. |
| Verify the result in use | What observation shows that the intended audience received the change and can complete the affected task? | Shorten time to confirmation. Reduce the chance of declaring success while users still experience the original problem. |
| Correct an adverse result | What will contain the impact, restore the affected behavior, and let unrelated work continue? | Reduce the duration of user impact and the amount of unrelated work interrupted by recovery. |

## How to tell whether delivery improved

Follow a change from **work started** to **behavior confirmed for the intended audience**. If a deployment finishes Tuesday and customers receive the feature Thursday, keep the intervening wait visible. For a change still awaiting confirmation, record where it is waiting. Use comparable changes when examining cycle time, since a copy edit and a data migration carry different uncertainties.

Measure speed with both time to the first actionable result and time to confirmed delivery. Measure efficiency with runner-minutes per delivered change, including repeated checks. Measure consistency by looking for conflicting verdicts on equivalent inputs or different readiness decisions for equivalent changes. Use these signals to explain a delay or compare placements. A single weighted score would hide which priority decided the tradeoff.

Also examine what the workflow costs the developer and the people using the product:

- **Developer attention.** How much time does a developer spend reconstructing readiness? A short account of the revision, observation, and unresolved decision can save another person from repeating the investigation.
- **Interference.** How long does otherwise-ready work wait for an unrelated change, an occupied environment, or a broken integrated build? This helps distinguish slow execution from waiting for access or repair.
- **User impact.** How often does a release require correction, and how long are users affected? Read these alongside cycle time when deciding whether a faster workflow helped.

The map and measures are proposed criteria. A team can examine a recent slow change and a recent failed release to find which criteria deserve attention in its repository. For decisions about check placement, integration, and rollout in a direct-to-main workflow, use [Direct-to-main delivery with parallel agents](../guides/direct-to-main-delivery.md).
