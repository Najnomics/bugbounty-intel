import zipfile,json,csv,re,os,sys,collections
R='/workspace/raw/cve'; OUT='/workspace/bugbounty-intel'
csv.field_size_limit(10**9)
kev={v['cveID']:v for v in json.load(open(R+'/kev.json'))['vulnerabilities']}
edb=collections.defaultdict(list)
for row in csv.DictReader(open(R+'/edb.csv',encoding='utf-8',errors='replace')):
    for c in (row.get('codes') or '').split(';'):
        c=c.strip()
        if c.startswith('CVE-'): edb[c].append({'edb':row['id'],'title':row['description'],'type':row['type'],'platform':row['platform'],'date':row['date_published'],'verified':row['verified']})
# vendor rules: (tag, assigner set, regex on vendor/product text)
RULES=[
 ('google-chrome',{'Chrome'},r'\bchrom(e|ium)\b'),
 ('android',{'google_android'},r'^android\b|\bandroid\s*(os|kernel)?$'),
 ('google',{'Google','GoogleCloud','google_devices'},r'^google\b'),
 ('linux-kernel',{'Linux'},r'^linux( kernel)?$'),
 ('php',set(),r'^php( group)?$|php-src|\bphp\s*(interpreter)?$'),
 ('apple',{'apple'},r'^apple\b'),
 ('microsoft',{'microsoft'},r'^microsoft\b'),
 ('mozilla',{'mozilla'},r'^mozilla\b|firefox|thunderbird'),
 ('openssl',{'openssl'},r'^openssl'),
 ('nodejs',{'hackerone'},r'^node(\.?js)?$|^nodejs'),
 ('python',{'PSF'},r'^python( software foundation)?$|cpython'),
 ('golang',{'Go'},r'^go(lang)?$|golang'),
 ('apache',{'apache'},r'^apache\b'),
 ('nginx',{'F5'},r'nginx'),
 ('wordpress',{'Wordfence','Patchstack','WPScan'},r'^wordpress$'),
 ('jenkins',{'jenkins'},r'^jenkins'),
 ('gitlab',{'GitLab'},r'^gitlab'),
 ('kubernetes',{'kubernetes'},r'kubernetes'),
 ('oracle-java',{'oracle'},r'^oracle\b|java se|openjdk'),
 ('cisco',{'cisco'},r'^cisco'),
 ('fortinet',{'fortinet'},r'^fortinet'),
 ('ivanti',{'ivanti'},r'^ivanti|pulse secure'),
 ('atlassian',{'atlassian'},r'^atlassian'),
 ('vmware',{'vmware'},r'^vmware|broadcom vmware'),
 ('citrix',{'Citrix'},r'^citrix'),
 ('paloalto',{'palo_alto'},r'^palo alto'),
 ('sap',{'sap'},r'^sap\b'),
 ('samsung-mobile',{'Samsung Mobile'},r'^samsung'),
 ('qualcomm',{'qualcomm'},r'^qualcomm'),
 ('intel',{'intel'},r'^intel\b'),
 ('amd',{'AMD'},r'^amd\b'),
 ('arm',{'Arm'},r'^arm\b|trusted firmware|op-tee'),
 ('electron',set(),r'^electron$'),
 ('curl',{'curl'},r'^curl$|libcurl'),
 ('openssh',set(),r'^openssh'),
 ('github',set(),r'^github enterprise'),
 ('crypto-libs',set(),r'^(gnutls|libgcrypt|wolfssl|mbed ?tls|boringssl|libressl|libsodium|bouncy ?castle|nss)$'),
]
CR=[(t,a,re.compile(r,re.I)) for t,a,r in RULES]
DESC=[('php',r'\bPHP (before|through|[0-9])|\bin PHP\b|php-src'),('openssl',r'\bOpenSSL\b'),('curl',r'\b(lib)?curl\b'),('nginx',r'\bnginx\b'),('openssh',r'\bOpenSSH\b'),
 ('linux-kernel',r'\bLinux kernel\b'),('android',r'\bAndroid\b'),('google-chrome',r'Google Chrome|\bChromium\b'),('mozilla',r'\bFirefox\b|Thunderbird|\bMozilla\b'),
 ('apple',r'\bApple (iOS|macOS|Safari|tvOS|watchOS)|\biOS before|\bmacOS\b|\bSafari before'),('microsoft',r'\bMicrosoft\b|Internet Explorer|\bWindows\b'),('python',r'\bCPython\b|\bPython (before|[23]\.)'),
 ('nodejs',r'\bNode\.js\b'),('golang',r'\bGo before [0-9]|\bGolang\b'),('wordpress',r'\bWordPress\b'),('jenkins',r'\bJenkins\b'),('gitlab',r'\bGitLab\b'),('oracle-java',r'\bOracle\b|Java SE'),
 ('cisco',r'\bCisco\b'),('fortinet',r'\bFortinet\b|FortiOS'),('apache',r'\bApache\b'),('kubernetes',r'\bKubernetes\b'),('crypto-libs',r'\b(GnuTLS|libgcrypt|wolfSSL|mbed ?TLS|BoringSSL|LibreSSL|libsodium|Bouncy ?Castle)\b')]
