# **Lost Limb Riders — Validation Test Scenarios**

**Document ID:** ADM-REF-006  
**Document Title:** Lost Limb Riders — Validation Test Scenarios  
**Department:** Administration  
**Document Type:** REF (Reference / Test protocol)  
**Version:** 1.0  
**Effective Date:** August 12, 2026  
**Review Date:** August 2027  
**Document Owner:** Records & Compliance Officer  
**Approving Authority:** Executive Director  
**Supersedes:** None  
**Related Documents:** ADM-REF-002, EVT-POST-001, tools/validate_ops.py  
**Related Forms:** EVT-POST-001  
**Record Classification:** Permanent — Governance  
**Retention Requirement:** Permanent

---

## **1. Purpose**

This document defines twelve test scenarios that exercise the transactional layer end to end. Each scenario is run on a **simulated** basis (fictional names, no real data) and documents which documents, IDs, and controls the scenario exercises. The results are reported in the completion report (`00-START-HERE/TRANSACTIONAL-LAYER-COMPLETION-REPORT.md`).

## **2. Scenario 1 — New Employee**

Hire an employee from authorization through first payroll.

| Step | Document | Expected output |
|------|----------|-----------------|
| Position need | HR-POS-001 | Authorization with ID |
| Compensation | HR-COMP-001 + HR-PROC-002 | Approved rate + board/ED sign-off |
| Recruitment/interview | HR-REC-001, HR-APP-001, HR-INT-001 | Documented selection |
| Offer/accept | HR-OFR-001 | Signed offer |
| Onboarding | HR-ONB-001 | W-4, I-9, Iowa withholding, direct deposit, new-hire report |
| Timekeeping | HR-TIME-001 | Certified + supervisor-approved record |
| Payroll | HR-CHK-001, HR-PROC-004 | PAY ID, journal entry, tax deposit |
| File/register | HR-FIL-001, ADM-REG-001 | EMP ID tracked to close |

**Pass criteria:** Every step has a document; the trail runs EMP → TIM → PAY; no step "handled."

## **3. Scenario 2 — Contractor**

Engage a contractor through payment and year-end review.

| Step | Document |
|------|----------|
| Classification | CTR-001 (must reach "contractor" by facts) |
| W-9 + agreement | CTR-PROC-001, CTR-002, CTR-003 |
| Invoice/verification | CTR-004 |
| Payment | CTR-005, FIN-PAY-001 |
| Year-end | CTR-CHK-001 (1099 determination) |

**Pass criteria:** No payment without W-9, agreement, verification; classification documented; 1099 reviewed.

## **4. Scenario 3 — Paid Event**

Accept a paid event through final closeout.

| Step | Document |
|------|----------|
| Event ID | EVT-MSTR-001 |
| Authorization | EVT-AUTH-001 |
| Feasibility | EVT-FIN-001 (flags run before acceptance) |
| Budget/staffing | EVT-BUD-001, EVT-HR-001 |
| Event day | EVT-DAY-001 (time, revenue, expenses captured) |
| Payroll/invoices | HR-CHK-001, CTR-005 |
| Closeout | EVT-CLOSE-001 (actual net; variance explained) |

**Pass criteria:** Economics known before acceptance; final result calculated; unfunded-labor flag would stop the Fort Dodge concert failure (EVT-POST-001).

## **5. Scenario 4 — Volunteer Event**

An event involving volunteers.

| Step | Document |
|------|----------|
| Volunteer onboarding | VOL-PROC-001, VOL-001, application |
| Event | EVT-MSTR-001, EVT-DAY-001 |
| Hours | Volunteer Hours Tracking form |
| Reimbursement (if any) | VOL-002, FIN-EXP-001 |
| Incident (if any) | SAF-INC-001 |

**Pass criteria:** Volunteers remain distinct from employees; no wage payments to volunteers; hours logged for recognition/reporting.

## **6. Scenario 5 — Expense Reimbursement ($250)**

An employee spends $250 personally and requests reimbursement.

