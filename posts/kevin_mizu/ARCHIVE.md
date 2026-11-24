# @kevin_mizu — full verbatim X archive (security-relevant posts)

_Generated 2026-11-24 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 75
- Conversations/threads: 58
- Oldest post captured: 2021-09-11
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

## 2026-10-16 · Post · I've been beta testing it, and I have to say it's a fun little idle game :D https://twitter.com/hiip


### Post — @kevin_mizu — 2026-10-16 15:04 UTC (2026-10-16 16:04 WAT)

- URL: https://x.com/kevin_mizu/status/2111111102394511707
- Metrics (at fetch): bookmark 9, impression 2688, like 32, quote 0, reply 2, retweet 2

> I've been beta testing it, and I have to say it's a fun little idle game :D https://twitter.com/hiippiiie/status/2111099846169936308

**Links in post:** https://twitter.com/hiippiiie/status/2111099846169936308

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

## 2026-07-21 · Thread · Chrome keeps adding fun features!


Tags (automatic): XSS


### Post — @kevin_mizu — 2026-07-21 13:06 UTC (2026-07-21 14:06 WAT)

- URL: https://x.com/kevin_mizu/status/2079553635470430622
- Metrics (at fetch): bookmark 33, impression 4859, like 88, quote 0, reply 3, retweet 7

> Chrome keeps adding fun features!
>
> After declarative partial updates, the CSS version is behind an experimental flag: https://issues.chromium.org/issues/448174611
>
> The new specifier attribute lets you poison import maps, even via DOMParser. Not XSS (text/css), but it can still block module loading :D [pic.x.com/al9OJxE0iV]

**Media:**
- photo: https://pbs.twimg.com/media/HNwOEsfWAAEQrRW.jpg — no alt text provided by author

**Links in post:** https://issues.chromium.org/issues/448174611


### Thread part 2 — @kevin_mizu — 2026-07-21 13:06 UTC (2026-07-21 14:06 WAT)

- URL: https://x.com/kevin_mizu/status/2079553637773148314
- Metrics (at fetch): bookmark 0, impression 771, like 8, quote 0, reply 0, retweet 0

> It's not in the stable release yet, but I've already reported it to the Chromium team, and they closed it as "Won't Fix (Infeasible)".
>
> If this ships, it could enable a fun gadget, even with HTML strings sanitized by DOMPurify :D


---

## 2026-07-17 · Post · 🔥🔥 https://twitter.com/hash_kitten/status/2078253959018648050


### Post — @kevin_mizu — 2026-07-17 23:05 UTC (2026-07-18 00:05 WAT)

- URL: https://x.com/kevin_mizu/status/2078254854087020589
- Metrics (at fetch): bookmark 9, impression 5974, like 37, quote 0, reply 0, retweet 1

> 🔥🔥 https://twitter.com/hash_kitten/status/2078253959018648050

**Links in post:** https://twitter.com/hash_kitten/status/2078253959018648050

**Quoted post** 2078253959018648050: not readable via the API (deleted, private, or withheld).


---

## 2026-07-09 · Post · It was a really fun event! Thanks to @Hacker0x01 and Salesforce for the invitation!


Tags (automatic): Platform: HackerOne


### Post — @kevin_mizu — 2026-07-09 15:05 UTC (2026-07-09 16:05 WAT)

- URL: https://x.com/kevin_mizu/status/2075234997246496822
- Metrics (at fetch): bookmark 10, impression 8483, like 102, quote 0, reply 7, retweet 7

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
> https://gmsgadget.com/preview/?html=%3Cscript%3E%0Afetch%28%22%2Fcdn-cgi%2Fimage%2Fformat%3D%3Cselect%3E%3Cselectedcontent%3E%3C%25252fselectedcontent%3E%3Coption%3E%3Csvg%3E%3Cscript%3Ealert%60%60%3C%25252fscript%3E%2Fx%22%29.then%28d%20%3D%3E%20d.text%28%29%29.then%28%28d%29%20%3D%3E%20%7B%20document.body.innerHTML%20%3D%20d%20%7D%29%3B%0A%3C%2Fscript%3E https://twitter.com/kinugawamasato/status/2074446473220214979

**Links in post:** https://gmsgadget.com/preview/?html=%3Cscript%3E%0Afetch%28%22%2Fcdn-cgi%2Fimage%2Fformat%3D%3Cselect%3E%3Cselectedcontent%3E%3C%25252fselectedcontent%3E%3Coption%3E%3Csvg%3E%3Cscript%3Ealert%60%60%3C%25252fscript%3E%2Fx%22%29.then%28d%20%3D%3E%20d.text%28%29%29.then%28%28d%29%20%3D%3E%20%7B%20document.body.innerHTML%20%3D%20d%20%7D%29%3B%0A%3C%2Fscript%3E, https://twitter.com/kinugawamasato/status/2074446473220214979

**Quoted post** 2074446473220214979: not readable via the API (deleted, private, or withheld).


---

## 2026-07-03 · Post · @J0R1AN I mean, on attr update**!


### Post — @kevin_mizu — 2026-07-03 10:08 UTC (2026-07-03 11:08 WAT)

- URL: https://x.com/kevin_mizu/status/2072985718272475531
- Metrics (at fetch): bookmark 0, impression 71, like 0, quote 0, reply 0, retweet 0

> @J0R1AN I mean, on attr update**!


---

## 2026-05-19 · Post · It's a really nice challenge! If you have some time, give it a try 🚩 https://twitter.com/hash_kitten


### Post — @kevin_mizu — 2026-05-19 07:19 UTC (2026-05-19 08:19 WAT)

- URL: https://x.com/kevin_mizu/status/2056635918648254507
- Metrics (at fetch): bookmark 4, impression 3515, like 30, quote 0, reply 1, retweet 0

> It's a really nice challenge! If you have some time, give it a try 🚩 https://twitter.com/hash_kitten/status/2056635004688769237

