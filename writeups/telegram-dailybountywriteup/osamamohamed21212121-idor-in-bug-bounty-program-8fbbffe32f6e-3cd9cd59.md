# IDOR in Bug Bounty Program

- **Source URL:** https://medium.com/@osamamohamed21212121/idor-in-bug-bounty-program-8fbbffe32f6e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250716121857/https://medium.com/@osamamohamed21212121/idor-in-bug-bounty-program-8fbbffe32f6e
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7259 (id 7259)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR in Bug Bounty Program

Hello, my name is Osama Mohammed, and I am a penetration tester and bug hunter.

A vulnerability has been discovered on the targeted website that allows users to delete documents without permission by exploiting the IDOR (Insecure Direct Object Reference) vulnerability. This vulnerability occurs because the website does not properly verify user permissions when processing document deletion requests. Additionally, the risk is compounded by the failure to verify the important security header “Authorization” on the server side.

Detailed Description:

This vulnerability allows an attacker to delete documents belonging to other users by exploiting a weakness in user authentication. The website relies on two parameters stored in user cookies to identify the document and authorize the deletion, but does not properly verify that the user attempting to delete the document has the appropriate permissions.

Relying on these cookie parameters poses a security risk, as they can be exploited if an attacker obtains these cookies (via attacks such as XSS or social engineering). Even though direct access to them is currently not possible, this vulnerability poses a significant risk.

I was also able to delete the Authorization header successfully and the server did not object to this.

The two parameters through which I was able to delete other people’s documents are

**grauth**

**csrf-token**They were also fixed values that are never changed for the user

This is a greater risk because if I get them, I can delete any file for the victim

After I get the ID of his file

# My journey to find IDOR Vulnerability:

I created two accounts on the infected site for example

ttps://app.eaxmple.com/

Then I created a document on the victim’s account so that I could delete it with the attacker’s account

I deleted a document on the hacker’s account and intercepted the requests using Burp Suite or a similar tool.

Then I extracted the grauth and csrf-token parameters from the cookies of the victim’s account

Then I added the values of the two parameters with the document identifier and deleted the document. In the hacker’s account that was obtained from

the victim’s account

The deleted document will be moved to the “Recycle Bin” folder and you can delete it permanently by following the same steps

Done

Thank you for watching.

“Don’t hesitate if you have any questions about anything.

I will leave my account for contact.

Follow me.”

*LinkedIn Profile :*
