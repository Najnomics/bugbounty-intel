# IDor Bug Bounty

- **Source URL:** https://medium.com/@ryuzakiryuga31/idor-bug-bounty-cfda034be7d6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230606055938/https://medium.com/@ryuzakiryuga31/idor-bug-bounty-cfda034be7d6
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2894 (id 2894)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
The vulnerability is to display customer-specific data that cannot be displayed

In principle The phone was used to extract the vulnerability and a phone application was used to find out the request called HTTP Canry

This is the application interface

The company to work on is an Egyptian software company

Let's get started. While opening the application and working on it, I found a link as an example

`http://10.10.10.10:8081/hr/salry=months=UID=1214`
After entering the link, I found the username and salary for the month Approved and rejected vacations

The information is displayed in changing the value of the person's identity if the application does not allow it to be displayed
