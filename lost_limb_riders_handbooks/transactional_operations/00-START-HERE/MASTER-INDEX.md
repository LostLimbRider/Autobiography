## Lost Limb Riders — Transactional Operations Layer

**Master Index**

**Document ID:** ADM-REF-001
**Document Title:** Master Index — Transactional Operations Layer
**Department:** Administration
**Document Type:** REF
**Version:** 1.0
**Effective Date:** August 12, 2026
**Review Date:** August 2027
**Document Owner:** Executive Director
**Approving Authority:** Board of Directors
**Supersedes:** None
**Related Documents:** GOV-POL-001 Document Control; ADM-PROC-001 Document Lifecycle; ADM-PROC-002 Change Control; 00-START-HERE.md (handbooks master index)
**Related Forms:** None
**Record Classification:** Administrative
**Retention Requirement:** Permanent (while in force)

---

## 1. What This Repository Is

This is the **transactional operations layer** for Lost Limb Riders. It sits beside the existing handbooks and contains the operational workflows, forms, registers, and controls that connect the organization’s governance, programs, and safety systems to day-to-day transactions.

The layer answers, for every material transaction:

1. What is happening?
2. Why is it happening?
3. Who authorized it?
4. Who executes it?
5. Who receives money or property?
6. Where did the money come from?
7. Where is the money going?
8. What documentation is required?
9. What approvals are required?
10. What accounting entry results?
11. What legal and compliance requirements apply?
12. Where is the supporting record stored?
13. How long must it be retained?
14. Who verifies completion?
15. What constitutes final closeout?

No material activity ends with “someone handled it.” It ends with a **documented transaction record and a defined closeout state.**

## 2. Who Should Use This

- **Board members** — approval matrix, governance policies, compliance calendar, retention matrix.
- **Executive leadership** — approval authorities, transaction registers, event authorization.
- **Finance staff** — expense, reimbursement, purchasing, payroll, donation, reconciliation procedures.
- **HR and administrators** — employee lifecycle, contractor lifecycle, records management.
- **Event coordinators** — event authorization, feasibility, staffing, day-of, closeout.
- **Program staff** — program coding reference, volunteer and participant support.
- **Volunteer coordinators** — volunteer lifecycle.
- **Auditors, accountants, attorneys, and insurers** — trace any transaction from authorization to closeout.

## 3. Active vs. Archived Material

- **Active material** lives in `lost_limb_riders_handbooks/` and `transactional_operations/`.
- **Archived material** lives in `ARCHIVE/` and is **off-limits**: it is not referenced, migrated, or modified. Historical records are preserved there but have no operational authority.
- This transactional layer is **authoritative** for the transactional workflows it documents. The existing Organization Handbook and program manuals remain authoritative for governance, program, and safety *content*; this layer adds the operational *controls* around those activities.
- Where a document in this layer conflicts with an existing handbook, the governing policy in this layer controls for the transaction in question, and the conflict must be reported through the change-control process (ADM-PROC-002).

## 4. Directory Structure

```text
transactional_operations/
├── 00-START-HERE/         Master index, transaction map, migration map, tests, reports
├── 01-GOVERNANCE/         Policies: document control, conflict of interest, compensation
├── 02-ADMINISTRATION/     Document lifecycle, change control, transaction IDs, registers
├── 03-HUMAN-RESOURCES/    Employee lifecycle, onboarding, timekeeping, payroll
├── 04-CONTRACTORS/        Contractor lifecycle, classification, agreements, 1099 review
├── 05-FINANCE/            Expense, purchasing, payroll, donations, reconciliation, closeout
├── 06-EVENTS/             Event authorization, feasibility, staffing, day-of, closeout
├── 07-PROGRAMS/           Program manual references and program/event coding
├── 08-VOLUNTEERS/         Volunteer lifecycle (distinct from employment)
├── 09-SAFETY-RISK/        Incident response, registers, escalation
├── 10-FUNDRAISING/        Donations vs sponsorships vs sales; sponsorship agreements
├── 11-GRANTS/             Grant lifecycle, budgets, reporting, closeout
├── 12-COMPLIANCE/         IRS and Iowa matrices, compliance calendar, annual checklist
├── 13-FORMS-AND-TEMPLATES/ Index of all transactional forms and letter templates
└── 14-RECORDS-MANAGEMENT/ Retention matrix, storage and protection, destruction
```

## 5. Document Numbering

Every controlled document carries a header with its **Document ID**. Format:

```text
DEPT-TYPE-NNN
```

| Code | Department | Code | Department |
|------|------------|------|------------|
| GOV | Governance | EVT | Events |
| ADM | Administration | PRG | Programs |
| HR | Human Resources | VOL | Volunteers |
| CTR | Contractors | SFT | Safety/Risk |
| FIN | Finance | FUND | Fundraising |
| GRT | Grants | CMP | Compliance |
| REC | Records Management | INC | Incidents (register) |

**Document types:**

