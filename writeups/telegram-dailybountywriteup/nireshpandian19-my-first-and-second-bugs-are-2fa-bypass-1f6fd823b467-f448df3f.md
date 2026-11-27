# MY FIRST AND SECOND BUGS ARE — 2FA BYPASS

- **Source URL:** https://medium.com/@nireshpandian19/my-first-and-second-bugs-are-2fa-bypass-1f6fd823b467?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211160848/https://medium.com/@nireshpandian19/my-first-and-second-bugs-are-2fa-bypass-1f6fd823b467
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/395 (id 395)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# MY FIRST AND SECOND BUGS ARE — 2FA BYPASS

Hey there guys,

This write up is about my very first bug and the second one that i found shortly after the first one, which are IMPROPER AUTHENTICATION CONTROLS that led to a 2FA bypass.

FIRST ONE :

The first bug was on a cryptocurrency wallet website, (lets call it redacted.com).

The bug was quite simple, an account with the 2FA authorization would recieve a response similar to

```
{
... ,
... ,
required: false
}
```
and would get redirected to the dashboard.

Whereas, a 2FA authentication enabled account would recieve a response similar to the below one.

```
{
... ,
... ,
required: true
}
```
I was pretty excited on seeing these parameters, and i immediately fired up my BURP proxy and intercepted these requests and obviously changed the required parameter’s value from true -> false, and guess what !

I was redirected to the dashboard due to the client side response manipulation, and BOOM ! I got all the details of the account, and in no time i was logged in to the account !

LESSON LEARNT : Always check for juicy parameters on the response.

SECOND ONE :

This was a bit tough to find, not because of it’s complexity, but it involved multiple endpoints which took time to find them.

This was an altogether different website, (lets call it bluedacted.com)

The first thing i checked here was the response of the login request, and to my excitement the response looked like

```
400 BAD REQUEST
.
.
.
{
error:"xxx",
message:"xxx",
need2FA:true
}
```
On noticing the juicy parameter -> “need2FA” , i was once again excited and in no time my burp was fired up and i tried out the same kind of response manipulation like the first one, and the same way i was redirected to the dashboard.

Unfortunately, that was it ! I was just redirected to the inner dashboard and option pages, but did not get the details of the user i tried to login.

Soon, i found out that the bluedacted.com website uses an Authorization token in it’s request, and this token is provided only if the 2FA step gets completed. This was enough to make my heart sink !

Since i manipulated the response, i never got my Auth token and all the requests made by my browser had this

`Authorization: Bearer undefined`
Neverthless, i did not give up, later that day when i was loittering around on the webpage, i came across an order page, where customers can order items, and it contained a LOGIN FORM which makes an ajax request to the server to fetch just the customer ID and the Name of the customer logging in.

SOON, i tried the credentials of my 2FA protected account and YEAH ! It got me my name and my customer ID without asking for the OTP.

This was not enough, I must escalate this to login to the account, as any sensible hacker would do, i went to my Developer tools and checked for the ajax responses made by my browser, and guess what !

The response was a JSON which had the details of my account and an Authorization token like

```
{
"customer_ID": 1452,
"name": Magma,
"token": xxxxxxxxxxxxxxxx
}
```
I rushed into the previous actual login page, and i replaced the Authorization: Bearer undefined -> with my actual token i got here, and

BOOOM !!! WE ARE BACK IN BUSINESS.

Once again it was a 2FA bypass !

LESSON LEARNT : Always spider around all the login pages and forms.

You could expect a lot of writeups, following this in the coming days !

Thank You
