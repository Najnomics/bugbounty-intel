# Found SSRF and LFI in Just 10 minutes of using burp!

- **Source URL:** https://xelkomy.medium.com/found-ssrf-and-lfi-in-just-10-minutes-of-using-burp-492fddef3f3e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230411001628/https://xelkomy.medium.com/found-ssrf-and-lfi-in-just-10-minutes-of-using-burp-492fddef3f3e?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2190 (id 2190)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Found SSRF and LFI in Just 10 minutes of using burp!

**Hello, and welcome again after about two years from the last published write-up. Here is a new write-up about a simple vulnerability I have got by just the browser and the burp suite.**

# **Summary**

At the beginning of the article, I have to say the vulnerability is so sample, but it needs some browsing into your targets, I have got two vulnerabilities in just one parameter named `src` and this parameter is taken URL as an input.

# **Requirements**

We just need to have the burp suite professional or the community edition. I think it will be enough for testing this vulnerability because we just need to crawl the target with the burp and use the *Auto Repeater* to test it.

# The Story

On the normal days, when I have to do bug bounty, already I have recon script using bash the script run `subfinder, amass, assetfinder,httpx , nuclei, ffuf, uncover, notify…etc` and after this script finished I do my manual work like creating new `burp suite` project and preparing my burp with my extensions like `AutoRepeater and ActiveScan++,.etc`

From three years I have seen an AutoRepeater regex was interesting to me on a medium blog from @[Renato Dante](https://web.archive.org/web/20230411001628/https://dant0x65.medium.com/?source=post_page-----ea344ec59962--------------------------------) and his write-up about the `Bug Bounty tip Automating SSRF` it was a good write-up but in the last three years I got nothing with this regex in the Renato write up but at least in this year I got a bounty with it.

```
https?://(www.)?[-a-zA-Z0–9@:%.+~#=]{1,256}.[a-zA-Z0–9()]{1,6}\b([-a-zA-Z0–9()@:%+.~#?&//=]*)
```
The Above regex is what I have used to get the SSRF, with those steps like below.

1 — Get the alive subdomain from `subfinder` and send them to `httpx`

2 — Open the `burp suite`, create a new project and set up your autorepeater with the above regex and settings like the above image.

3 — Use Katana tool by projectdiscvery and use the proxy option and add the burp proxy URL by the default, it will be `http://127.0.0.1:8080`

4 — Open the subdomain manually by the browser and visit every login page and any page you have seen on the target website you have.

5 — Open the burp again and you will see the catch by the burp suite auto repeater extension, if there are any parameters to take an input like [http://google.com](https://web.archive.org/web/20230411001628/http://google.com/)

One-liner for using `subfinder, httpx, katana` to send the result to burp proxy:

`subfinder -d hackerone.com | httpx -timeout 10 | katana -proxy http://127.0.0.1:8080 -jc -aff` In my case, I already got a SSRF by it just a low impact because I can’t get anything locally in the vulnerable website because there is an internal WAF block me from accessing the 127.0.0.1 or the AWS internal metadata IP.

But After some testing and testing multiple vulnerabilities on the same parameter I got LFI by the normal input was this

`?src=c%3a%5cwindows%5cwin.ini`

And after that, I have got a good deal of information about the targets, but I stop here because I don’t want to get banned from the H1 platform to getting any sensitive information about the internal system without permissions.

And I report it and get `$$$$` bounty after an about a week or week and half from reporting it.

# **Conclusion**

I have found a SSRF with help by AutoRepeater burp extension and didn’t get enough impact from SSRF and tried to find another vulnerability on the same parameter and I have found an LFI Vulnerability and accessing the internal file for the server.

Please don’t forget to follow me on Twitter [@0xELkomy](https://web.archive.org/web/20230411001628/https://twitter.com/0xElkomy), please don't hesitate to connect with me if you have anything.
