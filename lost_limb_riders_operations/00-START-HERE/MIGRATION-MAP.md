# **Lost Limb Riders — Repository Migration Map**

**Document ID:** ADM-REF-003  
**Document Title:** Lost Limb Riders — Repository Migration Map  
**Department:** Administration  
**Document Type:** REF (Reference)  
**Version:** 1.0  
**Effective Date:** August 12, 2026  
**Review Date:** August 2027  
**Document Owner:** Records & Compliance Officer  
**Approving Authority:** Board of Directors  
**Supersedes:** None  
**Related Documents:** ADM-REF-001, 00-START-HERE/TRANSACTIONAL-LAYER-COMPLETION-REPORT.md  
**Related Forms:** None  
**Record Classification:** Permanent — Governance  
**Retention Requirement:** Permanent (Board)

---

## **Purpose**

This map documents the inventory of the repository and the disposition of every existing document when the transactional operations layer was built. It satisfies the requirement that existing material be evaluated, integrated, and preserved — not silently rewritten or deleted.

## **Repository Inventory (as of August 2026)**

### Active — `lost_limb_riders_handbooks/`

| Path | Contents | Status | Action |
|------|----------|--------|--------|
| `00-START-HERE.md` | Handbook overview and navigation | Active | Retained. Updated to reference the new transactional layer. |
| `01-Organization-Handbook/00-ORGANIZATION-HANDBOOK.md` | Mission, governance framework, bylaws, board handbooks, governance policies, committee charters, admin ops, volunteer handbook, safety/risk, financial procedures, position descriptions, chapter development | Active | Retained and integrated. The transactional layer cross-references its policies rather than duplicating them. |
| `02-Member-Handbook/00-MEMBER-HANDBOOK.md` | Public-facing member handbook | Active | Retained. No change. |
| `03-Program-Manuals/*` | Six program manuals (Peer Connection, Ride Forward, Hospital/Prosthetic Outreach, Housing/Independence, Community Resource, Family Support) | Active | Retained. Mapped into `07-PROGRAMS/`. |
| `04-Forms-and-Templates/*` | 10 forms (release, style guide, enrollment, volunteer application, emergency contact, photo/media, accessibility, incident report, volunteer hours, feedback) | Active | Retained. Integrated into `13-FORMS-AND-TEMPLATES/` index. Incident form reused by the incident workflow (`SAF-INC-001`). |

### Active — `employees/`

| Path | Contents | Status | Action |
|------|----------|--------|--------|
| `01-Chairperson.md` … `42-Safety-Coordinator.md` | 42 position manuals | Active | Retained. Used as job-description source for HR position authorization. |
| `README.md` | Position manual index | Active | Retained. |
| `Wage-Structure-and-Benefits.md` | Compensation framework, wage bands, benefits, expense reimbursement policy | Active | Retained and integrated. Compensation worksheet (`HR-COMP-001`) and approval procedure (`HR-PROC-002`) reference it as the compensation basis. |
| `generate_positions.py` | Position manual generator script | Active | Retained. |

### Archived — `ARCHIVE/PRE-CONSOLIDATION/ORG-INFRASTRUCTURE/`

| File | Contents | Status | Action |
|------|----------|--------|--------|
| `01-Corporate-Governance-Manual.md` | Governance manual | Archived | Superseded by Organization Handbook governance framework. Controls retained. |
| `02-Administrative-Operations-Manual.md` | Admin operations | Archived | Controls integrated into Organization Handbook Admin Ops section. Preserved. |
| `03-Volunteer-Handbook.md` | Volunteer handbook | Archived | Controls integrated into Organization Handbook Volunteer section and `08-VOLUNTEERS/`. Preserved. |
| `04-Family-Support-Program-Manual.md` | Family support program | Archived | Superseded by Program Manuals. Preserved. |
| `05-Safety-and-Risk-Management-Manual.md` | Safety and risk | Archived | Controls retained; incident workflow expanded in `09-SAFETY-RISK/`. Preserved. |
| `06-Financial-Procedures-Manual.md` | Financial procedures | Archived | **Key source.** Expense approval limits, segregation of duties, donation handling, grant tracking, sponsorship management, purchasing, reporting — all integrated into `05-FINANCE/`, `10-FUNDRAISING/`, `11-GRANTS/`, and `FIN-CTRL-001`. Preserved. |
| `07-Chapter-Development-Manual.md` | Chapter development | Archived | Superseded by Organization Handbook Chapter Development section. Preserved. |
| `08-Position-Description-Manual.md` | Position descriptions | Archived | Superseded by `employees/` position manuals. Preserved. |

### Archived — `ARCHIVE/tmp/`

