# Broken Access Control OWASP Top 10 (2025)

- **Source URL:** https://medium.com/@shrutishinde1319/broken-access-control-owasp-top-10-2025-the-1-web-security-risk-d843bd36ef5e
- **Fetched from:** https://medium.com/@shrutishinde1319/broken-access-control-owasp-top-10-2025-the-1-web-security-risk-d843bd36ef5e?source=rss-85fdc83f6cda------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14928)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Shruti Vijay Shinde / Tue, 29 Sep 2026 16:43:53 GMT

Hey everyone! 👋

I’ll be splitting this article into **two parts**:

Let’s get started.

**OWASP** stands for **Open Worldwide Application Security Project**.

The **OWASP Top 10** is an awareness document that identifies and highlights the ten most critical security risks in web applications. It helps developers and security professionals understand, identify, and mitigate common application security risks.

In the **2025** edition, the number one risk is:

***A01:2025 — Broken Access Control***

Before we understand what is “broken”, we need to understand two terms that people often mix up.

**Broken Access Control is a failure of authorization.** The system knows who you are, but it doesn’t properly check what you’re allowed to do.

**Broken Access Control** is a common vulnerability that happens when a web application or API uses user-supplied input to directly access internal database records without verifying whether the user has permission to see them.

Imagine you log in to a banking website and open your account statement. The URL looks like this:

https://mybank.com/statement?account=12345

Now you change the number in the URL:

https://mybank.com/statement?account=12346

And suddenly you’re looking at **someone else’s bank statement**. 😱

The application trusted the value you sent (12346) and fetched the record. It never asked: *"Does this user actually own this account?"*

That missing check is Broken Access Control.

BAC shows up in a few common forms. that are above shown with the help of an diagram

Let’s look at them one by one.

**IDOR** occurs when an application allows a user to access another user’s or a restricted resource by changing a direct reference such as an ID, number, or filename.

This is where beginners often get caught. A reference can take many forms:

Anything that points to a specific object (a user, an order, a file, an account) can be a **direct reference**. If the server trusts it without checking ownership, it is a candidate for IDOR.

Privilege escalation means a user gains access to something beyond what they were meant to have. It comes in two types.

Horizontal privilege escalation occurs when a user accesses **another user’s** resources or functionality at the **same privilege level**.

**Example:** Amit and Priya are both regular customers. Amit changes ?order\_id=700 to ?order\_id=701 and sees Priya's order details.

Same role (customer), different person’s data. Amit moved *sideways*.

Vertical privilege escalation occurs when a user accesses **another user’s** resources or functionality at a **higher privilege level**.

**Example:** Amit is a regular user. He discovers that sending a request to /admin/delete-user works, even though he isn't an admin. Amit moved *upward*.

**Forced browsing** means directly accessing a page or endpoint that you are not supposed to access, usually by guessing or manually entering its URL.

Rahul is an employee. He can normally see:

/employee/dashboard

/employee/profile

The website doesn’t show him any “Manager Dashboard” button. So Rahul thinks:

“Maybe I can’t access it.”

But instead of looking for a button, Rahul manually types this into the address bar:

/manager/dashboard

If the page loads, the application relied on **hiding the link** rather than **enforcing access control**. The page was hidden, not protected. Hiding a button is not security.

Here is a question many people ask:

***“When I change*** ***?id=01 to*** ***?id=02, I'm also guessing. Isn't that forced browsing?"***

**No.** The difference is what you are guessing:

ending it with One idea ties all of these together: **hiding something is not the same as protecting it.** Every request must be checked on the server, every time.

In **Part 2**, we’ll turn this theory into a practical checklist for testing and preventing Broken Access Control.

Thanks for reading! If this helped you, give it a 👏 and follow for Part 2.
