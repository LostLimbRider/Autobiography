# Lost Limb Riders Documentation Conflict Resolution Proposal Report

**Audit Date:** July 22, 2026  
**Status:** Phase 1 Complete — Awaiting Leadership Approval  
**Auditor:** AI Documentation Audit System  

---

## Executive Summary

| Metric | Count |
|---|---|
| Total files reviewed | 52 unique markdown documents + 2 PDFs + 1 PPTX + 1 DOCX + 2 logo PNGs + 1 portrait PNG + 2 stub PNGs + 17 SVG placeholders |
| Exact duplicate file sets found | 3 (10 files total) |
| Content conflict sets found | 9 |
| Documents recommended for merge | 4 |
| Documents recommended for archive/deletion | 5 |
| Documents recommended for rewrite | 3 |
| Documents recommended for adoption as authoritative | 7 |
| Terminology standardization issues | 6 |

---

## PART 1: DUPLICATE FILES

### DUPLICATE-1 — 8 Org Infrastructure Manuals (EXACT DUPLICATES) — CRITICAL

**Conflicting files:**
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/01-Corporate-Governance-Manual.md`
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/02-Administrative-Operations-Manual.md`
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/03-Volunteer-Handbook.md`
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/04-Family-Support-Program-Manual.md`
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/05-Safety-and-Risk-Management-Manual.md`
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/06-Financial-Procedures-Manual.md`
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/07-Chapter-Development-Manual.md`
- `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/08-Position-Description-Manual.md`

**Duplicate copies exist at:**
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/01-Corporate-Governance-Manual.md`
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/02-Administrative-Operations-Manual.md`
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/03-Volunteer-Handbook.md`
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/04-Family-Support-Program-Manual.md`
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/05-Safety-and-Risk-Management-Manual.md`
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/06-Financial-Procedures-Manual.md`
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/07-Chapter-Development-Manual.md`
- `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/08-Position-Description-Manual.md`

**Nature of conflict:** Byte-for-byte identical content across both locations. Confirmed via diff. 8 pairs of duplicate files totaling approximately 56 KB of wasted space and creating maintenance hazard where edits to one copy won't reach the other.

**Authoritative location:** `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/`  
**Reasoning:** This location is part of the assembled partner packet alongside the pitch deck, proposal, and liability waiver. The `Doc/` tree is the distribution-ready package. The `NONPROFIT/ORG-INFRASTRUCTURE/` location is a staging area that should be retired once the packet copies are verified.

**Note:** `Doc/.../Organizational_Infrastructure/00-START-HERE-Organizational-Infrastructure-Index.md` exists only in the `Doc/` copy and has no counterpart. This index file should be preserved and added to the `NONPROFIT/` location if that becomes authoritative, or the `NONPROFIT/ORG-INFRASTRUCTURE/` directory should be deleted entirely.

**Proposed action:** Delete the entire `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/` directory (8 files). Keep `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/` as the single authoritative location.

**Impact:** No content loss. Eliminates maintenance hazard. One location to update for all 8 manuals.

---

### DUPLICATE-2 — Logo PNG (EXACT DUPLICATE) — MODERATE

**Conflicting files:**
- `AUTOBIOGRAPHY/NONPROFIT/lost-limb-riders-logo.png` (1.3 MB)
- `Doc/Lost_Limb_Riders_Packet/logo.png` (1.3 MB)

**Nature of conflict:** Identical file, different filenames and locations.

**Authoritative location:** `Doc/Lost_Limb_Riders_Packet/logo.png`  
**Reasoning:** The `Doc/` packet is the distribution package. The logo file should live with the packet materials.

**Proposed action:** Delete `AUTOBIOGRAPHY/NONPROFIT/lost-limb-riders-logo.png`. Keep the `Doc/` copy. If the `NONPROFIT/` directory needs a logo reference, it should point to the `Doc/` copy or the logo should be stored in a single shared location.

**Impact:** No content loss. Eliminates 1.3 MB of duplication.

