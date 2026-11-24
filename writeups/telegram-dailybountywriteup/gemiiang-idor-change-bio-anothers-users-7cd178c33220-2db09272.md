# IDOR CHANGES DESCRIPTION ANOTHERS USERS/COMPANY

- **Source URL:** https://medium.com/@GemiIang/idor-change-bio-anothers-users-7cd178c33220?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143054/https://medium.com/@GemiIang/idor-change-bio-anothers-users-7cd178c33220
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2555 (id 2555)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR CHANGES DESCRIPTION ANOTHERS USERS/COMPANY

Hello all.

Gemilang in here.

today i find bug idor to change bio anothers users. so in this case i will caled they as redacted.com because my report should prosses to fixed.

how i found this bug, basically it’s very simple but the impact is very severe. this is the second idor bug i found, in this case i can change the post/advertisement of another user. the id is very easy to guess.

so let’s get right to it.

when I’ve created an advert I get parameters like this [www.redacted.com/edit?postid=488587](http://www.redacted.com/edit?postid=488587)

I immediately thought that maybe here I would get an idor! then I created a second account and did the same thing. on the second account I got a postid like this [www.redacted.com/edit?postid=488590](http://www.redacted.com/edit?postid=488590)

then what if I change the postid into my second account, until it becomes like this. here I only change the input\_2 parameter.

So, what do I get? yup. response success 200 ok. that means I have successfully changed the input\_2 of my second account.

My message is, focus on one company and try all the features they have. because vulnerabilities are everywhere, we just haven’t found them and tried.
