# Why developers should never trust a null origin (Portswigger CORS lab #2 )

- **Source URL:** https://medium.com/@dwedar98/why-developers-should-never-trust-a-null-origin-portswigger-cors-lab-2-e64bfc14b722
- **Fetched from:** https://medium.com/@dwedar98/why-developers-should-never-trust-a-null-origin-portswigger-cors-lab-2-e64bfc14b722?source=rss-815cb76826a2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14953)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohamed Dwedar / Mon, 19 Oct 2026 17:12:01 GMT

*( lab #2 cors vulnerability with trusted null origin )*

*everything is the same in terms of the source code and the workflow as we discussed in the workthrough in lab #1, if you have not already read it i suggest you do before reading this one. so all we gotta do is to enumerate the whitelisted origins ( will do this using my scanner but you can absulotly do it manually )*

*and as you can see the null value and the original lab url are reflected, you can abuse the lab url if there is an XSS in it, but there is an easier way which is null origin*

*the null origin happens in couple situations such as:*

*i will leave the JS execution on the exploit server for you, but do not forget to add the sandbox attribute, another thing in real bug bounty assessments finding the vulnerability and reporting it is enough.*

*Potential Remediations:*

*2. Never reflect arbitrary origins or null*

*3. Set session cookie samesite to strict if cross-site functionality is not strictly required*

*check out my tool:*

*if you wanna get and try my CORS-Scanner: https://github.com/dwedar9487h/cors-scanner*

*if you got any ideas, feedback on it, please let me know*

*thanks for reading!*
