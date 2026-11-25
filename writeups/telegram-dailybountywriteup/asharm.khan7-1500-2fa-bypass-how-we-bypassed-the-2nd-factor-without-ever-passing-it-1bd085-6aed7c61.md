# €1500 | 2FA Bypass

- **Source URL:** https://medium.com/@asharm.khan7/1500-2fa-bypass-how-we-bypassed-the-2nd-factor-without-ever-passing-it-1bd085d4a126
- **Fetched from:** https://medium.com/@asharm.khan7/1500-2fa-bypass-how-we-bypassed-the-2nd-factor-without-ever-passing-it-1bd085d4a126?source=rss-75df5aebe490------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14917)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ashar Mahmood / Fri, 18 Sep 2026 20:44:49 GMT

Hello! I’m Ashar Mahmood, a 23 year old cybersecurity researcher who keeps coming back to one thing: broken authentication. There is something satisfying about a login flow that looks locked down but quietly trusts the wrong thing. This one is a great example. A **two-factor authentication bypass** that let me and my friend [Faique](https://medium.com/u/37bacdeff874) walk straight into an account with nothing but the password, on a private program running through a well known bug bounty platform.

I want to be upfront that this was a team effort, and that is the point. Bug bounty gets treated like a solo grind, but some bugs only fall when two people bounce ideas off each other. One of us kept poking at the mid-login state while the other questioned whether the settings page should even load there. Neither angle alone closes the loop. Together they did. If you hunt with a partner you trust, findings like this come faster and cleaner.

It paid out €750, plus a €750 bonus. Let me walk you through it.

The target lets you register in two flavours: a personal account, or a company account. On the login page there is a small link to create an account for “your company”.

I followed the company signup, but on the business form there is an escape hatch. If you do not have a Chamber of Commerce number, it offers to just make you a normal private account instead.

So I created a plain account, verified my email, and then did the responsible thing any attacker would do to their own test account. I turned on two-step verification, set to “Every time I log in”.

Account fully protected. Password plus an SMS code on every login. That is exactly the state I wanted, because now I could try to break it.\

I logged out, opened an incognito window, and logged back in with just the email and password. As expected, the SMS challenge appeared and asked for the six digit code.

This is the interesting moment. At this exact point I am not logged in. I have proven my password but not the second factor. The only things this session should be allowed to do are: enter the code, resend the code, or cancel. That is it.

So instead of entering the code, I opened a second tab and went straight to the 2FA settings page:

\`\`\`

[https://login.example.com/wsp/2fa/settings?code=test](https://login.example.com/wsp/2fa/settings?code=test)

\`\`\`

Two things jumped out. First, the \`code\` parameter did not matter. I passed \`code=test\`, a value that is clearly not a real verification token, and the page loaded anyway. Second, and this is the actual bug, the page loaded \*\*using my half-finished login session\*\*. My email even showed as verified.

From there I opened my security preference and flipped it from “Every time I log in” to “Never use when I log in”, then hit save.

I clicked “go back to settings” and landed on the account security page, fully logged in.

No code ever entered.

The company was extremely pleased with my report and the vulnerability, and they even rewarded me with an **additional bonus on top of the original bounty!**

The trick is easy. The reason it worked is the part worth understanding.

When you pass the password step, the app hands you a session, but it is a \*\*half-authenticated session\*\*. It represents “this person knows the password and is now being challenged”, not “this person is logged in”. Everything after that point is supposed to stay locked until the SMS code is accepted.

The flaw is that the 2FA settings endpoint never checked which kind of session it was talking to. It treated my half-authenticated session as if it were a fully logged-in user and happily let me change security settings. So I used that gap to switch off the exact control that was standing between me and the account. Once 2FA was set to “never”, the challenge had nothing left to enforce, and the session was promoted to fully authenticated.

In short: a session that has passed one factor was allowed to disable the second factor. The app confused “being challenged” with “being logged in”. The ignored \`code=test\` is the cherry on top, since the endpoint was not validating the token it was handed either.

Any account with 2FA enabled could be fully taken over with password only. Once inside, an attacker could:

1\. Act as the victim, including viewing and changing their orders.

2. Access personal data such as order history, saved addresses, and potentially stored payment details.

3. Permanently disable 2FA on the victim’s account, leaving it weaker for every future login.

The whole point of the second factor is to survive a leaked or guessed password. This bug quietly removed that protection

Two things close this cleanly:

1\. \*\*Bind sensitive actions to a fully authenticated session.\*\* Changing 2FA settings should only be possible after the second factor is actually satisfied, never from a mid-challenge session.

2. \*\*Re-authenticate for security-sensitive changes.\*\* Turning 2FA off is exactly the kind of action that should require stepping up, not stepping around.

And of course, actually validate the \`code\` value instead of accepting anything.

The most dangerous state in an auth flow is the in-between one. Everyone hardens “logged out” and “logged in”, but the half second where you have passed one check and not the other often gets treated like a formality. It is not a formality. It is a fully separate trust level, and it needs its own rules.

A valid session is not the same as a completed login. Whenever an app has a multi-step gate, poke at what a partial session is allowed to touch. If a half-authenticated user can reach the switch that turns off the very check they are stuck on, the whole gate falls.

Huge shoutout to my friend and hunting partner [Faique](https://medium.com/u/37bacdeff874) on this one. This bug was a proper team effort, and it is a good reminder that some findings only click when two people are picking at the same flow from different angles. Go give them a follow.