| Code | Type | Meaning |
|------|------|---------|
| POL | Policy | What the organization requires |
| SOP | Standard Operating Procedure | How a recurring task is performed |
| PROC | Procedure | Detailed how-to for a workflow |
| CHK | Checklist | What the operator must verify |
| FORM | Form | What data is captured |
| REG | Register | What recurring transactions are tracked |
| TMP | Template | Reusable letter or document shell |
| REF | Reference | Index, map, or guidance |

## 6. Transaction Numbering

Every transaction class uses a **year + sequence** ID. Register documents assign IDs; never assign your own.

| Prefix | Class | Prefix | Class |
|--------|-------|--------|-------|
| EMP | Employee | SPN | Sponsorship |
| CTR | Contractor | GRT | Grant |
| EVT | Event | AST | Asset |
| EXP | Expense | INC | Incident |
| DON | Donation | BRD | Board action |
| TIM | Time record | PAY | Payroll run |

Example: `EVT-2026-001`, `DON-2026-014`, `INC-2026-003`.

Related records cross-reference each other to form an audit trail:

```text
EVT-2026-001
    ↓
EMP-2026-004
    ↓
TIM-2026-017
    ↓
PAY-2026-009
    ↓
EXP-2026-023
```

See ADM-SOP-001 (Transaction ID Assignment) and ADM-REG-001 (Master Transaction Register).

## 7. Records Location

Templates and blank forms live in this repository. **Completed records do not.** Completed personnel, payroll, medical, donor, and financial records belong in the organization’s secure, encrypted, access-controlled records system. See REC-REF-001 (Records Location Register).

## 8. Confidentiality Rules

- **Public repository content (allowed):** policies, procedures, blank forms, templates, checklists, job descriptions, schemas, compliance instructions, generic examples.
- **Restricted records (never in this repository):** Social Security numbers, bank account numbers, W-4s, completed I-9s, medical information, private employee records, confidential donor information, sensitive participant information, passwords, credentials, private contracts when confidentiality applies.

If a form in this repository asks for sensitive information, that is because the form is a **blank template** meant to be completed and filed outside the repository. Never commit completed forms.

## 9. Compliance System

- **CMP-IRS-001** — Federal 501(c)(3) compliance matrix.
- **CMP-IA-001** — Iowa compliance matrix.
- **CMP-CAL-001** — Compliance calendar (all filings and deadlines).
- **CMP-CHK-001** — Annual compliance checklist.
- **CMP-REF-001** — Source and verification log (authorities and dates reviewed).

All compliance documents distinguish federal, Iowa, local, contractual, insurance, internal-control, and recommended-best-practice requirements.

## 10. How to Locate a Procedure

1. Start at the Transaction Map (`00-START-HERE/TRANSACTION-MAP.md`) and find your activity.
2. Open the department folder and the governing **POL** (policy) first.
3. Follow the **PROC/SOP** for the workflow.
4. Use the **CHK** checklist to execute it.
5. Complete the **FORM** referenced by the checklist.
6. Log the transaction in the department **REG**.
7. Store the completed record per **REC-REF-001** and the retention matrix **REC-MATRIX-001**.

## 11. How to Create a New Document

1. Follow the document lifecycle procedure (ADM-PROC-001).
2. Use the standard header block (Document ID, Title, Department, Type, Version, Effective Date, Review Date, Owner, Approving Authority, Supersedes, Related Documents, Related Forms, Record Classification, Retention Requirement).
3. Assign a Document ID from the department’s series (do not reuse numbers).
4. Link the new document to its policy, procedure, checklist, form, and register.
5. Run the validation script before committing.
6. Obtain the approval required by the approval matrix (FIN-CTRL-001).

## 12. How to Retire a Document

1. Follow ADM-PROC-002 (Change Control).
2. Mark the document **Superseded** in its header (set `Supersedes` on the replacement, add a supersession note on the old document).
3. Move obsolete material to the archive location designated by the Records Management function; **do not delete**.
4. Update every reference and index that points to the old document.

## 13. The Transactional Chain

```text
POLICY → PROCEDURE → CHECKLIST → FORM → TRANSACTION → APPROVAL → ACCOUNTING → RECORD → RECONCILIATION → CLOSEOUT → RETENTION
```

That chain is what this layer exists to make real.

## 14. Document Set Index

| ID | Title | Location |
|----|-------|----------|
| ADM-REF-001 | Master Index | `00-START-HERE/MASTER-INDEX.md` |
| ADM-REF-002 | Transaction Map | `00-START-HERE/TRANSACTION-MAP.md` |
| ADM-REF-003 | Migration Map | `00-START-HERE/MIGRATION-MAP.md` |

See the full register of controlled documents in `00-START-HERE/VALIDATION-REPORT.md` (generated) and the department indexes in each folder.

---

**Lost Limb Riders Organization**
*”I Can. I Will. Nobody Is Left Behind. Nobody Stands Alone.”*
