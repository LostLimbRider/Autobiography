# **Lost Limb Riders — Transactional Operations Master Index**

**Document ID:** ADM-REF-001  
**Document Title:** Lost Limb Riders — Transactional Operations Master Index  
**Department:** Administration  
**Document Type:** REF (Reference)  
**Version:** 1.1  
**Effective Date:** August 12, 2026  
**Review Date:** August 2027  
**Document Owner:** Records & Compliance Officer  
**Approving Authority:** Board of Directors  
**Supersedes:** None  
**Related Documents:** TRANSACTION-MAP.md, MIGRATION-MAP.md, ADM-DOC-001, FIN-CTRL-001, CMP-RET-001, REC-LOC-001  
**Related Forms:** None  
**Record Classification:** Permanent — Governance  
**Retention Requirement:** Permanent (Board)

---

## **What This Repository Is**

This directory — `lost_limb_riders_operations/` — is the **transactional operations layer** for Lost Limb Riders. It sits alongside the consolidated handbooks in `lost_limb_riders_handbooks/` and the position manuals in `employees/`.

The handbooks describe **how the organization is supposed to operate**. This layer describes **how every material transaction actually gets done**: who authorizes it, who executes it, what documentation is produced, how it is approved, how it is accounted for, where the record is stored, how long it is kept, and what constitutes closeout.

The guiding chain for every transaction:

```text
POLICY → PROCEDURE → CHECKLIST → FORM → TRANSACTION → APPROVAL → ACCOUNTING → RECORD → RECONCILIATION → CLOSEOUT → RETENTION
```

No major operational activity ends with "someone handled it." It ends with a documented transaction record and a defined closeout state.

## **Who Should Use This Repository**

| User | Start With |
|------|-----------|
| New board member | `01-GOVERNANCE/02-Approval-Matrix.md`, `01-GOVERNANCE/01-Master-Document-Control-Policy.md` |
| New officer | `00-START-HERE/TRANSACTION-MAP.md`, `01-GOVERNANCE/02-Approval-Matrix.md` |
| Executive Director | `01-GOVERNANCE/02-Approval-Matrix.md`, `14-RECORDS-MANAGEMENT/03-Master-Transaction-Register.md` |
| Finance Director / Bookkeeper | `05-FINANCE/`, `12-COMPLIANCE/` |
| Events Director / Coordinator | `06-EVENTS/` |
| Hiring manager / supervisor | `03-HUMAN-RESOURCES/` |
| Fundraising / grants staff | `10-FUNDRAISING/`, `11-GRANTS/` |
| Volunteer Coordinator | `08-VOLUNTEERS/` |
| Safety / risk staff | `09-SAFETY-RISK/` |
| Auditor / accountant / CPA | `00-START-HERE/TRANSACTION-MAP.md`, `12-COMPLIANCE/`, `14-RECORDS-MANAGEMENT/` |
| Records & Compliance Officer | Everything below |

## **Active vs. Archived Material**

- **Active:** Everything inside `lost_limb_riders_operations/` and the numbered folders of `lost_limb_riders_handbooks/` and `employees/`. These are the documents the organization lives by.
- **Archived:** Everything under `ARCHIVE/`. Archived material is historical. It may contain useful controls, but it is not the operating standard.
- **Superseded:** Any controlled document replaced by a newer version. Superseded versions stay in the document register (see `01-GOVERNANCE/01-Master-Document-Control-Policy.md`) but are never used for operations.
- A document marked **active** must live in an active folder. A document marked **superseded** must not be cited as authority.

See `00-START-HERE/MIGRATION-MAP.md` for the full inventory and disposition of existing material. See `00-START-HERE/TRANSACTIONAL-LAYER-COMPLETION-REPORT.md` for the build status of this layer and `00-START-HERE/VALIDATION-TEST-SCENARIOS.md` for the tested transaction scenarios.

## **Department Structure**

| Number | Department | Contents |
|--------|-----------|----------|
| 00 | START-HERE | Indexes, maps, completion report |
| 01 | GOVERNANCE | Document control, approval matrix, records policy, retention matrix, change control |
| 02 | ADMINISTRATION | Transaction register, records location register, document lifecycle |
| 03 | HUMAN-RESOURCES | Employer setup, employee lifecycle, onboarding, personnel files, compensation, timekeeping, payroll, performance, separation |
| 04 | CONTRACTORS | Classification, W-9, agreements, invoices, 1099 review |
| 05 | FINANCE | Expense reports, reimbursement, purchasing, payment authorization, asset register, closeout, reconciliation |
| 06 | EVENTS | Event authorization, feasibility, budget, staffing, event-day, revenue, closeout, postmortem |
| 07 | PROGRAMS | Pointer to program manuals in `lost_limb_riders_handbooks/03-Program-Manuals/` |
| 08 | VOLUNTEERS | Volunteer system, agreement, expense reimbursement |
| 09 | SAFETY-RISK | Incident workflow, incident log, insurance procedure |
| 10 | FUNDRAISING | Donations, acknowledgments, restricted funds, sponsorships |
| 11 | GRANTS | Grant lifecycle and grant file |
| 12 | COMPLIANCE | IRS matrix, Iowa matrix, compliance calendar, annual checklist |
| 13 | FORMS-AND-TEMPLATES | Pointers to all operational forms (blank templates live in their department folders) |
| 14 | RECORDS-MANAGEMENT | Retention, confidentiality, records location, lifecycle |