**Links in post:** https://twitter.com/hash_kitten/status/2056635004688769237

**Quoted post** 2056635004688769237: not readable via the API (deleted, private, or withheld).


---

## 2026-04-12 · Thread · The FCSC2026 ended today, and my write-ups are now available here:


### Post — @kevin_mizu — 2026-04-12 15:10 UTC (2026-04-12 16:10 WAT)

- URL: https://x.com/kevin_mizu/status/2043345976140656799
- Metrics (at fetch): bookmark 38, impression 8422, like 76, quote 1, reply 3, retweet 19

> The #FCSC2026 ended today, and my write-ups are now available here:
>
> https://mizu.re/post/fcsc-2026-writeups 🚩
>
> I'm really happy with the challenges I managed to create this year! It would be too long to list everything, so here's a little teaser 👇
>
> 1/2 [pic.x.com/NZc7H1VtRG] https://twitter.com/kevin_mizu/status/2040130397179126227

**Media:**
- photo: https://pbs.twimg.com/media/HFtsI_1a4AACON1.jpg — no alt text provided by author

**Links in post:** https://mizu.re/post/fcsc-2026-writeups, https://twitter.com/kevin_mizu/status/2040130397179126227

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
> 👉 https://github.com/kevin-mizu/domloggerpp-caido [pic.x.com/tRdiFP6M0T]

**Media:**
- photo: https://pbs.twimg.com/media/HFZE16XbQAAkn9V.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HFZE4nGXsAAskJN.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HFZE7CiXwAEQ10u.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/HFZE_EjWQAAdLl-.jpg — no alt text provided by author

**Links in post:** https://github.com/kevin-mizu/domloggerpp-caido


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

## 2025-09-03 · Thread · DOMLogger++ v1.0.9 is now out and available! 🎉


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


### Thread part 2 — @kevin_mizu — 2025-09-03 14:32 UTC (2025-09-03 15:32 WAT)

- URL: https://x.com/kevin_mizu/status/1963248710873145586
- Metrics (at fetch): bookmark 2, impression 1057, like 15, quote 0, reply 2, retweet 0

> Small teaser for Caido users :)
>
> 2/2 https://t.co/N6OOdW96a6

**Media:**
- photo: https://pbs.twimg.com/media/Gz7cAieXEAAmr5F.jpg — no alt text provided by author


---

## 2025-07-24 · Thread · I'm happy to release a script gadgets wiki inspired by the work of @slekies, @kkotowicz, and @sirdar


Tags (automatic): CSP / CSPT


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


### Thread part 2 — @kevin_mizu — 2025-07-24 15:31 UTC (2025-07-24 16:31 WAT)

- URL: https://x.com/kevin_mizu/status/1948405601488228684
- Metrics (at fetch): bookmark 3, impression 1994, like 7, quote 0, reply 1, retweet 2

> The wiki lets you filter gadgets by browser, tags, attributes, CSP, and timing, making it as easy as possible to find interesting vectors (at least I hope so!) 🔎
>
> 2/4 https://t.co/u8yYiwV3qy

**Media:**
- photo: https://pbs.twimg.com/media/GwofA9-W0AALIXY.png — no alt text provided by author


### Thread part 3 — @kevin_mizu — 2025-07-24 15:31 UTC (2025-07-24 16:31 WAT)

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


### Thread part 4 — @kevin_mizu — 2025-07-24 15:31 UTC (2025-07-24 16:31 WAT)

- URL: https://x.com/kevin_mizu/status/1948405607012167690
- Metrics (at fetch): bookmark 2, impression 1902, like 9, quote 0, reply 2, retweet 2

> This is still v1, there's lots to improve and many gadgets to add.
>
> If you'd like to contribute or have any feedback, please don't hesitate to reach out 😁
>
> 4/4


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


---

## 2025-04-18 · Post · This year again, with @BitK_, we've made the Web challenges 🚩


### Post — @kevin_mizu — 2025-04-18 16:32 UTC (2025-04-18 17:32 WAT)

- URL: https://x.com/kevin_mizu/status/1913269540156309910
- Metrics (at fetch): bookmark 19, impression 8879, like 93, quote 1, reply 1, retweet 7

> This year again, with @BitK_, we've made the Web challenges 🚩
>
> The CTF is solo and lasts 10 days, if you have some time, please give it a look 😁
>
> Btw, even if you're not doing Web challenges, there are 100+ challenges in various categories, you should find something you like! [pic.x.com/FSFLlVvkiH] https://twitter.com/ANSSI_FR/status/1913201106890477808

**Media:**
- photo: https://pbs.twimg.com/media/Go1MaLeXgBArbpC.png — no alt text provided by author

**Links in post:** https://twitter.com/ANSSI_FR/status/1913201106890477808

**Quoted post** 1913201106890477808: not readable via the API (deleted, private, or withheld).


---

## 2025-03-02 · Post · For this challenge, it was necessary to abuse a discrepancy between the DOM and the rendered page in


### Post — @kevin_mizu — 2025-03-02 17:14 UTC (2025-03-02 18:14 WAT)

- URL: https://x.com/kevin_mizu/status/1896247733721370815
- Metrics (at fetch): bookmark 58, impression 8303, like 106, quote 0, reply 1, retweet 22

> For this challenge, it was necessary to abuse a discrepancy between the DOM and the rendered page in Firefox's cache handling 💽
>
> 👉 https://bugzilla.mozilla.org/show_bug.cgi?id=356558
>
> This allows to shift iframe rendering from one to another leading to a sandbox bypass 🔥
>
> 👉 https://mizu.re/post/an-18-years-old-bug [pic.x.com/djNmmKrj0M] https://twitter.com/kevin_mizu/status/1895551723844083815

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1896246689377177600/pu/img/xthJ9ygUkRhWWUrt.jpg — no alt text provided by author

