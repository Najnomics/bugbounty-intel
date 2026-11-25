# How I Manipulated One Parameter to Love Another User’s Comment -IDOR & Broken Authorization

- **Source URL:** https://medium.com/@ankitrathva/how-i-manipulated-one-parameter-to-love-another-users-comment-idor-broken-authorization-5cd5a67a13cd
- **Fetched from:** https://medium.com/@ankitrathva/how-i-manipulated-one-parameter-to-love-another-users-comment-idor-broken-authorization-5cd5a67a13cd?source=rss-d479b91985ef------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14878)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ankit Rathva aka Gujarati Hacker / Wed, 26 Aug 2026 16:28:17 GMT

I am Ankit Rathva aka Gujarati Hacker and i am a student of MCA 2nd year, I am an ethical hacker and security researcher with a passion for finding logic, authorization, and data-integrity flaws in web applications. As a bug bounty hunter and red teamer, he combines hands-on testing, forensic analysis, and careful disclosure to help teams fix impactful issues while protecting users. He publishes clear, developer-friendly writeups and practical mitigation advice — connect to follow his work or collaborate on security research.

**Connect with me:** [https://linkedin.com/in/ankitrathva](https://linkedin.com/in/ankitrathva)

**How a simple comment interaction turned into a High-Severity authorization vulnerability**

While hunting for vulnerabilities on a web application, I was testing its **Community** functionality.

At first, everything appeared to work as expected. Users could create comments and interact with other users’ comments through actions such as replying, upvoting, and downvoting.

However, while testing the interaction functionality, I noticed something interesting.

There was a **“love”** action associated with comments, but the application behaved differently depending on who owned the comment.

That difference made me curious.

So I started testing whether the restriction was actually being enforced by the backend — or whether it was only a frontend restriction.

And that led to an interesting **IDOR + Broken Authorization + Business Logic** vulnerability.

The application had a **Community** section where users could post comments.

Users could interact with comments in several ways:

During my testing, I noticed an important behavior:

*A user could not use the* ***love*** *functionality on another user’s comment through the normal frontend interface.*

This immediately raised a question:

**Was the backend actually preventing this action, or was the frontend simply hiding/restricting it?**

Whenever I see a restriction implemented in the UI, I like to check whether the server independently enforces the same authorization rule.

So I started testing.

Instead of relying only on what the frontend allowed me to do, I performed the legitimate **love** action on a comment belonging to my attacker account.

I intercepted the request using an HTTP interception proxy.

The request contained a parameter called: comment\_ids

This parameter identified the comment on which the action was being performed.

At this point, I had a simple hypothesis:

*What happens if I replace the comment identifier belonging to my account with the identifier of another user’s comment?*

This is a common authorization-testing technique.

The important thing is that I wasn’t changing my authentication credentials.

I was simply testing whether the server would verify that the authenticated user was authorized to perform the requested action against the supplied object.

The behavior became even more interesting when I checked the victim account.

The victim’s own comment displayed:

***“You loved this”***

But the victim had never performed that action.

The application had incorrectly attributed the interaction to the victim.

In other words, I had been authenticated as the attacker, but the resulting state was presented as though the victim had performed the interaction.

This made the vulnerability significantly more interesting than a simple ability to manipulate a comment identifier.

I performed another check.

After the unauthorized love action was applied, the victim couldn’t simply dislike or revert the interaction from their own account.

This meant the attacker could cause a persistent change to another user’s interaction state.

The issue therefore affected **data integrity**, not merely what was displayed temporarily in the browser.

The core problem wasn’t simply that the comment ID could be changed.

The bigger issue was that the backend failed to answer an important security question:

***Is this authenticated user actually allowed to perform this action on this particular comment?***

Authentication answers:

**“Who are you?”**

Authorization answers:

**“Are you allowed to do this?”**

The application correctly knew who I was, but it failed to properly enforce whether I was authorized to perform this specific action against another user’s comment.

The company investigated the report and **accepted the vulnerability as High severity**.

I was rewarded with:

For me, this was another reminder that sometimes a vulnerability isn’t hidden behind a complicated exploit.

Sometimes, it’s hidden behind a single parameter.

This finding started with a relatively simple question:

**“Why can’t I love another user’s comment?”**

Instead of stopping at the frontend behavior, I inspected the underlying request and tested whether the backend enforced the same restriction.

Changing a single object identifier was enough to cross an authorization boundary.

The vulnerability ultimately demonstrated how **IDOR, broken authorization, and business-logic flaws can overlap**.

For bug hunters, this is a good reminder:

***Don’t just test what the application lets you do. Test what the backend actually allows you to do.***

Sometimes, the most interesting bugs are hiding behind the parameters we normally overlook.

If you found this write-up useful, feel free to share it with other security researchers.

I’ll be sharing more of my bug bounty findings, methodologies, and lessons learned from real-world web application security testing.

**Keep learning. Keep testing. Keep hacking responsibly. 🔐**
