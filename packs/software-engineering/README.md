# Software engineering

## The software engineering lifecycle

**Spec → Design → Implement → Test → Deploy → Operate**

These six activities recur throughout a product’s life. Spec establishes the behavior someone needs. Design and Implement turn it into a working change. Test supplies evidence while the change takes shape. Deploy puts a known version in its target environment, and Operate reveals what happens in use. That experience can prompt the next change or show when a service is ready to retire. [The software engineering lifecycle](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/software-engineering-lifecycle.md)

## Delivering a software change

**Implement → Land → Release → Confirm**

The implementer follows one change from the first working version to evidence that it solves the problem identified in Spec.

| Step | What the implementer owns |
| --- | --- |
| **Implement** | Build a small change in a checkout, worktree, or temporary branch. Exercise the behavior agreed in Spec. |
| **Land** | Check that the change works with current main, integrate it using the repository’s merge policy, and verify that it reached shared main. |
| **Release** | Deploy or publish the artifact built from a verified main revision. Follow the product’s cadence and rollout controls until the intended audience can use it. |
| **Confirm** | Observe the agreed behavior in use. If a release or observation is pending, identify the remaining step and its owner. |

Verification runs throughout delivery. Choose the fastest path to a confirmed change with sufficient coverage for each decision. Where timing is comparable, prefer lower compute and developer effort. Each repository’s **path to production** supplies the commands, hooks, CI jobs, deployment targets, and observations behind those decisions. Track where changes wait, which checks repeat, and which failures escape to users. [Delivering a software change](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/release-engineering/foundations/delivering-a-software-change.md)

## Use the pack

```sh
axm install @craigsmitham/packs/software-engineering
```

Ask “Can this change land?” or “Ship this fix” and the model can invoke the **delivery** skill directly. Calling `$delivery` uses the same behavior. Use its two named modes to work on the delivery process itself.

- `$delivery assess our path to production` traces a real change, reports what ran and where it waited, and ranks opportunities with supporting evidence.
- `$delivery improve our slow pre-push checks` starts from a baseline and verifies both the time saved and the failures the revised workflow can catch.

Ordinary requests such as “Where are releases waiting?” and “Speed up our pre-push checks” work too.

The shared knowledge bundle supports lookup by activity or by discipline. It covers business analysis, requirements engineering, architecture and design, software testing, release engineering, software operations, and project management. [Knowledge index](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/index.md)

## License

The pack and skill use MIT. The knowledge bundle identifies the Creative Commons licenses for each section.
