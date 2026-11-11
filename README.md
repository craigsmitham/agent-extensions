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
| [`codebase-renewal`](./packs/codebase-renewal/README.md) | Five standalone skills for codebase renewal: align with guidance, prune unnecessary elements, improve quality, generalize capabilities, and experiment to reduce uncertainty. | `axm install @craigsmitham/packs/codebase-renewal` |
| `effect` | Effect v4 guidance: a rule requiring v4 conventions plus a knowledge bundle of twenty-four concise topic checklists | `axm install @craigsmitham/packs/effect` |
| [`docs`](./packs/docs/README.md) | Documentation craft, checklist patterns, pattern authoring and collections, organization, and audits | `axm install @craigsmitham/packs/docs` |
| `research` | Fresh-context, read-only research framing and evidence gathering with inspectable uncertainty | `axm install @craigsmitham/packs/research` |
| `software-engineering` | Evidence-backed codebase review and coherent repository execution-surface craft, sourced from the `product-engineering` bundle | `axm install @craigsmitham/packs/software-engineering` |
| `work-management` | Consistent Operational Incident Records, Defect Reports, and Changes across repositories and trackers, sourced from the `product-engineering` bundle | `axm install @craigsmitham/packs/work-management` |

## Standalone knowledge

| Bundle | Purpose | Install |
| --- | --- | --- |
| `knowledge-management` | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources | `axm install @craigsmitham/knowledge/knowledge-management` |
| `product-engineering` | An opinionated product-development lifecycle from strategy through operations and maintenance, with shared conceptual foundations | `axm install @craigsmitham/knowledge/product-engineering` |

The `strategy`, `product-management`, `requirements-engineering`,
`software-engineering`, `work-management`, and `workflow-automation` bundles
were retired into `product-engineering`. Surviving concepts live under the
section that owns the question they answer, and each carries a `pe-` section
tag, because a query can be scoped to a bundle but not to a folder. Not all of
them survived. The `workflow-automation` and `strategy` concepts have since
been dropped rather than absorbed, because they summarized public sources that
are better read at the source: "Where to play" now holds its question, its
scope, and its boundaries and nothing else, and delivery automation is once
again claimed scope that has not been written.

## Standalone skills

| Skill | Purpose | Install |
| --- | --- | --- |
| [`align`](./skills/align/README.md) | Align a codebase or a specified part with supplied or identified requirements and guidance. | `axm install @craigsmitham/skills/align` |
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
axm publish --authored --owner @craigsmitham --preview --json
```

## Licensing

Package licenses are declared in each extension manifest and summarized in
[LICENSE.md](./LICENSE.md). The [licensing policy](./docs/licensing.md) defines
the prospective defaults and package-boundary rules. Third-party material and
attribution are recorded in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).
