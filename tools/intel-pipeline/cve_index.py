import json,glob,re,collections,os
O='/workspace/bugbounty-intel'
CL={
 'XSS':([79,80,83,87],r'cross.site scripting|xss'),
 'SQL injection':([89,564],r'sql injection'),
 'SSRF':([918],r'server.side request forgery|ssrf'),
 'OS command / code injection (RCE)':([77,78,94,95,917],r'command injection|code injection|remote code execution|\brce\b'),
 'Insecure deserialization':([502],r'deserializ'),
 'Path traversal / LFI':([22,23,35,73,98],r'path traversal|directory traversal|local file inclusion|\blfi\b'),
 'XXE':([611,776],r'\bxxe\b|xml external entit'),
 'Authentication bypass':([287,288,290,294,306,1390,620,640],r'authentication bypass|improper authentication|auth bypass'),
 'IDOR / broken access control':([639,284,285,862,863,566,425],r'idor|insecure direct object|improper access control|authorization bypass|missing authorization'),
 'CSRF':([352],r'csrf|cross.site request forgery'),
 'Open redirect':([601],r'open redirect'),
 'Unrestricted file upload':([434],r'file upload'),
 'SSTI':([1336],r'template injection|ssti'),
 'Prototype pollution':([1321],r'prototype pollution'),
 'HTTP request smuggling / response splitting':([444,113,93],r'request smuggling|response splitting|crlf'),
 'Web cache poisoning / deception':([524,349],r'cache poison|cache decept'),
 'JWT / signature verification':([347],r'\bjwt\b|json web token|signature verification'),
 'OAuth / SSO':([],r'\boauth\b|\bsaml\b|\bopenid\b|\bsso\b'),
 'Race condition / TOCTOU':([362,367],r'race condition|toctou'),
 'Use-after-free':([416],r'use.after.free'),
 'Buffer overflow / OOB write':([787,119,120,121,122,125],r'buffer overflow|out.of.bounds (write|read)|heap overflow'),
 'Type confusion':([843],r'type confusion'),
 'Integer overflow':([190,191],r'integer overflow|integer underflow'),
 'Cryptographic weakness':([327,326,328,330,338,295,354,203,208,385,1240,325,780],r'cryptograph|timing side|weak (cipher|hash|random)|nonce reuse|padding oracle|certificate validation'),
 'Information disclosure':([200,209,532,538],r'information disclosure|information exposure|sensitive data exposure'),
 'Privilege escalation (local/kernel)':([269,250,268,266],r'privilege escalation|elevation of privilege'),
 'Subdomain takeover':([],r'subdomain takeover'),
 'Business logic':([840,841],r'business logic'),
 'TEE / enclave (SGX, TDX, SEV, TrustZone)':([],r'\bsgx\b|\btdx\b|\bsev(-snp)?\b|trustzone|enclave|\btee\b|op-tee'),
 'Smart contract / blockchain':([],r'smart contract|solidity|ethereum|blockchain|\bdefi\b|\bevm\b|solana|zcash'),
 'LLM / prompt injection':([1427],r'prompt injection|\bllm\b'),
}
def cwes(r): return {int(m) for c in r.get('cwe',[]) for m in re.findall(r'CWE-(\d+)',c)}
def maxs(r):
    s=[m['score'] for m in r.get('metrics',[]) if m.get('score') is not None]; return max(s) if s else 0
kev=collections.defaultdict(list); edbw=collections.defaultdict(list); hi=collections.defaultdict(list)
for f in glob.glob(O+'/data/cve/all/*/*.jsonl'):
    for l in open(f):
        r=json.loads(l)
        if r['state']!='PUBLISHED': continue
        c=cwes(r); txt=(r.get('title','')+' '+r.get('description','')[:300]).lower()
        for k,(cw,rx) in CL.items():
            if (c & set(cw)) or (not c and re.search(rx,txt)) or (k in ('TEE / enclave (SGX, TDX, SEV, TrustZone)','Smart contract / blockchain','OAuth / SSO','JWT / signature verification','Web cache poisoning / deception') and re.search(rx,txt)):
                if r.get('kev'): kev[k].append(r)
                elif any(e.get('verified')=='1' for e in r.get('exploitdb',[])): edbw[k].append(r)
                elif maxs(r)>=8.0: hi[k].append(r)
