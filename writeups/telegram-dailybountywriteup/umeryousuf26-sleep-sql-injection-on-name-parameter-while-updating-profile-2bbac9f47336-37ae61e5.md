# Sleep SQL injection on Name Parameter While Updating Profile

- **Source URL:** https://medium.com/@umeryousuf26/sleep-sql-injection-on-name-parameter-while-updating-profile-2bbac9f47336?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230301061731/https://medium.com/@umeryousuf26/sleep-sql-injection-on-name-parameter-while-updating-profile-2bbac9f47336
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/779 (id 779)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Sleep SQL injection on Name Parameter While Updating Profile

Hi everyone, I am an Independent Cyber Security Researcher and a Bug Bounty Hunter from Pakistan.

I recently got invited to a private program, which allowed me to be hunted on all the assets that belong to them. So, Just grab a coffee and start hunting without wasting more time.

Start with the usual recon which gives some hanging fruits but after spending an hour at Target, I found an unusual parameter response in updating the profile picture. Therefore used an SQLI sleep payload, and it slept for 5 seconds since the sleep(5). We used it again and it did work.

**Payload:** 0'XOR(if(now()=sysdate(),sleep(5),0))XOR’Z

**The vulnerable updating profile request looked like this after injecting payload through burp intruder:**

**Rewarded €500**

**Important Tip**: Do check each parameter manually.
