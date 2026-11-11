# @kevin_mizu — full verbatim X archive (security-relevant posts)

_Generated 2026-11-11 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 29
- Conversations/threads: 28
- Oldest post captured: 2025-04-28
- Newest post captured: 2026-10-28


---

## 2026-10-28 · Reply · @Brumens2 @hash_kitten Ahaha exactly! :D


### Post — @kevin_mizu — 2026-10-28 17:12 UTC (2026-10-28 18:12 WAT)

- URL: https://x.com/kevin_mizu/status/2115492001982697842
- Metrics (at fetch): bookmark 0, impression 121, like 1, quote 0, reply 0, retweet 0

> @Brumens2 @hash_kitten Ahaha exactly! :D


---

## 2026-10-28 · Post · With @hash_kitten, we've been looking into Cloudflare's /cdn-cgi/image endpoint and managed to get a


Tags (automatic): XSS, CSP / CSPT


### Post — @kevin_mizu — 2026-10-28 14:21 UTC (2026-10-28 15:21 WAT)

- URL: https://x.com/kevin_mizu/status/2115448862869500312
- Metrics (at fetch): bookmark 72, impression 9047, like 203, quote 1, reply 8, retweet 46

> With @hash_kitten, we've been looking into Cloudflare's /cdn-cgi/image endpoint and managed to get an XSS :D
>
> To achieve this, we used what I believe to be a new CSP bypass involving the Cache-Control response header, combined with a sanitizer bypass!
>
> I hope you'll enjoy it! 👇 https://twitter.com/assetnote/status/2115447225534845431

**Links in post:** https://twitter.com/assetnote/status/2115447225534845431

**Quoted post (full text):**

    #### Quoted post — @884385805514526720 — 2026-10-28 14:14 UTC (2026-10-28 15:14 WAT)
    
    - URL: https://x.com/884385805514526720/status/2115447225534845431
    - Metrics (at fetch): bookmark 205, impression 28596, like 377, quote 7, reply 6, repost 78
    
    > Our security research team discovered a cross-site scripting vulnerability in Cloudflare's /cdn-cgi/image/ endpoint by chaining an SVG sanitizer bypass with a new Cache-Control header trick to bypass the CSP. The issue was reported to Cloudflare and has since been fixed. 
    >
    >  You can read more here: 
    >
    > https://www.slcyber.io/research/cache-me-if-you-can-xss-in-cloudflares-cdn-cgi-image
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HVuTHSAWUAA-QO2.jpg — no alt text provided by author
    
    **Links in post:** https://www.slcyber.io/research/cache-me-if-you-can-xss-in-cloudflares-cdn-cgi-image
    


---

## 2026-10-16 · Post · I've been beta testing it, and I have to say it's a fun little idle game :D https://t.co/M5JYiIXEca


### Post — @kevin_mizu — 2026-10-16 15:04 UTC (2026-10-16 16:04 WAT)

- URL: https://x.com/kevin_mizu/status/2111111102394511707
- Metrics (at fetch): bookmark 9, impression 2688, like 32, quote 0, reply 2, retweet 2

> I've been beta testing it, and I have to say it's a fun little idle game :D https://t.co/M5JYiIXEca

**Quoted post** 2111099846169936308: not readable via the API (deleted, private, or withheld).


---

## 2026-10-07 · Post · I'm happy that my first article as part of the @SLCyberSec research team is finally out! 😁


Tags (automatic): RCE, Race condition


### Post — @kevin_mizu — 2026-10-07 10:41 UTC (2026-10-07 11:41 WAT)

- URL: https://x.com/kevin_mizu/status/2107783292091007306
- Metrics (at fetch): bookmark 73, impression 9844, like 210, quote 1, reply 8, retweet 43

