# From File Upload Found LFI

- **Source URL:** https://medium.com/@g52238317/from-file-upload-found-lfi-7d17e5250b7a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905082344/https://medium.com/@g52238317/from-file-upload-found-lfi-7d17e5250b7a?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10147 (id 10147)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From File Upload Found LFI

Hi, i’m Abdelrhman Yasser, a penetration tester and bug hunter in the 4th year in computer science.

today i want to share how i found LFI from file upload function in a external program so lets get started.

the bug didn’t resolved yet so let refer to it as target.com


first i do some recon deeply after that i found subdomain called: posthog.target.com after that i found page of Subscription Plans

I choose Gold plan after that i found there are several way to pay: bank or online after that i choose bank i found file upload to Upload payment screenshot.

after click submit i found a link to my screenshot i clicked on it and intercept the request:

after that i try to upload a malicious file to execute php to try to get RCE but with my bad luck there was no server side execution php files.

after that i found path parameter so start to test LFI so i put these payload:

../../../../../etc/passwd and with my surprise its worked.

after that i try attempt another sensitive files to increase the impact like:

../../../../../etc/profile

../../../../../etc/hostname

../../../../../etc/hosts

../../../../../etc/group

../../../../../etc/issue

and they all worked.

that’s it i hope you have benefited from reading these writeup.

Thank you!
