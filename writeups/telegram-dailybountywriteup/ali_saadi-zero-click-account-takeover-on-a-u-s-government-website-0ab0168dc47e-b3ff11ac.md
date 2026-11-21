# Zero-Click Account Takeover on a U.S. Government Website

- **Source URL:** https://medium.com/@ali_saadi/zero-click-account-takeover-on-a-u-s-government-website-0ab0168dc47e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250716064836/https://medium.com/@ali_saadi/zero-click-account-takeover-on-a-u-s-government-website-0ab0168dc47e
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10178 (id 10178)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Zero-Click Account Takeover on a Government Website

Since this is my first article here, let me quickly introduce myself: 

I’m Ali Saadi, a full-stack web developer, web security researcher, and a law student from Iraq.

Alright, that’s enough about me, let’s talk about how I could take over any user’s account on a government website without the user clicking a single thing.

For the most part, I’m not really a recon guy, I only do recon when I absolutely have to. Usually, I just like to hop on the main domain and start hacking. And guess what? Most of the time, I actually find some pretty cool stuff.

This time, my target was a government website. But keep in mind, the report hasn’t been publicly disclosed yet, so I can’t share the program’s name. The program had a bunch of domains, so, as usual, I picked one and started messing around with the main domain.

While going through requests in Burp history, trying to understand the authentication mechanism, I noticed the web app was encrypting the request body for important actions like login, sign-up, reset-password, etc., before sending it to the backend. Maybe to stop script kiddies, who knows?

Since the encryption was done client-side, I downloaded some JavaScript files and spent hours digging through minified JS like a freak, trying to understand the encryption algorithm and maybe even find the encryption key.

After hours of sifting through thousands of lines of minified JS, I found a very interesting piece of code…

Voila! Now, you might be thinking, “Ali, what the hell is even that?”

So let me break it down for you…

This code handles password resets. It’s triggered when you visit the password reset page at:

“**https://www.redacted.com/some-path/resetpassword?uuid=password-reset-token”** and submit the form with a new password.

Now, let’s take a closer look at this part of the code:

```
const z = v.password;
const xe = localStorage.getItem("loggedInApplicantUser"); 
this.userInfo = JSON.parse(xe); 
const je = this.userInfo?.userName;
```
## Here’s what’s happening:

- “**v.password**” is just pulling the new password value from the form, then saving it in a variable called “**z**”.
- Then it grabs a value from “**localStorage**” called
“**loggedInApplicantUser**”. That value is expected to be a JSON string, so it gets parsed.
- And finally, it pulls out the “**userName**” field from that parsed object and stores it in a variable called “**je**”.
- After some digging, I found out that “**userName”** here actually refers to the email of the account, not a traditional username.

Keep “**z**” and “**je**” in mind, you’ll need them to understand the next part.

## Now for the juicy part “**null == this.uUID ? … : …**”

This is where things get interesting…

In **JavaScript**, this is called a ternary operator, basically a mini if-else. It checks if “**this.uUID”** is null:

- If “**this.uUID”** is null (or undefined):
this is the case for when you visit the password reset url without providing a password reset token. For example,
“[**https://www.redacted.com/some-path/resetpassword?uuid=**](https://www.redacted.com/some-path/resetpassword?uuid=%60)”
in this case, the web app would call “**resetPasswordForApp(z, je)”** and pass the new password as “**z**” and the “**userName**” as “**je**” to it.
- If “**this.uUID**” is NOT null:
That means a password reset token was provided in the URL (as uuid), for example,
“[**https://www.redacted.com/some-path/resetpassword?uuid=acde070d-8c4c-4f0d-9d8a-162843c10333**](https://www.redacted.com/some-path/resetpassword?uuid=acde070d-8c4c-4f0d-9d8a-162843c10333%60)”
in this case, the web app would call “**resetPassword(z, this.uUID)**” and pass the new password as “**z**” and the “**uUID**” to it.

**Have you spotted the vulnerability yet?**

What if we manipulate “**localStorage**” and insert the victim’s email as the “**userName**”, then visit the password reset page without a “**uuid**”?

Like this:

“[**https://www.redacted.com/some-path/resetpassword?uuid=**](https://www.redacted.com/some-path/resetpassword?uuid=%60)”

Well… that’s exactly what I did.

And yeah, it worked.

I opened DevTools in the browser and added the following values:

```
"key" : "loggedInApplicantUser"
"value" : {"userName": "victim's email"}
```
then navigated to “[**https://www.redacted.com/some-path/resetpassword?uuid=**](https://www.redacted.com/some-path/resetpassword?uuid=%60)” (notice the uuid is empty). typed in a new password, submitted the form, and received a 200 response with the message “**Password updated for user victim\_email**”. simple isn’t it?

I also found several user IDs being leaked in the Wayback Machine, which could be used to enumerate emails. I reported the whole thing as Critical, but the security team had a different opinion and closed it as Medium, claiming the attack complexity was high. But hey, it’s a VDP after all. Not the end of the world.

I requested disclosure back in February, but never got a response. so I decided to share the technical details of the vulnerability without disclosing the program name or anything that could lead to it. also, the vulnerability has been already fixed since February and is not reproducible anymore.

Please keep in mind that this was reported almost a year ago. I rarely do VDPs now, and when I do, it’s either automation, or for research purposes and trying out new techniques.

Now, you might be thinking…

Ali, what happened to that whole ‘understanding the encryption algorithm’ and ‘finding the encryption key’ thing?


Well… after reporting this, I had to go to court for summer practice. 

And after a while, let’s just say I either forgot about it… 

or maybe just lost the passion for a bit (:

I came back after a while and started hacking on other programs, specifically a Chinese company. and, well, let’s just say I got scammed. But that’s a story for another day. as for now, have a good day.

Final Disclaimer: 

This post is shared in accordance with the platform’s guidelines, no identifying info or exploit paths were mentioned.