**Links in post:** https://bugzilla.mozilla.org/show_bug.cgi?id=356558, https://mizu.re/post/an-18-years-old-bug, https://twitter.com/kevin_mizu/status/1895551723844083815

**Quoted post (full text):**

    #### Quoted post — @kevin_mizu — 2025-02-28 19:08 UTC (2025-02-28 20:08 WAT)
    
    - URL: https://x.com/kevin_mizu/status/1895551723844083815
    - Metrics (at fetch): bookmark 21, impression 12889, like 70, quote 1, reply 0, retweet 8
    
    > With @Geluchat, we created a challenge for the @pwnmectf inspired by a bug he found in bug bounty a year ago! 🚀
    >
    > If you have some time this weekend, give it a try! 👀
    >
    > 👉 https://pwnme.phreaks.fr/ [pic.x.com/Zc19b4oGUx] https://twitter.com/pwnmectf/status/1895551313737617463
    
    **Media:**
    - photo: https://pbs.twimg.com/media/Gk5aPkVXgAA8Bm-.png — no alt text provided by author
    
    **Links in post:** https://pwnme.phreaks.fr/, https://twitter.com/pwnmectf/status/1895551313737617463
    
    **Quoted post** 1895551313737617463: not readable via the API (deleted, private, or withheld).
    


---

## 2025-02-28 · Post · With @Geluchat, we created a challenge for the @pwnmectf inspired by a bug he found in bug bounty a 


### Post — @kevin_mizu — 2025-02-28 19:08 UTC (2025-02-28 20:08 WAT)

- URL: https://x.com/kevin_mizu/status/1895551723844083815
- Metrics (at fetch): bookmark 21, impression 12889, like 70, quote 1, reply 0, retweet 8

> With @Geluchat, we created a challenge for the @pwnmectf inspired by a bug he found in bug bounty a year ago! 🚀
>
> If you have some time this weekend, give it a try! 👀
>
> 👉 https://pwnme.phreaks.fr/ [pic.x.com/Zc19b4oGUx] https://twitter.com/pwnmectf/status/1895551313737617463

**Media:**
- photo: https://pbs.twimg.com/media/Gk5aPkVXgAA8Bm-.png — no alt text provided by author

**Links in post:** https://pwnme.phreaks.fr/, https://twitter.com/pwnmectf/status/1895551313737617463

**Quoted post** 1895551313737617463: not readable via the API (deleted, private, or withheld).


---

## 2025-02-10 · Thread · I'm very happy to finally share the second part of my DOMPurify security research 🔥


### Post — @kevin_mizu — 2025-02-10 17:53 UTC (2025-02-10 18:53 WAT)

- URL: https://x.com/kevin_mizu/status/1889009906994520260
- Metrics (at fetch): bookmark 233, impression 37110, like 358, quote 4, reply 4, retweet 101

> I'm very happy to finally share the second part of my DOMPurify security research 🔥
>
> This article mostly focuses on DOMPurify misconfigurations, especially hooks, that downgrade the sanitizer's protection (even in the latest version)!
>
> Link 👇
> https://t.co/Hg1MkqVuGw
>
> 1/2


### Thread part 2 — @kevin_mizu — 2025-02-10 17:53 UTC (2025-02-10 18:53 WAT)

- URL: https://x.com/kevin_mizu/status/1889009909896995247
- Metrics (at fetch): bookmark 2, impression 2408, like 21, quote 0, reply 0, retweet 1