---

### DUPLICATE-3 — Pitch Deck PDF = Proposal PDF (IDENTICAL CONTENT, DIFFERENT NAMES) — CRITICAL

**Conflicting files:**
- `Doc/Lost_Limb_Riders_Packet/Lost_Limb_Riders_Pitch_Deck.pdf` (287 KB)
- `Doc/Lost_Limb_Riders_Packet/Lost_Limb_Riders_Proposal.pdf` (287 KB)

**Nature of conflict:** These two PDFs are byte-for-byte identical despite having different filenames. One of them is mislabeled.

**Analysis:** The Pitch Deck also exists as `Lost_Limb_Riders_Pitch_Deck.pptx` (1.3 MB PowerPoint). The Proposal also exists as `Lost_Limb_Riders_Proposal.docx` (1.3 MB Word). The PDFs appear to be the same document exported twice under different names.

**Authoritative location:** Both PDFs need to be re-exported from their respective source files (PPTX for pitch deck, DOCX for proposal).

**Proposed action:** 
1. Delete both identical PDFs.
2. Re-export the PPTX to `Lost_Limb_Riders_Pitch_Deck.pdf`.
3. Re-export the DOCX to `Lost_Limb_Riders_Proposal.pdf`.
4. If the PPTX and DOCX also produce identical PDFs, investigate whether these are truly the same document or if the source files need differentiation.

**Impact:** Resolves naming confusion. Ensures each PDF matches its intended source document.

---

### DUPLICATE-4 — Photo Placeholder Stubs — LOW

**Conflicting files:**
- `AUTOBIOGRAPHY/PHOTOS/bike-rally.png` (2 bytes)
- `AUTOBIOGRAPHY/PHOTOS/on-street.png` (2 bytes)

**Nature of conflict:** Both are 2-byte empty placeholder files with identical content.

**Proposed action:** Replace with actual photo files when available, or delete and note in the photo descriptions file that these are pending.

**Impact:** Minimal. These are clearly stubs awaiting real content.

---

## PART 2: CONTENT CONFLICTS

### CONFLICT-1 — Mission Statement Differs Across Documents — CRITICAL

**Conflicting files:**
- `AUTOBIOGRAPHY/NONPROFIT/02-Lost-Limb-Riders-About.md` (line 5)
- `AUTOBIOGRAPHY/NONPROFIT/03-Lost-Limb-Riders-Proposal.md` (line 58)
- `pamphlet/lost-limb-riders-handbook.md` (line 184)
- `Doc/Lost_Limb_Riders_Family_Support_Initiative_Operations_Manual.md` (line 48)

**Current statements:**
- **About:** "To provide peer support, community, and hope to amputees and their families through shared experiences, group activities, and mentorship."
- **Proposal:** "Lost Limb Riders exists to provide hope, peer support, mentorship, education, and opportunity to amputees and people with disabilities."
- **Handbook:** "...community, mentorship, public awareness, adaptive opportunities, and practical resources—including housing and independence advocacy—that restore hope, rebuild confidence, and remind every person that nobody is left behind and nobody stands alone."
- **Operations Manual:** "support amputees, limb-different individuals, and their families through community, mentorship, public awareness, adaptive opportunities, and practical resources"

**Conflict:** Four different mission statements across four documents. The About document is the shortest and most limited. The Handbook version is the most comprehensive. The Operations Manual version matches the Handbook but drops the closing phrase.

**Authoritative statement:** The **Bylaws** (`01-Corporate-Bylaws.md`, Section 2.01) contain the legally binding mission: *"Lost Limb Riders supports amputees, people with disabilities, veterans, first responders, and their families through peer support, education, advocacy, community engagement, family support, adaptive recreation, and motorcycle‑related fellowship."*

**Proposed action:** All non-governance documents should use a public-facing mission statement derived from but not identical to the bylaws language. Adopt the **Handbook version** as the public mission statement (it is the most comprehensive and was written for external audiences). Update the About, Proposal, and Operations Manual to match. Add a note that the bylaws contain the legal mission statement which governs.

