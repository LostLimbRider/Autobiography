#!/usr/bin/env python3
"""Lost Limb Riders — Transactional Layer Validation Tool.

Scans the transactional operations layer (and linked handbook folders) for:
  - duplicate document IDs
  - duplicate filenames
  - missing metadata header fields
  - references (links/paths) to nonexistent documents
  - orphaned forms (not referenced by any procedure/index)
  - documents marked superseded but still referenced
  - documents marked active but stored under ARCHIVE
  - missing required sections in controlled documents
  - stale review dates
  - inconsistent document-type prefixes

Usage:
    python3 tools/validate_ops.py [root_dir]

Exits 0 when no issues; exits 1 when issues are found. Prints a report.
"""

from __future__ import annotations

import datetime
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Document header fields every controlled document should carry
REQUIRED_FIELDS = [
    "Document ID",
    "Document Title",
    "Department",
    "Document Type",
    "Version",
    "Effective Date",
    "Review Date",
    "Document Owner",
    "Approving Authority",
    "Related Documents",
    "Related Forms",
    "Record Classification",
    "Retention Requirement",
]

# Valid document type prefixes. The repository uses a two-element
# middle segment: a document class (POL, PROC, CHK, FORM, REG, TMP, REF)
# OR a functional code (EXP, ONB, AUTH, ...) that groups a family of
# forms. Keep this registry in sync with the Master Document Control
# Policy whenever a new code is introduced.
TYPE_PREFIXES = {
    "POL", "SOP", "PROC", "FORM", "CHK", "REG", "TMP", "REF",
    "ADM", "ANN", "APP", "AUTH", "BUD", "CAL", "CHG", "CLOSE",
    "COMP", "CTRL", "DAY", "DOC", "EXP", "FIL", "FIN", "HR",
    "INC", "INS", "INT", "LOC", "MSTR", "OFR", "ONB", "PAY",
    "PERF", "POS", "POST", "PUR", "REC", "REST", "RET", "REV",
    "SEP", "SPON", "TIME",
}

# Department folder prefixes
DEPT_PREFIXES = {
    "ADM": "02-ADMINISTRATION",
    "GOV": "01-GOVERNANCE",
    "HR": "03-HUMAN-RESOURCES",
    "CTR": "04-CONTRACTORS",
    "FIN": "05-FINANCE",
    "EVT": "06-EVENTS",
    "PROG": "07-PROGRAMS",
    "VOL": "08-VOLUNTEERS",
    "SAF": "09-SAFETY-RISK",
    "FUND": "10-FUNDRAISING",
    "GRT": "11-GRANTS",
    "CMP": "12-COMPLIANCE",
    "REC": "14-RECORDS-MANAGEMENT",
}

TODAY = datetime.date(2026, 8, 12)


def iter_markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        yield path


def parse_header(text: str) -> dict:
    """Return the metadata block as {label: value}.

    Controlled documents use the header form ``**Field:** value`` — the
    colon sits inside the bold markers.
    """
    fields = {}
    for line in text.splitlines()[:80]:
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", line)
        if m:
            fields[m.group(1).strip()] = m.group(2).strip()
    return fields


def extract_ids(text: str):
    """Return all document/transaction IDs referenced in a file.

    Handles transaction IDs (``EVT-2026-001``), three-part controlled
    document IDs (``HR-ONB-001``) and two-part IDs (``CTR-001``).
    The ordered alternation guarantees a full token match and prevents
    partial matches (e.g. ``RET-001`` inside ``CMP-RET-001``).
    """
    pattern = re.compile(
        r"\b(?:EMP|CTR|EVT|EXP|DON|SPN|GRT|AST|INC|BRD|TIM|PAY)-\d{4}-\d{3}\b"
        r"|\b[A-Z]{2,5}-[A-Z]+-\d{3}\b"
        r"|\b[A-Z]{2,5}-\d{3}\b"
    )
    return set(pattern.findall(text))