> I would like to thank @cure53berlin, @IcesFont, @Geluchat, @_Worty, @PikuHaku, @monkehack, and @Rhynorater (I hope I'm not missing anyone) for reviewing this article 🙏
>
> 2/2


---

## 2025-02-07 · Thread · Thanks to the recent @PortSwigger top 10, I finally found the motivation to finish writing the 2nd a


### Post — @kevin_mizu — 2025-02-07 16:32 UTC (2025-02-07 17:32 WAT)

- URL: https://x.com/kevin_mizu/status/1887902199390363799
- Metrics (at fetch): bookmark 55, impression 12117, like 145, quote 1, reply 1, retweet 15

> Thanks to the recent @PortSwigger top 10, I finally found the motivation to finish writing the 2nd article about DOMPurify security! 😁
>
> Before releasing it, I would like to share a small challenge 🚩
>
> Challenge link 👇
> https://t.co/Fw1ePWFOMB
>
> 1/2 https://t.co/EWJqS3e2Dd

**Media:**
- photo: https://pbs.twimg.com/media/GjMsl0bXYAATdsI.jpg — no alt text provided by author


### Thread part 2 — @kevin_mizu — 2025-02-07 16:32 UTC (2025-02-07 17:32 WAT)

- URL: https://x.com/kevin_mizu/status/1887902201881780684
- Metrics (at fetch): bookmark 1, impression 1039, like 9, quote 0, reply 0, retweet 0

> This is probably not the most realistic challenge, but I find the tricks behind it quite interesting!
>
> Rules 📜
> - You should only use the provided endpoint.
> - The solution must not involve user interaction.
>
> If you find the solution, please send me a DM 📩
>
> 2/2


---

## 2024-11-06 · Post · I recently reported an RCE to Happy-DOM (a Node.js HTML parser), and it’s now fixed!


Tags (automatic): RCE


### Post — @kevin_mizu — 2024-11-06 20:26 UTC (2024-11-06 21:26 WAT)

- URL: https://x.com/kevin_mizu/status/1854259206594945068
- Metrics (at fetch): bookmark 150, impression 21469, like 373, quote 1, reply 4, retweet 53

> I recently reported an RCE to Happy-DOM (a Node.js HTML parser), and it’s now fixed!
>
> The bug itself wasn't complex, but since finding an RCE in an HTML parser isn’t very common, I'm quite happy with this one :D
>
> https://github.com/capricorn86/happy-dom/security/advisories/GHSA-96g7-g7g9-jxw8 [pic.x.com/Szx64N2stR]

**Media:**
- photo: https://pbs.twimg.com/media/Gbumbh1WAAc_QZb.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/Gbumdf8WUB0M30m.jpg — no alt text provided by author

**Links in post:** https://github.com/capricorn86/happy-dom/security/advisories/GHSA-96g7-g7g9-jxw8


---

## 2024-10-28 · Post · I was really surprised to see that the Cache API is exposed on window, allowing a simple XSS to hija


Tags (automatic): XSS


### Post — @kevin_mizu — 2024-10-28 17:14 UTC (2024-10-28 18:14 WAT)

- URL: https://x.com/kevin_mizu/status/1850949199812313321
- Metrics (at fetch): bookmark 101, impression 19848, like 158, quote 1, reply 5, retweet 24

> I was really surprised to see that the Cache API is exposed on window, allowing a simple XSS to hijack a service worker and achieve persistent XSS on most pages of a vulnerable website!
>
> It might not be a new, but I feel like it is an incredible XSS leveraging gadget :D https://t.co/PR4fmszaQt https://t.co/zcaraRjDxl

**Media:**
- photo: https://pbs.twimg.com/media/Ga_kOGzaYAEG5s8.jpg — no alt text provided by author

**Quoted post** 1850932349569282491: not readable via the API (deleted, private, or withheld).


---

## 2024-07-18 · Thread · This HTML parsing behavior is absolutely wtf...


### Post — @kevin_mizu — 2024-07-18 15:00 UTC (2024-07-18 16:00 WAT)

- URL: https://x.com/kevin_mizu/status/1813951932639092785
- Metrics (at fetch): bookmark 99, impression 16668, like 162, quote 0, reply 2, retweet 32

> This HTML parsing behavior is absolutely wtf...
>
> It can be abused to completely bypass any server-side HTML sanitizer when a second user input is present earlier in the document within a script string... [pic.x.com/0SJhUCNDl3] https://twitter.com/garethheyes/status/1813658752245236105

**Media:**
- photo: https://pbs.twimg.com/media/GSxzfrzXkAAF1ur.jpg — no alt text provided by author
- photo: https://pbs.twimg.com/media/GSxzg6lXEAAilf6.jpg — no alt text provided by author

**Links in post:** https://twitter.com/garethheyes/status/1813658752245236105

**Quoted post** 1813658752245236105: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @kevin_mizu — 2024-07-18 15:13 UTC (2024-07-18 16:13 WAT)

- URL: https://x.com/kevin_mizu/status/1813955250614833458
- Metrics (at fetch): bookmark 0, impression 902, like 2, quote 0, reply 2, retweet 0

> @garethheyes Oops, I might need to read your book a second time! I wasn't aware of this parsing behavior at all, it's really impressive!
>
> Do you have any specification references associated with this specific behavior? I'm curious to see why this would be necessary :D


### Thread part 3 — @kevin_mizu — 2024-07-18 17:02 UTC (2024-07-18 18:02 WAT)

- URL: https://x.com/kevin_mizu/status/1813982733854818483
- Metrics (at fetch): bookmark 0, impression 346, like 0, quote 0, reply 1, retweet 0

> @garethheyes Thanks! I'll give it a look 😁


### Thread part 4 — @kevin_mizu — 2024-07-18 17:47 UTC (2024-07-18 18:47 WAT)

- URL: https://x.com/kevin_mizu/status/1813994009905578045
- Metrics (at fetch): bookmark 0, impression 370, like 0, quote 0, reply 1, retweet 0

> @garethheyes I feel you, specs can be really complicated to understand sometimes. I haven't tried Shazzer yet. I should give it some time, the tool looks super powerfull! :D


---

## 2024-07-15 · Thread · Great research from @scryh_!


### Post — @kevin_mizu — 2024-07-15 16:10 UTC (2024-07-15 17:10 WAT)

- URL: https://x.com/kevin_mizu/status/1812882499875319959
- Metrics (at fetch): bookmark 229, impression 33235, like 317, quote 0, reply 2, retweet 63

> Great research from @scryh_!
>
> I was keeping it for a CTF challenge, but it's probably too late now :p
>
> This trick is so powerful that it can be used to bypass most (if not all) server-side HTML sanitizers in the absence of a charset within the Content-Type response header 🤯 [pic.x.com/h5UHsLVR10] https://twitter.com/Sonar_Research/status/1812864424807444825

**Media:**
- photo: https://pbs.twimg.com/media/GSinBrYWEAAUADo.jpg — no alt text provided by author

**Links in post:** https://twitter.com/Sonar_Research/status/1812864424807444825

**Quoted post** 1812864424807444825: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @kevin_mizu — 2024-07-15 16:50 UTC (2024-07-15 17:50 WAT)

- URL: https://x.com/kevin_mizu/status/1812892594843582632
- Metrics (at fetch): bookmark 13, impression 2280, like 28, quote 0, reply 0, retweet 2

> The code is available here: https://t.co/ai1BHGfaLI


---

## 2024-05-23 · Thread · I think it's time for a solution ⏰


### Post — @kevin_mizu — 2024-05-23 15:28 UTC (2024-05-23 16:28 WAT)

- URL: https://x.com/kevin_mizu/status/1793665227202175483
- Metrics (at fetch): bookmark 33, impression 11642, like 90, quote 0, reply 2, retweet 24

> I think it's time for a solution ⏰
>
> TL;DR
> - Eventlet normalizes - to _ in header keys.
> - The Fetch spec blocks Transfer-Encoding but not Transfer_Encoding.
> - Bypass tracking policy on Firefox using open().
>
> Detailed writeup 👇
> https://mizu.re/post/twitter-eventlet-csd
>
> 1/2 https://twitter.com/kevin_mizu/status/1790035413685391775

**Links in post:** https://mizu.re/post/twitter-eventlet-csd, https://twitter.com/kevin_mizu/status/1790035413685391775

**Quoted post** 1790035413685391775: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @kevin_mizu — 2024-05-23 15:29 UTC (2024-05-23 16:29 WAT)

- URL: https://x.com/kevin_mizu/status/1793665584955351294
- Metrics (at fetch): bookmark 0, impression 950, like 3, quote 0, reply 1, retweet 0

> Again, congratz to all the solvers 🔥
>
> - @Alex_ctf_ 🏆
> - @Satoooon1024 🥈
> - @hulitw and @BrunoModificato 🥉
> - @BitK_
> - @frevadiscor89
> - @parrot409
> - @ldionmarcil
> - @taramtrampam
>
> 2/2


### Thread part 3 — @kevin_mizu — 2024-05-23 18:11 UTC (2024-05-23 19:11 WAT)

- URL: https://x.com/kevin_mizu/status/1793706425824252220
- Metrics (at fetch): bookmark 0, impression 283, like 3, quote 0, reply 0, retweet 0

> @S1r1u5_ Thanks 🙏
>
> I'll try to come up with more challenges in the upcoming month :p


---

## 2024-05-11 · Thread · Really proud of those bypass/mXSS variations. They involve some cool second-order DOM Clobbering and


### Post — @kevin_mizu — 2024-05-11 11:27 UTC (2024-05-11 12:27 WAT)

- URL: https://x.com/kevin_mizu/status/1789255979713941561
- Metrics (at fetch): bookmark 28, impression 11252, like 89, quote 0, reply 5, retweet 13

> Really proud of those bypass/mXSS variations. They involve some cool second-order DOM Clobbering and a new mutation gadget that I would like to call the elevator x)
>
> 1/2 https://twitter.com/cure53berlin/status/1789242798417281358

