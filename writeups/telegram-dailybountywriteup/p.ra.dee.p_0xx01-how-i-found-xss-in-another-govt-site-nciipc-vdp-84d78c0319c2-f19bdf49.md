# How I Found XSS In Another Govt. Site

- **Source URL:** https://medium.com/@p.ra.dee.p_0xx01/how-i-found-xss-in-another-govt-site-nciipc-vdp-84d78c0319c2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250806085330/https://medium.com/@p.ra.dee.p_0xx01/how-i-found-xss-in-another-govt-site-nciipc-vdp-84d78c0319c2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6080 (id 6080)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found XSS In Another Govt. Site :: NCIIPC VDP !!

Hello Fellow Hunters !! Hope you all are well !!

*Intro: I am p\_ra\_dee\_p whom you all know as Professor0xx01. Today I am gonna to explain you my story about finding XSS Bug in an another govt. website. So, let’s jump into it……..*

# Bug :: Cross Site Scripting (XSS) :: MEDIUM

**CVSS score : 5.4 :-** *CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N*

Let’s say the target is target.gov.in. I have already collected the domains during subdomain enumeration phase. While surfing different websites & seeing wappalyzer, one thing caught my eyes that the site it using rich text editor framework named “**CKEditor”. (Which is known to me before)**

After seeing that, i remembered that i have already tested this “**CKEditor**” — web text editor before in another hunting. See about my writeup about it : **XSS IN CKEditor — By Professor0xx01.**

So, let’s make start a directory enumeration using **dirsearch** & see if my guesses are right or not ..??

`dirsearch -u https://target.com -x 404,403`
I got that endpoint but not the text editor accordingly………….!!

Then i moved to my another writeup (**XSS IN CKEditor — By Professor0xx01.)** & searched the endpoint as follows ,, to check wheather the CKEditor page actually exist or not…!!! And yayyyhhhhh………………… I got that juicy html page ………….!!!!!

The Juicy endpoint :

`https://<target>.gov.in/ckeditor/samples/plugins/htmlwriter/outputhtml.html` Now I quickly Inserted my XSS Payload to this page & Got the Alert () !!

``Xss<!--{cke_protected} --!><img src=x onerror=alert(`Professor0xx01`)> -->Attack``
**Steps To Reproduce :**

1. **First click on source ….**
2. **Give the malicious payload …..**
3. **Then click again on source !!**
4. **You will got that alert ()**.

Getting that alert(),, I feel like……………………………………. this 👇👇 !!

Then I made a report about that vulnerability/issue & mailed it to the NCIIPC Team !!

**THANKS FOR READING !!**

Hope you enjoyed it !! If you like, then clap & follow me for more insightful articles !!

That’s it for this article now !!

**Happy Hunting \~\~**

**Keep Growing & Keep Securing \~\~**
