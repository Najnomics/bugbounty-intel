# How i found XSS and chained it with CSRF

- **Source URL:** https://medium.com/@alshormanmomen681/how-i-found-xss-and-chained-it-with-csrf-b99bc589ad5b?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@alshormanmomen681
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 9277)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
first i checked my personal account on the website and noticed that i can upload any image as my PFP

so i tried uploading an SVG file with XSS and boom,

it took it but no alert has shown…..

So i right clicked on my pfp and opened it in a new tab and them BOOM we got an XSS baby

but wait, the XSS is in a subdomain so not all important cookies will be there, we need to escalate that.

i inspected the cookies and noticed that there are 4 cookies on this subdomain.

after that i tried changing my account password and the only cookies that were required were those 4 cookies, Nice.

the endpoint was GRAPHQL so i used this to craft a CSRF paylaod( [https://medusa0xf.medium.com/how-to-perform-csrf-attack-in-graphql-api-fda9594dbd42](https://medusa0xf.medium.com/how-to-perform-csrf-attack-in-graphql-api-fda9594dbd42) )

CSRF was successfully done.

shout out to Hacking Notes he helped me a lot
