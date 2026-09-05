# Lost Limb Riders — Controlled Document ID Collision Reconciliation Report

**Document Type:** Reconciliation Report / Incident Analysis
**Subject:** 28 controlled Document IDs claimed by both `lost_limb_riders_operations/` and `lost_limb_riders_handbooks/transactional_operations/`
**Prepared:** September 4, 2026
**Related Evidence:** `HR-CONSOLIDATION-REPORT.md`; `lost_limb_riders_operations/00-START-HERE/TRANSACTIONAL-LAYER-COMPLETION-REPORT.md` (ADM-REF-007); `lost_limb_riders_operations/00-START-HERE/MIGRATION-MAP.md` (ADM-REF-003); `lost_limb_riders_handbooks/transactional_operations/00-START-HERE/MASTER-INDEX.md` (ADM-REF-001)

---

## 1. Scope

Every active controlled Document ID must uniquely identify one authoritative controlled document. Two materially different active documents may not share a Document ID.

Twenty-eight Document IDs are currently claimed by one document in each of two trees:

| Tree | Location | Controlled IDs |
|------|----------|----------------|
| First-generation transactional layer | `lost_limb_riders_operations/` | 79 |
| Current transactional layer | `lost_limb_riders_handbooks/transactional_operations/` | 172 |
| **IDs claimed by both** | | **28** |

None of the 28 pairs are byte-identical (`SHA-256` differs for every pair).

---

## 2. Root-Cause Provenance (established from repository history)

The collision set is **not a defect introduced randomly**. It is an incomplete architecture migration:

| Event | Date (evidence) | What happened |
|-------|-----------------|---------------|
| E1 — First generation built | 2026-08-12/13 (`git log` first add of ops files, commit `5fd7241`) | Transactional operations layer built in `lost_limb_riders_operations/` — 78 controlled documents, flat `NN-Slug.md` filenames, IDs in headers. Completion Report ADM-REF-007 (dated August 12, 2026) defines the layer as "the repository at `lost_limb_riders_operations/`". |
| E2 — HR consolidation precedent | 2026-08-25/26 (`HR-CONSOLIDATION-REPORT.md`) | Canonical `HR-*` tree built in `lost_limb_riders_handbooks/transactional_operations/03-HUMAN-RESOURCES/` (HR-REF-002 index, 28 docs). **All 18 first-generation ops HR files were retired with a "⛔ DO NOT USE — SUPERSEDED" banner** pointing to the canonical replacement. First documented instance of "second-generation file keeps the ID, first-generation file is retired and preserved." |
| E3 — Second generation published | 2026-08-25/26 (`git log` first add of tl files, commits `868cd6a`, `2508079`, `03cc979`) | Full transactional layer published at `lost_limb_riders_handbooks/transactional_operations/` — 172 controlled documents, canonical `DEPT-ID-NNN-Slug.md` naming, per-department indexes, master index. Every department was re-expressed here. |

**Conclusion:** `lost_limb_riders_handbooks/transactional_operations/` is the current, canonical, second-generation transactional layer. `lost_limb_riders_operations/` is the first-generation layer. The E2 precedent (HR) was applied to Human Resources only. The other 26 first-generation files that share IDs with the second generation were left **Active**, producing the collision.

The repository's document-control policy (`lost_limb_riders_operations/01-GOVERNANCE/01-Master-Document-Control-Policy.md`) requires one active version per ID, and requires that superseded versions "never be cited as authority." The E2 banner is the established, non-destructive retirement mechanism (the retired file is preserved with a pointer to the authoritative version).

**Corrective policy (single, evidence-based):** for each collided ID, the second-generation file in `transactional_operations/` keeps the ID (it is the authoritative active document, already named by the convention `DEPT-ID-NNN-Slug.md`). The first-generation file is retired with a `DO NOT USE — SUPERSEDED` banner pointing at its authoritative successor, exactly as HR already did. No document is deleted; history is preserved.

Three collisions (GOV-POL-001, FUND-PROC-002, CTR-CHK-001) are categorically different: the two files are genuinely different documents. In those cases the first-generation file is pointed at its true successor (which has a different ID), and the second-generation owner keeps the ID. Two collisions (HR-CHK-001, HR-TIME-001) are already retired and only require the validator to stop treating a retired document's historical ID as an active duplicate claim.

---

## 3. Collision-by-Collision Determination

Legend:
- **A** — Same logical document / divergent revisions
- **B** — Same logical document / renamed or expanded derivative
- **C** — Different documents incorrectly sharing an ID
- **D** — Superseded/legacy copy
- **E** — Generated/migrated duplicate
- **F** — Cannot determine automatically

