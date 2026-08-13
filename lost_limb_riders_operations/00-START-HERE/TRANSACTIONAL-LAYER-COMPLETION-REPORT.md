# **Lost Limb Riders — Transactional Layer Completion Report**

**Document ID:** ADM-REF-007  
**Document Title:** Lost Limb Riders — Transactional Layer Completion Report  
**Department:** Administration  
**Document Type:** REF (Reference / Status report)  
**Version:** 1.0  
**Effective Date:** August 12, 2026  
**Review Date:** August 2027  
**Document Owner:** Records & Compliance Officer  
**Approving Authority:** Board of Directors  
**Supersedes:** None  
**Related Documents:** ADM-REF-001 (Master Index), ADM-REF-003 (Migration Map), ADM-REF-002 (Transaction Map), ADM-REF-006 (Validation Test Scenarios), FIN-CTRL-001, tools/validate_ops.py  
**Related Forms:** None  
**Record Classification:** Permanent — Governance  
**Retention Requirement:** Permanent (Board)

---

## **1. Purpose**

This report records the build status of the transactional operations layer in `lost_limb_riders_operations/`. It is the authoritative answer to: what exists, whether it is internally consistent, what was tested, what still requires a professional review, and what remains open. The report is the living status record referenced by the Master Index (ADM-REF-001), the Migration Map (ADM-REF-003), the Validation Test Scenarios (ADM-REF-006), and the Change Control Procedure (CMP-CHG-001).

## **2. Scope and Definitions**

- **Transactional operations layer:** the repository at `lost_limb_riders_operations/` — the set of controlled documents describing how every material transaction is authorized, executed, documented, approved, accounted for, recorded, reconciled, and closed.
- **Controlled document:** a file carrying a `Document ID` header and the full metadata block defined in the Master Document Control Policy (ADM-DOC-001).
- **Validation:** the automated consistency check implemented in `tools/validate_ops.py`.
- **Transaction ID:** the registry key (e.g., `EVT-2026-001`, `PAY-2026-001`) assigned at transaction open and tracked in the Master Transaction Register (ADM-REG-001).
- This layer does **not** contain completed records, personnel files, payroll, donor databases, or any restricted content. Completed records live in the restricted locations defined in the Records Location Register (REC-LOC-001).

## **3. Document Inventory**

As of the build date the layer contains **78 controlled documents** across 15 folders:

| Folder | Department | Documents |
|--------|-----------|-----------|
| 00 | START-HERE | 4 |
| 01 | GOVERNANCE | 5 |
| 02 | ADMINISTRATION | 1 |
| 03 | HUMAN-RESOURCES | 18 |
| 04 | CONTRACTORS | 7 |
| 05 | FINANCE | 11 |
| 06 | EVENTS | 10 |
| 07 | PROGRAMS | 1 |
| 08 | VOLUNTEERS | 3 |
| 09 | SAFETY-RISK | 3 |
| 10 | FUNDRAISING | 5 |
| 11 | GRANTS | 2 |
| 12 | COMPLIANCE | 4 |
| 13 | FORMS-AND-TEMPLATES | 1 |
| 14 | RECORDS-MANAGEMENT | 3 |

The full list with document IDs lives in the Master Index (ADM-REF-001), the Document Register section of the Master Document Control Policy, and the department indexes under `13-FORMS-AND-TEMPLATES/`.

## **4. Validation Results**

The validation tool (`tools/validate_ops.py`) checks every controlled document for: required header fields, document ID format, broken `.md` references, referenced-but-missing document IDs, orphaned documents, and formatting rules. Current run:

- **Documents scanned:** 99
- **Controlled document IDs found:** 78
- **Issues found after this report:** **0** (the four previously reported broken references pointed at this file and are resolved by its creation).

Known advisory (non-error) conditions are documented in section 8.

## **5. Test Scenario Results**

Twelve simulated end-to-end scenarios are defined in ADM-REF-006. Each is run on fictional data and exercises the document trail end to end. Results are recorded in the table below as each scenario is executed. Scenarios not yet executed are marked **Pending** and are scheduled per section 15.

| # | Scenario | Pass/Fail | Date run | Notes |
|---|----------|-----------|----------|-------|
| 1 | New employee (EMP → TIM → PAY) | Pending | | |
| 2 | Contractor engagement and 1099 review | Pending | | |
| 3 | Paid event through closeout | Pending | | |
| 4 | Volunteer event | Pending | | |
| 5 | Expense reimbursement ($250) | Pending | | |
| 6 | Unrestricted $1,000 donation | Pending | | |
| 7 | Restricted $1,000 donation | Pending | | |
| 8 | $2,500 sponsorship | Pending | | |
| 9 | $10,000 restricted grant | Pending | | |
| 10 | Event incident | Pending | | |
| 11 | Employee separation | Pending | | |
| 12 | Audit trace ($1,842.17) | Pending | | |

## **6. Cross-Reference Integrity**

- Every controlled document carries the full metadata block required by ADM-DOC-001, including `Related Documents` and `Related Forms`.
- Document IDs referenced across the layer resolve to real documents; the validator confirms no broken `.md` references and no dangling document IDs.
- The Transaction Map (ADM-REF-002) defines the Requester → Approver → Payer → Reconciler chain for every transaction family; the Master Transaction Register (ADM-REG-001) is the operational tracking point.
- Archived material is referenced only through the Migration Map (ADM-REF-003) and is not cited as operating authority.

## **7. External Professional Review Items**

The following items require review by an attorney, CPA, payroll professional, or insurance professional before they are relied on in operations. These are the items referenced by CMP-CHG-001 section 6:

| Item | Professional required | Where |
|------|----------------------|-------|
| Employee vs. contractor classification, wage and hour, Iowa employment law (before first hire) | Attorney + payroll professional | HR-PROC-001 |
| Compensation: IRC §4958 excess-benefit compliance and Form 990 disclosure for key employees/disqualified persons | Attorney / CPA | HR-PROC-002 |
| Iowa payroll forms, deadlines, and rates (at setup and annually) | Payroll provider, IWD, Iowa DOR | HR-PROC-004 |
| COBRA eligibility and notices | Benefits provider / attorney | HR-SEP-001 |
| Contractor classification and W-9/TIN issues | Attorney | CTR-001, CTR-PROC-001 |
| Contractor agreement terms and indemnification | Attorney | CTR-002 |
| Contracts for real property, loans, leases; debt/loan resolutions | Attorney | FIN-CTRL-001 |
| Record-retention schedule (annually) | Attorney + CPA | CMP-RET-001 |
| IRS compliance matrix and Form 990 (before each filing) | CPA | CMP-IRS-001 |
| Iowa compliance matrix: rates, deadlines, thresholds at filing time | Counsel / CPA / state agency | CMP-IA-001 |
| Donation vs. sponsorship vs. sale classification when in doubt | Attorney / CPA | FUND-REF-001 |
| Restricted-fund acceptance (permanently restricted / endowment) | Attorney | FUND-REST-001 |
| UBIT review of revenue streams (year-end) | CPA | CMP-IRS-001, FUND-REF-001 |
| Iowa sales/use tax obligations (merchandise, admissions) | Iowa DOR / CPA | CMP-IA-001, FIN-PUR-001 |
| Insurance claims: settlement and admissions of fault | Carrier / attorney | SAF-INS-001 |
| Employment agreement provisions | Attorney | HR-OFR-001 |

## **8. Known Gaps and Deferred Items**

1. **Validation test execution (scenarios 1–12):** defined but not yet executed. Scheduled per section 15. Test records, even fictional, are restricted and are stored outside this repository.
2. **Pending professional reviews:** the retention schedule (CMP-RET-001), IRS matrix (CMP-IRS-001), and compensation procedure (HR-PROC-002) carry build notes that their numbers/rates are subject to counsel or CPA review. Nothing in this layer is legal, tax, or insurance advice; the items in section 7 must be confirmed before reliance.
3. **Board decisions required before first use:** pay frequency and pay dates (HR-PROC-004 section 2) are placeholders awaiting board resolution; any internal-control thresholds referenced as board-defined follow the same rule.
4. **Validation tooling:** `tools/validate_ops.py` is advisory automation. It does not replace document-owner review, professional review (section 7), or the change-control process (CMP-CHG-001).
5. **Archive hygiene:** superseded and archived material under `ARCHIVE/` is preserved intentionally and is not deleted (ADM-REF-003).

## **9. Recommendations**

1. Execute the twelve validation scenarios on simulated data and record results in section 5 before the first live use of the layer.
2. Obtain the professional reviews in section 7 before the first hire, first payroll, first grant award, or first restricted-fund acceptance.
3. Complete the board resolutions required in HR-PROC-004 (pay frequency and pay dates) before the first payroll run.
4. Re-run the validator after any change that touches document IDs, header fields, or file paths.
5. Review this report annually and update it through the change-control procedure.

## **10. Change-Control Integration**

- All changes to controlled documents, including this report, follow CMP-CHG-001.
- Version changes update the document version, revision history, and the Document Register.
- Emergency changes are approved per CMP-CHG-001 section 5 and ratified at the next board meeting.
- The external professional review items in section 7 are maintained here and are the source referenced by CMP-CHG-001 section 6.

## **11. Retention and Compliance Note**

- Record retention minimums are defined in CMP-RET-001; where law and schedule differ, the longest applicable requirement governs unless counsel directs otherwise.
- Compliance obligations and due dates are tracked in the IRS matrix (CMP-IRS-001), the Iowa matrix (CMP-IA-001), and the Compliance Calendar (CMP-CAL-001).
- This repository is public and must never contain SSNs, bank details, completed W-4/I-9 forms, medical records, donor or personnel records, or credentials (ADM-REF-001, REC-LOC-001).

## **12. Sign-Off**

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Records & Compliance Officer | | | |
| Executive Director | | | |
| Board of Directors (ratify) | | | |

Sign-off confirms the status in this report is accurate as of the date signed.

## **13. Revision History**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | August 12, 2026 | Administration | Initial completion report — build status, validation, scenarios, professional review list |

## **14. Repository Status**

The transactional layer is **built and structurally validated**. The layer is ready for the pending professional reviews (section 7), the board decisions (section 8 item 3), and scenario testing (section 5) before full operational use. Active, archived, and superseded material boundaries are documented in the Migration Map (ADM-REF-003) and preserved as required.

## **15. Follow-Up Schedule**

| Activity | Owner | Frequency / Due |
|----------|-------|-----------------|
| Run validation scenarios 1–12 on simulated data; record results | Records & Compliance Officer | Before first live use |
| Professional reviews (section 7) | Board / ED with counsel, CPA, payroll, insurance providers | Before first hire, payroll, grant, or restricted acceptance |
| Board resolutions: pay frequency and pay dates (HR-PROC-004) | Board | Before first payroll |
| Re-run validator | Records & Compliance Officer | After any material change |
| Review this completion report | Board / ED | Annual, via CMP-CHG-001 |

---

**Lost Limb Riders Organization**  
*"I Can. I Will."*