DESCR=[(t,re.compile(r)) for t,r in DESC]
def tags(asg,aff,desc=''):
    s=_tags(asg,aff)
    if not aff or all(str(a.get('vendor','n/a')).lower() in ('n/a','','unknown') for a in aff):
        for t,rx in DESCR:
            if rx.search(desc[:400]): s=sorted(set(s)|{t})
    return s
def _tags(asg,aff):
    s=set()
    prods=[(str(a.get('vendor') or ''),str(a.get('product') or ''),str(a.get('packageName') or '')) for a in aff]
    for t,A,rx in CR:
        if asg in A and t not in ('nodejs','nginx'): s.add(t); continue
        for p in prods:
            v,pr,pk=p
            if rx.search(v) or rx.search(pr) or rx.search(pk): s.add(t); break
    if asg=='hackerone' and any(re.search(r'node',' '.join(p),re.I) for p in prods): s.add('nodejs')
    if asg=='F5' and any('nginx' in ' '.join(p).lower() for p in prods): s.add('nginx')
    if 'android' in s and 'google' in s and asg=='google_android': s.discard('google')
    if asg in ('Wordfence','Patchstack','WPScan'): s.add('wordpress')
    return sorted(s)
def ver(v):
    s=v.get('status','')+' '+str(v.get('version',''))
    if 'lessThan' in v: s+=' <'+str(v['lessThan'])
    if 'lessThanOrEqual' in v: s+=' <='+str(v['lessThanOrEqual'])
    if v.get('versionType'): s+=' ('+v['versionType']+')'
    if v.get('changes'): s+=' changes:'+';'.join(c.get('status','')+'@'+str(c.get('at','')) for c in v['changes'])
    return s
def metrics(ms,src,out):
    for m in ms or []:
        for k,v in m.items():
            if k.startswith('cvss') and isinstance(v,dict):
                out.append({'src':src,'v':v.get('version'),'score':v.get('baseScore'),'sev':v.get('baseSeverity'),'vector':v.get('vectorString')})
            elif k=='other' and isinstance(v,dict):
                c=v.get('content') or {}
                if v.get('type')=='ssvc': out.append({'src':src,'ssvc':{list(o)[0]:list(o.values())[0] for o in c.get('options',[])}})
                elif v.get('type')=='kev': pass
                else: out.append({'src':src,'other':v.get('type'),'content':json.dumps(c)[:500]})
def conv(d):
    md=d['cveMetadata']; c=d.get('containers',{}); cna=c.get('cna',{}); cid=md['cveId']
    r={'id':cid,'state':md.get('state'),'assigner':md.get('assignerShortName'),'published':md.get('datePublished'),'updated':md.get('dateUpdated')}
    if md.get('state')=='REJECTED':
        r['rejected']=' '.join(x.get('value','') for x in cna.get('rejectedReasons',[])); return r
    if cna.get('title'): r['title']=cna['title']
    ds=[x['value'] for x in cna.get('descriptions',[]) if x.get('lang','').startswith('en')] or [x['value'] for x in cna.get('descriptions',[])]
    r['description']='\n\n'.join(ds)
    cwe=[]; refs=[]; ms=[]; seen=set(); aff=[]
    for cont,src in [(cna,'cna')]+[(a,(a.get('providerMetadata') or {}).get('shortName','adp')) for a in c.get('adp',[])]:
        for pt in cont.get('problemTypes',[]):
            for de in pt.get('descriptions',[]):
                x=(de.get('cweId') or '')+' '+(de.get('description') or '')
                if x.strip() and x not in cwe: cwe.append(x.strip())
        for rf in cont.get('references',[]):
            u=rf.get('url')
            if u and u not in seen: seen.add(u); refs.append({'url':u,**({'tags':rf['tags']} if rf.get('tags') else {}),**({'name':rf['name']} if rf.get('name') and rf.get('name')!=u else {})})
        metrics(cont.get('metrics'),src,ms)
        for a in cont.get('affected',[]):
            e={k:a[k] for k in ('vendor','product','packageName','collectionURL','repo','defaultStatus','cpes','modules','programFiles','platforms') if a.get(k)}
            if a.get('versions'): e['versions']=[ver(v) for v in a['versions']]
            if e and (src=='cna' or e not in aff): aff.append(e)
    r['cwe']=cwe; r['metrics']=ms; r['affected']=aff; r['references']=refs
    for k in ('exploits','solutions','workarounds','configurations'):
        v=[x.get('value') for x in cna.get(k,[]) if x.get('value')]
        if v: r[k]=v
    cr=[x.get('value') for x in cna.get('credits',[]) if x.get('value')]
    if cr: r['credits']=cr
    if cid in kev: r['kev']={k:kev[cid].get(k) for k in ('vendorProject','product','vulnerabilityName','dateAdded','shortDescription','requiredAction','dueDate','knownRansomwareCampaignUse','notes','cwes')}
    if cid in edb: r['exploitdb']=edb[cid]
    nv=NVD.get(cid)
    if nv:
        r['metrics']+=nv['metrics']
        for x in nv['cwe']:
            if not any(x in y for y in r['cwe']): r['cwe'].append(x+' (NVD)')
        r['nvd']={k:nv[k] for k in ('status','lastModified','cpe','cisa') if nv.get(k)}
    r['vendors']=tags(r['assigner'],aff,r.get('description',''))
    return r
