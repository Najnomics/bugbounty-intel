# Broken Access Control #2

- **Source URL:** https://osintteam.blog/broken-access-control-2-i-flipped-one-cookie-from-false-to-true-and-walked-into-the-admin-6bf2988c28e7
- **Fetched from:** https://web.archive.org/web/20261116205606/https://osintteam.blog/broken-access-control-2-i-flipped-one-cookie-from-false-to-true-and-walked-into-the-admin-6bf2988c28e7
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14970 (id 14970)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken Access Control #2: I Flipped One Cookie From “false” to “true” and Walked Into the Admin Panel

*Part of my OWASP Top 10 series — taught from the basics up, with a live lab you can follow along at home.*

Back in Part 1 of this series, I deleted a user from a shopping site without ever logging in as an admin. The server simply forgot to check who I was. Classic Broken Access Control.

I got a few messages after that one saying, “okay but that felt too easy, surely real apps don’t mess up access control like that.” Fair. So let me show you a second flavour of the exact same bug — one that looks a little smarter on the surface, and is still completely broken underneath.

This time the website does check. It asks a question before it lets anyone near the admin panel: *“Are you an administrator?”*

The problem is who it asks.

It doesn’t ask its own database. It asks *your browser*. And your browser will happily say whatever you tell it to say.

Grab a coffee. This one is fun.

## A quick refresher: what is Broken Access Control?

If you read Part 1, skip ahead. If not, here’s the two-line version.

Access control is just the app deciding *what you’re allowed to do*. Can you see this page? Can you delete that user? Can you open the admin area? Broken Access Control is when those checks are missing, half-done, or — like today — based on something the attacker can change.

OWASP ranks it as the **#1** risk on their Top 10 for a reason. It’s everywhere, it’s easy to get wrong, and when it breaks, a normal user can suddenly do things only staff were ever meant to do.

Part 1 was the “no check at all” version. Today is the “check, but trust the wrong thing” version.

## The thing nobody tells beginners about cookies

Let’s talk about cookies for a second, because this whole lab lives and dies on one misunderstanding about them.

When you log into a site, the server needs a way to remember you on your next click. So it hands your browser a little slip of paper — a cookie — and your browser shows that slip back to the server on every request. That’s how the site “remembers” you’re logged in.

Here’s the part that matters: **cookies live in your browser. Which means they live on your computer. Which means they are yours to edit.**

A cookie is not a vault. It’s a sticky note. If a developer writes something sensitive on that sticky note and then trusts whatever it says later, you can just… rewrite the note.

Keep that picture in your head. The whole hack is literally rewriting a sticky note.

## The lab: “User role controlled by request parameter”

I used a free lab from **PortSwigger’s Web Security Academy** for this — a legal, intentionally broken site built for exactly this kind of practice.

*Goal: Access the admin panel and use it to delete the user carlos. Given to us: a normal, low-privilege account — wiener : peter.*


That’s it. We log in as a regular customer and have to end up deleting another user from an admin panel we’re not supposed to touch. Let’s go.

## Step 1 — Knock on the admin door (and get it slammed)

First thing I always do: try the obvious. I went straight to `/admin`.

No luck:

`Admin interface only available if logged in as an administrator`
Good. Two things just happened. One, the admin panel clearly *exists* at `/admin`. Two, the server is making a decision — it looked at my request and decided I'm not an admin. So now the only question in the world is: **where is that decision coming from?**

## Step 2 — Log in and look at what the server gave me

I logged in with `wiener : peter` like a normal user. Nothing fancy on screen. But I wanted to see the paperwork — the cookies the site handed me when I logged in.

You don’t need any hacking tools for this. Just your browser:

- Open your browser’s developer tools (right-click anywhere → **Inspect**, or press F12).
- Go to the **Application** tab (in Firefox it’s **Storage**).
- On the left, click **Cookies**, then your lab’s address.

And there it was, sitting in plain sight:

`Admin = false`
I actually laughed. The server wrote down whether I’m an admin… and then handed me the piece of paper. It’s trusting me to be honest about my own permissions. That’s like a cinema giving you a ticket that says “VIP: no” and letting you scribble on it before you reach the door.

## Step 3 — Rewrite the sticky note

So I did the obvious thing. In that same Cookies panel, I double-clicked the value `false` and typed `true` over it. One word.

`Admin = true`
No re-login. No password. No special tool. I literally edited a value in my own browser, the same way you’d rename a file.

## Get Zahid Hussain Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

