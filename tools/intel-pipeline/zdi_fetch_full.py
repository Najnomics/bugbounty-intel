import re,subprocess,json,os,time,html,sys,trafilatura,concurrent.futures as cf
def get(u):
    for a in range(4):
        p=subprocess.run(['curl','-s','-m','40','-A','Mozilla/5.0','-w','\n%{http_code}',u],capture_output=True)
        b,_,c=p.stdout.rpartition(b'\n')
        if c==b'200': return b.decode('utf-8','replace')
        time.sleep(5*(a+1))
    return None
rows=json.load(open('index.json')) if os.path.exists('index.json') else {}
for y in ([] if rows else range(2005,2027)):
    h=get(f'https://www.zerodayinitiative.com/advisories/published/{y}/')
    if not h: print('listfail',y,file=sys.stderr); continue
    for tr in re.findall(r'<tr class="advisory-row.*?</tr>',h,re.S):
        cells=[html.unescape(re.sub(r'<[^>]+>','',c)).strip() for c in re.findall(r'<td[^>]*data-label="[^"]*"[^>]*>(.*?)</td>',tr,re.S)]
        labels=re.findall(r'data-label="([^"]*)"',tr)
        d=dict(zip(labels,cells))
        m=re.search(r'ZDI-\d{2}-\d+',tr)
        if m: rows[m.group(0)]={'zdi':m.group(0),**d}
    print(y,len(rows),file=sys.stderr,flush=True)
if not os.path.exists('index.json'): json.dump(rows,open('index.json','w'))
def page(z):
    fn=f'pages/{z}.json'
    if os.path.exists(fn): return
    h=get(f'https://www.zerodayinitiative.com/advisories/{z}/')
    if not h: open('failed.txt','a').write(z+'\n'); return
    t=trafilatura.extract(h,include_tables=True,favor_recall=True) or ''
    m=re.search(r'<title>(.*?)</title>',h,re.S)
    json.dump({'zdi':z,'title':html.unescape(m.group(1).strip()) if m else '','text':t},open(fn,'w'))
    time.sleep(0.1)
with cf.ThreadPoolExecutor(6) as ex:
    for n,_ in enumerate(ex.map(page,sorted(rows,reverse=True))):
        if n%500==0: print('pages',n,time.strftime('%H:%M'),file=sys.stderr,flush=True)
print('DONE',file=sys.stderr)
