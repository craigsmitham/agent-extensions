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
| `effect-v4` | Effect v4 patterns for types, services, failures, resources, schemas, concurrency, streams, testing, and observability | `axm install @craigsmitham/packs/effect-v4` |
| `docs` | Diátaxis-oriented documentation knowledge plus one consolidated authoring and review skill | `axm install @craigsmitham/packs/docs` |
| `field-notes` | Observe how work actually goes within declared subjects, then triage recurring obstacles into verified improvements | `axm install @craigsmitham/packs/field-notes` |
| `harness-engineering` | Garden project context, improve agent instructions, and apply harness- and context-engineering knowledge | `axm install @craigsmitham/packs/harness-engineering` |

## Standalone knowledge

| Bundle | Purpose | Install |
| --- | --- | --- |
| `harness-engineering` | Harness and context engineering principles, domain profiles, elements, patterns, practices, and guides | `axm install @craigsmitham/knowledge/harness-engineering` |
| `knowledge-management` | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources | `axm install @craigsmitham/knowledge/knowledge-management` |
| `product-management` | Product outcomes, risks, empowered teams, discovery, delivery, evidence, and product strategy | `axm install @craigsmitham/knowledge/product-management` |
| `software-architecture` | Responsibilities, boundaries, authority, invariants, dependencies, and change in software systems | `axm install @craigsmitham/knowledge/software-architecture` |
| `strategy` | Coherent choices about participation, advantage, capabilities, evidence, and value creation | `axm install @craigsmitham/knowledge/strategy` |
| `workflow-automation` | A platform-agnostic workflow model, vendor mappings, structural patterns, and continuous integration and delivery practices | `axm install @craigsmitham/knowledge/workflow-automation` |

## Standalone skills

| Skill | Purpose | Install |
| --- | --- | --- |
| `temporal-dates` | JavaScript Temporal type selection, API usage, interoperability, and pitfalls | `axm install @craigsmitham/skills/temporal-dates` |
| `author-okf` | Author and validate Open Knowledge Format v0.2 bundles | `axm install @craigsmitham/skills/author-okf` |
| `improve-whatever` | Evidence-based evaluation through the lens of Philippians 4:8–9 | `axm install @craigsmitham/skills/improve-whatever` |

## Layout

Canonical packages live under:

```text
.axm/extensions/@craigsmitham/
├── knowledge/
├── packs/
├── rules/
└── skills/
```

Agent-specific skill directories are AXM-managed projections. Author canonical
content under `.axm/extensions`, not through those projections.

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
[LICENSE.md](./LICENSE.md). Third-party material and attribution are recorded
in [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).