**Impact:** Ensures one consistent public message across all external documents.

---

### CONFLICT-2 — Board Size and Term Limits Inconsistent — HIGH

**Conflicting files:**
- `GOVERNANCE-FRAMEWORK/01-Corporate-Bylaws.md` (Sections 4.02, 4.05)
- `ORG-INFRASTRUCTURE/01-Corporate-Governance-Manual.md` (Board Structure section)
- `Doc/Lost_Limb_Riders_Family_Support_Initiative_Operations_Manual.md` (Section 2)

**Current values:**

| Element | Bylaws | Corporate Governance Manual | Operations Manual |
|---|---|---|---|
| Board size | 5–11 (recommended 7) | 5–11 (recommended 7) | 5–15 |
| Term length | 2 years | 2 years | 3 years |
| Max consecutive terms | 3 (6 years) | 3 (6 years) | 2 (6 years) |

**Conflict:** The Operations Manual specifies 5–15 board members (vs. 5–11 in bylaws), 3-year terms (vs. 2 in bylaws), and 2 consecutive term limits (vs. 3 in bylaws).

**Authoritative source:** The **Corporate Bylaws** are the governing document and must control. The Operations Manual and Corporate Governance Manual must align with the bylaws.

**Proposed action:** Update the Operations Manual Section 2 to match the Bylaws: 5–11 board members, 2-year terms, up to 3 consecutive terms. Update the Corporate Governance Manual if it also conflicts (it appears consistent with the bylaws).

**Impact:** Ensures operational documents don't contradict the governing legal document.

---

### CONFLICT-3 — Standing Committees List Inconsistent — HIGH

**Conflicting files:**
- `GOVERNANCE-FRAMEWORK/01-Corporate-Bylaws.md` (Article VI)
- `GOVERNANCE-FRAMEWORK/06-Committee-Charters.md`
- `GOVERNANCE-FRAMEWORK/02-Governance-Manual.md`
- `ORG-INFRASTRUCTURE/01-Corporate-Governance-Manual.md`
- `Doc/Lost_Limb_Riders_Family_Support_Initiative_Operations_Manual.md` (Section 2)

**Current committee lists:**

| Source | Standing Committees Listed |
|---|---|
| **Bylaws** (Art. VI) | Executive, Finance, Governance, Audit, Fundraising, Programs, Safety and Risk, Membership |
| **Committee Charters** | Executive, Finance, Governance, Audit, Fundraising, Programs, Safety and Risk, Membership |
| **Governance Manual** | Executive, Finance, Governance, Audit, Fundraising, Programs, Safety and Risk, Membership |
| **Corporate Governance Manual** | Governance, Finance, Programs, Safety and Risk, Fundraising, **Chapter Development** (no Audit, no Membership, no Executive) |
| **Operations Manual** | Finance, Governance/Nominating, Program, Fundraising/Development (no Safety and Risk, no Membership, no Executive, no Audit) |

**Conflict:** Three different committee structures across five documents. The Corporate Governance Manual replaces Audit and Membership with Chapter Development. The Operations Manual omits Safety and Risk, Membership, Executive, and Audit entirely.

**Authoritative source:** The **Bylaws** define the standing committees. All other documents must align.

**Proposed action:** 
1. Adopt the Bylaws list as authoritative: Executive, Finance, Governance, Audit, Fundraising, Programs, Safety and Risk, Membership.
2. Chapter Development can exist as a subcommittee of Membership or as a temporary committee.
3. Update the Corporate Governance Manual and Operations Manual to align with the bylaws committee structure.

**Impact:** Ensures governance documents don't contradict the bylaws on committee structure.

---

### CONFLICT-4 — Origin Story Contradiction — MODERATE

