#!/usr/bin/env python3
"""Lint the Spec profile, its modules, templates, and running example.

Enforces the maintainer conventions in skills/spec/README.md: rule
identifiers, retired identifiers, template anatomy, contract field and section
lists, vocabulary, named links, links, and example names. Exits 1 when any error is found unless --warn-only is given.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
PROFILE = SRC / "references" / "profile.md"
EXAMPLE = SRC / "references" / "example.md"
MODULES = SRC / "references" / "modules"
MODULE_AREAS = {"decomposition": "DEC", "rules": "RUL", "quality": "QUA", "data": "DAT"}
TEMPLATES = SRC / "templates"

TYPES = {
    "system": ("System", "SYS"),
    "subsystem": ("Subsystem", "SUB"),
    "business-requirements": ("Business Requirements", "BIZ"),
    "user-class": ("User Class", "USR"),
    "external-interface": ("External Interface", "EI"),
    "feature": ("Feature", "FEA"),
    "feature-component": ("Feature Component", "CMP"),
    "use-case": ("Use Case", "UC"),
    "requirement": ("Requirement", "REQ"),
    "business-rule": ("Business Rule", "BR"),
    "quality-characteristic": ("Quality Characteristic", "QC"),
    "quality-requirement": ("Quality Requirement", "QR"),
    "glossary": ("Glossary", "GLO"),
    "entity-type": ("Entity Type", "ET"),
    "value-type": ("Value Type", "VT"),
}
PROFILE_AREAS = {"TYP", "STR", "PLC", "OWN", "LNK", "STA", "CON", "DOC"}
SUPPORTING_SECTIONS = ["Illustrations", "Rationale", "Verification", "Open questions", "Related"]
README = ROOT / "README.md"
PURPOSE_END = (
    "Apply the [Spec profile](../references/profile.md). The Type contract is "
    "normative; the remaining sections guide authoring."
)

KEYWORD = re.compile(r"\b(MUST NOT|MUST|SHOULD NOT|SHOULD|MAY)\b")
TAG_ITEM = re.compile(r"^- \*\*((?:P-[A-Z]{3})|[A-Z]{2,3})-(\d+)\*\*")
TAG_REF = re.compile(r"\b((?:P-[A-Z]{3})|[A-Z]{2,3})-(\d+)\b")

# Vocabulary guards: (pattern, message). Removed fields, relationships, and
# anchors are caught by the relationship, link, and anatomy checks instead.
BANNED = [
    (re.compile(r"\btop-level\b"), "use 'system-level' or 'subsystem-level'"),
    (re.compile(r"^## Sources\b"), "provenance belongs in OKF `sources` frontmatter"),
    (re.compile(r"[Qq]uality [Aa]ttribute"), "use 'quality characteristic'"),
    (re.compile(r"\bsuccess measures?\b|Success measures"), "use 'success indicator'"),
    (re.compile(r"\bservice level agreements?\b"), "use 'operations concerns'"),
    (re.compile(r"\b[Oo]wner\b"), "use 'home' for a concept's location or 'owning type'"),
    (re.compile(r"[Rr]elationships tables?"), "use 'named links table'"),
    (re.compile(r"^### Differences from the "), "say how a type differs in a short topic subsection"),
]


@dataclass
class Finding:
    level: str
    path: Path
    line: int
    message: str

    def __str__(self) -> str:
        rel = self.path.relative_to(ROOT) if self.path.is_relative_to(ROOT) else self.path
        return f"{self.level} {rel}:{self.line} {self.message}"


@dataclass
class Rule:
    tag: str
    strength: str  # MUST, SHOULD, MAY
    path: Path
    line: int
    text: str


@dataclass
class Doc:
    path: Path
    lines: list[str]
    code: list[bool] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path) -> "Doc":
        lines = path.read_text().splitlines()
        code, fence = [], None
        for line in lines:
            stripped = line.lstrip()
            m = re.match(r"(`{3,}|~{3,})", stripped)
            if fence is None and m:
                fence = m.group(1)
                code.append(True)
            elif fence is not None and m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and stripped.strip() == m.group(1):
                code.append(True)
                fence = None
            else:
                code.append(fence is not None)
        return cls(path, lines, code)

    def headings(self, level: int) -> list[tuple[int, str]]:
        prefix = "#" * level + " "
        return [
            (i, l[len(prefix):].strip())
            for i, l in enumerate(self.lines)
            if l.startswith(prefix) and not self.code[i]
        ]

    def section(self, level: int, title: str) -> tuple[int, int] | None:
        """Return [start, end) line indexes of a section's body."""
        heads = self.headings(level)
        for n, (i, t) in enumerate(heads):
            if t == title:
                end = len(self.lines)
                for j in range(i + 1, len(self.lines)):
                    if self.code[j]:
                        continue
                    m = re.match(r"(#+) ", self.lines[j])
                    if m and len(m.group(1)) <= level:
                        end = j
                        break
                return i + 1, end
        return None


