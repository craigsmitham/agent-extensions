---
name: reconcile-gen-stack
description: Assesses or reconciles an established OKF v0.2 Gen Stack corpus against the current profile, including cross-cutting governance, Intent, Architecture, subject-colocated Requirements, ADRs, and the System Evaluation Approach. Use for review, maintenance, repair, refresh, cleanup, pruning, authorized migration, broken navigation, staleness, duplication, contradiction, or nonconformance. Not for initial adoption, inventing a new concept, choosing architecture, changing implementation, or treating concrete evaluation and operational artifacts as corpus concepts.
---

# Reconcile a Gen Stack corpus

Keep an established corpus coherent, discoverable, current enough to trust,
and small enough to justify maintaining without erasing uncertainty or
silently changing accepted meaning.

This skill is a non-standalone member of the Gen Stack pack. Always read:

- `knowledge/gen-stack/src/profile/gen-stack-application-profile.md`; and
- `knowledge/gen-stack/src/glossary.md`.

Open only the focused Intent or Architecture guide needed for a material
claim. Read `knowledge/gen-stack/src/architecture/requirements/one-authority-many-witnesses.md`
for duplication or contradiction involving Requirements, Implementation,
Evaluations, or Observations.

## Authority and modes

Review, assess, or report requests are read-only. Reconcile, maintain, repair,
refresh, clean up, or prune requests authorize bounded mechanical integrity
repair and unambiguous restoration of already accepted meaning. They do not
authorize semantic addition, deletion, merger, deprecation, reclassification,
changed Requirement subject, changed authority, or changed lifecycle unless
the user explicitly includes that class and scope.

If no explicit current-profile adoption exists, route setup or migration to
`setup-gen-stack`. A known new concept belongs to `author-gen-stack`.

## Workflow

1. **Resolve scope and mode.** Read repository instructions, the corpus root,
   current profile adoption, accepted authorities, and requested system. State
   whether the work is review-only or reconciling.
2. **Establish separate results.** Assess OKF v0.2 conformance and Gen Stack
   profile conformance independently. Do not infer completeness,
   implementation satisfaction, evaluation coverage, or operational fitness.
   Preserve unavailable evidence as `unknown`.
3. **Trace the corpus.** Follow root navigation through the five cross-cutting
   kernel concepts, the System Evaluation Approach, Intent, Architecture,
   Requirements, and ADRs. Inspect only
   repository and runtime evidence needed to evaluate material claims.
4. **Assess canonical ownership.** Check one stable file per concept, exact
   profile type and path, reachability, coherent relationships, and clear
   separation of accepted desired state from proposals, delivery state,
   implementation, and observations.
5. **Assess Requirements.** Check stable unique IDs, one of six types, exactly
   one eligible Architecture subject, subject-colocated path, one normative
   `shall` statement, rationale, and proportionate source or derivation
   traceability. Intent and governance concepts other than System cannot be
   subjects. A test or evaluation that repeats the predicate is a distinct
   witness, not a duplicate obligation.
6. **Assess root governance.** Confirm `system.md`, `lifecycle.md`,
   `ownership.md`, `decisions.md`, and `assurance.md` remain substantive and
   cross-cutting. Individual accepted ADRs belong under
   `architecture/decisions/`. Binding lifecycle, ownership, decision, or
   assurance obligations must be linked `process` Requirements owned by an
   eligible Architecture subject.
7. **Assess evaluation governance and corpus boundaries.** Require
   `evaluations/index.md` and the governed
   `evaluations/system-evaluation-approach.md`. Check its five required
   sections, routes by Architecture subject and Requirement ID, separate
   Requirement-satisfaction and Architecture-realization reports, provenance,
   uncertainty, lifecycle, and gaps. Corpus `implementation/`, `feedback/`,
   `signals/`, and `observations/` collections remain nonconforming, as do
   concrete Evaluation Definitions, Suites, Executions, Results, and Reports
   copied beneath `evaluations/`. Preserve useful artifacts at their
   repository-native or runtime authorities and repair links; do not delete
   evidence merely because it is outside the corpus.
8. **Classify each issue.** Use: base OKF nonconformance, profile
   nonconformance, mechanical repair, accepted semantic maintenance,
   consolidation or removal, authority disagreement, Requirement defect,
   implementation non-satisfaction, evaluation defect or gap, changed
   external condition, unresolved architecture decision, insufficient
   evidence, or no action.
9. **Act only within authority.** Repair unambiguous links, navigation,
   metadata, and path integrity in reconcile mode. Perform semantic moves,
   subject changes, mergers, removals, or clean-break migration only when that
   class is explicitly authorized and the target authority is established.
   Never invent missing meaning merely to clear a finding.
10. **Verify.** Re-run reachability, canonical-path, colocation, evaluation-
    approach, authority, and corpus-boundary checks. Run the established OKF check and
    `knowledge/gen-stack/scripts/validate-gen-stack-profile.py` when safe and
    authorized. Inspect the diff for collateral changes and silent decisions.

## Handoff

Lead with system, corpus root, scope, mode, and separate OKF/profile results.
State explicitly that profile conformance does not establish Requirement
satisfaction, evaluation coverage, or operational fitness, and report those
claims separately when evidence supports them.
Then report repairs and authorized lifecycle changes, retained good practices,
and unresolved semantic, implementation, evaluation, or evidence gaps with
their required authority. A classified failure or `unknown` remains visible;
it is not a successful conformance result.
