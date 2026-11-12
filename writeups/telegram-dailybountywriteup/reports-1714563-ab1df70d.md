# Jolokia Reflected XSS

- **Source URL:** https://hackerone.com/reports/1714563
- **Fetched from:** https://hackerone.com/reports/1714563.json
- **Fetched:** 2026-11-12
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/647 (id 647)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Jolokia Reflected XSS 

- **HackerOne report:** https://hackerone.com/reports/1714563
- **State:** Resolved
- **Severity:** medium (score 6.2)
- **Weakness:** Cross-site Scripting (XSS) - Reflected
- **Program:** Mars (https://hackerone.com/mars)
- **Reporter:** ramzanrl
- **Submitted (UTC):** 2022-09-27T17:29:15.614Z
- **Disclosed (UTC):** 2022-10-27T17:36:02.153Z
- **CVE:** CVE-2018-1000129

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:

(salam)
Hi team i hope you are well , after doing some recon on ███████ i saw that the website use jolkia 1.3.5 it's vulnerable to reflected XSS  

## Steps To Reproduce:

  1. Vuln Link : ████:
CVE-2018-1000129

Jolkia - Version
████████


##POC 

█████████

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can:
Perform any action within the application that the user can perform.
View any information that the user is able to view.
Modify any information that the user is able to modify.
Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

## Team summary (ideborah)

A Cross-Site Scripting (XSS) vulnerability is present in the Jolokia endpoint at ███████. User-supplied data is not properly sanitized before being reflected back, allowing an attacker to inject malicious JavaScript code that gets executed in the victim's browser.
