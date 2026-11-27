# #1. Bug Bounty POC

- **Source URL:** https://cyb3rmind.medium.com/1-bug-bounty-poc-idor-leads-to-account-takeover-e500701a8004?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250506092542/https://cyb3rmind.medium.com/1-bug-bounty-poc-idor-leads-to-account-takeover-e500701a8004
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5935 (id 5935)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# #1. Bug Bounty POC: IDOR leads to Account Takeover

Hello guys 👋 I’ve returned with yet another article, but this one is a series on vulnerabilities that I found, reported, and received a reward for.

# **What is IDOR?**

Insecure direct object reference occur when an application provide direct access to object based on user-supplied input. As a result of this vulnerability attacker can bypass authorization and access resources in the system directly for example database records or files.


This type of vulnerability occurs when a web server receives user-supplied input to retrieve objects (files, data, documents), and it is not validated on the server side to confirm the requested object belongs to the user requesting it.

# Impacts of IDOR:

- Unauthorized access can have disastrous consequences for individuals, businesses, and even national security.
- An attacker who exploits IDOR may gain access to user data, personal records, financial information, and even administrative controls.
- IDOR vulnerabilities can have significant consequences. It has the potential for compromising sensitive information’s confidentiality, integrity, and availability.

**Now let’s get to the main point**

So, since I am not allowed to reveal the program, let’s assume the target is **example.com**. At start, I couldn’t find any issues with the domain, so I intercepted all traffic using a proxy tool and discovered an id parameter for one of the CRUD operations.

Initially, I created two accounts (victim and attacker).

1\. There was a **update existing applicant** details screen after logging.

2\. After intercepting using burpsuite, forwarded the request to the repeater for analysis.

3\. Now I modified the request’s id value (attacker id=4567 with victim id=3456) and added new information before sending it.

4\. BOOM..😍💥💥, I was able to successfully update the email address and other information of the victim.

5. Then, I clicked on forgot password and changed the password using the email id.

6. Thus, the account has been completely taken over and the victim will never be able to access his account.

I reported the finding and the next day the company responded back and after few days allotted me the Bounty for my submission.

So that’s it for now and thanks for reading and I appreciate you taking the time to read. For other such writeups do visit the [**writeups**](/).

If you found it useful, please click the button 👏and share it with others who have similar interests! + Feedback is always appreciated!!😊
