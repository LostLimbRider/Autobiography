## Lost Limb Riders — Transaction ID Assignment SOP

**Document ID:** ADM-SOP-001
**Document Title:** Transaction ID Assignment — Standard Operating Procedure
**Department:** Administration
**Document Type:** SOP
**Version:** 1.0
**Effective Date:** August 12, 2026
**Review Date:** August 2027
**Document Owner:** Director of Administration
**Approving Authority:** Executive Director
**Supersedes:** None
**Related Documents:** ADM-REG-001 (Master Transaction Register); MASTER-INDEX.md §6; TRANSACTION-MAP.md
**Related Forms:** None
**Record Classification:** Administrative
**Retention Requirement:** Permanent (while in force)

---

## 1. Purpose

Every transaction class receives a unique, traceable ID. IDs are assigned by the responsible register, never improvised.

## 2. ID Format

```text
CLASS-YYYY-NNN
```

- **CLASS** — two- or three-letter prefix from the table below.
- **YYYY** — calendar year of the transaction.
- **NNN** — sequential number within the year, starting at 001.

| Prefix | Class | Prefix | Class |
|--------|-------|--------|-------|
| EMP | Employee | SPN | Sponsorship |
| CTR | Contractor | GRT | Grant |
| EVT | Event | AST | Asset |
| EXP | Expense | INC | Incident |
| DON | Donation | BRD | Board action |
| TIM | Time record | PAY | Payroll run |

## 3. Assignment Rules

1. Each register (HR-REG-001, CTR-REG-001, EVT-REG-001, FIN-REG-001/002/003, FIN-REG-005/006, GRT-REG-001, SAF-REG-001, GOV-REG-001) is the **single source** for its class’s sequence.
2. The responsible person requests/obtains the ID from the register at the **start** of the transaction (before execution), not after.
3. IDs are never reused, even for voided transactions. Voided transactions are closed as “VOID” with a note.
4. Records that belong to a transaction carry the transaction ID so the audit trail links them (e.g., `EVT-2026-001` → `TIM-2026-017` → `PAY-2026-009`).

## 4. Cross-Referencing

- Related IDs are recorded on the documents themselves.
- The Master Transaction Register (ADM-REG-001) provides the index from any ID to its transaction, parties, amounts, status, and locations.

## 5. Sample Audit Trail

```text
EVT-2026-001            Event authorized
  └── EMP-2026-004      Worker hired for the event
        └── TIM-2026-017  Time record
              └── PAY-2026-009  Payroll run
                    └── EXP-2026-023  Expense allocation
```

---

**End of SOP.**
