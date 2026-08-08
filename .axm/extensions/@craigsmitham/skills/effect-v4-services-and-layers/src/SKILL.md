---
name: effect-v4-services-and-layers
description: Designs Effect v4 service boundaries and Layer graphs. Use when dependencies are threaded through parameters, hidden in globals, difficult to replace in tests, constructed repeatedly, or require other dependencies or managed startup—even when Context or Layer is not yet present. Skip pure helpers, short-lived local values, and data that is not a capability.
---

# Effect v4 services and layers

Model capabilities as services and construction as layers.

## Decide

- Make a service represent a cohesive capability, not an implementation class or a bag of unrelated helpers.
- Put required services in an Effect's environment instead of threading them through every call.
- Use `Context.Service` for capabilities supplied by callers. Use `Context.Reference` only for a genuinely meaningful default.
- Keep business operations in the service contract; keep acquisition, configuration, and dependency wiring in its `Layer`.
- Compose the layer graph once near the application boundary. Provide individual services only at narrow integration or test boundaries.

## Preserve lifetimes

- Use scoped layers for clients, pools, servers, subscriptions, and other acquired resources.
- Rely on layer memoization for shared instances. Use `Layer.fresh` only when independent acquisition is intentional.
- Keep construction failures typed and distinct from operation failures.
- Avoid reading a service while constructing the same service through a circular dependency; split the capability or graph.

## Keep substitution honest

- Supply test implementations through layers rather than branching production code.
- Prefer small contract-compatible fakes over mocks of internal calls.
- Expose the least capability consumers need.

Do not turn pure functions, request data, or every configurable value into a service.