> I'm happy that my first article as part of the @SLCyberSec research team is finally out! 😁
>
> It covers an interesting ImageMagick race condition that I found back in June, which, combined with a polyglot payload, allowed me to achieve file read/RCE on Discourse. This should resonate with those who've seen the recent @HacktronAI research.
>
> I hope you'll enjoy it! 👇

**Links in post:** https://twitter.com/assetnote/status/2107782416479694949

**Quoted post (full text):**

    #### Quoted post — @884385805514526720 — 2026-10-07 10:37 UTC (2026-10-07 11:37 WAT)
    
    - URL: https://x.com/884385805514526720/status/2107782416479694949
    - Metrics (at fetch): bookmark 108, impression 23423, like 242, quote 3, reply 4, repost 61
    
    > Our research team discovered two vulnerabilities in Discourse: a pre-authentication cache poisoning to sitewide XSS (CVE-2026-55674), and an arbitrary file read (RCE) chaining a JPEG race condition with ImageMagick and Ghostscript (CVE-2026-55420). You can read more here: [pic.x.com/twDxtwCnoQ]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HUBYWTCXkAA9D6F.jpg — alt text: "https://www.slcyber.io/research/a-jpeg-a-race-and-a-ghost-breaking-discourses-image-pipeline"
    


---

## 2026-09-08 · Reply · @Dinosn Oh, I don't really know what to say! I found it in mid-July. Collisions are everywhere these


### Post — @kevin_mizu — 2026-09-08 07:14 UTC (2026-09-08 08:14 WAT)

- URL: https://x.com/kevin_mizu/status/2097222027543228750
- Metrics (at fetch): bookmark 0, impression 2167, like 8, quote 0, reply 1, retweet 0

> @Dinosn Oh, I don't really know what to say! I found it in mid-July. Collisions are everywhere these days :/


---

## 2026-09-07 · Post · A logical bug that I've reported to MariaDB has just been disclosed! 🎉


Tags (automatic): Platform: HackerOne


### Post — @kevin_mizu — 2026-09-07 20:14 UTC (2026-09-07 21:14 WAT)

- URL: https://x.com/kevin_mizu/status/2097055819447550388
- Metrics (at fetch): bookmark 330, impression 158458, like 827, quote 25, reply 8, retweet 157

> A logical bug that I've reported to MariaDB has just been disclosed! 🎉
>
> It's a nice logic issue that allows any user (no matter their rights) to update the password of any other user, including root :D
>
> You can find more details 👇
> https://hackerone.com/reports/3876430 [pic.x.com/Hxb99wFnUO]

**Media:**
- photo: https://pbs.twimg.com/media/HRo8_3YW4AA5lRu.jpg — no alt text provided by author

**Links in post:** https://hackerone.com/reports/3876430


---

## 2026-08-24 · Reply · @mpgn_x64 Encore merci pour l'invitation, c'était super de pouvoir passer sur le podcast 🫶


### Post — @kevin_mizu — 2026-08-24 10:13 UTC (2026-08-24 11:13 WAT)

- URL: https://x.com/kevin_mizu/status/2091831315104448781
- Metrics (at fetch): bookmark 0, impression 200, like 4, quote 0, reply 0, retweet 0

> @mpgn_x64 Encore merci pour l'invitation, c'était super de pouvoir passer sur le podcast 🫶


---

## 2026-08-17 · Post · Recently, I've been looking at DOMPurify again, trying to find ways to bypass 3.x.x after browsers s


### Post — @kevin_mizu — 2026-08-17 14:59 UTC (2026-08-17 15:59 WAT)

- URL: https://x.com/kevin_mizu/status/2089366491179122821
- Metrics (at fetch): bookmark 99, impression 11019, like 256, quote 0, reply 4, retweet 55

> Recently, I've been looking at DOMPurify again, trying to find ways to bypass 3.x.x after browsers started encoding attrs during serialization.
>
> I ended up with a nice ≤3.2.6 Safari default-configuration bypass using only SMIL tags/attrs :D
>
> Details 👇
> https://mizu.re/post/dompurify-bypass-smil-animatetransform-safari [pic.x.com/EdbsVyWwfb]

