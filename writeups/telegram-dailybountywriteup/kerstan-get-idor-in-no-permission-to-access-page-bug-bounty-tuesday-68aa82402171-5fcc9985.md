# Get IDOR In No Permission To Access Page— Bug Bounty Tuesday

- **Source URL:** https://medium.com/@kerstan/get-idor-in-no-permission-to-access-page-bug-bounty-tuesday-68aa82402171?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240126110542/https://medium.com/@kerstan/get-idor-in-no-permission-to-access-page-bug-bounty-tuesday-68aa82402171
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5095 (id 5095)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Subscribed to:** [https://medium.com/@kerstan](/@kerstan)

Hello everyone, I’m Kerstan.

Today is Bug bounty Tuesday, I will share with you how to get a IDOR bug in no permission to access page.

So, let’s dive right in.

During the bug bounty process, I encountered a target. After an initial round of information gathering about the target, I was unable to find any exploitable areas.

So, I began testing the various features of the website. I registered an account and logged in with it to view the site’s content.

After repeatedly testing with Burp Suite’s Repeater, I discovered a module which couldn’t be accessed without permission.

I felt that it should be possible to attempt a breakthrough, so I checked the burp data packets in detail, as follows:

Upon identifying the ‘templatetypeid’ parameter within the data packet, I thought of probing the current module’s path as ‘/template’, therefore leading me to conceive “/template?templatetypeid=fuzz”.

After fuzzing the parameter values, as anticipated, I successfully exploited Insecure Direct Object References (IDOR) to access the webpage. Subsequently, I compiled the report and reported this vulnerability.

If this writing has been helpful to you, please consider giving it a clap and following. Thanks bro.

Alternatively, you can just buy me a coffee [here](https://www.buymeacoffee.com/kerstan), any sort of support is much appreciated. Enjoy your reading.

If you want to learn more knowledge about Bug Bounty Tuesday, please be sure to take a look at my latest articles.

## [Get IDOR In No Permission To Access Page— Bug Bounty Tuesday](/@kerstan/get-idor-in-no-permission-to-access-page-bug-bounty-tuesday-68aa82402171)

## [How To Get A XSSI Bug In Bug Bounty — Bug Bounty Tuesday](/@kerstan/how-to-get-a-xssi-bug-in-bug-bounty-bug-bounty-tuesday-7440b0caf32c)

## [Account Takeover on International Exchange — Bug Bounty Tuesday](/@kerstan/account-takeover-on-international-exchange-bug-bounty-tuesday-cf41a54bc4b7)

## [URL Redirection To DOM XSS on Hackerone Programs — Bug Bounty Tuesday](/@kerstan/dom-xss-on-hackerone-programs-bug-bounty-tuesday-8973ecf6af95)

## [How I Discovered SSRF on Hackerone Program](/@kerstan/how-i-discovered-ssrf-on-hackerone-program-7bbe72334f74)

## [How I Automatically Discovered SSRF on Hackerone Program](/@kerstan/how-i-automatically-discovered-ssrf-in-hackerone-program-2ae0b7a6ef1b)

PS.