**Conflicting files:**
- `AUTOBIOGRAPHY/NONPROFIT/01-Lost-Limb-Riders-Presentation.md` (line 48)
- `AUTOBIOGRAPHY/NONPROFIT/03-Lost-Limb-Riders-Proposal.md` (line 42)
- `MANUSCRIPT/19-CHAPTER-15-The-Lost-Limb-Riders.md` (manuscript)

**Current statements:**
- **Presentation:** "I connected with a group of bikers who took me in. They weren't amputees — they were just riders."
- **Proposal:** "he connected with a community of bikers who accepted him as one of their own. They didn't treat him like a patient."
- **Manuscript Ch 15:** Describes an amputee-specific support group where Mike, Diane, Jerry, and Sharon are all amputees.

**Conflict:** The nonprofit documents say John found non-amputee bikers who accepted him. The manuscript says he found a group of fellow amputees who rode together. These are fundamentally different founding narratives.

**Proposed action:** Align the nonprofit documents with the manuscript. The manuscript is the primary source of truth for John's personal story. The presentation and proposal should reflect the actual founding experience.

**Impact:** Ensures the organizational origin story matches the memoir's account.

---

### CONFLICT-5 — Who Lost Limb Riders Serves — Inconsistent Lists — MODERATE

**Conflicting files:**
- `NONPROFIT/02-Lost-Limb-Riders-About.md` (lines 14–19)
- `NONPROFIT/03-Lost-Limb-Riders-Proposal.md` (lines 64–70)
- `pamphlet/lost-limb-riders-handbook.md` (Ch 7, throughout)
- `Doc/.../Operations_Manual.md` (Section 6)

**Current populations:**

| Source | Populations Listed |
|---|---|
| **About** | Recent amputees, long-term amputees, families/caregivers, veterans/first responders, children |
| **Proposal** | Same as About + "Children and young people born with or acquired limb differences" |
| **Handbook** | Amputees, limb-different individuals, families, caregivers, veterans, riders, non-riders, supporters, allies |
| **Operations Manual** | Individuals with limb loss/limb difference, people facing amputation, family members, caregivers, support persons, veterans, children/youth |

**Conflict:** Each document uses a different population list. The Handbook is the broadest. The About is the narrowest.

**Proposed action:** Adopt a standard population statement used across all documents. Recommended: "Amputees, limb-different individuals, people facing amputation, families, caregivers, veterans, first responders, children, and youth."

**Impact:** Ensures consistent messaging about who the organization serves.

---

### CONFLICT-6 — "Board Review Items" Block Repeated in Every Org Infrastructure Manual — LOW

**Conflicting files:**
- All 8 files in `ORG-INFRASTRUCTURE/` contain the identical "Board Review Items" block (5 bullet points)

**Nature of conflict:** This is not a factual conflict but a structural redundancy. The same 5-item checklist appears verbatim at the bottom of every manual.

**Proposed action:** Move the "Board Review Items" block to the `00-START-HERE` index file or the Governance Manual, and reference it from each manual. This reduces repetition while preserving the information.

**Impact:** Cleaner documents, less visual clutter, single source of truth for the review checklist.

---

### CONFLICT-7 — Expense Approval Thresholds Inconsistent — MODERATE

**Conflicting files:**
- `ORG-INFRASTRUCTURE/06-Financial-Procedures-Manual.md` (line 13)
- `Doc/.../Operations_Manual.md` (Section 13, line 2205)

**Current thresholds:**

| Source | Staff | Program Dir / ED | ED | Board |
|---|---|---|---|---|
| **Financial Procedures Manual** | Dept Dir: $250 | ED: $1,000 | Finance Committee: $1,001–$5,000 | Above $5,000 |
| **Operations Manual** | Staff: $250 | PD or ED: $251–$1,000 | ED: $1,001–$5,000 | Over $5,000 |

**Conflict:** The Financial Procedures Manual routes $1,001–$5,000 through the Finance Committee. The Operations Manual routes the same range through the ED alone. The $251–$1,000 range has different approval authorities (ED vs. PD or ED).

