# BAC

- **Source URL:** https://medium.com/@kiwi.bounty22/bac-unauthorized-email-sending-a38a07bd74f0
- **Fetched from:** https://medium.com/@kiwi.bounty22/bac-unauthorized-email-sending-a38a07bd74f0?source=rss-cedc0a6696e6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14919)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Saad / Mon, 21 Sep 2026 05:04:18 GMT

Date: 9/21/2026

After 3 weeks of testing on single SaaS VDP program on Bug crowd, I discovered that a lower privileged user who did not have access to the particular messaging feature and send emails to anyone was able to perform that action

I created 2 accounts User a and User b

User a was admin invited User b to the team and gave User b lowest permittion possible and without access to the relevant feature.

that messaging feature was unavailable through the User b UI

I captuerd this request with admin (User a)

POST /api/groups/\[REDACTED\]/messages/email/

Changed cokkies with User b cokkie and sent the following request:

POST /api/groups/\[REDACTED\]/messages/email/ HTTP/2

Host: \[REDACTED\]

{

“comment”: “[https://e](https://example.com)vil.com",

“email\_addresses”: \[

“victim[@gmail.com](mailto:attacker@example.com)”

\]

}

The server responded with:

HTTP/2 200 OK

the email was sent to the victim

The received email contained:

This indicates that authorization was not properly enforced at the server-side endpoint.

I got this bug after testing the programm for 3 weeks complettle understanding each and every permisttions also programm was public and old like 2017 with 713 reports

the report was p3 dupe :(

wait for my next logic flaw writeup on the same programm whcih is still under review
