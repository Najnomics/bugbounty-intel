# The Premium Paradox

- **Source URL:** https://medium.com/@vasanthgn/the-premium-paradox-a-youtube-music-bug-that-worked-only-in-india-unreproducible-in-other-53f0510bec20
- **Fetched from:** https://medium.com/feed/@vasanthgn
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14985 (id 14985)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### **The Premium Paradox: A YouTube Music Bug That Worked ONLY in India — Unreproducible in Other Countries!** 🌍💀🔥

### **🎬 TITLE CARD**

Hello Everyone 👋

Hope you’re all safe and doing well.

I’m **Vasanth** from **Madurai**, **Tamil Nadu** — a **part-time bug bounty hunter** who enjoys poking at web applications (responsibly, of course 😄). I’ve been acknowledged by **Google, Apple, Microsoft, GitHub, Pornhub**, and **10+ other organizations** for responsibly reported security issues. 🛡️

In this write-up, I’ll walk you through how I discovered an interesting bug in **YouTube Music** 🎵🐛

### **🌙 OPENING SCENE — The Midnight Call**

It was Feb 7, 2026 evening. M**y friend Usman and I** were speaking on a call 📞, and during that time only I found that members-only video views were leaked in the page source — you can read about it [here](https://medium.com/techiepedia/something-was-hidden-in-youtube-until-i-checked-the-page-source-9e8bf9b51401). So regarding that we were discussing on the call, and **later we connected on Google Meet** at 9 PM and I was showing that bug 🐛, and we had a normal conversation. The call ended **around 12 AM** and I was sleepy 😴, so I decided to hear some music to sleep, so I opened YT Music 🎧

Nothing fancy, right? I just opened YT music and i was searching for a song to play 🎵. At that time, **we can able to download songs in YT Music** — hope you all know that 😅

So I just clicked that download button 🔽. Hmm — **only if our account is premium we can download** songs in YT Music, which is expected. We can see the below message 👇

Cool… next, there was a **famous Prashanth song** that recently became popular again through Instagram wedding reels 🎶. I’m sure many of you have come across it 😄

Since **the issue has not yet been fully addressed**, I’m intentionally not mentioning the exact song name as part of responsible disclosure 🙏

So I just tried to download this song, same like before. When I clicked — guess what? 🤔 Hope you all will be **expecting that premium upgrade message, right**? But that time some magic happened ✨ — and I was sleepy during that time 😴

As this downloading option comes in the left corner, **I didn’t notice it at first**. After downloading, there was another pop-up message — and that **time only i noticed it was downloaded**!! 😳

### **✨ THE TWIST NOBODY SAW**

Wait, what??? 😮 Suddenly I refreshed the page and that message was gone, and I was surprised how the song was downloaded… I was not even able to remember how the song was downloaded without premium 🤯. I had no idea. I was trying to reproduce it by **clicking another song to download, and that time that premium upgrade message came up** — so I was confused 😵. For 30 minutes I kept on searching, but I was not able to find out how the song was downloaded. Suddenly, after some time, I remembered 💡 — “**right, that particular song was the one that got downloaded**!” So I deleted it from downloads and again I tried to download the same song, and it downloaded successfully without Premium ✅

And I verified it using **offline play** — it worked successfully, where these features are only available to premium users in YT Music 🎧. B**ut I was able to access it without paying a single rupee** 💸. After that, I tried to download the **other songs** from the same movie, and they were downloading successfully without any restrictions and without asking to upgrade to premium 😲. With that shock, **I slept at 4:30 AM** 😴, and in the morning I woke up and I was about to report it to Google VRP 📩

### **🧪 BUILDING THE CASE**

Simply we cannot report this to Google VRP — we need a proper attack scenario 📝. But at that time I had no impact scenario, no idea how this bug could be used 🤔. So I was checking the other YT options, and that **time I noticed that we can create a playlist** 📂

I created a new playlist. Next, to show impact to the Google VRP, what I did is — I said right, I was able to download some songs from **different movies** and different songs, right? **I added those songs** to the playlist and made the playlist “**PUBLIC**”.

After spending a full day 🕐, I was able to find more than 30 songs that could be downloaded without premium, so I added those 30 songs to the playlist 📂.

So here the **bug scenario is** — if I **send this link** to users whose account does not have premium, they can download all the playlist songs 🎵 and enjoy offline features without premium 😎. Cool..

### IMPACT 💥

- **Free users** could download **Premium-only songs** and play them **offline** — ad-free, without a Premium subscription. 🎧
- A **single public playlist link** had the potential to expose the behavior to **unlimited users**. 🔗
- Potential **revenue impact** for **YouTube Music** and the respective **music rights holders**. 💸
- Demonstrated **inconsistent enforcement** of a **paid subscription boundary**. 🔓

Here’s the report I submitted to Google VRP 👇

### **📩 THE SUBMISSION**

Now, reporting to Google. **On Sunday afternoon**, I created a PoC and submitted it to Google VRP 📩 and was waiting for their response. The first response was:

The next response from Google came **within 1 hour** ⏱️, and it was:

Wow, that was a very quick response from the Google team 😃. I was very happy that it was accepted, because you know Google’s response timeline — IYKYK 😅. After that, **I was very confident that I was going to get a bounty from Google again**, because this bug leads to financial loss and premium feature restriction bypass 💸. So, I was waiting for the panel response. Hope you all guys know — **when they accept it first, it is not the final decision**; the panel decision is going to be final. So I was waiting for the panel decision and **asking for updates every 10 to 15 days**, but they were saying they had high volumes of reports because of **AI slop** 🤖

### **💔 INTERVAL BLOCK — Heartbreak**

But I had full hope that I was going to get a bounty for sure 🤞. You guys don’t know how much hope I had on this bug for a reward, but that hope was **destroyed in a second** 💔. On March 26, finally I got a response from the panel:

I was shocked that time — **the impact of the issue does not meet the bar for reward** 😶. That day my heart was broken 💔, because I had so much hope on this bug!! So next, I appealed with additional details that this qualified for a reward, and the Google team again sent it to the panel for review. That time also I had hope that I would get a bounty 🤞

OK, now again we need to wait for panel response. So here we go again — but this time the response came fast, and they said:

Again, heart broken 💔. **I appealed again with more details**, but no use — and they finally said:

### **⚰️ INTERMISSION — Case Closed**

They clearly said **only HOF is eligible for this bug** — but I had already got that back in 2021 😅. And I also decided not to appeal again because I was already tired 😩. But still, I was in depression after this result 😔. So I left it, the ticket was closed 🔒, and I moved on with my normal day-to-day work as months passed by.

### **🔥 SECOND HALF BEGINS — The Comeback**

I had almost become normal and **forgotten this bug**. On Jun 18, some response came from the report 📩. First, I thought it was a fixed response, because in **Google once the bug is fixed, we will get a response** — but it was some hotlist update, removed and added. That’s it 🤷

Hmm, next I didn’t care about this. And **after six days**, again I got a response from that bug — and this time it was a **game changer** 🔥. They had r**eopened my report by themselves**! I couldn’t believe it — Google is really doing this 😳

I was shocked for the full day 😳, and I asked for an update.

And they replied:

I was like

I was happy, because they were **checking it again by themselves** — so still I had no hope, because you already know what happened the first time 😅. But suddenly my mind went back to that February time, and I started to keep hope again. This time **I had a little hope, because they reopened the report by themselves, which means some internal action had happened** — not sure though 🤔. Hmm, and here we go again. I knew this time it would take more months for the panel to respond, because by now the AI slop had become more and more at Google 🤖

Well, I left them — let them take the time. In between, I was asking for updates, and the same response came from the team: still they had not decided 😐. Hmm.. and in between, I **kept on checking whether the bug was fixed or no**t, but I was still able to reproduce it 🔁

### The Region Twist 🌍

Now here comes the interesting part 👀.

I was working on my company laptop. Hope you all know — most of us work for clients, and we connect to the client machines through **WVD (Windows Virtual Desktop)**. That OS is based in the **USA**, so if you check the IP and other details, everything will be related to the USA and the client’s region 🌐. I had been using this setup for a long time.

As I said earlier, in between I used to check whether the bug was still reproducing or not. But this time it was different — I was **inside the WVD**, and I tried to reproduce it. I chose the same song and clicked download 🎵

It was a shocking result — **it asked me to upgrade to premium** 😲. That time I thought they had fixed the bug. Suddenly, outside the WVD, I tried to download the same song — that is, from an **Indian region and IP** 🇮🇳 — and there it was downloading! And again I was confused and shocked… what is happening here?? 🤯

Then on **my personal laptop**, I connected to a **USA VPN and tried to reproduce it — but the bug was not happening there** 🚫. It was blocked and asked me to upgrade to premium. But when I disconnected the **VPN and downloaded the song, it was downloading**! 🤯

Same same, but different…… Imagine how you feel seeing it right in front of your eyes — the **same song** behaving in **two different scenarios**. Crazy, right? 😵💫

Then I tried connecting to VPNs from different countries — **Canada 🇨🇦, Singapore 🇸🇬, Nigeria 🇳🇬, and a few more** — and tried to reproduce it, but it was not working 🚫. The same song was blocked and asked me to upgrade to premium. Ohoo! That time only I noticed — it is **only reproducible in INDIA** 🇮🇳. Before that, I was thinking anyone in the world could reproduce it 🌍

Well, now I had some new additional details to send to the panel, so I shared this information with them 📩

And they acknowledged it 👍

### **🎉 CLIMAX — “Nice Catch!”**

Hope crept back in 🤞. Months of waiting, appeals, and heartbreak — and then that one notification arrived.

**🎉 Nice catch!**

I froze for a second. In Google VRP, that line is not just a compliment — it’s **the signal that you’re getting rewarded** 💰. After everything, it finally happened

Finally, my hope was not broken 🙏. I got the bounty, and I was very happy 😃 — this is **one of the coolest and craziest bugs I have ever found** 🐛🔥

### **ONE MORE THING**

Here’s what makes this bigger than just “an India bug”:

If the Premium check depends on the apparent region rather than the account, then a non-Premium user sitting anywhere in the world could potentially connect through an India-region VPN and get the same free downloads 🌍

**So the affected population isn’t just users in India — it’s anyone willing  to flip a VPN switch**. That’s exactly what I shared with the panel, and

I believe it played a big role in the reward decision 💰

### **WHY DID THIS HAPPEN? 🤔**

I can’t confirm the root cause — only Google’s team knows that. But here’s my guess.

An important detail: **not all songs were affected**. Most songs correctly asked me to upgrade to Premium — only certain tracks were downloadable for free.

YouTube Music uses region-specific licensing. My theory is that for those specific songs, the licensing or metadata details were not updated properly in the India catalogue — so the download permission got tied to that stale regional flag instead of the account’s actual Premium status. The Premium check simply never ran 🎯

Outside India, no such flag — the normal check kicked in, download blocked.

Same account, same song, two different answers. That’s a logic flaw, not a feature 🔓

### 🦋 Now Let’s Connect the Dots

This bug was never on my list — I found it completely by accident.

Think about that day. My friend and I were speaking over the phone, and usually we just end the call there. But that time, we decided to connect through Google Meet. My laptop was inside the locker 🔐 — I opened the locker, took it out, and joined the Meet. After the call, I went to YT Music, picked the **second song**, and simply tried to download it… and it downloaded 🎵

Just imagine — YT Music has **100M+ songs** 🤯. But on that day, luck or something favoured me. The **second song** I touched was the vulnerable one, and the bug showed up right in front of my eyes. One click, and it downloaded.

It was a big and surprising day for me 😮. After that, when I researched more, I found that more songs were downloadable — but not all of them. And the VPN/region thing? That was unexpected too 🌍

### **So think about it 🤔**

If I hadn’t picked the call → no conversation at all.

If I was outside that evening → just a normal call, no Google Meet.

If the laptop stayed in the locker 🔐 → no YT Music that night.

If I slept right after the call → no download attempt.

If I stopped at the first Premium popup → no second song.

**Any one of these, and the bug stays hidden forever.**

But that night, every single one of them fell into place 🦋

### TIMELINE 🕒

- **Reported:** Feb 8, 2026 📩
- **Triaged & Accepted:** Feb 10, 2026 ⚡
- **Panel Decision — No Reward:** Mar 26, 2026 💔
- **Appeal #1 Submitted:** Mar 26, 2026 🔁
- **Appeal #1 Rejected:** Mar 31, 2026 😩
- **Credit Only (Hall of Fame):** Apr 8, 2026 🏅
- **Report Reopened by Google:** Jun 24, 2026 🤯
- **India-Only Region Finding Shared:** Sep 2, 2026 🇮🇳
- **Panel Response — “🎉 Nice catch!” → Bounty Awarded:** Oct 1, 2026 💰
- **Coordinated Disclosure Approved:** Nov 9, 2026 ✅

I hope you enjoyed this write-up! 😊 Thanks for reading, and stay tuned for the next one. 🚀🔍

“**Don’t wait for the dream Chase it**”

Connect me on LinkedIn: [https://www.linkedin.com/in/vasanth-gn](https://www.linkedin.com/in/vasanth-gn-3163a155/)
