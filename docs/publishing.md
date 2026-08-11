# How to review and publish public extensions

This guide shows maintainers how to review changes and preflight a public AXM
release from this repository. Use it before committing or publishing any
package.

## Before you start

- Work only from this public repository.
- Read the root [agent instructions](../AGENTS.md), especially the
  public-by-construction and package-isolation policies.
- Read the `axm` skill and the relevant AXM help for the package type and
  command you will use.
- Know which changed packages are intended for this release.

## Review the complete change

1. Inspect the complete diff, untracked files, generated files, and symlink
   targets.
2. For every changed package, search its content for other extension names,
   FQNs, and canonical extension paths.
3. Treat every cross-extension reference as blocked until one pack manifest
   lists both extensions as direct dependencies, the referencing package sets
   `standalone: false` and names that pack in `recommendedPacks`, and the
   reference uses AXM's canonical cross-extension path. Current installation
   state is not evidence of co-installation.
4. Verify provenance, redistribution rights, attribution, license declarations,
   and synthetic examples manually. Scanners cannot establish these facts.
5. Run the local safety gate:

   ```bash
   scripts/check-public-safety.sh
   ```

Review every finding before continuing.

An unpublished change to a workspace-authored package reports
`workspace/authored-content-unpublished` as an informational finding. This is
the expected pre-publication state: keep the advisory visible, but do not treat
it as a reason to stop the release. Resolve every warning and error before
continuing; strict lint and the complete safety gate still fail on either.

## Version changed packages

Bump every package whose published archive changes. Registry versions are
immutable, so do not reuse a published version.

Preview and then apply the appropriate bump:

```bash
axm version @craigsmitham/skills/example patch --preview
axm version @craigsmitham/skills/example patch
```

Replace the example selector and bump level with the package and compatibility
change being released. Re-run the safety gate after versioning or other
generated-state changes.

## Preflight the publication

Establish the target registry identity before preparing a release:

```bash
axm whoami --json
```

Stop if it is not the intended public publisher. Follow the `axm` skill's
device-code flow if authentication is required; never paste a personal access
token into a transcript.

For an exact release, name every intended package explicitly:

```bash
axm publish @craigsmitham/skills/example --preview --json
```

For a catalog-wide release, select only packages authored here by the public
publisher:

```bash
axm publish --authored --owner @craigsmitham --preview --json
```

Review the JSON result and confirm that the package and dependency selection is
exactly the intended release. Add or remove selectors and repeat the preview
until it is.

## Publish

Run the same reviewed selection without `--preview`. Do not broaden the
selection between preview and publish, and do not publish from a private or
secondary workspace-authored copy.

If a secret was exposed, stop. Revoke or rotate it before any further release
work; deleting the file or rewriting Git history does not undo prior access or
copies.