**Media:**
- photo: https://pbs.twimg.com/media/HP7qEo6XIAAlh2W.jpg — alt text: "https://yeswehack.github.io/Dom-Explorer/shared?id=9c1f671a-fc8f-4284-9217-eba4df143db3"

**Links in post:** https://mizu.re/post/dompurify-bypass-smil-animatetransform-safari


---

## 2026-07-21 · Post · It's not in the stable release yet, but I've already reported it to the Chromium team, and they clos


### Post — @kevin_mizu — 2026-07-21 13:06 UTC (2026-07-21 14:06 WAT)

- URL: https://x.com/kevin_mizu/status/2079553637773148314
- Metrics (at fetch): bookmark 0, impression 771, like 8, quote 0, reply 0, retweet 0

> It's not in the stable release yet, but I've already reported it to the Chromium team, and they closed it as "Won't Fix (Infeasible)".
>
> If this ships, it could enable a fun gadget, even with HTML strings sanitized by DOMPurify :D


---

## 2026-07-21 · Post · Chrome keeps adding fun features!


Tags (automatic): XSS


### Post — @kevin_mizu — 2026-07-21 13:06 UTC (2026-07-21 14:06 WAT)

- URL: https://x.com/kevin_mizu/status/2079553635470430622
- Metrics (at fetch): bookmark 33, impression 4859, like 88, quote 0, reply 3, retweet 7

> Chrome keeps adding fun features!
>
> After declarative partial updates, the CSS version is behind an experimental flag: https://t.co/TMonPuOO4m
>
> The new specifier attribute lets you poison import maps, even via DOMParser. Not XSS (text/css), but it can still block module loading :D https://t.co/al9OJxE0iV

**Media:**
- photo: https://pbs.twimg.com/media/HNwOEsfWAAEQrRW.jpg — no alt text provided by author


---

## 2026-07-17 · Post · 🔥🔥 https://t.co/KSy3Z43V2h


### Post — @kevin_mizu — 2026-07-17 23:05 UTC (2026-07-18 00:05 WAT)

- URL: https://x.com/kevin_mizu/status/2078254854087020589
- Metrics (at fetch): bookmark 9, impression 5974, like 37, quote 0, reply 0, retweet 1

> 🔥🔥 https://t.co/KSy3Z43V2h

**Quoted post** 2078253959018648050: not readable via the API (deleted, private, or withheld).


---

## 2026-07-09 · Post · It was a really fun event! Thanks to @Hacker0x01 and Salesforce for the invitation!


Tags (automatic): Platform: HackerOne


### Post — @kevin_mizu — 2026-07-09 15:05 UTC (2026-07-09 16:05 WAT)

- URL: https://x.com/kevin_mizu/status/2075234997246496822
- Metrics (at fetch): bookmark 10, impression 8483, like 102, quote 0, reply 7, repost 7

> It was a really fun event! Thanks to @Hacker0x01 and Salesforce for the invitation!
>
> I'm really happy that we won Best Hacker and Best Team with @Geluchat, @hash_kitten, and @infosec_au! 🎉 :D https://twitter.com/Hacker0x01/status/2075220240925958529

**Links in post:** https://twitter.com/Hacker0x01/status/2075220240925958529

