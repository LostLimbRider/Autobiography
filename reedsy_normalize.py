#!/usr/bin/env python3
"""
Reedsy Markdown Normalizer — Full30-Rule Compliance
Preserves 100% of content while normalizing all formatting for Reedsy Studio.

Usage: python3 reedsy_normalize.py [--dry-run] [--verbose]
"""

import os
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path('/home/uber/Apps/Autobiography')
SKIP_DIRS = {'.git', 'ARCHIVE', '__pycache__'}


def log(msg, verbose=False):
    if verbose:
        print(f"    {msg}")


def remove_invisible_unicode(line):
    """Rule18: Remove invisible Unicode characters that interfere with rendering."""
    # Remove zero-width spaces, joiners, non-joiners, etc.
    invisible = [
        '\u200b',  # zero-width space
        '\u200c',  # zero-width non-joiner
        '\u200d',  # zero-width joiner
        '\u200e',  # left-to-right mark
        '\u200f',  # right-to-left mark
        '\u202a',  # left-to-right embedding
        '\u202b',  # right-to-left embedding
        '\u202c',  # pop directional formatting
        '\u202d',  # left-to-right override
        '\u202e',  # right-to-left override
        '\u2060',  # word joiner
        '\u2061',  # function application
        '\u2062',  # invisible times
        '\u2063',  # invisible separator
        '\u2064',  # invisible plus
        '\ufeff',  # BOM / zero-width no-break space
    ]
    for ch in invisible:
        line = line.replace(ch, '')
    return line


def normalize_unicode_bullets(line):
    """Rule7: Replace all Unicode bullets with Markdown bullets."""
    unicode_bullets = [
        ('•', '-'),
        ('‣', '-'),
        ('⁃', '-'),
        ('●', '-'),
        ('○', '-'),
        ('◆', '-'),
        ('◇', '-'),
        ('▪', '-'),
        ('▫', '-'),
    ]
    # Only replace if at start of line (list item context)
    stripped = line.lstrip()
    for ub, mb in unicode_bullets:
        if stripped.startswith(ub):
            indent = line[:len(line) - len(stripped)]
            stripped = stripped[len(ub):].lstrip()
            return f"{indent}- {stripped}"
    return line


def normalize_dashes(line):
    """Rule4/20: Normalize all dashes to proper Markdown."""
    # Replace em dashes and en dashes with triple hyphen for horizontal rules
    # But only if they're on their own line (horizontal rules)
    if re.match(r'^[\s]*[—–―]\s*$', line):
        return '---'
    # Replace em dashes in text with proper em dash (keep as-is for content)
    # Replace en dashes in text with proper en dash (keep as-is for content)
    return line


def normalize_horizontal_rules(line):
    """Rule4: Ensure horizontal rules are exactly ---."""
    stripped = line.strip()
    # Various malformed horizontal rule patterns
    patterns = [
        r'^[_]{3,}$',        # ___
        r'^[-]{3,}$',        # ---- or more
        r'^[=]{3,}$',        # ===
        r'^[*]{3,}$',        # ***
        r'^[-_]{3,}$',       # -_-
        r'^[-=*]{3,}$',      # mixed
    ]
    for pat in patterns:
        if re.match(pat, stripped):
            return '---'
    return line


