# IDOR leads to Account Takeover of all users (ATO).

- **Source URL:** https://medium.com/@xnum.1/idor-leads-to-account-takeover-of-all-users-ato-27af312c8481?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240605034648/https://medium.com/@xnum.1/idor-leads-to-account-takeover-of-all-users-ato-27af312c8481?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5969 (id 5969)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I was able to discover ATO Via IDOR vulnerability

Hello everyone ,

I’m Ahmed Tarek, Today I would like to share with you my second IDOR discovery in HackerOne ’s program, This is my 1st article so if there is any mistakes , leave on it or DM me on facebook. Without wasting any time we will start on article.**So let’s get started! 😉**

*Let’s consider the target as target.com . I quickly signed up with necessary information and created & Verified both accounts for testing purpose Account 1 & Account 2 in the same time.*

When I tried accessing the profile from both accounts, I noticed something kinda fishy. The application sends a request to an endpoint called `/api/v1/user/profile` to view the profile. Let's dissect the request, shall we?

For *Account 1*

```
GET /api/v1/user/profile?
user_id=273948261&auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWI
iOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxw
RJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c×tamp=1349328731
```
Now, pay close attention to the `user_id`: `273948261`. It's crucial, and here's why. When we peek at *Account 2* 

```
GET /api/v1/user/profile?
user_id=273948262&auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ
zdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkF0dGVudG9yIiwiaWF0IjoxNjQ5MjQwNjcwL
CJleHAiOjE2NDkyNDExNzB9×tamp=1349328732
```
Notice the subtle difference? The user ID in *Account 2* `user_id` in *Account 2*`user_id` increased by one from *Account 2 .*

Now, here’s the catch. The application is supposed to validate the user through three things: `user_id`, `auth_token`, and `timestamp`. But does it really do that?

I tried changing the `user_id` from the attacker to the user, but it gave me a bad request. So, it seems like it's validating the token, right? Wrong.

Upon further investigation, I realized that the application doesn’t validate the token’s validity based on the token itself. Instead, it validates it based on the `timestamp` so if the`timestamp` is right, and even if the token is wrong but it will accept the request.

lets explain it more

once a token is generated, it remains valid for 60 seconds from the time it was create, if the token is used after this 60-second period, it is considered expired and be invalid.

in our application, the timestamp increments by 1 every 10 seconds. After 60 seconds, it deems the token invalid. So, if the `timestamp` was `1349328731`, and a request sent 10 seconds later it will increase by 1 and the `timestamp` will be `1349328732` and would be accepted. But after 60 seconds, it will increase by 6 and will be`1349328737`, and it would be considered an invalid token, because the Token Validity Window will be expired.

So how do i expliot it ?

I changed the `user_id` from the *Account 2**Account 1**Account 2**Account 1*`1349328731` it didn't accept it, but when I bumped the *Account 2*`1349328733` which in the same Validity Window (still the 60 second didnt finshed), it went through smoothly. Can't pinpoint the exact reason, but hey, it worked!, and now i can takeover any account by just changing the `user_id.`

In the end, the company acknowledged the issue as a critical severity and got paid $$$.

Thanks for reading!

you can follow me on social media to see more Write-Ups
