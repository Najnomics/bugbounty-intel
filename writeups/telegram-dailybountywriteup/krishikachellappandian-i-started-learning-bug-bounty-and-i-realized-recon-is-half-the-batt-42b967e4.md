# I Started Learning Bug Bounty, and I Realized Recon Is Half the Battle

- **Source URL:** https://medium.com/@krishikachellappandian/i-started-learning-bug-bounty-and-i-realized-recon-is-half-the-battle-fee2a5ff940f
- **Fetched from:** https://medium.com/@krishikachellappandian/i-started-learning-bug-bounty-and-i-realized-recon-is-half-the-battle-fee2a5ff940f?source=rss-ad84bc00e8f1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14956 (id 14956)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** h3xiee / Thu, 22 Oct 2026 11:02:12 GMT

**At First, I Thought Bug Bounty Was About Finding Bugs**

When I first started learning bug bounty, I thought the process was pretty straightforward.

Learn XSS.

Learn SQL Injection.

Learn IDOR.

Learn SSRF.

Learn CSRF.

Learn authentication vulnerabilities.

Practice them. Find a bug. Report it.

Simple, right? Not quite.

After spending more time learning web security, I started realizing something I hadn’t expected:

Knowing how vulnerabilities work is only one part of bug hunting. The other part is figuring out where to look in the first place . And that’s where recon changed the way I look at a target.

One of the biggest things I learned is that a website is rarely just the website you see.

Imagine a company owns example.com.

You might visit it and see a homepage, products, about, and contact page.

But the actual infrastructure can be much larger

example.com

│

┌───────────────┼───────────────┐

│ │ │

▼ ▼ ▼

www.example.com api.example.com admin.example.com

│ │ │

▼ ▼ ▼

Web App API Server Admin Portal

│

┌─────────┼─────────┐

▼ ▼ ▼

/users /orders /profile

And that’s still a simplified example.

There could also be

Each asset may expose different functionality. That doesn’t automatically mean any of them are vulnerable. But they expand the attack surface. And if you don’t know they exist, you can’t investigate them. It made me realize that finding the right places to look is just as important as knowing what to look for.

Reconnaissance, usually shortened to recon, is the process of gathering information about a target and understanding its attack surface.

But I think there’s a better way to describe it:

***Recon is the process of turning an unknown target into something you understand.***

You’re trying to answer questions such as:

The goal isn’t simply to collect a massive amount of information.

It’s to build a picture.

This is the step that’s easiest to skip, and it’s the one that matters first.

Every bug bounty program has a policy page. It tells you what you’re allowed to test and what you’re not.

It usually looks something like this:

IN SCOPE

\*.example.com

api.example.com

Example mobile app (Android, iOS)

OUT OF SCOPE

blog.example.com (hosted by a third party)

status.example.com

Denial of service testing

Social engineering

The scope is not a formality.

It decides which assets you can investigate, which findings will be accepted, and which actions could get you banned from the program.

A wildcard like \*.example.com is a big hint too. It's the company telling you: "We know there's a lot under this domain. Go find it."

So recon doesn’t start with a tool.

It starts with reading.

One thing that surprised me is that a lot of recon can happen without touching the target at all.

PASSIVE RECON                         ACTIVE RECON

(you never contact the target) (you interact with the target)

• Public records & search engines • Visiting pages and following links

• Certificate logs • Checking which hosts respond

• Archived versions of the site • Looking at HTTP responses

• Public code & documentation • Exploring features as a user

• DNS data from public sources • Probing for endpoints

Passive recon is quiet. It builds your first map from information that’s already public.

Active recon is where you start knocking on doors. It gives you much better detail, but it’s also where scope and program rules really start to matter.

From the writeups and videos I’ve been learning from, I noticed a common pattern : start passive, build a picture, and then go active with a plan.

One thing I found surprisingly interesting was how subdomains can be discovered from public information.

I used to imagine subdomain discovery as guessing names. Some of it is. But a lot of subdomains are simply sitting in public places:

┌──────────────────────────┐

│ Certificate logs │ trusted HTTPS certificates

│ │ are publicly logged

└────────────┬─────────────┘

│

┌──────────────┐ ▼ ┌──────────────┐

│ Search │──────► SUBDOMAIN LIST ◄───────│ Web archives │

│ engines │ ▲ │ │

