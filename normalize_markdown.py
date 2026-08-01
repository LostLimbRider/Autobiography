#!/usr/bin/env python3
"""
Reedsy Markdown Normalizer
Fixes formatting issues in Markdown files for Reedsy Studio compatibility.

Usage: python3 normalize_markdown.py [--dry-run]
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path('/home/uber/Apps/Autobiography')
SKIP_DIRS = {'.git', 'ARCHIVE', '__pycache__'}


def remove_bold_from_headers(line):
    """Convert # **Header** to # Header"""
    return re.sub(r'^(#{1,6})\s+\*\*(.+?)\*\*\s*$', r'\1 \2', line)


def demote_h1_to_h2(line):
    """Convert # Header to ## Header (all H1s become H2)"""
    if line.startswith('# ') and not line.startswith('## '):
        return '#' + line
    return line


def convert_tables(lines):
    """Convert GitHub-style pipe tables to bullet lists."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if '|' in stripped and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if re.match(r'^[\|\s\-:]+$', next_line) and '---' in next_line:
                headers = [h.strip().strip('*') for h in stripped.split('|') if h.strip()]
                i += 2

                if len(headers) == 2:
                    while i < len(lines) and '|' in lines[i].strip():
                        row = lines[i].strip()
                        cells = [c.strip().strip('*') for c in row.split('|') if c.strip()]
                        if len(cells) >= 2:
                            result.append(f'- **{cells[0]}** -- {cells[1]}')
                        i += 1
                else:
                    while i < len(lines) and '|' in lines[i].strip():
                        row = lines[i].strip()
                        cells = [c.strip().strip('*') for c in row.split('|') if c.strip()]
                        if cells:
                            parts = [f'{headers[j]}: {cells[j]}' if j < len(cells) else ''
                                     for j in range(len(headers))]
                            result.append('- ' + ' | '.join(p for p in parts if p))
                        i += 1
                continue
        result.append(line)
        i += 1
    return result


def remove_html_comments(lines):
    """Remove HTML comments."""
    return [re.sub(r'<!--.*?-->', '', line) for line in lines]


def normalize_spacing(lines):
    """Normalize blank lines - max 2 consecutive blank lines."""
    result = []
    blank_count = 0
    for line in lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)
    return result


def normalize_file(filepath):
    """Apply all normalizations to a file. Returns True if modified."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ERROR reading {filepath}: {e}")
        return False

    lines = content.split('\n')

    lines = [remove_bold_from_headers(line) for line in lines]
    lines = [demote_h1_to_h2(line) for line in lines]
    lines = convert_tables(lines)
    lines = remove_html_comments(lines)
    lines = normalize_spacing(lines)

    new_content = '\n'.join(lines)

    if new_content != content:
        filepath.write_text(new_content, encoding='utf-8')
        return True
    return False


def main():
    dry_run = '--dry-run' in sys.argv

    md_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith('.md'):
                md_files.append(Path(root) / f)

    md_files.sort()

    print(f"Found {len(md_files)} Markdown files to normalize")
    if dry_run:
        print("DRY RUN - no files will be modified\n")

    modified = 0
    for filepath in md_files:
        rel = filepath.relative_to(REPO_ROOT)
        try:
            if dry_run:
                content = filepath.read_text(encoding='utf-8')
                lines = content.split('\n')
                lines = [remove_bold_from_headers(line) for line in lines]
                lines = [demote_h1_to_h2(line) for line in lines]
                lines = convert_tables(lines)
                new_content = '\n'.join(lines)
                if new_content != content:
                    print(f"  WOULD FIX: {rel}")
                    modified += 1
                else:
                    print(f"  OK: {rel}")
            else:
                if normalize_file(filepath):
                    print(f"  FIXED: {rel}")
                    modified += 1
                else:
                    print(f"  OK: {rel}")
        except Exception as e:
            print(f"  ERROR: {rel} - {e}")

    print(f"\n{'Would modify' if dry_run else 'Modified'}: {modified} files")


if __name__ == '__main__':
    main()
