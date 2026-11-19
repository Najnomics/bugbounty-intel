# How I found an IDOR on Achmea

- **Source URL:** https://medium.com/@nayeems3c/how-i-found-idor-on-achmea-cf9ce4b7d908?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251017075146/https://medium.com/@nayeems3c/how-i-found-idor-on-achmea-cf9ce4b7d908
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8295 (id 8295)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found an IDOR on Achmea

Assalamu Alaikum and greetings to everyone. This is my second write-up on how I exploited an IDOR to get cool swag from Achmea.

I was hunting on a subsidiary of Achmea. Let’s call our target example.com. I found a subdomain of example.com which allows users to create an account but a user can not see other users profile.

I created an account and while logging into my profile, I noticed an interesting API call like the one below

```
GET /api/users/me HTTP/1.1
Host: site.example.com
```
I intercepted the request and checked the response and found my test account’s Id, email, full name, address, date of birth in JSON format. There was an Id number but I was not sure what kind of Id it was.

```
{
  "id": 24,
  "email": "testaccount@example.com",
  "full_name": "Test User",
  "address": "123 Test Street, Test City, Test Country",
  "date_of_birth": "1990-01-01"
}
```
To confirm whether 24 is my profile number, I forwarded this request to repeater and replaced \`me\` with my account id \`24\` and it still gave me the same response.

Now it’s time to test Insecure Direct Object Reference (IDOR) vulnerability on that parameter.

So, I replaced id no. 24 with 23 on the API request and it looked like below.

```
GET /api/users/23 HTTP/1.1
Host: site.example.com
```
In response it disclosed other user’s information. I tried all sequential numbers on intruder and it disclosed every user’s information.

I immediately reported it to Achmea and after a few months I was awarded cool Hacker T-shirt.

I hope you enjoyed this write-up. If you have any questions please let me know.