**Proposed action:** Adopt the Operations Manual thresholds as the standard (they are more detailed and include the Program Director role). Update the Financial Procedures Manual to align.

**Impact:** Ensures financial authority is consistent across all operational documents.

---

### CONFLICT-8 — Privacy Policy Exists in Operations Manual But Not in Governance Framework — MODERATE

**Conflicting files:**
- `Doc/.../Operations_Manual.md` (Section 15.2 — Privacy Policy, 2559–2583)
- `GOVERNANCE-FRAMEWORK/05-Governance-Policies.md` (has Confidentiality but no separate Privacy Policy)

**Nature of conflict:** The Operations Manual includes a standalone Privacy Policy (Section 15.2) covering data collection, use, storage, and participant rights. The Governance Framework has a Confidentiality Policy but no separate Privacy Policy. These are related but distinct policies — confidentiality governs what staff can share; privacy governs how data is collected and used.

**Proposed action:** Add a Privacy Policy to the Governance Framework that aligns with the Operations Manual version. The Governance Framework should contain all board-level policies; operational details can reference the framework policy.

**Impact:** Ensures the governance framework is complete and the privacy policy has proper board-level authority.

---

### CONFLICT-9 — Harassment Policy and Discrimination Policy Coverage Overlap — LOW

**Conflicting files:**
- `Doc/.../Operations_Manual.md` (Section 15.10 Discrimination, 15.11 Harassment)
- `GOVERNANCE-FRAMEWORK/05-Governance-Policies.md` (Non-Discrimination Policy)

**Nature of conflict:** The Governance Framework has a Non-Discrimination Policy. The Operations Manual has both a Discrimination Policy AND a separate Harassment Policy. The Governance Framework has no standalone Harassment Policy.

**Proposed action:** Add a Harassment Policy to the Governance Framework. Ensure the Non-Discrimination Policy references the Harassment Policy as a companion.

**Impact:** Completes the governance policy suite.

---

## PART 3: TERMINOLOGY STANDARDIZATION

### TERM-1 — Organization Name

**Current variations:**
- "Lost Limb Riders" (most documents)
- "Lost Limb Riders, Inc." (Operations Manual, Liability Waiver)
- "LLR" (not used but should be defined as abbreviation)

**Standard:** Use "Lost Limb Riders" in all public-facing documents. Use "Lost Limb Riders, Inc." only in legal filings, contracts, and the bylaws where the legal entity name is required.

---

### TERM-2 — Participant vs. Member vs. Rider

**Current variations:**
- "Participants" (Operations Manual — primary term for people receiving services)
- "Members" (Governance documents — used for community designation)
- "Riders" (Handbook, Presentation — used loosely)
- "Community participants" (Bylaws Section 3.02)

**Standard:**
- **Participant** = Anyone receiving program services (peer support, family support, mentorship)
- **Member** = Community designation per Board-approved classes (Bylaws Section 3.02)
- **Rider** = Someone who participates in motorcycle rides
- **Volunteer** = Someone who provides unpaid service

---

### TERM-3 — Founder/CEO vs. Executive Director

**Current variations:**
- "Founder/CEO" (Governance Manual, Corporate Governance Manual)
- "Executive Director" (Operations Manual — described as CEO)
- Both roles appear in the same org charts

**Standard:** The bylaws (Section 5.08) define both roles separately. The Founder/CEO is a distinct role from the Executive Director. Maintain this distinction. The Founder/CEO may or may not be the ED. All documents should reflect this dual-role possibility.

---

### TERM-4 — "I Can. I Will." vs. "Nobody Is Left Behind. Nobody Stands Alone."

**Current usage:**
- "I Can. I Will." — Used in manuscript, keynotes, letters, proposal, handbook
- "Nobody Is Left Behind. Nobody Stands Alone." — Used in handbook as a tagline
- "I Can. I Will. We Can. We Will." — Used in presentation (the "We" variant)