**Links in post:** https://twitter.com/cure53berlin/status/1789242798417281358

**Quoted post** 1789242798417281358: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @kevin_mizu — 2024-05-11 11:28 UTC (2024-05-11 12:28 WAT)

- URL: https://x.com/kevin_mizu/status/1789256347743137963
- Metrics (at fetch): bookmark 2, impression 10255, like 24, quote 3, reply 4, retweet 0

> It was fun looking for bugs with @ryotkak, @hash_kitten, @joaxcar, @TheGrandPew and @IcesFont 😁
>
> As always, thanks to @cure53berlin for the reactivity 🙏
>
> 2/2


---

## 2024-04-26 · Post · I've finally finished my writeups for FCSC2024, which covered:


Tags (automatic): Request smuggling / desync


### Post — @kevin_mizu — 2024-04-26 16:01 UTC (2024-04-26 17:01 WAT)

- URL: https://x.com/kevin_mizu/status/1783889269372654064
- Metrics (at fetch): not returned

> I've finally finished my writeups for #FCSC2024, which covered:
>
> - Nginx X-Accel-Redirect file read
> - Werkzeug error-based request smuggling
> - HTTP/1.1 and HTTP/0.9 browser confusion
> - Connection: close bypass via Expect: 100-continue
> - ...
>
> Link 👇
>
> https://mizu.re/tag/FCSC2024
>
> 1/2

**Links in post:** https://mizu.re/tag/FCSC2024


---

## 2024-04-10 · Post · If you are doing bug bounty you should definitely check out @Icare1337's research on LibreOffice 🔥 h


### Post — @kevin_mizu — 2024-04-10 07:37 UTC (2024-04-10 08:37 WAT)

- URL: https://x.com/kevin_mizu/status/1777964155934253254
- Metrics (at fetch): not returned

> If you are doing bug bounty you should definitely check out @Icare1337's research on LibreOffice 🔥 https://twitter.com/Icare1337/status/1777956864501670003

**Links in post:** https://twitter.com/Icare1337/status/1777956864501670003

**Quoted post (full text):**

    #### Quoted post — @72546363 — 2024-04-10 07:08 UTC (2024-04-10 08:08 WAT)
    
    - URL: https://x.com/72546363/status/1777956864501670003
    - Metrics (at fetch): not returned
    
    > https://github.com/Icare1337/LibreOffice_Tips_Bug_Bounty
    > #BugBounty #bugbountytips  #libreoffice
    
    **Links in post:** https://github.com/Icare1337/LibreOffice_Tips_Bug_Bounty
    


---

## 2024-02-21 · Post · Recently, I discovered a DOMPurify bypass in the case of CUSTOM_ELEMENT_HANDLING and FORBID_CONTENT 


### Post — @kevin_mizu — 2024-02-21 16:31 UTC (2024-02-21 17:31 WAT)

- URL: https://x.com/kevin_mizu/status/1760341445872144520
- Metrics (at fetch): not returned

> Recently, I discovered a DOMPurify bypass in the case of CUSTOM_ELEMENT_HANDLING and FORBID_CONTENT options usage ⏭️
>
> This issue isn't a big deal as it doesn't involve a default configuration bypass. However, I thought it was interesting to document it 👇
>
> https://mizu.re/post/playing-with-dompurify-ce-handling

**Links in post:** https://mizu.re/post/playing-with-dompurify-ce-handling


---

## 2024-01-26 · Post · Challenge time is now over ⏰


Tags (automatic): XSS


### Post — @kevin_mizu — 2024-01-26 16:35 UTC (2024-01-26 17:35 WAT)

- URL: https://x.com/kevin_mizu/status/1750920355173351923
- Metrics (at fetch): not returned

> Challenge time is now over ⏰
>
> TL;DR
> - HTML injection
> - Axios DOM Based CSPP
> - Axios CSPP response overwrite gadget
> - jQuery DOM Clobbering + CSPP selector overwrite gadgets
> - Setting src attr to "javascript:" for each HTML node ➝ XSS
>
> Detailed writeup 👇
> https://mizu.re/post/intigriti-january-2024-xss-challenge https://twitter.com/kevin_mizu/status/1747566277244387636

**Links in post:** https://mizu.re/post/intigriti-january-2024-xss-challenge, https://twitter.com/kevin_mizu/status/1747566277244387636

