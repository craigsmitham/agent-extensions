from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_ROOT = Path(__file__).parents[1]
CLI_PATH = SCRIPT_ROOT / "gen-stack.py"
CONTRACT_ROOT = SCRIPT_ROOT / "contracts"
SCHEMA_PATH = CONTRACT_ROOT / "gen-stack-inspection-v1alpha1.schema.json"
EXAMPLE_PATH = CONTRACT_ROOT / "evaluation-context.example.json"
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))

from gen_stack_profile.frontmatter import replace_relationships
from gen_stack_profile.inspection import (
    MAX_CONCEPT_BYTES,
    SCHEMA_VERSION,
    InspectionFailure,
    InspectionPlane,
    diff_envelope,
)
from gen_stack_profile.relationships import analyze_relationships


def concept(
    concept_type: str,
    title: str,
    *,
    metadata: str = "",
    body: str = "Accepted synthetic meaning for public inspection fixtures.",
) -> str:
    return f"""---
type: {concept_type}
title: {title}
description: A public synthetic {concept_type} used to verify inspection.
status: stable
{metadata}---

# {title}

{body}
"""


def requirement(
    requirement_id: str,
    title: str,
    subject: str,
    *,
    lifecycle: str = "active",
    requirement_type: str = "functional",
    extra: str = "",
) -> str:
    lifecycle_body = (
        "\n## Lifecycle\n\nA synthetic accepted decision retired this obligation.\n"
        if lifecycle == "retired"
        else ""
    )
    return f"""---
type: Requirement
title: {title}
description: A public synthetic Requirement used to verify direct association.
status: stable
requirement_id: {requirement_id}
requirement_type: {requirement_type}
requirement_lifecycle: {lifecycle}
subject: {subject}
{extra}---

# {title}

## Requirement

When synthetic work is requested, the obligated subject shall preserve its accepted boundary.

## Rationale

The fixture needs an observable, non-private obligation.
{lifecycle_body}"""


def evaluation_approach() -> str:
    return concept(
        "System Evaluation Approach",
        "Synthetic evaluation approach",
        body="""## Scope and objectives

The approach covers the synthetic system.

## Evaluation portfolio

Definitions remain repository-native.

## Navigation and reporting

Evidence is navigable by subject and Requirement.

## Evidence and lifecycle

Unknown and harness errors remain visible.

## Gaps and maintenance

Coverage gaps remain explicit.""",
    )


