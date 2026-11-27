# Software engineering

Install one shared knowledge bundle and the release-engineering skill:

```sh
axm install @craigsmitham/packs/software-engineering
```

The [knowledge index](https://github.com/craigsmitham/agent-extensions/blob/main/knowledge/software-engineering/src/index.md) follows a change from understanding the need to confirming the result in production. Browse by discipline or go directly to a decision such as choosing which components a test should exercise.

For a release decision, ask the release-engineering skill “My change passed locally, then another agent updated the producer on main. Is my consumer ready to land?” It checks which results still apply and what would resolve the compatibility question.

## Migrate to 5.0.0

- **Earlier SWE pack.** Update the pack to 5.0.0 or later. A version constraint holding the pack to 4.x must be updated to admit the new major. Check the installed pack and its two members with `axm show @craigsmitham/packs/software-engineering`.
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

## License

The pack and skill use MIT. The knowledge bundle identifies the Creative Commons licenses for each section.
