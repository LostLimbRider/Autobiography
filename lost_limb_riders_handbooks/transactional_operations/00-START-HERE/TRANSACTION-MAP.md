## Lost Limb Riders — Transaction Map

**Document ID:** ADM-REF-002
**Document Title:** Transaction Map — Complete Lifecycle Reference
**Department:** Administration
**Document Type:** REF
**Version:** 1.0
**Effective Date:** August 12, 2026
**Review Date:** August 2027
**Document Owner:** Executive Director
**Approving Authority:** Board of Directors
**Supersedes:** None
**Related Documents:** ADM-REG-001 (Master Transaction Register); ADM-SOP-001 (Transaction ID Assignment); MASTER-INDEX.md
**Related Forms:** As referenced per workflow
**Record Classification:** Administrative
**Retention Requirement:** Permanent (while in force)

---

## 1. Purpose

This map shows the complete lifecycle of every material transaction class. Each workflow names the governing policy, the procedure, the checklist, the forms, the register, the approval authority, the accounting treatment, the record location, and the closeout.

## 2. Shared Principles

- Every transaction gets a **transaction ID** from its register (ADM-SOP-001).
- Every transaction is **authorized before** execution (except true emergencies, which follow the emergency-expenditure rule in FIN-CTRL-001).
- **Requester → Approver → Payer → Reconciler** are separated where practical; where the organization’s size makes this impossible, a compensating control is documented.
- Every transaction closes with a documented record and a closeout state.

## 3. Employee Hire and Pay

```text
Position Need → Position Authorization (HR-FORM-001) → Job Description (HR-REF-001)
→ Compensation Worksheet (HR-FORM-005) → Compensation Approval (HR-SOP-003)
→ Recruitment (HR-SOP-002) → Application (HR-FORM-002) → Interview (HR-FORM-003)
→ Selection + Conflict Check → Offer (HR-FORM-004) → Acceptance
→ Onboarding (HR-CHK-002, HR-SOP-004) → Payroll Setup (HR-FORM-006)
→ Active Employment → Timekeeping (HR-TIME-001, HR-SOP-005) → Payroll (FIN-PROC-004, FIN-CHK-001)
→ Performance Review (HR-FORM-007) → Separation (HR-SOP-006, HR-CHK-004, HR-CHK-005)
→ Final Payroll → Access Revocation → Property Return → Record Retention
```

- Policy: HR-POL-001, GOV-POL-005
- Registers: HR-REG-001 (employees), FIN-REG-004 (payroll)
- Accounting: FIN-PROC-004 (payroll journal entry)
- Records: HR-CHK-003 (personnel file), REC-MATRIX-001
- Closeout: separation record + final-payroll record

## 4. Contractor Engagement and Payment

```text
Business Need → Classification Review (CTR-CHK-001) → Selection → Conflict Review
→ W-9 (CTR-CHK-002) → Written Agreement (CTR-FORM-001) → Scope of Work (CTR-FORM-002)
→ Rate + Approval → Work Performed → Invoice (CTR-FORM-003) → Verification
→ Payment Authorization (CTR-FORM-004) → Payment → Accounting → 1099 Review (CTR-SOP-001)
→ Closeout
```

- Policy: CTR-POL-001
- Registers: CTR-REG-001
- Accounting: FIN-PROC-002
- Records: 14-RECORDS-MANAGEMENT

## 5. Event Lifecycle

```text
Event Opportunity → Event Authorization (EVT-AUTH-001) → Feasibility (EVT-FIN-001)
→ Contract + Insurance + Permits → Staffing Plan (EVT-HR-001) → Worker Assignments (EVT-HR-002)
→ Event Day (EVT-CHK-001) → Revenue/Expense Logs (EVT-FORM-001/002)
→ Closeout (EVT-CLOSE-001) → Postmortem if needed (EVT-PROC-002)
```

- Policy: EVT-POL-001
- Register: EVT-REG-001
- Accounting: FIN-PROC-008 (month-end), event cost allocation
- Records: EVT-REF-001 (event master file)

## 6. Expense and Reimbursement

```text
Need → Purchase Requisition (FIN-FORM-004) → Approval (FIN-CTRL-001) → Purchase
→ Receipt → Expense Report (FIN-FORM-001) or Mileage Log (FIN-FORM-002)
→ Supervisor Approval → Finance Review → Payment → Accounting → Reconciliation → Retention
```

- Missing receipt: FIN-FORM-003 (Missing Receipt Declaration) — never a loophole; see FIN-PROC-003.
- Register: FIN-REG-001
- Accounting: FIN-PROC-002

## 7. Donation

```text
Donation Received → Identify Donor → Determine Restriction → Receipt/Acknowledgment
(FIN-PROC-005) → Deposit (FIN-CHK-004) → Accounting → Donor Record → Restricted Fund
Tracking (FIN-PROC-006) → Reconciliation
```

- Register: FIN-REG-002 (donations), FIN-REG-003 (restricted funds)
- Distinguish: donation vs sponsorship vs sales (FUND-POL-001)

## 8. Sponsorship

```text
Prospect → Offer → Sponsorship Agreement (FUND-SPON-001) → Payment → Deliverables
→ Recognition → Tracking (FUND-FORM-001) → Closeout
```

- Register: FIN-REG-006

## 9. Grant

```text
Opportunity → Eligibility (GRT-FORM-001) → Application → Award → Classification
→ Budget (GRT-FORM-002) → Expenditures → Documentation → Reporting (GRT-FORM-003)
→ Program Performance → Closeout (GRT-FORM-004)
```

- Register: GRT-REG-001
- Restricted-fund tracking: FIN-PROC-006

## 10. Asset Acquisition and Disposal

```text
Need → Approval (FIN-CTRL-001) → Purchase → Tag and Record (FIN-REG-005, Asset Register)
→ Custodian → Depreciation/Accounting → Condition Review → Disposal Approval
→ Disposition → Proceeds Recorded
```

## 11. Incident

```text
Incident → Immediate Response → Incident Report (existing 04-Forms incident form
+ SFT-FORM-001 cover sheet) → Incident ID (SFT-REG-001) → Supervisor Review
→ Risk/Insurance Review (SFT-SOP-001) → Corrective Action (SFT-SOP-002)
→ Escalation if required (SFT-CHK-001) → Closeout
```

- Medical information stays out of the public repository (confidentiality rules, MASTER-INDEX.md §8).

## 12. Volunteer Lifecycle

```text
Application (existing 04-Forms volunteer application) → Screening → Orientation
→ Agreement (VOL-FORM-001) → Assignment → Service → Time Tracking (existing
09-Volunteer-Hours-Tracking form) → Expense Reimbursement (FIN-PROC-003)
→ Incident Reporting → Recognition → Separation
```

- Policy: VOL-POL-001 — a volunteer is not an unpaid employee.

## 13. Master Register Linkage

Every transaction class above writes a row into the Master Transaction Register (ADM-REG-001) with:

```text
Transaction ID | Date | Type | Department | Responsible Person | Counterparty | Amount
| Funding Source | Program/Event | Approval Status | Payment Status | Accounting Reference
| Document Location | Compliance Status | Closeout Status
```

## 14. Retention

Every transaction class maps to a retention line in REC-MATRIX-001. Destruction follows REC-SOP-002.

---

**End of Transaction Map.**
