---
type: Checklist
title: Filesystem
description: Evaluate whether file and path operations are portable, typed, containment-safe, resource-safe, and replaceable in tests.
tags: [effect, effect-v4, filesystem, path, platform, resource, testing]
status: stable
sources:
  - id: effect-filesystem
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/FileSystem.ts
    title: Effect 4.0.6 FileSystem source
  - id: effect-path
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/Path.ts
    title: Effect 4.0.6 Path source
  - id: applied-alchemy
    resource: https://github.com/alchemy-run/alchemy/blob/ba579a98ea24b41cbf77a89ec8602fe071d5e43a/examples/fly-service/src/worker.ts
    title: Alchemy FileSystem service use at ba579a9
  - id: effect-bytesize
    resource: https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/ByteSize.ts
    title: Effect 4.0.6 ByteSize source
generated: { by: codex/gpt-6, at: 2026-10-27T18:45:50Z }
---

# Filesystem

- [ ] Depend on Effect's `FileSystem` and `Path` services in portable logic;
  provide the Node, Bun, or other platform implementation at the edge.
- [ ] Reject rooted inputs and lexical traversal with `Path.resolveWithin`
  when resolving untrusted relative paths beneath a configured
  root.[^effect-path]
- [ ] Enforce the required symlink policy separately: `resolveWithin` does not
  follow symlinks, `lstat` inspects the link itself, and `open({ noFollow: true })`
  rejects only a final-component symlink on supported platforms.[^effect-filesystem]
- [ ] Keep not-found, permission, invalid-path, and I/O failures typed until the
  boundary that owns their domain meaning.
- [ ] Separate reading bytes or text from decoding the file's format so platform
  and schema failures remain distinguishable.
- [ ] Make overwrite, append, atomic replacement, durability, permissions, and
  directory-creation policy explicit for writes.
- [ ] Scope file handles, watchers, temporary files, and temporary directories
  so they close or disappear on failure and interruption.
- [ ] Avoid ambient current-directory assumptions when a stable base path can be
  configured or supplied.
- [ ] Preserve `bigint` and `Option<bigint>` file metadata at storage and JSON
  boundaries; avoid lossy number coercion and account for runtime precision
  limits.[^effect-filesystem]
- [ ] Test with a controlled filesystem layer, including traversal attempts,
  symlink escapes, absent files, partial failure, cleanup, and platform-relevant
  path cases; custom `FileSystem` implementations include `lstat`.[^effect-filesystem]

## Resources

- [FileSystem source](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/FileSystem.ts)
- [Path source](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/Path.ts)
- [Applied FileSystem service in Alchemy](https://github.com/alchemy-run/alchemy/blob/ba579a98ea24b41cbf77a89ec8602fe071d5e43a/examples/fly-service/src/worker.ts)
- [Byte sizes and filesystem offsets](https://github.com/Effect-TS/effect/blob/effect%404.0.6/packages/effect/src/ByteSize.ts)

[^effect-path]: Effect Path lexical containment contract.
[^effect-filesystem]: Effect FileSystem metadata and symlink contracts.
