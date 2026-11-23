# IDOR lead to PII Disclosure

- **Source URL:** https://medium.com/@karimelsayed0x1/idor-lead-to-pii-disclosure-121502394277?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240705212625/https://medium.com/@karimelsayed0x1/idor-lead-to-pii-disclosure-121502394277
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6020 (id 6020)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
IDOR, or Insecure Direct Object Reference, is a vulnerability where an attacker can access and manipulate resources directly by modifying parameters such as URLs or input fields, bypassing authorization controls. This flaw exposes sensitive information or functionalities that are supposed to be protected. When exploited, IDOR can lead to the unauthorized disclosure of personally identifiable information (PII), such as names, addresses, or financial data. PII disclosure poses serious risks to individuals’ privacy and can result in various forms of identity theft or fraud. Therefore, it’s crucial for organizations to implement robust access controls and thoroughly audit their applications to mitigate the risk of IDOR and protect users’ PII.

**Story of finding:**

During my holiday from military service, I’ve been dedicating time to revising my old notes and creating new ones. Alongside this, I’ve been actively engaged in honing my bug hunting skills, selecting specific targets for testing. One such target, “target.xyz”. Despite testing it twice before without success, I decided to give it another shot. Armed with various techniques and strategies, I delved into the platform’s systems, meticulously analyzing for vulnerabilities.

While on my bug hunting adventure at target.xyz, I dove deep into the cyber jungle, armed with my trusty OWASP Top 10 guidelines. Sadly, my search for vulnerabilities like Injection flaws or Broken Authentication felt like looking for a needle in a haystack. But fear not, fellow cyber explorers! I’m not giving up just yet. There’s still a treasure trove of potential weaknesses waiting to be discovered, and I’m determined to make target.xyz the Fort Knox of online sports platforms!

As I venture into the realm of logic bugs, my quest begins with tinkering around with response manipulation. Alas, no luck! Undeterred, I decide to tackle the ubiquitous beast known as IDOR, because, let’s face it, it’s everywhere! Within target.xyz, I stumble upon a fascinating discovery: two methods for placing orders — one for authenticated users and another for the unauthenticated bunch.

Authenticated order request:

Upon inspecting the request, I found that my attempts to manipulate it were unsuccessful, largely due to the Authorization: Bearer eyJ… header.

At this juncture, I am initiating an unauthenticated attempt to place an order, aiming to uncover any potential vulnerabilities or insights that may arise from this process.

Unauthenticated order request:

Ah, I see. In that case, even though the request is a simple POST to send data to the server without exposing any personally identifiable information, But what if we change the request method and try to GET data from the server rather than POST data.

Hmm, it seems like switching up the request method didn’t quite do the trick; the endpoint still won’t play ball. But hey, what if we zoom in on the “/buy-now/” part and see if tweaking that gets us anywhere? Let’s give it a shot and see if we can uncover any new possibilities.

and Booooom!!!!!!!!
