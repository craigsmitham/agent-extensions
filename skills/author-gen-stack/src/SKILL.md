---
name: author-gen-stack
description: "Creates or revises explicitly requested concepts in an established OKF v0.2 Gen Stack corpus: cross-cutting System governance, Intent, Architecture, subject-colocated Requirements, and the System Evaluation Approach. Use for offerings, audiences, needs, jobs, value propositions, use cases, subdomains, requirements, capabilities, features, surfaces, DDD, C4, accepted ADRs, lifecycle, ownership, decision policy, assurance, evaluation approach, or corpus organization. Not for initial profile adoption, corpus-wide reconciliation, choosing unaccepted meaning, implementing the system, or authoring concrete repository-native evaluations."
---

# Author Gen Stack concepts

Create the smallest authorized, profile-conforming semantic change. Preserve
one normative owner for each accepted obligation and keep Intent,
Requirements, Architecture, Implementation, Evaluations, and operational
evidence distinct.

This skill is a non-standalone member of the Gen Stack pack. From the active
AXM scope root, always read:

- `knowledge/gen-stack/src/profile/gen-stack-application-profile.md`; and
- `knowledge/gen-stack/src/glossary.md`; and
- the narrowest guide for the requested concept.

Read `knowledge/gen-stack/src/architecture/requirements/one-authority-many-witnesses.md`
when the work distinguishes desired state from implementation, tests,
evaluations, or observations.

The profile is normative for representation. Accepted repository-local
authority governs meaning. If the corpus is not OKF v0.2 or does not explicitly
adopt the current profile, preserve existing material and route the work to
`setup-gen-stack`. Route established corpus-wide integrity or lifecycle work to
`reconcile-gen-stack`.

## Concept routes

| Need | Read from `knowledge/gen-stack/src/` |
| --- | --- |
| System, lifecycle, ownership, decision policy, assurance | matching `governance/documenting-*.md` guide |
| System Evaluation Approach | `evaluations/designing-a-system-evaluation-approach.md` and `evaluations/evaluation-as-bounded-evidence.md` |
| Offering, Audience, Need, Job to Be Done, Value Proposition, Use Case, Subdomain | matching `intent/documenting-*.md` guide |
| Requirement or its six types | `architecture/requirements/documenting-requirements.md`, `architecture/requirements/requirement-classification.md`, then the matching type guide in that directory |
| Capability, Feature, Surface | matching guide under `architecture/{capabilities|features|surfaces}/` |
| Bounded Context or Context Map | matching guide and `architecture/domains/domain-driven-design.md` |
| C4 element or view | matching guide and `architecture/structure/c4-model.md` |
| Accepted architecture decision | `architecture/decisions/documenting-architecture-decision-records.md` |
| Responsibility or invariant analysis | `architecture/reviewing-responsibilities-with-scenarios.md` or the matching concept under `architecture/requirements/` |
| Corpus organization | `profile/gen-stack-application-profile.md` and `glossary.md` |

## Workflow

1. **Resolve scope and authority.** Distinguish authoring from review-only
   work. Read repository instructions, the corpus root and navigation, the
   current profile adoption, the existing subject, and the accepted sources
   needed for the requested meaning. Do not infer accepted desired state from
   code, test results, operational behavior, or a proposal.
2. **Classify the meaning.** Use a root concept for cross-cutting system
   context or governance, Intent for desired outcomes and reasons, Requirement
   for one accepted obligation, Architecture for a durable subject,
   responsibility, boundary, relationship, decision, or response, and the
   System Evaluation Approach for portfolio governance and discovery into
   repository-native assessment evidence.
3. **Choose the canonical owner.** Give each governed concept one stable named
   file. Intent sources may motivate a Requirement but cannot own it. Assign a
   Requirement to exactly one eligible Architecture subject: System,
   Capability, Feature, Surface, Bounded Context, C4 Software System, C4
   Container, or C4 Component. Select the subject whose accepted responsibility
   is obligated, not the source of the intent or the current code location.
4. **Stop at semantic gaps.** If no eligible subject exists, the obligation is
   not accepted, or its owner is disputed, preserve the gap for human judgment.
   Do not use System as a catch-all or invent an Architecture subject to make
   the corpus structurally complete.
5. **Apply the profile boundary.** Author only the governed concept requested
   and create collections only when they contain an authorized concept. Do not
   omit an accepted Requirement because implementation, tests, or runtime
   evidence happen to reveal the same predicate.
6. **Write the concept.** Follow the selected guide and exact profile type and
   path. Preserve Intent in non-binding language. Put one bounded, verifiable
   `shall` statement in a Requirement's `## Requirement` section and its reason
   in `## Rationale`. Let Architecture explain the obligated subject and its
   response without duplicating the obligation.
7. **Preserve peer authorities.** Do not create corpus Implementation,
   Feedback, Signals, or Observations concepts or directories. Within the
   required `evaluations/` area, author only the explicitly requested System
   Evaluation Approach and navigation. Link repository-native Evaluation
   Definitions, Suites, Executions, Results, Reports, and evidence; do not copy
   them into corpus concepts.
   Tests and evaluations may repeat a Requirement predicate while referencing
   its stable `requirement_id`.
8. **Create only earned navigation.** Add the minimum collection indexes needed
   by the admitted concept. Individual ADRs go under
   `architecture/decisions/`; `decisions.md` remains the root governance
   policy. The System Evaluation Approach earns `evaluations/index.md` and root
   navigation but no concrete evaluation subcollections. Do not create empty
   collections or plural catch-all concept files.
9. **Verify.** Check links, reachability, exact type and path, Requirement
   colocation and subject resolution, one normative owner, and absence of
   invented meaning. Run the established OKF check and
   `knowledge/gen-stack/scripts/validate-gen-stack-profile.py` when their
   provenance and effects fit the request. Report OKF, profile, and any
   coverage or satisfaction claim separately; preserve `unknown`.

## Handoff

Lead with the achieved semantic outcome. Name the concept, canonical path,
authority, important relationships, and verification performed. State any
unresolved subject, acceptance, coverage, implementation, evaluation, or
operational gap without turning it into profile nonconformance.

Do not choose an architecture, accept a requirement, change implementation,
author concrete repository-native evaluations, or modify external records unless the
user separately authorized that work.
