# Brave News feeds can open arbitrary chrome

- **Source URL:** https://hackerone.com/reports/1819668
- **Fetched from:** https://hackerone.com/reports/1819668.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3090 (id 3090)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Brave News feeds can open arbitrary chrome: URLs

- **HackerOne report:** https://hackerone.com/reports/1819668
- **State:** Resolved
- **Severity:** high
- **Weakness:** Privilege Escalation
- **Program:** Brave Software (https://hackerone.com/brave)
- **Reporter:** nishimunea
- **Submitted (UTC):** 2023-01-01T08:55:37.266Z
- **Disclosed (UTC):** 2023-06-22T05:50:08.953Z
- **Attachments (filenames only; expiring CDN URLs omitted):** open_chrome_urls_from_brave_news_feed.mov (video/quicktime)

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
URL link in Brave News feeds can open arbitrary chrome: URLs.
This behavior can be exploited as a way to bypass SOP and gain access to privileged URLs.

## Products affected: 

 * 1.46.144 Chromium: 108.0.5359.128 (Official Build) （x86_64）

## Steps To Reproduce:

 * Open new tab and click customize button
 * Follow https://csrf.jp/brave/rss_chrome.php as a RSS feed of Brave News
 * Reload the tab
 * RSS feeed that name is "Access chrome: URLs" is shown on Brave News
 * Click the feed
 * `chrome://settings/resetProfileSettings?origin=userclick` is opened on the tab

## Supporting Material/References:

  * See the demonstration movie I attached

## Impact

Bypass SOP and gain access to privileged URLs.
