# How I Turned RFI Into RCE in 48 Hours for Just $200

- **Source URL:** https://medium.com/@ibtissamhammadi1/how-i-turned-rfi-into-rce-in-48-hours-for-just-200-215b4be27425?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905075909/https://medium.com/@ibtissamhammadi1/how-i-turned-rfi-into-rce-in-48-hours-for-just-200-215b4be27425?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9928 (id 9928)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How I Turned RFI Into RCE in 48 Hours for Just $200

### How a $200 weekend hack taught me to always check \<pre> tags.

It started with a call from *Rajesh’s Uncle* — the kind of relative who forwards WhatsApp “hacking tips” but runs a blog with **“admin” as the username**.

\*”Beta, my site is unhackable! I pay $50/month for ‘premium security’,”\* he declared. Meanwhile, his WordPress blog (earning **$800/month** from ads) had **Social Warfare plugin v3.5.2** — a version retired faster than a Bollywood one-hit-wonder.

I sighed. *“Let me check.”*

What began as a casual favor turned into a **48-hour race**: either stop a disaster or cash a **$200 bug bounty**.

### From RFI to RCE (Step-by-Step)

**The Lazy Sunday Scan**

A quick `wpscan` revealed the usual suspects: outdated plugins, weak permissions, and—jackpot—an unpatched *Social Warfare* vulnerability (CVE-2019-9978).

The plugin used `file_get_contents()` to fetch share counts… *without sanitizing user input*.

```
// Vulnerable code snippet (simplified)  
$url = $_GET['metrics_url'];  
$data = file_get_contents($url);  
echo "<pre>" …
```
