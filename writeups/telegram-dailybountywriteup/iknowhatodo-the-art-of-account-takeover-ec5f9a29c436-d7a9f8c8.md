# The art of account takeover

- **Source URL:** https://medium.com/@iknowhatodo/the-art-of-account-takeover-ec5f9a29c436?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240223124509/https://medium.com/@iknowhatodo/the-art-of-account-takeover-ec5f9a29c436
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5065 (id 5065)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The art of account takeover

**بسم الله الرحمن الرحيم**

Hello reader,

I hope you are doing well. Today I want to talk about one of my findings.

**About the target application**


- The bounty program belongs to one of the largest company in the world, and it’s provides many services related to storing files in different formats, also creating or editing PDF, …etc.
- Each service provided by the company is considered a product and has a separate domain that distinguishes it from other services.
- Since there are so many products that each have their domain, it means that there are different authentication mechanisms.

Let’s call the main app and available products as follows:

0. Main app: example.com ==> API plans, Help center, …etc

1. Product 1: example1.com ==> Upload, store and share files

2. Product 2: example2.com ==> Create and edit the PDF files

3. Product 3: example3.com ==> — — — — — — — — — — — — — — 

4. Product 4: example4.com ==> — — — — — — — — — — — — — —

**What about authentication mechanisms?**


I will explain the authentication process in the website that caused this critical vulnerability

**The authentication mechanism in Product 1 \[example1.com\]**:

There are options for login or registration such as using email and password, and also through social logins such as Facebook and Google.

Nothing is remarkable about the authentication process except for two steps that the client performs after the success of the authentication process, where the authentication process is as follows:

1. The user enters the email and password, and if these credentials are correct, the JWT is returned in the response \[IdToken\].
— During the investigation when I decoded the token, I noticed that the program’s main domain name exists as “iss”, along with some other values, including email.

1. The application sends an additional request to the server with the IdToken obtained from the previous request, and two important values are returned in the response, namely: user\_id and token.
— What I realized later was that example1.com uses these values as headers to prove the authenticated user instead of the idToken.

1. The client sends another request to the server to retrieve the IdToken and accessToken for example2.com that refers to product 2, and the client can use these tokens if the user wants to use the features that allow modifying the PDF files, which is the competence of the example2.com without the need to move to the website, login, and other steps.

What about the features offered by example1.com?


There are many features offered by example1.com, including, which I will explain in this write-up: Create and manage Organization.

**About the Organization:**

There are multiple functions in the organization such as: inviting someone to join, resetting the password of a user who already exists in the org, locking his account, or giving him admin privilege.

*Reviews:*

- When I send an invitation to someone, that user’s account automatically takes a UUID associated with the organization.

- In the user interface, the Reset password function cannot be used for a user who has not joined the organization and whose status is still pending
- But when I use the endpoint responsible for this action with the account’s UUID, a temporary password is sent to the email associated with the user account that has still not accepted the invitation.
- When I used the Reset password function several times, I noticed that JWT was in the response header each time as a cookie value!

I said: Why don’t I decode this token?

When I decoded this token, I found that it belonged to the user whose password I had reset.

What!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

I said earlier that this JWT is comprehensive and specific to the company’s main domain \[example.com\]. {ATO}

**Escalate the scenario:**

1. I can use the JWT to retrieve a user\_id and token for Product 1 \[example1.com\]. Now, I can access the same account but on a different website \[Product 1\]! {ATO}
2. I can use the same JWT to connect with the endpoint responsible for retrieving an accessToken for Product 2 \[example2.com\] as I explained earlier in the authentication process. {ATO}

Hint


Understand the authentication mechanism well, and always look at HTTP response headers when you make some changes to the account because one of the cons of Restful API is overfetching!

**I hope you enjoyed reading, Thanks.**

Follow me on Twitter: [@iknowhatodo0x01](https://twitter.com/iknowhatodo0x01)