**Quoted post (full text):**

    #### Quoted post — @Hacker0x01 — 2026-07-09 14:07 UTC (2026-07-09 15:07 WAT)
    
    - URL: https://x.com/Hacker0x01/status/2075220240925958529
    - Metrics (at fetch): bookmark 27, impression 34098, like 162, quote 7, reply 5, repost 11
    
    > Congratulations to the winners from our Live Hacking Event with @Salesforce in Tokyo! 🎉🇯🇵
    >
    > First place:
    > Metnew (@v_metnew)
    >
    > Second place:
    > Geluchat (@Geluchat)
    > Hashkitten (@hash_kitten)
    > kevin_mizu
    > Shubs (@infosec_au)
    >
    > Third place:
    > adibou
    > snorlhax
    >
    > Collaboration:
    > Aussie
    > Baguette 
    >
    > Best Hacker:
    > Aussie
    > Baguette
    >
    > An incredible week of collaboration, creativity, and impact from the global security researcher community.
    >
    > In the agentic AI era, live collaboration helps organizations identify and remediate vulnerabilities faster. 
    >
    > Thank you to everyone who participated and made the internet safer. 💻🔍
    
    **Media:**
    - video: https://pbs.twimg.com/media/HMypy03WsAA7HOc.jpg — no alt text provided by author
    


---

## 2026-07-07 · Post · This makes cloudflare /cdn-cgi/image a valid CSPT → innerHTML gadget btw :D


Tags (automatic): CSP / CSPT


### Post — @kevin_mizu — 2026-07-07 12:01 UTC (2026-07-07 13:01 WAT)

- URL: https://x.com/kevin_mizu/status/2074463929401516413
- Metrics (at fetch): bookmark 136, impression 15572, like 187, quote 0, reply 0, retweet 19

> This makes cloudflare /cdn-cgi/image a valid CSPT → innerHTML gadget btw :D
>
> https://t.co/dDfblnPHR5 https://t.co/dLwFFYavP9

**Quoted post** 2074446473220214979: not readable via the API (deleted, private, or withheld).


---

## 2026-07-03 · Post · @J0R1AN I mean, on attr update**!


### Post — @kevin_mizu — 2026-07-03 10:08 UTC (2026-07-03 11:08 WAT)

- URL: https://x.com/kevin_mizu/status/2072985718272475531
- Metrics (at fetch): bookmark 0, impression 71, like 0, quote 0, reply 0, retweet 0

> @J0R1AN I mean, on attr update**!


---

## 2026-05-19 · Post · It's a really nice challenge! If you have some time, give it a try 🚩 https://t.co/jLSeWBNOzx


### Post — @kevin_mizu — 2026-05-19 07:19 UTC (2026-05-19 08:19 WAT)

- URL: https://x.com/kevin_mizu/status/2056635918648254507
- Metrics (at fetch): bookmark 4, impression 3515, like 30, quote 0, reply 1, retweet 0

> It's a really nice challenge! If you have some time, give it a try 🚩 https://t.co/jLSeWBNOzx

**Quoted post** 2056635004688769237: not readable via the API (deleted, private, or withheld).


---

## 2026-04-12 · Thread · The FCSC2026 ended today, and my write-ups are now available here:


### Post — @kevin_mizu — 2026-04-12 15:10 UTC (2026-04-12 16:10 WAT)

- URL: https://x.com/kevin_mizu/status/2043345976140656799
- Metrics (at fetch): bookmark 38, impression 8422, like 76, quote 1, reply 3, retweet 19

> The #FCSC2026 ended today, and my write-ups are now available here:
>
> https://t.co/6e2WWjxKpD 🚩
>
> I'm really happy with the challenges I managed to create this year! It would be too long to list everything, so here's a little teaser 👇
>
> 1/2 https://t.co/NZc7H1VtRG https://t.co/FKow8aKOuN

**Media:**
- photo: https://pbs.twimg.com/media/HFtsI_1a4AACON1.jpg — no alt text provided by author

**Quoted post (full text):**

    #### Quoted post — @kevin_mizu — 2026-04-03 18:12 UTC (2026-04-03 19:12 WAT)
    
    - URL: https://x.com/kevin_mizu/status/2040130397179126227
    - Metrics (at fetch): bookmark 63, impression 25958, like 138, quote 1, reply 4, retweet 17
    
    > This year again, with @BitK_ and @_Worty, we've made the Web challenges 🚩
    >
    > The CTF is solo and lasts 10 days, if you have some time, please give it a look 😁
    >
    > Even if you're not doing Web challenges, there are challenges in various categories, you should find something you like! [pic.x.com/S2z1mDPUu6]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HE__yLmWUAA5QTG.png — no alt text provided by author
    


