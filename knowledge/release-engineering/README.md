# Release engineering

This placeholder reserves space for guidance on release preparation, packaging, distribution, deployment, and rollout. It currently contains only a scope notice.

From the project where you want to use this bundle, install the [release-engineering pack](https://github.com/craigsmitham/agent-extensions/tree/main/packs/release-engineering) to get this bundle and its companion placeholder skill.

```sh
axm install @craigsmitham/packs/release-engineering
```

If AXM prompts for project setup, select the agents that should discover the
bundle and enable instruction syncing to give them its lookup route. For
command-line lookup alone, you can leave the agent selection empty.

Read the installed bundle's [scope notice](src/placeholder.md) from the same project.

```sh
axm knowledge concepts get '@craigsmitham/knowledge/release-engineering#placeholder'
```

## License

CC-BY-4.0. This package currently contains scope and placeholder metadata only.
