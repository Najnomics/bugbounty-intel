# An Easy RACE CONDITION Bug That Made Me Fame

- **Source URL:** https://medium.com/@hashimamin/an-easy-race-condition-bug-that-made-me-fame-97d6921ae7f4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240628155640/https://medium.com/@hashimamin/an-easy-race-condition-bug-that-made-me-fame-97d6921ae7f4
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6537 (id 6537)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# An Easy RACE CONDITION That Made Me Fame

Hey Hackers, This’s `mrhashimamin` And today I’ll talk about a `Race Condition` bug that i found on a Vulnerability Disclosure Program ( VDP ) on bugcrowd ( Let’s call it `target.com` ).

## What’s RACE CONDITION?

`Race conditions` are a common type of vulnerability closely related to `business logic flaws`. They occur when websites process requests concurrently without adequate safeguards. This can lead to multiple distinct threads interacting with the same data at the same time, resulting in a `collision` that causes `unintended` behavior in the application.

To take a deeper dive into this topic, I highly recommend reading this amazing [write-up](/@mora2023/race-condition-e93eb33b85d1).

## How i did it?

After decades of searching for a program that truly fits me :D, I finally found one, I started to use it like a real user `and this helps a lot`, noting everything such as `oh, i found a login page, register, reset function, ..etc`.

Now, looks like i have a good starting point and a focused mindset. So, i started with some basic tests for the login, register page and the password reset function.

Okay, i love this part. Every time i test the `reset function`, I brainstorm ways to achieve an Account Takeover (ATO), that’s really make me feel like a real hacker :D

So, I tried a lot of good techniques while testing the reset function. You can check out some of them in my last [Vulnerable Lab](/@hashimamin/0xhashimresetriddle-4f3270411800)

But sadly, I didn’t succeed :(

Hey you, we can’t just give up! ( `talking to myself :D` ). So, I kept testing the app. It’s a site for sharing `photos, posts, and memes`.

I made a new post and noticed there were `reactions` and `comments`, just like any social media app. I focused on `rate limiting` and tried to get some likes on my post using a `race condition`, but as usual, I failed xD.

When I saw the comment section, I had some ideas. First, You need to know that the site `doesn’t allow the publisher` to delete other users’ comments — `only the user can delete their own comment`. I tried to bypass that, but yeah, I failed again :(

Now, something really caught my attention — `the comment section` again. This time, I noticed that I could react to comments by `Upvoting/Downvoting` them, which affects user `reputation/points`. So, yeah, I tried a race condition here.

## Step by step

1- I registered `two users` on the app.

2- Uploaded an image using `user_1`.

3- Commented on this image using `user_2`.

4- Switched back to `user_1` and upvoted `user_2`’s comment.

5- I intercepted the API request using `Burp Suite`, and it looked like this:

6- I sent this request to the `Turbo Intruder` extension in `Burp Suite` using a simple Python script and hit the `Attack` button.

*Now, if we go to this comment, we see that we finally hacked it !!*

As you can see, when we sent the request to the endpoint `/vote/up?client_id=*` using `Turbo Intruder`, the `comment's points` decreased, and the `user's reputation/points` changed too.

*Who’s the fame now xD ??*

After that, I started writing my report to them, and I guess I’ll keep testing this app. It seems like it’s full of more surprises!

Thanks for joining me on this bug-hunting journey! Your support rocks. Let’s keep squashing bugs together! 🐜🛠️
