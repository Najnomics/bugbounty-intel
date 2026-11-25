# The Illusion of Instant Block

- **Source URL:** https://medium.com/@yosefmostef99/the-illusion-of-instant-block-4620220283f9
- **Fetched from:** https://medium.com/@yosefmostef99/the-illusion-of-instant-block-4620220283f9?source=rss-a21460dfdabc------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14924 (id 14924)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Yosef Mostef :) / Fri, 25 Sep 2026 14:16:36 GMT

بِسْمِ اللَّهِ الرَّحْمٰنِ الرَّحِيمِ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى النَّبِيِّ الْمُجَاهِدِ الشَّهِيدِ…اللَّهُمَّ انصُرْ أَهْلَ غَزَّةَ وَفِلَسْطِينَ وَالسُّودَانَ، وَطَهِّرِ الْأَقْصَى مِنْ دَنَسِ الْيَهُودِ… أَمَّا بَعْدُ

Hey folks, I’m back after quite a long hiatus… and honestly, it’s good to be back. Oh man, I’d almost forgotten how to write writeups :’(

Anyway, enough of that. As usual, on just another random day, I was doing what I love — putting security systems to the test — and I stumbled on a vulnerability built on a familiar idea, just executed differently.

*When you get someone deactivated, are you sure that’s really the end of it?*

As usual, you test any given feature by first understanding how it works, then trying to break it by any means possible. In this case, the idea was that the site offered a feature letting you deactivate any user — even if that user was an Admin.

*But is that claim actually true?*

Take a closer look at the second user’s account, and you’ll find that it was indeed blocked — but the site never invalidated the old sessions. They stayed alive and kept communicating with the server as if nothing had changed.

I found that the existing session remained valid and retained the account’s pre-deactivation privileges. To prove the vulnerability — and the site made this embarrassingly easy — I changed the account’s name as a simple proof of concept, and even went ahead and blocked the other users, evend delete other admins !!…all from that same “deactivated” account :)

Digging into it further, the root cause -i think- The application validated the account status during authentication, but failed to revoke existing sessions or enforce the blocked state on subsequent requests.

The triager was about to close it as Out of Scope, but I walked him through the actual impact :)

And thankfully, it was accepted 😁

*Scenario 2-Trust nothing that comes from the user. And if you do… you’ve already been fooled !*

So I dug a bit deeper, going back through the old requests, and one of them caught my attention. While reproducing the original vulnerability — following the same steps as before: the user gets blocked, and from there we check whether they can still interact with the system, and whether they can still change anything while blocked — I noticed that when I changed the name, the response came back with “status”: “BLOCKED”

I thought — why not take this parameter and throw it back into the request that edits any profile field?

And to my surprise, it actually worked!

By manually injecting that parameter into the request body, I was able to modify the status — a textbook Mass Assignment vulnerability.

And sure enough, looking at it from the admin’s side, you can actually see that the user lifted the block off themselves.

Naturally, the next question was: if “status”was injectable this way, what about “permissions”? I tried the exact same approach — grabbing the permissions field from a legitimate response and replaying it in the profile-update request — but this one was properly validated server-side and got rejected. So the mass assignment issue here was scoped specifically to the status field, not a full privilege-escalation path.

This isn’t just a passing session-management issue, or some minor edge-case tweak. It strikes at the very structure of your organization on your SaaS platform — a user being able to remove or delete assets, remove members, or block them outright, all while you’re supposed to be confident that the assumption you built your system on can’t be broken.

The door was never locked in the first place for it to be “broken.” The door was already wide open.

And in other cases, a copy of that very door was sitting in the hands of the person it was supposedly locked against.

I hope these simple scenarios gave you something useful. And in closing — don’t forget to keep our Uyghur brothers and sisters, the people of Gaza, and oppressed Muslims everywhere in your prayers. Wassalamu alaikum.

U can find me on:

[www.linkedin.com/in/yosef-mostef](http://www.linkedin.com/in/yosef-mostef)