gh=collections.defaultdict(list)
for f in glob.glob(O+'/data/ghsa/*/*.jsonl'):
    eco=f.split('/')[-2]
    for l in open(f):
        d=json.loads(l); ds=d.get('database_specific') or {}
        if ds.get('severity')!='CRITICAL': continue
        c={int(x.split('-')[1]) for x in ds.get('cwe_ids',[]) if x.startswith('CWE-')}; txt=(d.get('summary','')).lower()
        for k,(cw,rx) in CL.items():
            if (c & set(cw)) or re.search(rx,txt): gh[k].append((eco,d))
h1=collections.defaultdict(list)
for f in glob.glob(O+'/data/h1/*.jsonl'):
    for l in open(f):
        r=json.loads(l); w=((r.get('weakness') or {}).get('name') or '').lower(); txt=w+' '+(r.get('title') or '').lower()
        for k,(cw,rx) in CL.items():
            if re.search(rx,txt): h1[k].append(r)
rca=collections.defaultdict(list)
for f in glob.glob(O+'/cves/google-project-zero/0day-RCAs/**/*.md',recursive=True):
    t=open(f,errors='ignore').read(4000).lower()
    for k,(cw,rx) in CL.items():
        if re.search(rx,t): rca[k].append(os.path.relpath(f,O))
L=['# Bug class → strongest public CVE / H1 / Project Zero examples','','Auto-built 2026-11-12 from `data/cve/all` (cvelistV5 + CISA KEV + Exploit-DB joins), `data/ghsa`, `data/h1`, `cves/google-project-zero`. Each line points at a full verbatim record inside this repo. Classification is by CWE where present, else by keyword in title/description, so expect some noise.','']
def bty(r): return r['bounty'] if isinstance(r.get('bounty'),float) else 0
for k in CL:
    L.append(f'## {k}'); L.append(f'CWEs: {", ".join("CWE-"+str(c) for c in CL[k][0]) or "(keyword-based)"}'); L.append('')
    ks=sorted(kev[k],key=lambda r:r['kev']['dateAdded'],reverse=True)[:12]
    if ks: L.append(f'**CISA KEV (exploited in the wild), {len(kev[k])} total — newest:**'); L+= [f"- {r['id']} ({r['kev']['vendorProject']} {r['kev']['product']}, KEV {r['kev']['dateAdded']}, CVSS {maxs(r)}): {r.get('description','')[:180].replace(chr(10),' ')} → `data/cve/all/{r['id'].split('-')[1]}/`" for r in ks]; L.append('')
    es=sorted(edbw[k],key=lambda r:r.get('published') or '',reverse=True)[:8]
    if es: L.append(f'**Verified Exploit-DB PoC (not KEV), {len(edbw[k])} total — newest:**'); L+= [f"- {r['id']} EDB-{r['exploitdb'][0]['edb']} {r['exploitdb'][0]['title'][:120]} → `data/exploitdb/{r['exploitdb'][0]['type']}/{r['exploitdb'][0]['date'][:4]}.jsonl`" for r in es]; L.append('')
    if len(kev[k])<10 and hi[k]:
        hs2=sorted(hi[k],key=lambda r:r.get('published') or '',reverse=True)[:10]
        L.append(f'**Other CVSS>=8 CVEs, {len(hi[k])} total — newest:**'); L+= [f"- {r['id']} ({r['assigner']}, CVSS {maxs(r)}): {(r.get('title') or r.get('description',''))[:160].replace(chr(10),' ')} → `data/cve/all/{r['id'].split('-')[1]}/`" for r in hs2]; L.append('')
    gs=sorted(gh[k],key=lambda x:x[1].get('published',''),reverse=True)[:8]
    if gs: L.append(f'**GHSA CRITICAL, {len(gh[k])} total — newest:**'); L+= [f"- {d['id']} ({eco}) {d.get('summary','')[:140]} → `cves/ghsa/{eco}/{d.get('published','')[:4]}.md`" for eco,d in gs]; L.append('')
    hs=sorted(h1[k],key=lambda r:(-bty(r),-(r.get('vote_count') or 0)))[:12]
    if hs: L.append(f'**HackerOne disclosed, {len(h1[k])} total — top by bounty:**'); L+= [f"- #{r['id']} {r['title'][:120]} — {r['program']} — {r.get('formatted_bounty') or '-'} → `hackerone/reports/{(r.get('disclosed_at') or '0000')[:4]}/{r['id']}.md`" for r in hs]; L.append('')
    if rca[k]: L.append(f'**Project Zero 0-day RCAs ({len(rca[k])}):** '+', '.join(f'`{p}`' for p in rca[k][:10])); L.append('')
open(O+'/harness/cve-index.md','w').write('\n'.join(L)+'\n')
print({k:(len(kev[k]),len(edbw[k]),len(gh[k]),len(h1[k]),len(rca[k])) for k in CL})