def maxscore(r):
    s=[m['score'] for m in r.get('metrics',[]) if m.get('score') is not None]
    return max(s) if s else None
def exploited(r):
    if r.get('kev') or r.get('exploitdb'): return True
    for m in r.get('metrics',[]):
        e=(m.get('ssvc') or {}).get('Exploitation')
        if e and e.lower() in ('active','poc'): return True
    return False
def md(r):
    L=[f"### {r['id']}" + (f" — {r['title']}" if r.get('title') else '')]
    ms=maxscore(r)
    L.append(f"- Assigner: {r['assigner']} | Published: {(r.get('published') or '')[:10]} | Updated: {(r.get('updated') or '')[:10]} | Max CVSS: {ms}")
    if r.get('cwe'): L.append('- CWE: '+'; '.join(r['cwe']))
    for m in r['metrics']:
        if m.get('vector'): L.append(f"- CVSS {m['v']} ({m['src']}): {m['score']} {m['sev']} `{m['vector']}`")
        elif m.get('ssvc'): L.append(f"- SSVC ({m['src']}): "+', '.join(f'{k}={v}' for k,v in m['ssvc'].items()))
    if r.get('kev'): k=r['kev']; L.append(f"- **CISA KEV**: added {k['dateAdded']}, ransomware={k['knownRansomwareCampaignUse']} — {k['vulnerabilityName']}")
    for e in r.get('exploitdb',[]): L.append(f"- Exploit-DB {e['edb']}: {e['title']} ({e['type']}/{e['platform']}, {e['date']}, verified={e['verified']})")
    L.append(''); L.append(r.get('description',''))
    for k in ('exploits','workarounds','solutions'):
        for v in r.get(k,[]): L.append(f"\n**{k}:** {v}")
    if r.get('affected'):
        L.append('\nAffected:')
        for a in r['affected'][:20]:
            vs=a.get('versions',[]); L.append(f"- {a.get('vendor','')} / {a.get('product') or a.get('packageName','')}: "+'; '.join(vs[:15])+(f' …(+{len(vs)-15} more in JSONL)' if len(vs)>15 else '')+(f" files: {', '.join(a['programFiles'][:5])}" if a.get('programFiles') else ''))
    if r.get('credits'): L.append('\nCredits: '+'; '.join(r['credits'][:10]))
    L.append('\nReferences:'); L+= ['- '+x['url']+(' ['+','.join(x['tags'])+']' if x.get('tags') else '') for x in r['references'][:40]]
    if len(r['references'])>40: L.append(f'- …(+{len(r["references"])-40} more in JSONL)')
    return '\n'.join(L)+'\n'
