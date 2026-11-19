# The correct approach to testing for privilege escalation bugs...❕❗

- **Source URL:** https://medium.com/@mahdisalhi0500/the-correct-approach-to-testing-for-privilege-escalation-bugs-d03bd9281a3e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250122211145/https://medium.com/@mahdisalhi0500/the-correct-approach-to-testing-for-privilege-escalation-bugs-d03bd9281a3e
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8555 (id 8555)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The correct approach to testing for privilege escalation bugs...❕❗

إِنَّ اللَّهَ وَمَلَائِكَتَهُ يُصَلُّونَ عَلَى النَّبِيِّ ۚ يَا أَيُّهَا الَّذِينَ آمَنُوا صَلُّوا عَلَيْهِ وَسَلِّمُوا تَسْلِيمًا

Salam Alaykum, guys! I hope you are doing well. Today, inshallah, I will explain my approach to privilege escalation bugs (with a faster approach and creativity).

## **Privilege escalation bugs**

happen when a user can do things they shouldn’t be allowed to do.

- **Example 1:** A regular user changes their role to “admin” using a trick like modifying requests.
- **Example 2:** A user accesses another person’s data without permission.

These bugs happen because the system doesn’t check permissions properly.

## Type of Privileges

**Privilege Escalation (Horizontal):**This happens when a user gains access to another user’s data or actions at the same level.

**Example:** A user accesses another user’s account by guessing or changing the user ID.

**Privilege Escalation (Vertical):**This happens when a user gains higher-level access than they should have.

**Example:** A regular user becomes an admin by changing their role or bypassing checks. ( thank you chat-Gpt 🙃 )

Now, after understanding the types of privilege escalation, let’s explain how to look for them more quickly. Sometimes, I find bugs without any tools or complex thinking, just by following this methodology:

## **Horizontal ⬆**⬆⬆⬆⬆⬆⬆

We have agents and admin roles in a SaaS application. The best tip here is to check for an important thing: **if there is strong sync with cookies**.

I mean, if the owner changes the role from admin to agent, does this change happen immediately? This tip is related to the user interface. Why? Because if the cookies need a refresh to sync with the owner’s change, you can skip a lot of hard work.

Okay, let’s return to the scenario:

We have an organization admin who invites me as an admin. Now, my user interface shows a lot of requests. Then the admin changes my role.

If the page doesn’t refresh automatically (causing delays in syncing the role), this can create many opportunities. Sometimes, when you click on certain functions, they’ll still work because the role change hasn’t synced yet.

Now, just open those sections, try the functions, see who still gives you access, and get your bounty! 😛❤

## **Vertical ⬅➡**

After getting your bounty, you start asking yourself how to test vertical privilege escalation faster.

Okay, do the same stuff, but now open Burp Suite to capture sensitive requests and send them to Repeater (focus on `GET` requests).

Now, try deleting users or modifying actions through the user interface, and send some requests through Burp.

# But remember…

This approach doesn’t work for all applications. Some applications have well-implemented cookies, and sometimes you’ll notice that your target secures requests by making them expire or adding other protections.

However, this approach gives you an idea about the type of application you’re dealing with. The most helpful bugs, though, come when you work hard, take the time to understand your target, and break its logic.

Take your time to understand the target. Use the application like a normal user, analyze its behavior, and build your plan to hunt effectively.

**References:**

- Fares Waild: I actually got this methodology after watching this video: [https://www.youtube.com/watch?v=x98-sPJ\_s1g](https://www.youtube.com/watch?v=x98-sPJ_s1g).
- Ahmed Najah: [https://www.youtube.com/watch?v=Dwtg9LSmfIo&t=2088s](https://www.youtube.com/watch?v=Dwtg9LSmfIo&t=2088s).
- [Bugs Ar](https://www.youtube.com/@BugsAR) : [https://www.youtube.com/watch?v=FjiCbidb8v8&t=9s](https://www.youtube.com/watch?v=FjiCbidb8v8&t=9s)
