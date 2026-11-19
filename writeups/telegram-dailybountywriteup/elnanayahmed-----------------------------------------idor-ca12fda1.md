# خلل في التحكم بالوصول / IDOR في تدفق دعوة المجموعة

- **Source URL:** https://medium.com/@elnanayahmed/%D8%AE%D9%84%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%AA%D8%AD%D9%83%D9%85-%D8%A8%D8%A7%D9%84%D9%88%D8%B5%D9%88%D9%84-idor-%D9%81%D9%8A-%D8%AA%D8%AF%D9%81%D9%82-%D8%AF%D8%B9%D9%88%D8%A9-%D8%A7%D9%84%D9%85%D8%AC%D9%85%D9%88%D8%B9%D8%A9-61c693fec30e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260519143302/https://medium.com/@elnanayahmed/%D8%AE%D9%84%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%AA%D8%AD%D9%83%D9%85-%D8%A8%D8%A7%D9%84%D9%88%D8%B5%D9%88%D9%84-idor-%D9%81%D9%8A-%D8%AA%D8%AF%D9%81%D9%82-%D8%AF%D8%B9%D9%88%D8%A9-%D8%A7%D9%84%D9%85%D8%AC%D9%85%D9%88%D8%B9%D8%A9-61c693fec30e
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13507 (id 13507)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken Access Control / IDOR in Group Invitation Flow

{وَآتَاكُم م كُلِّ مَا سَأَلْتُمُوهُ ۚ وَإِن تَعُدُّوا نِعْمَتَ اللَّهِ لا تُحْصُوهُ ۗ }

Broken Access Control / IDOR in Group Invitation Flow

During a security assessment of a Study Groups feature, I discovered a Broken Access Control vulnerability affecting the invitation acceptance mechanism.

The issue was related to improper authorization handling in a request responsible for accepting group invitations. By manipulating the `userId` parameter, it was possible to perform actions on behalf of other users without proper authorization.

Vulnerability behavior:

• Users could be added to groups without explicit consent

• In some cases, the system ignored the user’s actual decision (Accept / Reject)

• Reusing an invitation link could result in users being re-added to a group after leaving it

Classification:

Broken Access Control (BAC) > Insecure Direct Object Reference (IDOR)

Security impact highlights:

• Weak server-side validation of user identity

• Lack of proper binding between user session and decision logic

• Trusting client-controlled parameters for sensitive operations

Key takeaways:

• Business logic flaws can be more impactful than traditional technical vulnerabilities

• Client-side input should never be trusted for authorization decisions

• Invitation-based features require strict access control enforcement

• IDOR remains one of the most common and impactful API security issues

This finding reinforced my understanding of authorization flaws and how subtle logic issues in backend workflows can lead to serious access control bypasses.

#BugBounty #CyberSecurity #AppSec #IDOR #API #WebSecurity