└──────────────┘ │ └──────────────┘

┌────────────┴─────────────┐

│ JavaScript & public code │ apps mention their

│ │ own hosts constantly

└──────────────────────────┘

The certificate transparency part was especially interesting to me.

When a company sets up HTTPS for staging.example.com, that certificate gets recorded in public transparency logs. Anyone can search them. So a host the company never linked to anywhere can still be discoverable.

Tools mostly automate collecting from these sources. Understanding where the data comes from made the tools make sense to me.

And once you have a list, the real questions start:

Every time a server responds, it tells you a little about itself.

Some clues are in the headers:

HTTP/1.1 200 OK

Server: nginx

X-Powered-By: Express

Set-Cookie: session=...; HttpOnly; Secure

Content-Type: application/json

From these headers, you can start forming a picture of the technology and how the application is communicating: nginx, Express, cookie-based sessions, and a JSON response.

One clue that’s easy to underestimate is the status code.

200  OK            →  it exists and I can see it

301/302 Redirect → it sends me somewhere (often a login)

401 Unauthorized → probably exists, but I need to log in

403 Forbidden → probably exists, but I'm not allowed in

404 Not Found → nothing here (or so it says)

That difference between 401, 403 and 404 is quietly useful.

A 404 on /admin tells me very little. A 403 on /admin suggests something is there, and the server is keeping me out

That doesn’t make it a vulnerability. But it tells me where the walls are, and walls are worth understanding.

Websites publish a few files on purpose, and they’re more revealing than I expected.

https://example.com/robots.txt            →  pages search engines are asked NOT to index

https://example.com/sitemap.xml → a list of pages the site wants indexed

https://example.com/.well-known/security.txt → how to report security issues

https://api.example.com/docs → API documentation (sometimes public)

robots.txt is my favourite example of this. A company might write:

User-agent: \*

Disallow: /internal/

Disallow: /beta-dashboard/

The intention is “search engines, please don’t index these.”

For a security researcher, it can also reveal paths that aren’t prominently linked from the public site, which makes them worth understanding

And API documentation, when it’s public, can be an entire map of the backend handed to you in a neat, organised format: every route, every expected input, sometimes even example requests.

None of this is hacking. It’s reading what the site has already published.

The pages you click through are usually a tiny slice of what an application responds to.

What I click                    What actually exists

──────────────────── ────────────────────────────

/products /api/v1/products

/login /api/v1/auth/login

/profile /api/v1/users/{id}

/api/v2/users/{id}

/api/v1/users/{id}/export

/account/preferences

/admin/dashboard

Notice the v1 and v2. When an API has multiple versions, the older one sometimes stays running alongside the new one, and it may not have received every improvement the new one did.

Then there are parameters, the inputs an application accepts:

https://example.com/orders?id=1042&view=summary

└──┬──┘ └────┬─────┘

which order how to show it

Every parameter is the application saying, “I’ll take input from you here.”

Instead of immediately thinking, “What payload should I try?”, I’m learning to ask a different question:

*What does this input control, and does the server check whether I’m allowed to control it?* That single question sits behind a whole family of real-world bugs, especially access control issues like IDOR.

Modern web apps ship a lot of their logic to the browser. And that code has to know how to talk to the backend.

So it often contains something like:

const API\_BASE = "https://api.example.com/v1";

```
const endpoints = {
    profile:  "/user/profile",
    orders:   "/user/orders",
    export:   "/user/export",          // no button for this in the UI
    invite:   "/team/invite"
};
```
```
if (user.features.includes("beta_reports")) {
    showReportsTab();
}
```
In a few lines, the frontend has told me:

Two things that made JavaScript even more interesting to me:

**Frontend checks are not security.** If the only thing hiding the Reports tab is that if statement in my browser, the real question is whether the server enforces the same rule.

**Source maps exist.** Production JavaScript is usually minified into an unreadable blob. But sometimes a .map file is left alongside it, and the browser can use it to show the original, readable code sometimes including original file names and comments.

The interface shows you what the company wants you to use.

The JavaScript often shows you what actually exists.

Websites change constantly. Pages get removed. Features get retired. Whole subdomains disappear.

But web archives keep snapshots of pages over the years, along with the URLs they once linked to.

2019 ──── /api/v1/reports/download?file=

2021 ──── /beta/new-dashboard

