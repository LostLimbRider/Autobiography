# Workflow terminology correction

Changed 20 files: 17 active documents, repository instructions, and two validator display/documentation files.

## Files changed

- AGENTS.md
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/COMPLETION-REPORT.md
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/MASTER-INDEX.md
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/MIGRATION-MAP.md
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/VALIDATION-REPORT.md
- lost_limb_riders_handbooks/transactional_operations/01-GOVERNANCE/GOV-POL-001-Document-Control-Policy.md
- lost_limb_riders_handbooks/transactional_operations/01-GOVERNANCE/GOV-POL-002-Records-and-Record-Keeping-Policy.md
- lost_limb_riders_handbooks/transactional_operations/01-GOVERNANCE/GOV-REF-001-Governance-Index.md
- lost_limb_riders_handbooks/transactional_operations/02-ADMINISTRATION/ADM-PROC-001-Document-Lifecycle-Procedure.md
- lost_limb_riders_handbooks/transactional_operations/07-PROGRAMS/PRO-REF-001-Programs-Index-and-Transactional-Controls.md
- lost_limb_riders_handbooks/transactional_operations/08-VOLUNTEERS/VOL-REF-001-Volunteer-Program-Index.md
- lost_limb_riders_handbooks/transactional_operations/13-FORMS-AND-TEMPLATES/00-FORMS-INDEX.md
- lost_limb_riders_handbooks/transactional_operations/validate_transactional_layer.py
- lost_limb_riders_operations/00-START-HERE/TRANSACTIONAL-LAYER-COMPLETION-REPORT.md
- lost_limb_riders_operations/00-START-HERE/VALIDATION-TEST-SCENARIOS.md
- lost_limb_riders_operations/02-ADMINISTRATION/00-Administration-Department-Index.md
- lost_limb_riders_operations/06-EVENTS/10-Event-Postmortem-and-Lessons-Learned.md
- lost_limb_riders_operations/07-PROGRAMS/00-Programs-Department-Index.md
- lost_limb_riders_operations/13-FORMS-AND-TEMPLATES/00-Forms-and-Templates-Index.md
- lost_limb_riders_operations/tools/validate_ops.py

## Verification

- Founder identity: PASS (339 production documents).
- Operations: PASS (286 documents; zero issues; zero active-ID collisions). 16 advisories concern superseded HR IDs without active claimants.
- Current workflow layer: PASS (173 files).
- Original file inventory unchanged; only the listed original files changed. Scripts and audit records added under scripts/workflow-terminology/.
- Document ID tokens, Markdown link targets, document/script path references, and actual transaction/transactions words unchanged in every edited file.
- Archives and superseded documents unchanged. Official was not edited.
- Source direction and daily source-refresh requirement recorded in AGENTS.md.

## Remaining occurrences

### Archive preserved (2 matching lines)

- ARCHIVE/tmp/LEGAL-REVIEW-QUEUE.md:7
- ARCHIVE/tmp/org/Hospital-and-Prosthetic-Partner-Outreach-Administrative-Operations-Manual.md:1569

### Historical reconciliation evidence preserved (14 matching lines)

- ID-COLLISION-RECONCILIATION-REPORT.md:4
- ID-COLLISION-RECONCILIATION-REPORT.md:6
- ID-COLLISION-RECONCILIATION-REPORT.md:18
- ID-COLLISION-RECONCILIATION-REPORT.md:19
- ID-COLLISION-RECONCILIATION-REPORT.md:32
- ID-COLLISION-RECONCILIATION-REPORT.md:33
- ID-COLLISION-RECONCILIATION-REPORT.md:34
- ID-COLLISION-RECONCILIATION-REPORT.md:36
- ID-COLLISION-RECONCILIATION-REPORT.md:40
- ID-COLLISION-RECONCILIATION-REPORT.md:111
- ID-COLLISION-RECONCILIATION-REPORT.md:113
- ID-COLLISION-RECONCILIATION-REPORT.md:172
- ID-COLLISION-RECONCILIATION-REPORT.md:200
- ID-COLLISION-RECONCILIATION-REPORT.md:213

### Legitimate relational meaning: appreciation-event tone (1 matching lines)

- lost_limb_riders_handbooks/03-Program-Manuals/03-Hospital-and-Prosthetic-Outreach-Program.md:1569

### Superseded document preserved (85 matching lines)

