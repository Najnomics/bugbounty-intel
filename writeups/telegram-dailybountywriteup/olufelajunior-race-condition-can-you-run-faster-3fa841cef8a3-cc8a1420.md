# Race Condition — can you run faster?

- **Source URL:** https://medium.com/@olufelajunior/race-condition-can-you-run-faster-3fa841cef8a3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821171701/https://medium.com/@olufelajunior/race-condition-can-you-run-faster-3fa841cef8a3
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10130 (id 10130)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Race Condition — can you run faster?

*There will be typos, I am not perfect. :)*

I am humble enough to accept that there are simply things that I do not know, and humble enough to accept that there is more to learn and push myself to learn more each day, I have not been writing lately, I have been doing more of my learning privately, as a way to show that I still can write I decided to write this post, if you found it useful, give it a thumbs up, if you have any addition, feel free to reach out to me.

I was at a BugBounty meetup with some friends of mine, and it sort of changed my perspective about a lot of things. I have been working as a Pentester full-time, and while the skills are the same, the approach is quite different. There is still so much for me to do, to learn, and I am taking a step towards that.

I was having a conversation with a good friend of mine, [Ewaoluwa](https://www.linkedin.com/in/ewaoluwa-adeniji/) who first mentioned race condition vulnerabilities to me. He asked me if I knew about it, and I said no. Next, he told me to check out Portswigger Web Academy to learn more about it, and that is what I did.

**What are race condition vulnerabilities?**

Race condition vulnerabilities happen when multiple requests run simultaneously and the application lacks proper safeguards to handle these simultaneous actions. Without adequate safeguards in place, these simultaneous operations can cause the application to behave incorrectly or unpredictably due to collisions. Race conditions are specific to the application’s design and logic, and uncovering them can lead to serious security issues such as bypassing usage limits, duplicating transactions, or escalating privileges.

**How can I learn more about race condition vulnerabilities?**

I am not going to bore you out, but check out these links below to learn more about it, I would recommend going to Portswigger web academy the link will be below, to learn more about it and aim to solve all the labs, if you get stuck don’t be afraid to check the hints, you are learning.

- [https://portswigger.net/web-security/race-conditions](https://portswigger.net/web-security/race-conditions)
- [https://www.geeksforgeeks.org/operating-systems/race-condition-vulnerability/](https://www.geeksforgeeks.org/operating-systems/race-condition-vulnerability/)

Drum rolls, here is the fun part, I did not set out to write this post to bore you with with too much technical jargon, to solidify my learning and learn from other hacker’s perspective, I read over 60 reports from Hackerone about race condition vulnerabilities to give you these different scenarios while testing for race condition vulnerabilities.

This is not an exhaustive list, but the purpose of this list is to help you see the different scenarios in which these vulnerabilities could occur and help you be creative when you start hunting for them in the wild.

Here you go,

1. **Multiple Invitations via Link**
User can add themselves multiple times via invitation link. For this to work, an admin account that sends an invitation link should exist. Try joining using the invitation link, intercept the request, send to repeater, add to group tabs, and send in parallel requests. The number of times to send depends on the scenario. ([https://hackerone.com/reports/604534](https://hackerone.com/reports/604534))
2. **Vote Manipulation**
Upvoting or downvoting posts: intercept the request depending on the scenario and send multiple times.
3. **Two-Factor Authentication Reset Abuse**
Resetting two-factor authentication (2FA) of a web application: after sending the 2FA reset request, intercept it, send in parallel, cancel one after receiving the email notification, and check if other reset links remain active depending on the scenario. ([https://hackerone.com/reports/2598548](https://hackerone.com/reports/2598548))
4. **Bonus Activation Exploit**
Try race condition in activating email for a bonus or something; this could lead to having more than originally intended. ([https://hackerone.com/reports/331940](https://hackerone.com/reports/331940))
5. **Following Users Multiple Times**
While trying to follow a user, intercept the request and send multiple times. ([https://hackerone.com/reports/927384](https://hackerone.com/reports/927384))
6. **Verification Limit Bypass**
Race condition to bypass verification checks under certain conditions, e.g., maximum allowed verifications, trying to do more than required. ([https://hackerone.com/reports/2110030](https://hackerone.com/reports/2110030))
7. **Credit or Money Transfer Duplication**
While transferring credits or money to person B, send the request to Turbo Intruder, using the racer.py script. The idea is to let the other user potentially have more than what you are transferring. ([https://hackerone.com/reports/974892](https://hackerone.com/reports/974892))
8. **Token Limit Bypass**
Sending more tokens than allowed in an account by sending concurrent requests (reference: [https://blog.credshields.com/race-condition-in-tendermints-starport-7cebe176d935](https://blog.credshields.com/race-condition-in-tendermints-starport-7cebe176d935)).
9. **Premium Offer Inflation**
Get more premium offers than originally stated. If you find this functionality, send it to Turbo Intruder and use the race script to see what happens. Aim to get more than allocated (e.g., 5 instead of 3). ([https://hackerone.com/reports/1037430](https://hackerone.com/reports/1037430))
10. **Test Credentials Abuse**
In programs where test credentials are limited (e.g., 2 per user), try sending requests to Intruder to gain more credentials. ([https://hackerone.com/reports/488985](https://hackerone.com/reports/488985))
11. **OAuth2 Token Overflow**
For OAuth2 implementations, check if you can get more tokens or refresh tokens than allocated.
12. **Folder Creation Limit Bypass**
For folder creation limits (e.g., 10 folders per user), exploit race condition by sending multiple requests when near the limit (e.g., at 9). Use Burp Suite Intruder or custom scripts. ([https://hackerone.com/reports/3104355](https://hackerone.com/reports/3104355))
13. **Likes and Reviews Inflation**
Race condition vulnerability allows inflation of upvotes on user comments (e.g., restaurant reviews). ([https://hackerone.com/reports/1409913](https://hackerone.com/reports/1409913))
14. **Email Addition Limit Bypass**
If there is a limit on the number of emails you can add, intercept the add-email request, send it to Intruder with an email list payload, and fire requests to add more than allowed.
15. **Unliking Posts Multiple Times**
On liking posts, also test unliking posts by intercepting and sending multiple unlike requests to see if you can unlike more than once.
16. **Coupon Code Reuse**
Redeeming coupon codes multiple times: intercept promo code redemption and resend requests to use the same promo code more than once.
17. **Vote Count Manipulation**
Race conditions in upvoting and downvoting: you can upvote or downvote more than once.
18. **Cloud Service Key Limit Bypass**
For cloud services with limits on keys, try creating additional keys by submitting multiple requests.
19. **Coin Purchase Inflation**
Buying more coins than intended: intercept purchase requests and send parallel requests in Burp Suite. ([https://hackerone.com/reports/801743](https://hackerone.com/reports/801743))
20. **Store Location Limit Bypass**
Race condition allowing bypass of store location limits by submitting multiple requests simultaneously.
21. **Member Limit Bypass in Invitation System**
Race condition in invitation systems to exceed the maximum allowed members by plan.
22. **Invite Your Friend Abuse**
“Invite your friend” feature: sending multiple requests to the same endpoint can exploit race conditions. ([https://hackerone.com/reports/1460373](https://hackerone.com/reports/1460373))
23. **Survey Credit Inflation**
Survey forms: race conditions allowing users to get credits multiple times by intercepting and sending parallel requests. ([https://hackerone.com/reports/165570](https://hackerone.com/reports/165570))
24. **API Seat Limit Bypass**
API endpoints with maximum seat limit: race conditions can allow bypassing this limit. ([https://hackerone.com/reports/1418419](https://hackerone.com/reports/1418419))
25. **Follower Count Inflation**
Potentially increase the number of followers a user has by sending multiple follow requests. ([https://hackerone.com/reports/927384](https://hackerone.com/reports/927384))
26. **File Import Collision Access**
Import file collisions: gaining access to others’ imports due to files named the same (e.g., file1 and file1). ([https://hackerone.com/reports/214028](https://hackerone.com/reports/214028))
27. **Multiple Invitations to the Same Team**
Race condition allows inviting a user multiple times to a single team.
28. **Rate Limiting Test via Race Condition**
Use race conditions to test rate limiting by sending many requests simultaneously to see how the app handles it. ([https://hackerone.com/reports/249319](https://hackerone.com/reports/249319))
29. **Trial Limit Bypass**
Get more trials than allocated by sending multiple parallel requests. ([https://hackerone.com/reports/1087188](https://hackerone.com/reports/1087188))
30. **Captcha Reuse Vulnerability**
Misconfiguration in captcha mechanism allowing reuse of the same captcha, bypassing uniqueness. ([https://hackerone.com/reports/67562](https://hackerone.com/reports/67562))
31. **White-label Subdomain Limit Bypass**
Adding more than the limit of 5 white-label subdomains; 5 is a soft limit.
32. **Multiple Feedback Submission**
Multiple parallel requests allow sending feedback to a user more than once. ([https://hackerone.com/reports/1132171](https://hackerone.com/reports/1132171))
33. **Multiple Invitation Acceptance**
Accepting an invitation more than once via repeated requests. ([https://hackerone.com/reports/119354](https://hackerone.com/reports/119354))
34. **Email Bombing via Race Condition**
Race condition that may cause bombing a user with a large volume of emails. ([https://hackerone.com/reports/1293377](https://hackerone.com/reports/1293377))
35. **Multiple OAuth Application Reviews**
Race condition allows reviewing an OAuth application multiple times. ([https://hackerone.com/reports/106360](https://hackerone.com/reports/106360))
36. **Unlimited Folder or Email Creation**
Creating new emails or folders multiple times with no limit on the number of folders created.

Here is a compilation of race condition bug reports below for your reference, credit goes to the owner of the repository.

I hope this helps, thank you for reading and happy hunting.
