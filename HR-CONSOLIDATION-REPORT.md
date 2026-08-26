# **Lost Limb Riders — HR Documentation Consolidation Report**

**Document Type:** Consolidation Report (§XIII)
**Effective Date:** August 26, 2026
**Prepared By:** Document Control
**Approved By:** Executive Director

---

## 1. Purpose

This report documents the consolidation of all HR documentation into one canonical source of truth, per the executive directive. It identifies what changed, what was superseded, what references were repaired, and what the final state is.

---

## 2. Executive Summary

**Before consolidation:** Two HR documentation trees existed in the repository:
1. **Legacy numbered tree** (`lost_limb_riders_operations/03-HUMAN-RESOURCES/`) — 18 documents with flat numbered filenames and legacy IDs (HR-ADM-001, HR-PROC-001, etc.)
2. **Canonical `HR-*` tree** (`lost_limb_riders_handbooks/transactional_operations/03-HUMAN-RESOURCES/`) — 28 documents with the controlled `HR-*` ID scheme, a master index (HR-REF-002), and full lifecycle coverage.

**After consolidation:** The canonical `HR-*` tree is the single authoritative source. The legacy tree is marked superseded. All cross-references from other departmental documents have been repaired.

---

## 3. Canonical System (Authoritative)

**Location:** `lost_limb_riders_handbooks/transactional_operations/03-HUMAN-RESOURCES/`
**Master Index:** `HR-REF-002-HR-Packet-Index.md`
**Version:** 1.0
**Effective Date:** August 25, 2026

### Document Inventory (28 documents)

| ID | Title | Type |
|----|-------|------|
| HR-POL-001 | Employment Policy | Policy |
| HR-POL-002 | Employee Handbook | Policy |
| HR-EMP-001 | Employee Lifecycle Map | Reference |
| HR-REF-001 | Position Descriptions Index | Reference |
| HR-REF-002 | HR Packet — Master Index | Reference |
| HR-CHK-001 | Employer Setup Checklist | Checklist |
| HR-SOP-001 | Employer Setup SOP | SOP |
| HR-FORM-001 | Position Authorization Form | Form |
| HR-SOP-002 | Recruitment SOP | SOP |
| HR-FORM-002 | Employee Application Form | Form |
| HR-FORM-003 | Interview Evaluation Form | Form |
| HR-SOP-003 | Selection & Compensation Approval SOP | SOP |
| HR-FORM-004 | Offer Letter Template | Form |
| HR-FORM-005 | Position Compensation Worksheet | Form |
| HR-SOP-004 | Onboarding SOP | SOP |
| HR-CHK-002 | Employee Onboarding Checklist | Checklist |
| HR-FORM-006 | Payroll Setup Form | Form |
| HR-SOP-005 | Timekeeping SOP | SOP |
| HR-TIME-001 | Employee Time Record | Form |
| HR-CHK-003 | Personnel File Checklist | Checklist |
| HR-REG-001 | Employee Register | Register |
| HR-SOP-006 | Employee Separation SOP | SOP |
| HR-CHK-004 | Employee Separation Checklist | Checklist |
| HR-CHK-005 | Final Payroll Checklist | Checklist |
| HR-SOP-007 | Performance Review & Discipline SOP | SOP |
| HR-FORM-007 | Performance Review Form | Form |
| HR-FORM-008 | Disciplinary Action Form | Form |
| HR-FORM-009 | Separation Notice Form | Form |

**Lifecycle coverage:** Complete — employer setup, recruit, offer, onboard, time & pay, records, performance & discipline, separate.

**Cross-departmental links:**
- Finance: FIN-PROC-004 (Payroll Procedure), FIN-CHK-001 (Payroll Checklist), FIN-REG-004 (Payroll Register)
- Governance: GOV-POL-005 (Insider Compensation Approval), GOV-POL-004 (Conflict of Interest)
- Compliance: CMP-IA-001 (Iowa Compliance), CMP-IRS-001 (Federal Compliance)

---

## 4. Superseded System (Deprecated)

**Location:** `lost_limb_riders_operations/03-HUMAN-RESOURCES/`
**Status:** Superseded as of August 25, 2026
**Superseded By:** The canonical HR packet (see section 3)

### Document Inventory (18 documents — all superseded)

