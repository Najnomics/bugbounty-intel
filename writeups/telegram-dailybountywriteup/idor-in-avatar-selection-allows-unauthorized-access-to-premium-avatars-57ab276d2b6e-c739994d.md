# IDOR in Avatar Selection Allows Unauthorized Access to Premium Avatars

- **Source URL:** https://mmnahian.medium.com/idor-in-avatar-selection-allows-unauthorized-access-to-premium-avatars-57ab276d2b6e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250503060401/https://mmnahian.medium.com/idor-in-avatar-selection-allows-unauthorized-access-to-premium-avatars-57ab276d2b6e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9305 (id 9305)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR in Avatar Selection Allows Unauthorized Access to Premium Avatars

**Hey everyone!**

Its mmnahian, During one of my recent bug bounty hunting public VDP program, I came across a vulnerability in an avatar selection feature of a web application. This bug allowed users at the **“New Level”** to bypass restrictions and use **premium avatars** that were meant only for higher-level users.

Here’s a breakdown of how I found it, exploited it, and why it matters.

# 🧭 Bug Discovery

While exploring the profile customization section of the app, I noticed something interesting.

“20 more icons will become available when you reach Beginner Level.”


I started examining how avatars were loaded. I dragged one of the avatar images into a new browser tab and noticed the following endpoint format: /library/img/avatar/58-m.png

The number **58** looked like an internal ID. I wondered: what would happen if I just changed that number?

So I modified the URL to: /library/img/avatar/61-m.png

I noticed that this particular avatar wasn’t available to new-level users because it was not in the allocated avatars for **new level** user.

This led me to believe one of two things:

— It was reserved for higher-level users

— Or it would only become available after leveling up from new level status.

then after that I selected an avatar that was allocated for me and clicked “save” and intercepted that request.

While inspecting the request, I noticed a parameter `avatar_id=58`, which matched the avatar I had seen earlier at the endpoint `/library/img/avatar/58-m.png`. I changed the value to `avatar_id=61` and forwarded the request. and **BOOM!**

No error. No restriction. The avatar updated successfully.

I viewed my profile — and sure enough, the **restricted premium avatar** was now showing, even though my account was still at the “New Level.”

# 💥 Impact

This vulnerability exposed a classic **authorization flaw**:

- Any user, regardless of level, could apply premium avatars just by modifying a parameter.
- It broke the platform’s **progression system**, reducing the value of level-based rewards.
- If avatars were tied to reputation or extra features, it could lead to **privilege escalation**.

This was a classic case of **IDOR meets broken access control**. A simple parameter change gave me access to restricted content — all because the backend trusted the client a little too much.

The lesson?

**Always validate permissions on the server side.** If your system has rules, enforce them where it matters.

Hope you found this write-up helpful! Until next time,

**happy hacking!** 🎯
