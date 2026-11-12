import json,os,collections,re
O='/workspace/bugbounty-intel'; idx=json.load(open('/workspace/raw/zdi/index.json'))
by=collections.defaultdict(list); got=0
for z,row in idx.items():
    fn=f'/workspace/raw/zdi/pages/{z}.json'
    r={'zdi':z,'can':row.get('ZDI CAN'),'vendor':row.get('Vendor / Product'),'cve':row.get('CVE'),'cvss':row.get('CVSS'),'published':row.get('Published'),'updated':row.get('Updated'),'url':f'https://www.zerodayinitiative.com/advisories/{z}/'}
    if os.path.exists(fn):
        p=json.load(open(fn)); r['title']=re.sub(r'\s*\|\s*Zero Day Initiative.*$','',p.get('title','')); r['text']=p.get('text',''); got+=1
    else: r['text']=None; r['status']='page not yet fetched'
    by['20'+z[4:6]].append(r)
os.makedirs(O+'/data/zdi',exist_ok=True); os.makedirs(O+'/cves/zdi',exist_ok=True)
for y,rs in by.items():
    rs.sort(key=lambda r:int(r['zdi'].split('-')[2]))
    with open(f'{O}/data/zdi/{y}.jsonl','w') as w:
        for r in rs: w.write(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n')
    with open(f'{O}/cves/zdi/{y}.md','w') as w:
        w.write(f'# ZDI published advisories {y} ({len(rs)}; {sum(1 for r in rs if r["text"])} with full text)\n\n')
        for r in rs:
            w.write(f"## {r['zdi']} — {r.get('title') or r['vendor']}\n- Vendor: {r['vendor']} | CVE: {r['cve'] or '-'} | CVSS: {r['cvss']} | Published: {r['published']} | {r['url']}\n\n{r['text'] if r['text'] else '_Full page not fetched yet (see data/cve_state.json zdi cursor)._'}\n\n")
json.dump({'index':len(idx),'pages':got},open('/workspace/raw/zdi/build_stats.json','w')); print(len(idx),got)