If you prefer doing it the “proper” pentester way — the way I showed in Part 2 with Burp Suite — you can intercept the server’s login response and change the `Set-Cookie: Admin=false` line to `Admin=true` as it flies past. Same result, different scenery. For a bug this simple, the browser's own dev tools are more than enough, and honestly it makes the point land harder for beginners: *no tools, just a text edit.*

## Step 4 — Walk in and delete carlos

With my shiny new `Admin=true` cookie, I reloaded `/admin`.

The door opened.

A full admin panel — a list of users, each with a **Delete** button next to it. The server had asked my browser “are you an admin?”, my browser said “yep, says so right here,” and the server just… believed it.

I found `carlos`, clicked **Delete**, and the lab flipped to **Solved**.

From “you can’t come in here” to deleting other people’s accounts, in the time it takes to change one word.

## So what actually went wrong?

Let’s name it properly, because the whole point of this series is that you walk away able to *spot* these, not just repeat the steps.

The developer wasn’t lazy about checking. There was a real check: “is `Admin` true?" The mistake was *where they stored the answer*. They put the user's privilege level inside a cookie — data that lives on the attacker's machine and can be edited freely — and then trusted it on the way back in.

This is the golden rule of access control, and it’s the same lesson as Part 1 wearing a different outfit:

*Never trust the client to tell you who it’s allowed to be.*


Anything that comes from the browser — cookies, hidden form fields, URL parameters, headers — is a suggestion from a stranger, not a fact. The user controls all of it. Your server has to decide permissions using data *the user can’t reach*: the session on the server side, looked up against the real database.

## How a developer should actually fix this

If you build apps, here’s how you avoid becoming the villain of someone’s write-up:

- **Keep the role on the server, not in the cookie.** The browser should only hold a random session ID. The server looks that ID up in its own records to find out “oh, this is wiener, a normal user.” The user never gets to touch the part that says `admin`.
- **Check permissions on every sensitive action — server-side.** Don’t just hide the admin link in the menu. Actually verify, on the server, that this session is allowed to hit `/admin` and `/admin/delete` before doing anything.
- **Treat all client input as hostile.** Cookies, parameters, headers — assume every one of them has been tampered with, because one day one of them will be.
- **Deny by default.** If you’re not *sure* someone is allowed, the answer is no.

None of this is exotic. It’s just the discipline of never letting the user grade their own exam.

## Why this matters outside a practice lab

A cookie that says `Admin=false` sounds almost too silly to be real. But the *pattern* — trusting client-controlled data to make a security decision — is one of the most common ways real applications get owned. Swap "admin cookie" for "a hidden `user_id` field," or "a `role=user` parameter," or "an `isPremium` flag in local storage," and you're looking at bugs that have paid out real bounties and caused real breaches.

Once you internalise *“the client lies,”* you start seeing this everywhere. That’s the actual skill. The cookie edit is just the party trick.

## Key takeaways

- **Cookies are editable by the user. Always.** If a security decision depends on a cookie’s value, that decision is already broken.
- **Broken Access Control isn’t always a missing check** — sometimes the check is there, but it’s trusting data the attacker controls.
- The fix is boring and absolute: **store roles and permissions server-side, and re-check them on every sensitive request.**
- When you’re testing, your instinct should be: *where is this app getting its “yes you’re allowed” answer from — and can I reach that place and change it?*

I changed one word in my own browser and got the keys to an admin panel. No password, no exploit code, no tools you don’t already have installed. That’s how low the bar can be.

## What’s next

This was the second lab in my walk through **Broken Access Control**. If you missed the first one, start there — I delete a user with no admin login at all, and it sets up everything we did here:

👉 **Part 1 — Broken Access Control: I Deleted a User Without Logging In**

I’m writing this whole series the way I wish someone had taught it to me when I started — plain English first, then hands you can actually get dirty.

If this is your kind of thing, come hang out. I put all my free labs, courses and write-ups on [**bitcops.net**](https://bitcops.net), and we’ve got a growing community of learners breaking (and fixing) stuff together at [**community.bitcops.net**](https://community.bitcops.net) — bring your questions, your wins, and your “wait why did that work” moments.

See you in the next one.

*Written by Zahid Hussain Shah — ethical hacker and security instructor. Everything in this article was done inside PortSwigger’s free, intentionally-vulnerable Web Security Academy labs, which exist for exactly this kind of practice. Never test these techniques on systems you don’t own or don’t have explicit written permission to test. Unauthorized access is a crime, full stop. Learn on labs, hack what you’re allowed to hack, and use it to build safer software.*
