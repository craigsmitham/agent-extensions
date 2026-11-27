---
name: release-engineering
description: Design CI/CD workflows or assess whether a software change is ready to land, deploy, expand, or call complete. Use for check placement, concurrent changes to main, release cadence, and verification after deployment.
---

# Release engineering

Help a developer deliver a change and confirm it works for its intended users. Use the repository's actual integration model and release policy. Apply direct-to-main guidance where the team has chosen it.

Unless project instructions specify otherwise, prioritize **speed first, efficiency second, consistency third**. Compare options that provide credible evidence in time for the decision and satisfy required checks. Choose the shortest path to actionable feedback and confirmed delivery across the team, including queueing and rework. For comparable timing, prefer lower resource and attention cost. For comparable cost as well, prefer the more reproducible verdict. Apply a scoped project override only where it governs.

Read the relevant concept in the software-engineering bundle under
`release-engineering/`. For example:

```sh
axm knowledge concepts get '@craigsmitham/knowledge/software-engineering#release-engineering/guides/direct-to-main-delivery'
```

## Design a workflow

For requests about how a team should deliver changes, use `foundations/delivering-a-software-change` to identify the outcome the team wants to improve. Use `guides/direct-to-main-delivery` for check placement, integration, and rollout under concurrent development.

Trace a representative change using the repository instructions, scripts, CI triggers, artifact and deploy configuration, and available observations. Explain the current path and recommend where each consequential check should run, which decision it should block, and how a failure is handled. Tie recommendations to repository commands or facilities and distinguish proposed capabilities from ones already available. Give each verification claim one default place. Account for broader coverage that can safely run later, including when its findings need action. Where placements compete, identify which priority decides and which outcome would show improvement.

## Decide whether a change can advance

For a particular change, start at the decision the developer faces. Use `guides/direct-to-main-delivery` where the decision depends on concurrent integration or deployment from main.

- Establish the intended behavior and audience, the candidate revision or artifact, and what the available results actually exercised. Inspect relevant code, commands, checks and history when available.
- Start with evidence already available. If main advanced, identify the intervening changes and which assumptions they affect. Reuse applicable results. Run a check again where changed inputs, a distinct claim, or a project requirement justifies it. Choose the quickest credible way to resolve the remaining question under the applicable priorities.
- For a deployment or rollout decision, associate the checks with the artifact and target. For completion, look for evidence of the intended behavior in use. If the result is adverse, identify how to contain it and confirm recovery.
- State what can advance now, what supports that judgment, and any observation still needed. Run available in-scope checks to resolve uncertainty. A request for assessment authorizes investigation. Changes to shared state, deployment, or wider exposure follow the user's requested scope and the repository's policy.

Keep routine decisions brief. Seek a specific human judgment when an unresolved product expectation or release tradeoff requires it. Detailed test design belongs with software testing, and incident diagnosis with software operations.
