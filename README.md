# agent-extensions

Public, reusable agent extensions maintained by
[@craigsmitham](https://github.com/craigsmitham) and managed with
[AXM](https://axm.sh).

This repository is the authoritative source for the packages below. Personal,
machine-specific, and private operational extensions are maintained separately
and are not published from this repository.

## AgentXM-owned extensions

The reusable AI-agent engineering extensions formerly published here have
moved to
[`agentxm/agent-extensions`](https://github.com/agentxm/agent-extensions).
Install the replacement `@agentxm` identities; the previously published
`@craigsmitham` identities are deprecated.

| Type | Moved extensions |
| --- | --- |
| Packs | `@agentxm/packs/agent-engineering`, `@agentxm/packs/context-engineering`, `@agentxm/packs/harness-engineering`, `@agentxm/packs/skill-engineering` |
| Knowledge | `@agentxm/knowledge/agent-engineering`, `@agentxm/knowledge/context-engineering`, `@agentxm/knowledge/eval-engineering`, `@agentxm/knowledge/harness-engineering`, `@agentxm/knowledge/prompt-engineering`, `@agentxm/knowledge/skill-engineering` |
| Skills | `@agentxm/skills/admit-agent-skill`, `@agentxm/skills/audit-agent-skill`, `@agentxm/skills/author-agent-skill`, `@agentxm/skills/evaluate-agent-skill`, `@agentxm/skills/govern-agent-skill-library`, `@agentxm/skills/garden-context`, `@agentxm/skills/improve-instructions` |

## Packs

| Pack | Purpose | Install |
| --- | --- | --- |
| `effect-v4` | Effect v4 guidance: a routing skill plus a knowledge bundle of twenty-two guides for data modeling, services and layers, failure, lifetimes, concurrency, platform integration, and verification | `axm install @craigsmitham/packs/effect-v4` |
| `docs` | Portable documentation craft plus distinct authoring/remediation and read-only audit skills | `axm install @craigsmitham/packs/docs` |
| `field-notes` | Observe how work actually goes within declared subjects, then triage recurring obstacles into verified improvements | `axm install @craigsmitham/packs/field-notes` |
| `gen-stack` | A Change-centered realization process spanning Shape, Research, Investigation, Change Specification and Design, Planning, Implementation with focused review feedback, fresh integrated Review, Shipping, and corpus learning | `axm install @craigsmitham/packs/gen-stack` |

The former `software-architecture` and `software-engineering` packs are
superseded by `gen-stack`. Their final published versions remain available for
reproducibility but should not be used for new adoption.

The former `qrspi` pack and standalone `question` skill are also superseded by
`gen-stack`. Research now owns both concern-aware Research Brief framing and
read-only evidence gathering through the Researcher subagent.

## Standalone knowledge

| Bundle | Purpose | Install |
| --- | --- | --- |
| `knowledge-management` | Durable knowledge authority, lifecycle, discovery, provenance, and maintenance across human and executable sources | `axm install @craigsmitham/knowledge/knowledge-management` |
| `gen-stack` | Cohesive Shape, Intent, Requirements, Architecture, work-item, Implementation, Evaluation, OODA, and regenerative-software guidance | `axm install @craigsmitham/knowledge/gen-stack` |
| `product-management` | Product outcomes, risks, empowered teams, discovery, delivery, evidence, and product strategy | `axm install @craigsmitham/knowledge/product-management` |
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
