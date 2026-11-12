import json,glob,re,os,collections,sys
sys.path.insert(0,'/workspace/raw/cvebuild')
O='/workspace/bugbounty-intel'
src=open('/workspace/raw/cvebuild/cveindex.py').read()
CL=eval(src[src.index('CL={')+3:src.index('\n}\n')+2])
def cls(r):
    t=(((r.get('weakness') or {}).get('name') or '')+' '+(r.get('title') or '')).lower()
    for k,(cw,rx) in CL.items():
        if re.search(rx,t): return k
    return None
def snippets(body):
    out=re.findall(r'```[^\n]*\n(.*?)```',body,re.S)
    out+=re.findall(r'((?:^|\n)(?:GET|POST|PUT|PATCH|DELETE) /[^\n]* HTTP/[12](?:\.\d)?\n(?:[^\n]+\n){1,25}(?:\n[^\n]{1,800})?)',body)
    out+=[m for m in re.findall(r'(?m)^ {4}.+(?:\n {4}.+)*',body) if len(m)>40][:3]
    seen=[];
    for s in out:
        s=s.strip('\n')
        if 15<len(s) and s not in seen: seen.append(s[:1500])
    return seen
recs=[json.loads(l) for f in glob.glob(O+'/data/h1/*.jsonl') for l in open(f)]
def b(r): return r['bounty'] if isinstance(r.get('bounty'),float) else 0
by=collections.defaultdict(list)
for r in recs:
    if r.get('vulnerability_information'):
        k=cls(r)
        if k: by[k].append(r)
os.makedirs(O+'/harness/payloads',exist_ok=True)
pc=0; files=[]
for k,rs in by.items():
    rs.sort(key=lambda r:(-b(r),-(r.get('vote_count') or 0)))
    L=[f'# {k} — verbatim payloads/PoC snippets from disclosed HackerOne reports','',f'Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter\'s own text). Top reports by bounty, then votes. Full context: the linked report file.','']
    n=0
    for r in rs:
        sn=snippets(r['vulnerability_information'])
        if not sn: continue
        L.append(f"## #{r['id']} {r['title']} — {r['program']} — {r.get('formatted_bounty') or '-'} — {(r.get('weakness') or {}).get('name')}")
        L.append(f"Source: `hackerone/reports/{(r.get('disclosed_at') or '0000')[:4]}/{r['id']}.md` ({r['url']})\n")
        for s in sn[:3]: L.append('```\n'+s.replace('```',"'''")+'\n```\n'); pc+=1
        n+=1
        if n>=40: break
    if n:
        fn='h1-'+re.sub(r'[^a-z0-9]+','-',k.lower()).strip('-')+'.md'; files.append((fn,n))
        open(f'{O}/harness/payloads/{fn}','w').write('\n'.join(L)+'\n')
# findings
existing=set()
for l in open(O+'/harness/findings.jsonl'):
    try: existing.add(json.loads(l).get('post_url'))
    except: pass
new=[]
top=sorted([r for r in recs if r.get('vulnerability_information') or r.get('summaries')],key=lambda r:(-b(r),-(r.get('vote_count') or 0)))
for r in top:
    if r['url'] in existing: continue
    k=cls(r)
    if not k and b(r)<5000: continue
    body=r.get('vulnerability_information') or ''
    team=[s['content'] for s in r['summaries'] if s.get('category')=='team' and s.get('content')]
    rep=[s['content'] for s in r['summaries'] if s.get('category')=='researcher' and s.get('content')]
    steps=re.search(r'(?is)(steps to reproduce|reproduction steps|poc|proof of concept)[^\n]*\n(.{50,1200}?)(\n#+ |\Z)',body)
    sn=snippets(body)
    new.append({'researcher':r['reporter'],'marius':r['reporter']=='mdp_sec','platform':'HackerOne','bug_class':k or (r.get('weakness') or {}).get('name') or 'Unspecified',
      'target_type':((r.get('asset') or {}).get('asset_type') or 'unknown').lower(),'title':r['title'],
      'root_cause':(team[0] if team else body)[:1200],'discovery_method':(steps.group(2).strip() if steps else body[:600]),
      'takeaway':(rep[0][:800] if rep else (team[0][:400] if team else '')),'payload':(sn[0][:1200] if sn else ''),
      'bounty':r.get('formatted_bounty') or '','post_url':r['url'],'source_files':[f"hackerone/reports/{(r.get('disclosed_at') or '0000')[:4]}/{r['id']}.md"],
      'source':'hackerone-hacktivity','weakness':(r.get('weakness') or {}).get('name'),'severity':r.get('severity_rating'),'program':r['program'],'cve_ids':r.get('cve_ids')})
    if len(new)>=600: break
# KEV web/mobile/thick-client/crypto items 2023+ as findings
kevn=0
for f in sorted(glob.glob(O+'/data/cve/all/202[3-6]/*.jsonl')):
    for l in open(f):
        r=json.loads(l)
        if not r.get('kev'): continue
        url='https://www.cve.org/CVERecord?id='+r['id']
        if url in existing: continue
        txt=(r.get('title','')+' '+r['description']).lower(); k=None
        for kk,(cw,rx) in CL.items():
            cws={int(m) for c in r.get('cwe',[]) for m in re.findall(r'CWE-(\d+)',c)}
            if cws & set(cw) or re.search(rx,txt): k=kk; break
        new.append({'researcher':'; '.join(r.get('credits',[])[:3]) or 'unknown','marius':False,'platform':'CVE / CISA KEV','bug_class':k or '; '.join(r.get('cwe',[])) or 'Unspecified',
          'target_type':r['kev']['vendorProject']+' '+r['kev']['product'],'title':r['id']+' '+(r.get('title') or r['kev']['vulnerabilityName']),
          'root_cause':r['description'][:1200],'discovery_method':'Exploited in the wild (CISA KEV, added '+r['kev']['dateAdded']+')','takeaway':r['kev']['shortDescription'][:600],
          'payload':(r['exploitdb'][0]['title'] if r.get('exploitdb') else ''),'bounty':'','post_url':url,'source_files':[f"data/cve/all/{r['id'].split('-')[1]}/","cves/kev/"+r['kev']['dateAdded'][:4]+".md"],
          'source':'cvelistV5+cisa-kev','cve_ids':[r['id']]}); kevn+=1
with open(O+'/harness/findings.jsonl','a') as w:
    for x in new: w.write(json.dumps(x,ensure_ascii=False)+'\n')
print('payload snippets',pc,'files',files,'findings added',len(new),'kev',kevn)
