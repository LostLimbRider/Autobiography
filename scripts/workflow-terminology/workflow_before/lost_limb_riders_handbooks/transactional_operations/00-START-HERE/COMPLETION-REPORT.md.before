## Lost Limb Riders — Transactional Operations Layer: Completion Report

**Document ID:** VAL-REPORT-002
**Document Title:** Transactional Layer Completion Report
**Department:** Compliance
**Document Type:** REF
**Version:** 1.0
**Effective Date:** August 12, 2026
**Review Date:** August 2027
**Document Owner:** Compliance Officer
**Approving Authority:** Board of Directors
**Supersedes:** None
**Related Documents:** MASTER-INDEX; MIGRATION-MAP; TRANSACTION-MAP; VAL-REPORT-001 (Validation); validate_transactional_layer.py
**Related Forms:** None
**Record Classification:** Compliance
**Retention Requirement:** Permanent (while in force)

---

## 1. Status

**COMPLETE.** The transactional operations layer implements the approved design: every material transaction is traceable from authorization to closeout. The validator passes clean (see §3).

## 2. What Was Built

| Department Folder | Files | Content |
|---|---|---|
| 01-GOVERNANCE | 9 | Board governance, records/retention, conflict of interest, insider compensation, whistleblower, board action register |
| 02-ADMINISTRATION | 6 | Document lifecycle, change control, audit retrieval, transaction ID assignment, master registers |
| 03-HUMAN-RESOURCES | 26 | Employment policy, lifecycle map, hiring/onboarding/payroll/performance/separation SOPs, checklists, forms, time records, employee register |
| 04-CONTRACTORS | 10 | Contractor classification, W-9, agreements, scope, invoices, payment auth, 1099 review, register |
| 05-FINANCE | 30 | Approval matrix, financial controls, cash handling, purchasing, payment auth, expense/reimbursement, payroll, donations, restricted funds, bank reconciliation, month-end/year-end close, budget, checklists, forms, 6 registers |
| 06-EVENTS | 8 | Event authorization, feasibility, staffing, closeout, budget/summary forms, event register |
| 07-PROGRAMS | 3 | Programs index and transactional controls, program financial tracking, program register |
| 08-VOLUNTEERS | 5 | Volunteer policy, application, screening, onboarding checklist, register |
| 09-SAFETY-RISK | 5 | Risk management, incident reporting, safety checklist, incident report, incident register |
| 10-FUNDRAISING | 5 | Fundraising policy, donation processing, sponsorship procedure, sponsorship agreement, register |
| 11-GRANTS | 4 | Grant lifecycle, tracking form, budget form, grant register |
| 12-COMPLIANCE | 8 | Compliance policy, federal reference, Iowa reference, compliance calendar, annual/quarterly checklists, monitoring procedure, source-verification register |
| 13-FORMS-AND-TEMPLATES | 1 | Forms and templates index (links all forms; existing program forms referenced, retained unchanged) |
| 14-RECORDS-MANAGEMENT | 5 | Master retention matrix, records location, storage/protection, destruction, annual review |
| 00-START-HERE | 5 + 12 tests | Master index, migration map, transaction map, validation report, completion report, lessons-learned, 12 test scenarios |
| **Total** | **142** | 130 controlled documents + 12 test scenarios |

## 3. Validation

- `python3 validate_transactional_layer.py` — **PASS, 130 controlled files OK** (tests are walkthroughs, not controlled documents).
- Checks: filename pattern, metadata block, cross-reference integrity, curly-quote typography, directory completeness.
- Fix pass applied: 63+ straight quotes converted to curly; 11 stale legacy references (`SFT-*`, `FIN-PROC-003`, `FIN-FORM-001`) corrected to real files.

## 4. External Verification (Compliance Facts)

All tax and compliance figures in CMP-IRS-001 and CMP-IA-001 were verified against live sources on August 12, 2026 and logged in CMP-REF-001. Highlights confirmed: 990-series thresholds and revocation rule; W-2/1099-NEC Jan 31 (Feb 1, 2027); FICA 2026 wage base $184,500; FUTA 0.6% effective; Form 941 quarterly dates; monthly vs. semiweekly deposit schedules; I-9 retention; Iowa new-hire within 15 days; Iowa UI and withholding quarterly dates; Iowa biennial report in odd-numbered years; Iowa workers’ comp insurance; Iowa sales-tax rules for nonprofits and gambling; Iowa no general solicitation registration (professional fundraisers register under Ch. 13C); Iowa minimum wage $7.25; required workplace postings.

## 5. Items Flagged for CPA / Attorney Review

1. **1099-NEC reporting threshold:** current IRS guidance may change the aggregate threshold ($600 → $2,000 for certain payments after 2025). Confirm before the 2027 filing season (CMP-REF-001 §4).
2. **990-EZ thresholds** are indexed; confirm each year.
3. **Iowa withholding deposit frequency** thresholds and the organization’s **UI contribution rate** are specific to the organization; confirm with the CPA and Iowa Workforce Development.
4. **Gambling activity** (raffles/bingo) requires Iowa Code Ch. 99B licensing plus a sales tax permit; review with counsel before launching.
5. **Internal control thresholds** in FIN-CTRL-001 ($250/$1,000/$5,000) mirror the Organization Handbook but are marked subject to formal Board adoption — the Board should ratify them as the single standard.
6. **Workers’ comp insurance** and the **biennial report** are real action items to execute; the 2027 biennial report window opens January 1, 2027.

## 6. Handoff Notes

- All registers are blank-layout templates ready for use; completed records are filed outside the repository (REC-REF-001).
- Existing handbooks and program forms were referenced, never modified. ARCHIVE was not touched.
- Re-run the validator after any change; new documents must follow `DEPT-TYPE-NNN-Name.md` and the metadata block (GOV-POL-001 §4).
- Annual review: update the compliance calendar and verification register each August (CMP-CHK-001).

---

**End of Report.**
