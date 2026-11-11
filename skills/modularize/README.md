# modularize

Modularize a codebase or a specified part around cohesive responsibilities that can evolve independently.

The concise [skill](src/SKILL.md) describes the desired outcome and leaves
methods to the caller and model. Boundaries follow responsibilities and
reasons for change; improvement may involve bringing related knowledge
together or separating independently changing policies.

## Usage

Invoke this skill directly during maintenance with a scope. Automatic model
invocation is disabled through the supported native settings.

```text
$modularize src/billing/ around independently changing responsibilities
$modularize the importer so format changes remain local
```

## Sources and inspiration

Original synthesis of [Robert C. Martin's Single Responsibility
Principle](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)
and [Hunt and Thomas's account of duplicated
knowledge](https://media.pragprog.com/titles/tpp20/dry.pdf). These inform the
balance between cohesion, independent change, and shared knowledge.

## License

MIT. Linked sources retain their respective rights; no source text or code
is vendored in this package.
