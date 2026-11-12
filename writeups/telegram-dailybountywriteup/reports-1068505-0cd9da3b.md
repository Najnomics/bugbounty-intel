# Phishing/Malware site blocking on Brave iOS can be bypassed with trailing dot in hostname

- **Source URL:** https://hackerone.com/reports/1068505
- **Fetched from:** https://hackerone.com/reports/1068505.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3117 (id 3117)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Phishing/Malware site blocking on Brave iOS can be bypassed with trailing dot in hostname

- **HackerOne report:** https://hackerone.com/reports/1068505
- **State:** Resolved
- **Severity:** medium (score 6.1)
- **Weakness:** Violation of Secure Design Principles
- **Program:** Brave Software (https://hackerone.com/brave)
- **Reporter:** nishimunea
- **Submitted (UTC):** 2020-12-29T23:14:50.203Z
- **Disclosed (UTC):** 2023-06-22T05:52:15.530Z
- **Attachments (filenames only; expiring CDN URLs omitted):** brave_malware_protection_bypass.mov (video/quicktime)

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:

Phishing/Malware site blocking feature on Brave iOS blocks navigation to the domains in [simple_malware.txt](https://github.com/brave/brave-ios/blob/821785db8fc71fd084a8a0b2600ff43ea7165ce9/Client/WebFilters/SafeBrowsing/Lists/simple_malware.txt).
But that logic doesn't care existence of a trailing dot in the hostname, so http://3e1.cn/ in the list is correctly blocked but [http://3e1.cn./](http://3e1.cn./) is not blocked.

Safe browsing in Brave for PC/Mac (Chromium based) can blocks both URLs, so Brave iOS should align with it.

## Products affected: 

* Brave iOS nightly build

## Steps To Reproduce:

* Enable "Blocking Phishing and Malware" feature on Setting
* Open [http://3e1.cn./](http://3e1.cn./)

## Supporting Material/References:

  * See attached demonstration movie file

## Impact

User is taken to the prohibited malware/phishing site with bypassing Brave Shield protection.