Reference counts are repository-wide (excluding `ARCHIVE/` and `.git/`).

---

### Group 1 — Already retired; validator scoping only (no content mutation)

**ID: HR-TIME-001** | Classification: **D** | Confidence: High | Owner decision: **NO**
- Documents: ops `03-HUMAN-RESOURCES/13-Employee-Time-Record.md` — SHA256 `8c997bd71da1e069197b9daa5f0c0128ea232d208bb03eaf20d65036f7279355` vs tl `03-HUMAN-RESOURCES/HR-TIME-001-Employee-Time-Record.md` — SHA256 `3754723f2d6b3030a27f9b799c920d836a0110f1ac7e449c5ac4ac49d23bda9c`
- Titles: "Employee Time Record" vs "Employee Time Record" (identical logical document)
- Status: ops = Superseded (banner, Aug 25, 2026) → tl = Active
- Version / Effective: ops 1.0 / Aug 12, 2026 vs tl 1.0 / Aug 12, 2026
- Relationship & evidence: The ops banner explicitly states the authoritative version is "HR-TIME-001 (Employee Time Record)" at the tl location. Succession is declared in the document itself.
- Recommended authoritative owner: tl file.
- Recommended disposition of other: none — file is already correctly retired and preserved. No banner/text rewrite.
- References affected: 33 files reference `HR-TIME-001` (remap to tl path/ID; the retired file stays historical).

**ID: HR-CHK-001** | Classification: **D** | Confidence: High | Owner decision: **NO**
- Documents: ops `03-HUMAN-RESOURCES/15-Payroll-Checklists.md` — SHA256 `92db698b9981ebe69ac35ee8e0fe75e9dfe9ba503d51b71d3bec0d70c78eef90` vs tl `03-HUMAN-RESOURCES/HR-CHK-001-Employer-Setup-Checklist.md` — SHA256 `7ad2e6442fdabe34a50cf41fc510869052c0263962094ef3ad2bf13d8a46b326`
- Titles: "Payroll Checklists" (retired) vs "Employer Administration Setup Checklist" (active) — different documents
- Status: ops = Superseded (banner) → tl = Active
- Relationship & evidence: The ops banner declares authoritative replacement = `FIN-CHK-001 + FIN-CHK-003 (Payroll Checklists — moved to Finance)`. The ops file is a retired historical record; its ID header is historical.
- Recommended authoritative owner: tl `HR-CHK-001` (Employer Administration Setup Checklist), already the active owner.
- Recommended disposition of other: none — already retired and preserved.
- References affected: 16 files reference `HR-CHK-001` (remap to active owner; retired file historical).

---

### Group 2 — Same logical document; second-generation owner keeps ID (Classification A/B)

