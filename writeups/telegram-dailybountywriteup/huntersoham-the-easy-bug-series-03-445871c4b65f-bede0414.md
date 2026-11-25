# The Easy Bug Series | #03

- **Source URL:** https://medium.com/@huntersoham/the-easy-bug-series-03-445871c4b65f
- **Fetched from:** https://systemweakness.com/the-easy-bug-series-03-445871c4b65f?source=rss-c501c19c2da6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14925 (id 14925)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Soham D. Jadhav / Sun, 27 Sep 2026 05:49:31 GMT

Hello everyone 👋

Welcome to my 15 days low hanging fruits series, where i share my simple methodologies to find interesting bugs that every beginner should hunt.

In today’s article, I will explain **Password Reset Link Reuse After Successful Password Reset**

**What’s the issue basically?**

Whenever we go to the forget password function, we enter our email and then we get a unique password reset link/token.

Normally, after successfully changing the password, the reset link should not work again.

But what if i use the old password reset link and can able to change the password from that used link then?

Let’s see how we can test this.

**Reproduction:**

**Step 1:** Go to the Login page and click on forget password button.

**Step 2:** Enter your email address for getting the link.

**Step 3:** You will get reset link in your mail copy that reset link in notepad and open that link.

**Step 4:** Change the password with that link.

For ex., Old password → New password

**Step 5:** Try to open the same password link again.

**Step 6:** Check whether the application still allows us to change the password from that same link.

If the old password reset link **is still valid** and allows another password change from that same link, this may indicate the **Password Reset Link Reuse** vulnerability.

**Why is this a problem?**

Imagine an attacker somehow gets access to the reset link.

The original user notices something **suspicious** and changes their password using the password reset process.

But if the old reset link is still valid, the attacker can use the same link again and reset the password.

So changing the password doesn’t completely invalidate the previously issued reset link.

**Impact:**

Depending on the implementation, this can lead to :

The severity of this vulnerability depends on how long the old token remains valid, whether it can be reused multiple times, and what an attacker can achieve with this.

This issue can be considered **P4 or P3** depending on the **actual impact** and the program’s severity guidelines.

**How should it be fixed?**

After successful password reset, application should:

That’s it for **Day 3** 🚀

A simple test, but while testing password reset functionality, don’t just check whether the reset link works or not.

Also check **what happens to the same link after the password has already been changed.**

See you in the next part where we will explore another interesting finding.

Let’s connect

Happy Hunting! 🐞🔍

#BugBounty #WebSecurity #CyberSecurity #Pentesting #VAPT #BugBountyTips

[The Easy Bug Series | #03](https://systemweakness.com/the-easy-bug-series-03-445871c4b65f) was originally published in [System Weakness](https://systemweakness.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
