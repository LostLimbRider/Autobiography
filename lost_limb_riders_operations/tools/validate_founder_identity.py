#!/usr/bin/env python3
"""Lost Limb Riders — Founder Identity Regression Guard.

Protects the FOUNDER IDENTITY invariant defined in AGENTS.md:

  - Public organizational documentation must identify the founder as
    "J. Thompson" where the abbreviated public founder identity is required.
  - Unresolved founder-name placeholders (`[founder name]`, `[Founder Name]`,
    `[FOUNDER NAME]`, `[insert founder name]`, ...) must not ship in
    production documentation.
  - Founder imagery must reference the single canonical professional headshot
    asset `assets/images/FOUNDER_HEADSHOT.png`, never a nonexistent or
    duplicated image path.

ARCHIVE is treated as non-production and is intentionally excluded so that
historical records can reference the original defect without failing the
guard. Production paths are everything outside `.git/` and `ARCHIVE/`.

Usage:
    python3 lost_limb_riders_operations/tools/validate_founder_identity.py

Exits 0 when no issues; exits 1 when issues are found. Prints a report.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

CANONICAL_HEADSHOT = "assets/images/FOUNDER_HEADSHOT.png"
CANONICAL_FOUNDER_NAME = "J. Thompson"

LEGACY_HEADSHOT_PLACEHOLDER = "chapter-13-founder-headshot-placeholder.svg"

# AGENTS.md documents the founder-identity invariant itself, so it must
# literally show the banned placeholder spellings. It is the definition of
# the rule, not a production organizational document, and is therefore
# exempt from placeholder detection.
INVARIANT_DEFINITION_DOC = "AGENTS.md"

# Any bracketed founder-name placeholder is banned in production docs.
FOUNDER_PLACEHOLDER_RE = re.compile(
    r"\[[ \t]*(?:insert[ \t]+)?founder[ \t]+"
    r"(?:name|bio|photo|image)[ \t]*\]",
    re.IGNORECASE,
)

# Markdown image + HTML <img> links that reference the canonical headshot
# (also catches legacy SVG placeholder references for resolution checks).
MARKDOWN_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_IMG_RE = re.compile(r"<img[^>]+src\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)


def iter_docs(root: Path) -> list[Path]:
    docs = []
    for path in sorted(root.rglob("*.md")):
        parts = path.parts
        if ".git" in parts or "ARCHIVE" in parts:
            continue
        docs.append(path)
    return docs


def resolve_link(path: Path, link: str) -> Path | None:
    link = link.strip().strip("<>")
    if not link or "://" in link or link.startswith("#") or link.startswith("data:"):
        return None
    return (path.parent / link).resolve()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    canonical = (REPO_ROOT / CANONICAL_HEADSHOT).resolve()
    if not canonical.is_file():
        errors.append(f"Canonical founder headshot missing: {CANONICAL_HEADSHOT}")
    else:
        warnings.append(f"Canonical founder headshot present: {CANONICAL_HEADSHOT}")

    docs = iter_docs(REPO_ROOT)
    for path in docs:
        rel = path.relative_to(REPO_ROOT)
        text = path.read_text(encoding="utf-8")
        is_invariant_doc = path.name == INVARIANT_DEFINITION_DOC and path.parent == REPO_ROOT

        if not is_invariant_doc:
            for match in FOUNDER_PLACEHOLDER_RE.finditer(text):
                errors.append(
                    f"{rel}: unresolved founder placeholder {match.group(0)!r} "
                    f"(canonical name: {CANONICAL_FOUNDER_NAME})"
                )

            if LEGACY_HEADSHOT_PLACEHOLDER in text:
                errors.append(
                    f"{rel}: legacy founder-headshot placeholder SVG reference "
                    f"({LEGACY_HEADSHOT_PLACEHOLDER}) must point to "
                    f"{CANONICAL_HEADSHOT}"
                )

        for regex in (MARKDOWN_LINK_RE, HTML_IMG_RE):
            for match in regex.finditer(text):
                link = match.group(1)
                lower = link.lower()
                if not any(k in lower for k in ("founder_headshot", "founder-headshot",
                                                "headshot", "portrait")):
                    continue
                target = resolve_link(path, link)
                if target is None:
                    continue
                if target == canonical:
                    continue
                if target.name.lower() in ("chapter-13-founder-headshot-placeholder.svg",):
                    errors.append(
                        f"{rel}: founder-image link still targets placeholder "
                        f"SVG instead of {CANONICAL_HEADSHOT}"
                    )
                    continue
                if not target.exists():
                    errors.append(
                        f"{rel}: founder-image reference does not resolve: "
                        f"{link!r} (expected {CANONICAL_HEADSHOT})"
                    )
                    continue
                if target != canonical:
                    warnings.append(
                        f"{rel}: founder-image reference points at non-canonical "
                        f"path {link!r}; canonical is {CANONICAL_HEADSHOT}"
                    )

    print("FOUNDER IDENTITY REGRESSION GUARD")
    print(f"Scan root: {REPO_ROOT}")
    print(f"Production documents scanned: {len(docs)}")
    print(f"Canonical founder name: {CANONICAL_FOUNDER_NAME}")
    print(f"Canonical headshot: {CANONICAL_HEADSHOT}")
    print()
    for warning in warnings:
        print(f"NOTE  {warning}")
    for error in errors:
        print(f"FAIL  {error}")

    print()
    if errors:
        print(f"RESULT: FAIL ({len(errors)} error(s))")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())