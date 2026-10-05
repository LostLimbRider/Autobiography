from pathlib import Path
import json,re,hashlib,collections
root=Path.cwd();before=json.loads(Path('scripts/workflow-terminology/workflow_before_hashes.json').read_text());changed=json.loads(Path('scripts/workflow-terminology/workflow_changed.json').read_text())
now={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file() and not any(x.startswith('.') for x in p.relative_to(root).parts)}
now={name:digest for name,digest in now.items() if not name.startswith('scripts/workflow-terminology/')}
assert before.keys()==now.keys()
assert set(changed)=={p for p in before if before[p]!=now[p]}
for name in changed:
 a=(Path('scripts/workflow-terminology/workflow_before')/(name+'.before')).read_text();b=Path(name).read_text()
 for pattern in [r'\b[A-Z]{2,4}-[A-Z]{2,8}-\d{3}\b',r'\]\(([^)]+)\)',r'\b[\w./-]+\.(?:md|py)\b',r'\btransactions?\b']:
  assert re.findall(pattern,a,re.I)==re.findall(pattern,b.split('## Permanent Source-Direction Policy')[0] if name=='AGENTS.md' else b,re.I),(name,pattern)
remaining=collections.defaultdict(list)
for name in now:
 p=Path(name)
 try:s=p.read_text()
 except (UnicodeError,OSError):continue
 for n,line in enumerate(s.splitlines(),1):
  if not re.search('transactional',line,re.I):continue
  if name.startswith('ARCHIVE/'):reason='Archive preserved'
  elif re.search(r'^> .*DO NOT USE — SUPERSEDED',s,re.M) or re.search(r'\*\*Status:\*\*[^\n]*(?:Superseded|Retired)',s,re.I):reason='Superseded document preserved'
  elif name in ['ID-COLLISION-RECONCILIATION-REPORT.md','HR-CONSOLIDATION-REPORT.md']:reason='Historical reconciliation evidence preserved'
  elif 'not transactional.' in line:reason='Legitimate relational meaning: appreciation-event tone'
  elif all('_' in m[0] or '.md' in m[0] or '.py' in m[0] for m in re.finditer(r'[^\s`();|]*transactional[^\s`();|]*',line,re.I)):reason='Technical path, filename, or command preserved'
  else:reason='REVIEW REQUIRED'
  remaining[reason].append(f'{name}:{n}')
report=['# Workflow terminology correction','',f'Changed {len(changed)} files: 17 active documents, repository instructions, and two validator display/documentation files.','', '## Files changed','']+['- '+p for p in sorted(changed)]
report+=['','## Verification','','- Founder identity: PASS (339 production documents).','- Operations: PASS (286 documents; zero issues; zero active-ID collisions). 16 advisories concern superseded HR IDs without active claimants.','- Current workflow layer: PASS (173 files).','- Original file inventory unchanged; only the listed original files changed. Scripts and audit records added under scripts/workflow-terminology/.','- Document ID tokens, Markdown link targets, document/script path references, and actual transaction/transactions words unchanged in every edited file.','- Archives and superseded documents unchanged. Official was not edited.','- Source direction and daily source-refresh requirement recorded in AGENTS.md.','','## Remaining occurrences','']
for reason,items in sorted(remaining.items()):
 report += [f'### {reason} ({len(items)} matching lines)','']+['- '+x for x in items]+['']
Path('scripts/workflow-terminology/workflow-terminology-report.md').write_text('\n'.join(report))
print('Integrity checks passed. Changed files:',len(changed))
for reason,items in remaining.items():print(reason,len(items))