import glob as _g
NVD={}
for fn in sorted(_g.glob('/workspace/raw/nvd/page_*.json')):
    for v in json.load(open(fn)).get('vulnerabilities',[]):
        c=v['cve']; e={'status':c.get('vulnStatus'),'lastModified':c.get('lastModified')}
        ms=[]
        for k,arr in (c.get('metrics') or {}).items():
            for m in arr:
                d=m.get('cvssData',{}); ms.append({'src':'nvd:'+m.get('source','')+':'+m.get('type',''),'v':d.get('version'),'score':d.get('baseScore'),'sev':d.get('baseSeverity') or m.get('baseSeverity'),'vector':d.get('vectorString')})
        e['metrics']=ms
        e['cwe']=sorted({x['value'] for w in c.get('weaknesses',[]) for x in w.get('description',[]) if x.get('value','').startswith('CWE-')})
        cp=[]
        for cf in c.get('configurations',[]):
            for nd in cf.get('nodes',[]):
                for m in nd.get('cpeMatch',[]):
                    if m.get('vulnerable'):
                        x=m['criteria']
                        for k2 in ('versionStartIncluding','versionStartExcluding','versionEndIncluding','versionEndExcluding'):
                            if m.get(k2): x+=f' {k2}={m[k2]}'
                        cp.append(x)
        e['cpe']=cp[:60]+([f'...(+{len(cp)-60} more)'] if len(cp)>60 else [])
        if c.get('cisaExploitAdd'): e['cisa']={'added':c.get('cisaExploitAdd'),'action':c.get('cisaRequiredAction'),'name':c.get('cisaVulnerabilityName')}
        NVD[c['id']]=e
print('nvd',len(NVD),file=sys.stderr)
z=zipfile.ZipFile(R+'/cves.zip')
allb=collections.defaultdict(list); vend=collections.defaultdict(list); stats=collections.Counter()
for n in z.namelist():
    if not n.endswith('.json') or '/CVE-' not in n: continue
    try: r=conv(json.load(z.open(n)))
    except Exception as e: stats['err']+=1; print('ERR',n,e,file=sys.stderr); continue
    y=r['id'].split('-')[1]; num=int(r['id'].split('-')[2]); stats[r['state']]+=1
    allb[(y,num//10000)].append(r)
    for v in r.get('vendors',[]): vend[(v,y)].append(r)
def key(r): return (int(r['id'].split('-')[1]),int(r['id'].split('-')[2]))
for (y,b),rs in allb.items():
    p=f'{OUT}/data/cve/all/{y}'; os.makedirs(p,exist_ok=True)
    rs.sort(key=key)
    with open(f'{p}/CVE-{y}-{b}xxxx.jsonl','w') as f:
        for r in rs: f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
vstat=collections.defaultdict(lambda: collections.Counter())
for (v,y),rs in vend.items():
    rs.sort(key=key)
    p=f'{OUT}/data/cve/vendors/{v}'; os.makedirs(p,exist_ok=True)
    with open(f'{p}/{y}.jsonl','w') as f:
        for r in rs: f.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
    hv=[r for r in rs if r['state']=='PUBLISHED' and (exploited(r) or (maxscore(r) or 0)>=7.0 or (v in ('linux-kernel',) and False))]
    if v=='wordpress': hv=[r for r in rs if r['state']=='PUBLISHED' and (exploited(r) or (maxscore(r) or 0)>=9.0)]
    vstat[v]['total']+=len(rs); vstat[v]['md']+=len(hv)
    if hv:
        p=f'{OUT}/cves/vendors/{v}'; os.makedirs(p,exist_ok=True)
        with open(f'{p}/{y}.md','w') as f:
            f.write(f'# {v} — {y} high-value CVEs (CVSS>={"9" if v=="wordpress" else "7"}, CISA KEV, Exploit-DB, or SSVC exploitation active/poc)\n\nFull records for all {len(rs)} {v} CVEs of {y} are in `data/cve/vendors/{v}/{y}.jsonl`.\n\n')
            for r in hv: f.write(md(r)+'\n')
# KEV markdown
kv=collections.defaultdict(list)
for (y,b),rs in allb.items():
    for r in rs:
        if r.get('kev'): kv[r['kev']['dateAdded'][:4]].append(r)
os.makedirs(f'{OUT}/cves/kev',exist_ok=True)
for y,rs in kv.items():
    rs.sort(key=lambda r:r['kev']['dateAdded'])
    with open(f'{OUT}/cves/kev/{y}.md','w') as f:
        f.write(f'# CISA Known Exploited Vulnerabilities added in {y} ({len(rs)})\n\n')
        for r in rs:
            k=r['kev']; f.write(md(r)+f"\nKEV short description: {k['shortDescription']}\nRequired action: {k['requiredAction']}\nNotes: {k['notes']}\n\n")
json.dump({'stats':stats,'vendors':vstat,'kev_in_cvelist':sum(len(v) for v in kv.values()),'kev_total':len(kev),'edb_cves':len(edb)},open('/workspace/raw/cvebuild/stats.json','w'),indent=1)
print(stats, {v:dict(c) for v,c in vstat.items()})
