---
name: setup-gen-stack
description: Plans or establishes the smallest discoverable OKF v0.2 Gen Stack corpus for one or more repository systems, including explicit profile adoption, the required cross-cutting governance kernel, and the governed System Evaluation Approach. Use for initial setup, adoption, initialization, connection, federation, or an explicitly authorized clean migration. Not for choosing missing meaning, maintaining an established corpus, implementing the system, or moving concrete evaluation artifacts into the corpus.
---

# Set up a Gen Stack corpus

Establish a discoverable, authority-aware corpus without inventing semantic
state or generating a speculative taxonomy.

This skill is a non-standalone member of the Gen Stack pack. Always read:

- `knowledge/gen-stack/src/profile/gen-stack-application-profile.md`; and
- `knowledge/gen-stack/src/glossary.md`; and
- `knowledge/gen-stack/src/evaluations/designing-a-system-evaluation-approach.md`.

Read `knowledge/gen-stack/src/architecture/requirements/one-authority-many-witnesses.md` when
mapping existing requirements, tests, implementation, or observations.

## Authority and modes

A setup, adoption, initialize, connect, or migrate request authorizes bounded
changes to the selected corpus roots and canonical persistent repository
instructions. An assess, plan, preview, or recommend request is read-only.
Setup does not authorize choosing system boundaries or desired-state claims
that the available authority has not accepted.

Route maintenance of an established current-profile corpus to
`reconcile-gen-stack`. Route substantive authoring of a known concept to
`author-gen-stack`.

## Workflow

1. **Build an adoption brief.** Identify each accepted documented System and
   one canonical corpus root, the persistent discovery authority, existing
   accepted concepts, proposals, evidence routes, the profile version, and the
   authorities for lifecycle, ownership, decisions, and assurance. Repository
   structure can suggest candidates but cannot accept them.
2. **Choose a playbook.** Bootstrap one clear System; connect a coherent corpus
   already carrying accepted meaning; federate several accepted
   system-to-corpus mappings; perform only explicitly authorized migration
   classes; or recommend when a semantic choice is missing.
3. **Establish the root.** Create `index.md` with `okf_version: "0.2"`, an
   explicit linked adoption of `gen-stack` version `0.1.0`, the documented
   System and corpus root, and links to `system.md`, `lifecycle.md`,
   `ownership.md`, `decisions.md`, `assurance.md`, and `evaluations/index.md`.
4. **Populate the kernel only from accepted authority.** Root concepts are
   cross-cutting context and governance. `system.md` defines subject and
   boundary; the other files define lifecycle, ownership, decision policy, and
   assurance. A bounded absence conclusion needs rationale, consequences, and
   reassessment triggers. A placeholder does not conform.
5. **Establish evaluation governance and discovery.** Create
   `evaluations/index.md` and
   `evaluations/system-evaluation-approach.md` with exact type `System
   Evaluation Approach`. Populate its five profile-required sections only from
   accepted system, assurance, repository, CI, and operational authority. It
   must route to repository-native Definitions, Suites, Executions, Results,
   Reports, and evidence; make evidence navigable by Architecture subject and
   stable Requirement ID; separate Requirement-satisfaction from
   Architecture-realization reporting; and preserve `unknown` and harness
   errors. Do not invent coverage or a physical suite taxonomy.
6. **Connect admitted concepts.** Preserve existing accepted Intent and
   Architecture meaning, use profile-canonical paths when migration is
   authorized, and keep proposals and delivery records in their own lifecycle.
   Do not silently transfer semantic ownership or convert prose into a
   Requirement.
7. **Keep concrete peer authorities out of the corpus.** Do not create corpus
   `implementation/`, `feedback/`, `signals/`, or `observations/` directories,
   and do not place concrete Evaluation Definitions, Suites, Executions,
   Results, or Reports under the required `evaluations/` navigation area.
   Existing code, schemas, tests, evaluation artifacts, and telemetry remain
   at their natural repository or runtime locations and are linked from the
   Approach.
8. **Create only earned collections.** Do not precreate `intent/`,
   `architecture/`, Requirement, ADR, or type directories without an admitted
   concept. Individual ADRs belong under `architecture/decisions/`; the root
   `decisions.md` remains governance.
9. **Add discovery.** Update one canonical persistent instruction route so a
   contributor can map every documented System to its root and discover the
   Gen Stack pack. Preserve unrelated instructions and avoid duplicating the
   shared method.
10. **Verify.** Confirm one root per System, profile adoption, five substantive
   root concepts, the required System Evaluation Approach and navigation,
   reachability, correct concept paths, no copied concrete peer authorities,
   and an effective instruction route. Run the
   established OKF check and
   `knowledge/gen-stack/scripts/validate-gen-stack-profile.py` when safe and
   authorized. Report OKF and profile results separately; neither establishes
   coverage, satisfaction, evaluation coverage, or operational fitness.

## Migration boundary

A clean-break profile migration may move paths and remove old profile identity,
aliases, and compatibility structures when the user authorizes it. It still
MUST NOT choose a new Requirement subject, split or merge concepts, accept an
ADR, create a missing System boundary, or change normative ownership without
the applicable human authority. Preserve unresolved cases as explicit gaps.

## Handoff

Lead with each documented System, canonical root, adopted profile, kernel
status, and discovery route. Then state what existing meaning was preserved,
what changed, which checks ran, and which semantic decisions remain. A
read-only or blocked run must explicitly state that no files changed.
