# AppSec Tales XVII | SSRF

- **Source URL:** https://karol-mazurek95.medium.com/appsec-tales-xvii-ssrf-35e3a08c278?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012154548/https://karol-mazurek95.medium.com/appsec-tales-xvii-ssrf-35e3a08c278
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3658 (id 3658)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# AppSec Tales XVII | SSRF

--

Application Security Testing for the Server Side Request Forgery.

# INTRODUCTION

The article describes how to test the application to find Server Side Request Forgery vulnerabilities. The advice in this article is based on the following:

- OWASP Web Security Testing Guide
- OWASP Application Security Verification Standard
- Bug bounty reports
- Own experience.

# TOOLING

Tools with basic usage & wordlist used for SSRF detection.

## STANDALONE TOOLS

- [**SSRFmap**](https://github.com/swisskyrepo/SSRFmap)— SSRF semi-automatic discovery and exploitation tool.

I am not using it due to problems with JSON parsing and the need to specify injection points manually. However, I decided to share it here in case it may be helpful to someone else and if the tool improves in the future.


- [**internal\_ip\_addr\_disclosure.py**](https://github.com/Karmaz95/crimson/blob/master/scripts/internal_addr_disclosure.py) — script for detecting internal IP leak.

- [**ffuf**](https://github.com/ffuf/ffuf) — web fuzzer written in GO.
- [**Nessus**](https://www.tenable.com/products/nessus) & [**Burp Suite Professional**](https://portswigger.net/burp/pro) automatic scanners.

I have described how to use above automatic scanners in another article:


## BURP SUITE PRO EXTENSIONS

- [**Burp Bounty Pro**](https://burpbounty.net/) — additional automatic scanning capabilities.

## WORDLISTS

- [**SSRF**](https://github.com/Karmaz95/crimson/blob/master/words/exp/SSRF) —designed to find SSRF vulnerabilities. This wordlist contains ([**schemes.txt**](https://github.com/Karmaz95/crimson/blob/master/words/exp/schemes.txt)+[**hosts.txt**](https://github.com/Karmaz95/crimson/blob/master/words/exp/hosts.txt)), [**SSRF\_unique.txt**](https://github.com/Karmaz95/crimson/blob/master/words/exp/SSRF_unique.txt) and [**RFI**](https://github.com/Karmaz95/crimson/blob/master/words/exp/RFI) payloads.
- [**single-char**](https://github.com/Karmaz95/crimson/blob/master/words/exp/single-char) — stack trace detection.
- [**common\_TCP\_ports.txt**](https://raw.githubusercontent.com/Karmaz95/crimson/master/words/common_TCP_ports.txt) — top 1000 TCP ports.