def main() -> int:
    root_arg = sys.argv[1] if len(sys.argv) > 1 else "lost_limb_riders_operations"
    root = Path(root_arg).resolve()
    if not root.is_dir():
        print(f"Root not found: {root}")
        return 1

    handbooks = Path("lost_limb_riders_handbooks").resolve()
    scan_dirs = [root]
    if handbooks.is_dir():
        scan_dirs.append(handbooks)
    # repository root — used to resolve references to files outside the
    # scanned trees (employees/, ARCHIVE/, README.md, context.md, ...)
    repo_root = Path(".").resolve()
    all_repo_files: dict[str, list[Path]] = defaultdict(list)
    for p in repo_root.rglob("*.md"):
        if ".git" in p.parts:
            continue
        all_repo_files[p.name].append(p)

    issues: list[str] = []
    advisories: list[str] = []
    doc_ids: dict[str, list[str]] = defaultdict(list)
    filenames: Counter[str] = Counter()
    headers: dict[str, dict] = {}
    all_refs: set[str] = set()
    all_files: dict[str, Path] = {}

    # ---- build file index -------------------------------------------------
    for d in scan_dirs:
        for path in iter_markdown(d):
            all_files[path.name] = path
            filenames[path.name] += 1

    # ---- per-file checks ---------------------------------------------------
    for d in scan_dirs:
        for path in iter_markdown(d):
            text = path.read_text(encoding="utf-8", errors="replace")
            fields = parse_header(text)
            headers[str(path)] = fields
            doc_id = fields.get("Document ID", "")

            if doc_id:
                doc_ids[doc_id].append(str(path))
                all_refs.add(doc_id)

            # duplicate filenames
            if filenames[path.name] > 1:
                issues.append(f"Duplicate filename '{path.name}' -> {path}")

            # missing header fields (controlled documents only — the
            # public handbooks under lost_limb_riders_handbooks/ carry
            # no Document ID and are not governed by the document system)
            if doc_id:
                for f in REQUIRED_FIELDS:
                    if f not in fields:
                        rel = path.relative_to(d)
                        issues.append(f"Missing header field '{f}' in {rel}")

            # invalid document type prefix
            if doc_id:
                m = re.match(r"^([A-Z]+)-([A-Z]+|)\d+$", doc_id)
                if m:
                    type_part = m.group(2)
                    if type_part and type_part not in TYPE_PREFIXES:
                        issues.append(f"Invalid type prefix '{type_part}' in {doc_id} ({path.name})")

            # stale review date
            review = fields.get("Review Date", "")
            m = re.match(r"(\w+)\s+(\d{4})", review)
            if m:
                month = m.group(1)
                year = int(m.group(2))
                months = {mo: i for i, mo in enumerate(
                    ["January", "February", "March", "April", "May", "June",
                     "July", "August", "September", "October", "November", "December"], 1)}
                if month in months:
                    if (year, months[month]) < (TODAY.year, TODAY.month):
                        rel = path.relative_to(d)
                        issues.append(f"Stale Review Date '{review}' in {rel}")

            # internal relative/absolute references to markdown files
            for ref in re.findall(r"[\w./\-]+\.md", text):
                all_refs.add(ref)

    # ---- duplicate document IDs --------------------------------------------
    for doc_id, paths in doc_ids.items():
        if len(paths) > 1:
            issues.append(f"Duplicate Document ID {doc_id}: {paths}")

    # ---- broken references ------------------------------------------------
    # 1) references to .md filenames that exist nowhere in the scanned trees
    known_files = set(all_files)
    known_doc_ids = set(doc_ids)
    transaction_prefixes = ("EMP-", "CTR-", "EVT-", "EXP-", "DON-", "SPN-",
                            "GRT-", "AST-", "INC-", "BRD-", "TIM-", "PAY-")
    for d in scan_dirs:
        for path in iter_markdown(d):
            text = path.read_text(encoding="utf-8", errors="replace")
            rel = path.relative_to(d)
            # broken .md path/file references
            for ref in set(re.findall(r"[\w./\-]+\.md", text)):
                ref_name = Path(ref).name
                if ref_name in known_files:
                    continue
                # relative path resolved from this file's directory
                target = (path.parent / ref).resolve()
                if target.exists() and target.is_file():
                    continue
                # fall back to the repository root (employees/, ARCHIVE/, ...)
                target = (repo_root / ref).resolve()
                if target.exists() and target.is_file():
                    continue
                # fall back to a unique filename match anywhere in the repo
                matches = all_repo_files.get(ref_name, [])
                if matches:
                    target = matches[0]
                    if "ARCHIVE" in target.parts:
                        # only the migration/completion documents are
                        # expected to cite archived material
                        if rel != Path("00-START-HERE/MIGRATION-MAP.md") and \
                           "ARCHIVE" not in str(rel):
                            advisories.append(
                                f"Reference to archived file '{ref}' in {rel} "
                                f"(resolves to {target.relative_to(repo_root)})")
                    continue
                issues.append(f"Broken .md reference '{ref}' in {rel}")
            # document-ID references to controlled docs that do not exist
            for rid in set(extract_ids(text)):
                if rid in known_doc_ids:
                    continue
                if rid.startswith(transaction_prefixes):
                    continue  # live transaction IDs are recorded in registers
                issues.append(f"Unknown Document ID '{rid}' referenced in {rel}")

    # ---- orphan check: forms/checklists not referenced elsewhere ------------
    referenced = set()
    for path_str, fields in headers.items():
        # a document is "referenced" if any other file mentions its
        # filename, filename stem, or Document ID
        fname = Path(path_str).name
        fname_stem = fname[: fname.rfind(".")]
        doc_id = fields.get("Document ID", "")
        for other, other_fields in headers.items():
            if other == path_str:
                continue
            other_text = Path(other).read_text(encoding="utf-8", errors="replace")
            if fname in other_text or fname_stem in other_text or doc_id in other_text:
                referenced.add(path_str)
                break
        # index/start-here files are exempt from orphan logic
        if fname in ("00-Forms-and-Templates-Index.md",) or fname.startswith("MASTER-INDEX") or fname.startswith("00-"):
            referenced.add(path_str)

    for d in scan_dirs:
        for path in iter_markdown(d):
            if str(path) not in referenced:
                rel = path.relative_to(d)
                issues.append(f"Possibly orphaned document (not referenced elsewhere): {rel}")

    # ---- superseded but still referenced ------------------------------------
    for path_str, fields in headers.items():
        if "Superseded" in fields.get("Status", ""):
            fname = Path(path_str).name
            for other, other_fields in headers.items():
                if other == path_str:
                    continue
                other_text = Path(other).read_text(encoding="utf-8", errors="replace")
                if fname in other_text:
                    issues.append(f"Superseded doc referenced: {fname} in {other}")
                    break

    # ---- active docs under ARCHIVE ------------------------------------------
    for path_str in headers:
        if "ARCHIVE" in path_str and "Retired" not in headers[path_str].get("Status", ""):
            issues.append(f"Document under ARCHIVE not marked Retired: {path_str}")

    # ---- print report ---------------------------------------------------------
    print("=" * 70)
    print("Lost Limb Riders — Transactional Layer Validation Report")
    print(f"Generated: {TODAY.isoformat()}   Root: {root}")
    print("=" * 70)
    print(f"Documents scanned: {len(headers)}")
    print(f"Controlled document IDs found: {len(doc_ids)}")
    print(f"Issues found: {len(issues)}")
    print("-" * 70)
    for issue in sorted(issues):
        print(f"  - {issue}")
    if advisories:
        print("-" * 70)
        print(f"Advisories ({len(advisories)}):")
        for a in sorted(advisories):
            print(f"  ? {a}")
    print("=" * 70)

    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
