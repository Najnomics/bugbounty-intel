# XSS

- **Source URL:** https://medium.com/@n45ht/xss-bypass-cloudfront-waf-9d0c8a12dc33?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501140137/https://medium.com/@n45ht/xss-bypass-cloudfront-waf-9d0c8a12dc33
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8512 (id 8512)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS: Bypass CloudFront WAF

In this article, we will share how we successfully bypassed the **CloudFront WAF** (Web Application Firewall) to exploit a **Cross-Site Scripting (XSS)** vulnerability.

# Payloads:

To bypass the **CloudFront WAF**, we crafted a special XSS payload. The goal was to find a way to inject JavaScript while preventing the WAF from detecting it as malicious. Here is the payload we used:

`<object/data="javascript:alert/**/(document.domain)">//</object>`
This payload is interesting because it uses a combination of an `<object>` tag and a **javascript** URI scheme. Notice how the colon (`:`) in `javascript:` is encoded as `:`, which can help bypass basic filtering rules in the WAF. Additionally, the `/**/` is used to comment out portions of the string, making it harder for the WAF to detect the attack.

After injecting the payload, we successfully triggered the **XSS** attack. The **CloudFront WAF** was bypassed, and the alert box displayed the document’s domain. This confirmed that the vulnerability existed and that the WAF didn’t block our payload.

More information:
