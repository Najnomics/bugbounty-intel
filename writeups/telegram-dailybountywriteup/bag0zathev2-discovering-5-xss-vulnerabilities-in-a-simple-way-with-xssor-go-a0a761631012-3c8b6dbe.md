# Discovering 5 XSS Vulnerabilities In a Simple Way With Xssor.go

- **Source URL:** https://medium.com/@bag0zathev2/discovering-5-xss-vulnerabilities-in-a-simple-way-with-xssor-go-a0a761631012?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241229192916/https://medium.com/@bag0zathev2/discovering-5-xss-vulnerabilities-in-a-simple-way-with-xssor-go-a0a761631012
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1593 (id 1593)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Discovering 5 XSS Vulnerabilities In a Simple Way With Xssor.go

This write-up is specially made for showing the power of my new tool, It’s called Xssor.go

This tool is a XSS payload reflection tester

It’s checking all the params reflections with encoding or without

like submitting in all the params value like “Hi\<>” and checking if the \<> are reflected without encoding, so now there’s a XSS Possibility !!

Go try to send your payload ❤

I was able here to get more than 5 XSS Vulnerabilities with this tool, But how did i do that?

First of all You can find the tool in my [Github@SirBugs/Xssor.go](https://github.com/SirBugs/Xssor.go)

You need now to get subdomains!

[Github@OWASP/Amass](https://github.com/OWASP/Amass)
[Github@tomnomnom/assetfinder](https://github.com/tomnomnom/assetfinder)
Then to get all the urls now containing as much as params as u can get! How to do that?

There’s more than a tool using

[Github@projectdiscovery/katana](https://github.com/projectdiscovery/katana)

[Github@tomnomnom/waybackurls](https://github.com/tomnomnom/waybackurls)
[Github@lc/gau](https://github.com/lc/gau)
[Github@hakluke/hakrawler](https://github.com/hakluke/hakrawler)

Since some of them are taking urls, and the others are taking only domain names, We should prepare a file for the only subdomains, and another one for the “https://”+\<DOMAINS> 

I called the subdomains file: **hosts-live.txt**

And called the urls file: **hosts-urls.txt**

So, What are the commands?

```
// subdomain enumeration
amass enum -active -d <DOMAIN> -dir amass_active/<DOMAIN>/
amass enum -passive -d <DOMAIN> -dir amass_passive/<DOMAIN>/
assetfinder <DOMAIN> | tee ./subdomains/assetfinder.txt
// web crawlling
for i in $(cat hosts-urls.txt); do katana -u $i >> ./katana_rzlts.txt; done
cat hosts-urls.txt | hakrawler -timeout 5 -subs | tee ./hakrawler_rzlts.txt
cat hosts-live.txt | gau --threads 15 | tee ./gau_rzlts.txt
cat hosts-live.txt | waybackurls | tee ./wburls_rzlts.txt
// filtering .txt files, Running Xssor.go
cat katana_rzlts.txt hakrawler_rzlts.txt gau_rzlts.txt wburls_rzlts.txt | sort -u > uniq.txt; cat uniq.txt | grep "<DOMAIN>" | grep "\?" > to_xssor.txt
Xssor.go to_xssor.txt
```
Now The tool started to get me ouput! and Some reflections (with encoding), I don’t need them, and the others reflecting the \<> without encoding!

I was able to basically send my payload in the params in those URLS! who are reflecting without encoding. very basic payloads like: 

1. h”>\<script>alert(1)\</script>

2. \<img src=x onerror=alert(1)>

Then Boom!!

Easily Getting free XSS Reports!

Wish you like this write-up, as soon as i get smth interesting to write about it, im gonna share it :D

Keep viewing my Github, I am gonna start foucsing alittlebit for making some tools for bug bounty hunting ❤

Have fun and keep digging ❤
