#!/usr/bin/env python3
"""Lint the System Spec skill's profile, templates, running example, and job.

Checks what breaks silently when these files change: links and anchors, rule
identifiers and references to them, where normative keywords appear, and
agreement between each template's Type contract and Suggested document. The
other conventions in skills/system-spec/MAINTAINING.md are left to review. Exits 1
when any finding is reported.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SPEC = Path(__file__).resolve().parent.parent / "skills" / "system-spec"
SRC = SPEC / "src"
SUPPORTING = {"Illustrations", "Rationale", "Verification", "Open questions", "Related"}

KEYWORD = re.compile(r"\b(MUST|SHOULD|MAY)\b")
TAG_ITEM = re.compile(r"^- \*\*((?:P-[A-Z]{3})|[A-Z]{2,3})-(\d+)\*\*")
TAG_REF = re.compile(r"\b((?:P-[A-Z]{3})|[A-Z]{2,3})-(\d+)\b")
ENTRY = re.compile(r"^  - \*\*([^*]+)\*\*", re.M)

findings: list[str] = []


def report(path: Path, index: int, message: str) -> None:
    findings.append(f"{path.relative_to(SPEC)}:{index + 1} {message}")


class Doc:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.lines = path.read_text().splitlines()
        self.code: list[bool] = []
        fence = None
        for line in self.lines:
            m = re.match(r"(`{3,}|~{3,})\s*(\S*)$", line.strip())
            if fence is None and m:
                fence = m.group(1)
                self.code.append(True)
            elif fence and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and not m.group(2):
                fence = None
                self.code.append(True)
            else:
                self.code.append(fence is not None)

    def headings(self, level: int) -> list[tuple[int, str]]:
        prefix = "#" * level + " "
        return [(i, l[len(prefix):].strip()) for i, l in enumerate(self.lines) if l.startswith(prefix) and not self.code[i]]

    def section(self, title: str) -> range:
        """Body of the first level-2 section with this title, or an empty range."""
        heads = self.headings(2)
        for n, (i, t) in enumerate(heads):
            if t == title:
                return range(i + 1, heads[n + 1][0] if n + 1 < len(heads) else len(self.lines))
        return range(0)

    def blocks(self, lines: range) -> list[tuple[int, str]]:
        """Top-level list items, with their nested lines, and paragraphs."""
        out, i = [], lines.start
        while i < lines.stop:
            if self.code[i] or not self.lines[i].strip():
                i += 1
                continue
            j = i + 1
            while j < lines.stop and not self.code[j]:
                nxt = self.lines[j]
                if nxt.startswith("#") or (nxt.startswith(("- ", "|")) and self.lines[i].startswith("- ")):
                    break
                if not nxt.strip():
                    k = j
                    while k < lines.stop and not self.lines[k].strip():
                        k += 1
                    if self.lines[i].startswith("- ") and k < lines.stop and self.lines[k].startswith("  "):
                        j = k
                        continue
                    break
                j += 1
            out.append((i, "\n".join(self.lines[i:j])))
            i = j
        return out


def collect_rules(doc: Doc, lines: range, rules: dict[str, Path]) -> list[str]:
    """Record tagged rules and report keywords outside them. Returns the block texts."""
    texts = []
    for i, text in doc.blocks(lines):
        strengths = set(KEYWORD.findall(text))
        m = TAG_ITEM.match(text)
        if not m:
            if strengths and not text.startswith("|"):
                report(doc.path, i, f"keyword {sorted(strengths)} outside a tagged rule")
            continue
        tag = f"{m.group(1)}-{m.group(2)}"
        if len(strengths) != 1:
            report(doc.path, i, f"{tag}: needs exactly one strength, found {sorted(strengths) or 'none'}")
        if tag in rules:
            report(doc.path, i, f"{tag}: duplicate identifier")
        rules[tag] = doc.path
        texts.append(text)
    return texts


def no_keywords(doc: Doc, lines: range) -> None:
    for i in lines:
        if not doc.code[i] and KEYWORD.search(doc.lines[i]):
            report(doc.path, i, "normative keyword outside the profile or a Type contract")


def check_template(doc: Doc, rules: dict[str, Path]) -> None:
    contract = doc.section("Type contract")
    if not contract:
        report(doc.path, 0, "missing '## Type contract'")
        return
    texts = collect_rules(doc, contract, rules)
    no_keywords(doc, range(0, contract.start - 1))
    no_keywords(doc, range(contract.stop, len(doc.lines)))

    includes = next((ENTRY.findall(t) for t in texts if "MUST include these sections:" in t.splitlines()[0]), None)
    context = next((ENTRY.findall(t) for t in texts if "`Context | Value` table" in t), [])
    if includes is None:
        report(doc.path, contract.start, "the Type contract needs a 'MUST include these sections:' rule")
        return

    sections, rows, in_table = [], [], False
    for i in doc.section("Suggested document"):
        line = doc.lines[i]
        if not doc.code[i]:
            continue
        if line.startswith("## "):
            sections.append(line[3:].strip())
        if line.startswith("| Context | Value |"):
            in_table = True
        elif in_table and line.startswith("|"):
            if not line.startswith("| ---"):
                rows.append(line.split("|")[1].strip())
        else:
            in_table = False
    own = [s for s in sections if s not in SUPPORTING or s in includes]
    if own != includes:
        report(doc.path, contract.start, f"Suggested document sections {own} differ from the contract's {includes}")
    if rows != context:
        report(doc.path, contract.start, f"Suggested document Context rows {rows} differ from the contract's {context}")


def slug(heading: str) -> str:
    return re.sub(r"[^\w\s-]", "", heading.lower()).strip().replace(" ", "-")


def check_links(docs: list[Doc]) -> None:
    anchors = {d.path: {slug(t) for level in range(1, 7) for _, t in d.headings(level)} for d in docs}
    for d in docs:
        for i, line in enumerate(d.lines):
            if d.code[i]:
                continue
            for m in re.finditer(r"\]\(([^)\s<>]+)\)", re.sub(r"`[^`]*`", "", line)):
                target = m.group(1)
                if re.match(r"[a-z]+:", target):
                    continue
                path, _, anchor = target.partition("#")
                resolved = (d.path.parent / path).resolve() if path else d.path
                if not resolved.exists():
                    report(d.path, i, f"broken link {target}")
                elif anchor and resolved in anchors and anchor not in anchors[resolved]:
                    report(d.path, i, f"broken anchor {target}")


def check_references(docs: list[Doc], rules: dict[str, Path]) -> None:
    prefixes = {tag.rpartition("-")[0] for tag in rules}
    for d in docs:
        for i, line in enumerate(d.lines):
            for m in TAG_REF.finditer(line):
                if m.group(1) in prefixes and m.group(0) not in rules:
                    report(d.path, i, f"reference to unknown rule {m.group(0)}")


def main() -> int:
    rules: dict[str, Path] = {}
    profile = Doc((SRC / "references" / "profile.md").resolve())
    templates = [Doc(p.resolve()) for p in sorted((SRC / "templates").glob("*.md"))]
    example = Doc((SRC / "references" / "example.md").resolve())
    job = Doc((SRC / "references" / "job.md").resolve())
    others = [Doc((SRC / "SKILL.md").resolve()), Doc((SPEC / "README.md").resolve()), Doc((SPEC / "MAINTAINING.md").resolve())]

    collect_rules(profile, range(profile.headings(2)[0][0], len(profile.lines)), rules)
    for doc in templates:
        check_template(doc, rules)
    no_keywords(example, range(len(example.lines)))
    no_keywords(job, range(len(job.lines)))

    docs = [profile, example, job] + templates + others
    check_links(docs)
    check_references(docs, rules)

    for finding in findings:
        print(finding)
    print(f"{len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
