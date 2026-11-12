# Compact NVD enrichment layer: data/nvd/<year>.jsonl (NVD analysis: vulnStatus, CVSS v2/v3/v4 per source, CWE, CPE criteria, reference tags).
# Descriptions and CNA data are NOT duplicated here (they live in data/cve/all). Input: NVD API 2.0 pages from nvd_fetch.py.
import json,glob,os,collections
O='/workspace/bugbounty-intel'; R='/workspace/raw/nvd'
by=collections.defaultdict(list); lm=''; ts=''
for f in sorted(glob.glob(R+'/page_*.json')):
    d=json.load(open(f)); ts=max(ts,d.get('timestamp',''))
    for v in d['vulnerabilities']:
        c=v['cve']; lm=max(lm,c.get('lastModified',''))
        met=[]  # NVD Primary (NVD-analysed) metrics only; CNA/ADP metrics are in data/cve/all
        for k,arr in (c.get('metrics') or {}).items():
            if not k.startswith('cvss'): continue
            for m in arr:
                if m.get('type')!='Primary': continue
                cd=m.get('cvssData',{}); met.append({'v':cd.get('version'),'src':m.get('source'),'type':m.get('type'),'score':cd.get('baseScore'),'sev':cd.get('baseSeverity') or m.get('baseSeverity'),'vector':cd.get('vectorString')})
        cwe=sorted({x['value'] for w in c.get('weaknesses',[]) for x in w.get('description',[]) if x.get('value','').startswith('CWE-') or x.get('value','').startswith('NVD-CWE')})
        cpe=[]
        for cf in c.get('configurations',[]):
            for n in cf.get('nodes',[]):
                for m in n.get('cpeMatch',[]):
                    if m.get('vulnerable'):
                        s=m['criteria']; 
                        for k in ('versionStartIncluding','versionStartExcluding','versionEndIncluding','versionEndExcluding'):
                            if m.get(k): s+=f' {k}={m[k]}'
                        if s not in cpe: cpe.append(s)
        refs=[r['url'] for r in c.get('references',[]) if 'Exploit' in (r.get('tags') or [])]
        r={'id':c['id'],'published':c.get('published'),'lastModified':c.get('lastModified'),'vulnStatus':c.get('vulnStatus'),'metrics':met,'cwe':cwe,'cpe':cpe[:15],'cpe_total':len(cpe),'exploit_refs':refs}
        if c.get('cisaExploitAdd'): r['cisa']={k:c.get(k) for k in ('cisaExploitAdd','cisaActionDue','cisaVulnerabilityName')}
        by[c['id'].split('-')[1]].append(r)
os.makedirs(O+'/data/nvd',exist_ok=True)
import shutil; shutil.rmtree(O+'/data/nvd',ignore_errors=True); os.makedirs(O+'/data/nvd')
for y,rs in by.items():
    rs.sort(key=lambda r:int(r['id'].split('-')[2])); os.makedirs(f'{O}/data/nvd/{y}',exist_ok=True)
    for r in rs:
        b=int(r['id'].split('-')[2])//10000
        with open(f'{O}/data/nvd/{y}/CVE-{y}-{b}xxxx.jsonl','a') as w: w.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
st={'records':sum(map(len,by.values())),'max_lastModified':lm,'api_timestamp':ts,'pages':len(glob.glob(R+'/page_*.json'))}
json.dump(st,open(R+'/build_stats.json','w')); print(st)
