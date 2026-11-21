# How I discovered Reflected XSS in GoldAcademy.

- **Source URL:** https://medium.com/@secourses8/how-i-discovered-reflected-xss-in-goldacademy-257b69a14be8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250906033532/https://medium.com/@secourses8/how-i-discovered-reflected-xss-in-goldacademy-257b69a14be8
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9759 (id 9759)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I discovered Reflected XSS in GoldAcademy.

First of all, as usual, we need to make some infogathering

In this write-up, I will share a methodology for subdomain enumeration

GoldAcademy is a learning platform in Jordan, and I do hunting on it, and I discovered a vulnerability and I reported it, without no answer. No problem, we will just use it for educational purposes, not to harm the platform.

1. [Securitytrails.com](http://Securitytrails.com)
2. [subdomainfinder.c99.nl](http://subdomainfinder.c99.nl)
3. shrewdeye.app/search

These are some good sites I use to enumerate subdomains, but I didn't find a subdomain because the website doesn't have

I continue subdomain enum.

Subfinder -d gold-jo.com -all

And I didn't find it.

u should gather more info about the technology used, a I don't use it in this situation, but I didn't recommend this

I am using automated scanning using Nessus Professional, and Nessus tells me there is xss vulnerability, so I started looking find any input and I tried using many inputs, but I didn't find also.

Finally I found the XSS in the URL **https://gold-jo.com/ar/course?crs=\<script>alert(“XSS Alert by LIme”)\</script>**

I reported the vulnerability, and no answer
