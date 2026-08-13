# **Lost Limb Riders — Transaction Map**

**Document ID:** ADM-REF-002  
**Document Title:** Lost Limb Riders — Transaction Map  
**Department:** Administration  
**Document Type:** REF (Reference)  
**Version:** 1.0  
**Effective Date:** August 12, 2026  
**Review Date:** August 2027  
**Document Owner:** Records & Compliance Officer  
**Approving Authority:** Board of Directors  
**Supersedes:** None  
**Related Documents:** ADM-REF-001, ADM-REF-003, FIN-CTRL-001, 14-RECORDS-MANAGEMENT/03-Master-Transaction-Register.md  
**Related Forms:** None  
**Record Classification:** Permanent — Governance  
**Retention Requirement:** Permanent (Board)

---

## **Purpose**

This map shows the complete lifecycle of every material organizational transaction. For each transaction class it identifies the responsible parties, the authorizing document, the forms and checklists used, the resulting accounting, the record produced, and closeout. It is the quickest way to answer: *"What do we do for this?"*

## **How to Read This Map**

Each transaction class lists the **workflow** followed by the **control documents** that govern it. A "→" shows handoff from one responsible party to the next. Cross-references point to the exact file that carries the detail.

## **Transaction Classes**

### 1. Employment (Hire to Separation)

**Workflow:**

```text
Position Need → Position Authorization → Job Description → Compensation Analysis →
Recruitment → Application → Interview → Selection → Conflict Check →
Compensation Approval → Offer → Acceptance → Onboarding → Payroll Setup →
Training → Active Employment → Timekeeping → Payroll → Performance Review →
Compensation Review → Separation → Final Payroll → Access Revocation →
Property Return → Record Retention
```

**Responsible chain:** Board/Executive → Hiring manager → HR/Records & Compliance → Payroll → Finance.

**Control documents:** `03-HUMAN-RESOURCES/` — position authorization (HR-POS-001), recruitment (HR-REC-001), application (HR-APP-001), interview (HR-INT-001), offer (HR-OFR-001), onboarding (HR-ONB-001), personnel file (HR-FIL-001), compensation worksheet (HR-COMP-001), compensation approval (HR-PROC-002), time record (HR-TIME-001), payroll (HR-PROC-004), performance (HR-PERF-001), separation (HR-SEP-001).

**Transaction IDs:** `EMP-YYYY-###` (employee file), `TIM-YYYY-###` (time records), `PAY-YYYY-###` (payroll runs).

**Record trail:** Personnel file → payroll file → time records → tax filings → Master Transaction Register.

### 2. Contractor Engagement

**Workflow:**

```text
Business Need → Classification Review → Selection → Conflict Review → W-9 →
Written Agreement → Scope of Work → Rate → Approval → Work → Invoice →
Verification → Payment → Accounting → 1099 Determination → Closeout
```

**Control documents:** `04-CONTRACTORS/` — classification (CTR-001), W-9 procedure (CTR-PROC-001), agreement (CTR-002), scope of work (CTR-003), invoice (CTR-004), payment authorization (CTR-005), 1099 review (CTR-CHK-001).

**Transaction ID:** `CTR-YYYY-###`.

**Record trail:** Contract file → invoice → payment record → 1099 file → Master Transaction Register.

### 3. Event

**Workflow:**

```text
Request → Event Authorization & Feasibility → Approval → Staffing Plan → Event Day →
Revenue & Expense Capture → Payroll/Invoices → Event Closeout → Postmortem
```

**Control documents:** `06-EVENTS/` — master record (EVT-MSTR-001), authorization (EVT-AUTH-001), feasibility (EVT-FIN-001), budget (EVT-BUD-001), staffing (EVT-HR-001), event-day (EVT-DAY-001), revenue (EVT-REV-001), closeout (EVT-CLOSE-001), postmortem (EVT-POST-001).

**Transaction ID:** `EVT-YYYY-###`. Related records cross-reference it: `EMP-`, `TIM-`, `PAY-`, `EXP-`, `SPN-`, `DON-`.

**Record trail:** Event file → financial feasibility → staffing plan → time records → expense reports → revenue logs → closeout → postmortem.

### 4. Expense / Reimbursement

**Workflow:**

```text
Need → Purchase or Out-of-Pocket Spend → Documentation → Expense Report →
Approval → Payment (or Reimbursement) → Accounting → Reconciliation → Retention
```

**Control documents:** `05-FINANCE/` — expense report (FIN-EXP-001), reimbursement procedure (FIN-EXP-002), mileage log (FIN-EXP-003), missing receipt (FIN-EXP-004), purchasing (FIN-PUR-001), purchasing authorization (FIN-PUR-002), payment authorization (FIN-PAY-001).

**Transaction ID:** `EXP-YYYY-###`.

**Record trail:** Expense report → receipts → approval → payment → journal entry → reconciliation.

### 5. Donation

**Workflow:**

```text
Donation Received → Identify Donor → Determine Restriction → Receipt/Acknowledgment →
Deposit → Accounting → Donor Record → Restricted Fund Tracking → Reconciliation
```