| ID | Ops document (first generation) | Tl document (authoritative) | Class | Refs |
|----|--------------------------------|------------------------------|-------|------|
| ADM-PROC-001 | `14-RECORDS-MANAGEMENT/02-Document-Lifecycle-Procedure.md` | `02-ADMINISTRATION/ADM-PROC-001-Document-Lifecycle-Procedure.md` | A | 9 |
| ADM-REF-001 | `00-START-HERE/MASTER-INDEX.md` (v1.1) | `00-START-HERE/MASTER-INDEX.md` (v1.0) | B | 8 |
| ADM-REF-002 | `00-START-HERE/TRANSACTION-MAP.md` | `00-START-HERE/TRANSACTION-MAP.md` | B | 10 |
| ADM-REF-003 | `00-START-HERE/MIGRATION-MAP.md` | `00-START-HERE/MIGRATION-MAP.md` | B | 6 |
| ADM-REG-001 | `14-RECORDS-MANAGEMENT/03-Master-Transaction-Register.md` | `02-ADMINISTRATION/ADM-REG-001-Master-Transaction-Register.md` | A | 24 |
| CMP-CAL-001 | `12-COMPLIANCE/03-Compliance-Calendar.md` | `12-COMPLIANCE/CMP-CAL-001-Compliance-Calendar.md` | A | 28 |
| CMP-IA-001 | `12-COMPLIANCE/02-Iowa-Compliance-Matrix.md` | `12-COMPLIANCE/CMP-IA-001-Iowa-Compliance-Reference.md` | B | 39 |
| CMP-IRS-001 | `12-COMPLIANCE/01-IRS-Compliance-Matrix.md` | `12-COMPLIANCE/CMP-IRS-001-Federal-Compliance-Reference.md` | B | 50 |
| CTR-PROC-001 | `04-CONTRACTORS/02-W9-and-Contractor-Engagement-Procedure.md` | `04-CONTRACTORS/CTR-PROC-001-Contractor-Lifecycle-Procedure.md` | B | 14 |
| EVT-AUTH-001 | `06-EVENTS/03-Event-Authorization-Checklist.md` | `06-EVENTS/EVT-AUTH-001-Event-Authorization-Form.md` | B | 25 |
| EVT-CLOSE-001 | `06-EVENTS/09-Event-Closeout-Checklist.md` (v1.1) | `06-EVENTS/EVT-CLOSE-001-Event-Closeout.md` | B | 25 |
| EVT-FIN-001 | `06-EVENTS/04-Event-Financial-Feasibility-Worksheet.md` | `06-EVENTS/EVT-FIN-001-Event-Financial-Feasibility.md` | B | 24 |
| EVT-HR-001 | `06-EVENTS/06-Event-Staffing-Plan.md` | `06-EVENTS/EVT-HR-001-Event-Staffing-and-Personnel.md` | B | 18 |
| FIN-CTRL-001 | `01-GOVERNANCE/02-Approval-Matrix.md` | `05-FINANCE/FIN-CTRL-001-Organizational-Approval-Matrix.md` | A | 87 |
| FIN-EXP-001 | `05-FINANCE/01-Expense-Report.md` (v1.1) | `05-FINANCE/FIN-EXP-001-Expense-Report.md` (v1.0) | A | 29 |
| FIN-EXP-002 | `05-FINANCE/02-Expense-and-Reimbursement-Procedure.md` (v1.1) | `05-FINANCE/FIN-EXP-002-Reimbursement-Procedure.md` | A/B | 21 |
| FIN-EXP-003 | `05-FINANCE/03-Mileage-Log.md` | `05-FINANCE/FIN-EXP-003-Mileage-Log.md` | A | 11 |
| FIN-EXP-004 | `05-FINANCE/04-Missing-Receipt-Declaration.md` (v1.1) | `05-FINANCE/FIN-EXP-004-Missing-Receipt-Declaration.md` | A | 11 |
| FUND-PROC-001 | `10-FUNDRAISING/01-Donation-Transaction-Procedure.md` (v1.1) | `10-FUNDRAISING/FUND-PROC-001-Donation-Processing-Procedure.md` | B | 17 |
| FUND-SPON-001 | `10-FUNDRAISING/04-Sponsorship-Agreement.md` | `10-FUNDRAISING/FUND-SPON-001-Sponsorship-Agreement.md` | A | 16 |
| GRT-PROC-001 | `11-GRANTS/01-Grant-Lifecycle-Procedure.md` | `11-GRANTS/GRT-PROC-001-Grant-Lifecycle-Procedure.md` | A | 17 |
| SAF-REG-001 | `09-SAFETY-RISK/02-Incident-Log.md` | `09-SAFETY-RISK/SAF-REG-001-Incident-Register.md` | B | 19 |
| VOL-PROC-001 | `08-VOLUNTEERS/01-Volunteer-System-Procedure.md` | `08-VOLUNTEERS/VOL-PROC-001-Volunteer-Assignment-Process.md` | B | 29 |

**Relationship evidence (applies to all 23):** same topic, same `DEPT` family, same ID, all original files dated Effective August 12, 2026 at the first-generation location; second-generation files carry the identical ID under the canonical `DEPT-ID-NNN-Slug.md` naming convention at the `transactional_operations/` location. Titles are either identical (A) or a renamed/expanded derivative (B). This is the exact pattern HR resolved in E2.

**Determination for all 23:** Recommended authoritative ID owner = the `transactional_operations/` file. Recommended disposition of other = retire the ops file by adding the standard `⛔ DO NOT USE — SUPERSEDED` banner (pointing at the tl path) — matching the HR banner verbatim — leaving the file preserved. Confidence: High. Owner decision: **NO** (established by the E2 precedent and the naming convention).

---

### Group 3 — Different documents sharing an ID; first-generation pointed at its true successor

