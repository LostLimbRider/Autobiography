# **Lost Limb Riders — Master Transaction Register**

**Document ID:** ADM-REG-001  
**Document Title:** Lost Limb Riders — Master Transaction Register  
**Department:** Administration  
**Document Type:** REG (Register)  
**Version:** 1.0  
**Effective Date:** August 12, 2026  
**Review Date:** August 2027  
**Document Owner:** Records & Compliance Officer  
**Approving Authority:** Executive Director  
**Supersedes:** None  
**Related Documents:** ADM-REF-002 (Transaction Map), GOV-POL-001, CMP-RET-001  
**Related Forms:** None  
**Record Classification:** Permanent — Governance  
**Retention Requirement:** Permanent (Board)

---

## **1. Purpose**

This register is the single index of every material organizational transaction. Each transaction receives a Transaction ID when opened and is tracked to closeout. The register is the starting point for any audit trail.

## **2. Transaction ID System**

| Prefix | Transaction | Example |
|--------|-------------|---------|
| EMP | Employee lifecycle file | EMP-2026-001 |
| CTR | Contractor engagement | CTR-2026-001 |
| EVT | Event | EVT-2026-001 |
| EXP | Expense / reimbursement | EXP-2026-001 |
| DON | Donation | DON-2026-001 |
| SPN | Sponsorship | SPN-2026-001 |
| GRT | Grant | GRT-2026-001 |
| AST | Asset | AST-2026-001 |
| INC | Incident | INC-2026-001 |
| BRD | Board matter | BRD-2026-001 |
| TIM | Time record | TIM-2026-001 |
| PAY | Payroll run / payment | PAY-2026-001 |

Format: `<PREFIX>-<YEAR>-<SEQUENCE>`. Sequence numbers are never reused.

## **3. Register Columns**

```text
Transaction ID | Date | Type | Department | Responsible Person | Counterparty |
Funding Source | Program/Event | Approval Status | Payment Status | Accounting Reference |
Document Location | Compliance Status | Closeout Status
```

## **4. Lifecycle Rules**

1. **Open:** Assign the ID and create the row when the transaction begins (application accepted, event requested, expense incurred, donation received, grant awarded, asset acquired, incident reported).
2. **Update:** Change statuses as approvals, payments, and accounting steps occur. Related IDs (e.g., `EVT-2026-001 → TIM-2026-017`) are recorded in the same row or the event file.
3. **Close:** A transaction is closed only when all required steps are complete: approval, payment/receipt, accounting entry, documentation filed, and reconciliation done.
4. **Never delete rows.** Corrections are dated and annotated.

## **5. Status Values**

**Approval status:** Not Requested, Pending, Approved, Denied, Ratified.  
**Payment status:** Not Due, Pending, Paid, Partial, Refunded, N/A.  
**Compliance status:** Not Required, Pending, Filed, Confirmed, Exempt.  
**Closeout status:** Open, In Progress, Closed, Pending Review, Disputed.

## **6. How to Use**

- The Records & Compliance Officer maintains the register. Department leads report completed transaction IDs monthly for entry.
- Anyone starting a transaction requests an ID from the register owner before spending, committing, or recording.
- Auditors start at the register, then follow each row to its source file.

## **7. Revision History**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | August 12, 2026 | Administration | Initial version |

---

**Lost Limb Riders Organization**  
*"I Can. I Will."*