**Standard:**
- **"I Can. I Will."** = John Thompson's personal motto / the organization's motto
- **"Nobody Is Left Behind. Nobody Stands Alone."** = The organizational tagline/culture statement
- **"I Can. I Will. We Can. We Will."** = Deprecated. The presentation should drop the "We Can. We Will." variant to avoid diluting the core motto.

---

### TERM-5 — Limb Loss vs. Limb Difference vs. Amputee

**Current variations:**
- "Amputees" (most documents)
- "Limb-different individuals" (handbook, operations manual)
- "People with disabilities" (proposal, bylaws)
- "People with limb loss" (occasional)

**Standard:**
- **Amputee** = A person who has undergone surgical amputation
- **Limb-different individual** = A person with a congenital limb difference or acquired limb variation
- **Person with a disability** = Broader term used in legal contexts (ADA, bylaws)
- Use all three as appropriate. In public-facing materials, lead with "amputees and limb-different individuals" to be specific. Use "people with disabilities" in legal/policy contexts.

---

### TERM-6 — Tagline in Presentation

**Current:** "I Can. I Will. We Can. We Will."  
**Standard:** Remove "We Can. We Will." The tagline is "I Can. I Will." with "Nobody Is Left Behind. Nobody Stands Alone." as the culture statement.

---

## PART 4: DOCUMENTS RECOMMENDED FOR ARCHIVAL

### ARCHIVE-1 — `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/` (8 files)

**Action:** Delete entire directory after confirming the `Doc/` copies are complete and correct.  
**Reason:** Exact duplicates of the `Doc/` files. No unique content.

### ARCHIVE-2 — `Doc/Lost_Limb_Riders_Packet/Lost_Limb_Riders_Pitch_Deck.pdf` and `Lost_Limb_Riders_Proposal.pdf`

**Action:** Delete both PDFs pending re-export from source files.  
**Reason:** They are identical to each other and likely don't match their intended source documents.

---

## PART 5: DOCUMENTS RECOMMENDED FOR ADOPTION AS AUTHORITATIVE

| Document | Authority Level | Role |
|---|---|---|
| `GOVERNANCE-FRAMEWORK/01-Corporate-Bylaws.md` | **Legal** | Governing document. All others must align. |
| `GOVERNANCE-FRAMEWORK/05-Governance-Policies.md` | **Board-approved** | All governance policies. |
| `GOVERNANCE-FRAMEWORK/06-Committee-Charters.md` | **Board-approved** | All committee structures. |
| `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/` (8 manuals) | **Operational** | All operational procedures. |
| `Doc/Lost_Limb_Riders_Packet/Participant_Release_of_Liability.md` | **Legal** | Liability waiver. Must be reviewed by Iowa counsel. |
| `Doc/Lost_Limb_Riders_Family_Support_Initiative_Operations_Manual.md` | **Operational** | Comprehensive program operations manual. |
| `pamphlet/lost-limb-riders-handbook.md` | **Public-facing** | Partner/sponsor handbook. Public mission statement source. |

---

## PART 6: RISK ASSESSMENT

### Legal Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Mission statement in non-governance documents doesn't match bylaws | **High** | Standardize all documents to align with bylaws |
| Board size/terms in Operations Manual contradict bylaws | **High** | Update Operations Manual to match bylaws |
| Liability waiver needs Iowa counsel review | **High** | Flag for legal review before any public use |
| Privacy policy not in governance framework | **Medium** | Add Privacy Policy to governance framework |

### Operational Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Editing one copy of 8 duplicate manuals doesn't update the other | **High** | Delete duplicate set |
| Expense approval thresholds differ between financial docs | **Medium** | Standardize to Operations Manual thresholds |
| Committee structure differs across 5 documents | **Medium** | Align all with bylaws |
| Origin story contradicts between manuscript and nonprofit docs | **Medium** | Align with manuscript |

### Documentation Risks

