# Easy 2000$ Race Condition

- **Source URL:** https://medium.com/@_deshine_/easy-2000-race-condition-b4d093c9bc3c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230126201010/https://medium.com/@_deshine_/easy-2000-race-condition-b4d093c9bc3c
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1507 (id 1507)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Easy 2000$ Race Condition

In this post, I will show you how Race Condition can be critical.

A few months ago, I was invited to a new Hackerone program. This program is about managing the games of basketball and baseball teams. It has a lot of roles and permissions but in this post I won’t talk about them.

This program has 2 domains that can be temporarily called:

- [https://redacted.com](https://redacted.com) (This is the main site for people to join the team or create a team that invites everyone to join).
- [https://bv.redacted.com](https://bv.redacted.com) (This is a site for admins to manage teams, times, locations of matches, etc).

Admins can configure membership fees to participate in the tournament or join the team. They can also configure discount vouchers for participants.

If we use a voucher to join the team or enter the tournament, we will get a discount or free. But the voucher is limited.

So how can we make vouchers unlimited?

We will use multiple accounts to race at the same time, then all accounts registered to the team will be discounted or free.

This will cause the voucher to exceed the amount allowed in the configuration resulting in the organization losing money. And if it has anything to do with money, it will be CRITICAL.

Thank you for spending time reading.

DESHINE
