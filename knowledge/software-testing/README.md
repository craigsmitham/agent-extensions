# Software testing

Test design, executable specifications, execution, evidence, suite quality, and defect reporting.

From the project where you want to use this bundle, install the [software-testing pack](https://github.com/craigsmitham/agent-extensions/tree/main/packs/software-testing) to get this bundle and its companion placeholder skill.

```sh
axm install @craigsmitham/packs/software-testing
```

If AXM prompts for project setup, select the agents that should discover the
bundle and enable instruction syncing to give them its lookup route. For
command-line lookup alone, you can leave the agent selection empty.

When deciding which dependencies a test can substitute, open this pattern to identify which failures the test must still distinguish.

```sh
axm knowledge concepts get '@craigsmitham/knowledge/software-testing#patterns/evidence-matched-test-world'
```

The [bundle index](src/index.md) covers seven concepts, including a [testing pattern collection](src/patterns/index.md) on executable specifications, evidence-matched test worlds, and owned test worlds.

Optional readings identify the companion bundle and concept to look up.

## License

CC-BY-SA-4.0. Migrated material retains the previous product-engineering bundle’s license and source attribution.
