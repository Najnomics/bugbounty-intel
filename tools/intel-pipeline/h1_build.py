import json,os,re,collections,glob
R='/workspace/raw/h1/reports'; O='/workspace/bugbounty-intel'
idx={json.loads(l)['id']:json.loads(l) for l in open('/workspace/raw/h1/ids.jsonl')}
# existing telegram-H1 writeups
tg=set()
for f in glob.glob(O+'/writeups/telegram-dailybountywriteup/**/*',recursive=True):
    m=re.match(r'reports-(\d+)-',os.path.basename(f))
    if m: tg.add(m.group(1))
def clean(d):
    e={'id':d['id'],'url':d.get('url'),'title':d.get('title'),
       'program':(d.get('team') or {}).get('handle'),'program_name':((d.get('team') or {}).get('profile') or {}).get('name'),
       'state':d.get('state'),'substate':d.get('substate'),'severity_rating':d.get('severity_rating'),
       'severity':d.get('severity'),'weakness':d.get('weakness'),'asset':d.get('structured_scope'),
       'reporter':(d.get('reporter') or {}).get('username'),'bounty':(float(d['bounty_amount']) if str(d.get('bounty_amount') or '').replace('.','',1).isdigit() else d.get('bounty_amount')),'formatted_bounty':d.get('formatted_bounty'),'has_bounty':d.get('has_bounty?'),
       'created_at':d.get('created_at'),'submitted_at':d.get('submitted_at'),'disclosed_at':d.get('disclosed_at'),
       'cve_ids':d.get('cve_ids') or [],'visibility':d.get('visibility'),'vote_count':d.get('vote_count'),
       'vulnerability_information':d.get('vulnerability_information') or '',
       'summaries':[{'category':s.get('category'),'author':(s.get('user') or {}).get('username'),'content':s.get('content'),'updated_at':s.get('updated_at'),
                     'attachments':[{'file_name':a.get('file_name'),'type':a.get('type')} for a in s.get('attachments') or []]} for s in d.get('summaries') or []],
       'attachments':[{'file_name':a.get('file_name'),'type':a.get('type'),'size':a.get('file_size')} for a in d.get('attachments') or []],
       'original_report_id':d.get('original_report_id')}
    if (d.get('severity') or {}).get('metrics') is None and e['severity']: pass
    return e
recs=[]
for f in os.listdir(R):
    try: recs.append(clean(json.load(open(f'{R}/{f}'))))
    except Exception as ex: print('bad',f,ex)
recs.sort(key=lambda r:(r['disclosed_at'] or '',r['id']))
by=collections.defaultdict(list)
for r in recs: by[(r['disclosed_at'] or '0000')[:4]].append(r)
os.makedirs(O+'/data/h1',exist_ok=True)
for y,rs in by.items():
    # shard by half-year if big
    with open(f'{O}/data/h1/disclosed_{y}.jsonl','w') as w:
        for r in rs: w.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
def md(r):
    sev=r.get('severity') or {}
    L=[f"# H1 #{r['id']}: {r['title']}",'',
       f"- URL: {r['url']}",f"- Program: {r['program']} ({r.get('program_name') or ''})",f"- Reporter: {r['reporter']}",
       f"- Weakness: {(r.get('weakness') or {}).get('name')}",f"- Severity: {r.get('severity_rating')} (score {sev.get('score')}; metrics {json.dumps(sev.get('metrics'))})",
       f"- Bounty: {r.get('formatted_bounty') or ('yes' if r.get('has_bounty') else 'none/undisclosed')}",
       f"- Asset: {(r.get('asset') or {}).get('asset_type')} {(r.get('asset') or {}).get('asset_identifier')}",
       f"- State: {r['state']}/{r['substate']} | Submitted: {(r.get('submitted_at') or '')[:10]} | Disclosed: {(r.get('disclosed_at') or '')[:10]}",
       f"- CVE: {', '.join(r['cve_ids']) or '-'}"+(f" | Also in writeups/telegram-dailybountywriteup/" if str(r['id']) in tg else ''),'']
    for s in r['summaries']:
        if s.get('content'): L+= [f"## Summary ({s['category']}, by {s.get('author')})",'',s['content'],'']
    if r['vulnerability_information']: L+=['## Original report (vulnerability_information, verbatim)','',r['vulnerability_information'],'']
    elif not any(s.get('content') for s in r['summaries']): L+=['_Report body not public (H1 visibility: '+str(r.get('visibility'))+'); metadata only._','']
    if r['attachments']: L+=['Attachments: '+', '.join(a['file_name'] or '' for a in r['attachments'])]
    return '\n'.join(L)+'\n'
n=collections.Counter()
for r in recs:
    y=(r['disclosed_at'] or '0000')[:4]; p=f'{O}/hackerone/reports/{y}'; os.makedirs(p,exist_ok=True)
    open(f"{p}/{r['id']}.md",'w').write(md(r))
    n['body' if r['vulnerability_information'] else ('summary' if any(s.get('content') for s in r['summaries']) else 'meta')]+=1
# index by program and weakness
prog=collections.defaultdict(list); weak=collections.defaultdict(list)
for r in recs:
    prog[r['program']].append(r); weak[(r.get('weakness') or {}).get('name') or 'Unspecified'].append(r)
def line(r): return f"- [{r['id']}](reports/{(r['disclosed_at'] or '0000')[:4]}/{r['id']}.md) {r['title']} — {r['program']} — {r.get('severity_rating') or '-'} — {r.get('formatted_bounty') or ''} — {(r.get('weakness') or {}).get('name') or ''}"
with open(O+'/hackerone/BY_WEAKNESS.md','w') as f:
    f.write(f'# HackerOne disclosed reports by weakness ({len(recs)} reports)\n\n')
    for k,rs in sorted(weak.items(),key=lambda x:-len(x[1])):
        f.write(f'\n## {k} ({len(rs)})\n\n'+'\n'.join(line(r) for r in sorted(rs,key=lambda r:-(r.get('bounty') if isinstance(r.get('bounty'),float) else 0)))+'\n')
with open(O+'/hackerone/BY_PROGRAM.md','w') as f:
    f.write(f'# HackerOne disclosed reports by program ({len(prog)} programs)\n\n')
    for k,rs in sorted(prog.items(),key=lambda x:-len(x[1])):
        f.write(f'\n## {k} ({len(rs)})\n\n'+'\n'.join(line(r) for r in rs)+'\n')
top=sorted([r for r in recs if isinstance(r.get('bounty'),float)],key=lambda r:-r['bounty'])[:500]
with open(O+'/hackerone/TOP_BOUNTIES.md','w') as f:
    f.write('# Top 500 disclosed HackerOne reports by bounty\n\n'+'\n'.join(line(r) for r in top)+'\n')
json.dump({'reports':len(recs),'content':n,'in_telegram_writeups':len(tg & {str(r['id']) for r in recs}),'enumerated':len(idx)},open('/workspace/raw/h1/build_stats.json','w'))
print(len(recs),n)
