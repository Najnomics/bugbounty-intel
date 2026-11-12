import re,subprocess,trafilatura,os,json,time
urls=sorted(set(re.findall(r'href="(/[0-9]{4}/[0-9]{2}/[^"#]+)"',open('archive.html').read())))
urls=['/0day.html']+urls
log=[]
for u in urls:
    fn='posts/'+u.strip('/').replace('/','_').replace('.html','')+'.md'
    if os.path.exists(fn): continue
    h=subprocess.run(['curl','-sL','-m','40','https://projectzero.google'+u],capture_output=True).stdout.decode('utf-8','replace')
    t=trafilatura.extract(h,output_format='markdown',include_links=True,include_tables=True,include_formatting=True,favor_recall=True)
    m=re.search(r'<title>(.*?)</title>',h,re.S); title=(m.group(1).strip() if m else u)
    if not t or len(t)<300: log.append({'url':u,'status':'fail','len':len(t or '')}); continue
    open(fn,'w').write(f'# {title}\n\nSource: https://projectzero.google{u}\nCaptured verbatim (article body extracted from HTML) on 2026-11-12.\n\n---\n\n{t}\n')
    log.append({'url':u,'status':'ok','len':len(t)}); time.sleep(0.5)
json.dump(log,open('p0log.json','w'),indent=0)
print(len(urls),sum(1 for l in log if l['status']=='ok'),[l for l in log if l['status']!='ok'])