### Thread part 2 — @kevin_mizu — 2026-04-12 15:10 UTC (2026-04-12 16:10 WAT)

- URL: https://x.com/kevin_mizu/status/2043345979491926255
- Metrics (at fetch): bookmark 0, impression 929, like 3, quote 0, reply 1, retweet 2

> All the other challenge write-ups (not just web) are available in the #writeup channel of the CTF Discord server:
>
> https://discord.gg/rwZY6hh8z8
>
> Btw, all the challenges have also been (will be) added to http://hackropole.fr! 🚩
>
> 2/2

**Links in post:** https://discord.gg/rwZY6hh8z8, http://hackropole.fr


---

## 2026-04-09 · Reply · @sudhanshur705 Really great article and findings, congratz! :)


### Post — @kevin_mizu — 2026-04-09 13:44 UTC (2026-04-09 14:44 WAT)

- URL: https://x.com/kevin_mizu/status/2042237271668031610
- Metrics (at fetch): bookmark 0, impression 896, like 5, quote 0, reply 1, retweet 0

> @sudhanshur705 Really great article and findings, congratz! :)


---

## 2026-04-08 · Post · I'm happy to release the first version of my DOMLogger++ plugin for @CaidoIO! 🔎


Tags (automatic): AI-assisted hunting


### Post — @kevin_mizu — 2026-04-08 15:09 UTC (2026-04-08 16:09 WAT)

- URL: https://x.com/kevin_mizu/status/2041896181744161159
- Metrics (at fetch): bookmark 81, impression 12346, like 177, quote 3, reply 4, retweet 32

> I'm happy to release the first version of my DOMLogger++ plugin for @CaidoIO! 🔎
>
> It improves the browser extension in several ways:
> • Persistent, per-project storage
> • Temporary session recording
> • AI support
> • Stack trace reconstitution
> • ...
>
> 👉 https://t.co/tj72KXjAN9 https://t.co/tRdiFP6M0T

**Media:**
- photo: https://pbs.twimg.com/media/HFZE16XbQAAkn9V.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HFZE4nGXsAAskJN.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HFZE7CiXwAEQ10u.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HFZE_EjWQAAdLl-.jpg — no alt text provided by author


---

## 2026-04-04 · Post · Ouppps I forgot the CTF link!


### Post — @kevin_mizu — 2026-04-04 15:46 UTC (2026-04-04 16:46 WAT)

- URL: https://x.com/kevin_mizu/status/2040455966324392184
- Metrics (at fetch): bookmark 15, impression 3158, like 34, quote 0, reply 0, retweet 1

> Ouppps I forgot the CTF link!
>
> 👉 https://fcsc.fr/ https://twitter.com/kevin_mizu/status/2040130397179126227

**Links in post:** https://fcsc.fr/, https://twitter.com/kevin_mizu/status/2040130397179126227

**Quoted post (full text):**

    #### Quoted post — @kevin_mizu — 2026-04-03 18:12 UTC (2026-04-03 19:12 WAT)
    
    - URL: https://x.com/kevin_mizu/status/2040130397179126227
    - Metrics (at fetch): bookmark 63, impression 25958, like 138, quote 1, reply 4, retweet 17
    
    > This year again, with @BitK_ and @_Worty, we've made the Web challenges 🚩
    >
    > The CTF is solo and lasts 10 days, if you have some time, please give it a look 😁
    >
    > Even if you're not doing Web challenges, there are challenges in various categories, you should find something you like! [pic.x.com/S2z1mDPUu6]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/HE__yLmWUAA5QTG.png — no alt text provided by author
    