- HR-CONSOLIDATION-REPORT.md:20
- HR-CONSOLIDATION-REPORT.md:28
- HR-CONSOLIDATION-REPORT.md:134
- HR-CONSOLIDATION-REPORT.md:187
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:5
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:7
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:8
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:12
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:15
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:33
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:68
- lost_limb_riders_operations/00-START-HERE/MASTER-INDEX.md:190
- lost_limb_riders_operations/00-START-HERE/TRANSACTION-MAP.md:7
- lost_limb_riders_operations/00-START-HERE/TRANSACTION-MAP.md:8
- lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md:7
- lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md:8
- lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md:24
- lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md:33
- lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md:41
- lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md:42
- lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md:113
- lost_limb_riders_operations/01-GOVERNANCE/02-Approval-Matrix.md:7
- lost_limb_riders_operations/01-GOVERNANCE/02-Approval-Matrix.md:8
- lost_limb_riders_operations/01-GOVERNANCE/03-Records-Policy.md:7
- lost_limb_riders_operations/01-GOVERNANCE/03-Records-Policy.md:8
- lost_limb_riders_operations/03-HUMAN-RESOURCES/01-Employer-Setup-Checklist.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/02-Employee-Lifecycle-Procedure.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/03-Position-Authorization-Form.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/04-Recruitment-Checklist.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/05-Employment-Application-Template.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/06-Interview-Evaluation-Form.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/07-Offer-Letter-Template.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/08-Employee-Onboarding-Checklist.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/09-Personnel-File-System.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/10-Compensation-Worksheet.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/11-Compensation-Approval-Procedure.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/12-Timekeeping-Procedure.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/13-Employee-Time-Record.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/14-Payroll-Procedure.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/15-Payroll-Checklists.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/16-Performance-Review-Form.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/17-Disciplinary-Procedure.md:7
- lost_limb_riders_operations/03-HUMAN-RESOURCES/18-Employee-Separation-Checklist.md:7
- lost_limb_riders_operations/04-CONTRACTORS/02-W9-and-Contractor-Engagement-Procedure.md:7
- lost_limb_riders_operations/04-CONTRACTORS/02-W9-and-Contractor-Engagement-Procedure.md:8
- lost_limb_riders_operations/04-CONTRACTORS/07-Year-End-1099-Review.md:7
- lost_limb_riders_operations/04-CONTRACTORS/07-Year-End-1099-Review.md:8
- lost_limb_riders_operations/05-FINANCE/01-Expense-Report.md:7
- lost_limb_riders_operations/05-FINANCE/01-Expense-Report.md:8
- lost_limb_riders_operations/05-FINANCE/02-Expense-and-Reimbursement-Procedure.md:7
- lost_limb_riders_operations/05-FINANCE/02-Expense-and-Reimbursement-Procedure.md:8
- lost_limb_riders_operations/05-FINANCE/03-Mileage-Log.md:7
- lost_limb_riders_operations/05-FINANCE/03-Mileage-Log.md:8
- lost_limb_riders_operations/05-FINANCE/04-Missing-Receipt-Declaration.md:7
- lost_limb_riders_operations/05-FINANCE/04-Missing-Receipt-Declaration.md:8
- lost_limb_riders_operations/06-EVENTS/03-Event-Authorization-Checklist.md:7
- lost_limb_riders_operations/06-EVENTS/03-Event-Authorization-Checklist.md:8
- lost_limb_riders_operations/06-EVENTS/04-Event-Financial-Feasibility-Worksheet.md:7
- lost_limb_riders_operations/06-EVENTS/04-Event-Financial-Feasibility-Worksheet.md:8
- lost_limb_riders_operations/06-EVENTS/06-Event-Staffing-Plan.md:7
- lost_limb_riders_operations/06-EVENTS/06-Event-Staffing-Plan.md:8
- lost_limb_riders_operations/06-EVENTS/09-Event-Closeout-Checklist.md:7
- lost_limb_riders_operations/06-EVENTS/09-Event-Closeout-Checklist.md:8
- lost_limb_riders_operations/08-VOLUNTEERS/01-Volunteer-System-Procedure.md:7
- lost_limb_riders_operations/08-VOLUNTEERS/01-Volunteer-System-Procedure.md:8
- lost_limb_riders_operations/09-SAFETY-RISK/02-Incident-Log.md:7
- lost_limb_riders_operations/09-SAFETY-RISK/02-Incident-Log.md:8
- lost_limb_riders_operations/10-FUNDRAISING/01-Donation-Transaction-Procedure.md:7
- lost_limb_riders_operations/10-FUNDRAISING/01-Donation-Transaction-Procedure.md:8
- lost_limb_riders_operations/10-FUNDRAISING/02-Donation-Acknowledgment-Procedure.md:7
- lost_limb_riders_operations/10-FUNDRAISING/02-Donation-Acknowledgment-Procedure.md:8
- lost_limb_riders_operations/10-FUNDRAISING/04-Sponsorship-Agreement.md:7
- lost_limb_riders_operations/10-FUNDRAISING/04-Sponsorship-Agreement.md:8
- lost_limb_riders_operations/11-GRANTS/01-Grant-Lifecycle-Procedure.md:7
- lost_limb_riders_operations/11-GRANTS/01-Grant-Lifecycle-Procedure.md:8
- lost_limb_riders_operations/12-COMPLIANCE/01-IRS-Compliance-Matrix.md:7
- lost_limb_riders_operations/12-COMPLIANCE/01-IRS-Compliance-Matrix.md:8
- lost_limb_riders_operations/12-COMPLIANCE/02-Iowa-Compliance-Matrix.md:7
- lost_limb_riders_operations/12-COMPLIANCE/02-Iowa-Compliance-Matrix.md:8
- lost_limb_riders_operations/12-COMPLIANCE/03-Compliance-Calendar.md:7
- lost_limb_riders_operations/12-COMPLIANCE/03-Compliance-Calendar.md:8
- lost_limb_riders_operations/14-RECORDS-MANAGEMENT/02-Document-Lifecycle-Procedure.md:7
- lost_limb_riders_operations/14-RECORDS-MANAGEMENT/02-Document-Lifecycle-Procedure.md:8
- lost_limb_riders_operations/14-RECORDS-MANAGEMENT/03-Master-Transaction-Register.md:7
- lost_limb_riders_operations/14-RECORDS-MANAGEMENT/03-Master-Transaction-Register.md:8

