# How I Found My First $$$ Bug on HackerOne (A Simple API Call Changed Everything)

- **Source URL:** https://medium.com/@princelassey/how-i-found-my-first-bug-on-hackerone-a-simple-api-call-changed-everything-2be8ac3db822
- **Fetched from:** https://infosecwriteups.com/how-i-found-my-first-bug-on-hackerone-a-simple-api-call-changed-everything-2be8ac3db822?source=rss-22e6c38d4ef5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14926 (id 14926)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Prince Lassey / Mon, 28 Sep 2026 03:17:11 GMT

*A story about a LinkedIn DM that aged surprisingly well, why I started caring about bug bounty when I swore I never would, and the exact API response that made me stop scrolling and start typing a report.*

In 2025, I did something that felt completely normal to me but perhaps mildly embarrassing to someone else at the time; I cold-messaged a senior security researcher on LinkedIn, not to network in that hollow professional sense, not to ask for a job referral, but genuinely just because I’d been watching this person drop bounties made and vulnerability writeups like it was nothing and I needed to understand how someone actually gets to that level.

*What does the path look like from the outside versus what it actually feels like from the inside?*

He replied, which surprised me, and his advice was almost frustratingly simple: start with portswigger labs , then read medium write-ups Hackerone reports. Collaboration with bug bounty hunters will give more knowledge.

Yep, you heard right.. no secret resources, no special community to join, just consistent deliberate practice on fundamentals. So that’s what I did (from time to time) I won’t sugar-coat it as if I did that always lol but yeah I took PortSwigger labs at weird hours, I saved and read disclosed H1 reports I found via medium writeups and took part in CTF challenges that humbled me a lot.

I got to a point where I could look at a vulnerability writeup and understand not just what happened but why it happened, which felt like meaningful progress.

But somewhere along the way, the defensive side of security started pulling harder than the offensive side. Threat detection, log analysis, alert triage, even to the extent of incident response, understanding how attacks look from the perspective of someone trying to catch them rather than execute them; there was something more satisfying about that to me, and offensive skills started feeling less like the main event and more like a lens that made me better at defense.

I kept doing CTFs occasionally just to maintain the muscle memory, but bug bounty specifically never really called to me. The scope documents, the legal requirements, the careful rules of engagement.. all felt like a lot of administrative overhead for something I wasn’t particularly motivated to pursue.

That changed in September 2026, not because my opinion shifted dramatically, but because my circumstances did. I found myself in a position where offensive security was no longer optional background knowledge.. it was going to matter in ways it hadn’t before, and I needed to close a real gap between where I was and where I needed to be.

Sitting in labs felt too passive at this point. I needed real targets, real applications and real feedback. So I opened HackerOne for the first time in 2 years and started hacking my way into programs.

The first thing I noticed when browsing programs was that the long-running ones.. I mean the ones that had been live on HackerOne for three, four, five years felt almost impenetrable lol. Thousands of resolved reports, massive researcher communities combing through them constantly, and this uncomfortable feeling that every obvious surface had already been picked clean by someone smarter and faster.

I’m not saying those programs are impossible, clearly people still find things, but as someone coming in once more, the signal-to-noise ratio felt terrible. It was like buying bitcoin in 2026 rather than 2013 lol.. *I would be a millonaire by now if I had bought bitcoin at that tender age.* That was just btw..

So I shifted focus to newer programs, things that had been added recently where the attack surface hadn’t been exhausted by years of accumulated research, and that filter alone made the whole exercise feel significantly more approachable.

I eventually landed on a \[REDACTED\] management platform; large enterprise customer base, HIPAA and PCI DSS territory, the kind of product that businesses trust with assets they genuinely cannot afford to lose. More importantly for my purposes, they had a full REST API that was comprehensively documented, multiple asset tiers in scope, and a clear authenticated testing process.

I’m keeping the program name redacted per disclosure policy and will refer to it as **\[REDACTED\],** and others as **shared-\[ASSET\], and course** throughout.. in case you saw some in the earlier text which I know you literally did.

Before creating an account, I wanted to understand what the application exposed to someone with zero credentials, because that’s usually where you find the cheapest wins such as endpoints that should require authentication but don’t, information leaking through error messages or public surfaces that behave differently than intended.

The application was a React single-page app, which meant that the real attack surface wasn’t the HTML being served but the API underneath it, so I looked up the developer documentation and started reading it.

While reading, I got to know that the API supported **course-scoped API keys**, meaning you could create a key restricted to a specific course and that key would theoretically only be able to operate within that path.

The documentation described this explicitly as a delegation mechanism.. a way to give a third-party integration or automation limited access without handing over full site privileges.

Well, we want something to execute code remotely.. “I guessed” and kept reading, but it stayed in the back of my mind as something worth probing properly once I was inside. What if the app does not work as documented?

Unauthenticated enumeration didn’t yield much beyond the expected 401s on anything meaningful.

