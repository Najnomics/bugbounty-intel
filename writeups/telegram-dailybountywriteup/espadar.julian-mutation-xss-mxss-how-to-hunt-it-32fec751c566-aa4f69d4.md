# Mutation XSS (mXSS)

- **Source URL:** https://medium.com/@espadar.julian/mutation-xss-mxss-how-to-hunt-it-32fec751c566
- **Fetched from:** https://medium.com/@espadar.julian/mutation-xss-mxss-how-to-hunt-it-32fec751c566?source=rss-8064117de3f2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14917)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** julichaan / Fri, 18 Sep 2026 20:18:46 GMT

*Last few months, I’ve spent a lot of time hunting XSS. Some findings came quickly. Others took days of staring at DOM trees, browser developer tools, and application flows that looked perfectly secure at first glance.*

One vulnerability class that completely changed how I approach XSS hunting is **Mutation XSS**, commonly known as **mXSS**.

The funny thing is that when I first heard about mXSS, I thought it was just another niche browser quirk that only affected researchers building proof-of-concepts.

I was wrong.

Today, many mature bug bounty targets have strong sanitization libraries, modern frontend frameworks, CSP deployments, and developers who understand the basics of XSS prevention.

Yet researchers continue finding impactful XSS vulnerabilities.

The reason is simple:

*The browser doesn’t always interpret content the same way the sanitizer does.*

And that’s where things get interesting.

Years ago my XSS workflow was straightforward.

Find an input.

Try a payload.

Observe the response.

Repeat.

Sometimes it worked.

Most of the time it didn’t.

As bug bounty programs became more mature, I noticed something changing.

Applications were escaping output correctly.

Libraries like DOMPurify were everywhere.

Frontend frameworks were automatically sanitizing content.

Traditional payload lists became less useful.

For a while, I thought I was simply targeting harder applications.

Then I started reading more writeups from researchers who consistently found XSS in programs where everybody else failed.

One pattern immediately stood out.

They weren’t spending most of their time crafting payloads.

They were studying parsers.

That realization completely changed my approach.

Today, when I see a sanitization layer, my first question is no longer:

*“How do I bypass this?”*

Instead, I ask:

*“Will this content ever be parsed again?”*

If I had to pick one pattern that appears repeatedly in modern mXSS research, it would be **double parsing**.

A surprising number of applications follow a flow similar to this:

Everything appears secure.

The sanitizer did its job.

The dangerous content was removed.

The developers move on.

But somewhere later in the rendering pipeline, the browser receives a slightly different version of that content.

And suddenly the DOM being interpreted is not the same DOM that was originally inspected.

The first time I started looking for these scenarios deliberately, I began finding strange parser behavior everywhere.

Not necessarily vulnerabilities.

But enough weirdness to understand why mXSS continues to exist in 2026.

If there’s one place I instinctively investigate whenever I start a new target, it’s rich text editors.

Not because they’re inherently insecure.

Because they do too much.

A modern editor often:

That’s a huge number of transformations.

Every transformation creates opportunities for assumptions to break.

I’ve lost count of how many times I’ve watched an editor silently modify content between the moment it was submitted and the moment it appeared on screen.

Most of the time it’s harmless.

Sometimes it isn’t.

The important lesson is that mXSS often begins with a mutation long before any JavaScript execution becomes possible.

One habit I’ve developed is spending time observing what the browser changes automatically.

Not what executes.

What changes.

When hunting mXSS, I frequently ask questions like:

These small mutations often reveal more than hundreds of payload attempts.

Some of my most interesting investigations started because I noticed the browser quietly transforming HTML in ways I didn’t expect.

The mutation itself was the clue.

The vulnerability came later.

Every researcher who spends enough time studying mXSS eventually ends up in the same place.

SVG.

MathML.

Namespaces.

I remember reading older research and wondering why so many talented researchers were obsessed with technologies that most applications barely use.

Then I understood the real lesson.

The issue isn’t SVG.

The issue isn’t MathML.

The issue is that browsers switch parsing rules depending on context.

Once different parsing modes become involved, assumptions begin to break.

And when assumptions break, mutations appear.

Whenever I encounter applications that support custom diagrams, SVG uploads, advanced editors, documentation platforms, or mathematical rendering engines, I immediately start paying closer attention.

Not because a vulnerability must exist.

But because complexity usually creates opportunity.

One area I think many researchers underestimate is automatic browser correction.

Browsers are incredibly forgiving.

Malformed markup gets repaired.

Broken structures get fixed.

Invalid trees get reconstructed.

Most users never notice.

Most developers never notice.

Bug bounty hunters should notice.

Whenever a browser “helps” by correcting content, I become curious.

Because the repaired version may be significantly different from the version originally inspected by the application’s security controls.

The more transformations involved, the more interesting the target becomes.

Over time my workflow has become much simpler.

When reviewing any feature that accepts user-controlled HTML, I usually ask myself the following questions:

None of these questions directly test for XSS.

That’s intentional.

I’ve found that modern mXSS research is often less about payloads and more about understanding the application’s rendering lifecycle.

Once you understand that lifecycle, the interesting bugs tend to reveal themselves naturally.

The most valuable lesson I’ve taken from recent mXSS research is that sanitization is not a final destination.

It’s merely one step in a much larger process.

Developers often think:

*“The sanitizer approved it, therefore it’s safe.”*

Researchers think:

*“What happens next?”*

That difference in mindset is where many modern findings originate.

The browser still has work to do.

The framework still has work to do.

The editor still has work to do.

And every additional step introduces another opportunity for the final DOM to differ from the original one.

Mutation XSS remains one of the most fascinating vulnerability classes because it rewards curiosity more than creativity.

The best mXSS researchers I’ve met are rarely the people with the biggest payload collections.

They’re the people who spend hours understanding how browsers think.

How parsers behave.

How rendering pipelines transform content.

How assumptions quietly break between one processing stage and the next.

These days, when I begin testing a target, I’m rarely looking for an XSS payload.

I’m looking for a mutation.

Because in my experience, that’s often where the real story begins.
