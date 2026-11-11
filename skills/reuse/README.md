# reuse

Adapt a codebase or a specified part to use suitable existing capabilities with less maintenance burden.

The concise [skill](src/SKILL.md) describes a coherent adoption of available
capabilities while preserving required behavior, policy ownership, and
operational guarantees. A candidate's fit and total maintenance costs determine
whether substitution is worthwhile.

## Usage

Invoke this skill directly during maintenance with a scope. Automatic model
invocation is disabled through the supported native settings.

An opportunity question requests findings and recommendations without edits:

```text
Where could we $reuse adopted parser capabilities in our import pipeline?
```

A direct change request asks for implementation and verification:

```text
$reuse existing parser capabilities in src/importers/
$reuse the capabilities of our adopted dependencies in the retry implementation
```

## Sources and inspiration

Original synthesis of [Software Engineering at Google's dependency-management
guidance](https://abseil.io/resources/swe-book/html/ch21.html) and
[Sandi Metz's The Wrong Abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction).
These inform attention to ongoing ownership costs, contractual fit, and
preserving independent policies when shared code would entangle them.

## Maintenance companion

`reuse` remains independently installable after software-maintenance 0.2.0.
It is no longer a member of that pack. Install it directly when this specific
outcome is needed:

```bash
axm install @craigsmitham/skills/reuse
```

## License

MIT. Linked sources retain their respective rights; no source text or code
is vendored in this package.
