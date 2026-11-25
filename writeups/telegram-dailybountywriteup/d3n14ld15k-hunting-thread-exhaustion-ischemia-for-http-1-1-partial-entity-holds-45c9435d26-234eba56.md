# Hunting Thread Exhaustion

- **Source URL:** https://medium.com/@d3n14ld15k/hunting-thread-exhaustion-ischemia-for-http-1-1-partial-entity-holds-45c9435d269d
- **Fetched from:** https://medium.com/@d3n14ld15k/hunting-thread-exhaustion-ischemia-for-http-1-1-partial-entity-holds-45c9435d269d?source=rss-d06514b60e0f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14956 (id 14956)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** denialdisk / Fri, 23 Oct 2026 04:44:57 GMT

Howdy cowboys! This write-up is a quick note about how and why I developed this tool. Although I’ve been using a version of this internally for many years, this public release got some AI polish. Sorry hAIters.

While testing large-scope, on-premises deployments over the years, I kept noticing the exact same pattern: manually holding a POST request caused certain endpoints to hang indefinitely. Yes, even in 2026. This takes me back to when I was a teen lol. So many years later and it’s still current.

The backend was using a synchronous, “thread per request” architecture (common in older Java, PHP-FPM, Apache Tomcat, or default Python/Flask setups). By sending a valid Content-Length header and deliberately withholding the final byte of the body, I could tie up a worker thread indefinitely. **It’s pure OG material**

Doing this manually proves the concept, but try explaining “I slowed down the server” to a triage team and watch them close it as *“Theoretical / Low Severity”*. To turn this into a validated, reproducible vulnerability, I needed to scale it without triggering WAF rate limits or exhausting my own local resources, so, I built [Ischemia](https://github.com/D3N14LD15K/ischemia).

When testing for resource exhaustion, you face three immediate hurdles:

For Ischemia, Python’s asyncio does the job perfectly. Ischemia doesn’t just flood; it orchestrates. It is designed for evidentiary integrity.

Tool here: [https://github.com/D3N14LD15K/ischemia](https://github.com/D3N14LD15K/ischemia)

**Disclaimer: This tool is for educational purposes only. Ischemia may cause a denial of service on the target. I am not responsible for any damage caused while testing with this tool.**

A report needs a clear before and after. Ischemia generates a JSON summary that gives triage teams undeniable proof.

**Step 1: Run a baseline (no hold)**

python3 ischemia.py --host target.com --port 443 --scheme https --endpoint /api/login --connections 500 --hold-seconds 0 --out baseline

**Step 2: Run the hold**

python3 ischemia.py --host target.com --port 443 --scheme https --endpoint /api/login --connections 2000 --arm-concurrency 100 --arm-rate 50 --hold-seconds 30 --data 'user=test&pass=test' --out attack

Here is what a successful, vulnerable hit actually looks like in the output:

**3. Chain the Impact**: Don’t just report DoS. If the login endpoint is exhausted, can you prevent a user from resetting their password while you brute-force it? If the API is down, does it fail open or break a dependent business workflow?

If you are securing an application, fix this at the edge:

All right, that’s all for today folks lol. Hack the planet!