class SyntheticCorpus:
    def __init__(self, *, include_architecture: bool = True) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.repository_root = Path(self.temp.name)
        self.root = self.repository_root / "gen-stack"
        self.root.mkdir()
        self._write_kernel(include_architecture=include_architecture)
        if include_architecture:
            self._write_architecture()
            self._write_requirements()
        self._sync()

    def cleanup(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def _write_kernel(self, *, include_architecture: bool) -> None:
        root_links = []
        for filename, concept_type in {
            "system.md": "System",
            "lifecycle.md": "System Lifecycle",
            "ownership.md": "System Ownership",
            "decisions.md": "Architecture Decision Policy",
            "assurance.md": "System Assurance",
        }.items():
            body = "Accepted synthetic governance meaning."
            if filename == "lifecycle.md":
                body += "\n\n[Processor](architecture/structure/containers/api/components/processor.md)"
            self.write(filename, concept(concept_type, concept_type, body=body))
            root_links.append(f"- [{concept_type}]({filename})")
        self.write(
            "evaluations/index.md",
            "# Evaluations\n\n- [Approach](system-evaluation-approach.md)\n",
        )
        self.write("evaluations/system-evaluation-approach.md", evaluation_approach())
        root_links.append("- [Evaluations](evaluations/)")
        if include_architecture:
            root_links.append("- [Architecture](architecture/)")
        self.write(
            "index.md",
            """---
okf_version: "0.2"
---

# Synthetic Gen Stack corpus

This public fixture adopts the
[gen-stack profile](https://example.test/gen-stack) version 0.4.0.

"""
            + "\n".join(root_links)
            + "\n",
        )

    def _write_architecture(self) -> None:
        self.write(
            "architecture/index.md",
            "# Architecture\n\n- [Capabilities](capabilities/)\n- [Features](features/)\n- [Surfaces](surfaces/)\n- [Structure](structure/)\n",
        )
        self.write(
            "architecture/capabilities/index.md",
            "# Capabilities\n\n- [Operate](operate.md)\n",
        )
        self.write(
            "architecture/capabilities/operate.md",
            concept("Capability", "Operate synthetic work"),
        )
        self.write(
            "architecture/features/index.md",
            "# Features\n\n- [Install](install.md)\n",
        )
        self.write(
            "architecture/features/install.md",
            concept(
                "Feature",
                "Install synthetic extension",
                metadata="""relationships:
  contributes-to-capability:
    - /architecture/capabilities/operate.md
  is-available-through-surface:
    - /architecture/surfaces/cli/install.md
  is-realized-by-c4-element:
    - /architecture/structure/containers/api/components/processor.md
""",
            ),
        )
        self.write(
            "architecture/surfaces/index.md",
            "# Surfaces\n\n- [CLI](cli.md)\n",
        )
        self.write(
            "architecture/surfaces/cli.md",
            concept(
                "Surface",
                "Synthetic CLI",
                body="Accepted command-line encounter point.\n\n[Narrow surfaces](cli/)",
            ),
        )
        self.write(
            "architecture/surfaces/cli/index.md",
            "# CLI surfaces\n\n- [Install command](install.md)\n",
        )
        self.write(
            "architecture/surfaces/cli/install.md",
            concept(
                "Surface",
                "Install command",
                metadata="""relationships:
  is-realized-by-c4-element:
    - /architecture/structure/containers/api/components/processor.md
""",
                body="Accepted install interaction.\n\n[Requirements](install/requirements/)",
            ),
        )
        self.write(
            "architecture/structure/index.md",
            "# Structure\n\n- [Systems](systems/)\n- [Containers](containers/)\n- [Views](views/)\n",
        )
        self.write(
            "architecture/structure/systems/index.md",
            "# Systems\n\n- [Extensions](extensions.md)\n",
        )
        self.write(
            "architecture/structure/systems/extensions.md",
            concept("C4 Software System", "Extensions system"),
        )
        self.write(
            "architecture/structure/containers/index.md",
            "# Containers\n\n- [API](api.md)\n",
        )
        self.write(
            "architecture/structure/containers/api.md",
            concept(
                "C4 Container",
                "Extension API",
                metadata="""relationships:
  belongs-to-c4-software-system:
    - /architecture/structure/systems/extensions.md
""",
                body="Accepted runtime boundary.\n\n[Components](api/components/)",
            ),
        )
        self.write(
            "architecture/structure/containers/api/index.md",
            "# API details\n\n- [Components](components/)\n",
        )
        self.write(
            "architecture/structure/containers/api/components/index.md",
            "# Components\n\n- [Processor](processor.md)\n",
        )
        self.write(
            "architecture/structure/containers/api/components/processor.md",
            concept(
                "C4 Component",
                "Install processor",
                body="Accepted cohesive responsibility.\n\n[Requirements](processor/requirements/)",
            ),
        )
        self.write(
            "architecture/structure/views/index.md",
            "# Views\n\n- [Containers](containers.md)\n",
        )
        self.write(
            "architecture/structure/views/containers.md",
            concept(
                "C4 View",
                "Container view",
                metadata="""view_type: container
relationships:
  projects-c4-element:
    - /architecture/structure/containers/api.md
    - /architecture/structure/systems/extensions.md
""",
            ),
        )

    def _write_requirement_collection(
        self,
        subject_file: str,
        requirement_type: str,
        filename: str,
        body: str,
    ) -> None:
        sidecar = subject_file[:-3]
        collection = f"{sidecar}/requirements"
        type_root = f"{collection}/{requirement_type}"
        self.write(
            f"{sidecar}/index.md",
            f"# Subject details\n\n- [Requirements](requirements/)\n",
        )
        self.write(
            f"{collection}/index.md",
            f"# Requirements\n\n- [{requirement_type}]({requirement_type}/)\n",
        )
        existing = self.root / type_root / "index.md"
        links = existing.read_text(encoding="utf-8") if existing.exists() else f"# {requirement_type}\n\n"
        links += f"- [{filename}]({filename})\n"
        self.write(f"{type_root}/index.md", links)
        self.write(f"{type_root}/{filename}", body)

    def _write_requirements(self) -> None:
        surface = "architecture/surfaces/cli/install.md"
        self._write_requirement_collection(
            surface,
            "functional",
            "preserve-boundary.md",
            requirement("SYN-REQ-0001", "Preserve install boundary", f"/{surface}"),
        )
        self._write_requirement_collection(
            surface,
            "functional",
            "retired-behavior.md",
            requirement(
                "SYN-REQ-0002",
                "Retired install behavior",
                f"/{surface}",
                lifecycle="retired",
            ),
        )
        component = "architecture/structure/containers/api/components/processor.md"
        self._write_requirement_collection(
            component,
            "constraint",
            "preserve-component.md",
            requirement(
                "SYN-REQ-0003",
                "Preserve processor boundary",
                f"/{component}",
                requirement_type="constraint",
            ),
        )

    def _sync(self) -> None:
        analysis = analyze_relationships(self.root)
        blocking = [
            item for item in analysis.diagnostics if item.rule != "relationship-projection"
        ]
        if blocking:
            raise AssertionError([(item.rule, str(item.path), item.message) for item in blocking])
        for relative in analysis.projection_paths:
            replace_relationships(
                analysis.concepts[relative].path,
                analysis.expected.get(relative, {}),
            )


class InspectionPlaneTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = SyntheticCorpus()
        self.addCleanup(self.fixture.cleanup)
        self.plane = InspectionPlane(self.fixture.repository_root)
        self.assertTrue(self.plane.conforming, self.plane.validation_report)

    def test_status_and_envelope_are_public_deterministic_and_layered(self) -> None:
        first = self.plane.status()
        second = self.plane.status()
        self.assertEqual(SCHEMA_VERSION, first["schema_version"])
        self.assertEqual("conforming", first["discovery"]["state"])
        self.assertEqual("unknown", first["discovery"]["semantic_result"])
        self.assertEqual(first["output_digest"], second["output_digest"])
        self.assertNotIn(str(self.fixture.repository_root), json.dumps(first))

    def test_established_sparse_greenfield_context_is_valid_and_empty_without_gap_claims(self) -> None:
        greenfield = SyntheticCorpus(include_architecture=False)
        self.addCleanup(greenfield.cleanup)
        plane = InspectionPlane(greenfield.repository_root)
        context = plane.evaluation_context()
        self.assertEqual([], context["data"]["surfaces"])
        self.assertEqual([], context["data"]["structure"])
        self.assertEqual({}, context["data"]["requirements"])
        self.assertFalse(
            any(item["rule"] == "missing-requirements" for item in context["diagnostics"])
        )

    def test_list_search_and_show_resolve_concepts_and_requirement_ids(self) -> None:
        surfaces = self.plane.list_concepts("surfaces")["data"]["concepts"]
        self.assertEqual(2, len(surfaces))
        results = self.plane.search("install boundary")["data"]["results"]
        self.assertEqual("SYN-REQ-0001", results[0]["requirement_id"])
        shown = self.plane.show("SYN-REQ-0001")["data"]["result"]
        self.assertEqual("active", shown["requirement_lifecycle"])
        self.assertIn("Requirement", shown["sections"])

    def test_show_requirements_is_direct_only_and_preserves_lifecycle(self) -> None:
        parent = self.plane.show("/architecture/surfaces/cli.md", "requirements")["data"]["result"]
        self.assertEqual([], parent["direct_requirements"])
        self.assertIsNone(parent["inherited_requirements"])
        child = self.plane.show(
            "/architecture/surfaces/cli/install.md", "requirements"
        )["data"]["result"]
        self.assertEqual(
            {"active", "retired"},
            {item["requirement_lifecycle"] for item in child["direct_requirements"]},
        )

    def test_evaluation_context_projects_both_hierarchies_and_requirements(self) -> None:
        context = self.plane.evaluation_context()["data"]
        self.assertEqual("/architecture/surfaces/cli.md", context["surfaces"][0]["ref"])
        install = context["surfaces"][0]["children"][0]
        self.assertEqual(["SYN-REQ-0001", "SYN-REQ-0002"], install["direct_requirements"])
        system = context["structure"][0]
        self.assertEqual("C4 Software System", system["type"])
        self.assertEqual("C4 Container", system["children"][0]["type"])
        self.assertEqual("C4 Component", system["children"][0]["children"][0]["type"])
        self.assertEqual(
            {"SYN-REQ-0001", "SYN-REQ-0002", "SYN-REQ-0003"},
            set(context["requirements"]),
        )
        self.assertTrue(context["cross_view_mappings"])
        self.assertFalse(context["c4_views"][0]["evaluation_subject"])
        self.assertEqual("not-inferred", context["interpretation"]["requirement_inheritance"])

    def test_scoped_evaluation_context_separates_ancestors_and_explicit_relations(self) -> None:
        context = self.plane.evaluation_context(
            "/architecture/surfaces/cli/install.md"
        )["data"]
        self.assertEqual("scoped", context["scope"]["mode"])
        self.assertEqual(
            ["/architecture/surfaces/cli.md"],
            [item["ref"] for item in context["ancestor_context"]],
        )
        self.assertTrue(
            any(item["type"] == "C4 Component" for item in context["related_subjects"])
        )

    def test_ordinary_markdown_link_does_not_become_graph_relation(self) -> None:
        with self.assertRaises(InspectionFailure) as raised:
            self.plane.path(
                "/lifecycle.md",
                "/architecture/structure/containers/api/components/processor.md",
            )
        self.assertEqual("path-not-found", raised.exception.code)

    def test_path_why_and_affected_concepts_preserve_provenance_and_limits(self) -> None:
        path = self.plane.path(
            "/architecture/features/install.md",
            "/architecture/structure/containers/api/components/processor.md",
        )["data"]
        self.assertEqual(1, len(path["hops"]))
        edge_ref = path["hops"][0]["edge"]["ref"]
        why = self.plane.why(edge_ref)["data"]
        self.assertEqual("relationship", why["kind"])
        self.assertEqual("asserted", why["explanation"]["derivation"])
        affected = self.plane.affected_concepts("/architecture/features/install.md")["data"]
        self.assertIn("not implementation", affected["interpretation"])

    def test_snapshot_and_diff_report_concept_change_without_peer_impact_claims(self) -> None:
        before = self.plane.snapshot()
        requirement_path = self.fixture.root / "architecture/surfaces/cli/install/requirements/functional/preserve-boundary.md"
        requirement_path.write_text(
            requirement_path.read_text(encoding="utf-8").replace(
                "preserve its accepted boundary", "preserve its revised accepted boundary"
            ),
            encoding="utf-8",
        )
        after_plane = InspectionPlane(self.fixture.repository_root)
        after = after_plane.snapshot()
        diff = diff_envelope(before, after)
        changed = diff["data"]["concepts"]["changed"]
        self.assertEqual(1, len(changed))
        self.assertIn("body", changed[0]["changed_fields"])
        self.assertIn("implementation-or-evaluation-impact", json.dumps(diff["unknowns"]))

    def test_cli_emits_json_contract_and_human_views(self) -> None:
        json_run = subprocess.run(
            [
                sys.executable,
                str(CLI_PATH),
                "-C",
                str(self.fixture.repository_root),
                "--json",
                "evaluation-context",
                "/architecture/surfaces/cli/install.md",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, json_run.returncode, json_run.stdout + json_run.stderr)
        payload = json.loads(json_run.stdout)
        self.assertEqual(SCHEMA_VERSION, payload["schema_version"])
        human_run = subprocess.run(
            [
                sys.executable,
                str(CLI_PATH),
                "-C",
                str(self.fixture.repository_root),
                "show",
                "SYN-REQ-0001",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, human_run.returncode, human_run.stdout + human_run.stderr)
        self.assertIn("Preserve install boundary [Requirement]", human_run.stdout)

        trailing_option = subprocess.run(
            [
                sys.executable,
                str(CLI_PATH),
                "status",
                "--json",
                "-C",
                str(self.fixture.repository_root),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, trailing_option.returncode, trailing_option.stderr)
        self.assertEqual("status", json.loads(trailing_option.stdout)["operation"])


class InspectionFailClosedTest(unittest.TestCase):
    def test_absent_corpus_reports_state_and_refuses_queries(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            plane = InspectionPlane(Path(temporary))
            self.assertEqual("absent", plane.status()["data"]["state"])
            with self.assertRaises(InspectionFailure) as raised:
                plane.list_concepts("concepts")
            self.assertEqual("operation-ineligible", raised.exception.code)

    def test_oversized_source_is_rejected_before_profile_parsing(self) -> None:
        fixture = SyntheticCorpus(include_architecture=False)
        self.addCleanup(fixture.cleanup)
        (fixture.root / "system.md").write_text(
            "x" * (MAX_CONCEPT_BYTES + 1), encoding="utf-8"
        )
        plane = InspectionPlane(fixture.repository_root)
        self.assertFalse(plane.conforming)
        self.assertEqual(
            "inspection-resource-limit", plane.validation_report["errors"][0]["rule"]
        )

    def test_internal_symlink_is_rejected_without_reading_its_target(self) -> None:
        fixture = SyntheticCorpus(include_architecture=False)
        self.addCleanup(fixture.cleanup)
        external = fixture.repository_root / "external-public-fixture.md"
        external.write_text("Synthetic external content.", encoding="utf-8")
        (fixture.root / "linked.md").symlink_to(external)
        plane = InspectionPlane(fixture.repository_root)
        self.assertFalse(plane.conforming)
        self.assertEqual(
            "inspection-symlink", plane.validation_report["errors"][0]["rule"]
        )

    def test_corpus_change_invalidates_an_existing_inspection_snapshot(self) -> None:
        fixture = SyntheticCorpus(include_architecture=False)
        self.addCleanup(fixture.cleanup)
        plane = InspectionPlane(fixture.repository_root)
        assurance = fixture.root / "assurance.md"
        assurance.write_text(
            assurance.read_text(encoding="utf-8") + "\nChanged after indexing.\n",
            encoding="utf-8",
        )
        with self.assertRaises(InspectionFailure) as raised:
            plane.status()
        self.assertEqual("corpus-changed-during-inspection", raised.exception.code)


class InspectionContractTest(unittest.TestCase):
    def test_schema_and_public_example_are_parseable_and_version_aligned(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        example = json.loads(EXAMPLE_PATH.read_text(encoding="utf-8"))
        self.assertEqual("https://json-schema.org/draft/2020-12/schema", schema["$schema"])
        self.assertEqual(SCHEMA_VERSION, schema["properties"]["schema_version"]["const"])
        self.assertEqual(SCHEMA_VERSION, example["schema_version"])
        self.assertEqual("evaluation-context", example["operation"])
        self.assertEqual("direct-only", example["data"]["interpretation"]["requirement_association"])
        self.assertNotIn(Path.home().as_posix(), json.dumps(example))

    def test_documented_cli_entrypoint_has_help(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(CLI_PATH), "--help"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("usage:", completed.stdout)

    def test_invalid_diff_input_still_emits_the_machine_envelope(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            invalid = Path(temporary) / "invalid.json"
            invalid.write_text("{}\n", encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable,
                    str(CLI_PATH),
                    "--json",
                    "diff",
                    str(invalid),
                    str(invalid),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(1, completed.returncode)
            payload = json.loads(completed.stdout)
            self.assertEqual("diff", payload["operation"])
            self.assertEqual("snapshot-contract", payload["diagnostics"][0]["rule"])


if __name__ == "__main__":
    unittest.main()
