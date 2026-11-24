# XSS in Email Login Fields($$$)

- **Source URL:** https://medium.com/@videopourtoujour/xss-in-email-login-fields-bd1a7e4ff568?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230614054458/https://medium.com/@videopourtoujour/xss-in-email-login-fields-bd1a7e4ff568
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2976 (id 2976)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS in Email Login Fields($$$)

## [**full vuln Report On https://bugbeat.tech.**](https://bugbeat.tech)

--

Cross Site Scripting (XSS) is a security flaw found in web applications that permits an external entity to execute a script within a user’s web browser. By exploiting XSS, an attacker can inject JavaScript code into a webpage, which is then executed on the user’s device rather than the server.

Apologies, due to disclosure rules, I am unable to reveal the specific target name. For the purpose of this discussion, let’s refer to it as “xyz.com”.

Once I selected xyz.com as my target, I began searching for any input fields that could potentially be vulnerable to XSS. I suspected that there might be some input fields, such as a search bar, where users can provide input. I tried numerous techniques in my attempt to discover an XSS vulnerability, but unfortunately, my efforts were fruitless. I am becoming increasingly discouraged as I am unable to find an XSS vulnerability on the target site, xyz.com.

In the second step, you can proceed by visiting an online RFC822 email validator. This validator is a tool that helps validate and verify email addresses according to the RFC822 standard.

Once you have accessed the RFC822 email validator, you can now begin constructing your own XSS payload. This payload is specifically designed to exploit potential vulnerabilities related to cross-site scripting.

My Payload is : “>\<sCriPt>alert(1)\</ScRipt>”@gmail.com

and a window has pop up , and this how you got the job done
