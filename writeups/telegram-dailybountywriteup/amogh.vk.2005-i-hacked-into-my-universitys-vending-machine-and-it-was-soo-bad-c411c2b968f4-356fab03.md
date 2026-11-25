# I Hacked into my University’s Vending Machine And it was soo BAD!

- **Source URL:** https://medium.com/@amogh.vk.2005/i-hacked-into-my-universitys-vending-machine-and-it-was-soo-bad-c411c2b968f4
- **Fetched from:** https://infosecwriteups.com/i-hacked-into-my-universitys-vending-machine-and-it-was-soo-bad-c411c2b968f4?source=rss-df316a97e72f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14896 (id 14896)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Amogh V K / Wed, 02 Sep 2026 19:16:45 GMT

Okay some time ago i hacked into the vending machine which is in MIT-BLR ( *J Vend* ) iykyk, which now I’m opening it to everyone.

Before I begin Im not here to leak the apk also not here to say HOW I DID IT coz it will definitely cause me trouble ( Though i didnt exploit it myself as its againt my principles) but I can give you hints how you can do it.

I’ve seen people say they tired and they failed it’s just that they suck at it that’s all. took me a few weeks to figure it out found a shit load of vulnerabilities \* aka its worse than a vibe coded app \*

I mean who in the world just puts their auth key, user name and password hardcoded into the front end? like seriously dude? its in prod!!!!

but for the first time I thought about being a soo called *Responsible Citizen* i.e keeping it private and I mailed the company and its founders, and guess what?

*NO REPLY*

So I thought..

fine.

If you won’t listen to me privately, let’s talk publicly.

Soo why am I posting this?

I think that Hacking is bad, *I guess*? but what ever listing out vulnerability isn’t.

Soo imma give all my findings and lets see who gets there first

from the TOP you log in via google mail

↓

You get assigned a user ID where all the orders and history is stored

↓

you place an item to cart and order ID is assigned and you press pay

↓

the server send the item price from the DB to the app aka hard( Im not shitting devs that’s how bad the design is )

↓

and the app fires Razorpay with that money

↓

you pay and when its sucessful and the back-end verifies the you click vend and the item vends.

then the main scrutiny starts. the server fetches the db price with the order id and the amount payed, if razor pay amount you paid associated with the order id is == the product price in DB, wallah the server fires GET myorder.php?… the motor in the vending machine and it vends or else it dosent.

now let’s get into the fun part a test for you if you know any thing about true hacking.

it’s purposeful btw not a typo

here is how a regular human things,

If this came into your mind even after reading the first half this isn’t for you. better luck trying for the next decade.

Now I will list the true vulnerability.

Where does it fit in?

yep.

*/phpmyadmin*

Tho it sounds easy it isn’t.

Obv the user has changed the password and now we need to find if the user actually exists.

How do we find out?

my boy SQL INJECTION will help.

And yes, this is where things start getting interesting.

I found that the application had exposed information that should absolutely not have been exposed to the client.

Using CVE-2017–1000017 The acess was denied for the hardcoded username with password:yes, if you think we failed this ain’t ur domain coz we won, what it means for me is that the user exists in the database.

The hardcoded credentials weren’t just some random useless strings sitting inside the APK.

They pointed towards an actual backend account.

But the password had been changed.

So now we have a username.

But wab password?

This is where another problem comes in.

The admin kept the rate limiting off.

If you know what this means then you also know what to do.

I’m not going to give you the exact commands or the exact attack chain here because I’m not trying to hand someone a ready made way into somebody else’s server.

But the important part is the vulnerability itself.

An authentication endpoint with sensitive access behind it and no proper rate limiting is basically asking to be abused.

And that’s enough data for you to get in. I did it and now its your turn.

The funny thing is everyone who tried before me immediately thought about the vending logic.

“Can I just make it vend without paying?”

“Can I change the price?”

“Can I reuse the order?”

“Can I force the motor?”

“Can I fuck with Razorpay payment signatures and end up in jail?

That’s not what made me spend weeks looking at this.

The interesting part was the architecture around the application.

The frontend trusted things it absolutely shouldn’t have trusted.

Sensitive information was sitting where a client could inspect it.

Backend endpoints exposed functionality that needed much stronger authentication and authorization.

And some of the security controls that should have existed simply… didn’t.

Again, I’m not posting the APK.

I’m not posting the credentials.

I’m not posting the exact exploit chain.

I’m not posting instructions for breaking into the actual system.

I’m posting the findings because there is a massive difference between saying “I found a vulnerability” and publishing everything required for someone else to abuse it.

not trynaa BRAG about it but yeah Before making this public I actually tried doing the boring responsible thing.

I contacted the company.

I contacted the founders.

I explained that I had found security issues.

I waited.

And waited.

And…

*NO REPLY.*

So yeah.

At some point I figured if nobody wants to listen privately, I might as well document what happened publicly.

I’m not saying I’m some cybersecurity god.

I’m not saying this was some NASA level shit.

But for a vending machine?

There were way too many things wrong with it.

The biggest thing is pretty simple.

Never trust the client.

If your app contains your secrets, they’re not secrets.

If your authentication endpoint has no meaningful protection against repeated attempts, that’s a problem.

If your backend assumes the frontend will behave correctly, that’s a problem.

If your payment system is secure but everything around it isn’t, the payment system being secure doesn’t magically save the application.

And if you’re building a vending machine application…

maybe don’t accidentally turn it into a cybersecurity lab.

That’s basically it.

I found a bunch of shit.

I reported it.

I’m not leaking everything because I’m not stupid.

But I’m also not going to pretend nothing happened.

Soo yeah.

If the company wants to reach out and actually talk about the vulnerabilities, my inbox exists.

Until then… lets see who gets to who first.

*J Vend to me or you guys to them. Lets see what happens!*

[I Hacked into my University’s Vending Machine And it was soo BAD!](https://infosecwriteups.com/i-hacked-into-my-universitys-vending-machine-and-it-was-soo-bad-c411c2b968f4) was originally published in [InfoSec Write-ups](https://infosecwriteups.com) on Medium, where people are continuing the conversation by highlighting and responding to this story.
