# Release engineering

Deliver a change to a running product and establish that it works for its intended users. This pack helps solo developers and small teams choose tests, keep concurrent changes compatible, deploy a verified revision from main, and follow the result into use.

**Prioritize speed first, efficiency second, and consistency third.** Choose the quickest credible feedback for the team. When timing is comparable, conserve compute and developer attention. When both are comparable, favor reproducibility. Project instructions can change that order. Give each claim one default place to be checked and reuse the result while it applies.

```sh
axm install @craigsmitham/packs/release-engineering
```

## Try it

- **Design the workflow.** “Five agents work in this repository. What should run before pushing, on main, and after deployment?” The skill traces the repository’s commands and triggers and identifies which failures should hold a change.
- **Assess a change.** “My tests passed, but the API changed on main. Is my consumer ready to land?” The skill identifies the assumptions that changed and the check that can settle compatibility.
- **Confirm delivery.** “The deployment succeeded. Can I call this change done?” The skill checks what reached the intended audience and what observation would establish that their task works.

The pack includes the release-engineering skill and its knowledge bundle. The bundle contains the delivery job map and a guide to direct integration without a PR queue. Adopt the guide where that workflow fits. Repository instructions supply local commands, required checks, deploy authority, and rollout policy.

## License

Pack metadata, documentation, and skill are MIT. The knowledge bundle is CC-BY-4.0.
