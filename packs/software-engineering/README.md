# Software engineering

The pack supports six recurring activities in the life of a software product: **Spec → Design → Implement → Test → Deploy → Operate**. Follow a change from an initial need through delivery to its result in use. A failed test can reopen a design decision. Experience operating the product can reveal the next change or tell the team when it is time to retire a service.

[The software engineering lifecycle](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/software-engineering-lifecycle.md) traces one account recovery change across all six activities. The [knowledge index](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/index.md) links each activity to relevant guidance and also supports browsing by discipline.

Install the shared knowledge bundle and release-engineering skill together.

```sh
axm install @craigsmitham/packs/software-engineering
```

Use the release-engineering skill for decisions that span activities. Ask “My change passed locally, then main advanced. Can it land?” to check whether the integration evidence still holds. Ask “The rollout finished. Can we call the change done?” to connect the deployed revision to the behavior users experienced.

## License

The pack and skill use MIT. The knowledge bundle identifies the Creative Commons licenses for each section.