| Legacy ID | Filename | Canonical Replacement |
|-----------|----------|----------------------|
| HR-ADM-001 | 01-Employer-Setup-Checklist.md | HR-CHK-001 |
| HR-PROC-001 | 02-Employee-Lifecycle-Procedure.md | HR-EMP-001 |
| HR-POS-001 | 03-Position-Authorization-Form.md | HR-FORM-001 |
| HR-REC-001 | 04-Recruitment-Checklist.md | HR-SOP-002 |
| HR-APP-001 | 05-Employment-Application-Template.md | HR-FORM-002 |
| HR-INT-001 | 06-Interview-Evaluation-Form.md | HR-FORM-003 |
| HR-OFR-001 | 07-Offer-Letter-Template.md | HR-FORM-004 |
| HR-ONB-001 | 08-Employee-Onboarding-Checklist.md | HR-CHK-002 |
| HR-FIL-001 | 09-Personnel-File-System.md | HR-CHK-003 |
| HR-COMP-001 | 10-Compensation-Worksheet.md | HR-FORM-005 |
| HR-PROC-002 | 11-Compensation-Approval-Procedure.md | HR-SOP-003 |
| HR-PROC-003 | 12-Timekeeping-Procedure.md | HR-SOP-005 |
| HR-TIME-001 | 13-Employee-Time-Record.md | HR-TIME-001 (same ID) |
| HR-PROC-004 | 14-Payroll-Procedure.md | FIN-PROC-004 (moved to Finance) |
| HR-CHK-001 | 15-Payroll-Checklists.md | FIN-CHK-001 + FIN-CHK-003 (moved to Finance) |
| HR-PERF-001 | 16-Performance-Review-Form.md | HR-FORM-007 |
| HR-PROC-005 | 17-Disciplinary-Procedure.md | HR-SOP-007 |
| HR-SEP-001 | 18-Employee-Separation-Checklist.md | HR-CHK-004 |

### ID Conflict Resolution

Two legacy IDs conflicted with canonical IDs (same ID, different documents):

| Legacy ID | Legacy Document | Canonical ID | Canonical Document | Resolution |
|-----------|----------------|--------------|-------------------|------------|
| HR-CHK-001 | Payroll Checklists | HR-CHK-001 | Employer Setup Checklist | Canonical wins. Legacy Payroll Checklists → FIN-CHK-001 + FIN-CHK-003 |
| HR-TIME-001 | Employee Time Record | HR-TIME-001 | Employee Time Record | Same document — direct duplicate. Canonical is authoritative. |

### Superseded Notices Applied

All 18 legacy HR files now carry a blockquote banner at the top:
- `> **⛔ DO NOT USE — SUPERSEDED (August 25, 2026)**`
- Points to the canonical replacement ID and location
- Folder-level notice retained in `SUPERSEDED-NOTICE.md`

---

## 5. Reference Repairs

### Scope

All references to legacy HR IDs in `lost_limb_riders_operations/` (outside `03-HUMAN-RESOURCES/`) were repaired to point to the correct canonical equivalents.

### Files Modified (24 files)

| Department | File | References Repaired |
|-----------|------|-------------------|
| 00-START-HERE | MASTER-INDEX.md | HR-ONB-001 → HR-CHK-002 |
| 00-START-HERE | TRANSACTION-MAP.md | 13 legacy HR IDs updated |
| 00-START-HERE | TRANSACTIONAL-LAYER-COMPLETION-REPORT.md | HR-PROC-001, HR-PROC-002, HR-PROC-004, HR-SEP-001, HR-OFR-001 |
| 00-START-HERE | VALIDATION-TEST-SCENARIOS.md | HR-POS-001, HR-FORM-005, HR-SOP-003, HR-SOP-002, HR-FORM-002, HR-FORM-003, HR-FORM-004, HR-CHK-002, HR-TIME-001, HR-CHK-003, FIN-CHK-001, HR-FORM-004, HR-CHK-004 |
| 00-START-HERE | MIGRATION-MAP.md | HR-COMP-001 → HR-FORM-005, HR-PROC-002 → HR-SOP-003 |
| 01-GOVERNANCE | 02-Approval-Matrix.md | HR-COMP-001 → HR-FORM-005, HR-PROC-002 → HR-SOP-003 |
| 01-GOVERNANCE | 03-Records-Policy.md | HR-FIL-001 → HR-CHK-003 |
| 04-CONTRACTORS | 01-Classification-Checklist.md | HR-PROC-001 → HR-EMP-001 |
| 04-CONTRACTORS | 07-Year-End-1099-Review.md | HR-CHK-001 → FIN-CHK-003 |
| 05-FINANCE | 07-Payment-Authorization.md | HR-PROC-004 → FIN-PROC-004 |
| 05-FINANCE | 08-Financial-Closeout-and-Reconciliation-Procedure.md | HR-PROC-004 → FIN-PROC-004, HR-CHK-001 → FIN-CHK-003 |
| 05-FINANCE | 09-Annual-Budget-Procedure.md | HR-PROC-002 → HR-SOP-003 |
| 06-EVENTS | 01-Event-Procedures-Overview.md | HR-TIME-001 (unchanged), HR-PROC-004 → FIN-PROC-004 |
| 06-EVENTS | 04-Event-Financial-Feasibility-Worksheet.md | HR-PROC-004 → FIN-PROC-004 |
| 06-EVENTS | 06-Event-Staffing-Plan.md | HR-TIME-001 (unchanged), HR-PROC-004 → FIN-PROC-004 |
| 06-EVENTS | 07-Event-Day-Checklist.md | HR-TIME-001 (unchanged) |
| 06-EVENTS | 09-Event-Closeout-Checklist.md | HR-TIME-001 (unchanged), HR-PROC-004 → FIN-PROC-004 |
| 06-EVENTS | 10-Event-Postmortem-and-Lessons-Learned.md | HR-TIME-001 (unchanged), HR-COMP-001 → HR-FORM-005 |
| 07-PROGRAMS | 00-Programs-Department-Index.md | HR-TIME-001 (unchanged), HR-PROC-004 → FIN-PROC-004 |
| 08-VOLUNTEERS | 01-Volunteer-System-Procedure.md | HR-PROC-001 → HR-EMP-001 |
| 12-COMPLIANCE | 01-IRS-Compliance-Matrix.md | HR-PROC-002 → HR-SOP-003, HR-COMP-001 → HR-FORM-005, HR-PROC-004 → FIN-PROC-004 |
| 12-COMPLIANCE | 03-Compliance-Calendar.md | HR-CHK-001 → FIN-CHK-003 |
| 12-COMPLIANCE | 04-Annual-Compliance-Checklist.md | HR-CHK-001 → FIN-CHK-003, HR-COMP-001 → HR-FORM-005 |
| 13-FORMS-AND-TEMPLATES | 00-Forms-and-Templates-Index.md | Full HR section rewritten with canonical IDs |

