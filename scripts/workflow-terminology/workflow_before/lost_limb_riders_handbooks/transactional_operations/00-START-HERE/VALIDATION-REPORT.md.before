## Lost Limb Riders — Transactional Layer Validation Report

**Document ID:** VAL-REPORT-001
**Document Title:** Transactional Layer Validation Report
**Department:** Compliance
**Document Type:** REF
**Version:** 1.0
**Effective Date:** August 12, 2026
**Review Date:** August 2027
**Document Owner:** Compliance Officer
**Approving Authority:** Executive Director
**Supersedes:** None
**Related Documents:** MASTER-INDEX; MIGRATION-MAP; TRANSACTION-MAP; validate_transactional_layer.py; CMP-PROC-001
**Related Forms:** None
**Record Classification:** Compliance
**Retention Requirement:** Permanent (while in force)

---

## 1. Scope

Validation of the transactional operations layer, run August 12, 2026 with `python3 validate_transactional_layer.py` (Python 3.11.2, stdlib only).

## 2. Checks Performed

| Check | What It Verifies | Result |
|---|---|---|
| Filename pattern | Every file is `DEPT-TYPE-NNN-Name.md` | PASS |
| Metadata block | All 14 required header fields present | PASS |
| Cross-references | Every `DEPT-TYPE-NNN` token resolves to a real file | PASS |
| Typography | No straight quotes (’) or (“) anywhere; curly/smart required | PASS (after fix pass) |
| Directory completeness | Required files present in 00-START-HERE, 12-COMPLIANCE, 13-FORMS-AND-TEMPLATES | PASS |

## 3. Result

**VALIDATION PASSED — 128 file(s) OK**

## 4. Fixes Applied During Validation

- **Quote pass (`--fix`):** 63 straight apostrophes and paired straight double quotes converted to curly (`’`/`“`/`”`) across the layer. House style now consistent with the organization’s manuscript conventions.
- **Legacy references corrected:** stale IDs from the original design updated to real files:
  - `SFT-SOP-001` → `SAF-POL-002` (Incident Reporting) — 4 files
  - `SFT-SOP-002` → `SAF-POL-001` (Risk Management) — 2 files
  - `SFT-REG-001` → `SAF-REG-001` (Incident Register) — 2 files
  - `FIN-PROC-003` → `FIN-EXP-002` (Reimbursement Procedure) — 2 files
  - `FIN-FORM-001` → `FIN-EXP-001` (Expense Report) — 1 file
- Planning docs (00-START-HERE) intentionally still reference legacy/planned IDs as a migration record and are exempt from cross-reference checks.

## 5. Intentionally Not Enforced

- `---` separators after the metadata block and before “End of” — established layer style.
- ```` ```text ```` fenced blocks — used by GOV-POL-001, MASTER-INDEX, and others.

## 6. Re-Running

```text
python3 validate_transactional_layer.py
python3 validate_transactional_layer.py --fix   # to auto-convert straight quotes
```

Run the validator after any layer change; it must pass before a file is treated as current.

---

**End of Report.**
