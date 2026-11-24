# My First IDOR - Hiding in the Header Request

- **Source URL:** https://medium.com/@hbenja47/my-first-idor-hiding-in-the-header-request-8a03dddc23b5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250904193730/https://medium.com/@hbenja47/my-first-idor-hiding-in-the-header-request-8a03dddc23b5
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4483 (id 4483)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My First IDOR - Hiding in the Header Request

In the midst of a busy schedule, the little time I dedicate to bug hunting brings immense joy, especially when I stumble upon something new. Reporting my first IDOR was a thrilling experience.

While examining a web application, **I noticed that it didn’t use cookies for API requests but relied on a header: “Authorization: Bearer XXTXXXXOXXXXXKXXXXXEXXXXXXNXX”**. Investigating **the GET request that responded with my user data** — email, name, UUID, etc. — **I realized there was no ID in the URL**. I speculated that the Bearer token not only managed access control but also identified the user’s ID to fetch their data.

Curious, **I removed the entire header: “Authorization: Bearer XXTXXXXOXXXXXKXXXXXEXXXXXXNXX”** and repeated the request. Surprisingly, **it still returned my user data**. Intrigued, I delved into the headers — a step I initially skipped — and **discovered a custom header named “DomName,**” containing a string of three letters, a dash, three letters, and three numbers: “ABC-AB012”. **This was the user ID for the system**.

To validate this, I created another user and tested with a different user ID, which worked flawlessly.

Crafting the report, I highlighted the triviality of guessing and brute-forcing such user IDs. Although I didn’t perform a brute-force attack on real user data, I made it clear in the report that it was easily achievable. I even offered to provide the script for brute-forcing and dumping data, though it wasn’t necessary.

*This discovery was considered a high severity issue, earning me points and rewards.*

I shared on X (formerly Twitter) that I found an IDOR using a header request as a parameter. A Bugcrowd triager responded, suggesting that if I continued with this methodology, I might uncover many more similar bugs. It seems like this is a common bug in the wild.

😎 Happy hunting!!!
