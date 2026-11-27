# How I found an IDOR Worth $1500

- **Source URL:** https://adilnbabras.medium.com/how-i-found-an-idor-worth-1500-d5f78bc22a7e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221005165409/https://adilnbabras.medium.com/how-i-found-an-idor-worth-1500-d5f78bc22a7e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/385 (id 385)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found an IDOR Worth $1500

Hello, today I am talking about the bug I recently found in one of biggest companies in the world. The bug was one of the my favourite bugs **Insecure Direct Object Reference (IDOR)**. If you are from cyber security then you know that what is this bug and why hackers and bug hunters love this bug. If you are not then let me tell you breif description about this bug.

# Insecure Direct Object Reference (IDOR):

IDOR is a branch of Broken Access Control. In which a user can do something or can perform an action which he is not intended or authorized to do. For example, In a note taking application, you have a private note when ever you access that note in url bar you see a parameter i.e. [https://www.example.com/notes/private?noteId=1002.](https://www.example.com/notes/private?noteId=1002.) So here, your note is referenced with id 1002 on backend. Now if application is vulnerable to IDOR and you change 1002 to 1001 in url then you can see some other user’s private note which is not good. Ofcourse this is not as simple as just changing 1002 to 1001 now-a-days. There is much more to explain but I am not going deep now.

# Story Time 😉:

Well the bug I found is not disclosed yet so I can’t disclosed the company name due to policies. Lets assume that example.com. As usual I choose a target from hackerone public programs and start hunting. Scope was very very limited so I have no choice to do recon. I have to find bug on main app. So first I create an account and start using application and try to understand the flow and logics of application. For now I am not hunting for any bug just using application as a normal user.

Then after some time I identify session cookies, anti-csrf tokens and headers. From this point I start hunting for CSRF (Client Side Request Forgery). Since almost all functionality on application are sensitive so I have to check each of them. I fired up burp and start capturing all the request one by one and start looking for csrf, I checked almost all major functionalites but after that I realized that may be I have no luck with CSRF.

So I move towards IDOR and start hunting for IDORs. First of all I have to identify what are the unique identifiers for each profile how we get that and where they disclosed. So I came across that each profile has a unique identifier a long random string (**afdt3628veyv37ECE3bfcb6vdEvcdstgh36Rvsdvye**) which is available in source code. For example if we visit someone’s profile and check page source code we get this unique identifer for that profile surely we can also get the same using burp but viewing source code is the easy way.

Also each Post, Image, Comment, etc everything have its own unique identifier. So, I make two account one is attacker and the other is victim’s account and note that unique identifiers. Using burp again I start capturing request and checking each functionality and days move on. Bye The Way scope was very limited but funtionality was very extensive.

Then I came accross a functionality where we can add images in our profile. After uploading image when I saw image in browser, in url there are two parameters one of them contain profile unique identifier and other param contains that image unique identifier. If I change that identifiers to my other account’s identifiers then I can see my other account image…but..but..but..thats not a bug because that image is available publically for all users. If I navigate to someone’s profile then I can see his images because they are always public. So whats the bug??

But when I deleted that image and capture the request in burp I see there is a DELETE request to an endpoint and the request has same identifiers that I enumerate previously. As I try all the requests I have to try this one also, I change the respected indentifers with my other account’s indentifiers and send the request, It respond with 204 status code. When I see my victim account in browser the respected image got deleted.

And at that time I was shocked because I did’nt expect bug there and it was an extremely secure application. I was in state of happiness and shocked. I don’t get that, is there is any bug or not. For surity I deleted some real user’s images in production (Ofcourse thats not allowed and if company know that then I am not eligible for bounty) but who tell them 😏.

# Now Proof-Of-Concept:

\- Upload an image in your profile.

\- Delete that image and capture request using burp.

\- Now navigate to any profile copy image url paste it in notepad and copy respected identifiers.

\- Change that identifiers in burp and send request.

\- Victim’s image got deleted.

Using this vulnerability I can delete billions of user’s images. But as I am a white hat hacker I report it. After some days I got this.

Somethings I learn from this bug are

\- Never Give Up , Never Ever

\- Bugs Are Everywhere — Nothing is secure

\- Be Persistant

\- Understand Logic

\- Dont Rely on Tools — its all manual

So thats it for know. I hope you enjoy and learn from it, if you have any question feel free to comment or contact me.

Email: adilnbabras@gmail.com

Thanks..😊
