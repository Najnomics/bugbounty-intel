# Reflected XSS via File Upload on Sony

- **Source URL:** https://dr34m14.medium.com/reflected-xss-via-file-upload-on-sony-0aa0f3295216?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905081954/https://dr34m14.medium.com/reflected-xss-via-file-upload-on-sony-0aa0f3295216?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10004 (id 10004)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS via File Upload on Sony

Hi,

This is my **first writeup**! I discovered a **reflected XSS vulnerability** via the **file upload** feature on a Sony subdomain. This vulnerability allowed JavaScript payloads to be executed through a crafted file upload, posing serious risks such as session hijacking and unauthorized actions.

**Main application(target):**

[https://\*.\*.\*.sony.com/#/PATH1/PATH2](https://web.archive.org/web/20250905081954/https://*.*.*.sony.com/#/PATH1/PATH2)

How I Found the Subdomain

I used the **Project Discovery Chaos database** ([https://chaos.projectdiscovery.io/](https://web.archive.org/web/20250905081954/https://chaos.projectdiscovery.io/)) to enumerate Sony subdomains. To identify live and responsive subdomains, I filtered the results using the `httpx-toolkit` as follows:

**Initial filtering to find alive hosts:**

`httpx-toolkit - silent`
**Further filtering to keep only HTTP 200 OK responses:**

`httpx-toolkit --silent -sc | grep 200`
This process helped me identify a live Sony subdomain hosting the vulnerable application where I performed the file upload test.

## Vulnerable Endpoint

Once a file is uploaded through the form, it becomes publicly accessible:

`https://*.*.*.sony.com/uploads/PATH1/bnUnlZzw_js_injected_xss.pdf`
This file, when accessed, executes the injected script due to improper output encoding.

## XSS Payload File

You can view the crafted XSS payload file used in this test at:

👉 [https://dr34m14.github.io/dr34m14/payloads/js\_injected\_xss.pdf](https://web.archive.org/web/20250905081954/https://dr34m14.github.io/dr34m14/payloads/js_injected_xss.pdf)

## Reproduction Steps

1. Go to: [https://*.*.*.sony.com/#/PATH1/PATH2](https://web.archive.org/web/20250905081954/https://*.*.*.sony.com/#/PATH1/PATH2)
2. Complete all required form fields.
3. Click **Continue** to proceed.
4. Upload the crafted PDF: `js_injected_xss.pdf`
5. 5.Retrieve the public URL of the uploaded file.
6. Share the link with a target — the payload will trigger upon visiting.

Proof of Concept

## Payload Location

The XSS was triggered by unsafe reflection of **user-supplied input (e.g., filename or metadata)** in the server’s response. The content was served directly in a way that allowed the injected script to execute.

## Impact

- Reflected XSS on a **Sony-owned subdomain**
- Payload executes from the uploaded file’s URL
- Could lead to:
- **Account takeover** via session theft
- **Phishing attacks**
- **Unauthorized actions** in the context of the victim’s session

## Reward

Sony acknowledged the issue and sent me **swags** as a thank-you.

Thanks for reading! This is my first writeup and I hope it helps raise awareness about secure file handling. Stay safe and happy bug hunting!

Twitter: [https://twitter.com/dr34m14](https://web.archive.org/web/20250905081954/https://twitter.com/dr34m14)

GitHub: [https://github.com/dr34m14](https://web.archive.org/web/20250905081954/https://github.com/dr34m14)

HackerOne: [https://hackerone.com/dr34m14](https://web.archive.org/web/20250905081954/https://hackerone.com/dr34m14)

LinkedIn: [https://linkedin.com/in/dr34m14](https://web.archive.org/web/20250905081954/https://linkedin.com/in/dr34m14)