**ID: GOV-POL-001** | Classification: **C** | Confidence: High | Owner decision: **NO**
- Documents: ops `01-GOVERNANCE/03-Records-Policy.md` ("Records Policy") vs tl `01-GOVERNANCE/GOV-POL-001-Document-Control-Policy.md` ("Document Control Policy")
- Status: both Active. Ops file references the OLD ops Master Document Control Policy ID system.
- Relationship & evidence: different documents. The tl tree separately owns GOV-POL-002 ("Records and Record-Keeping Policy") and GOV-POL-003 ("Records Retention Policy"), which cover the ops Records Policy topic. `GOV-POL-001` in the tl tree is named "Document Control Policy" — the ops file `01-GOVERNANCE/03-Records-Policy.md` is NOT that document.
- Recommended authoritative owner: tl `GOV-POL-001` Document Control Policy.
- Recommended disposition of other: retire ops `03-Records-Policy.md` with banner pointing to tl `GOV-POL-002` + `GOV-POL-003` (the actual successors of its content).
- References affected: 17 files reference `GOV-POL-001` (verify each; those meaning the ops records-policy concept must point to GOV-POL-002/003, those meaning document control keep GOV-POL-001).

**ID: FUND-PROC-002** | Classification: **C** | Confidence: High | Owner decision: **NO**
- Documents: ops `10-FUNDRAISING/02-Donation-Acknowledgment-Procedure.md` ("Donation Receipt and Acknowledgment Procedure") vs tl `10-FUNDRAISING/FUND-PROC-002-Sponsorship-Procedure.md` ("Sponsorship Procedure")
- Status: both Active.
- Relationship & evidence: different documents. The tl tree owns the donation-receipt content under `05-FINANCE/FIN-PROC-005-Donation-Receipt-and-Acknowledgment-Procedure.md` and `FIN-FORM-006-Donation-Acknowledgment.md`. `FUND-PROC-002` in the tl tree is named "Sponsorship Procedure."
- Recommended authoritative owner: tl `FUND-PROC-002` Sponsorship Procedure.
- Recommended disposition of other: retire ops `02-Donation-Acknowledgment-Procedure.md` with banner pointing to tl `FIN-PROC-005` + `FIN-FORM-006` (true successors of its content).
- References affected: 15 files reference `FUND-PROC-002` (verify each).

**ID: CTR-CHK-001** | Classification: **C** | Confidence: High | Owner decision: **NO**
- Documents: ops `04-CONTRACTORS/07-Year-End-1099-Review.md` ("Year-End 1099 Review", v1.1) vs tl `04-CONTRACTORS/CTR-CHK-001-Contractor-Classification-Checklist.md` ("Contractor Classification Checklist", v1.0)
- Status: both Active.
- Relationship & evidence: different documents. The tl tree owns the 1099 review as `CTR-SOP-001-Year-End-1099-Review-SOP.md`. `CTR-CHK-001` in the tl tree is named "Contractor Classification Checklist."
- Recommended authoritative owner: tl `CTR-CHK-001` Contractor Classification Checklist.
- Recommended disposition of other: retire ops `07-Year-End-1099-Review.md` with banner pointing to tl `CTR-SOP-001` (true successor of its content).
- References affected: 21 files reference `CTR-CHK-001` (verify each).

---

## 4. Summary of Determinations

| Classification | Count | IDs |
|----------------|-------|-----|
| A — Same logical document / divergent revisions | 10 | ADM-PROC-001, ADM-REG-001, CMP-CAL-001, FIN-CTRL-001, FIN-EXP-001, FIN-EXP-002, FIN-EXP-003, FIN-EXP-004, FUND-SPON-001, GRT-PROC-001 |
| B — Same logical document / renamed or expanded derivative | 13 | ADM-REF-001, ADM-REF-002, ADM-REF-003, CMP-IA-001, CMP-IRS-001, CTR-PROC-001, EVT-AUTH-001, EVT-CLOSE-001, EVT-FIN-001, EVT-HR-001, FUND-PROC-001, SAF-REG-001, VOL-PROC-001 |
| C — Different documents incorrectly sharing an ID | 3 | GOV-POL-001, FUND-PROC-002, CTR-CHK-001 |
| D — Superseded/legacy copy (already retired) | 2 | HR-CHK-001, HR-TIME-001 |
| E / F | 0 | — |

**Arithmetic check (verified September 4, 2026 against the manifest):** total collisions = 10 + 13 + 3 + 2 = **28**; of which already-superseded historical claims = **2** (D) and active collisions requiring remediation = **26** (A+B+C); 2 + 26 = **28**. Every enumerated ID appears exactly once across the four classes.

**Owner-level policy decisions required: NONE.** Every collision resolves deterministically from:
1. the E2 HR precedent (retire first-generation file with banner; second-generation keeps ID);
2. the naming convention (`DEPT-ID-NNN-Slug.md` = second-generation ownership);
3. the true-successor mappings for the three C-classification collisions.

---

## 5. Proposed Atomic Correction Plan (after authorization)

