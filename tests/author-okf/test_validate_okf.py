#!/usr/bin/env python3
"""Focused tests for author-okf's progressive-discovery checks."""

from __future__ import annotations

import datetime as dt
import importlib.util
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = (
    REPO_ROOT
    / ".axm/extensions/@craigsmitham/skills/author-okf/src/scripts/validate_okf.py"
)
SPEC = importlib.util.spec_from_file_location("validate_okf", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ProgressiveDiscoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name).resolve()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")

    def findings(self):
        findings, _ = VALIDATOR.validate(self.root, dt.date(2026, 8, 8))
        return findings.items

    def test_nested_discovery_with_matching_metadata_is_clean(self) -> None:
        self.write(
            "index.md",
            """
            ---
            okf_version: "0.2"
            ---

            # Example knowledge

            Portable examples for testing authored discovery routes.

            ## Area

            * [Useful area](area/) - Concepts used by the synthetic example.
            """,
        )
        self.write(
            "area/index.md",
            """
            # Useful area

            Concepts used by the synthetic example.

            * [Useful concept](useful-concept.md) - How the synthetic concept
              demonstrates discovery.
            """,
        )
        self.write(
            "area/useful-concept.md",
            """
            ---
            type: Explanation
            title: Useful concept
            description: How the synthetic concept demonstrates discovery.
            ---

            # Useful concept

            Synthetic content.
            """,
        )

        self.assertEqual(self.findings(), [])

    def test_reports_stale_index_metadata_and_unreachable_concept(self) -> None:
        self.write(
            "index.md",
            """
            ---
            okf_version: "0.2"
            ---

            # Example knowledge

            Portable examples for testing authored discovery routes.

            * [Old title](linked.md) - An outdated description.
            """,
        )
        self.write(
            "linked.md",
            """
            ---
            type: Explanation
            title: Current title
            description: The current description.
            ---

            # Current title
            """,
        )
        self.write(
            "orphan.md",
            """
            ---
            type: Reference
            title: Orphan
            description: A concept absent from every index.
            ---

            # Orphan
            """,
        )

        codes = {item["code"] for item in self.findings()}
        self.assertIn("index-title-mismatch", codes)
        self.assertIn("index-description-mismatch", codes)
        self.assertIn("discovery-unreachable", codes)

    def test_missing_root_index_is_advisory(self) -> None:
        self.write(
            "concept.md",
            """
            ---
            type: Reference
            title: Standalone concept
            description: A conformant concept without an authored discovery root.
            ---

            # Standalone concept
            """,
        )

        items = self.findings()
        self.assertEqual(
            [item["code"] for item in items if item["severity"] == "warn"],
            ["discovery-root-missing"],
        )
        self.assertFalse([item for item in items if item["severity"] == "error"])

    def test_index_without_scope_introduction_is_reported_as_info(self) -> None:
        self.write(
            "index.md",
            """
            ---
            okf_version: "0.2"
            ---

            # Example knowledge

            * [Concept](concept.md) - A synthetic concept.
            """,
        )
        self.write(
            "concept.md",
            """
            ---
            type: Reference
            title: Concept
            description: A synthetic concept.
            ---

            # Concept
            """,
        )

        matches = [item for item in self.findings() if item["code"] == "index-introduction-missing"]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["severity"], "info")


if __name__ == "__main__":
    unittest.main()
