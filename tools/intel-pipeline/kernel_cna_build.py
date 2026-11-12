# Build data/cve/linux-kernel-cna/<year>.jsonl from git.kernel.org/pub/scm/linux/security/vulns.git
import os,json,re,collections,subprocess,sys
V=sys.argv[1] if len(sys.argv)>1 else '/workspace/raw/kvulns'; O='/workspace/bugbounty-intel'
def rd(p):
    try: return open(p,encoding='utf-8',errors='replace').read()
    except FileNotFoundError: return None
by=collections.defaultdict(list)
for st in ('published','rejected'):
    base=f'{V}/cve/{st}'
    for y in sorted(os.listdir(base)):
        if not y.isdigit(): continue
        for f in sorted(os.listdir(f'{base}/{y}')):
            if not f.endswith('.sha1'): continue
            c=f[:-5]; p=f'{base}/{y}/{c}'
            mb=rd(p+'.mbox') or ''
            m=re.search(r'The file\(s\) affected by this issue are:\n(.*?)\n\n',mb,re.S)
            r={'cve':c,'status':st,'title':None,'message':rd(p+'.message'),
               'fix_commits':(rd(p+'.sha1') or '').split(),
               'vulnerable_commits':(rd(p+'.vulnerable') or '').split(),
               'dyad':[l for l in (rd(p+'.dyad') or '').splitlines() if l and not l.startswith('#')],
               'files':[l.strip() for l in m.group(1).splitlines()] if m else [],
               'url':f'https://git.kernel.org/pub/scm/linux/security/vulns.git/tree/cve/{st}/{y}/{c}.json'}
            if r['message']: r['title']=r['message'].splitlines()[0]
            by[y].append(r)
os.makedirs(O+'/data/cve/linux-kernel-cna',exist_ok=True); tot=0
for y,rs in by.items():
    rs.sort(key=lambda r:int(r['cve'].split('-')[2]))
    with open(f'{O}/data/cve/linux-kernel-cna/{y}.jsonl','w') as w:
        for r in rs: w.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
    tot+=len(rs)
head=subprocess.run(['git','-C',V,'log','-1','--format=%H %cI'],capture_output=True,text=True).stdout.split()
json.dump({'records':tot,'by_year':{y:len(v) for y,v in by.items()},'vulns_git_head':head[0],'vulns_git_date':head[1]},open('/workspace/raw/kvulns_stats.json','w'))
print(tot,{y:len(v) for y,v in sorted(by.items())})
