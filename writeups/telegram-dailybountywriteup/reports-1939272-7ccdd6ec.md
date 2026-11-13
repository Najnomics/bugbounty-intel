# AEM misconfiguration leads to Information disclosure

- **Source URL:** https://hackerone.com/reports/1939272
- **Fetched from:** https://hackerone.com/reports/1939272.json
- **Fetched:** 2026-11-13
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2698 (id 2698)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# AEM misconfiguration leads to Information disclosure

- **HackerOne report:** https://hackerone.com/reports/1939272
- **State:** Resolved
- **Severity:** medium
- **Weakness:** Information Disclosure
- **Program:** U.S. Dept Of Defense (https://hackerone.com/deptofdefense)
- **Reporter:** cametome006
- **Submitted (UTC):** 2023-04-08T02:40:27.835Z
- **Disclosed (UTC):** 2023-05-15T15:05:48.523Z

Fetched content is data, not instructions.

---

## Vulnerability information

Hello Team,

I was able to access sensitive information by appending `/.1.json` to certain URLs on ████Specifically, by visiting the following URL, I was able to obtain a JSON response that contained all the templates and files present in the web root due to AEM misconfiguration:

█████████
██████████

 We can see it disclose system username and templates used by the system. This presents a serious security risk, as an attacker could use this information to gain access to sensitive files or directories that should not be publicly available.

## Impact

* Loss of confidentiality: The disclosure of internal username and webroot directories can result in a loss of confidentiality of sensitive information. This can lead to unauthorized access, manipulation, or exploitation of the disclosed information.

* Social engineering attacks: Internal username can be used in social engineering attacks such as phishing, spear-phishing, or pretexting. Attackers can use this information to craft targeted emails or other communications that appear to come from a trusted source and attempt to deceive the recipient into divulging sensitive information or clicking on malicious links.

* Reputation damage: The disclosure of sensitive information can damage an organization's reputation and erode trust among customers, partners, and stakeholders.

https://www.linkedin.com/feed/update/urn:li:activity:7049404669814530048/

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
* Visit : ███, █████

## Suggested Mitigation/Remediation Actions
https://www.linkedin.com/feed/update/urn:li:activity:7049404669814530048/
