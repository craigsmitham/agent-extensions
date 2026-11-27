---
name: delivery
description: >-
  Use when a software change needs to land on main, ship, roll out, or be
  confirmed in use, including questions about whether it can advance.
  Also assess a repository’s path to production or improve its hooks,
  verification, CI, deployment, or release feedback.
---

# Delivery

Guide the current change through **Implement → Land → Release → Confirm**.
“Ship this fix” calls for action. “Can this land?” calls for a readiness
decision. Start at the decision in front of the implementer and follow the
change as far as the request authorizes. Use the same behavior for an ordinary
request and for `$delivery`.

Two named modes work on the **delivery process**. Use `$delivery assess` for
“Where are changes waiting?” and `$delivery improve` for “Make this check
faster.” Route equivalent plain-language requests the same way. Assessing
whether a particular fix is ready is ordinary change guidance.

Use the repository’s actual commands, required checks, permissions, and
release cadence. Choose the fastest path with sufficient evidence for the
decision. When timing is comparable, prefer lower compute and developer
effort. Count queueing and rework in elapsed time.

## Deliver a change

- **Implement.** Establish the intended behavior and audience. Work in a
  checkout, temporary branch, or worktree as appropriate. Exercise the changed
  path. For a reproducible defect, show the original failure and the correction.
- **Land.** The implementer owns integration on shared main. Compare the
  candidate with current main. Keep results whose inputs still hold and check
  interactions affected by intervening changes. Follow the repository’s merge
  policy, resolve conflicts, and verify the landed revision. For a readiness
  question, run the relevant checks and report what can advance.
- **Release.** Deploy or publish the artifact built from a verified main revision
  on the repository’s cadence. Follow an authorized release through rollout to
  its intended audience. Track the revision, target, checks, and rollout order.
  If a scheduled release is pending, identify its trigger and owner.
- **Confirm.** Exercise or observe the intended behavior in use. On an adverse
  result, contain the effect within scope and check recovery. If confirmation
  is pending, state what was observed, what still needs observing, and who
  or what will observe it.

For the delivery model and its measures, use the shared SWE concept
`@craigsmitham/knowledge/software-engineering#release-engineering/foundations/delivering-a-software-change`.
For hook placement, concurrent integration, and rollout decisions, use
`@craigsmitham/knowledge/software-engineering#release-engineering/guides/direct-to-main-delivery`.
Resolve either through host discovery or `axm knowledge concepts get '<reference>'`.

## Assess the path to production

Trace a representative recent change through the requested scope. Connect
configuration to actual commits, check runs, artifacts, deployments, and
observations where available. Keep a process assessment read-only. Use three
parts for the report.

1. **Verdict and scope.** Name the change and what the evidence covers.
   Identify practices worth keeping and consequential delays or coverage gaps
   where the trace supports them.
2. **Observed path.** At each relevant step, identify what ran, on which inputs
   and target, which decision waited, and what failure it could detect. Separate
   queue time from execution when measured. Label configured-only steps and
   missing observations explicitly.
3. **Ranked findings.** Give each actionable finding a number, its evidence,
   the effect on speed, efficiency, or coverage, and a proposed improvement
   with a way to verify it. Show where evidence supports the current placement.
   When a measurement would change the ranking, name it.

## Improve the path to production

Start with a selected finding or the requested outcome. Establish a baseline
from comparable runs or a focused reproduction. Identify which behavior,
failure modes, and required checks the change must still cover. For a design
question, recommend a concrete change and explain how to test it. For an
implementation request, make the bounded change through the normal workflow.

Repeat the relevant workload. Exercise a valid change and a representative
failure the check must still catch, using an isolated fixture when needed.
Report the before-and-after result, verification coverage, and any remaining
production measurement. Distinguish observed gains from expected savings.
