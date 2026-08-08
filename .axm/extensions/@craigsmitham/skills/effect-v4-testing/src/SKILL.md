---
name: effect-v4-testing
description: Builds deterministic tests for Effect v4 programs and their lifetimes. Use when tests sleep in real time, mock repeated internals, depend on real services, leak fibers, or are nondeterministic through time, scheduling, randomness, or concurrency—even when Effect test utilities are not yet used. Skip pure synchronous logic already covered by straightforward value tests.
---

# Effect v4 testing

Test observable Effect behavior with controlled services and time.

## Control dependencies

- Supply test implementations through layers at the program boundary.
- Prefer small fakes that model capability behavior over mocks coupled to call order.
- Capture console, clock, and other environmental behavior with their test services.
- Keep one clear runtime boundary per test instead of scattering `runPromise`.

## Make time deterministic

- Never wait on wall-clock sleeps.
- Fork the program that waits, advance `TestClock`, then join and assert.
- Exercise schedules, retries, timeout boundaries, and cancellation with virtual time.
- Ensure background fibers are supervised and complete or are interrupted before the test ends.

## Assert semantics

- Assert successes, typed failures, defects, interruption, and finalization according to the contract.
- Test resource release on both failure and cancellation.
- Test concurrency outcomes without depending on incidental scheduling order.
- Use schema/property generation when invariants span a broad input space.
- Keep integration tests for real adapters, but retain deterministic core tests through service substitution.

Flakiness is usually evidence of an uncontrolled dependency or lifetime, not something to fix with longer delays.
