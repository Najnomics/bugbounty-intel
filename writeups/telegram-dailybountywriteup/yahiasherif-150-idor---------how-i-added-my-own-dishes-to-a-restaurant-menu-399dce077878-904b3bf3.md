# $150 IDOR️‍♂️ — How I Added My Own Dishes to a Restaurant Menu

- **Source URL:** https://medium.com/@yahiasherif/150-idor-%EF%B8%8F-%EF%B8%8F-how-i-added-my-own-dishes-to-a-restaurant-menu-399dce077878?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250424213945/https://medium.com/@yahiasherif/150-idor-%EF%B8%8F-%EF%B8%8F-how-i-added-my-own-dishes-to-a-restaurant-menu-399dce077878
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9273 (id 9273)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $$$ 🕵️♂️IDOR How I Added My Own Dishes to a Restaurant Menu🍽

Hi, I’m Yahia Sherif, a security researcher and bug bounty hunter. Today, I’d like to share my latest findings in a restaurant booking platform where I could take over any restaurant menu using **IDOR**!

# What is IDOR?

**IDOR** (Insecure Direct Object Reference) is a type of Access Control vulnerability that occurs when a user can manipulate an input (such as a URL, form field, or API parameter) to directly access or modify data they shouldn’t have permission to access.

# The Story

Our program here is a restaurant booking platform, which has 2 types of users:

- **Manager User**: If you own a restaurant and want to list it on the app, you’re a manager user.
- **Customer-User**: If you’re looking for a restaurant to book for your date or something 😉

I first created a customer user, but there weren’t many functionalities to look for. Everything was limited until I could book a restaurant. The program prevented testing on real restaurants, so I opened the manager domain and started filling in fake restaurant info because, well… I didn’t have one 😢.

I noticed a function in my manager account where I could upload my menu in 3 ways:

- **PDF file**
- **Menu link**
- **Image files**

So, I uploaded a PDF file and captured the request. It looked like this

```
POST /api/graphql HTTP/2
Host: target.com
Cookie: 🍪
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://target.com
Content-Type: application/json
X-App-Version: v24.104.1
X-App-Name: tfm-front
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6bnVsbCwidXNlcm…
Restaurant-Id: null
Content-Length: 341
Origin: https://target.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=4
Te: trailers
{"operationName":"generateMenuSignedUrl","variables":{"restaurantUuid":"a19d3f42-7c8e-4d1b-b92c-8fc1d5f81a6e"},"query":"mutation generateMenuSignedUrl($restaurantUuid: ID!) {\n generateMenuSignedUrl(restaurantUuid: $restaurantUuid) {\n pdfMenuUuid\n signedUrl {\n url\n key\n __typename\n }\n __typename\n }\n}
```
The `restaurantUuid` is a unique identifier that carries the restaurant ID.

I created another manager account and swapped its `restaurantUuid` with my target restaurant's UUID in the request. However, when I sent it, I received the following response:

`{"errors":[{"message":"Unauthorized","locations":[{"line":2,"column":3}],"path":["restaurant"],"extensions":{"code":"UNAUTHENTICATED"}}],"data":null}`
I tried the same with the **upload image method**, but it returned the same response.

I didn’t expect the **add link method** to work either, but I decided to give it a shot. I captured the **add link request**, swapped its `restaurantUuid`, and this time, it returned the following response:

`{"data":{"uploadMenuUrl":{"url":"https://website.com","__typename":"MenuUrl"}}}`
It worked! I opened my secondary restaurant account and noticed that the added link webpage was now displaying in the restaurant menu section.

But here’s the problem the `restaurantUuid` is a unique identifier that only the restaurant owner should have and it cannot be guessed or brute-forced. I considered reporting it as it, but I was sure that would get an informative or n/a after all that work.

So, I opened my **customer account** and interacted with the restaurant in every possible way — made a booking, canceled it, wrote a review, reported it, and added it to my favorites.

After that, I opened my **Burp Suite traffic** and searched for `restaurantUuid`, and guess what? It was reflected in the **add-to-favorites function**! The request looked like this:

`[{"operationName":"CreateBookmarkCollection","variables":{"isPublic":false,"name":"12","restaurantUuid":"a19d3f42-7c8e-4d1b-b92c-8fc1d5f81a6e"},"query":"mutation CreateBookmarkCollection($name: String!, $isPublic: Boolean!) {\n createBookmarkCollection(name: $name, isPublic: $isPublic) {\n id\n name\n isPublic\n createdTs\n updatedTs\n bookmarkCount\n defaultEmoji\n __typename\n } \n}" }]`
As soon as I tested the vulnerability, I reported it immediately. Bugcrowd responded quickly, triaged the issue, and awarded me the bounty

# Timeline

- **25 Mar 2025** → Report submitted.
- **28 Mar 2025** → Report triaged.
- **31 Mar 2025** → Submission confirmed, bounty rewarded.

# My links

linkedin: [https://www.linkedin.com/in/yahia-sherif-891ab8301/](https://www.linkedin.com/in/yahia-sherif-891ab8301/)

facebook: [https://www.facebook.com/profile.php?id=100068354653706](https://www.facebook.com/profile.php?id=100068354653706)
