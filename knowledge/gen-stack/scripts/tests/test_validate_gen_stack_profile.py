from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote


VALIDATOR_PATH = Path(__file__).parents[1] / "validate-gen-stack-profile.py"
PACKAGE_ROOT = Path(__file__).parents[2]
BUNDLE_SRC = PACKAGE_ROOT / "src"
PROFILE_PATH = BUNDLE_SRC / "profile" / "gen-stack-application-profile.md"
GLOSSARY_PATH = BUNDLE_SRC / "glossary.md"
SPEC = importlib.util.spec_from_file_location("gen_stack_profile", VALIDATOR_PATH)
assert SPEC is not None and SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

from gen_stack_profile.frontmatter import replace_relationships


REQUIRED = {
    "system.md": "System",
    "lifecycle.md": "System Lifecycle",
    "ownership.md": "System Ownership",
    "decisions.md": "Architecture Decision Policy",
    "assurance.md": "System Assurance",
}


def concept(concept_type: str, title: str = "Synthetic concept") -> str:
    return f"""---
type: {concept_type}
title: {title}
description: A synthetic concept used to validate the profile checker.
status: stable
---

# {title}

Accepted synthetic meaning with an authority, consequence, and review trigger.
"""


def requirement(
    requirement_id: str = "SYN-REQ-0001",
    requirement_type: str = "functional",
    requirement_lifecycle: str | None = "active",
    subject: str = "/system.md",
    extra: str = "",
) -> str:
    lifecycle_field = (
        f"requirement_lifecycle: {requirement_lifecycle}\n"
        if requirement_lifecycle is not None
        else ""
    )
    return f"""---
type: Requirement
title: Preserve accepted state
description: A failed operation leaves accepted state unchanged.
status: stable
requirement_id: {requirement_id}
requirement_type: {requirement_type}
{lifecycle_field}subject: {subject}
{extra}---

# Preserve accepted state

## Requirement

When an operation fails, the System shall leave accepted state unchanged.

## Rationale

Partial state would make the outcome ambiguous.
"""


def evaluation_approach() -> str:
    return """---
type: System Evaluation Approach
title: Synthetic system evaluation approach
description: How synthetic evaluations are discovered, navigated, reported, and maintained.
status: stable
---

# Synthetic system evaluation approach

## Scope and objectives

The approach covers the synthetic System and supports assurance review.

## Evaluation portfolio

Repository-native definitions and suites use explicit Evaluation Roles.

## Navigation and reporting

Subject and Requirement views separate satisfaction from realization.

## Evidence and lifecycle

Results preserve provenance, unknown, failures, and review triggers.

## Gaps and maintenance

Known coverage gaps remain visible and have a maintenance route.
"""


class ProfileValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repository_root = Path(self.temp.name)
        self.root = self.repository_root / "gen-stack"
        self.root.mkdir()
        self.write_valid_kernel()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_valid_kernel(self) -> None:
        links = []
        for filename, concept_type in REQUIRED.items():
            title = concept_type
            (self.root / filename).write_text(concept(concept_type, title), encoding="utf-8")
            links.append(f"- [{title}]({filename})")
        evaluations = self.root / "evaluations"
        evaluations.mkdir()
        (evaluations / "index.md").write_text(
            "# Evaluations\n\n- [System evaluation approach](system-evaluation-approach.md)\n",
            encoding="utf-8",
        )
        (evaluations / "system-evaluation-approach.md").write_text(
            evaluation_approach(), encoding="utf-8"
        )
        links.append("- [Evaluations](evaluations/)")
        (self.root / "index.md").write_text(
            """---
okf_version: "0.2"
---

# Synthetic Gen Stack corpus

This documentation set adopts the
[gen-stack profile](https://example.test/profile) version 0.4.0.

"""
            + "\n".join(links)
            + "\n",
            encoding="utf-8",
        )

    def rules(self) -> set[str]:
        report = VALIDATOR.validate(self.repository_root)
        return {item["rule"] for item in report["errors"]}

    def sync_relationships(self) -> None:
        analysis = VALIDATOR.analyze_relationships(self.root)
        blocking = [
            item for item in analysis.diagnostics if item.rule != "relationship-projection"
        ]
        self.assertEqual([], blocking)
        for relative in analysis.projection_paths:
            replace_relationships(
                analysis.concepts[relative].path,
                analysis.expected.get(relative, {}),
            )

    def add_system_requirement(self, body: str | None = None) -> Path:
        subject = self.root / "system"
        requirement_root = subject / "requirements"
        functional = requirement_root / "functional"
        functional.mkdir(parents=True)
        (subject / "index.md").write_text(
            "# System details\n\n- [Requirements](requirements/)\n", encoding="utf-8"
        )
        (requirement_root / "index.md").write_text(
            "# System requirements\n\n- [Functional](functional/)\n", encoding="utf-8"
        )
        (functional / "index.md").write_text(
            "# Functional requirements\n\n- [Preserve accepted state](preserve-state.md)\n",
            encoding="utf-8",
        )
        path = functional / "preserve-state.md"
        path.write_text(body or requirement(), encoding="utf-8")
        with (self.root / "system.md").open("a", encoding="utf-8") as system:
            system.write("\n[System requirements](system/requirements/)\n")
        return path

    def test_minimal_required_kernel_passes(self) -> None:
        report = VALIDATOR.validate(self.repository_root)
        self.assertEqual("pass", report["structural_result"])
        self.assertEqual("conforming", report["state"])
        self.assertEqual("unknown", report["semantic_result"])
        self.assertEqual("0.4.0", report["profile"]["version"])
        self.assertEqual(str(self.repository_root.resolve()), report["repository_root"])
        self.assertEqual(str(self.root.resolve()), report["corpus_root"])

    def test_missing_gen_stack_directory_is_absent(self) -> None:
        relocated = self.repository_root / "docs" / "gen-stack"
        relocated.parent.mkdir()
        self.root.rename(relocated)
        report = VALIDATOR.validate(self.repository_root)
        self.assertEqual("absent", report["state"])
        self.assertEqual("fail", report["structural_result"])
        self.assertEqual("corpus-not-adopted", report["errors"][0]["rule"])

    def test_repository_root_corpus_is_explicitly_unsupported(self) -> None:
        for child in list(self.root.iterdir()):
            child.rename(self.repository_root / child.name)
        self.root.rmdir()
        report = VALIDATOR.validate(self.repository_root)
        self.assertEqual("unsupported", report["state"])
        self.assertEqual(
            "unsupported-corpus-placement", report["errors"][0]["rule"]
        )

    def test_passing_the_corpus_as_repository_root_is_unsupported(self) -> None:
        report = VALIDATOR.validate(self.root)
        self.assertEqual("unsupported", report["state"])
        self.assertEqual(
            "unsupported-corpus-placement", report["errors"][0]["rule"]
        )

    def test_gen_stack_directory_without_adoption_is_invalid(self) -> None:
        index = self.root / "index.md"
        index.write_text(
            index.read_text(encoding="utf-8").replace(
                "This documentation set adopts the\n"
                "[gen-stack profile](https://example.test/profile) version 0.4.0.",
                "This is an ordinary OKF bundle.",
            ),
            encoding="utf-8",
        )
        report = VALIDATOR.validate(self.repository_root)
        self.assertEqual("invalid", report["state"])
        self.assertIn("profile-adoption", self.rules())

    def test_unsupported_profile_version_is_invalid(self) -> None:
        index = self.root / "index.md"
        index.write_text(
            index.read_text(encoding="utf-8").replace("version 0.4.0", "version 0.2.0"),
            encoding="utf-8",
        )
        report = VALIDATOR.validate(self.repository_root)
        self.assertEqual("invalid", report["state"])
        self.assertIn("profile-adoption", self.rules())

    def test_corpus_symlink_must_not_escape_repository(self) -> None:
        with tempfile.TemporaryDirectory() as external:
            relocated = Path(external) / "corpus"
            self.root.rename(relocated)
            self.root.symlink_to(relocated, target_is_directory=True)
            report = VALIDATOR.validate(self.repository_root)
            self.assertEqual("unsupported", report["state"])
            self.assertEqual("corpus-boundary", report["errors"][0]["rule"])

    def test_internal_corpus_symlink_is_unsupported(self) -> None:
        relocated = self.repository_root / "stored-corpus"
        self.root.rename(relocated)
        self.root.symlink_to(relocated, target_is_directory=True)
        report = VALIDATOR.validate(self.repository_root)
        self.assertEqual("unsupported", report["state"])
        self.assertEqual("corpus-symlink", report["errors"][0]["rule"])

    def test_cli_defaults_to_current_repository_root(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--json"],
            cwd=self.repository_root,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn('"state": "conforming"', completed.stdout)

    def test_cli_does_not_walk_up_from_a_subdirectory(self) -> None:
        subdirectory = self.repository_root / "work"
        subdirectory.mkdir()
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--json"],
            cwd=subdirectory,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(1, completed.returncode)
        self.assertIn('"state": "absent"', completed.stdout)

    def test_missing_system_fails(self) -> None:
        (self.root / "system.md").unlink()
        self.assertIn("required-root-concept", self.rules())

    def test_wrong_required_type_fails(self) -> None:
        (self.root / "system.md").write_text(
            concept("C4 Software System", "Wrong root type"), encoding="utf-8"
        )
        self.assertIn("required-root-type", self.rules())

    def test_valid_colocated_requirement_passes(self) -> None:
        self.add_system_requirement()
        self.sync_relationships()
        self.assertEqual(
            "pass", VALIDATOR.validate(self.repository_root)["structural_result"]
        )

    def test_requirement_lifecycle_is_required_and_controlled(self) -> None:
        self.add_system_requirement(requirement(requirement_lifecycle=None))
        self.assertIn("requirement-lifecycle", self.rules())

    def test_retired_requirement_requires_lifecycle_section(self) -> None:
        self.add_system_requirement(requirement(requirement_lifecycle="retired"))
        self.assertIn("requirement-lifecycle-body", self.rules())

    def test_retired_requirement_with_lifecycle_section_passes(self) -> None:
        body = requirement(requirement_lifecycle="retired") + """

## Lifecycle

The applicable authority retired this synthetic obligation; decision
Provenance remains available from its source record.
"""
        self.add_system_requirement(body)
        self.sync_relationships()
        self.assertEqual(
            "pass", VALIDATOR.validate(self.repository_root)["structural_result"]
        )

    def test_requirement_type_must_match_path(self) -> None:
        self.add_system_requirement(requirement(requirement_type="usability"))
        self.assertIn("requirement-colocation", self.rules())

    def test_requirement_subject_must_resolve(self) -> None:
        self.add_system_requirement(requirement(subject="/missing.md"))
        self.assertIn("requirement-subject-resolves", self.rules())

    def test_intent_concept_cannot_be_requirement_subject(self) -> None:
        intent = self.root / "intent"
        offerings = intent / "offerings"
        offerings.mkdir(parents=True)
        (intent / "index.md").write_text(
            "# Intent\n\n- [Offerings](offerings/)\n", encoding="utf-8"
        )
        (offerings / "index.md").write_text(
            "# Offerings\n\n- [Synthetic offering](synthetic-offering.md)\n",
            encoding="utf-8",
        )
        (offerings / "synthetic-offering.md").write_text(
            concept("Offering", "Synthetic offering"), encoding="utf-8"
        )
        with (self.root / "index.md").open("a", encoding="utf-8") as index:
            index.write("- [Intent](intent/)\n")
        self.add_system_requirement(
            requirement(subject="/intent/offerings/synthetic-offering.md")
        )
        self.assertIn("requirement-subject-type", self.rules())

    def test_cross_cutting_governance_cannot_be_requirement_subject(self) -> None:
        self.add_system_requirement(requirement(subject="/assurance.md"))
        self.assertIn("requirement-subject-type", self.rules())

    def test_legacy_root_use_case_collection_is_prohibited(self) -> None:
        use_cases = self.root / "use-cases"
        use_cases.mkdir()
        (use_cases / "index.md").write_text(
            "# Use cases\n\n- [Synthetic use case](synthetic.md)\n", encoding="utf-8"
        )
        (use_cases / "synthetic.md").write_text(
            concept("Use Case", "Synthetic use case"), encoding="utf-8"
        )
        with (self.root / "index.md").open("a", encoding="utf-8") as index:
            index.write("- [Use cases](use-cases/)\n")
        rules = self.rules()
        self.assertIn("superseded-collection", rules)
        self.assertIn("canonical-path", rules)

    def test_quality_requirement_requires_quality_metadata(self) -> None:
        path = self.add_system_requirement(requirement(requirement_type="quality"))
        quality = path.parent.parent / "quality"
        quality.mkdir()
        (quality / "index.md").write_text(
            "# Quality requirements\n\n- [Preserve accepted state](preserve-state.md)\n",
            encoding="utf-8",
        )
        path.rename(quality / path.name)
        (path.parent / "index.md").unlink()
        path.parent.rmdir()
        self.assertIn("quality-requirement-metadata", self.rules())

    def test_empty_requirement_type_fails(self) -> None:
        self.add_system_requirement()
        usability = self.root / "system" / "requirements" / "usability"
        usability.mkdir()
        (usability / "index.md").write_text("# Usability requirements\n", encoding="utf-8")
        self.assertIn("empty-requirement-type", self.rules())

    def test_legacy_constraint_type_is_prohibited(self) -> None:
        path = self.root / "legacy.md"
        path.write_text(concept("Architecture Constraint"), encoding="utf-8")
        with (self.root / "index.md").open("a", encoding="utf-8") as index:
            index.write("- [Legacy](legacy.md)\n")
        self.assertIn("profile-type-prohibited", self.rules())

    def test_top_level_quality_collection_is_prohibited(self) -> None:
        quality = self.root / "quality"
        quality.mkdir()
        (quality / "index.md").write_text("# Quality\n", encoding="utf-8")
        self.assertIn("superseded-collection", self.rules())

    def test_named_decision_collection_passes(self) -> None:
        architecture = self.root / "architecture"
        decisions = architecture / "decisions"
        decisions.mkdir(parents=True)
        (architecture / "index.md").write_text(
            "# Architecture\n\n- [Decisions](decisions/)\n", encoding="utf-8"
        )
        (decisions / "index.md").write_text(
            "# Decisions\n\n- [Preserve state](preserve-state.md)\n", encoding="utf-8"
        )
        (decisions / "preserve-state.md").write_text(
            concept("Architecture Decision Record", "Preserve state"), encoding="utf-8"
        )
        with (self.root / "index.md").open("a", encoding="utf-8") as index:
            index.write("- [Architecture](architecture/)\n")
        self.assertEqual(
            "pass", VALIDATOR.validate(self.repository_root)["structural_result"]
        )

    def test_generic_relationship_requires_sync_then_passes_full_validation(self) -> None:
        offering_root = self.root / "intent" / "offerings"
        capability_root = self.root / "architecture" / "capabilities"
        offering_root.mkdir(parents=True)
        capability_root.mkdir(parents=True)
        (self.root / "intent" / "index.md").write_text(
            "# Intent\n\n- [Offerings](offerings/)\n",
            encoding="utf-8",
        )
        (offering_root / "index.md").write_text(
            "# Offerings\n\n- [Support](support.md)\n",
            encoding="utf-8",
        )
        (offering_root / "support.md").write_text(
            concept("Offering", "Support").replace(
                "status: stable\n",
                "status: stable\n"
                "relationships:\n"
                "  depends-on-capability:\n"
                "    - /architecture/capabilities/respond.md\n",
            ),
            encoding="utf-8",
        )
        (self.root / "architecture" / "index.md").write_text(
            "# Architecture\n\n- [Capabilities](capabilities/)\n",
            encoding="utf-8",
        )
        (capability_root / "index.md").write_text(
            "# Capabilities\n\n- [Respond](respond.md)\n",
            encoding="utf-8",
        )
        (capability_root / "respond.md").write_text(
            concept("Capability", "Respond"),
            encoding="utf-8",
        )
        with (self.root / "index.md").open("a", encoding="utf-8") as index:
            index.write("- [Intent](intent/)\n- [Architecture](architecture/)\n")

        self.assertIn("relationship-projection", self.rules())
        self.sync_relationships()
        self.assertEqual(
            "pass", VALIDATOR.validate(self.repository_root)["structural_result"]
        )

    def test_missing_evaluation_approach_fails(self) -> None:
        (self.root / "evaluations" / "system-evaluation-approach.md").unlink()
        self.assertIn("required-evaluation-approach", self.rules())

    def test_evaluation_approach_requires_sections(self) -> None:
        path = self.root / "evaluations" / "system-evaluation-approach.md"
        path.write_text(concept("System Evaluation Approach"), encoding="utf-8")
        self.assertIn("evaluation-approach-section", self.rules())


class AuthorityContractTest(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = PROFILE_PATH.read_text(encoding="utf-8")
        self.glossary = GLOSSARY_PATH.read_text(encoding="utf-8")

    def test_every_governed_type_maps_to_one_glossary_term(self) -> None:
        for concept_type in sorted(VALIDATOR.GOVERNED_TYPES):
            matches = re.findall(
                rf"`{re.escape(concept_type)}`(?:(?!\n\n).){{0,500}}?"
                r"\.\./glossary\.md#term-([a-z0-9-]+)",
                self.profile,
                flags=re.DOTALL,
            )
            self.assertEqual(
                1,
                len(matches),
                f"{concept_type} must map exactly once to an authoritative glossary term",
            )

    def test_profile_term_and_relationship_links_resolve_to_stable_glossary_ids(self) -> None:
        fragments = set(
            re.findall(
                r"\.\./glossary\.md#((?:term|relationship)-[a-z0-9-]+)",
                self.profile,
            )
        )
        self.assertTrue(fragments)
        for fragment in fragments:
            self.assertIn(f'<a id="{fragment}"></a>', self.glossary)

    def test_authority_documents_keep_semantics_and_representation_separate(self) -> None:
        self.assertNotIn("Minimum semantic contract", self.profile)
        self.assertNotIn("| Canonical record |", self.glossary)
        self.assertNotIn("profile value", self.glossary)
        self.assertIn("authoritative only for the\ngoverned OKF representation", self.profile)
        self.assertIn("semantic authority for the Gen Stack method", self.glossary)

    def test_every_guide_declares_a_representation_contract(self) -> None:
        guides = []
        for path in BUNDLE_SRC.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            if re.search(r"^type: Guide$", text, flags=re.MULTILINE):
                guides.append(path)
                self.assertIn("\n## Representation\n", text, str(path))
        self.assertTrue(guides)

    def test_preferred_body_order_is_not_profile_style_validation(self) -> None:
        self.assertIn(
            "preferred logical body order where this profile does\n"
            "not require exact structure",
            self.profile,
        )
        self.assertIn(
            "Do\nnot add a style or preferred-body-order failure",
            self.profile,
        )

    def test_profile_prescribes_one_fixed_repository_location(self) -> None:
        self.assertIn(
            "MUST place its one supported\nGen Stack corpus at `<repository-root>/gen-stack/`",
            self.profile,
        )
        self.assertIn(
            "The repository root itself\nand every alternate corpus location are unsupported",
            self.profile,
        )
        self.assertIn("MUST NOT scan for candidate corpora", self.profile)
        self.assertIn(
            "Bundle-relative\npaths beginning with `/` resolve beneath `gen-stack/`",
            self.profile,
        )

    def test_explanations_and_guides_declare_their_dependent_authority(self) -> None:
        seen = {"Explanation": 0, "Guide": 0}
        for path in BUNDLE_SRC.rglob("*.md"):
            meta, _ = VALIDATOR.parse_frontmatter(path)
            concept_type = meta.get("type")
            if concept_type not in seen:
                continue
            seen[concept_type] += 1
            text = path.read_text(encoding="utf-8")
            self.assertIn("> **Authority:**", text, path.as_posix())
            self.assertIn("](/glossary.md)", text, path.as_posix())
            self.assertIn("](/profile/gen-stack-application-profile.md)", text, path.as_posix())
        self.assertGreater(seen["Explanation"], 0)
        self.assertGreater(seen["Guide"], 0)
        self.assertFalse((BUNDLE_SRC / "explainers").exists())
        self.assertNotIn("type: Explainer", "\n".join(
            path.read_text(encoding="utf-8") for path in BUNDLE_SRC.rglob("*.md")
        ))

    def test_profile_and_glossary_local_routes_resolve(self) -> None:
        for source in (PROFILE_PATH, GLOSSARY_PATH):
            text = source.read_text(encoding="utf-8")
            for raw_target in VALIDATOR.LINK_RE.findall(text):
                target = raw_target.strip().split()[0].strip("<>")
                if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                    continue
                target_path, _, fragment = target.partition("#")
                candidate = (
                    BUNDLE_SRC / target_path.lstrip("/")
                    if target_path.startswith("/")
                    else source.parent / unquote(target_path)
                ).resolve(strict=False)
                if candidate.is_dir():
                    candidate = candidate / "index.md"
                self.assertTrue(candidate.is_file(), f"{source}: missing {target}")
                if not fragment:
                    continue
                target_text = candidate.read_text(encoding="utf-8")
                explicit = f'<a id="{fragment}"></a>' in target_text
                heading_ids = {
                    re.sub(r"[^a-z0-9 -]", "", heading.lower()).strip().replace(" ", "-")
                    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", target_text, flags=re.MULTILINE)
                }
                self.assertTrue(
                    explicit or fragment in heading_ids,
                    f"{source}: missing fragment {target}",
                )


if __name__ == "__main__":
    unittest.main()