class Linter:
    def __init__(self) -> None:
        self.findings: list[Finding] = []
        self.rules: dict[str, Rule] = {}

    def error(self, path: Path, line: int, msg: str) -> None:
        self.findings.append(Finding("ERROR", path, line + 1, msg))

    def warn(self, path: Path, line: int, msg: str) -> None:
        self.findings.append(Finding("WARN", path, line + 1, msg))

    # ---- rule items ---------------------------------------------------
    def items(self, doc: Doc, start: int, end: int) -> list[tuple[int, int, str]]:
        """Top-level list items and paragraphs as (start, end, text) blocks."""
        blocks, i = [], start
        while i < end:
            if doc.code[i] or not doc.lines[i].strip():
                i += 1
                continue
            j = i + 1
            if doc.lines[i].startswith("- "):
                while j < end and not doc.code[j]:
                    nxt = doc.lines[j]
                    if nxt.startswith("- ") or nxt.startswith("#") or nxt.startswith("|"):
                        break
                    if not nxt.strip():
                        k = j
                        while k < end and not doc.lines[k].strip():
                            k += 1
                        if k < end and doc.lines[k].startswith("  "):
                            j = k
                            continue
                        break
                    j += 1
            else:
                while j < end and doc.lines[j].strip() and not doc.code[j] and not doc.lines[j].startswith("#"):
                    j += 1
            blocks.append((i, j, "\n".join(doc.lines[i:j])))
            i = j
        return blocks

    def strength_of(self, text: str) -> set[str]:
        return {k.split()[0] for k in KEYWORD.findall(text)}

    def collect_rules(self, doc: Doc, start: int, end: int, code: str | None, areas: set[str] = PROFILE_AREAS) -> list[Rule]:
        found = []
        for s, e, text in self.items(doc, start, end):
            m = TAG_ITEM.match(text)
            kws = self.strength_of(text)
            if not m:
                if kws and not text.startswith("|"):
                    self.error(doc.path, s, f"keyword {sorted(kws)} outside a tagged rule")
                continue
            prefix, num = m.group(1), m.group(2)
            tag = f"{prefix}-{num}"
            if code is None:
                if not prefix.startswith("P-") or prefix[2:] not in areas:
                    self.error(doc.path, s, f"{tag}: rules here use P-<AREA> with AREA in {sorted(areas)}")
            elif prefix != code:
                self.error(doc.path, s, f"{tag}: expected code {code}")
            if len(kws) != 1:
                self.error(doc.path, s, f"{tag}: needs exactly one strength, found {sorted(kws) or 'none'}")
            if tag in self.rules:
                self.error(doc.path, s, f"{tag}: duplicate identifier")
            rule = Rule(tag, next(iter(kws)) if kws else "?", doc.path, s, text)
            self.rules[tag] = rule
            found.append(rule)
        return found

    def entries(self, text: str) -> list[str]:
        return re.findall(r"^  - \*\*([^*]+)\*\*", text, re.M)

    def keywords_forbidden(self, doc: Doc, start: int, end: int, where: str) -> None:
        for i in range(start, end):
            if doc.code[i]:
                continue
            kws = KEYWORD.findall(doc.lines[i])
            if kws:
                self.error(doc.path, i, f"keyword {kws} in {where}; rules live in the profile or Type contract")

    # ---- template anatomy ---------------------------------------------
    def template(self, path: Path) -> list[Rule]:
        stem = path.stem
        type_name, code = TYPES[stem]
        doc = Doc.load(path)
        h1 = doc.headings(1)
        if not h1 or h1[0][1] != f"{type_name} template":
            self.error(path, 0, f"title must be '# {type_name} template'")
        paras = [b for b in self.items(doc, (h1[0][0] + 1) if h1 else 0, doc.headings(2)[0][0] if doc.headings(2) else len(doc.lines))]
        flat = [" ".join(x.strip() for x in p[2].splitlines()) for p in paras]
        if not flat:
            self.error(path, 0, "needs a purpose paragraph")
        else:
            if not flat[0].startswith("Use for") or not flat[0].endswith(PURPOSE_END):
                self.error(path, paras[0][0], "purpose paragraph must begin 'Use for' and end with the standard sentence")
            if len(flat) > 1:
                self.error(path, paras[1][0], "only the purpose paragraph precedes the Type contract; lineage belongs in the README's Template sources")
        h2 = [t for _, t in doc.headings(2)]
        if h2 != ["Type contract", "Suggested document", "Writing guidance"]:
            self.error(path, 0, f"H2 sections must be Type contract, Suggested document, Writing guidance; found {h2}")

        rules: list[Rule] = []
        identifies = False
        lists: dict[int, list[str]] = {}
        requires_sources = False
        sec = doc.section(2, "Type contract")
        if sec:
            requires_sources = "`sources` frontmatter" in "\n".join(doc.lines[sec[0]:sec[1]])
            for i, t in doc.headings(3):
                if sec[0] <= i < sec[1]:
                    self.error(path, i, "the Type contract has no subsections")
            rules = self.collect_rules(doc, sec[0], sec[1], code)
            blocks = self.items(doc, sec[0], sec[1])
            rank_names = {1: "title", 2: "identify", 3: "include", 5: "type-specific", 6: "prohibition"}
            last_rank = 0
            article = "An" if type_name[0] in "AEIO" else "A"
            opening = f"{article} {type_name} document is placed as"
            if not blocks:
                self.error(path, sec[0], "the Type contract is empty")
            elif not TAG_ITEM.match(blocks[0][2]) and not blocks[0][2].startswith(opening):
                self.error(path, sec[0], f"an untagged placement paragraph must begin '{opening} …'")
            for n, (s, e, text) in enumerate(blocks):
                flat_text = " ".join(x.strip() for x in text.splitlines())
                if n == 0 and not TAG_ITEM.match(text):
                    continue
                if not TAG_ITEM.match(text):
                    if "binding and illustrative content" in flat_text:
                        self.error(path, s, "binding content is defined once in the profile, not in the contract")
                    continue
                else:
                    head = text.splitlines()[0]
                    if re.search(r"\btitle (MUST|SHOULD)", flat_text):
                        rank = 1
                    elif re.search(r"\b(MUST|SHOULD|MAY)( NOT)? identify\b", head):
                        rank = 2
                        identifies = identifies or True
                    elif re.search(r"\b(MUST|SHOULD|MAY)( NOT)? include\b", head):
                        rank = 3
                    elif re.search(r"\b(MUST NOT|SHOULD NOT)\b", flat_text) and not re.search(r"\b(MUST|SHOULD)\b(?! NOT)", flat_text):
                        rank = 6
                    else:
                        rank = 5
                    if rank in (2, 3):
                        want_head = f"MUST {rank_names[rank]} these {'fields' if rank == 2 else 'sections'}:"
                        if want_head not in head or rank in lists:
                            self.error(path, s, f"one {rank_names[rank]} rule per contract, headed '… {want_head}'; mark optional entries instead of adding MAY rules")
                        lists[rank] = self.entries(text)
                if rank < last_rank:
                    self.error(path, s, f"{rank_names[rank]} appears after {rank_names[last_rank]}")
                last_rank = max(last_rank, rank)
            if not rules or not re.search(r"\btitle (MUST|SHOULD)", rules[0].text):
                self.error(path, sec[0], "the first tagged rule is the title rule")
            identifies = any(re.search(r"\bidentify\b", r.text.splitlines()[0]) for r in rules)

        # suggested document
        context_rows, sections = [], []
        sec = doc.section(2, "Suggested document")
        if sec:
            fence_lines = [i for i in range(sec[0], sec[1]) if doc.code[i]]
            outside = [i for i in range(sec[0], sec[1]) if not doc.code[i] and doc.lines[i].strip()]
            if outside:
                self.error(path, outside[0], "Suggested document contains only its fenced block")
            body = [doc.lines[i] for i in fence_lines[1:-1]]
            text = "\n".join(body)
            for key, want in (("type", type_name), ("status", "draft")):
                if not re.search(rf"^{key}: {re.escape(want)}$", text, re.M):
                    self.error(path, sec[0], f"suggested frontmatter needs '{key}: {want}'")
            for key in ("title", "description"):
                if not re.search(rf"^{key}: ", text, re.M):
                    self.error(path, sec[0], f"suggested frontmatter needs '{key}:'")
            front = text.split("\n---", 1)[0] if text.startswith("---") else ""
            allowed = {"type", "title", "description", "status"} | ({"sources"} if requires_sources else set())
            extra = sorted(set(re.findall(r"^([a-z_]+):", front, re.M)) - allowed)
            if extra:
                self.error(path, sec[0], f"suggested frontmatter carries only type, title, description, status, and sources when the contract requires it; found {extra}")
            if requires_sources and "sources" not in extra and not re.search(r"^sources:", front, re.M):
                self.error(path, sec[0], "the contract requires `sources`, so the suggested frontmatter carries it")
            has_context = "| Context | Value |" in text
            if has_context != identifies:
                self.error(path, sec[0], "a Context table is present exactly when the contract identifies fields")
            in_ctx = False
            for line in body:
                if line.startswith("| Context | Value |"):
                    in_ctx = True
                    continue
                if in_ctx:
                    if not line.startswith("|"):
                        in_ctx = False
                    elif not line.startswith("| ---"):
                        context_rows.append(line.split("|")[1].strip())
                if line.startswith("## "):
                    sections.append(line[3:].strip())
            shared = [s for s in sections if s in SUPPORTING_SECTIONS]
            if shared != [s for s in SUPPORTING_SECTIONS if s in shared]:
                self.error(path, sec[0], f"supporting sections out of order: {shared}")
            if shared and sections[-len(shared):] != shared:
                self.error(path, sec[0], "supporting sections come last")
            if lists.get(2, []) != context_rows:
                self.error(path, sec[0], f"Context rows {context_rows} must match the identified fields {lists.get(2, [])}")
            own = [s for s in sections if s not in SUPPORTING_SECTIONS or s in lists.get(3, [])]
            if lists.get(3, []) != own:
                self.error(path, sec[0], f"suggested sections {own} must match the included sections {lists.get(3, [])}")

        # writing guidance
        sec = doc.section(2, "Writing guidance")
        if sec:
            h3 = [(i, t) for i, t in doc.headings(3) if sec[0] <= i < sec[1]]
            names = [t for _, t in h3]
            for banned in ("Context", "Sections"):
                if banned in names:
                    self.error(path, sec[0], f"'### {banned}' restates the contract; move any extra guidance into a topic subsection")
            if "Neighboring concepts" in names:
                self.error(path, sec[0], "'### Neighboring concepts' relists profile links; link from the contract or guidance instead")
            self.keywords_forbidden(doc, sec[0], sec[1], "Writing guidance")
        return rules

    # ---- links -----------------------------------------------------------
    def links(self, docs: list[Doc]) -> None:
        anchors: dict[Path, set[str]] = {}
        for d in docs:
            anchors[d.path.resolve()] = {
                re.sub(r"[^\w\s-]", "", t.lower()).strip().replace(" ", "-")
                for lvl in range(1, 7)
                for _, t in d.headings(lvl)
            }
        for d in docs:
            for i, line in enumerate(d.lines):
                if d.code[i]:
                    continue
                for m in re.finditer(r"\]\(([^)\s<>]+)\)", re.sub(r"`[^`]*`", "", line)):
                    target = m.group(1)
                    if re.match(r"[a-z]+:", target):
                        continue
                    path, _, anchor = target.partition("#")
                    tp = (d.path.parent / path).resolve() if path else d.path.resolve()
                    if not tp.exists():
                        self.error(d.path, i, f"broken link {target}")
                    elif anchor and tp in anchors and anchor not in anchors[tp]:
                        self.error(d.path, i, f"broken anchor {target}")

    def named_links(self, profile: Doc, modules: list[Doc], templates: list[Doc]) -> None:
        names: set[str] = set()
        for src in [profile] + modules:
            sec = src.section(2, "Named links")
            if not sec:
                continue
            for i in range(sec[0], sec[1]):
                line = src.lines[i]
                if line.startswith("|") and not line.startswith("| ---") and not line.startswith("| Named link |"):
                    cells = line.split("|")
                    name = cells[1].strip()
                    extends = cells[2].strip().startswith("Also:")
                    if extends and (src is profile or name not in names):
                        self.error(src.path, i, f"named link '{name}' extends no profile named link")
                    elif not extends and name in names:
                        self.error(src.path, i, f"named link '{name}' is defined in more than one table; a module row that extends it begins 'Also:'")
                    names.add(name)
        if not names:
            self.error(profile.path, 0, "no Named links table found")
            return
        first_h2 = profile.headings(2)[0][0] if profile.headings(2) else 0
        for d in templates + [profile] + modules:
            for i, line in enumerate(d.lines):
                if d.code[i] or (d is profile and i < first_h2):
                    continue
                for m in re.finditer(r"\*\*([a-z][a-z ]*[a-z])\*\*", line):
                    if m.group(1) not in names:
                        self.warn(d.path, i, f"bold lowercase '{m.group(1)}' is not a named link")

    def retired(self) -> set[str]:
        doc = Doc.load(README)
        sec = doc.section(3, "Retired identifiers")
        if not sec:
            self.error(README, 0, "missing '### Retired identifiers'")
            return set()
        tags = {f"{a}-{b}" for i in range(*sec) for a, b in TAG_REF.findall(doc.lines[i])}
        if not tags:
            # Before 1.0 nothing is retired, so identifiers run 1..n in document order.
            counters: dict[str, int] = {}
            for tag, rule in self.rules.items():
                prefix, _, num = tag.rpartition("-")
                counters[prefix] = counters.get(prefix, 0) + 1
                if int(num) != counters[prefix]:
                    self.error(rule.path, rule.line, f"{tag}: expected {prefix}-{counters[prefix]}; renumber in document order")
        for tag in tags & set(self.rules):
            r = self.rules[tag]
            self.error(r.path, r.line, f"{tag} is retired and must not be reused")
        return tags

    def references(self, docs: list[Doc], retired_tags: set[str]) -> None:
        for d in docs:
            for i, line in enumerate(d.lines):
                for m in TAG_REF.finditer(line):
                    prefix, num = m.group(1), m.group(2)
                    if prefix in {"ISO", "IEC", "RFC", "UTF"} or (not prefix.startswith("P-") and prefix not in {c for _, c in TYPES.values()}):
                        continue
                    tag = f"{prefix}-{num}"
                    if tag in retired_tags:
                        self.error(d.path, i, f"reference to retired rule {tag}")
                    elif tag not in self.rules:
                        self.error(d.path, i, f"reference to unknown rule {tag}")

    def vocabulary(self, docs: list[Doc]) -> None:
        for d in docs:
            for i, line in enumerate(d.lines):
                for pattern, msg in BANNED:
                    if msg and pattern.search(line):
                        self.error(d.path, i, f"vocabulary: {msg}")

    def concept_types(self, profile: Doc, modules: list[Doc]) -> None:
        declared: dict[str, Path] = {}
        for src in [profile] + modules:
            sec = src.section(2, "Concept types")
            if not sec:
                if src is not profile:
                    self.error(src.path, 0, "a module needs a '## Concept types' table")
                continue
            for i in range(sec[0], sec[1]):
                m = re.match(r"\| \[`([^`]+)`\]", src.lines[i])
                if m:
                    if m.group(1) in declared:
                        self.error(src.path, i, f"type {m.group(1)} is declared in more than one Concept types table")
                    declared[m.group(1)] = src.path
        want = {name for name, _ in TYPES.values()}
        for name in sorted(want - set(declared)):
            self.error(profile.path, 0, f"type {name} is not declared in the profile or a module")
        for name in sorted(set(declared) - want):
            self.error(declared[name], 0, f"type {name} has no template")

    def examples(self, templates: list[Doc]) -> None:
        text = EXAMPLE.read_text()
        lower = text.lower()
        for d in templates:
            for i, line in enumerate(d.lines):
                for m in re.finditer(r"\[([^\]]+)\]\(<[^>]*>\)", line):
                    name = m.group(1)
                    if name.startswith("<") or name.lower() in {"link"}:
                        continue
                    if name.lower() not in lower:
                        self.warn(d.path, i, f"example name '{name}' is not in example.md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--warn-only", action="store_true", help="report errors without failing")
    parser.add_argument("files", nargs="*", help="limit template anatomy findings to these files")
    args = parser.parse_args()

    lint = Linter()
    profile = Doc.load(PROFILE)
    first_h2 = profile.headings(2)[0][0] if profile.headings(2) else 0
    lint.collect_rules(profile, first_h2, len(profile.lines), None)
    modules: list[Doc] = []
    for stem, area in MODULE_AREAS.items():
        path = MODULES / f"{stem}.md"
        if not path.exists():
            lint.error(MODULES, 0, f"missing module {stem}.md")
            continue
        mod = Doc.load(path)
        modules.append(mod)
        h2 = mod.headings(2)
        lint.collect_rules(mod, h2[0][0] if h2 else 0, len(mod.lines), None, {area})
    for path in sorted(MODULES.glob("*.md")):
        if path.stem not in MODULE_AREAS:
            lint.error(path, 0, "unknown module file")
    lint.concept_types(profile, modules)

    template_paths = sorted(TEMPLATES.glob("*.md"))
    for p in template_paths:
        if p.stem not in TYPES:
            lint.error(p, 0, "unknown template file")
    missing = [s for s in TYPES if not (TEMPLATES / f"{s}.md").exists()]
    for s in missing:
        lint.error(TEMPLATES, 0, f"missing template {s}.md")

    for p in template_paths:
        if p.stem in TYPES:
            lint.template(p)
    retired = lint.retired()

    # keywords outside normative homes
    example = Doc.load(EXAMPLE)
    lint.keywords_forbidden(example, 0, len(example.lines), "the running example")

    docs = [profile, example] + modules + [Doc.load(p) for p in template_paths] + [Doc.load(ROOT / "README.md"), Doc.load(SRC / "SKILL.md")]
    lint.links(docs)
    lint.vocabulary([d for d in docs if d.path.name != "README.md" or d.path.parent != ROOT])
    lint.examples([Doc.load(p) for p in template_paths])
    lint.named_links(profile, modules, [Doc.load(p) for p in template_paths])
    lint.references([d for d in docs if d.path.name != "README.md"], retired)

    findings = lint.findings
    if args.files:
        keep = {Path(f).resolve() for f in args.files}
        findings = [f for f in findings if f.path.resolve() in keep]
    for f in sorted(findings, key=lambda f: (str(f.path), f.line)):
        print(f)
    errors = sum(1 for f in findings if f.level == "ERROR")
    warnings = len(findings) - errors
    print(f"{errors} error(s), {warnings} warning(s)")
    return 1 if errors and not args.warn_only else 0


if __name__ == "__main__":
    sys.exit(main())