**Quoted post (full text):**

    #### Quoted post — @kevin_mizu — 2024-01-17 10:27 UTC (2024-01-17 11:27 WAT)
    
    - URL: https://x.com/kevin_mizu/status/1747566277244387636
    - Metrics (at fetch): not returned
    
    > GG to all the solvers! However, no one solved it in the intended way :p
    >
    > Before giving my solution, I'm extending the challenge for another week with a fixed version!
    >
    > If you find the solution, please send me a DM 📮
    >
    > The challenge is accessible here 👇
    > http://mizu.re:3000/ https://twitter.com/intigriti/status/1747292757125693764
    
    **Links in post:** http://mizu.re:3000/, https://twitter.com/intigriti/status/1747292757125693764
    
    **Quoted post** 1747292757125693764: not readable via the API (deleted, private, or withheld).
    


---

## 2024-01-17 · Post · GG to all the solvers! However, no one solved it in the intended way :p


### Post — @kevin_mizu — 2024-01-17 10:27 UTC (2024-01-17 11:27 WAT)

- URL: https://x.com/kevin_mizu/status/1747566277244387636
- Metrics (at fetch): not returned

> GG to all the solvers! However, no one solved it in the intended way :p
>
> Before giving my solution, I'm extending the challenge for another week with a fixed version!
>
> If you find the solution, please send me a DM 📮
>
> The challenge is accessible here 👇
> http://mizu.re:3000/ https://twitter.com/intigriti/status/1747292757125693764

**Links in post:** http://mizu.re:3000/, https://twitter.com/intigriti/status/1747292757125693764

**Quoted post** 1747292757125693764: not readable via the API (deleted, private, or withheld).


---

## 2023-12-21 · Post · In September, I looked into mlflow, and found several critical vulnerabilities 😁


### Post — @kevin_mizu — 2023-12-21 16:18 UTC (2023-12-21 17:18 WAT)

- URL: https://x.com/kevin_mizu/status/1737870103985996207
- Metrics (at fetch): not returned

> In September, I looked into mlflow, and found several critical vulnerabilities 😁
>
> Most of these reports are now patched and publicly available here: https://huntr.com/users/kevin-mizu
>
> My favorite one involves a fully controlled file write via a custom rogue FTP 👇https://huntr.com/bounties/029a3824-cee3-4cf1-b260-7138aa539b85/

**Links in post:** https://huntr.com/users/kevin-mizu, https://huntr.com/bounties/029a3824-cee3-4cf1-b260-7138aa539b85/


---

## 2023-12-16 · Post · I think it's time for a solution ⏰


Tags (automatic): XSS


### Post — @kevin_mizu — 2023-12-16 11:24 UTC (2023-12-16 12:24 WAT)

- URL: https://x.com/kevin_mizu/status/1735984327274688630
- Metrics (at fetch): not returned

> I think it's time for a solution ⏰
>
> To solve this challenge, you had to abuse the DOMPurify namespace misconfiguration to trigger an XSS this way 👇
>
> Solution link: https://challenges.mizu.re/xss_02.html?html=a%3Cstyle%3E%3C!--%3C/style%3E%3Ca%20id=%22--!%3E%3Cimg%20src=x%20onerror=alert()%3E%22%3E
>
> 1/6 [pic.x.com/crztnomjq6] https://twitter.com/kevin_mizu/status/1733086824518787473

**Media:**
- photo: https://pbs.twimg.com/media/GBd0i-wbsAACgA3.jpg — no alt text provided by author

**Links in post:** https://challenges.mizu.re/xss_02.html?html=a%3Cstyle%3E%3C!--%3C/style%3E%3Ca%20id=%22--!%3E%3Cimg%20src=x%20onerror=alert()%3E%22%3E, https://twitter.com/kevin_mizu/status/1733086824518787473

**Quoted post (full text):**

    #### Quoted post — @kevin_mizu — 2023-12-08 11:31 UTC (2023-12-08 12:31 WAT)
    
    - URL: https://x.com/kevin_mizu/status/1733086824518787473
    - Metrics (at fetch): not returned
    
    > Small XSS Challenge Time 🚩
    >
    > Rules 📜
    > - You should only use the provided endpoint.
    > - The solution must not involve user interaction.
    >
    > If you find the solution, please do not send it in the comments; send me a DM instead 📩
    >
    > Challenge link 👇
    > https://challenges.mizu.re/xss_02.html [pic.x.com/68HPqR7pOG]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/GA0pSELbkAAvskD.jpg — no alt text provided by author
    
    **Links in post:** https://challenges.mizu.re/xss_02.html
    


---

## 2023-12-08 · Post · Small XSS Challenge Time 🚩


Tags (automatic): XSS


### Post — @kevin_mizu — 2023-12-08 11:31 UTC (2023-12-08 12:31 WAT)

- URL: https://x.com/kevin_mizu/status/1733086824518787473
- Metrics (at fetch): not returned

> Small XSS Challenge Time 🚩
>
> Rules 📜
> - You should only use the provided endpoint.
> - The solution must not involve user interaction.
>
> If you find the solution, please do not send it in the comments; send me a DM instead 📩
>
> Challenge link 👇
> https://challenges.mizu.re/xss_02.html [pic.x.com/68HPqR7pOG]

**Media:**
- photo: https://pbs.twimg.com/media/GA0pSELbkAAvskD.jpg — no alt text provided by author

**Links in post:** https://challenges.mizu.re/xss_02.html


---

## 2023-11-19 · Post · For the @GrehackConf 2023 CTF, I made 2 hard web challenges 🚩


Tags (automatic): RCE


### Post — @kevin_mizu — 2023-11-19 11:10 UTC (2023-11-19 12:10 WAT)

- URL: https://x.com/kevin_mizu/status/1726196358489727069
- Metrics (at fetch): not returned

