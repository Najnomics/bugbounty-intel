# How I Bypassed 2FA by Changing One Request Parameter — and Earned a $$$ Bounty

- **Source URL:** https://nowisar.medium.com/how-i-bypassed-2fa-by-changing-one-request-parameter-and-earned-a-bounty-3582027c135e
- **Fetched from:** https://nowisar.medium.com/how-i-bypassed-2fa-by-changing-one-request-parameter-and-earned-a-bounty-3582027c135e?source=rss-57e4c76743c7------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14976 (id 14976)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohamed Nowisar  / Tue, 10 Nov 2026 08:18:32 GMT

Hello everyone! I’m Nowisar, and today I’m thrilled to share one of my recent findings — a logic flaw in the target’s login flow that let me skip 2FA entirely: no code, no OTP, just a different string in the request.

Now, let’s start.

The target’s login is a two-step handshake. Step one: send a username and password. If the account has 2FA configured, the server doesn’t log you in yet — it returns an intermediate session and tells you exactly what it’s waiting for next.

POST /api/v1.0/auth/initiate-auth/

{"username":"\<victim>","password":"\<known password>"}

200 OK

{"challenge\_name":"SOFTWARE\_TOKEN\_MFA","session":"\<JWT>"}

Decode that session JWT and it confirms the same thing from the server’s side:

`{"authentication_flow":"SOFTWARE_TOKEN_MFA","scope":"authentication","user_id":1698586}`
The server has already decided this account needs a TOTP code before it’s done. That decision is baked into the session.

Step two — respond-to-auth-challenge — takes the session back, plus two things the *client* supplies: a challenge\_name and an answer (the code). The design intent is obvious: challenge\_name should just be the server echoing back what it already decided in step one, and answer is how you prove you cleared it.

Here’s the actual bug: **the server never checks that the challenge\_name the client sends matches the authentication\_flow stored in the session.** It just looks at whatever string you send and branches on it. That means the client gets to pick *which challenge it wants to satisfy* — including picking one that doesn’t require anything at all.

MFA\_SETUP is the branch meant for a different scenario entirely: a user who has *no* second factor yet, going through the one-time setup screen. It’s not supposed to be reachable once SOFTWARE\_TOKEN\_MFA is the recorded flow. I sent it anyway, against an account that genuinely has 2FA turned on, with no answer field at all:

POST /api/v1.0/auth/respond-to-auth-challenge/

{"session":"\<session from step 1>","challenge\_name":"MFA\_SETUP"}

200 OK

{"token":"\<DRF token>","jwt":{"access":"...","refresh":"..."}}

No TOTP code submitted. No OTP. Full, finished session handed back — confirmed by decoding the access token:

`{"token_type":"access","user":{"id":1698586,"profile":{"role":"manager"}}}`
No authentication\_flow claim left on it. As far as the API is concerned, login is complete.

Proving It’s Real, Not a Fluke

A bypass that only grants read access is bad. One that lets the attacker lock the real owner out is a different severity entirely — so I tested that too, on my own account, with a planned revert:

POST /api/v1.0/account/change-password/

-H 'Authorization: Token \<bypass-derived token>'

{"old\_password":"\<known>","new\_password":"\<new>","new\_password\_confirmation":"\<new>"}

`200 {"status":"Password changed successfully"}`
Old password: now 400. New password logs in — and still prompts SOFTWARE\_TOKEN\_MFA next time, because the 2FA enrollment itself was never touched. It was only ever *skipped*, not removed.

That’s the part that makes this dangerous in practice: the victim’s authenticator app keeps working, their security settings show nothing has changed, and nothing tells them someone bypassed their second factor entirely on the way to taking their account. With 2FA enabled, an account here is, in practice, protected by its password alone — the second factor adds no real barrier once this challenge-name bypass is in play.

**Root Cause**

challenge\_name should be derived from the session the server already issued, never read from the request — letting the client choose it turns a step that’s supposed to verify a factor into a step where the client picks which factor to satisfy, including “none.”

Follow for more findings, methodologies, and bug bounty tips. 🔥

[https://www.linkedin.com/in/mohamed-nowisar-073964327](https://www.linkedin.com/in/mohamed-nowisar-073964327)

[https://x.com/nowisar1878](https://x.com/nowisar1878)
