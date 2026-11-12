import json,subprocess,time,os,sys
start=0; tot=None
while tot is None or start<tot:
    fn=f'page_{start:07d}.json'
    if os.path.exists(fn) and os.path.getsize(fn)>1000:
        d=json.load(open(fn)); tot=d['totalResults']; start+=2000; continue
    for a in range(8):
        p=subprocess.run(['curl','-s','-m','120','-w','\n%{http_code}',f'https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=2000&startIndex={start}'],capture_output=True)
        b,_,c=p.stdout.rpartition(b'\n')
        if c==b'200':
            try: d=json.loads(b); break
            except Exception: pass
        print('retry',start,c,file=sys.stderr,flush=True); time.sleep(15*(a+1))
    else: print('FAIL',start,file=sys.stderr); start+=2000; continue
    open(fn,'wb').write(b); tot=d['totalResults']; print(start,tot,file=sys.stderr,flush=True); start+=2000; time.sleep(6.5)
print('DONE',file=sys.stderr)
