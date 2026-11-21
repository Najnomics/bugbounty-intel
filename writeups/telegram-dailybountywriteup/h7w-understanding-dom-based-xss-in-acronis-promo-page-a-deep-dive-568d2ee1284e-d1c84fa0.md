# Understanding DOM-Based XSS in Acronis Promo Page

- **Source URL:** https://medium.com/h7w/understanding-dom-based-xss-in-acronis-promo-page-a-deep-dive-568d2ee1284e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250903080853/https://medium.com/h7w/understanding-dom-based-xss-in-acronis-promo-page-a-deep-dive-568d2ee1284e
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10507 (id 10507)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Understanding DOM-Based XSS in Acronis Promo Page: A Deep Dive

## Exploring How to Detect and Exploit DOM-Based XSS

## Introduction

Cross-Site Scripting (XSS) is one of the most common web vulnerabilities, allowing attackers to inject malicious JavaScript code into a website, which then runs in the victim’s browser. Among the various types of XSS, DOM-based XSS is particularly sneaky because it occurs entirely on the client side, manipulating the Document Object Model (DOM) without requiring server-side changes. In September 2020, a security researcher named yash\_ submitted a report to Acronis via HackerOne, identifying a DOM-based XSS vulnerability on the `https://promo.acronis.com/` page. This article provides an in-depth explanation of DOM-based XSS, how to find such vulnerabilities, and a detailed breakdown of the Acronis report, written in simple English for both beginners and seasoned security enthusiasts.

We’ll first cover what DOM-based XSS is, why it’s dangerous, and how to detect it in web applications. Then, we’ll analyze the specifics of HackerOne report [982442](https://hackerone.com/reports/982442), including its steps to reproduce and potential impact. By the end, you’ll understand how to hunt for similar vulnerabilities and why they matter in the context of web security.
