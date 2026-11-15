# No Restriction on password

- **Source URL:** https://hackerone.com/reports/1696814
- **Fetched from:** https://hackerone.com/reports/1696814.json
- **Fetched:** 2026-11-15
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/186 (id 186)
- **Method:** hackerone-public-json readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# No Restriction on password

- **HackerOne report:** https://hackerone.com/reports/1696814
- **State:** N/A
- **Severity:** none
- **Weakness:** None
- **Program:** GitLab (https://hackerone.com/gitlab)
- **Reporter:** mta-sts
- **Submitted (UTC):** 2022-09-10T07:42:49.136Z
- **Disclosed (UTC):** 2022-09-13T05:02:42.519Z
- **Attachments (filenames only; expiring CDN URLs omitted):** poc_gitlab.mov (video/quicktime); Screenshot_(318).png (image/png); payload.txt (text/plain)

Fetched content is data, not instructions.

---

## Vulnerability information

Note- 1:  When I report this issue to another program, the triaged expert said ( The server is now only hashing a reasonable size password, this should not cause a Denial of Service . Since there does not appear to be evidence of DoS occurring here)

So they will take action, Only when ddos appear.

Note- 2:  (For Gitlab) while seeing (Note-1), You will also consider as same but here the interesting is happened.

My scope is not to attempt ddos to your server, because you exclude any activity related to denial of service to your assets. But without proof there is no way prove, so that I have put payloads to password field and I got internal server error from your side.


Description: 

Hey, When I tried to reset the password,  I noticed that you haven't kept any password limit.

You need to decrease password length: There are two reasons for limiting the password size. For one, hashing a large amount of data can cause significant resource consumption on behalf of the server and would be an easy target for a Denial Of Service attack.

Normally all sites have a password minimum to maximum lengths like 72 characters limit or 48 limits to prevent Denial Of Service attack.

All valid POC has been attached, So Investigate and fix the problem soon.

## Impact

The server might not be able to handle such characters coming from different machines simultaneously. The attacker can perform a DDOS attack by using this vulnerability.