---

## 2026-04-03 · Post · This year again, with @BitK_ and @_Worty, we've made the Web challenges 🚩


### Post — @kevin_mizu — 2026-04-03 18:12 UTC (2026-04-03 19:12 WAT)

- URL: https://x.com/kevin_mizu/status/2040130397179126227
- Metrics (at fetch): bookmark 63, impression 25958, like 138, quote 1, reply 4, retweet 17

> This year again, with @BitK_ and @_Worty, we've made the Web challenges 🚩
>
> The CTF is solo and lasts 10 days, if you have some time, please give it a look 😁
>
> Even if you're not doing Web challenges, there are challenges in various categories, you should find something you like! [pic.x.com/S2z1mDPUu6]

**Media:**
- photo: https://pbs.twimg.com/media/HE__yLmWUAA5QTG.png — no alt text provided by author


---

## 2025-10-17 · Post · Two weeks ago, I did my first (in-person) @Hacker0x01 LHE in Singapore! I worked with @hash_kitten a


Tags (automatic): Platform: HackerOne


### Post — @kevin_mizu — 2025-10-17 08:16 UTC (2025-10-17 09:16 WAT)

- URL: https://x.com/kevin_mizu/status/1979099248973980127
- Metrics (at fetch): bookmark 9, impression 14160, like 125, quote 0, reply 7, retweet 6

> Two weeks ago, I did my first (in-person) @Hacker0x01 LHE in Singapore! I worked with @hash_kitten and @infosec_au, and I'm really happy with how it went and what we found :D
>
> (We won the Best Team and Best Bug awards! 🔥)
>
> It was an amazing event, thanks @Hacker0x01! 😁 https://twitter.com/Hacker0x01/status/1975254699063304297

**Links in post:** https://twitter.com/Hacker0x01/status/1975254699063304297

**Quoted post** 1975254699063304297: not readable via the API (deleted, private, or withheld).


---

## 2025-09-08 · Post · For the @ASIS_CTF, I created a challenge based on an interesting (novel?) DOM Clobbering technique! 


### Post — @kevin_mizu — 2025-09-08 15:10 UTC (2025-09-08 16:10 WAT)

- URL: https://x.com/kevin_mizu/status/1965070327345709143
- Metrics (at fetch): bookmark 54, impression 14014, like 132, quote 1, reply 1, retweet 29

> For the @ASIS_CTF, I created a challenge based on an interesting (novel?) DOM Clobbering technique! 🚩
>
> In short, in non-strict mode, HTMLCollection items are not writable. This blocks property assignment, allowing unexpected values to be created 😄
>
> 👉 https://mizu.re/post/under-the-beamer [pic.x.com/GknI26XHNX]

**Media:**
- photo: https://pbs.twimg.com/media/G0VUbt_XIAADp4_.jpg — no alt text provided by author

**Links in post:** https://mizu.re/post/under-the-beamer


---

## 2025-09-03 · Post · DOMLogger++ v1.0.9 is now out and available! 🎉


### Post — @kevin_mizu — 2025-09-03 14:32 UTC (2025-09-03 15:32 WAT)

- URL: https://x.com/kevin_mizu/status/1963248707039621232
- Metrics (at fetch): bookmark 48, impression 8081, like 152, quote 1, reply 2, retweet 28

> DOMLogger++ v1.0.9 is now out and available! 🎉
>
> This update fixes a lot of issues, including the historical DevTools bug on Chromium 🔥
>
> It also brings full Caido session handling, which is going to be useful in the near future! 👀
>
> 👉 https://t.co/wQHbXqzvkq
>
> 1/2 https://t.co/xT93PZtPZW

**Media:**
- photo: https://pbs.twimg.com/media/Gz7b40oXIAAPJp0.jpg — no alt text provided by author


---

## 2025-07-24 · Post · Each library page includes:


