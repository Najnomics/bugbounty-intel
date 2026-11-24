# My $1000 Bounty Bug

- **Source URL:** https://medium.com/@a13h1/my-1000-bounty-bug-how-i-stopped-companies-from-losing-money-with-an-idor-flaw-2366984a6c40?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230828131748/https://medium.com/@a13h1/my-1000-bounty-bug-how-i-stopped-companies-from-losing-money-with-an-idor-flaw-2366984a6c40
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3709 (id 3709)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My $1000 Bounty Bug: How I Stopped Companies from Losing Money with an IDOR Flaw

--

Discover the intriguing tale of how I stumbled upon an IDOR (Insecure Direct Object Reference) vulnerability in Examfit’s (Virtual Name of private program)Expense Validation system, and how this flaw had the potential to lead to unauthorized expense approvals, potentially costing companies a fortune.

An IDOR vulnerability caught my eye in Examfit’s(Not Using the orignal name of private program) Expense Validation scheme. But what’s IDOR, you ask? It’s like opening a door to a room you’re not supposed to enter — except it’s a digital room filled with sensitive data. In this case, it was the power to approve or reject expense requests on behalf of a victim company. Yes, you read that right!

Unleashing the Power of IDOR


Imagine this scenario: A company uses Examfit for expense management, and an employee submits an expense request. Now, imagine having the power to approve or reject those expenses on behalf of the company. With two accounts — one belonging to the victim’s company employee account and the other to the attacker’s company — the stage is set for some sneaky maneuvers.

1. Create an Expense Request: Put on your employee hat and create an expense request as you normally would.
2. Sneak a Peek: As the expense request is processing, keep an eye on the company ID for the victim’s company. Remember, we’re just looking, not touching.
3. Capture the Request: Now, switch over to another account. This account should belong to a different company. Use this account to capture the /hr/expenses/validation request — it’s like taking a snapshot of what’s happening.
4. The Switcheroo: Here’s where the magic happens. In the captured request, find the expense ID. It’s like swapping a puzzle piece. Change the expense ID to the one you want to give the green light to.
5. Let the Request Fly: Send the edited request on its way, like a secret message. You’ve just put your hacker hat to work.
6. Check the Result: Open up the expense requests and see the magic unfold. The expense that you’ve slyly given the thumbs up to gets approved.

Why This Matters


Now, you might be thinking, “What’s the big deal?” Well, imagine the chaos if someone can approve or reject expenses without permission. It’s like letting someone else decide what to do with your money — definitely not a good idea! If the attackers or employees use this bug to create fake expense requests and accept those themselves, companies start losing money

A Bounty Earned,


With great vulnerability discovery comes great responsibility. After alerting Examfit’s security team to this sneaky IDOR, the issue was addressed, and a well-earned $1000 bounty was awarded.

Final Thoughts


And there you have it — the story of how a little bug made a big impact and turned into a rewarding experience in the world of bug bounties.Stay curious, keep exploring, and remember that every bug found is a step towards a safer online world and increasing in your bank balance. :)

Until next time, fellow explorers!


Leave a clap if you enjoyed this read, and consider following me for more exciting content.

If you’re eager to discuss findings or dive into the world of bug bounties, you can also find me on Twitter.

*Find me on Twitter: @a13h1\_*


Thank you everyone
