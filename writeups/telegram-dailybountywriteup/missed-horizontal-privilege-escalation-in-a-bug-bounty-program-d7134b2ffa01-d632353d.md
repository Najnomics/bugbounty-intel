# Missed Horizontal Privilege Escalation in a Bug Bounty Program!

- **Source URL:** https://spider7.medium.com/missed-horizontal-privilege-escalation-in-a-bug-bounty-program-d7134b2ffa01?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502102227/https://spider7.medium.com/missed-horizontal-privilege-escalation-in-a-bug-bounty-program-d7134b2ffa01
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9520 (id 9520)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Missed Horizontal Privilege Escalation in a Bug Bounty Program! 😭

Hello everyone, I’d like to share my disappointing experience with a bug bounty adventure I just had. Brace yourselves, this is a story about finding a cool bug but having it patched before I could report it. IYKYK!

**How It Started**

I was exploring a bug bounty program on HackerOne. As a newbie, I was particularly interested in the “manage family account” feature that had owner and member roles. As the name suggests, the owner has full privileges — they can invite and remove members, etc. Members, on the other hand, can only leave the family.

My brain immediately thought, “Hmm, this has great potential for privilege escalation!” Logically, members shouldn’t be able to perform actions that are reserved for owners.

**The Experiment Begins**

With great enthusiasm, I set up 2 accounts for testing:

- Owner account (with full privileges)
- Member account (with limited privileges)

**Then I started testing:**

1. Intercepted a request from the owner account while inviting a new member
2. Saved that request
3. Replaced the cookie in the request with the cookie from the member account
4. Resent the modified request

And guess what? IT WORKED! 🤯

The member account, which shouldn’t have been able to invite people, could invite new members! Classic horizontal privilege escalation! I was extremely excited about finding a legitimate vulnerability.

# The Plot Twist

When I tried to test again and document it for my report, suddenly…

`{"data":{"householdShareInviteWithDetail":{"id":"ccb54c2c","errorTypes":["notOwner"],"viewSection":{"id":"users_response_backed:9d5866af:household_invite_error:5390a9d3","descriptionString":null,"ctaString":null,"titleString":null,"__typename":"UsersResponseBackedHouseholdInviteErrorSection"},"__typename":"UsersHouseholdInviteErrorResponse"}}}`
Darn! An error appeared saying “notOwner”! Previously there was no such validation. It seems I tested too much until their security team detected it and patched it on the spot 💀

# Valuable Lessons

From this disappointing experience, I learned several things:

1. When you find a bug, **DOCUMENT IT IMMEDIATELY** (screenshots, video, request logs) before testing further
2. **Don’t delay reporting!** As soon as you’re confident you’ve found something valid, report it
3. Don’t repeat the same request too many times in a short period as it might trigger their alert system
4. Timing is everything in the bug bounty world

# For Fellow Newbies

For those of you who are also just starting in the bug bounty world, don’t give up if something like this happens. Consider it an experience and validation that you actually have the skills to find bugs.

Sometimes we need to be reminded the hard way that in bug bounty, **“The early bird gets the worm.”** 😎

I’m still very much a newbie, and although I didn’t get a bounty this time, at least now I know my hunting skills are on the right track. Next time I’ll be luckier! 🚀

By the way, for privilege escalation, keep focusing on features that involve access control and permissions. And don’t forget to always test all endpoints, not just those visible in the UI.

That’s my story. Keep hunting, and see you on the leaderboard! ✌️

#BugBounty #PrivilegeEscalation #HorizontalPrivilegeEscalation #InfoSec #HackerLife #BugHunting
