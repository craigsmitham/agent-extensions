# Gen Stack

An opinionated software-change system that uses OODA to carry Signals and
Observations through human-oriented Intent, canonical Requirements,
Architecture, Compilation, Implementation, Evaluations, and operational
learning.

The pack installs one knowledge authority and focused workflows around this
contract:

- a Gen Stack corpus owns cross-cutting system governance, Intent,
  Architecture, and subject-colocated Requirements;
- Requirements are canonicalized Intent and obligate exactly one eligible
  Architecture subject;
- the repository owns Implementation and Evaluations; and
- Signals, Observations, results, and other evidence enter the OODA loop without
  becoming desired state by themselves.

## Included extensions

| Extension | Role |
| --- | --- |
| `@craigsmitham/knowledge/gen-stack` | Gen Stack terminology, profile, authority, change-loop, Implementation, Evaluation, and regeneration guidance |
| `@craigsmitham/skills/author-software-work-items` | Author Change Specifications, Bugfix Specifications, Defect Reports, and Operational Incident Records with explicit Requirement, Architecture, and evidence impact |
| `@craigsmitham/skills/author-gen-stack` | Author one accepted corpus concept or bounded subject |
| `@craigsmitham/skills/setup-gen-stack` | Establish the smallest conforming Gen Stack corpus |
| `@craigsmitham/skills/reconcile-gen-stack` | Assess or reconcile an established corpus |
| `@craigsmitham/rules/yagni` | Defer speculative commitments while preserving costly options cheaply |
| `@craigsmitham/rules/tidy-first` | Consider the smallest useful structural preparation before behavior change |

## Install

```bash
axm install @craigsmitham/packs/gen-stack
```

The current pack uses Gen Stack knowledge `0.6.0`,
`author-software-work-items` `3.0.0`, the `gen-stack` OKF application profile
`0.1.0`, and the `author-gen-stack`, `setup-gen-stack`, and
`reconcile-gen-stack` skill identities. Knowledge `0.6.0` organizes guidance
by the profile's semantic neighborhoods, keeps software work-item guidance at
`src/work-items/`, defines bounded Change Specifications and corrective Bugfix
Specifications as first-class work-item roles, keeps unbounded requests as
Signals or source records, and removes redundant intent-to-feedback and
change-signal reconciliation concepts without treating this explanatory bundle
as an instantiated system corpus. It provides no aliases or compatibility
paths for superseded package, profile, workflow, or concept identities.

## Working model

1. **Observe** Signals and contextual Observations without inferring desired
   state or cause.
2. **Orient** across Intent, Requirements, Architecture, Implementation,
   Evaluations, operations, and Provenance.
3. **Decide** on the smallest authorized hypothesis, including preservation or
   further investigation.
4. **Act** within that authority, then return new evidence to Observe.

Installing the pack does not imply a complete corpus, satisfied Requirements,
automated regeneration, evaluation coverage, or production fitness.

## Attribution and license

The synthesis was influenced by Chad Fowler's
[The Generative Stack](https://chadfowler.com/regenerative-software/3miwhqqvwxc2x/)
and John R. Boyd's
[The Essence of Winning and Losing](https://www.coljohnboyd.com/documents/1995-06-28__Boyd_John_R__The_Essence_of_Winning_and_Losing__PPT-PDF.pdf).
See `THIRD_PARTY_NOTICES.md` for provenance.

The pack metadata and README are MIT-licensed. Each member retains the license
declared in its manifest.
