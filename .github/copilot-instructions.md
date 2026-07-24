# Copilot Instructions for Autobiography Repository

This repository contains John Thompson's autobiography manuscript, keynote speeches, and supporting materials for Lost Limb Riders nonprofit.

## Repository Structure

```
.
├── AGENTS.md              — Full agent custom instructions
├── context.md             — Tone/voice reference (ChatGPT logs)
├── Doc/                   — Lost Limb Riders organizational documents
│   └── Lost_Limb_Riders_Packet/
├── ARCHIVE/               — Historical content (reference only)
└── tmp/                   — Working drafts and audit reports
```

The manuscript itself (26 files: outline, title, dedication, foreword, author's note, 17 chapters, afterword, acknowledgments, about the author, back cover) exists in a connected workspace outside this repo root.

## Writing Voice & Tone

**Non-negotiable:** John Thompson's authentic voice is direct, conversational, and unapologetic.

- **Short, punchy sentences.** No flowery language.
- **Tell it like it is.** Raw truth—no self-pity, no sanitization.
- **Use humor** to cut through heavy material (cancer, amputation, addiction, recovery).
- **Swear naturally** if it fits the context. This is a memoir, not a textbook.
- **Talk to the reader like a friend at a bar**, not a lecture.

**Reference:** `context.md` contains real conversation examples showing John's exact speech patterns and humor. Match that energy.

**Book tagline:** "I Can. I Will."

## Key Content Constraints

### Manuscript Word Count (Hard Requirements)
- **Full manuscript target:** 15,000–20,000 words across 17 chapters
- **Per-chapter minimum:** 1,200 words (exceeding is fine; being under is not)
- **Check chapter length before considering content complete**

### Reedsy-Compatible Markdown (Hard Requirements)
All manuscript content must survive copy-paste into Reedsy Studio without broken formatting:

- **Chapter headings:** `# **Chapter X: Title**` (bold inside heading, not outside)
- **Apostrophes & quotes:** Always curly/smart (`' ' " "`) — never straight (`' "`)
- **Dialogue:** Use blockquote `>` for spoken words; put speaker attribution **outside** the blockquote
- **Em dashes:** `—` (not `--` or `-`)
- **Compound-word hyphens:** `‐` (non-breaking hyphen U+2011, not regular hyphen `-`)
- **Horizontal rules:** `---` permitted in title page and outline, but **NOT in chapter content**
- **No tables, fenced code blocks, raw HTML, or fancy formatting**
- **UTF-8 encoding only**

**Gotcha:** Back matter (Afterword, Acknowledgments, About the Author, Back Cover) uses plain `# Heading` format, not `# **Chapter X: Title**`.

### Keynote & Non-Manuscript Content
- Keynote speeches use a different format (speech notes with audience/tone headers)
- Do **not** apply manuscript chapter formatting rules to keynote files
- Letters and other supporting content follow their own conventions (check existing files)

## Key People & Context

These characters recur throughout:

- **John Thompson** — Amputee (right leg, below knee), cancer survivor, heart attack survivor, recovering addict, motorcycle rider, motivational speaker.
- **Genie** — John's wife. Stuck with him through everything.
- **Daughters** — Two adult daughters, appear throughout the narrative.
- **Roxy** — John's dog. Recurring character with personality. "Roxy... Roxanne... scan, scan, scan."
- **Lost Limb Riders** — Amputee motorcycle community. John rides with them. Also a nonprofit organization featured in the repo.
- **Grinnell** — John's hometown. His father worked for the city there.

## When You Edit or Create Content

1. **Check word count.** Every chapter must exceed 1,200 words. Count carefully.
2. **Validate formatting.** Use curly quotes, em dashes, non-breaking hyphens in compounds.
3. **Match tone.** If it sounds like a textbook, it's not John's voice. Strip it back down.
4. **Reference context.md** if you're unsure about tone. That conversation is the north star.
5. **Never invent facts.** Every event, name, and detail is John's actual life. Verify or ask.

## For Other File Types

- **PPTX, DOCX files** (Doc/): Treat as supporting materials. Don't reformat them.
- **Photo descriptions**: Keep them factual and brief.
- **Nonprofit documents**: Use professional tone; don't apply memoir voice rules.

## No Build, Test, or Lint Commands

This is a content repository. There are no automated builds, tests, or linters. Quality is maintained through:
- Manual review of word count per chapter
- Verification of Reedsy markdown compatibility (copy-paste test)
- Tone consistency checks against `context.md`
- Factual accuracy review by John Thompson

---

**Full agent instructions:** See `AGENTS.md` in the repository root.
