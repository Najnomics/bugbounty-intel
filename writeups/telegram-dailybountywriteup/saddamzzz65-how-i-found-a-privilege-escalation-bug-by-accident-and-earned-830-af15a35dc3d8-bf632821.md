# “How I Found a Privilege Escalation Bug by Accident and Earned $830”

- **Source URL:** https://medium.com/@saddamzzz65/how-i-found-a-privilege-escalation-bug-by-accident-and-earned-830-af15a35dc3d8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501123755/https://medium.com/@saddamzzz65/how-i-found-a-privilege-escalation-bug-by-accident-and-earned-830-af15a35dc3d8?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9403 (id 9403)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# “How I Found a Privilege Escalation Bug by Accident and Earned $830”

Sometimes, being lazy leads to the most interesting bugs

While I was casually bug hunting one day, I stumbled upon an interesting privilege escalation bug — and unexpectedly earned a \*\*$830\*\* reward for it.

At first, I was trying all the basic techniques to bypass access controls on a certain website. After a while, I got a bit lazy and decided to take a break from hardcore testing. That’s when things got interesting.

The website had a feature where users could join a group using a shared link. The process was simple: copy the invite link, paste it, and click the “Join” button. I joined a group this way, then removed my account from the group manually.

Later, out of curiosity, I tried to rejoin the group using the same invite link. This time, it threw an error — the system wouldn’t let me in because the group admin had previously removed me. That’s when I remembered seeing some IDOR tricks and methods earlier that day, and a new idea sparked.

I captured the “join” request in Burp Suite and initially just replayed it — no luck. But then I tried something different. I changed the HTTP method of the request (something I hadn’t experimented with before), and boom — it worked.

I checked the website again, and to my surprise, I was back in the group. But it got even more interesting. I noticed that the admin of the group could no longer remove me. Any attempt to remove my account would return an error on their end — I had essentially bypassed the restriction and locked myself into the group as an untouchable member.

I reported the bug to the program, and they validated the issue as a critical privilege escalation vulnerability. As a reward, I received $830.

Sometimes the best bugs show up when you’re just experimenting — or even feeling lazy.

X (Twitter) — [@saddamzzz65](https://web.archive.org/web/20250501123755/https://x.com/Saddamzzz65)
