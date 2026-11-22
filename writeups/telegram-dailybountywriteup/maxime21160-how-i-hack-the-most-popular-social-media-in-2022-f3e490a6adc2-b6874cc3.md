# How i hack the most popular social media in 2022(broken access control)

- **Source URL:** https://medium.com/@maxime21160/how-i-hack-the-most-popular-social-media-in-2022-f3e490a6adc2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311162434/https://medium.com/@maxime21160/how-i-hack-the-most-popular-social-media-in-2022-f3e490a6adc2
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1750 (id 1750)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How i hack the most popular social media in 2022(broken access control)

by Maxime Jourdan


Hi my name is maxime i’m 🇫🇷 and i am 18 years old. I write this article to explain you how i hack and won 1600$, in the most popular social media in 2022.

# How all started ?

All started when i discover the world of cybersecurity, i watch a lot of video about the subject on youtube, and one was about bug Bounty.

# So what exactly is a bug Bounty ?

A Bounty bug is a financial reward offered to ethical hackers for discovering and reporting a vulnerability or bug to an application developer.

So i wonder if i can make the same things with my skill, so i started to look every where and start hacking things and this is how i do it :

# 1) Find your target :

so i naturally turn my research in social media, as these app contain a lot of user data. So i search in the most use social media of 2022. Unfortunately i can’t say the name of the app as i’m part of a private programs and i can’t tell much information that why i dont tell details of my findings

# 2) Start Hacking :

this is the most long but funny part. I installed the app on my phone and i create a Man in the middle attack (MITM).

See the video i created on my youtube channel about the sujet :

So why use a Man in the middle attack ?


well because this is very easy to know how the app works what services they use how, when, with what request.

this is how a man in the middle attacks works :


So in this case the user is my phone connected to internet (via my computer) with the app running, and the man in the middle device is my mac which use mitproxy a tool in macOS that show all the request that my phone made.

**by performing the attack i launch the app on my phone, and i look of all the request the app perform. I touch all the button and use all the features of the app, and after a lot of research i fond a interesting endpoint.**

This endpoint was use by the app when i access my video, after look into this endpoint i discovers that is was not protected by anything, and find out that it was a database that contain a lot of info in clear :

i figure out that this list that contain the id of user and a link to privates videos (about 50000 american user video )

# 3) Alerting the developpeur of the app

just after my discover, i contacted the owner of the platform via mail and, they sent me a private invitation to her HakerOne Programs i was very happy at this point.

# what is HackerOne ?

HackerOne is a company specialised in cybersecurity, especially attack resistance management, which combines the security expertise of ethical hackers with discovery

so i created an account and i reported it to the \<confidential> company through their bug bounty program. The process of reporting the vulnerability was straightforward and well-documented. I provided a detailed description of the vulnerability, along with a proof-of-concept exploit write up that demonstrated how the vulnerability could be exploited. After talk to the developpeur, and 2 week later a receive a notification that tell me that i win 1600$ for Broken Access control. I was not expecting this amount of money, i was surprising. I also win a badges in Hackerone see below :

So this is how i win 1600$ by hacking the most used social media in 2022

thanks for reading this article if you have questions you can contact me via Email : maxime21160@icloud.com
