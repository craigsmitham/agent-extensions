# agent-extensions

Public, reusable agent extensions maintained by
[@craigsmitham](https://github.com/craigsmitham) and managed with
[AXM](https://axm.sh).

This repository is the authoritative source for the packages below. Personal,
machine-specific, and private operational extensions are maintained separately
and are not published from this repository.

## Packs

| Pack | Purpose | Install |
| --- | --- | --- |
| [`codebase-renewal`](./packs/codebase-renewal/README.md) | Six standalone skills for codebase renewal: align with guidance, reconcile duplication and drift, prune unnecessary elements, improve quality, generalize capabilities, and experiment to reduce uncertainty. | `axm install @craigsmitham/packs/codebase-renewal` |
| `effect` | Effect v4 guidance: a rule requiring v4 conventions plus a knowledge bundle of twenty-four concise topic checklists | `axm install @craigsmitham/packs/effect` |
| [`docs`](./packs/docs/README.md) | Documentation craft, checklist patterns, pattern authoring and collections, organization, and audits | `axm install @craigsmitham/packs/docs` |
| `research` | Fresh-context, read-only research framing and evidence gathering with inspectable uncertainty | `axm install @craigsmitham/packs/research` |
| [`software-engineering`](./packs/software-engineering/README.md) | Aggregate of ten discipline collections: migrated knowledge, shared foundations, and placeholder skills | `axm install @craigsmitham/packs/software-engineering` |

## Software-engineering disciplines

Each discipline pack includes its same-named skill and knowledge bundle, plus
`software-engineering-foundations`. All ten skills are placeholders. Knowledge
coverage reflects existing migrated material; release engineering contains only
a placeholder notice. No new domain guidance was authored for this migration.

| Pack | Intended scope |
| --- | --- |
| [`business-analysis`](./packs/business-analysis/README.md) | Business context, strategy, customer progress, and service modeling |
| [`requirements-engineering`](./packs/requirements-engineering/README.md) | Requirements development, specification, review, and maintenance |
| [`architecture-and-design`](./packs/architecture-and-design/README.md) | Software architecture, domain modeling, and design |
| [`software-construction`](./packs/software-construction/README.md) | Software implementation, integration, review, and evolution |
| [`software-testing`](./packs/software-testing/README.md) | Test design, execution, evidence, suite quality, and defect reporting |
| [`release-engineering`](./packs/release-engineering/README.md) | Release preparation, packaging, distribution, deployment, and rollout |
| [`software-operations`](./packs/software-operations/README.md) | Software operation, service reliability, incident response, and recovery |
| [`configuration-and-change-management`](./packs/configuration-and-change-management/README.md) | Software configurations, baselines, change records, and traceability |
| [`project-management`](./packs/project-management/README.md) | Project capabilities, plans, commitments, resources, and progress |
| [`engineering-environment`](./packs/engineering-environment/README.md) | Engineering tools, repository interfaces, workflows, and environments |

Install a discipline with `axm install @craigsmitham/packs/<discipline>`.
The placeholder skills are disabled in this authoring workspace; their packages
remain members of the published packs.

## Standalone knowledge

| Bundle | Purpose | Install |
| --- | --- | --- |
| [`software-engineering-foundations`](./knowledge/software-engineering-foundations/README.md) | Shared concepts, evidence, quality, maintenance, and cross-discipline examples | `axm install @craigsmitham/knowledge/software-engineering-foundations` |

The former `product-engineering` bundle has been distributed across these
collections. The [migration map](./docs/software-engineering-migration.json)
records the source revision, every migrated concept, extracted existing
passages, and retired organizational material.

## Standalone skills

| Skill | Purpose | Install |
| --- | --- | --- |
| [`align`](./skills/align/README.md) | Align a codebase or a specified part with supplied or identified requirements and guidance. | `axm install @craigsmitham/skills/align` |
| [`reconcile`](./skills/reconcile/README.md) | Reconcile a repository or a specified part by resolving unnecessary duplication and unintended divergence in its content. | `axm install @craigsmitham/skills/reconcile` |
| [`improve`](./skills/improve/README.md) | Improve a codebase or a specified part with evidence-backed gains in fitness for its intended purpose. | `axm install @craigsmitham/skills/improve` |
| [`experiment`](./skills/experiment/README.md) | Experiment within a codebase or a specified scope to reduce uncertainty about an engineering question through empirical evidence. | `axm install @craigsmitham/skills/experiment` |
| [`prune`](./skills/prune/README.md) | Prune a codebase or a specified part by removing unnecessary elements and their associated maintenance burden. | `axm install @craigsmitham/skills/prune` |
| `temporal-dates` | JavaScript Temporal type selection, API usage, interoperability, and pitfalls | `axm install @craigsmitham/skills/temporal-dates` |
| `okf` | Author and validate Open Knowledge Format v0.2 bundles | `axm install @craigsmitham/skills/okf` |
| `devops-docs` | Set up, discover, author, and maintain engineering and operations documentation | `axm install @craigsmitham/skills/devops-docs` |
| `improve-whatever` | Evidence-based evaluation through the lens of Philippians 4:8–9 | `axm install @craigsmitham/skills/improve-whatever` |
| `spot-spew` | Spot avoidable maintenance burden from custom or non-idiomatic code and weigh replacing it with adopted capabilities | `axm install @craigsmitham/skills/spot-spew` |
| [`generalize`](./skills/generalize/README.md) | Generalize a codebase or a specified part to support a broader, coherent family of cases. | `axm install @craigsmitham/skills/generalize` |

## Layout

Canonical packages live under:

```text
├── knowledge/
├── packs/
├── rules/
├── subagents/
└── skills/
```

Agent-specific skill directories are AXM-managed projections. Author canonical
content under the root package directories above, not through those
projections. Acquired packages live under `agent_extensions/<source-key>/`.

## Contributing and publishing

Read [AGENTS.md](./AGENTS.md) before changing or adding an extension. Public
content must be portable, rights-cleared, intentionally safe to disclose, and
free of private dependencies or real sensitive data.

Follow [How to review and publish public extensions](./docs/publishing.md) for
the complete commit and release gate. For a catalog-wide registry preflight:

```bash
axm publish --owner @craigsmitham --preview --json
```

## Licensing

Package licenses are declared in each extension manifest and summarized in
[LICENSE.md](./LICENSE.md). The [licensing policy](./docs/licensing.md) defines
the prospective defaults and package-boundary rules. Third-party material and
attribution are recorded in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).
