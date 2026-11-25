# How I Found an Easy Dom xss.

- **Source URL:** https://medium.com/infosecmatrix/how-i-found-an-easy-dom-xss-b93bbe09e2bf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250224210844/https://medium.com/infosecmatrix/how-i-found-an-easy-dom-xss-b93bbe09e2bf?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8870 (id 8870)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Found an Easy Dom xss.

## Learn how to find one of the easy bugs.

**FREE LINK IN THE COMMENTS**


**BUGNAME: CVE : CVE-2022–29455. DOM CROSS SITE SCRIPTING.**


**In this blog, You will see how I found an easy dom xss.**

**Now let’s see.**

**After loading my target URL.**

**I checked which technologies are running on this domain using Wappalyzer.**

**in Wappalyzer I observed this website’s page builder is Elementor 3.25.4 is the version.**

**After I copied that URL I checked that URL in nuclei using nuclei templates.**

`nuclei -u yoururl -t /root/nuclei-templates/http/technologies/`
**And I confirmed the version using nuclei.**

**It’s time to exploit this.**

`https://yourtargeturl/#elementor-action:action=lightbox&settings=eyJ0eXBlIjoibnVsbCIsImh0bWwiOiI8c2NyaXB0PmFsZXJ0KCd4c3MnKTwvc2NyaXB0PiJ9Cg==`
**I entered this above payload in my target URL and clicked on enter.**
