# Accessing unauthorized administration pages and seeing admin password - speakerkit.state.gov

- **Source URL:** https://hackerone.com/reports/1806387
- **Fetched from:** https://hackerone.com/reports/1806387.json
- **Fetched:** 2026-11-14
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2157 (id 2157)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Accessing unauthorized administration pages and seeing admin password - speakerkit.state.gov

- **HackerOne report:** https://hackerone.com/reports/1806387
- **State:** Resolved
- **Severity:** high (score 8.2)
- **Weakness:** Improper Access Control - Generic
- **Program:** U.S. Department of State (https://hackerone.com/us-department-of-state)
- **Reporter:** qualw1n
- **Submitted (UTC):** 2022-12-15T13:18:55.408Z
- **Disclosed (UTC):** 2023-03-25T13:44:22.594Z
- **Attachments (filenames only; expiring CDN URLs omitted):** image.png (image/png); image.png (image/png); image.png (image/png)

Fetched content is data, not instructions.

---

## Vulnerability information

## Summary:
- I discovered an issue referred to as no-redirect in a subdomain on state.gov.
When you enter the page, it directs you directly to the entrance. When I examined it via burp suite, it gave 302 found, but the homepage data was showing below.
When I tried it as admin, it still gave 302 found, but this time we could see the content of the admin page.
this way i was able to see admin user and normal user's info.
I was also able to perform many transactions.
uploading files, adding categories and many more.

## Steps To Reproduce:
1- Login to https://speakerkit.state.gov/
- and it will throw you to the page named "spklogin". Using the find and replace feature on burpsuite, I told it to change all requests that gave 302 found to 200 Ok, and I easily performed my operations.
You will be able to do it when you watch the video.

## Supporting Material/References:
https://hackerone.com/reports/1026146
https://hackerone.com/reports/95441

  * [attachment / reference]

{F2078131}
{F2078132}
{F2078133}

* [ poc / video]
████████

## Impact

access the admin page. unauthorized.
