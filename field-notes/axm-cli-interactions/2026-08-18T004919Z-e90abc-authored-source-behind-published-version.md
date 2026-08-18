---
id: 2026-08-18T004919Z-e90abc
subject: axm-cli-interactions
key: authored-source-behind-published-version
observed_at: "2026-08-18T00:49:19Z"
session: e90abc
kind: gap
status: open
---

**Expected:** The public repository described as the authoritative publishing source would contain the latest published `@craigsmitham/knowledge/effect-v4` package.
**Observed:** After fast-forwarding `main` to `origin/main`, the authored package was version `0.2.0` and had no `src/sql.md`, while `axm view ... versions --json` reported published `0.3.0` and an AXM-managed registry installation in another workspace was version `0.3.0` with `src/sql.md`.
**Impact:** The requested guide revision could not begin from public `main`; recovery of the published package content was required first. Delay was not measured.
**Recovery:** In progress; use immutable published or installed `0.3.0` content to restore canonical source before authoring `0.3.1`.
**Detected by:** `sed` failed to open the expected public-repository `src/sql.md` during the documented publishing preflight.
**Observed factors:** Public repository `main` matched `origin/main`; registry identity was `@craigsmitham`; `axm knowledge lint` passed the older authored `0.2.0` package.
**Hypothesis:** The `0.3.0` release was published from local authored state that was not subsequently pushed to public `main`.
**Suggests:** A publish postcondition could verify that the package archive matches content reachable from the declared repository default branch.

Evidence: `axm view @craigsmitham/knowledge/effect-v4 versions --json` returned `0.3.0`, `0.2.0`, `0.1.1`, and `0.1.0`; public `knowledge.json` declared `0.2.0`; the separately installed registry package declared `0.3.0` and contained `src/sql.md`.