**Control documents:** `10-FUNDRAISING/` — donation procedure (FUND-PROC-001), acknowledgment (FUND-PROC-002), restricted funds (FUND-REST-001), sponsorship vs. donation vs. sales (FUND-REF-001).

**Transaction ID:** `DON-YYYY-###`.

**Record trail:** Donation log → acknowledgment copy → deposit slip → journal entry → donor record.

### 6. Sponsorship

**Workflow:**

```text
Prospect → Proposal → Negotiation → Agreement → Deliverables Defined → Payment →
Recognition/Performance → Reconciliation → Thank-You & Report
```

**Control documents:** `10-FUNDRAISING/04-Sponsorship-Agreement.md` (FUND-SPON-001), `10-FUNDRAISING/05-Donations-vs-Sponsorships-vs-Sales.md` (FUND-REF-001).

**Transaction ID:** `SPN-YYYY-###`.

**Record trail:** Agreement → deliverables log → payment → acknowledgment/report → donor record.

### 7. Grant

**Workflow:**

```text
Opportunity → Eligibility → Application → Approval → Award Agreement →
Restricted/Unrestricted Classification → Budget → Expenditures → Documentation →
Program Performance → Financial Reporting → Grant Closeout
```

**Control documents:** `11-GRANTS/` — lifecycle (GRT-PROC-001), grant file (GRT-001).

**Transaction ID:** `GRT-YYYY-###`.

**Record trail:** Dedicated grant file (application, award, budget, expenditures, reports) → reconciliation → closeout.

### 8. Purchase

**Workflow:**

```text
Need → Budget Check → Authorization → Quoting (if required) → Purchase →
Receipt of Goods/Services → Invoice → Verification → Payment → Accounting
```

**Control documents:** `05-FINANCE/` — purchasing procedure (FIN-PUR-001), purchasing authorization (FIN-PUR-002), payment authorization (FIN-PAY-001), Approval Matrix (FIN-CTRL-001).

**Transaction ID:** `EXP-YYYY-###` (or procurement line within the purchasing authorization).

**Record trail:** Purchase authorization → invoice → approval → payment → journal entry.

### 9. Incident

**Workflow:**

```text
Incident → Immediate Response → Incident Report → Supervisor Review →
Risk/Insurance Review → Corrective Action → Board/Escalation if Required → Closeout
```

**Control documents:** `09-SAFETY-RISK/` — incident procedure (SAF-INC-001), incident log (SAF-REG-001), insurance procedure (SAF-INS-001); form `08-Incident-Report-Form.md` in `lost_limb_riders_handbooks/04-Forms-and-Templates/`.

**Transaction ID:** `INC-YYYY-###`.

**Record trail:** Incident report → follow-up → insurance/legal notification → corrective action → closeout. Medical details stay out of this repository.

### 10. Volunteer Assignment

**Workflow:**

```text
Application → Screening → Orientation → Agreement → Assignment →
Time Tracking → Reimbursement (if any) → Safety Training → Incident Reporting → Separation
```

**Control documents:** `08-VOLUNTEERS/`, plus existing forms in `lost_limb_riders_handbooks/04-Forms-and-Templates/` (Volunteer Application, Volunteer Hours Tracking).

**Record trail:** Volunteer file → hours log → incident records → recognition/closeout.

### 11. Board Matter

**Workflow:**

```text
Matter → Notice → Discussion → Disclosure/Recusal → Motion → Vote →
Minutes/Resolution → Filing/Storage
```

**Control documents:** `01-GOVERNANCE/`, governance framework in `lost_limb_riders_handbooks/01-Organization-Handbook/`.

**Transaction ID:** `BRD-YYYY-###`.

**Record trail:** Minutes/resolution → corporate records → Master Transaction Register.

### 12. Asset Acquisition and Disposal

**Workflow (acquisition):** Need → Budget → Authorization → Purchase → Receipt → Tag/Register → Accounting.  
**Workflow (disposal):** Authorization → Disposition → Proceeds → Register Update → Accounting.

**Control documents:** `05-FINANCE/11-Asset-Register.md` (AST-001).

**Transaction ID:** `AST-YYYY-###`.

**Record trail:** Asset register → purchase/disposal records → depreciation/accounting → register update.

## **Cross-Reference Conventions**

Related transaction records reference each other so the trail stays intact. Example:

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

Every document in a trail carries the related IDs. The Master Transaction Register (`14-RECORDS-MANAGEMENT/03-Master-Transaction-Register.md`) is the single index that ties them together.

## **Separation of Duties**

For every money-moving transaction, the people performing these roles should differ where practical:

```text
Requester → Approver → Payer → Reconciler
```

Where the organization's size makes full separation impractical, the limitation and the compensating control are documented in `01-GOVERNANCE/02-Approval-Matrix.md` (FIN-CTRL-001). The minimum control is always: the approver is not the requester, and a second person reviews bank statements.

## **Emergency Transactions**

Emergency expenditures or actions are permitted when safety or legal exposure requires immediate action. The action is documented immediately, and the approval is ratified by the Executive Director within 24 hours and by the Board at the next meeting. Emergency does not bypass documentation.

---

## **Revision History**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | August 12, 2026 | Administration | Initial version — transaction layer launch |

---

**Lost Limb Riders Organization**  
*"I Can. I Will."*
