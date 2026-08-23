# Set up architecture docs

Plans or establishes the minimal repository-local adoption, navigation,
authority, and agent discovery needed to use Just Enough Architecture Docs.
It classifies the repository before acting, supports one or several explicitly
mapped systems, establishes required OKF v0.2 and software-architecture-docs
profile conformance, and avoids empty documentation trees or substantive
architecture by inference.

Use it when a repository is planning or adopting the practice for the first
time, needs scattered accepted material connected to one canonical root, or
needs several accepted system corpora exposed coherently. Do not use it to
choose an architecture, author substantive desired-state meaning, assess or
repair an established corpus, or maintain existing architecture docs.
Existing unprofiled documentation is preserved as migration input rather than
accepted as an alternative Just Enough Architecture Docs format.

This skill is a non-standalone member of the software-architecture pack because
it loads that pack's software-architecture knowledge.

## Revision 0.4.0

- Requires every completed setup to pass separate OKF v0.2 and current
  software-architecture-docs profile checks.
- Adds a migration playbook for useful legacy architecture material.
- Removes plain Markdown and repository-local profile waivers as valid adoption
  outcomes.

This is a breaking change from `0.3.3`. Existing unprofiled corpora require
setup and any separately authorized identity-changing migration; rollback is to
`0.3.3`.

## Install

```bash
axm install @craigsmitham/packs/software-architecture
```

## Example

> Set up Just Enough Architecture Docs for this repository. Preserve the
> accepted boundary material in place, use the repository's canonical
> instruction route, avoid empty collections, and surface missing lifecycle or
> stewardship context for later authoring.

## License

MIT. The software-architecture knowledge bundle retains its separately declared
license.
