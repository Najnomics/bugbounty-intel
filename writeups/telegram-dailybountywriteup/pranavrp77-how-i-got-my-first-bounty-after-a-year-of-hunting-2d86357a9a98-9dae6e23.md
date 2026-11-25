# How I Got My First Bounty After a Year of Hunting

- **Source URL:** https://medium.com/@pranavrp77/how-i-got-my-first-bounty-after-a-year-of-hunting-2d86357a9a98
- **Fetched from:** https://medium.com/@pranavrp77/how-i-got-my-first-bounty-after-a-year-of-hunting-2d86357a9a98?source=rss-fc921eebbf2e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14886 (id 14886)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Pranav Patil / Sat, 29 Aug 2026 06:46:24 GMT

So, hello everyone! My name is **Pranav Patil**. I’m a security researcher and, like many of you reading this, I’m also on the bug bounty journey.

I started doing bug bounty around a year to a year and a half ago. But honestly, I wasn’t very consistent.

First, college kept me busy. Then, after graduating, my job took most of my time. I would occasionally participate in bug bounty programs, hunt for a couple of days, and then move on.

And the result?

**I had many valid bugs that got me Hall of Fames, But No bounties.**

I had spent quite a lot of time learning about web security, reading reports, understanding vulnerabilities, and practicing different techniques, but I still hadn’t received my first bounty.

Then one day, an newly joined office friend who had great success in bug bounty told me something very simple:

***“You should just do bug bounty consistently.”***

That sounded obvious, but it actually changed the way I approached bug hunting.

I realized that one of my biggest problems wasn’t necessarily my technical knowledge. It was my consistency.

Whenever I started hunting on a target, I usually spent only two or three days on it. If I didn’t find anything interesting, I moved on to another target.

So this time, I decided to do something different.

I decided that I would pick **one target and give it at least a month**.

No matter whether I found a vulnerability or not, I wanted to understand the application properly instead of jumping from target to target.

I chose a self-hosted bug bounty program and started hunting for around **2–3 hours every day after office**.

For the first ten days, I spent most of my time understanding the application.

I explored different features, observed how users interacted with the application, looked at API requests, understood the application’s authorization model, and tried to build a mental map of how different parts of the application were connected.

Eventually, I submitted three vulnerabilities.

And guess what?

**All three were marked as duplicates.**

Obviously, getting three duplicates in a row isn’t exactly motivating.

But this time I had already made a decision:

**I was going to complete the one-month challenge no matter what.**

So I didn’t stop.

Instead, those ten days of testing had given me something valuable — **a much better understanding of the application.**

I knew what the important features were.

I knew how different users interacted with the application.

I had a better idea of how the application’s APIs worked.

And most importantly, I started noticing where the application’s authorization boundaries were.

After my third duplicate, I decided that I wanted to look for something more interesting.

That evening, after coming back from the office, I started hunting at around **10 PM**.

I wasn’t expecting anything special.

I was simply going through the application and testing the features I had already spent days understanding.

About an hour later…

**I found something.**

It was an authorization vulnerability that allowed an authenticated user to perform actions against another organization’s resources.

I submitted the report.

And this time, instead of another duplicate…

**The report was accepted.**

The vulnerability was rated **High severity**, and I received my **first $100 bounty**.

After spending more than a year trying to get that first bounty, it finally happened.

And interestingly, the vulnerability wasn’t some extremely complicated exploit chain.

It came from something that every web application security tester should understand very well:

**Broken access control.**

I found this in March but I was just delaying this write-up don’t know why:) but here’s it now . So, let’s look at what I found.

For this article, I’ll refer to the target as:

**redacted.com**

I won’t disclose the real application, organization IDs, or any other identifying information.

The vulnerability was essentially an **Cross Tenant IDOR / Broken Access Control vulnerability** in organization-level APIs.

The application was a multi-tenant SaaS platform where different users belonged to different organizations.

For example:

Organization A

├── User A

├── Branch A1

└── Branch A2

Organization B

├── User B

├── Branch B1

└── Branch B2

A user from Organization A should obviously not be able to create branches or add users to Organization B.

That was exactly what I tested.

While exploring the application as a normal user, I reached the organization settings area.

There were several administrative functions, including:

I intercepted the requests using Burp Suite.

The application was making API requests where the organization identifier was included directly in the URL.

Conceptually, the request looked like this:

POST /api/company/\<organization\_id>/branches/

For example, when I was logged in as a user belonging to Organization A:

POST /api/company/ORG\_A/branches/

At first, this looked normal.

The interesting question was:

***What happens if I replace*** ***ORG\_A with the ID of another organization?***

This is a classic authorization test.

The important thing here wasn’t simply changing an ID.

The real question was whether the **server would verify that my authenticated account was actually authorized to perform the requested action on that organization.**

I used two separate accounts belonging to two different organizations.

Let’s call them:

User A → Organization A

User B → Organization B

I first performed the legitimate action as User A and captured the request.

Then I modified only the organization identifier in the request.

Conceptually:

was changed to:

POST /api/company/ORG\_B/branches/

I sent the modified request.

The server accepted it.