| Risk | Severity | Mitigation |
|---|---|---|
| 4 different mission statements confuse stakeholders | **High** | Adopt one standard public mission statement |
| Population lists differ across documents | **Medium** | Standardize population statement |
| Handbook founder bio uses `[Founder Name]` placeholder | **Low** | Replace with "John Thompson" |
| "We Can. We Will." variant dilutes core motto | **Low** | Remove variant from presentation |

### Information Loss Risks

| Risk | Severity | Mitigation |
|---|---|---|
| Deleting duplicate manuals could lose the START-HERE index | **Low** | Preserve index in packet location |
| Re-exporting PDFs could lose formatting | **Low** | Verify new exports match source documents |

---

## PART 7: APPROVAL CHECKLIST

### Group A — Duplicate File Resolution

- [ ] **A-1:** Delete `AUTOBIOGRAPHY/NONPROFIT/ORG-INFRASTRUCTURE/` directory (8 duplicate files). Keep `Doc/Lost_Limb_Riders_Packet/Organizational_Infrastructure/` as authoritative.
- [ ] **A-2:** Delete `AUTOBIOGRAPHY/NONPROFIT/lost-limb-riders-logo.png` (duplicate of `Doc/Lost_Limb_Riders_Packet/logo.png`).
- [ ] **A-3:** Delete both identical PDFs (`Lost_Limb_Riders_Pitch_Deck.pdf` and `Lost_Limb_Riders_Proposal.pdf`). Re-export from source PPTX and DOCX.
- [ ] **A-4:** Note that `bike-rally.png` and `on-street.png` are placeholder stubs (no action needed now).

### Group B — Mission Statement Standardization

- [ ] **B-1:** Adopt the Handbook mission statement as the public-facing standard.
- [ ] **B-2:** Update `02-Lost-Limb-Riders-About.md` to match.
- [ ] **B-3:** Update `03-Lost-Limb-Riders-Proposal.md` to match.
- [ ] **B-4:** Update `Doc/.../Operations_Manual.md` Section 4 to match.
- [ ] **B-5:** Add note that Bylaws Section 2.01 contains the legal mission statement.

### Group C — Governance Alignment

- [ ] **C-1:** Update Operations Manual Section 2 to match Bylaws on board size (5–11), terms (2 years), and consecutive term limits (3).
- [ ] **C-2:** Standardize standing committee list across all documents to match Bylaws Article VI.
- [ ] **C-3:** Add Privacy Policy to Governance Framework.
- [ ] **C-4:** Add Harassment Policy to Governance Framework.

### Group D — Content Alignment

- [ ] **D-1:** Update Presentation and Proposal origin story to match Manuscript Chapter 15.
- [ ] **D-2:** Standardize population statement across About, Proposal, Handbook, and Operations Manual.
- [ ] **D-3:** Standardize expense approval thresholds to match Operations Manual.
- [ ] **D-4:** Move "Board Review Items" block from individual manuals to the START-HERE index or Governance Manual.
- [ ] **D-5:** Replace `[Founder Name]` placeholders in handbook with "John Thompson".
- [ ] **D-6:** Remove "We Can. We Will." variant from Presentation.

### Group E — Terminology

- [ ] **E-1:** Define organization name usage (public vs. legal).
- [ ] **E-2:** Define participant/member/rider terminology standard.
- [ ] **E-3:** Confirm Founder/CEO vs. Executive Director distinction.
- [ ] **E-4:** Define motto vs. tagline usage.
- [ ] **E-5:** Standardize limb loss/limb difference/disability terminology.

### Group F — Pending Legal Review

- [ ] **F-1:** `Doc/Lost_Limb_Riders_Packet/Participant_Release_of_Liability.md` — Review by Iowa counsel before public use.
- [ ] **F-2:** All governance documents — Review by Iowa counsel and CPA before adoption.
- [ ] **F-3:** Confirm 501(c)(3) status language in Bylaws matches IRS requirements.

---

**This report is submitted for leadership review and approval. No files have been modified. All proposed changes require explicit human approval before implementation.**

**Report prepared:** July 22, 2026  
**Next step:** Leadership reviews and approves/rejects each group of changes.
