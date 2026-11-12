# Stored XSS on wordpress.com

- **Source URL:** https://hackerone.com/reports/2012636
- **Fetched from:** https://hackerone.com/reports/2012636.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3176 (id 3176)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Stored XSS on wordpress.com

- **HackerOne report:** https://hackerone.com/reports/2012636
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Cross-site Scripting (XSS) - Stored
- **Program:** Automattic (https://hackerone.com/automattic)
- **Reporter:** riadalrashed
- **Submitted (UTC):** 2023-06-05T00:56:43.440Z
- **Disclosed (UTC):** 2023-06-26T15:49:29.173Z

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
Hello team,
I found a Stored XSS vulnerability in WordPress.com via app.crowdsignal.com. It is similar to report #1987172.

## Platform(s) Affected:
wordpress.com

1 .Go to https://app.crowdsignal.com/dashboard and create a poll.
2. Enter the following payload as an answer: "style="position:fixed;top:0;left:0;border:999em solid green;" onmouseover="alert(document.cookie)"
3. Go to "Share Your Poll" and copy the link.
4. Navigate to https://wordpress.com/posts and add a new post.
5. Include the copied link in the post.
6. Save the post.
7. Open the page and click on "View Results."
8. The XSS vulnerability will be triggered.

████

## Impact

The attacker can use this issue to execute malicious script code in the victim user browser also redirect the victim user to malicious sites
