# Mass assignment simplified

- **Source URL:** https://tonettao.medium.com/mass-assignment-simplified-c4bf5b9ca1b1
- **Fetched from:** https://tonettao.medium.com/feed
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14995 (id 14995)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I will start this article by telling you about one of my first bounties. I was testing a change-password and username workflow on a B2B platform, and analyzing the response in the Caido proxy, My request sent a POST with like 4 params, and the response returned the original 4 plus 5 more params.

I realized: if I try to use these params from the response in the sent POST request and see what happens… after minutes of just trying values and params, I noticed that only 2 of the 5 params were enabled to be sent and was accept. One of them was like use\_limit: 0. This platform has a premium plan, and on the free plan you have a limit of 5 uses. My use limit was 0 because I didn’t try to use the credits at that moment, when I used one that value changed to use\_limit: 1, and I understood what that param was. I spent all my 5 credits, and when I reached the limit I just tried to set it to 0 again and it worked. The backend accepted the value and reset my use limit.

Hello, my name is João Tonetto, I am an eternal student, a Bug hunter and a lot of other random things and in this article I will try to help you understand and identify a Mass Assignment API vulnerability.

### Why does this vulnerability occur?

*It is necessary for you to understand a little about JSON objects, but I will exemplify it very quickly. Imagine you have a user object, and this user object has many attributes like name, age, address, phone, email, role; all of this is part of the user object, and in JSON it is like this structure: {"user":{"name":"joao","age":24,"address":"fimdomundo","phone":"999999","email":"sabido@email.com","is\_admin": false}}*

1- Auto binding

When you send a request with a JSON object but with just a few attributes like {"user":{"name":"joao","email":"sabido@email.com"}}, you don’t necessarily know which other attributes exist in the backend User object. However, the backend knows the complete structure of that object. If the application uses automatic binding without properly restricting which attributes can be assigned by the user, the framework may allow incoming request parameters to be mapped directly to internal object properties and may return other parameters of the user object like: {"user":{"name":"joao","age":24,"address":"fimdomundo","phone":"999999","email":"sabido@email.com","is\_admin": false}}.

This is the first problem.

2 — Validation issue (or lack of validation)

The correct treatment is to validate and control so the user can’t edit state-changing values/params like a role param, because imagine if I can change "is\_admin": false to "is\_admin": true and this change persists in the backend; now I have the admin role and I can access a few endpoints with sensitive functions and data just by changing the role, This is a big problem.

*In my example at the beginning of the article, it was not a Privilege Escalation but a business logic flaw that enabled me to get infinite credits on the platform. It is very important to understand the concept of this vulnerability and not fix your mind on only one possible action, like a Privilege Escalation, for example. You need to analyze and understand what’s happening and what the platform does and has, make a connection with the params received in the response/request, and try and try those params and think about what you can do with those values and what you can change. This is how you find a bug.*

### The real world

I explained to you basically what the vulnerability is, but in real life you will face different situations. Imagine you are testing a username change function and you send a JSON like this {"user":{"name":"joao","email":"sabido@email.com"}} and in the response you receive the same thing: {"user":{"name":"joao","email":"sabido@email.com"}} or something like {"status":"Username\_Change\_OK!"}, just a simple return without any interesting parameter.

In this case a lot of people will go and think: "Okay, nothing here. Let's move on to the next function." but just because you didn't receive anything interesting doesn't mean there's nothing there. There might be a gold parameter hidden somewhere, with no state-change validation. You just need to discover it.

In this case, you need to use some techniques, such as fuzzing parameters with tools like Param Miner or similar tools, combined with a good wordlist. With this type of technique, you can discover hidden parameters. Once you find them, you need to test whether they accept modifications and whether those changes persist.

**Remember the GOLD RULE: Try to understand what the parameter does and what its context is within the application.**

Another **VERY IMPORTANT** tip: When you find an interesting parameter and discover that it’s safe on a specific endpoint (meaning you can’t modify its value), don’t just leave it alone. Take notes and keep it! Try testing other functions and sending that parameter to different endpoints. There’s a chance that other endpoints don’t have proper state-change validation. This kind of thing happens more often than you might think.

### How to Enumerate

Follow the spirit of bug hunting: just poke around and rummage through everything. Be curious, analyze your requests, and try to understand what’s happening behind each function. But remember to have a logical testing methodology.

This type of vulnerability usually appears in API requests, and to reach those requests, you need to test different application functions. Look for functions related to login, username changes, or any other type of modification you can perform on your account within the application. In general, try all the functions where you can edit or create things. These are the places where you’re more likely to find something like this vulnerability.

**Enumerate Swagger docs:** check for exposed API documentation, such as Swagger or OpenAPI. These documents can reveal hidden endpoints, HTTP methods, request parameters, authentication requirements, and internal API structures. Look for common paths like /swagger, /swagger-ui, /api-docs, and /openapi.json; this information can help you understand the application’s API structure and identify interesting endpoints and parameters to investigate during your testing.

### To finish

This was a quick explanation of this API vulnerability, I recommend doing some labs and practicing to understand exactly how it works and get familiar with the concepts. I’ll leave some links here. They’re all really good resources.

I hope you enjoyed this content! :)

𝗯𝗹𝗼𝘄 𝗲𝘃𝗲𝗿𝘆𝘁𝗵𝗶𝗻𝗴 𝘂𝗽 …

*tonetto*

#### Material and Labs:

[https://portswigger.net/web-security/api-testing#mass-assignment-vulnerabilities](https://portswigger.net/web-security/api-testing#mass-assignment-vulnerabilities)

[https://cheatsheetseries.owasp.org/cheatsheets/Mass\_Assignment\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)

[https://portswigger.net/web-security/api-testing/lab-exploiting-mass-assignment-vulnerability](https://portswigger.net/web-security/api-testing/lab-exploiting-mass-assignment-vulnerability)

[https://pentesterlab.com/glossary/mass-assignment](https://pentesterlab.com/glossary/mass-assignment)

**POST Request Fuzzing**:

[https://ffuf.hashnode.dev/parameter-fuzzing](https://ffuf.hashnode.dev/parameter-fuzzing)
