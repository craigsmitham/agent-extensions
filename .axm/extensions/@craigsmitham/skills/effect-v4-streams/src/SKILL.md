---
name: effect-v4-streams
description: Models Effect v4 workflows that produce zero to many values over time. Use for manual async iteration, event or callback consumption, paginated or unbounded input, repeated buffering code, or a multi-value workflow forced into one Effect—even without current Stream usage. Skip single-result operations and small finite collections already handled clearly by ordinary Effect traversal.
---

# Effect v4 streams

Use `Stream` when multiplicity, incremental delivery, or backpressure is part of the contract.

## Shape the pipeline

- Keep a single result in `Effect`; use `Stream` for zero-to-many values over time.
- Adapt queues, pub-sub, async iterables, platform streams, and callbacks at the edge.
- Represent normal completion separately from failure.
- Keep transformations incremental; avoid collecting merely to continue processing.

## Make pressure explicit

- Bound concurrency, buffering, and chunk size from expected producer and consumer rates.
- Choose whether ordering matters before parallelizing.
- Make dropping, sliding, batching, and retry policies visible.
- Apply rate limits and time windows where they express domain or external-system constraints.

## Preserve lifetime

- Scope event listeners, subscriptions, files, sockets, and producer fibers.
- Ensure callback adapters unregister on stream completion or interruption.
- Place retry around the operation that is safe to repeat, not blindly around the entire pipeline.
- Use reusable `Sink` abstractions for meaningful consumers and descend to `Channel` only for custom streaming protocols or low-level composition.

Avoid converting an unbounded stream to an in-memory collection.
