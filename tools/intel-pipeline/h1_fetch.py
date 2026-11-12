import json,subprocess,time,os,sys,concurrent.futures as cf,threading
ids=[json.loads(l)['id'] for l in open('ids.jsonl')]
done=set(f[:-5] for f in os.listdir('reports'))
fail=open('failed.jsonl','a'); lock=threading.Lock(); backoff=[0]
def get(i):
    for a in range(5):
        if backoff[0]>time.time(): time.sleep(backoff[0]-time.time())
        p=subprocess.run(['curl','-s','-m','15','-w','\n%{http_code}',f'https://hackerone.com/reports/{i}.json','-H','Accept: application/json'],capture_output=True)
        body,_,code=p.stdout.rpartition(b'\n'); code=code.decode()
        if code=='200':
            try: d=json.loads(body)
            except Exception: code='badjson'
            else:
                d.pop('abilities',None)
                for k in ('reporter','team'):
                    if isinstance(d.get(k),dict): d[k].pop('profile_picture_urls',None)
                open(f'reports/{i}.json','w').write(json.dumps(d,ensure_ascii=False)); return
        if code=='429':
            with lock: backoff[0]=time.time()+60
            print('429',i,file=sys.stderr,flush=True); continue
        if code in ('404','403'): break
        print('code',code,i,file=sys.stderr,flush=True); time.sleep(3*(a+1))
    with lock: fail.write(json.dumps({'id':i,'code':code})+'\n'); fail.flush()
todo=[i for i in ids if i not in done]
print('todo',len(todo),file=sys.stderr,flush=True)
with cf.ThreadPoolExecutor(6) as ex:
    for n,_ in enumerate(ex.map(lambda i:(get(i),time.sleep(0.25)),todo)):
        if n%200==0: print('progress',n,time.strftime('%H:%M:%S'),file=sys.stderr,flush=True)
print('DONE',file=sys.stderr)
