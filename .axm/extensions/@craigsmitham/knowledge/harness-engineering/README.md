# Harness engineering knowledge

Portable knowledge for designing, evaluating, and maintaining the system
around an agent: runtime, interfaces, state, feedback, authority, containment,
and operating environment. Context is one harness responsibility, but its
detailed selection, routing, memory, and lifecycle practices belong to the
separate context-engineering discipline.

Begin with harness engineering, agent-system composition, and classification,
then inspect agent legibility and the concrete system responsibilities under
harness elements. Domain and environment profiles apply those foundations to
recognizable work and ownership boundaries, including coding harnesses and
repository harnesses.

For context surfaces and Agent Skills, this bundle owns only their place in the
whole system. Their detailed design and lifecycle belong to their respective
engineering disciplines. The knowledge bundle is independently installable.
The harness-engineering pack remains a compatibility umbrella for the broader
harness and context toolset.

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
axm knowledge open harness-engineering foundations/agent-system-composition
axm knowledge open harness-engineering foundations/harness-classification
axm knowledge open harness-engineering foundations/agent-legibility
axm knowledge open harness-engineering elements/action-and-observation-interfaces
axm knowledge open harness-engineering elements/runtime-and-environments
axm knowledge open harness-engineering elements/feedback-and-verification
axm knowledge open harness-engineering elements/authority-and-containment
axm knowledge open harness-engineering domains/software-engineering/harnesses
axm knowledge open harness-engineering domains/software-engineering/repository-harnesses
axm knowledge open harness-engineering operations/evaluating-and-improving-harnesses
```

The bundle was migrated from the original `@agentxm` package while preserving
its content provenance.

Stable concepts record machine generation and verification events in OKF
frontmatter. Machine confirmation does not claim human review.

## License

MIT.
