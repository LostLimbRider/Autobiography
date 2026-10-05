from pathlib import Path
import re,json,hashlib
root=Path.cwd()
raise SystemExit('Completed one-time migration; retained for review only. Use audit_workflow_terms.py to verify.')
files=[p for p in root.rglob('*') if p.is_file() and not any(x.startswith('.') for x in p.relative_to(root).parts)]
snapshot={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
Path('scripts/workflow-terminology/workflow_before_hashes.json').write_text(json.dumps(snapshot))
changed=[]
for p in files:
    rel=str(p.relative_to(root))
    if p.suffix not in ('.md','.py'): continue
    s=p.read_text()
    if not (rel=='AGENTS.md' or rel.startswith(('lost_limb_riders_operations/','lost_limb_riders_handbooks/transactional_operations/'))): continue
    if '⛔ DO NOT USE — SUPERSEDED' in s or re.search(r'\*\*Status:\*\*[^\n]*(?:Superseded|Retired)',s,re.I): continue
    # Match prose words only; preserve path components and identifiers.
    t=re.sub(r'\btransactional workflows\b','workflows',s,flags=re.I)
    t=re.sub(r'(?<![\w/.-])transactional(?![\w/]|-[A-Z]+-)',lambda m:'WORKFLOW' if m[0].isupper() else 'Workflow' if m[0][0].isupper() else 'workflow',t,flags=re.I)
    if rel=='AGENTS.md':
        t+='\n\n## Permanent Source-Direction Policy\n\nAutobiography is the authoritative source for Lost Limb Riders organizational\ndocumentation. Source direction is Autobiography → Official only. Corporate-document\nchanges must originate here, never in Official’s checkout. Official must refresh its\nsource checkout from Autobiography at the beginning of each new workday.\n\nUse workflow terminology for the organizational documentation layer. Preserve\nexisting technical paths, filenames, Document IDs, and legitimate references to\nactual financial or operational transactions.\n'
    if t!=s:
        backup=Path('scripts/workflow-terminology/workflow_before')/(rel+'.before');backup.parent.mkdir(parents=True,exist_ok=True);backup.write_text(s)
        p.write_text(t);changed.append(rel)
Path('scripts/workflow-terminology/workflow_changed.json').write_text(json.dumps(changed,indent=2))
print('\n'.join(changed))
