#!/usr/bin/env python3
"""
Lost Limb Riders — Transactional Operations Layer Validator

Checks every .md file in the transactional_operations layer for:
  1. Filename pattern   DEPT-TYPE-NNN-Descriptive-Name.md
  2. Required metadata block fields
  3. Cross-references that resolve to real files (ID tokens like GOV-POL-001)
  4. House-style typography: curly apostrophes and smart double quotes,
     no straight quotes (' or ") anywhere in a document

Layer conventions that are intentionally NOT enforced here:
  - `---` separators after the metadata block and before "End of" (established style)
  - ```text fenced blocks (used by GOV-POL-001, MASTER-INDEX, etc.)

Exit code 0 when all checks pass; 1 when any issue is found.

Run:  python3 validate_transactional_layer.py [--fix]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LAYER = Path(__file__).resolve().parent
ALLOWED_DIRS = {
    "00-START-HERE", "01-GOVERNANCE", "02-ADMINISTRATION", "03-HUMAN-RESOURCES",
    "04-CONTRACTORS", "05-FINANCE", "06-EVENTS", "07-PROGRAMS", "08-VOLUNTEERS",
    "09-SAFETY-RISK", "10-FUNDRAISING", "11-GRANTS", "12-COMPLIANCE",
    "13-FORMS-AND-TEMPLATES", "14-RECORDS-MANAGEMENT",
}

REQUIRED_META = [
    "Document ID", "Document Title", "Department", "Document Type",
    "Version", "Effective Date", "Review Date", "Document Owner",
    "Approving Authority", "Supersedes", "Related Documents",
    "Related Forms", "Record Classification", "Retention Requirement",
]

# Filenames: DEPT-TYPE-NNN-Description.md where DEPT is 2-4 letters (HR, FIN, GOV...)
# and TYPE is 2-8 letters (POL, PROC, FORM, CLOSE, FIN, EXP, IRS, MATRIX...)
FILE_PATTERN = re.compile(
    r"^[A-Z]{2,4}-[A-Z]{2,8}-\d{3}-.+\S$"
)

# Any document ID token used in cross-references
ID_TOKEN = re.compile(r"\b[A-Z]{2,4}-[A-Z]{2,8}-\d{3}\b")

EXPECTED_DIR_FILES = {
    "00-START-HERE": ["MASTER-INDEX.md", "MIGRATION-MAP.md", "TRANSACTION-MAP.md"],
    "12-COMPLIANCE": [
        "CMP-POL-001", "CMP-IRS-001", "CMP-IA-001", "CMP-CAL-001",
        "CMP-CHK-001", "CMP-CHK-002", "CMP-PROC-001", "CMP-REF-001",
    ],
    "13-FORMS-AND-TEMPLATES": ["00-FORMS-INDEX.md"],
}

issues: list[str] = []
fixed_files: set[Path] = set()


def walk_files() -> list[Path]:
    return sorted(
        p
        for p in LAYER.rglob("*.md")
        if p.parent.name in ALLOWED_DIRS and p.parent.parent == LAYER
    )


def check_filename(p: Path) -> None:
    stem = p.stem
    if p.parent.name == "00-START-HERE":
        return
    if stem.startswith(("00-", "01-")) and p.parent.name == "13-FORMS-AND-TEMPLATES":
        return
    if not FILE_PATTERN.match(stem):
        issues.append(f"[FILE-NAME] {p.relative_to(LAYER)}: does not match DEPT-TYPE-NNN-Name.md")


def check_metadata(text: str, p: Path) -> None:
    for field in REQUIRED_META:
        if f"{field}:" not in text:
            issues.append(f"[META] {p.relative_to(LAYER)}: missing '{field}'")


def check_cross_refs(text: str, p: Path, known_ids: set[str]) -> None:
    if p.parent.name == "00-START-HERE":
        return  # planning docs reference legacy and planned IDs by design
    own_id = ""
    m = re.search(r"\*\*Document ID:\*\*\s*(\S+)", text)
    if m:
        own_id = m.group(1)
    for tok in sorted(set(ID_TOKEN.findall(text))):
        if tok == own_id:
            continue  # the file's own Document ID is not a cross-reference
        if tok not in known_ids:
            issues.append(f"[REF] {p.relative_to(LAYER)}: ID '{tok}' referenced but file not found")


def fix_typography(text: str) -> str:
    out = []
    for ch in text:
        if ch == "'":
            out.append("\u2019")
        elif ch == '"':
            prev = out[-1] if out else ""
            if prev in ("", " ", "\t", "\n", "(", "[", "{", "\u2014", "\u2013", ":", "-"):
                out.append("\u201c")
            else:
                out.append("\u201d")
        else:
            out.append(ch)
    return "".join(out)


def check_typography(text: str, p: Path, fix: bool) -> None:
    rel = p.relative_to(LAYER)
    if "'" in text or '"' in text:
        count = text.count("'") + text.count('"')
        issues.append(f"[QUOTE] {rel}: {count} straight quote(s) found")
        if fix:
            p.write_text(fix_typography(text), encoding="utf-8")
            fixed_files.add(p)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the transactional operations layer.")
    parser.add_argument("--fix", action="store_true", help="Rewrite straight quotes to curly in place")
    args = parser.parse_args()

    files = walk_files()
    if not files:
        issues.append("[GLOBAL] no .md files found")
        return 1

    known_ids = set()
    for p in files:
        m = ID_TOKEN.search(p.stem)
        if m:
            known_ids.add(m.group(0))

    for p in files:
        text = p.read_text(encoding="utf-8")
        check_filename(p)
        check_metadata(text, p)
        check_cross_refs(text, p, known_ids)
        check_typography(text, p, args.fix)

    for dirname, expected in EXPECTED_DIR_FILES.items():
        d = LAYER / dirname
        if not d.exists():
            issues.append(f"[DIR] missing directory {dirname}/")
            continue
        for f in expected:
            if f.endswith(".md"):
                found = (d / f).exists()
            else:
                found = any(p.stem.startswith(f) for p in d.iterdir())
            if not found:
                issues.append(f"[DIR] {dirname}/ missing expected file {f}")

    if args.fix and fixed_files:
        print(f"Fixed typography in {len(fixed_files)} file(s):")
        for f in sorted(fixed_files):
            print(f"  - {f.relative_to(LAYER)}")

    if issues:
        print(f"VALIDATION FAILED — {len(issues)} issue(s)")
        for issue in sorted(set(issues)):
            print(f"  {issue}")
        return 1
    print(f"VALIDATION PASSED — {len(files)} file(s) OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