1. Add `⛔ DO NOT USE — SUPERSEDED` banner (HR verbatim format) to the 26 first-generation ops files (24 from Groups 2-3, plus the 2 Group-1 files only if headers still claim IDs — see scoping note).
2. For C-classification retirements, the banner names the true successor ID (`GOV-POL-002/GOV-POL-003`, `FIN-PROC-005/FIN-FORM-006`, `CTR-SOP-001`).
3. Update references in the first-generation tree and handbooks to point at the authoritative second-generation documents (atomic referential-integrity change; FIN-CTRL-001 alone touches 87 files).
4. Scope `validate_ops.py` duplicate checks to **active controlled documents only** — retired/superseded documents are historical records, not active claims. This satisfies the invariant without rewriting archived history (per the executive directive's scoping rule).
5. Add the repository invariant to this incident's documentation and to `AGENTS.md`: *"Every active controlled Document ID must uniquely identify one authoritative controlled document."*
6. Add regression protection to `validate_ops.py`: duplicate-ID detection on the active corpus (reporting Document ID, all claiming files, titles, collision count), failing the build when an unauthorized collision is introduced. Duplicate IDs may exist only among retired/historical documents, and that exception is now explicit.
7. Re-run `validate_ops.py`, `validate_transactional_layer.py`, `validate_founder_identity.py`, and the reference audits until green.
8. Document this incident (this report) and register it as the incident record.

---

## 6. Invariant

> **Every active controlled Document ID must uniquely identify one authoritative controlled document. Two materially different active documents may not share the same Document ID. Duplicate IDs are permitted only on retired/superseded historical records, which are exceptions and are never cited as authority.**

---

## 7. Execution Record — Atomic Remediation (September 4, 2026)

Executed under the Executive Directive of September 4, 2026. All steps from Section 5 were completed.

**Collision dispositions:**
- Original collision set: **28**
- Already-superseded historical claims (Group 1): **2** — HR-CHK-001, HR-TIME-001 (no content mutation; existing banners retained)
- First-generation documents newly retired with the canonical `⛔ DO NOT USE — SUPERSEDED` banner: **26** (23 same-ID successors + 3 true-successor mappings)
- First-generation files now carrying a `DO NOT USE` banner (including pre-existing HR retirements): **44**
- No Document IDs were renumbered, deleted, overwritten, or merged.

**Class-C reference resolution (semantic, per-citation — no blind replacement):**
- `GOV-POL-001` (Records Policy): 2 active first-generation files retargeted to GOV-POL-002 (Records and Record-Keeping) and GOV-POL-003 (Records Retention). 1 pre-retired file left as history.
- `FUND-PROC-002` (Donation Receipt and Acknowledgment): 3 active first-generation files retargeted to FIN-PROC-005 (Receipt and Acknowledgment); the active reference meaning "sponsorship" was preserved as the current FUND-PROC-002 (Sponsorship Procedure).
- `CTR-CHK-001` (Year-End 1099 Review): 8 active first-generation citations retargeted to CTR-SOP-001 (Year-End 1099 Review SOP); classification-checklist citations now resolve to the current CTR-CHK-001 (Contractor Classification) owner in the canonical layer.

**Path-based reference retargeting (active → canonical layer):**
- 3 active first-generation documents retargeted path references to retired files onto `lost_limb_riders_handbooks/transactional_operations/` (Change Control; Master Document Control Policy ×2; Administration Department Index ×5).
- GOV-REF-001 (Governance Index) added to the canonical MASTER-INDEX; no longer orphaned.

**Validator changes:**
- `validate_ops.py` now enforces ACTIVE-ID uniqueness — one authoritative active document per ID. Superseded documents (canonical banner or Status field) keep historical IDs, are exempt from duplicate-ID, duplicate-filename, and orphan checks, and are never treated as authority. Failure output reports Document ID, claiming files, titles, statuses, and the active-collision count. References to superseded-only filenames are errors; 00-START-HERE migration records are exempt.

**Results:**
- Active duplicate IDs: **0**
- Broken .md references: **0**
- Unknown Document ID references: **0**
- Orphaned active documents: **0**
- References to superseded documents: **0**
- `validate_ops.py`: PASS (exit 0; 285 documents scanned, 223 controlled IDs, 0 active-ID collisions)
- `validate_transactional_layer.py`: PASS (172 files)
- `validate_founder_identity.py`: PASS
- `AGENTS.md`: Document ID Active Uniqueness invariant recorded
- Commit: delivered atomically with the incident; SHA reported in the delivery completion report

---

*This report was produced under the Executive Directive of September 4, 2026. No controlled Document IDs were mutated during the analysis or the remediation; the 26 first-generation documents were retired with supersession banners that preserve their historical IDs.*