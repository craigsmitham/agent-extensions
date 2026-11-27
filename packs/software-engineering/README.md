# Software engineering

The pack supports six recurring activities in the life of a software product: **Spec → Design → Implement → Test → Deploy → Operate**. Follow a change from an initial need through delivery to its result in use. A failed test can reopen a design decision. Experience operating the product can reveal the next change or tell the team when it is time to retire a service.

[The software engineering lifecycle](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/software-engineering-lifecycle.md) traces one account recovery change across all six activities. The [knowledge index](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/index.md) links each activity to relevant guidance and also supports browsing by discipline.

Install the shared knowledge bundle and release-engineering skill together.

```sh
axm install @craigsmitham/packs/software-engineering
```

Use the release-engineering skill for decisions that span activities. Ask “My change passed locally, then main advanced. Can it land?” to check whether the integration evidence still holds. Ask “The rollout finished. Can we call the change done?” to connect the deployed revision to the behavior users experienced.

## Migrate to 5.x

- **Earlier SWE pack.** Update the pack to 5.x. For a workspace pinned to 4.1.0, AXM 0.53.1 can report `membership unknown (identity-mismatch)` when changing the pin in place. Record the old selection, run `axm uninstall @craigsmitham/packs/software-engineering`, then run `axm install '@craigsmitham/packs/software-engineering@^5.0.0'`. This replaces the old pack selection and resolves its two current members. Check the installed pack and its two members with `axm show @craigsmitham/packs/software-engineering`.
- **Discipline pack.** Install the SWE pack first. Verify that you can read a moved concept, then uninstall your old pack by its full identity, for example `axm uninstall @craigsmitham/packs/release-engineering`.
- **Direct bundle or placeholder skill.** Install the SWE pack, update saved concept references, then uninstall any retired identity you installed directly. Six placeholder skills are retired. Their subject matter is available in the corresponding discipline directory. Keep the release-engineering skill if you selected it directly.
- **Projects staying on an older pack.** Release-engineering skill 0.1.1 can read its guides from the old release-engineering bundle supplied by release pack 0.2.0 or SWE pack 4.1.0. Historical package versions remain available for pinned workspaces.

For every concept in the final seven discipline bundles, translate
`@craigsmitham/knowledge/<discipline>#<id>` to
`@craigsmitham/knowledge/software-engineering#<discipline>/<id>`.
The suffix is preserved, including the historical release placeholder. For example:

```sh
axm knowledge concepts get '@craigsmitham/knowledge/software-engineering#software-testing/patterns/executable-specifications'
```

For a file bookmark, change `knowledge/<discipline>/src/<path>` to
`knowledge/software-engineering/src/<discipline>/<path>`. This includes assets and the reserved index and log files, which are browsed as files. The mapping covers the seven discipline bundles consolidated in this release. Earlier versions of the historical software-engineering bundle through 2.8.1 had their own layout.

A workspace with a minimum release age may need to wait for these versions to become eligible. To select a just-published version immediately, add `--ignore-release-age` to the install or update command.

## License

The pack and skill use MIT. The knowledge bundle identifies the Creative Commons licenses for each section.
