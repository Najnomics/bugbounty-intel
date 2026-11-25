# 2FA simple bypass — An Authentication Bypass  Lab Walkthrough

- **Source URL:** https://vivek0x.medium.com/2fa-simple-bypass-an-authentication-bypass-lab-walkthrough-cacdd16ed682
- **Fetched from:** https://vivek0x.medium.com/2fa-simple-bypass-an-authentication-bypass-lab-walkthrough-cacdd16ed682?source=rss-a3d6c85e9637------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14966)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vivek Yadav / Sat, 31 Oct 2026 16:19:51 GMT

Platform: Portwigger’s Web Security Academy

Two-factor authentication gets sold to us as the thing that finally makes accounts “safe.” Password gets stolen? No big deal, the attacker still needs that six-digit code from your email or phone. In theory, that’s a solid second layer of defense.

In practice, a lot of real-world 2FA implementations are bolted onto an existing login flow as an afterthought, and that’s exactly where things fall apart. PortSwigger’s **“2FA simple bypass”** lab (Apprentice level, from the Authentication topic) is a perfect, bite-sized demonstration of this. It shows how a 2FA check that only lives on the *client-facing navigation* — and not on the *server’s session state* — can be skipped entirely just by typing a different URL into your browser.

Here’s how I solved it.

The lab gives you two sets of credentials:

The goal is stated plainly: you have valid credentials for Carlos, but no access to his 2FA verification code. To solve the lab, you need to land on Carlos’s account page anyway.

That framing already tells you something important — this isn’t about cracking or intercepting a code. It’s about finding a flaw in the *logic* of the authentication flow that lets you walk around the 2FA check rather than through it.

Before trying to break anything, I wanted to understand what a legitimate login looks like end to end. So I logged in as my own user first.

Nothing unusual yet — this is just how a standard 2FA flow is supposed to behave: login with credentials → get redirected to a code-entry page → submit the correct code → get access.

But I did one more thing before moving on: I **copied the exact URL of the my-account page**. That small, almost lazy step ended up being the whole key to the lab.

Next, I logged out and went back to the login page, this time entering Carlos’s credentials: carlos:montoya.

As expected, the app accepted the username and password — because remember, in this scenario I already *have* valid credentials for Carlos — and then redirected me to the same verification code screen, /login2.

This is where a real attacker would normally be stuck. I don’t have access to Carlos’s email inbox, so I have no way to generate or retrieve the actual verification code that’s supposed to be tied to his session.

Instead of fighting the verification form, I just… ignored it.

I took the browser’s address bar, which currently showed /login2, and manually replaced it with the **/my-account** URL I had copied earlier while logged in as myself.

I hit enter.

And I was in — looking directly at **Carlos’s account page**, fully authenticated as him, having never entered any verification code at all.

The lab immediately flagged as solved.

This is the part worth sitting with, because it’s not a flashy exploit — it’s a boring, extremely common mistake, and that’s exactly why it matters.

When I entered Carlos’s correct username and password, the application’s backend did something subtle but critical: **it created a valid, authenticated session for Carlos *before* the 2FA step had been completed.** The **/login2** verification page wasn’t gatekeeping access to the account — it was just gatekeeping *navigation*. The server had already decided “this person is logged in as Carlos” the moment the password check passed. The verification code screen was essentially a UI formality sitting on top of an already-privileged session, rather than a hard requirement enforced on every subsequent request.

So the actual security boundary — the thing that was supposed to stop me — only existed as a page the front end *showed* me, not as a check the back end *enforced*. Once I had a session that the server already considered authenticated, I could request any URL that session was entitled to, **/my-account** included, and the server happily served it. It never re-checked “wait, did this session actually complete its 2FA step?”

This is a textbook example of **broken access control arising from flawed authentication logic**: the state “username + password verified” got conflated with the state “fully authenticated,” when those two things should never be treated as equivalent once 2FA is in play.

It’s tempting to treat this as a toy example because the “attack” is so simple — there’s no fuzzing, no interception, no clever payload, just a copy-pasted URL. But that simplicity is exactly why this class of bug shows up in real applications more often than you’d think. It tends to happen when 2FA gets retrofitted onto an existing session-based login system:

The result is 2FA that protects the *happy path* through the UI, but not the actual account.

A few concrete fixes would close this off:

What I like about this lab is how much it demystifies 2FA bypasses. People often imagine these attacks requiring SIM-swapping, OTP interception, or some kind of code-generation trick. This one requires none of that — it just requires understanding that “the app shows you a code screen” and “the app actually checks you passed the code screen” are two very different guarantees, and attackers only care about the second one.

It’s a good reminder for anyone building or reviewing authentication systems: **every privileged endpoint needs to independently verify the full authentication state on its own, every single time** — never inherit trust from whatever page the user happened to arrive from.

*This lab is part of PortSwigger’s Web Security Academy, a free resource for learning web application security hands-on.*

GoodBye…
