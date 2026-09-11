# DevOps docs

Set up, author, consult, and maintain connected operational documentation for
software products. The skill helps product engineers make necessary knowledge
available to collaborators and future maintainers, with explicit accountability,
authoritative references, and maintenance triggers.

## Use

```text
$devops-docs setup
$devops-docs setup providers
$devops-docs maintain providers
$devops-docs maintain github.md
$devops-docs discover who owns the package registry
$devops-docs author — implement the accepted provider changes
```

Choose setup, discover, author, or maintain explicitly, or describe the work
naturally. Scope can name document types, files, directories, or subjects.

Setup and maintain analyze the selected scope and present one final proposal
for feedback. The proposal explains relevant document types, groups suggested
changes by type, and ends with the overall recommendation. It lives only in the
conversation; neither task changes files. Related impacts outside the selected
scope are identified separately.

Discover answers from existing docs with sources and uncertainty. Author creates
or revises records within the requested authority, including implementing an
accepted proposal. An inline draft stays in the conversation.

## Default location

Default to **`/devops/` at the adopting repository's root**. Preserve a coherent
existing layout unless migration is selected. Create only populated type folders:
providers, services, teams, tools, environments, organizations, repositories,
playbooks, runbooks, and measures. The adoption README owns scope and maintenance;
reserved indexes own navigation. Setup proposes the convention and any moves; author applies accepted changes.

Adoption, migration, and maintenance reassess whether local guidance still
needs a document once the skill supplies it. Preserve applicable unique meaning
and human reader needs; redundant guidance may be retired without a successor.
Adoption declarations contain repository-specific decisions and references to
shared guidance.

## Package map

| Read | For |
| --- | --- |
| [Skill](src/SKILL.md) | Routing and execution workflow |
| [Profile](src/references/profile.md) | Versioned common contract and routes to ten type templates |
| [Proposal template](src/templates/plan.md) | Conversational orientation and proposed changes grouped by type |
| [Connected example](src/references/example.md) | A fictional draft Service, Measure, and Runbook |

The canonical AXM package is `@craigsmitham/skills/devops-docs`, version 0.2.0.
`src/` is the portable runtime payload. README is package documentation.
This package has no executable helpers or mandatory runtime sibling dependencies.
When available, `author-docs` contributes documentation craft and `author-okf`
contributes OKF authoring and base validation. Their absence leaves manual checks
available and automated-check limitations explicit.

## Boundaries and evidence

Documentation work does not deploy software, grant access, accept service
commitments, execute procedures, or publish external changes. Documents identify
their sources and limitations; record acceptance is distinct from live health
or successful exercise.

The profile is an application convention over OKF v0.2, not an OKF extension
standard. Profile review is manual. Base validation, profile consistency,
source support, and actual use evidence are distinct results.

## Changes in 0.2.0

Setup, maintenance, and authoring now explicitly support retirement without a
successor after checking unique meaning, human access, and affected references.
The proposal example demonstrates this alongside consolidation.

Profile 0.2.0 limits adoption declarations to local decisions and references.
Before migrating an existing declaration from 0.1.0, remove copied shared
guidance while preserving applicable local meaning and access to needed
instruction. Record types, metadata, and relationships are unchanged. A skill
upgrade does not itself migrate an adopting repository. Keep the prior skill
and declared profile at 0.1.0 if that review is deferred.

Routing and authority are unchanged: setup and maintain propose; author applies
authorized changes. Validation covers package structure and manual consistency;
the package's behavioral evaluation suite remains deferred during design.

License: CC-BY-SA-4.0. Examples are fictional.