It was then time to get an account.

I followed the program’s instructions precisely, HackerOne alias as the work email. Once inside, I created two accounts.. my primary admin account and a second regular user with no elevated privileges because testing privilege escalation and IDOR properly requires an attacker and a victim, and in this context I was playing both roles simultaneously.

I spent about thirty minutes clicking through the web UI first, just to get a feel for how the application presented itself to a normal user, and that’s when I noticed something that reframed my whole approach.

The UI was showing me a filtered subset of what the API could actually do, and the program’s own documentation acknowledged this directly:

*“The API exposes functionality the UI does not. That is by design.”*

That sentence is essentially an invitation to stop using the browser and start talking to the API directly, because if the UI is a filtered view and the API accepts parameters the UI never sends, the interesting question becomes what happens when you send those parameters yourself.

curl became the obvious tool for direct HTTP requests against the API with full control over every field.

I came back to a feature that had caught my attention during the documentation review, because the gap between what it promised and what I could actually verify had been sitting with me.

The endpoint was POST /api/rest/v1/api\_keys, and the documented course (redacted)parameter was described clearly: set it to an \[asset\] name and the key's access would be restricted to that \[asset\].

The documentation even spelled out the use case.. create a defined key, hand it to a third-party integration, and that integration can only touch the \[asset\] you specified.

Everything else on the site remains inaccessible to it

This is a trust boundary. An explicitly documented, apparently designed trust boundary. And the right question to ask about any trust boundary is whether it actually holds when you push on it.

curl -s -X POST -H "\[REDACTED\]API-Key: $ADMIN\_KEY" -H "Content-Type: application/json" \

-d '{

"name": "test-key",

"permission\_set": "full",

"course (redacted)": "shared-\[ASSET\]",

"user\_id": \[REDACTED\]

}' \

"$BASE/api/rest/v1/api\_keys" | python3 -m json.tool

The response came back clean with no error, no validation failure, just the newly created key object. I read through the fields one by one and landed on this:

```
{
    "id": [REDACTED],
    "name": "test-key",
    "permission_set": "full",
    "course (redacted)": null,
    ...
}
```
I had sent "course (redacted)": "shared-\[ASSET\]" and the API had returned "course (redacted)": null , not a different representation of the same value, not a normalized path format, just null.

The restriction I'd explicitly requested had been silently dropped, and the key had been created with no indication anything had gone wrong.

The root cause wasn’t that course restrictions didn’t work at all… it was specifically that when you supply a course pointing to an \[ASSET\] that doesn’t yet exist on the site, the platform silently drops the restriction instead of storing it or returning an error.

If the \[ASSET\] exists at creation time, the path gets stored and enforced correctly. If it doesn’t exist, you get course: null

That’s a meaningful distinction, the failure mode is subtle: a developer or administrator creates a key for an \[ASSET\] they’re about to set up, or makes a typo in the course name, and walks away believing they’ve created a restricted key when they’ve actually created a fully privileged one. No error. No indication. Just a silent footgun built into the creation flow.

The program shipped a fix and invited me to retest, which I ran immediately. Same creation request, same nonexistent asset path and this time the response came back correctly:

json

```
{
    "id": [REDACTED],
    "name": "retest-nonexistent-course-key",
    "course": "nonexistent-asset-abc123",
    "permission_set": "full",
    "user_id": [REDACTED]
}
```
Course stored as submitted rather than dropped to null. And when I tested the key against endpoints:

GET /api/rest/v1/redacted/

-> 403 Api Key Is Course Restricted

"Invalid course for the API key. The API key is only valid for course nonexistent-asset-abc123"

Restriction enforced correctly even on an \[ASSET\] that doesn’t exist yet.

Fixed cleanly.

The bounty came in at $250 + $50 rewarded for a retest.

More importantly, I’d say it pays to read and understand how things are documented to work by the developer and validate if there’s no broken access control.

The finding came from reading the documentation like it was a contract, identifying a specific feature that established a documented trust boundary, and then verifying whether the application honored that boundary when you interacted with it directly through the API.

The web UI would never have surfaced this, the UI doesn’t expose key creation in a way that would let you observe the silent drop. It took constructing the raw API request myself and reading the response field by field to catch "course": null where "course": "shared-\[ASSET\]" should have been.

If there’s one thing I’d pass on to someone starting out, it’s this: when a program’s documentation describes a feature that restricts access, that description is a test case.

The documentation told me exactly what the courseparameter was supposed to do, which meant the documentation also told me exactly what to look for when it didn't do that.

I believe there’s more to learn, more to grasp and better days ahead,

Peace.

[How I Found My First $$$ Bug on HackerOne (A Simple API Call Changed Everything)](https://infosecwriteups.com/how-i-found-my-first-bug-on-hackerone-a-simple-api-call-changed-everything-2be8ac3db822) was originally published in [InfoSec Write-ups](https://infosecwriteups.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
