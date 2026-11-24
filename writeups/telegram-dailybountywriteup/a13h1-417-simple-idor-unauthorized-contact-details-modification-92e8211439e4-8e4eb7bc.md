# 417$ Simple IDOR

- **Source URL:** https://medium.com/@a13h1/417-simple-idor-unauthorized-contact-details-modification-92e8211439e4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231231181822/https://medium.com/@a13h1/417-simple-idor-unauthorized-contact-details-modification-92e8211439e4
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4853 (id 4853)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 417$ Simple IDOR: Unauthorized Contact Details Modification

--

This article is about a bug which i recently found in one private program where an attacker can modify or add contact details for other users integrations that are applying to go public without proper authorization . Learn about the issue, its potential impact, and the steps taken to address this security concern.

**Understanding Target**


Exapier(Virtual name of BBP) is a product that allows end users to integrate the web applications they use**.** Developer.exapier.com serves as a platform for developers to create and manage their applications, providing a space for collaboration and integration. It plays a crucial role in the Exapier ecosystem, allowing developers to publish and manage their apps seamlessly.

**Bug Description**


Recently, i found IDOR in developer.exapier.com platform, specifically in the functionality related to Publishing Contact Details. It enables an attacker to tamper with or insert contact details on another user’s account without the necessary authorization.

## Steps to Reproduce:

To illustrate how this vulnerability works, here’s a step-by-step breakdown:

1. The attacker logs into developer.exapier.com using their own account.
2. Using their account, the attacker initiates a PATCH request to a specific endpoint, modifying the contact details.
3. The request payload includes changes to the “id” field, replacing it with the victim’s ID, and provides the updated contact information.
4. The attacker receives a 200 OK response, indicating that the request was successful.
5. The victim, upon reviewing their publishing contact details, discovers that the information has been altered by the attacker.

**The Bounty**


The security team at Exapier acknowledged and rewarded a bounty of $417 for the discovery of an Insecure Direct Object Reference (IDOR) vulnerability. Although the impact was categorized as Medium severity, the team provided insights into the specific context. The vulnerability was limited to Integrations applying to go public, which undergo manual review by the team.So the bounty is lower than expected to this kind of issue.

*Leave some clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting findings.*


*Find me on Twitter: @a13h1\_*


# Thank you everyone

Keep Supporting, Keep Clapping, Keep Commenting.