### Technical path, filename, or command preserved (26 matching lines)

- AGENTS.md:97
- AGENTS.md:112
- lost_limb_riders_handbooks/transactional_operations/validate_transactional_layer.py:5
- lost_limb_riders_handbooks/transactional_operations/validate_transactional_layer.py:18
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/MASTER-INDEX.md:59
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/MASTER-INDEX.md:67
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/MIGRATION-MAP.md:34
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/VALIDATION-REPORT.md:13
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/VALIDATION-REPORT.md:22
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/VALIDATION-REPORT.md:57
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/VALIDATION-REPORT.md:58
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/COMPLETION-REPORT.md:13
- lost_limb_riders_handbooks/transactional_operations/00-START-HERE/COMPLETION-REPORT.md:47
- lost_limb_riders_handbooks/transactional_operations/03-HUMAN-RESOURCES/HR-REF-002-HR-Packet-Index.md:22
- lost_limb_riders_operations/00-START-HERE/VALIDATION-TEST-SCENARIOS.md:22
- lost_limb_riders_operations/01-GOVERNANCE/01-Master-Document-Control-Policy.md:13
- lost_limb_riders_operations/01-GOVERNANCE/01-Master-Document-Control-Policy.md:133
- lost_limb_riders_operations/01-GOVERNANCE/05-Change-Control-Procedure.md:13
- lost_limb_riders_operations/01-GOVERNANCE/05-Change-Control-Procedure.md:55
- lost_limb_riders_operations/02-ADMINISTRATION/00-Administration-Department-Index.md:28
- lost_limb_riders_operations/02-ADMINISTRATION/00-Administration-Department-Index.md:29
- lost_limb_riders_operations/02-ADMINISTRATION/00-Administration-Department-Index.md:30
- lost_limb_riders_operations/02-ADMINISTRATION/00-Administration-Department-Index.md:31
- lost_limb_riders_operations/02-ADMINISTRATION/00-Administration-Department-Index.md:33
- lost_limb_riders_operations/03-HUMAN-RESOURCES/SUPERSEDED-NOTICE.md:7
- lost_limb_riders_operations/13-FORMS-AND-TEMPLATES/00-Forms-and-Templates-Index.md:28