The response indicated that the operation was successful, and when I checked Organization B, the new branch had actually been created there.

That was the moment I knew I had found something interesting.

**User A was authenticated, but User A was not authorized to modify Organization B.**

Yet the server allowed it.

I didn’t stop after finding the branch creation issue.

Whenever I find an authorization vulnerability, I try to understand its **scope**.

I asked myself:

*“Is this only one vulnerable endpoint, or is there a broader authorization problem?”*

The application also had functionality for adding users/team members to an organization.

The request followed a similar structure:

POST /api/company/\<organization\_id>/team-members/

Again, I tested the request using User A.

Then I replaced Organization A’s identifier with Organization B’s identifier.

The server again accepted the request.

This time, a user could be added to the other organization.

So the issue wasn’t limited to one endpoint.

It affected multiple organization-level operations.

A common misunderstanding about IDOR is:

*“If I can change an ID, it’s automatically an IDOR.”*

That’s not quite correct.

The important part is **authorization**.

An application can expose predictable IDs without necessarily being vulnerable.

The vulnerability exists when the server accepts an object identifier supplied by the user **without verifying whether that user is authorized to access or modify that object.**

In this case, the server effectively trusted:

/api/company/\<organization\_id>/

without properly checking:

Does the authenticated user have permission to modify this organization?

The missing authorization check created a cross-tenant access-control issue.

Another interesting part was that organization identifiers appeared to be sequential.

That made testing easier because an attacker could potentially identify other organization IDs instead of needing to discover completely random identifiers.

However, it’s important to understand that **predictable IDs were not the root cause of the vulnerability.**

Even if the organization IDs were random UUIDs, the application would still be vulnerable if an attacker could obtain another valid organization ID and use it to perform unauthorized actions.

The real vulnerability was:

**Missing server-side authorization.**

The impact was significant because this was a multi-tenant application.

A normal authenticated user belonging to Organization A could potentially perform organization-management operations against Organization B.

The demonstrated impact included:

An attacker could create branches inside another organization.

An attacker could add users/team members to another organization without being authorized to manage that organization.

The application was supposed to isolate organizations from each other.

Instead, a user from one tenant could modify resources belonging to another tenant.

The severity could become even higher depending on what permissions were available when adding users.

For example, if an attacker could control roles or permissions assigned to the newly added user, the issue could potentially lead to more serious privilege escalation or unauthorized access.

In my case, I reported the demonstrated impact rather than claiming impacts I hadn’t verified.

That’s an important lesson when writing bug bounty reports:

***Report what you can prove. Don’t inflate the impact with hypothetical scenarios.***

Before submitting the report, I made sure the behavior was reproducible.

My basic validation process was:

Account A

↓

Organization A

↓

Perform legitimate action

↓

Capture API request

↓

Replace Organization A ID

↓

Organization B ID

↓

Send request

↓

Server accepts request

↓

Verify change in Organization B

I repeated the same methodology against the user-management functionality.

This gave me confidence that the issue wasn’t a UI bug or an accidental display problem.

**The backend itself was accepting an unauthorized cross-organization modification.**

Looking back, the most valuable part of this bounty wasn’t the $100.

It was the process that led to it.

For the first ten days, I didn’t find a valid bug.

I got three duplicates.

But those ten days weren’t wasted.

They helped me understand the application.

And that understanding eventually allowed me to ask the right question:

***“What happens if I perform this action against an organization that doesn’t belong to me?”***

That question led to my first bounty.

It also taught me something important about bug bounty hunting:

**You don’t always need a complicated exploit.**

Sometimes the vulnerability is hidden behind a simple API request.

The difficult part is understanding the application’s logic well enough to recognize what shouldn’t be possible.

One Regret I had now is if I submitted 2 separate reports for this bug as 2 different API endpoints were vulnerable, I would I got 2 valid reports with $200 as bounty :) But I was so excited when I found this bug that I forgot I can do this and get more bounty, but no worries first bounties are always special regardless of bounty amount

If you’re currently doing bug bounty and haven’t received your first bounty yet, I completely understand how frustrating it can feel.

You might spend days hunting and find nothing. You might submit reports that get closed. You might get duplicates.

You might start wondering whether you’re actually good enough.

I had all of those thoughts.

But my first bounty came when I stopped focusing on finding a vulnerability quickly and started focusing on **understanding the target deeply.**

Instead of:

*“What vulnerability can I find today?”*

I started thinking:

***“How does this application actually work, and where does its security model break?”***

That small change in mindset made a huge difference.

And after more than a year of trying, I finally got my first bounty **$100.**

Maybe it’s not a huge amount of money.

But for me, it was proof that the time I had spent learning, practicing, failing, getting duplicates, and continuing to hunt was finally starting to pay off.

And honestly?

**That first bounty felt pretty damn good.** 😄

If you’re still waiting for yours, keep learning, keep testing, and most importantly — **stay consistent.**

Your first valid finding might be one good question away.

More bug bounty write-ups are on the way, make sure to follow me for more coz it’s free:)

Follow me on [X/Twitter](https://x.com/0xlevi_87)

Connect me on [linkedIn](https://www.linkedin.com/in/pranav-patil-19281322b/)