> For the @GrehackConf 2023 #CTF, I made 2 hard #web challenges 🚩
>
> They were about:
> [1] Python class pollution to RCE on Flask application
> [2] HTTPOnly cookie leak due to Werkzeug improper Cookie parsing
>
> Detailed writeups 👇
> [1] https://mizu.re/post/insecure-session-storage
> [2] https://mizu.re/post/another-html-renderer

**Links in post:** https://mizu.re/post/insecure-session-storage, https://mizu.re/post/another-html-renderer


---

## 2023-11-13 · Post · Challenge time is now over, I hope you've liked it! 😁


Tags (automatic): XSS


### Post — @kevin_mizu — 2023-11-13 14:27 UTC (2023-11-13 15:27 WAT)

- URL: https://x.com/kevin_mizu/status/1724071543159046278
- Metrics (at fetch): not returned

> Challenge time is now over, I hope you've liked it! 😁
>
> TL;DR
> - mXSS via client-side / server-side confusion
> - auto download to store the payload on file://
> - puppeteer bot without SOP ➝ devtools (CDP)
> - open file:// ➝ leak the flag
>
> Detailed writeup 👇
> https://mizu.re/post/intigriti-october-2023-xss-challenge https://twitter.com/intigriti/status/1724066913561493834

**Links in post:** https://mizu.re/post/intigriti-october-2023-xss-challenge, https://twitter.com/intigriti/status/1724066913561493834

**Quoted post (full text):**

    #### Quoted post — @736615159653924864 — 2023-11-13 14:09 UTC (2023-11-13 15:09 WAT)
    
    - URL: https://x.com/736615159653924864/status/1724066913561493834
    - Metrics (at fetch): not returned
    
    > 📚 Can't get enough of this challenge? Here's the official writeup by @kevin_mizu 💜
    >
    > https://mizu.re/post/intigriti-october-2023-xss-challenge
    
    **Links in post:** https://mizu.re/post/intigriti-october-2023-xss-challenge
    


---

## 2023-09-01 · Post · I wasn't knowing what to do yesterday night so, I decided to create an XSS challenge 🚩


Tags (automatic): XSS


### Post — @kevin_mizu — 2023-09-01 15:02 UTC (2023-09-01 16:02 WAT)

- URL: https://x.com/kevin_mizu/status/1697625861543923906
- Metrics (at fetch): not returned

> I wasn't knowing what to do yesterday night so, I decided to create an XSS challenge 🚩
>
> There is nothing to win, I made it just for fun! If you want to try it out, click on the link below 👇
>
> https://mizu.re/challenges/xss_1/index.html
>
> The final goal it to pop an alert without any interaction 🔥 [pic.x.com/1dVA3qn8Yk]

**Media:**
- photo: https://pbs.twimg.com/media/F48tqfUWMAApKf_.jpg — no alt text provided by author

**Links in post:** https://mizu.re/challenges/xss_1/index.html


---

## 2023-07-27 · Post · My vulnerability reports on http://draw.io are now available! ⚠️


Tags (automatic): XSS, RCE


### Post — @kevin_mizu — 2023-07-27 15:43 UTC (2023-07-27 16:43 WAT)

- URL: https://x.com/kevin_mizu/status/1684590428954173440
- Metrics (at fetch): not returned

> My vulnerability reports on http://draw.io are now available! ⚠️
>
> If you use the desktop version, think about updating it! More information bellow 👇
>
> - RCE: https://shorturl.at/ahlKM
> - XSS to RCE: https://shorturl.at/yAFJ9
> - XSS: https://shorturl.at/rwBFR

**Links in post:** http://draw.io, https://shorturl.at/ahlKM, https://shorturl.at/yAFJ9, https://shorturl.at/rwBFR


---

## 2023-07-04 · Post · Recently, I've started to search for full chains XSS to RCE on http://draw.io desktop application. W


Tags (automatic): XSS, RCE, CSP / CSPT


### Post — @kevin_mizu — 2023-07-04 15:22 UTC (2023-07-04 16:22 WAT)

- URL: https://x.com/kevin_mizu/status/1676250162908282882
- Metrics (at fetch): not returned

> Recently, I've started to search for full chains XSS to RCE on http://draw.io desktop application. With this objective in mind, I came up with an interesting concept of CSP script-src self bypass for local electron apps on Linux! ⏭️
>
> Link below 👇
> https://mizu.re/post/linux-local-electron-application-script-src-self-bypass

**Links in post:** http://draw.io, https://mizu.re/post/linux-local-electron-application-script-src-self-bypass


---

## 2023-06-08 · Post · I'm glad to finally present my research about "Abusing Client-Side Desync on Werkzeug" at @sstic 202


Tags (automatic): Request smuggling / desync


### Post — @kevin_mizu — 2023-06-08 15:16 UTC (2023-06-08 16:16 WAT)

- URL: https://x.com/kevin_mizu/status/1666826474727391236
- Metrics (at fetch): not returned

> I'm glad to finally present my research about "Abusing Client-Side Desync on Werkzeug" at @sstic 2023 📜
>
> Research paper is available here: https://mizu.re/post/abusing-client-side-desync-on-werkzeug 
> Slides are available here: https://slides.com/kevin-mizu/sstic-2023-abusing-client-side-desync-on-werkzeug-cve-2022-29361 [pic.x.com/lutDYt5vSF]

**Media:**
- photo: https://pbs.twimg.com/media/FyHB1vKWAAAEZoJ.jpg — no alt text provided by author

**Links in post:** https://mizu.re/post/abusing-client-side-desync-on-werkzeug, https://slides.com/kevin-mizu/sstic-2023-abusing-client-side-desync-on-werkzeug-cve-2022-29361


---

## 2023-04-11 · Post · My writeup for the march @intigriti XSS challenge :


Tags (automatic): XSS


### Post — @kevin_mizu — 2023-04-11 14:21 UTC (2023-04-11 15:21 WAT)