| Step | Document |
|------|----------|
| Pre-approval | FIN-EXP-002 (over $100 pre-approval) |
| Documentation | FIN-EXP-001 + receipt |
| Approval | FIN-CTRL-001 (approver ≠ claimant) |
| Payment | FIN-PAY-001, PAY ID |

**Pass criteria:** Approval before the fact (or justified exception); receipt attached; approver differs from claimant.

## **7. Scenario 6 — Unrestricted $1,000 Donation**

| Step | Document |
|------|----------|
| Receive/identify | FUND-PROC-001 (DON ID) |
| Restriction | Unrestricted (FUND-REST-001) |
| Acknowledgment | FUND-PROC-002 |
| Deposit/accounting | EVT-REV-001 log or donation log; journal entry |
| Reconciliation | FIN-CLOSE-001 |

**Pass criteria:** Donation logged with DON ID; acknowledgment issued; deposit verified; record retained.

## **8. Scenario 7 — Restricted $1,000 Donation**

Same as Scenario 6, plus: restriction recorded exactly; funds tracked in FUND-REST-001; spending matches restriction; monthly restricted-fund reconciliation.

**Pass criteria:** Restricted funds never commingled in reporting; if purpose impossible, donor agreement or return documented.

## **9. Scenario 8 — $2,500 Sponsorship**

| Step | Document |
|------|----------|
| Agreement | FUND-SPON-001 (benefits defined) |
| Payment | SPN ID; deposit; acknowledgment per FUND-REF-001 |
| Deliverables | Deliverable log; post-event report |

**Pass criteria:** Payment classified as sponsorship (not donation); benefits delivered and verified; quid-pro-quo acknowledgment.

## **10. Scenario 9 — $10,000 Restricted Grant**

| Step | Document |
|------|----------|
| Opportunity/application | GRT-PROC-001 |
| Award/agreement | GRT-001, approval per FIN-CTRL-001 |
| Restriction | FUND-REST-001 |
| Spending | Purchasing (FIN-PUR-001) coded to GRT |
| Reporting | Grant reports by deadline |
| Closeout | Final report + funder sign-off |

**Pass criteria:** Dedicated grant file; restricted spend; reports on time; closeout documented.

## **11. Scenario 10 — Event Incident**

| Step | Document |
|------|----------|
| Report | Incident Report Form within 24 hours |
| ID/log | INC ID; SAF-REG-001 |
| Review | Supervisor + risk review (SAF-INC-001) |
| Insurance | SAF-INS-001 notification |
| Corrective action | Assigned, tracked to completion |
| Closeout | Log closed; lessons captured |

**Pass criteria:** Escalation path defined; insurance notified; no medical data in public repository.

## **12. Scenario 11 — Employee Separation**

| Step | Document |
|------|----------|
| Separation | HR-SEP-001 |
| Final pay | HR-CHK-001 (Checklist C), Iowa timing |
| Access/property | Revocation + return logs |
| Records | HR-FIL-001 closeout; EMP ID closed in register |

**Pass criteria:** Final payroll within Iowa timing; access revoked; property logged; record retention set.

## **13. Scenario 12 — Audit Trace ($1,842.17)**

An auditor asks: "Show me why this $1,842.17 expenditure occurred."

| Step | Document |
|------|----------|
| Register | Master Transaction Register row (EXP/EVT ID) |
| Authorization | FIN-PUR-002 / EVT-AUTH-001 / EVT-FIN-001 |
| Support | Invoice, receipt, purchase documents |
| Approval | FIN-CTRL-001 approver |
| Payment | FIN-PAY-001, bank reconciliation |
| Accounting | Journal entry, program/event allocation |
| Closeout | Event closeout / reconciliation |

**Pass criteria:** The auditor can trace the amount from authorization through supporting records to the ledger in under 30 minutes using the register.

## **14. Running the Scenarios**

Run each scenario using fictional data on paper or in a test spreadsheet. Complete every form, assign IDs, and file the results in a restricted test folder (test records are still restricted if they mimic real forms). Record results in the completion report. Re-run any scenario after a material system change.

## **15. Revision History**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | August 12, 2026 | Administration | Initial version |

---

**Lost Limb Riders Organization**  
*"I Can. I Will."*
