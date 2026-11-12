import subprocess,json,urllib.request,time,sys,datetime
Q="query H($queryString: String!, $from: Int, $size: Int, $sort: SortInput!) { search(index: CompleteHacktivityReportIndex, query_string: $queryString, from: $from, size: $size, sort: $sort) { total_count nodes { ... on HacktivityDocument { report { databaseId: _id title disclosed_at } } } } }"
def gq(qs,frm=0,size=100):
    body=json.dumps({"operationName":"H","variables":{"queryString":qs,"from":frm,"size":size,"sort":{"field":"disclosed_at","direction":"ASC"}},"query":Q}).encode()
    for a in range(6):
        try:
            p=subprocess.run(["curl","-s","-m","40","https://hackerone.com/graphql","-H","Content-Type: application/json","--data-binary","@-"],input=body,capture_output=True)
            return json.loads(p.stdout)["data"]["search"]
        except Exception as e:
            print("err",e,file=sys.stderr); time.sleep(5*(a+1))
    raise SystemExit("fail "+qs)
ids={}
try:
    for l in open("ids.jsonl"): d=json.loads(l); ids[d["id"]]=d
except FileNotFoundError: pass
out=open("ids.jsonl","a")
def rng(a,b): return f'disclosed:true AND disclosed_at:[{a} TO {b}]'
def walk(a,b):
    s=gq(rng(a,b),0,100); n=s["total_count"]
    print(a,b,n,file=sys.stderr)
    if n>9000:
        da=datetime.date.fromisoformat(a); db=datetime.date.fromisoformat(b); mid=da+(db-da)/2
        walk(a,mid.isoformat()); walk((mid+datetime.timedelta(days=1)).isoformat(),b); return
    frm=0
    while frm<n:
        s=gq(rng(a,b),frm,100) if frm else s
        for nd in s["nodes"]:
            r=nd.get("report") or {}
            i=r.get("databaseId")
            if i and i not in ids:
                ids[i]={"id":i,"title":r.get("title"),"disclosed_at":r.get("disclosed_at")}; out.write(json.dumps(ids[i])+"\n")
        frm+=100; time.sleep(0.7)
    out.flush()
# by year, then month if needed
for y in range(2013,2027):
    for m in range(1,13):
        a=datetime.date(y,m,1); b=(datetime.date(y+(m==12),m%12+1,1)-datetime.timedelta(days=1))
        walk(a.isoformat(),b.isoformat())
print("TOTAL",len(ids),file=sys.stderr)