2023 ──── /api/v2/reports

2026 ──── (homepage redesigned, old links gone)

The links are gone from the site. That doesn’t always mean the endpoints behind them are gone from the server.

History is also just good context. Seeing how an application evolved helps explain why its current structure looks the way it does, including the odd leftover pieces.

This is the lesson that keeps me honest.

Recon produces a lot of things that feel exciting:

Found                              What it actually is

───────────────────────────── ──────────────────────────

admin.example.com a lead

A 403 on /internal/ a lead

An old /api/v1/ endpoint a lead

A feature flag in JavaScript a lead

A staging subdomain a lead

Every one of these is a lead. None of them is a vulnerability by itself.

A vulnerability is when you can show real impact: someone can see, change, or do something they shouldn’t be able to.

**Recon gives you leads. Testing tells you whether they matter.**

Once I started exploring recon tools, I ran into a classic beginner mistake: trying to collect everything.

It is easy to end up with:

Thousands of URLs

Hundreds of subdomains

More parameters than you can count

And absolutely no idea what to do with any of it.

That’s when I learned the difference between two things that look similar:

DATA COLLECTION                      RECON

"Here is everything I found." "Here is what I found, what matters,

and how the pieces connect."

Imagine two researchers looking at the same target.

Researcher A has a huge list of URLs but doesn’t know what most of them do.

Researcher B has a smaller list but understands it: which app each URL belongs to, which ones need a login, and which ones are worth a closer look.

Researcher B is much more likely to find something real.

Tools are great at collecting information quickly. But they can’t tell you which result actually matters. That part needs human thinking.

Everyone has the same tools. What makes the difference is what you do with the results.

This is something I’m trying to build as a habit early.

It’s easy to spend an evening on a target, come back three days later, and remember almost nothing. Which host had the odd redirect? Where was that feature flag?

Here’s the simple notes format I’m practising with

TARGET: example.com

SCOPE: \*.example.com, mobile app | NOT: blog, status

ASSETS

app.example.com main product, React + JSON API

api.example.com v1 and v2 both respond

staging.example.com login page, 403 on most paths

INTERESTING

- /user/export in JS, no button in UI

- feature flag "beta\_reports"

- v1 /users/{id} still live

QUESTIONS

- Does v1 check permissions the same way as v2?

- Who is supposed to see beta\_reports?

TESTED / RULED OUT

- /admin → proper 403, redirects to SSO

The “Questions” section has become the most important part.

Writing down what I don’t understand yet turns out to be the best way to decide what to do next.

And the “Ruled out” section stops me from testing the same dead end twice.

I used to think of recon as a straight line — discover subdomains, then URLs, then parameters, then test.

In practice it looks a lot more like this:

┌──────────────────────┐

│ Discover something │◄─────────┐

└──────────┬───────────┘ │

▼ │

┌──────────────────────┐ │

│ Understand it │ │

└──────────┬───────────┘ │

▼ │

┌──────────────────────┐ │

│ Ask a new question │ │

└──────────┬───────────┘ │

▼ │

┌──────────────────────┐ │

│ Investigate more │──────────┘

└──────────────────────┘

Here’s an example of how one thing leads to another:

Imagine a JavaScript file mentions api.example.com/v1, but the website itself uses v2.

That raises a question: does v1 still respond?

If it does, the next step is comparing how the two versions handle the same request.

At that point, you’ve moved into testing, but you got there by following questions, not by running down a checklist.

Recon made me realize bug bounty isn’t one skill. It’s several, stacked on top of each other:

Bug Bounty

│

┌────────────┼────────────┐

▼ ▼ ▼

HTTP Web architecture JavaScript

│ │ │

└────────────┼────────────┘

▼

APIs & Recon

│

▼

Authentication & Authorization

│

▼

Business logic & Testing

│

▼

Chaining findings & Writing reports

Each layer makes the next one easier. Understanding HTTP made APIs click. Understanding APIs made authentication make sense. Understanding authentication is what makes authorization bugs visible.

I’m not an expert, and I’m genuinely enjoying not being one yet. Right now my goal is simple: learn to think like a security researcher, not just operate security tools.

It’s what tells you where the battle is.

*If you’re on the same path, I’d love to hear how you approach recon, and what you wish you’d known when you started*

Until the next lead — keep your notes messy and your questions honest. :)
