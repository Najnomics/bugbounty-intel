import json,os,glob,subprocess,datetime
TODAY=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime('%Y-%m-%d')+' (Africa/Lagos)'
O='/workspace/bugbounty-intel'; R='/workspace/raw'
def J(p,d=None):
    try: return json.load(open(p))
    except Exception: return d
def cnt(p): return sum(sum(1 for _ in open(f)) for f in glob.glob(p,recursive=True))
def maxf(p,k):
    m=''
    for f in glob.glob(p):
        for l in open(f):
            v=json.loads(l).get(k) or ''
            if v>m: m=v
    return m
kev=J(R+'/cve/kev.json',{})
kn=J(R+'/kvulns_stats.json',{}); nv=J(R+'/nvd/build_stats.json',{}); zd=J(R+'/zdi/build_stats.json',{})
edbh=subprocess.run(['git','-C',R+'/edb','log','-1','--format=%H %cI'],capture_output=True,text=True).stdout.split() or ['?','?']
p0=[x for x in sorted(os.listdir(O+'/cves/google-project-zero/blog')) if x!='0day.md']
st={'generated':TODAY,'note':'Markers for the daily incremental CVE run. See cves/README.md "Daily incremental procedure".',
 'sources':{
  'cvelistV5':{'status':'complete','records':cnt(O+'/data/cve/all/*/*.jsonl'),'years':'1999-2026','max_dateUpdated':maxf(O+'/data/cve/all/202[56]/*.jsonl','updated'),
     'source':'https://github.com/CVEProject/cvelistV5 (release zip)','incremental':'download https://github.com/CVEProject/cvelistV5/releases latest *_delta_CVEs_at_*.zip or the daily cumulative delta since max_dateUpdated; re-run tools/intel-pipeline/cve_build.py'},
  'nvd':{'status':'complete' if nv.get('records',0)>=424000 and nv.get('api_timestamp') else 'pending','records':nv.get('records'),'max_lastModified':nv.get('max_lastModified'),'api_timestamp':nv.get('api_timestamp'),
     'incremental':'GET https://services.nvd.nist.gov/rest/json/cves/2.0?lastModStartDate=<max_lastModified>&lastModEndDate=<now> (max 120-day window, 2000/page, sleep 6s), then tools/intel-pipeline/nvd_build.py'},
  'cisa_kev':{'status':'complete','catalogVersion':kev.get('catalogVersion'),'dateReleased':kev.get('dateReleased'),'count':kev.get('count'),'source':'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'},
  'ghsa':{'status':'complete','records':cnt(O+'/data/ghsa/*/*.jsonl'),'max_modified':maxf(O+'/data/ghsa/*/*.jsonl','modified'),'source':'https://github.com/github/advisory-database (reviewed)','incremental':'GitHub REST GET /advisories?type=reviewed&sort=updated&direction=desc until modified <= max_modified'},
  'osv_non_ghsa':{'status':'complete','records':cnt(O+'/data/osv/*/*.jsonl'),'max_modified':maxf(O+'/data/osv/*/*.jsonl','modified'),'source':'https://osv-vulnerabilities.storage.googleapis.com/<eco>/all.zip; skipped: GHSA dups, MAL- malicious-package records, GIT and Linux ecosystems (covered by cvelist/kernel CNA)','incremental':'per ecosystem modified_id.csv at https://osv-vulnerabilities.storage.googleapis.com/<eco>/modified_id.csv, entries newer than max_modified'},
  'exploitdb':{'status':'complete','records':cnt(O+'/data/exploitdb/**/*.jsonl'),'git_head':edbh[0],'git_date':edbh[1] if len(edbh)>1 else None,'source':'https://gitlab.com/exploit-database/exploitdb','incremental':'git -C /workspace/raw/edb pull; diff files_exploits.csv for new ids'},
  'linux_kernel_cna':{'status':'complete','records':kn.get('records'),'vulns_git_head':kn.get('vulns_git_head'),'vulns_git_date':kn.get('vulns_git_date'),'source':'https://git.kernel.org/pub/scm/linux/security/vulns.git','incremental':'git -C /workspace/raw/kvulns pull; re-run tools/intel-pipeline/kernel_cna_build.py'},
  'google_project_zero':{'status':'complete','blog_posts':len(p0),'last_post_file':'2026_11_disclosure-policy.md','source':'https://projectzero.google/ blog + 0day ITW sheet + 0days-in-the-wild RCAs'},
  'zdi':{'status':'complete' if zd.get('pages')==zd.get('index') else 'pending','advisories_indexed':zd.get('index'),'full_text_pages':zd.get('pages'),
     'cursor':'fetch https://www.zerodayinitiative.com/advisories/<ZDI-ID>/ for every id in data/zdi/*.jsonl whose "text" is null (status "page not yet fetched"); raw pages cached in /workspace/raw/zdi/pages; then re-run tools/intel-pipeline/zdi_build.py','incremental':'https://www.zerodayinitiative.com/advisories/published/<year>/ table'},
  'repo_advisories':{'status':'complete','php_src':cnt(O+'/data/repo-advisories/php__php-src.jsonl'),'electron':cnt(O+'/data/repo-advisories/electron__electron.jsonl'),'wordpress_develop':cnt(O+'/data/repo-advisories/WordPress__wordpress-develop.jsonl'),'incremental':'GitHub REST GET /repos/<owner>/<repo>/security-advisories?state=published'},
 }}
json.dump(st,open(O+'/data/cve_state.json','w'),indent=1)
ids=[json.loads(l) for l in open(R+'/h1/ids.jsonl')]
recs=cnt(O+'/data/h1/*.jsonl'); last=max(ids,key=lambda d:d.get('disclosed_at') or '')
bs=J(R+'/h1/build_stats.json',{})
h={'generated':TODAY,'status':'complete' if recs>=len(ids) else 'pending','enumerated':len(ids),'captured':recs,'content':bs.get('content'),
 'also_in_telegram_writeups':bs.get('in_telegram_writeups'),'failed_ids':[json.loads(l) for l in open(R+'/h1/failed.jsonl')] if os.path.exists(R+'/h1/failed.jsonl') else [],
 'last_disclosed_at':last.get('disclosed_at'),'last_disclosed_id':last['id'],'max_report_id':max(int(d['id']) for d in ids),
 'enumeration':'POST https://hackerone.com/graphql search(index: CompleteHacktivityReportIndex, query_string: "disclosed:true AND disclosed_at:[A TO B]", sort disclosed_at ASC, size 100) — one window per month (<10k results/window)',
 'fetch':'GET https://hackerone.com/reports/<id>.json (6 threads, 0.25s gap, 60s pause on 429)',
 'incremental':'enumerate disclosed_at:[<last_disclosed_at date> TO <today>], fetch ids not already in data/h1/*.jsonl, re-run tools/intel-pipeline/h1_build.py then h1_harness.py (h1_harness appends only findings whose post_url is new)'}
json.dump(h,open(O+'/data/h1_state.json','w'),indent=1)
print(json.dumps(st['sources']['nvd']),json.dumps(st['sources']['zdi']),h['status'],h['captured'])