### Full Legacy → Canonical ID Mapping

| Legacy ID | Canonical ID | Document |
|-----------|-------------|----------|
| HR-ADM-001 | HR-CHK-001 | Employer Setup Checklist |
| HR-PROC-001 | HR-EMP-001 | Employee Lifecycle Map |
| HR-PROC-002 | HR-SOP-003 | Selection & Compensation Approval SOP |
| HR-PROC-003 | HR-SOP-005 | Timekeeping SOP |
| HR-PROC-004 | FIN-PROC-004 | Payroll Procedure (Finance) |
| HR-PROC-005 | HR-SOP-007 | Performance Review & Discipline SOP |
| HR-POS-001 | HR-FORM-001 | Position Authorization Form |
| HR-REC-001 | HR-SOP-002 | Recruitment SOP |
| HR-APP-001 | HR-FORM-002 | Employee Application Form |
| HR-INT-001 | HR-FORM-003 | Interview Evaluation Form |
| HR-OFR-001 | HR-FORM-004 | Offer Letter Template |
| HR-ONB-001 | HR-CHK-002 | Employee Onboarding Checklist |
| HR-FIL-001 | HR-CHK-003 | Personnel File Checklist |
| HR-COMP-001 | HR-FORM-005 | Position Compensation Worksheet |
| HR-CHK-001 (Payroll) | FIN-CHK-001 | Payroll Checklist (Finance) |
| HR-CHK-001 (Year-end) | FIN-CHK-003 | Year-End Close Checklist (Finance) |
| HR-TIME-001 | HR-TIME-001 | Employee Time Record (same ID) |
| HR-PERF-001 | HR-FORM-007 | Performance Review Form |
| HR-SEP-001 | HR-CHK-004 | Employee Separation Checklist |

---

## 6. Remaining Work

| Item | Status | Action Required |
|------|--------|----------------|
| Operations tree `00-START-HERE/SUPERSEDED-NOTICE.md` | Not created | The entire `lost_limb_riders_operations/` tree is being superseded by `lost_limb_riders_handbooks/transactional_operations/`. A root-level superseded notice may be added when that broader consolidation is executed. |
| Employee manuals (`employees/`) | 42 generated position manuals | These are generated from `generate_positions.py` and reference canonical HR IDs. No changes needed. |
| Canonical HR tree — pushed to `master` | Not yet pushed | The canonical HR tree exists in the local checkout of Autobiography but has not been pushed to the remote `master` branch. The website submodule indexes only the deployed `master`. |
| Operations tree non-HR departments | Not in scope | This directive covers HR consolidation only. The broader operations-to-handbooks migration is a separate effort. |

---

## 7. Verification

- [x] All 28 canonical HR documents verified present
- [x] All 18 legacy HR documents marked with DO NOT USE banners
- [x] Folder-level SUPERSEDED-NOTICE.md retained
- [x] Zero remaining legacy HR ID references in operations tree (outside 03-HR)
- [x] Forms Index rewritten with canonical HR IDs
- [x] ID conflict (HR-CHK-001) resolved — canonical wins, legacy mapped to Finance
- [x] ID duplicate (HR-TIME-001) confirmed — same document, canonical is authoritative

---

**Lost Limb Riders Organization**
*"I Can. I Will. Nobody Is Left Behind. Nobody Stands Alone."*
