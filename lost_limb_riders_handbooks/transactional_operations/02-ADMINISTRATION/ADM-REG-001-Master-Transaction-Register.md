## Lost Limb Riders — Master Transaction Register

**Document ID:** ADM-REG-001
**Document Title:** Master Transaction Register
**Department:** Administration
**Document Type:** REG
**Version:** 1.0
**Effective Date:** August 12, 2026
**Review Date:** August 2027
**Document Owner:** Director of Administration
**Approving Authority:** Executive Director
**Supersedes:** None
**Related Documents:** ADM-SOP-001 (Transaction ID Assignment); TRANSACTION-MAP.md; department registers
**Related Forms:** None
**Record Classification:** Administrative
**Retention Requirement:** Permanent (while in force)

---

## 1. Purpose

The Master Transaction Register is the index of every material transaction across all classes. It lets anyone trace a transaction from authorization through closeout without relying on memory.

## 2. How It Is Maintained

- Each department register feeds a row into this master register.
- Rows are added at transaction start and updated at closeout.
- Maintained by the Director of Administration (or designee).

## 3. Required Columns

```text
Transaction ID | Date | Type | Department | Responsible Person | Counterparty | Amount
| Funding Source | Program/Event | Approval Status | Payment Status | Accounting Reference
| Document Location | Compliance Status | Closeout Status
```

## 4. Status Definitions

- **Approval Status:** NOT AUTHORIZED / AUTHORIZED / PENDING / DENIED / VOID
- **Payment Status:** UNPAID / PAID / PARTIAL / REFUNDED
- **Compliance Status:** COMPLIANT / NON-COMPLIANT / REVIEW NEEDED / NOT APPLICABLE
- **Closeout Status:** OPEN / IN PROGRESS / CLOSED / PENDING / DISPUTED / VOID

## 5. Master Register Table

| Transaction ID | Date | Type | Dept | Responsible | Counterparty | Amount | Funding Source | Program/Event | Approval | Payment | Acct Ref | Doc Location | Compliance | Closeout |
|----------------|------|------|------|-------------|--------------|--------|----------------|---------------|----------|---------|----------|--------------|------------|----------|
| | | | | | | | | | | | | | | |

## 6. Related Department Registers

| Register | ID Series | Location |
|----------|-----------|----------|
| Employee Register | EMP | HR-REG-001 |
| Contractor Register | CTR | CTR-REG-001 |
| Event Register | EVT | EVT-REG-001 |
| Expense Register | EXP | FIN-REG-001 |
| Donation Register | DON | FIN-REG-002 |
| Restricted Funds Register | DON | FIN-REG-003 |
| Payroll Register | PAY | FIN-REG-004 |
| Asset Register | AST | FIN-REG-005 |
| Sponsorship Register | SPN | FIN-REG-006 |
| Grant Register | GRT | GRT-REG-001 |
| Incident Register | INC | SAF-REG-001 |
| Board Action Register | BRD | GOV-REG-001 |
| Contract Register | n/a | ADM-REG-002 |

## 7. Monthly Close

The master register is reconciled to the finance close each month (FIN-CHK-002). Any transaction left OPEN past its expected closeout is reviewed.

---

**End of Register.**