| Location | Contents | Status | Action |
|----------|----------|--------|--------|
| `ARCHIVE/tmp/org/Organizational_Infrastructure/` | Pre-consolidation copies of the eight manuals | Archived | Duplicate of `ARCHIVE/PRE-CONSOLIDATION/`. Preserved as historical. |
| `ARCHIVE/tmp/org/GOVERNANCE-FRAMEWORK/` | Bylaws, governance manual, board handbook, orientation, policies, committee charters | Archived | Superseded by Organization Handbook governance framework. Preserved. |
| `ARCHIVE/tmp/org/` program operations manuals (Peer Connection, Ride Forward) | Program operations manuals | Archived | Superseded by `lost_limb_riders_handbooks/03-Program-Manuals/`. Preserved. |
| `ARCHIVE/tmp/org/*.md` (proposal, about, presentation) | Fundraising collateral | Archived | Preserved. |
| `ARCHIVE/tmp/forms/` | Documentation style guide, participant release | Archived | Duplicate of active forms. Preserved. |
| `ARCHIVE/tmp/pub/` | Pamphlet and proposal (DOCX, markdown, placeholder images) | Archived | Preserved. |
| `ARCHIVE/tmp/AUTOBIOGRAPHY/` | Manuscript, keynote, letters, nonprofit framework | Archived | Preserved as project history. |

### Other Active Content

| Path | Contents | Status | Action |
|------|----------|--------|--------|
| `assets/Presentations/Lost_Limb_Riders_Pitch_Deck.pptx` | Pitch deck | Active | Retained. |
| `.github/` | Agent and copilot instructions | Active | Retained. |
| `AGENTS.md` | Repo operating instructions | Active | Retained. |
| `context.md` | Tone reference for the memoir | Active | Retained. |

## **Duplicates Identified**

1. **Eight ORG-INFRASTRUCTURE manuals** exist in three places: `ARCHIVE/PRE-CONSOLIDATION/ORG-INFRASTRUCTURE/`, `ARCHIVE/tmp/org/Organizational_Infrastructure/`, and consolidated into `lost_limb_riders_handbooks/01-Organization-Handbook/`. The active copy is the Organization Handbook. Archives are preserved as history.
2. **Governance framework** exists in `ARCHIVE/tmp/org/GOVERNANCE-FRAMEWORK/`, `ARCHIVE/tmp/AUTOBIOGRAPHY/NONPROFIT/GOVERNANCE-FRAMEWORK/`, and in the Organization Handbook. Active copy: Organization Handbook.
3. **Program operations manuals** exist in `ARCHIVE/tmp/org/`, `ARCHIVE/tmp/AUTOBIOGRAPHY/NONPROFIT/`, and `lost_limb_riders_handbooks/03-Program-Manuals/`. Active copy: Program Manuals.
4. **Participant release and style guide** exist in `ARCHIVE/tmp/forms/` and in `lost_limb_riders_handbooks/04-Forms-and-Templates/`. Active copy: Forms and Templates.

**Policy going forward:** One active copy per document. Anything else is archived. The Document Register (`01-GOVERNANCE/01-Master-Document-Control-Policy.md`) is the single list of active documents.

## **Integrations Performed**

| Archived control | Integrated into |
|------------------|-----------------|
| Expense approval limits ($250/$1,000/$1,000+/$5,000+) | `01-GOVERNANCE/02-Approval-Matrix.md` (FIN-CTRL-001), `05-FINANCE/05-Purchasing-Procedure.md` |
| Segregation of duties | `FIN-CTRL-001`, `ADM-REF-002` (Transaction Map), `05-FINANCE/08-Financial-Closeout-and-Reconciliation-Procedure.md` |
| Donation handling | `10-FUNDRAISING/01-Donation-Transaction-Procedure.md` |
| Grant tracking | `11-GRANTS/` |
| Sponsorship management | `10-FUNDRAISING/04-Sponsorship-Agreement.md` |
| Incident reporting | `09-SAFETY-RISK/` incident workflow |
| Compensation framework | `03-HUMAN-RESOURCES/10-Compensation-Worksheet.md`, `HR-PROC-002` |

## **New Architecture**

The transactional layer lives in `lost_limb_riders_operations/` with the department structure defined in `ADM-REF-001` (Master Index). The existing `lost_limb_riders_handbooks/` and `employees/` directories are preserved in place. The conceptual separation required by the project directive is preserved: governance, administration, human resources, contractors, finance, events, programs, volunteers, safety/risk, fundraising, grants, compliance, forms, and records management.

## **Consolidation Decisions Recorded**

- No active document was deleted.
- No archived document was deleted.
- Archived documents retain their controls; where a control was integrated, the destination is listed above.
- The word "handled it" is not a closeout. Every transaction now terminates in a documented record per `ADM-REF-002`.

---

## **Revision History**

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | August 12, 2026 | Administration | Initial inventory and migration map |

---

**Lost Limb Riders Organization**  
*"I Can. I Will."*