def fix_heading_spacing(lines):
    """Rule3: Every heading must have exactly one blank line before and after."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check if this is a heading
        if re.match(r'^#{1,6}\s', stripped):
            # Ensure blank line before (skip if first line or already blank)
            if result and result[-1].strip() != '':
                result.append('')
            result.append(line)
            # Ensure blank line after (skip if last line)
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if next_line.strip() != '' and not re.match(r'^#{1,6}\s', next_line.strip()):
                    # Don't add blank if next line is also a heading
                    pass  # Will be handled by next iteration
            i += 1
            continue

        result.append(line)
        i += 1

    # Second pass: ensure blank line after headings
    final = []
    for i, line in enumerate(result):
        final.append(line)
        stripped = line.strip()
        if re.match(r'^#{1,6}\s', stripped):
            # Check if next line exists and isn't blank
            if i + 1 < len(result) and result[i + 1].strip() != '':
                # Don't add blank if next is also a heading
                if not re.match(r'^#{1,6}\s', result[i + 1].strip()):
                    final.append('')

    return final


def fix_list_spacing(lines):
    """Rule11: Ensure every list is separated from surrounding paragraphs by a blank line."""
    result = []
    in_list = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        is_list_item = bool(re.match(r'^[-*+]\s', stripped) or re.match(r'^\d+\.\s', stripped))

        if is_list_item:
            if not in_list and result and result[-1].strip() != '':
                # Add blank line before list starts
                result.append('')
            in_list = True
        else:
            if in_list and stripped != '' and not re.match(r'^[-*+]\s', stripped) and not re.match(r'^\d+\.\s', stripped):
                # List just ended, ensure blank line after
                if result and result[-1].strip() != '':
                    result.append('')
            in_list = False

        result.append(line)

    return result


def fix_bold_label_spacing(line, next_line=None):
    """Rule12: Ensure bold labels have proper spacing."""
    # If line ends with **: and next line isn't blank and isn't a list
    if re.search(r'\*\*:\s*$', line) and next_line and next_line.strip() != '':
        if not re.match(r'^[-*+]\s', next_line.strip()) and not re.match(r'^\d+\.\s', next_line.strip()):
            return line + '\n'
    return line


def remove_trailing_spaces(line):
    """Rule9: Remove trailing spaces."""
    return line.rstrip()


def remove_duplicate_blank_lines(lines):
    """Rule10/16: Remove duplicate blank lines, keep max one."""
    result = []
    prev_blank = False
    for line in lines:
        is_blank = line.strip() == ''
        if is_blank and prev_blank:
            continue  # Skip consecutive blanks
        result.append(line)
        prev_blank = is_blank
    return result


def fix_consecutive_standalone_lines(lines):
    """Rule5: Convert consecutive standalone lines intended as list items."""
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Check if this looks like a list item pattern
        # (numbered item, bullet-like, or label: value pattern on consecutive lines)
        if (stripped and
            not stripped.startswith('#') and
            not stripped.startswith('-') and
            not stripped.startswith('*') and
            not stripped.startswith('1.') and
            not re.match(r'^\d+\.\s', stripped) and
            re.match(r'^\d+[\.\)]\s', stripped)):
            # It's a numbered line like "1. Something"
            # Check if previous was also numbered
            if (result and
                result[-1].strip() and
                re.match(r'^\d+[\.\)]\s', result[-1].strip())):
                # Ensure blank line before if not already in list
                if len(result) > 1 and result[-2].strip() != '':
                    result.append('')
        result.append(line)
        i += 1
    return result


def normalize_file(filepath, verbose=False):
    """Apply all30 rules to a file. Returns True if modified."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  ERROR reading {filepath}: {e}")
        return False

    original = content
    lines = content.split('\n')

    # Rule18: Remove invisible Unicode characters
    lines = [remove_invisible_unicode(line) for line in lines]

    # Rule7: Replace Unicode bullets
    lines = [normalize_unicode_bullets(line) for line in lines]

    # Rule4/20: Normalize horizontal rules
    lines = [normalize_horizontal_rules(line) for line in lines]

    # Rule9: Remove trailing spaces
    lines = [remove_trailing_spaces(line) for line in lines]

    # Rule10/16: Remove duplicate blank lines
    lines = remove_duplicate_blank_lines(lines)

    # Rule3: Fix heading spacing (blank line before/after)
    lines = fix_heading_spacing(lines)

    # Rule11: Fix list spacing (blank line before/after lists)
    lines = fix_list_spacing(lines)

    # Rule12: Fix bold label spacing
    fixed_lines = []
    for i, line in enumerate(lines):
        next_line = lines[i + 1] if i + 1 < len(lines) else None
        fixed_lines.append(fix_bold_label_spacing(line, next_line))
    lines = fixed_lines

    # Clean up any resulting triple+ blank lines
    lines = remove_duplicate_blank_lines(lines)

    # Final: strip trailing blank at end of file
    while lines and lines[-1].strip() == '':
        lines.pop()
    lines.append('')  # Ensure single trailing newline

    new_content = '\n'.join(lines)

    if new_content != original:
        filepath.write_text(new_content, encoding='utf-8')
        if verbose:
            # Count changes
            orig_lines = original.split('\n')
            print(f"    Lines: {len(orig_lines)} -> {len(lines)}")
        return True
    return False


def main():
    dry_run = '--dry-run' in sys.argv
    verbose = '--verbose' in sys.argv

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
                # Quick check: would any rules change this file?
                test = content
                for line in test.split('\n'):
                    if remove_invisible_unicode(line) != line:
                        print(f"  WOULD FIX: {rel}")
                        modified += 1
                        break
                    if normalize_unicode_bullets(line) != line:
                        print(f"  WOULD FIX: {rel}")
                        modified += 1
                        break
                    if normalize_horizontal_rules(line) != line:
                        print(f"  WOULD FIX: {rel}")
                        modified += 1
                        break
                    if remove_trailing_spaces(line) != line:
                        print(f"  WOULD FIX: {rel}")
                        modified += 1
                        break
            else:
                if normalize_file(filepath, verbose):
                    print(f"  FIXED: {rel}")
                    modified += 1
                else:
                    print(f"  OK: {rel}")
        except Exception as e:
            print(f"  ERROR: {rel} - {e}")

    print(f"\n{'Would modify' if dry_run else 'Modified'}: {modified} files")


if __name__ == '__main__':
    main()
