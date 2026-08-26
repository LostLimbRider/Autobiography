## Lost Limb Riders — Test Scenario 01: Purchase Requisition Through Payment

**Test ID:** TEST-01
**Test Type:** Control walkthrough (hypothetical)
**Documents Under Test:** FIN-FORM-004, FIN-PROC-001, FIN-FORM-005, FIN-PROC-002, FIN-EXP-001, FIN-CTRL-001, FIN-REG-001
**Tested By:** ____________________ **Date:** ____________

---

## 1. Scenario

The organization needs a $180 public-address amplifier for a ride safety briefing. All amounts are hypothetical.

## 2. Steps

- [ ] Requester completes FIN-FORM-004 (Purchase Requisition) for $180.00.
- [ ] Requester is not the approver. Approver is the Department Director (within the $250 limit per FIN-CTRL-001).
- [ ] Approval is documented on the requisition with signature and date.
- [ ] Purchase is made; supplier invoice and receipt are attached.
- [ ] Requester completes FIN-EXP-001 (Expense Report) with receipt attached.
- [ ] Supervisor approves the expense report.
- [ ] Finance reviews the payment for policy compliance (FIN-PROC-002).
- [ ] Finance processes payment; two-person review where required.
- [ ] Transaction ID is assigned from FIN-REG-001 (EXP-2026-####).
- [ ] Transaction is posted to the accounting records (FIN-PROC-002 §accounting).
- [ ] Record is filed per REC-MATRIX-001.
- [ ] Master Transaction Register (ADM-REG-001) is updated.

## 3. Expected Result

Transaction is traceable end to end: requisition → approval → purchase → receipt → report → payment → register → accounting → retention. All approval levels match FIN-CTRL-001.

## 4. Result

- [ ] Pass — traceability confirmed
- [ ] Fail — variance noted: ______________________________________________

---

**End of Test.**
