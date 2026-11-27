---
type: Guide
title: Direct-to-main delivery with parallel agents
description: Choose checks, integrate concurrent work, and confirm a release when developers and agents land changes directly on main and deploy from it.
tags: [continuous-integration, continuous-delivery, trunk-based-development, readiness, deployment, rollout, stale-evidence]
status: draft
sources:
  - id: trunk
    title: Fast, green builds
    resource: https://trunkbaseddevelopment.com/fast-green-builds/
  - id: steinberger
    title: Just Talk To It
    resource: https://steipete.me/posts/just-talk-to-it
  - id: ball
    title: Joy & Curiosity 71
    resource: https://registerspill.thorstenball.com/p/joy-and-curiosity-71
  - id: amp
    title: The Company of the Future
    resource: https://ampcode.com/podcast/season-02/episode-06
  - id: willison
    title: Red/green TDD
    resource: https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/
generated: { by: codex/gpt-6, at: 2026-11-27T17:44:17Z }
---

# Direct-to-main delivery with parallel agents

Use this guide in a repository where developers and agents integrate directly into `main` and deployments originate there. The person or agent responsible for a change chooses when the evidence supports advancing it. They can bring in another developer for a specific uncertainty, such as two plausible interpretations of an API contract. Routine changes can proceed without a PR or a standing review queue.

## Choose a verification strategy

The default order is **speed, then efficiency, then consistency**. Apply a different priority or required check wherever project instructions specify one. For each claim, ask what a failure would change and when the answer is needed. Choose one default verification point. A second run earns its place when an input changed, a different environment answers a distinct question, or project policy requires it.

Consider a compatibility suite that can run on one runner or be split across several. The choice depends on the constraint:

| Leading priority | Placement decision | Benefit and tradeoff |
| --- | --- | --- |
| Speed (pack default) | Split the suite across spare runners if that returns an actionable result sooner. Include the wait imposed on other agents when estimating the gain. | The developer can advance or correct the change sooner, at the cost of extra runner-minutes. |
| Efficiency (project preference) | With metered runners and an acceptable detection window, share one result for the verified candidate and use the cheaper serial run. | Conserves compute. A failure can reach its author later. |
| Consistency (project preference) | If the project calls for a reproducible compatibility verdict on a designated runner, use that environment for the release decision. | Agents can compare results under controlled conditions. Waiting for that runner can extend delivery time. |

Under the default order, if two credible placements finish at roughly the same time, take the cheaper one. If cost is also comparable, choose the more repeatable one. A result already available for the relevant inputs may satisfy all three at once.

## Design the workflow around one real change

Trace a recently shipped change from the author's first check to its effect in production. Inspect the repository instructions, actual commands, CI triggers, artifact and deployment records, rollout controls, and available production observations. Distinguish the workflow the repository runs today from a proposed improvement. Establish which branch and revision supply a deployment, who or what initiates it, which checks are required, and where the result is visible. These repository facts belong in its own instructions or linked operational guidance.

Choose parallel work by the assumptions it shares. An API producer and a consumer can conflict across entirely different files. Coordinate the contract, sequence the changes, or land a compatible intermediate version. Independent fixes can proceed while that happens. Keep each change small enough to test and undo on its own. In a shared checkout, account for uncommitted edits when interpreting a test run and include only the intended changes in the commit. Steinberger describes choosing simultaneous work by the scope of each change and keeping agents’ commits separable.[^steinberger]

## Place checks where their results affect a decision

| Decision | Evidence and placement | What a failure should affect |
| --- | --- | --- |
| Continue implementation or correct it | Exercise the changed path in the developer or agent environment. For a reproducible bug, see the regression check fail for the original reason and pass with the fix. Use a browser, CLI, or real request when that is how the behavior can be observed.[^willison][^ball] | The author can correct the change while the cause is fresh. |
| Integrate with current work | Compare the candidate with current main. Exercise changed contracts and dependencies together. Run the repository’s required pre-integration checks. | Hold the affected change until the evidence supports landing it. |
| Deploy a revision from main | Use evidence valid for the integrated revision and the artifact built from it, including any required CI result. Reuse an applicable candidate result when project policy accepts it. Packaging checks may find missing assets or dependencies that a checkout supplies. | Exclude a failed or unchecked candidate from deployment. Restore a broken main promptly by correcting or reverting the responsible change. |
| Expose the change more widely | Exercise the deployed path with a suitable initial audience and observe the consequence that matters. A smoke request may suffice for a copy edit. A database change under load may need a representative traffic window. | Pause expansion, contain the effect, or correct the release according to what the observation shows. |

