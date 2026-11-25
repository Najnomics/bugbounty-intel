# Referer-based access control — A portswigger lab walkthrough

- **Source URL:** https://vivek0x.medium.com/referer-based-access-control-a-portswigger-lab-walkthrough-6a273c21db3f
- **Fetched from:** https://vivek0x.medium.com/referer-based-access-control-a-portswigger-lab-walkthrough-6a273c21db3f?source=rss-a3d6c85e9637------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14936 (id 14936)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vivek Yadav / Mon, 05 Oct 2026 18:33:09 GMT

**Platform:** Portswigger’s web security academy

**Category:** Broken Access Control

**Lab:** Referer-based access control

The goal of this lab was to log in as the normal user wiener and exploit a broken access control mechanism to promote that account to an administrator.

I started by opening the lab and logging in with the administrator credentials provided in the description:

administrator:admin

I didn’t use the administrator account to solve the lab directly. I mainly used it to understand what the application considered an administrative action.

After logging in, I opened the Admin panel. There was a Users section where I could see users and perform two actions on them: upgrade and downgrade.

To understand how the upgrade functionality worked behind the scenes, I selected carlos and upgraded his account while Burp Suite was running.

Burp Suite captured the request responsible for the upgrade. It looked roughly like this:

GET /admin-roles?username=carlos&action=upgrade HTTP/2 

Host: \<LAB-ID>.web-security-academy.net

Cookie: session=\<ADMIN\_SESSION>

Referer: https://\<LAB-ID>.web-security-academy.net/admin

The interesting part was the /admin-roles endpoint.

I sent this request to Repeater because I wanted to see what would happen if I changed different parts of it.

At this point, I had a working request that could promote a user:

/admin-roles?username=carlos&action=upgrade

Next, I logged out of the administrator account and logged in as:

wiener:peter

I captured the request from this session in Burp Suite as well.

The important thing I needed from this session was the wiener user’s session cookie.

I then went back to the /admin-roles request I had saved in Repeater.

Instead of using the administrator’s session cookie, I replaced it with the session cookie belonging to wiener.

I also changed the username parameter from:

username=carlos

to:

username=wiener

So the **request** became:

GET /admin-roles?username=wiener&action=upgrade HTTP/2 

Host: \<LAB-ID>.web-security-academy.net

Cookie: session=\<WIENER\_SESSION>

Referer: https://\<LAB-ID>.web-security-academy.net/admin

The Response i got:

I sent the request.

The server accepted it, and wiener was successfully promoted to an administrator.

The lab was solved.

The interesting part of this lab is the Referer header.

The application was using the Referer header as part of its access-control logic. In other words, it was essentially trusting the request because it appeared to originate from the administrator page:

But the request was actually being sent using the session of the normal user, wiener.

This means the application wasn’t properly checking whether the authenticated user was genuinely authorized to perform the administrative action.

The Referer header is supplied by the client, so it should never be treated as proof that a user has administrator privileges.

The important thing here is that I didn’t need to obtain the administrator’s session cookie. I simply reused the administrative endpoint with my own authenticated session and supplied the expected Referer value.

The request that ultimately solved the lab was essentially:

The combination that mattered was:

The main takeaway from this lab was that authentication and authorization are two different things.

I was correctly authenticated as wiener, but I shouldn’t have been authorized to access the administrative functionality.

The application made the mistake of relying on a client-controlled header instead of checking the user’s actual privileges on the server side.

From a testing perspective, this was also a good reminder that whenever I find an interesting privileged request, I should try replaying it with a lower-privileged session. If the request still succeeds, there is a good chance that the application’s authorization checks are flawed.

Broken access control caused by relying on the HTTP Referer header to restrict access to administrative functionality.

The proper fix would be to perform server-side authorization checks based on the authenticated user’s privileges, rather than trusting headers such as Referer.

GoodByeee…
