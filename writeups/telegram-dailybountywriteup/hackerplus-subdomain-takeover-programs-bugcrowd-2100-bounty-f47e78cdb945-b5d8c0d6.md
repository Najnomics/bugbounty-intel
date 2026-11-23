# Subdomain TakeOver Programs BugCrowd $2100 Bounty

- **Source URL:** https://medium.com/@HackerPlus/subdomain-takeover-programs-bugcrowd-2100-bounty-f47e78cdb945?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250604080313/https://medium.com/@HackerPlus/subdomain-takeover-programs-bugcrowd-2100-bounty-f47e78cdb945
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8612 (id 8612)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Subdomain TakeOver Programs **BugCrowd** $2100 Bounty

Welcome to **HackerPlus**! 🌐💻

We specialize in **pentesting** and **Bug Bounty** to enhance the security of web applications. We share reports on past vulnerabilities and spread knowledge to help the cybersecurity community grow.

**HackerPlus — Together, we make the digital world safer.** 🛡️

# Subdomain TakeOver Programs HackerOne $2100 Bounty

Let me explain what was the bug, it kind of subdomain takeover type of bug, let me explain what was that and how I reported.

While exploring the private program, I found some of the endpoints where you have option to change/edit the unique business URL, so I tried and changed the URL 2–3 times and I noted all the URLs I changed, now it was the time to check that program allows me to takeover the recently deleted/ changed business URL. I created another account and used same old deleted business URL in this another account and you know what it was claimable. So this was the kind of low level bug, I tried to increase impact of this bug by something else related to it.

So I started with subdomain enumeration with some available github tools, I grabbed almost 500 domains, copied and opened all in my browser, it tooks me 2–3 min to open all links. Now I started checking all the links manually, I got 404 or 403 pages, tried to bypass but not possible then I found some crazy unique business URLs which was deleted before but I found while doing subdomain enumeration, so it means they all are claimable.

Now I created one more account and tried all the claimable unique business URL which I found during subdomain enumeration and you know what I can claim all the URLs I stopped and reported and Why it was unexpected reward for me ? Because they was not having any mechanism that we can claim the unique business URL instant or after few days or not ! Also there is no confirms email that we can claim same or old username till few days then it will be free to claim by anyone. So I didn’t expected any reward, then also I reported and I got bounty. So here is how I reported.

I can’t reveal program name so I’m using TARGET

# Summary

During subdomain takeover, I found some of the subdomain whose unique URL are claimable, even if it is recently deleted or old. This will leads to business url takeover of the business or organisation.

# Steps To Reproduce :

1. Signup and login to target[.com](https://once.deputy.com/my/#edit_company/8ea5760e-d07f-416d-83fa-f9b1877725a4/edit-org-general)
2. Create a company then navigate edit company unique URL and Business name from Edit Business
3. From here [https://](https://once.deputy.com/my/#edit_company/8ea5760e-d07f-416d-83fa-f9b1877725a4/edit-org-general)target[.com/my/#edit\_company/\<business\_id>/edit-org-general](https://once.deputy.com/my/#edit_company/8ea5760e-d07f-416d-83fa-f9b1877725a4/edit-org-general)
4. Now click on Unique URL, and edit the unique URL with old URL or any subdomain you found during enumeration.
5. You can see you can procceed after this step, it means that URL is claimed by you.
6. Also if someone delete the same unique URL, then anyone can claim it instantly.

I found some domain’s while doing subdomain enumeration, there are lots of target.com, na.redacted.com, etc all are claimable.

# Impact:

It seems that the use of tokens and access checks will prevent this issue from causing a large amount of harm. It was basic subdomain takeover.

The Vulnerability has been sent to **Bugcrowd**.

Programs : **Bugcrowd** BBP

Bounty : $2100

Note :

The HackerPlus team has created a training camp that will teach you the field from scratch to professionalism. You will get a job with us after the training camp ends, and your level will be professional. After the training camp ends, you will be on real programs on the HackerOne website. You will share a lot of information from professional people in the field of Bug Bounty.

Contact us on Telegram : [https://t.me/HackerPllus](https://t.me/HackerPllus)

Follow us on X Platform : [https://x.com/HackerPllus](https://x.com/HackerPllus)

We Hope You Benefited

Team HackerPlus+