- URL: https://x.com/kevin_mizu/status/1645794203325337605
- Metrics (at fetch): bookmark 4, impression 6941, like 49, quote 0, reply 1, retweet 12

> My writeup for the march @intigriti #XSS challenge :
>
> https://t.co/hzp9pQsxI5
>
> Thanks @0xGodson_ and @BrunoModificato for the quality of the challenge 🙏


---

## 2023-03-22 · Post · I'm glad to announce that I will present a talk at @sstic 2023 about an interesting Client-Side Des


Tags (automatic): XSS, Request smuggling / desync


### Post — @kevin_mizu — 2023-03-22 16:30 UTC (2023-03-22 17:30 WAT)

- URL: https://x.com/kevin_mizu/status/1638578821258518531
- Metrics (at fetch): bookmark 0, impression 7373, like 81, quote 2, reply 0, retweet 25

> I'm glad to announce that I will present a talk at @sstic #2023 about an interesting Client-Side Desync case I found past year in Werkzeug that can be leveraged to XSS on default configurations 🔥
>
> More information here: https://t.co/WSZsoD798E


---

## 2023-03-09 · Thread · Last month, I did some research on NodeJS templating libraries. During this research, I found an int


Tags (automatic): RCE


### Post — @kevin_mizu — 2023-03-09 16:08 UTC (2023-03-09 17:08 WAT)

- URL: https://x.com/kevin_mizu/status/1633862447302860801
- Metrics (at fetch): bookmark 63, impression 28034, like 225, quote 2, reply 5, retweet 65

> Last month, I did some research on NodeJS templating libraries. During this research, I found an interesting Server Side Prototype Pollution gadget inside EJS library that can be leveraged to RCE!
>
> Technical details here: https://t.co/Bra3kinYb6


### Thread part 2 — @kevin_mizu — 2023-03-11 15:15 UTC (2023-03-11 16:15 WAT)

- URL: https://x.com/kevin_mizu/status/1634573754658353153
- Metrics (at fetch): bookmark 1, impression 702, like 9, quote 0, reply 1, retweet 2

> I'm really sorry, but it seems that someone found it before me...
>
> He made a more complete article on his research, you can read it here:
> https://t.co/8L1G021Bwx


### Thread part 3 — @kevin_mizu — 2023-03-11 16:43 UTC (2023-03-11 17:43 WAT)

- URL: https://x.com/kevin_mizu/status/1634595802675916803
- Metrics (at fetch): bookmark 0, impression 514, like 1, quote 0, reply 0, retweet 0

> https://t.co/DtdR17uCAo

**Quoted post (full text):**

    #### Quoted post — @1074912314 — 2021-12-15 16:00 UTC (2021-12-15 17:00 WAT)
    
    - URL: https://x.com/1074912314/status/1471148042577350659
    - Metrics (at fetch): bookmark 11, impression 0, like 168, quote 3, reply 6, retweet 28
    
    > Can you spot the vulnerability? #codeadvent2021 #typescript
    >
    > Why is this code dangerous? Bonus points if you can describe exactly how to exploit this! https://t.co/TbJj0A4o8Q
    
    **Media:**
    - media `3_1465674818980913160` (details not returned by the API)
    


---

## 2022-12-14 · Post · Yesterday, I did a talk on @rootme_org about electron security. In this talk I also presented a ste


Tags (automatic): XSS, RCE


### Post — @kevin_mizu — 2022-12-14 16:57 UTC (2022-12-14 17:57 WAT)

- URL: https://x.com/kevin_mizu/status/1603071806776164355
- Metrics (at fetch): bookmark 29, impression 0, like 95, quote 1, reply 2, retweet 38

> Yesterday, I did a talk on @rootme_org about #electron security. In this talk I also presented a step-by-step writeup of the research leading to finding the XSS to RCE vulnerability on @drawio last summer (CVE-2022-3133) ☀️
>
> You can find the slides here: https://t.co/XHlYtUFG7Z


---

## 2022-10-25 · Post · Last week, I created 3 web challenges for the 10kCTF organised by @rootme_org. 🚩


Tags (automatic): SQL injection


### Post — @kevin_mizu — 2022-10-25 14:56 UTC (2022-10-25 15:56 WAT)

- URL: https://x.com/kevin_mizu/status/1584921942578151425
- Metrics (at fetch): bookmark 3, impression 0, like 37, quote 1, reply 2, retweet 5

> Last week, I created 3 web challenges for the #10kCTF organised by @rootme_org. 🚩
>
> They were about: URL parsing confusion, SQLi in prepared query and HTML sanitizer bypass!
>
> You can find the writeups here: https://t.co/8aFUds3TQI


---

## 2022-08-30 · Post · This week, I solved an interesting challenge made by @0xItarow at @_barbhack_ 🌞


### Post — @kevin_mizu — 2022-08-30 15:52 UTC (2022-08-30 16:52 WAT)

- URL: https://x.com/kevin_mizu/status/1564642151870480385
- Metrics (at fetch): bookmark 2, impression 0, like 45, quote 0, reply 1, retweet 20

> This week, I solved an interesting challenge made by @0xItarow at @_barbhack_ 🌞
> It was about RPO abuse on a file upload feature!
>
> You can find the writeup here: https://t.co/5lseja2CJr 🎉


---

## 2021-09-11 · Post · Hello👋


### Post — @kevin_mizu — 2021-09-11 10:14 UTC (2021-09-11 11:14 WAT)

- URL: https://x.com/kevin_mizu/status/1436634166226038787
- Metrics (at fetch): not returned

> Hello👋
>
> Pendant le CTF web de l'@EuCyberCup, avec @Ooggule et @FeelProud_sec, nous avons obtenu le flag du 2ème challenge "Panid" d'une manière non attendue, vous pouvez retrouver le writeup ici :
> https://mizu.re/post/Panid_EC2_2021
>
> PS: Merci à l'admin pour le flag :)

**Links in post:** https://mizu.re/post/Panid_EC2_2021
