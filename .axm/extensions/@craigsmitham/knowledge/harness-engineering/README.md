# Harness engineering knowledge

Portable knowledge for designing, evaluating, and maintaining the systems
around agents: their context, runtime, interfaces, state, feedback, and
controls. The bundle separates explanations, goal-oriented guides, reusable
patterns, and recurring operating practices.

Begin with the general harness- and context-engineering disciplines and the
principle of agent legibility. Domain profiles apply those foundations to kinds
of work, starting with software engineering across local, repository-centered,
remote, and distributed runtimes. It also captures reusable structures and
operating disciplines such as progressive disclosure and context gardening.

Harness elements include agent skills, `AGENTS.md`, `CLAUDE.md`, and related
harness surfaces. The knowledge bundle is independently installable. The
harness-engineering pack pairs it with the coupled `garden-context` and
`improve-instructions` workflows.

## Install

```bash
axm install @craigsmitham/knowledge/harness-engineering
```

Install `@craigsmitham/packs/harness-engineering` instead when you also want
the context-gardening and instruction-file workflows.

## Usage

Browse from the bundle index or open a concept directly:

```bash
axm knowledge open harness-engineering foundations/harness-engineering
axm knowledge open harness-engineering foundations/agent-legibility
axm knowledge open harness-engineering elements/agent-skills
axm knowledge open harness-engineering domains/software-engineering/harnesses
axm knowledge open harness-engineering domains/software-engineering/practices/spec-driven-development
axm knowledge open harness-engineering domains/software-engineering/patterns/spec-anchored
axm knowledge open harness-engineering domains/software-engineering/guides/repository-instruction-files
axm knowledge open harness-engineering patterns/progressive-disclosure
axm knowledge open harness-engineering practices/context-gardening
```

The bundle was migrated from the original `@agentxm` package while preserving
its content provenance.

Stable concepts record machine generation and verification events in OKF
frontmatter. Machine confirmation does not claim human review.

## License

MIT.
