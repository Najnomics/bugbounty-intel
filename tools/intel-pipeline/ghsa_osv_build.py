import json,os,glob,zipfile,collections,re
OUT='/workspace/bugbounty-intel'
def sev(d):
    s=(d.get('database_specific') or {}).get('severity')
    return s
def md(d):
    L=[f"### {d['id']} — {d.get('summary','')}"]
    L.append(f"- Aliases: {', '.join(d.get('aliases',[]))} | Published: {d.get('published','')[:10]} | Modified: {d.get('modified','')[:10]} | Severity: {sev(d)}")
    ds=d.get('database_specific') or {}
    if ds.get('cwe_ids'): L.append('- CWE: '+', '.join(ds['cwe_ids']))
    for s in d.get('severity',[]): L.append(f"- {s['type']}: `{s['score']}`")
    for a in d.get('affected',[]):
        p=a.get('package',{}); rs=[]
        for r in a.get('ranges',[]):
            rs.append(' '.join(f"{k}:{v}" for e in r.get('events',[]) for k,v in e.items()))
        L.append(f"- Affected {p.get('ecosystem')}/{p.get('name')}: {' | '.join(rs)}"+(f" versions: {', '.join(a['versions'][:20])}" if a.get('versions') else ''))
    L.append(''); L.append(d.get('details',''))
    L.append('\nReferences:'); L+=['- '+r.get('url','')+f" [{r.get('type','')}]" for r in d.get('references',[])[:40]]
    if d.get('credits'): L.append('\nCredits: '+'; '.join(c.get('name','') for c in d['credits']))
    return '\n'.join(L)+'\n'
def w(base,groups,mdbase=None,mdpred=None,title=''):
    st=collections.Counter()
    for (eco,y),rs in groups.items():
        rs.sort(key=lambda d:d.get('published',''))
        p=f'{OUT}/{base}/{eco}'; os.makedirs(p,exist_ok=True)
        with open(f'{p}/{y}.jsonl','w') as f:
            for d in rs: f.write(json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n')
        st[eco]+=len(rs)
        if mdbase:
            hv=[d for d in rs if mdpred(d)]
            if hv:
                p=f'{OUT}/{mdbase}/{eco}'; os.makedirs(p,exist_ok=True)
                with open(f'{p}/{y}.md','w') as f:
                    f.write(f'# {title} — {eco} {y} ({len(hv)} shown; all {len(rs)} in `{base}/{eco}/{y}.jsonl`)\n\n')
                    for d in hv: f.write(md(d)+'\n')
    return st
def safe(e): return re.sub(r'[^A-Za-z0-9._-]','_',e)
# GHSA reviewed
g=collections.defaultdict(list); ghsa_ids=set()
for fn in glob.glob('/workspace/raw/cve/ghsa/advisories/github-reviewed/*/*/*/*.json'):
    d=json.load(open(fn)); ghsa_ids.add(d['id'])
    ecos=sorted({a.get('package',{}).get('ecosystem','none') for a in d.get('affected',[])}) or ['none']
    g[(safe(ecos[0]),d.get('published','0000')[:4])].append(d)
gs=w('data/ghsa',g,'cves/ghsa',lambda d:sev(d) in ('HIGH','CRITICAL'),'GitHub-reviewed advisories, HIGH/CRITICAL')
# OSV non-GHSA, non-MAL
o=collections.defaultdict(list); skipped=collections.Counter()
for zf in glob.glob('/workspace/raw/osv/*.zip'):
    eco=os.path.basename(zf)[:-4]
    if eco in ('GIT','Linux'): skipped[eco]=len(zipfile.ZipFile(zf).namelist()); continue
    z=zipfile.ZipFile(zf)
    for n in z.namelist():
        if n.startswith('GHSA-') : skipped[eco+':GHSA-dup']+=1; continue
        if n.startswith('MAL-'): skipped[eco+':MAL']+=1; continue
        d=json.load(z.open(n)); o[(safe(eco),d.get('published','0000')[:4])].append(d)
os_=w('data/osv',o,'cves/osv',lambda d:True,'OSV advisories (non-GHSA)')
json.dump({'ghsa':gs,'ghsa_total':len(ghsa_ids),'osv':os_,'osv_skipped':skipped},open('/workspace/raw/cvebuild/advis_stats.json','w'),indent=1)
print(sum(gs.values()),dict(os_),dict(skipped))
