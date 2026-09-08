# Software engineering

Evidence-backed guidance for reviewing software quality, designing tests at
the narrowest effective level through cross-boundary and browser-dependent
worlds, giving decided behavior an authoritative specification, and shaping
coherent repository execution surfaces. This pack installs one standalone
knowledge bundle and introduces no rules, skills, subagents, hooks, or MCP
servers.

## Included extension

| Extension | Role |
| --- | --- |
| `@craigsmitham/knowledge/product-engineering` | The How to build it section holds outcome-centered codebase review criteria, cross-cutting quality concerns, test-suite quality and architecture guidance, executable-specification authority and lifecycle, review aids, and execution-surface craft |

The `software-engineering` bundle was retired into `product-engineering`, where
its concepts live under `src/engineering/` and carry the `pe-engineering` tag.
Installing this pack therefore brings the whole product-engineering body of
knowledge, not the engineering section alone.

## Install

```bash
axm packs install @craigsmitham/packs/software-engineering
```

## Use it for

- Reviewing a codebase against ten product-quality pillars and explicit
  cross-cutting concerns.
- Assessing test-suite quality separately from product testability.
- Admitting a test deliberately, proving each behavior once at the cheapest
  trustworthy level, and substituting collaborators through explicit seams.
- Designing the smallest representative cross-boundary or end-to-end test
  world for a material integration risk.
- Deciding when interface evidence requires a real browser and choosing a
  focused scope, matrix, and observation contract.
- Deciding which rules earn an authoritative, human-readable specification,
  keeping incidental mechanics out of its text, and keeping it trustworthy
  once accepted.
- Selecting evidence and investigation aids without turning inspection methods
  into quality outcomes.
- Designing task graphs, script surfaces, caching intent, and invocation
  contracts shared by humans, agents, and CI.

The knowledge bundle remains useful and installable on its own, and it also
answers the five questions either side of How to build it.

## License

The pack metadata and README are MIT-licensed. The included knowledge bundle
retains the license declared in its own manifest.