### Post — @kevin_mizu — 2025-07-24 15:31 UTC (2025-07-24 16:31 WAT)

- URL: https://x.com/kevin_mizu/status/1948405604629811640
- Metrics (at fetch): bookmark 2, impression 2865, like 11, quote 1, reply 1, retweet 4

> Each library page includes:
>
> * Affected versions
> * A short description
> * Root cause of the gadget
> * Related links
> * Credit to the discoverer
> * And even a preview button to play with the gadget live!
>
> 3/4 https://t.co/jHDvyxR9GV

**Media:**
- photo: https://pbs.twimg.com/media/GwofiRPWwAAA3uw.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GwoflBUW8AEfCrl.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GwofoGSXkAAoLf0.jpg — no alt text provided by author


---

## 2025-07-24 · Post · I'm happy to release a script gadgets wiki inspired by the work of @slekies, @kkotowicz, and @sirdar


### Post — @kevin_mizu — 2025-07-24 15:31 UTC (2025-07-24 16:31 WAT)

- URL: https://x.com/kevin_mizu/status/1948405598019518967
- Metrics (at fetch): bookmark 301, impression 43592, like 456, quote 3, reply 12, retweet 172

> I'm happy to release a script gadgets wiki inspired by the work of @slekies, @kkotowicz, and @sirdarckcat in their Black Hat USA 2017 talk! 🔥
>
> The goal is to provide quick access to gadgets that help bypass HTML sanitizers and CSPs 👇
>
> https://t.co/SgsSyxoEMR
>
> 1/4 https://t.co/RafUkR3NVn

**Media:**
- photo: https://pbs.twimg.com/media/Gwoey2BXcAEhPwY.jpg — no alt text provided by author


---

## 2025-06-19 · Post · If you love client-side challenges, I highly recommend checking this one out!


### Post — @kevin_mizu — 2025-06-19 12:53 UTC (2025-06-19 13:53 WAT)

- URL: https://x.com/kevin_mizu/status/1935682383035982064
- Metrics (at fetch): bookmark 8, impression 2524, like 50, quote 0, reply 0, retweet 2

> If you love client-side challenges, I highly recommend checking this one out!
>
> I'm sure you'll learn something new, amazing challenge by @Toogidog 🔥 https://t.co/4evtw5oNep

**Quoted post** 1935667064318185886: not readable via the API (deleted, private, or withheld).


---

## 2025-05-22 · Post · I've released my CTF bot template! :D


### Post — @kevin_mizu — 2025-05-22 18:02 UTC (2025-05-22 19:02 WAT)

- URL: https://x.com/kevin_mizu/status/1925613198096339196
- Metrics (at fetch): bookmark 40, impression 5811, like 119, quote 0, reply 0, retweet 19

> I've released my CTF bot template! :D
>
> It's not a big deal, but it comes with a heavily hardened Docker setup. The bot also sends a lot of debugging information over the TCP socket (console logs, navigation), which makes remote debugging much easier! 🔎
>
> 👉https://t.co/PGoeSZuqkh https://t.co/hs4Zisexv8

**Media:**
- photo: https://pbs.twimg.com/media/GrkmvM1XsAABZ3i.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GrkmxoGXEAAHtIN.jpg — no alt text provided by author


---

## 2025-04-28 · Post · All the other challenge write-ups (not just web) are available in the writeup channel of the CTF Di


### Post — @kevin_mizu — 2025-04-28 15:48 UTC (2025-04-28 16:48 WAT)

- URL: https://x.com/kevin_mizu/status/1916882108418806083
- Metrics (at fetch): bookmark 1, impression 809, like 6, quote 0, reply 0, retweet 1

> All the other challenge write-ups (not just web) are available in the #writeup channel of the CTF Discord server:
>
> https://t.co/sLWYnQTlie
>
> Thanks again to @ECSC_TeamFrance for the opportunity! 💙
>
> 2/2
