# Discovering SQLi Vulnerabilities Through Deeper Analysis

- **Source URL:** https://medium.com/@erkankavas/discovering-sqli-vulnerabilities-through-deeper-analysis-4e305dfbc181?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250202110754/https://medium.com/@erkankavas/discovering-sqli-vulnerabilities-through-deeper-analysis-4e305dfbc181
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8393 (id 8393)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Discovering SQLi Vulnerabilities Through Deeper Analysis

During a deeper exploration of the site I mentioned in [my recent Medium blog](/@erkankavas/bypassing-wafs-a-unique-xss-exploit-journey-and-insights-520d7060c281), I discovered not only XSS vulnerabilities but also SQLi vulnerabilities.

Let’s discuss why it’s crucial to dig deeper into a site when you discover a vulnerability **before** deciding to report it.

As I’ve mentioned before, the reconnaissance phase is incredibly important, and you should continue your reconnaissance efforts even after finding an initial vulnerability. Every small mistake might lead you to something much bigger, so patience and keeping your **eyes open** are key.

The least painful and most common method for testing SQLi vulnerabilities is the time-based approach. Generally, WAF systems block Boolean and other types of attacks as they have corresponding payloads archived. However, time-based SQLi often provides an option to bypass such systems.

While analyzing areas of the site where I had found XSS vulnerabilities, I noticed a section that displayed color palettes. This section communicated via a simple PHP file (`like.php`) using parameters. Functions like "like" and "follow," which are often poorly sanitized by developers, are some of the most promising areas for discovering SQLi vulnerabilities. Focusing on such areas can yield significant benefits.

Using Burp Suite or a similar program, you can analyze these “like” and “follow” functions to identify parameters. Typically, `GET` requests are used, but if `POST` requests are…
