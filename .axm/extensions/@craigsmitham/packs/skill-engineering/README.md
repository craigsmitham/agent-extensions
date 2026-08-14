# Skill engineering

Engineer Agent Skills as durable artifacts rather than one-off prompts. This
pack combines portable knowledge with workflows for authoring a skill,
evaluating its behavior, auditing its trust, admitting exact candidates, and
governing a shared library over time.

Use it for the lifecycle of individual Agent Skills and a shared portfolio:
deciding what each skill owns, making activation discoverable, measuring
behavior and coexistence, reviewing authority and executable content, assigning
operational ownership, admitting exact versions, enforcing change control, and
maintaining catalog coherence from evidence.

The pack does not own general harness design, repository context, always-on
instruction files, agent definitions, MCP implementation, or plugin packaging.
Those may constrain a skill, but they are separate engineering surfaces.

## Included extensions

| Extension | Role |
| --- | --- |
| `@craigsmitham/knowledge/skill-engineering` | Concepts and practices for skill boundaries, routing, workflow design, evaluation, trust, governance, portability, and portfolio lifecycle operations |
| `@craigsmitham/skills/author-agent-skill` | Creates or revises a skill from concrete workflow evidence and exercises the resulting package |
| `@craigsmitham/skills/evaluate-agent-skill` | Evaluates routing and execution separately against representative cases and baselines |
| `@craigsmitham/skills/audit-agent-skill` | Reviews a skill statically for quality, portability, authority, provenance, licensing, and supply-chain risk |
| `@craigsmitham/skills/admit-agent-skill` | Makes an independent, portfolio-aware admission or reapproval decision for one exact candidate |
| `@craigsmitham/skills/govern-agent-skill-library` | Assesses ownership, capability policy, lifecycle, coherence, evidence, and utility across a bounded skill library |

The five skills read the shared knowledge bundle and are therefore coupled to
this pack (`standalone: false`). The knowledge bundle may be installed by
itself.

## Lifecycle

```text
observed need -> author -> evaluate -> audit -> admit -> bounded exposure
                    ^         |          |        |             |
                    +--------- evidence and governance ----------+
                                      |
                           govern portfolio -> revise, reapprove,
                                               migrate, or retire
```

Each workflow preserves separation of duties. Evaluation and audit report
evidence without repairing; admission does not self-approve or publish; library
governance does not silently consolidate, revoke, retire, or delete. Findings
return to the smallest responsible workflow and human authority.

## Install

```sh
axm install @craigsmitham/packs/skill-engineering
```

## Example

Ask an agent to turn a repeated workflow into an Agent Skill, evaluate it in
isolation and with its active cohort, audit its capability and supply-chain
surface, decide whether the exact candidate should be admitted, then assess the
library periodically for ownership, evidence, collision, and lifecycle drift.

## License

The skills and pack metadata are MIT licensed. The knowledge bundle is
CC-BY-SA-4.0; see each member manifest for the applicable license.
