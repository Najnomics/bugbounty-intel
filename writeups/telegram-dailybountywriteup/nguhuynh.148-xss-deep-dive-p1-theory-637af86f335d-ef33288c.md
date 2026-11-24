# XSS deep dive P1 (theory)(publish early,please waiting for 2 days to read)

- **Source URL:** https://medium.com/@nguhuynh.148/xss-deep-dive-p1-theory-637af86f335d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231230161241/https://medium.com/@nguhuynh.148/xss-deep-dive-p1-theory-637af86f335d
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4856 (id 4856)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS deep dive P1 (theory)(publish early, waited for 2 days to read😅)

Hi everyone, XSS is a common and popular vulnerability that is quite hard to good at XSS.

If you care about statistics, H1 has created [this](https://hackerone.com/hacktivity/cwe_discovery?id=cwe-79):

So XSS is an important skill for a bug hunter. If you are good at XSS you can create a lot of money:)).

In this Blog, I will explain some impressive reports, blogs, and some tricks. I don’t like to write something basic here, because there have many blogs, videos,… about that.

# 1. Where should I inject the XSS payloads?

Many people just care about the parameters in the URL(https://target.com/?parameter=\<script>alert()\</script>). Or some way to check Stored XSS (username, email,…). But that is not all.

## a) Reflected

Anything reflected :))

- XSS in the URL parameter, For example:

Payload: [http://marketsandresearch.td.com/tdwca/Public/Stocks/TechnicalInsight/ca/TD'-alert('def1ant')-'?=](<http://marketsandresearch.td.com/tdwca/Public/Stocks/TechnicalInsight/ca/TD%27-alert(%27def1ant%27)-%27?=>)

The payload reflects in functions, creates the payload to inject

decrypt: → search=*“ , internalSearchTerm: \[7\].map(alert) , numOfSearchResultsReturned: “b*

- …

## b) The payload in another website

## c) Other

XSS in Cookie

# 2. Filter

To understand or create some complex payload you must understand the context or the filter. There have 3 filters: *CSP*, *Cloud Flare*, and *Sanitize*.

Each website has its own filter (maybe no filter:)) ) so the payload can be so easy

## a) Cloudflare (The first one you must bypass to create the XSS Payload)

To bypass Cloudflare, you can try to access redirect to the IP address(if you can, that is the [vulnerability](https://hackerone.com/reports/1536299)). If you can’t, try this:

Check what tag, event, function,… Cloudflare allows. → *For example*: allow \<img> tag, onerror event, and alert function so our payload is: *\<img src=x onerror=alert()> ¯\\\_(ツ)\_/¯*

Sometimes you can use this [\<scr%00ipt>, alert/\*\*/()](https://buer.haus/2017/03/08/airbnb-when-bypassing-json-encoding-xss-filter-waf-csp-and-auditor-turns-into-eight-vulnerabilities/), […](https://0xjin.medium.com/new-xss-bypass-cloudflare-filters-2a878c01d312) to bypass Cloudflare

## b) Sanitize

Sanitize has 2 main functions:

- Remove special characters or some sensitive words: “ ‘ \< > / ( ) alert eval prompt …
- Encrypt special characters to URL, HTML,…

To bypass this you must be creative in creating the payload, reference:

- [XSS Payloads all the things](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSS%20Injection).
- Read someone's blog and [report](https://hackerone.com/hacktivity/cwe_discovery?id=cwe-79) to learn the way to bypass.

## c) CSP

Internet Explorer doesn’t support CSP. So if you can’t bypass CSP, you can inject it into that browser. Or the platform doesn’t agree with your vulnerability, you can argue with them:))

To get CSP information on the website you can use [https://csp-evaluator.withgoogle.com/](https://csp-evaluator.withgoogle.com/) or [Extention](https://chrome.google.com/webstore/detail/csp-evaluator/fjohamlofnakbnbfjkohkbdigoodcejf)

To bypass CSP:

- Get information on CSP at the target.com, focus on the serious problem

- To bypass you must analyze that information, it is not too hard:))

To check your payload has bypassed CSP you can use console in dev tool
