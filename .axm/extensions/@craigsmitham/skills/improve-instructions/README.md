# improve-instructions

Audits and improves always-on agent instruction files such as `AGENTS.md` and
`CLAUDE.md`. It identifies duplicated procedures, stale commands, weak routing
triggers, misplaced local detail, and cuts that would accidentally damage
progressive discovery.

Use it to audit, trim, reindex, or localize instruction files. It is not a
general documentation-authoring or feature-implementation skill.

This skill uses the instruction-file doctrine in the harness-engineering
knowledge bundle and is distributed through the harness-engineering pack.

## Install

```bash
axm packs install @craigsmitham/packs/harness-engineering
```

## Example

Ask your agent to audit the root `AGENTS.md` for always-on bloat while
preserving its discovery indexes.

## License

MIT.