A fast private build and a shared integration build can establish different facts.[^trunk] Place longer checks according to what a late failure would cost. If a compatibility test is the only way to catch an unreadable file format before distribution, wait for it before releasing the artifact. A broad exploratory run can proceed in the background when its findings can safely arrive later and someone will act on them. Use a representative test environment when an answer needs deployment configuration or realistic data. Introduce a shared staging environment when its evidence justifies the wait for access.

## Decide what still holds when main advances

Identify the revision and inputs behind a prior result. Compare the intervening changes with the behavior, dependencies, configuration, data, and artifact the check exercised. A new commit by itself tells you little about which claims need revisiting. Carry forward evidence whose assumptions still hold. If an assumption changed, test the interaction on the combined candidate. Keep required repository checks in force.

For example, an agent adds an order summary that reads an API fixture. While its tests run, another agent renames a field in the provider. The formatting tests still describe the summary code. The fixture-based pass establishes how it handled the old response. Run the actual provider and consumer together on the updated candidate and verify the displayed order total. A mismatch calls for a compatible change or a coordinated landing. If the tested candidate lands unchanged and project policy accepts the result, carry it forward. Check any remaining deployment requirements against the integrated revision. If another push wins the race, reconcile with the new tip and reconsider only the assumptions it touches.

## Choose the deployment and release boundary

Tie the deploy decision to a verified main revision and its artifact. If main advances while a build is in flight, promote the artifact whose checks passed. Preserve rollout order so an older job finishing late cannot replace a newer deployment unintentionally. An automatically deployed web service and a CLI distributed on a schedule can share main. Amp describes both cadences and using feature flags or instrumentation to learn from production before expanding a release.[^amp]

Choose exposure according to the cost of a wrong decision and the ability to recover. Use an existing flag, limited audience, or canary when it isolates a meaningful risk. Identify who or what will observe the deployed behavior and which result supports widening, pausing, or restoring it. When access or traffic is missing, state what has been established, what observation remains, and how to obtain it. A successful deployment record establishes which build reached an environment. Completion of the user’s task requires an observation tied to that behavior.

## Three changes through the same workflow

| Change | Before landing | From main through confirmation |
| --- | --- | --- |
| Correct a label on a settings page | Render the affected page with the relevant locale and check that the wording fits. An unrelated backend change leaves that observation useful. | Deploy the verified web artifact on the usual cadence. Open the affected route as the intended user and confirm the label appears. The normal rollout is sufficient if the text can be corrected cheaply. |
| Add an order summary while its provider changes | Exercise the real response through the consumer on the combined candidate. Retain unrelated results. A passing fixture test alone leaves an open compatibility question. | Deploy the compatible integrated revision. Exercise the order-summary path for an eligible account and check its total against the source order. Hold wider exposure if values disagree. |
| Change stored data while old workers are active | Use representative existing records. Exercise old and new readers and writers against the proposed schema. Rehearse interruption and resumption of the backfill. | Land compatible schema expansion first. Backfill incrementally and compare migrated values. Switch reads when evidence supports it and retire the old representation after old consumers are gone. If values diverge, pause writes or the backfill as appropriate, preserve recoverable data, and reconcile affected records. Reverting an application binary leaves persisted writes in place. |

When a release goes wrong, contain the affected path, confirm recovery with the same user-visible observation that revealed the failure, and identify when unrelated releases can resume. Release engineering owns the decision to advance or hold a revision. Draw on testing expertise for the design of a discriminating check and operations expertise for diagnosis and service recovery. Use the [delivery job map](../foundations/delivering-a-software-change.md) to decide whether a workflow change reduced delay, interference, or user impact.

[^trunk]: [Trunk Based Development, Fast, green builds](https://trunkbaseddevelopment.com/fast-green-builds/).
[^steinberger]: [Peter Steinberger, Just Talk To It](https://steipete.me/posts/just-talk-to-it).
[^ball]: [Thorsten Ball, Joy & Curiosity 71](https://registerspill.thorstenball.com/p/joy-and-curiosity-71).
[^amp]: [Quinn Slack and Thorsten Ball, The Company of the Future](https://ampcode.com/podcast/season-02/episode-06).
[^willison]: [Simon Willison, Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/).
