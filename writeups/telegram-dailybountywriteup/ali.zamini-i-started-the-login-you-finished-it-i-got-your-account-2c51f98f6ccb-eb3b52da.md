# I Started the Login. You Finished It. I Got Your Account.

- **Source URL:** https://medium.com/@ali.zamini/i-started-the-login-you-finished-it-i-got-your-account-2c51f98f6ccb
- **Fetched from:** https://medium.com/feed/@ali.zamini
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14987 (id 14987)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
#### A one-click account takeover through a genuine Google link, built from a popup that never talked, a token handed out too early, and two extra path segments.

OAuth flows are some of my favourite things to test in bug bounty. Every company wires “Continue with Google” together a little differently, and the bugs live in the glue between the steps.

This one was on a big online shop’s bug bounty program. I can’t name it, so let’s call it ‘shop.example’. Customer accounts there hold the usual valuables: name, home address, phone number, order history and etc.

My setup was simple: two Google test accounts of my own, one playing the **attacker** and one playing the **victim**, each in its own browser. The goal was to map the Google login step by step and see where it could be bent.

By the end, the attacker browser (one that had never typed a password or signed into Google) was logged in to the victim test account. All the victim had done was click a link to ‘accounts.google.com’ (a real one, not a lookalike) and pick their Google account.

#### Where it started

I began the way I always do with OAuth: log in normally with my own account, watch every request go by, and understand the flow before attacking anything. Almost immediately, something didn’t add up.

#### The popup that didn’t talk

I clicked **Continue with Google** and the Google sign-in opened in a **popup**. I picked my account, the popup closed, and the page behind it was already logged in.

A popup login usually means ‘postMessage’. The popup finishes the OAuth dance and messages the result back to the page that opened it. Sloppy origin checks on that message are a classic bug, so I opened DevTools and went looking for it.

There was no ‘postMessage’. Not one.

That raised a better question than any message handler could have:

If the popup never tells the parent page anything, how does the parent page know I just logged in?

The two windows weren’t talking to each other, so they had to be talking to the server about the same thing. I wanted to know what that thing was.

#### Reading the flow

The shop doesn’t simply redirect to Google. It builds the whole login through its **GraphQL API**:

1. The page sends a GraphQL request to **start a Google login**. It includes a ‘callbackUrl’, which is where the browser lands at the end.
2. The backend answers with two things: an **‘Id’** for this login attempt, and a ready-made Google sign-in URL containing a ‘state’ value.
3. The popup opens that Google URL. The user picks an account, and Google redirects back to the shop’s auth server with a ‘code’.
4. The auth server exchanges the code with Google, marks the login attempt as **done**, and redirects to the ‘callbackUrl’ with a token attached: ‘?t=…’
5. A second GraphQL request **redeems** ‘t’ and gets session cookies back.

I lined up the responses side by side, and the ‘t’ from step 4 was **exactly the same string** as the ‘Id’ from step 2.

That answered my question. The parent page never needed a message from the popup, because it got the ‘Id’ in the very first response, before anyone had authenticated. Once Google was done, it only had to swap that ‘Id’ for a session.

#### What happens if someone else finishes my login?

Look at the flow again with a suspicious mind.

The value that buys a logged-in session at the end is handed out at the start, to whoever begins the login. The backend never checks that the browser redeeming it is the one that went through Google: there is no cookie binding and no per-device secret. The ‘Id’ works like a cloakroom ticket, and whoever holds the ticket gets the coat.

So what happens if **I** start the login and **somebody else** does the Google part and then **I** finish it?

#### The catch: the victim spends the token first

My first try failed, and for a good reason.

‘t’ is single-use. On the normal, **happy path**, the victim’s browser lands on the callback page and the shop’s frontend redeems ‘t’ immediately. The victim gets logged in, the token is burned, and my copy of the ‘Id’ becomes a dead string. The backend just says no.

To make this work, I needed an **unhappy path**: the victim has to finish the Google step, but their browser must never spend the token.

#### Building the unhappy path

The ‘callbackUrl’ from step 1 was the only lever I had, and it was a narrow one.

The backend locked the callback down hard. I could not change the host, the existing path, or any of the query parameters the frontend sends by default. Every attempt to swap the redirect for something else was rejected.

There was one thing it allowed: **appending to the end of the path.** As long as the URL still began with the real callback, anything I added after it went through.

So I put the “start login” GraphQL request through my proxy, intercepted it, and added two junk segments to the path:

default:   https://shop.example/account/auth/login?redirect=...&provider=GOOGLE

appended: https://shop.example/account/auth/login/x/y?redirect=...&provider=GOOGLE

The backend accepted it, because it still started with the real callback path. The frontend, though, didn’t recognise ‘/login/x/y’ as a login callback. When the victim’s browser lands there, the page shrugs, redirects to the homepage, and **never touches ‘t’**.

The victim ends up on the shop’s front page, not logged in, and assumes the link was boring. Meanwhile ‘t’ sits on the server: authenticated as the victim, unused, and waiting for me.

#### The full attack

In plain words:

1. **I start a login** as an anonymous guest, intercept the GraphQL request, and append ‘/x/y’ to the callback path.
2. **I keep the Id’** and send the victim the Google URL. It really is ‘accounts.google.com’. Hover over it, inspect it, run it through a link scanner: it’s clean, because it is clean. The shop generated it.
3. **The victim clicks and picks their Google account.** If they’ve used Google sign-in on the shop before, there isn’t even a consent screen.
4. **Their browser hits my unhappy path**, lands on the homepage, and leaves ‘t’ alone.
5. **I redeem my ‘Id’**. The backend replies with the victim’s email, name and user ID, and sets logged-in session cookies in my browser.

#### Why this one is nasty

- **The lure is a real Google link**. Security training tells people to check the domain, and this domain checks out.
- **The victim does nothing wrong.** They sign in to a shop they already use, with the account they already use.
- **Nothing looks off afterwards.** They land on the homepage with no error and no warning.
- **It scales across the brand.** The same login component ran every regional storefront I tried, so one bug covered all of them.

The one honest limit is the click. This is a one-click takeover, not a zero-click one.

#### The fix

1. **Bind the login attempt to the browser that started it.** Set an unguessable, HttpOnly cookie when the login starts and require it at redemption. An attacker can start as many logins as they like, but they can’t redeem one their own browser didn’t complete.
2. **Never reuse the public ‘Id’ as the redemption token**. Whatever you hand out before authentication must not be the thing that buys a session after it.
3. **Match callback URLs exactly.** “Starts with our callback” is not an allowlist. Two extra path segments were enough to flip the happy path into an unhappy one.

#### What I took away from it

- **Every OAuth flow might differ. You need to understand it first, then start asking questions: what happens if…?** What happens if someone else finishes this step? What happens if this value is redeemed from another browser? What happens if the callback lands somewhere unexpected? I didn’t find this with payloads. I found it by asking how the parent page knew.
- **A missing thing is a clue.** I expected ‘postMessage’ and found nothing. “Then how does this work?” was worth more than any scanner result.
- **Compare values across steps.** The core of the bug was two strings being equal.
- **Ask “who is this bound to?” for every token.** A token bound to nobody belongs to everybody.
- **Small gadgets make big bugs.** “You can append to the callback path” isn’t a report on its own. Chained with an unbound login, it turned a dead token into a reliable account takeover.