## **Document Numbering**

Every controlled document carries a unique Document ID. Format:

```text
<DEPARTMENT PREFIX>-<TYPE PREFIX>-<SEQUENCE>
```

Examples: `HR-ONB-001`, `EVT-AUTH-001`, `FIN-EXP-001`, `CMP-IRS-001`, `CTR-001`.

Document type prefixes: POL (Policy), SOP (Standard Operating Procedure), PROC (Procedure), FORM (Form), CHK (Checklist), REG (Register), TMP (Template), REF (Reference).

See `01-GOVERNANCE/01-Master-Document-Control-Policy.md` for the full scheme, metadata block, version rules, and how to create or retire a document.

## **Transaction Numbering**

Every material transaction receives a unique Transaction ID when it is opened:

```text
EMP-2026-001   Employee
CTR-2026-001   Contractor
EVT-2026-001   Event
EXP-2026-001   Expense / reimbursement
DON-2026-001   Donation
SPN-2026-001   Sponsorship
GRT-2026-001   Grant
AST-2026-001   Asset
INC-2026-001   Incident
BRD-2026-001   Board matter
TIM-2026-001   Time record
PAY-2026-001   Payroll run / payment
```

The Transaction ID is recorded in the **Master Transaction Register** (`14-RECORDS-MANAGEMENT/03-Master-Transaction-Register.md`) and appears on every related document so the whole trail can be traced. See `00-START-HERE/TRANSACTION-MAP.md`.

## **Records Location**

Blank templates, procedures, and policies live **in this repository**. Completed records — signed forms, pay documents, bank records, personnel files — do **not** live in a public GitHub repository.

See `14-RECORDS-MANAGEMENT/01-Records-Location-Register.md` for exactly where each class of record belongs (secure file cabinets, encrypted drives, payroll provider, insurance carrier, state/federal systems).

## **Confidentiality Rules**

This repository is public. It may contain:

- policies, procedures, blank forms, templates, checklists, job descriptions, document schemas, compliance instructions, generic examples

It must never contain:

- Social Security numbers, bank account information, completed W-4s or I-9s, medical information, private employee/donor/participant records, passwords, credentials, or confidential contracts

If you are about to commit a file and it contains any of the restricted items above, **stop**. The record belongs in a restricted location, not here. See `14-RECORDS-MANAGEMENT/01-Records-Location-Register.md`.

## **Compliance System**

Two compliance matrices govern the organization's filings:

- `12-COMPLIANCE/01-IRS-Compliance-Matrix.md` — federal 501(c)(3) obligations
- `12-COMPLIANCE/02-Iowa-Compliance-Matrix.md` — Iowa obligations

Every filing with a due date is tracked in the **Compliance Calendar** (`12-COMPLIANCE/03-Compliance-Calendar.md`). Every requirement is mapped to an authoritative source and a responsible person. The matrices are reviewed on the schedule in `01-GOVERNANCE/05-Change-Control-Procedure.md`.

## **How to Locate a Procedure**

1. Ask what transaction is happening (hiring, paying, event, donation, grant, purchase, reimbursement, incident).
2. Look it up in `00-START-HERE/TRANSACTION-MAP.md`.
3. Open the department folder and the named document.
4. Follow the procedure end to end. Complete every checklist and form it references.
5. Record the Transaction ID in the Master Transaction Register when the transaction opens and when it closes.

## **How to Create a New Document**

1. Confirm a real need — the document must map to an actual workflow (see `01-GOVERNANCE/01-Master-Document-Control-Policy.md`, section "Justification").
2. Draft using the controlled-document header block.
3. Obtain review from the document owner and the affected department lead.
4. Obtain approval from the authority specified in the Approval Matrix.
5. Register the document in the Document Register.
6. Publish, and update cross-references.

## **How to Retire a Document**

1. Identify why the document is obsolete (replaced, no longer needed, merged).
2. Mark it superseded in the Document Register; keep the superseded version for audit history.
3. Update every cross-reference.
4. If a replacement exists, confirm the replacement is active before retiring the old version.
5. Board approval is required to retire governance or financial-control documents.

## **Document Maintenance**

- **Review cycle:** Annual, or when law, structure, or process changes.
- **Owner:** Records & Compliance Officer maintains indexes and registers. Department owners maintain their own documents.
- **Version rule:** Every change increments the version and updates the revision history. Unversioned documents are drafts, not authority.
- **Source authority:** Compliance documents cite authoritative sources (IRS, Iowa Legislature, Iowa Department of Revenue, Iowa Workforce Development, Iowa Secretary of State). Where a requirement changes, follow `01-GOVERNANCE/05-Change-Control-Procedure.md`.

---

## **Revision History**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | August 12, 2026 | Administration | Initial version — transactional layer launch |
| 1.1 | August 12, 2026 | Administration | Added completion report and validation scenarios to the index |

---

**Lost Limb Riders Organization**  
*"I Can. I Will."*
