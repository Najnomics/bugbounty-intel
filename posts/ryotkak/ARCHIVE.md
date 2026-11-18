# @ryotkak — full verbatim X archive (security-relevant posts)

_Generated 2026-11-18 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 200
- Conversations/threads: 133
- Oldest post captured: 2019-05-29
- Newest post captured: 2026-07-30


---

## 2026-07-30 · Reply · @0xacb @flatt_security Yeah, I need to get some decent sleep now... :P


### Post — @ryotkak — 2026-07-30 03:03 UTC (2026-07-30 04:03 WAT)

- URL: https://x.com/ryotkak/status/2082663441710649826
- Metrics (at fetch): bookmark 0, impression 284, like 2, quote 0, reply 0, retweet 0

> @0xacb @flatt_security Yeah, I need to get some decent sleep now... :P


---

## 2026-07-30 · Reply · @0xacb @flatt_security Thank you so much for all your help coordinating the disclosure! You guys are


**Context — conversation root by another account:**

#### Root post — @0xacb — 2026-07-29 15:13 UTC (2026-07-29 16:13 WAT)

- URL: https://x.com/0xacb/status/2082484609820823929
- Metrics (at fetch): bookmark 192, impression 91215, like 388, quote 10, reply 13, retweet 99

> 🚨We reported KindaRails2Shell, a critical RCE in Ruby on Rails via Active Storage.
>
> It’s not a one-shot RCE, but the preconditions are kinda common under default configurations.
>
> Patch your applications now!
>
> https://t.co/Cj9XDk3qTN


### Post — @ryotkak — 2026-07-30 00:33 UTC (2026-07-30 01:33 WAT)

- URL: https://x.com/ryotkak/status/2082625697294807330
- Metrics (at fetch): bookmark 0, impression 343, like 2, quote 0, reply 1, retweet 0

> @0xacb @flatt_security Thank you so much for all your help coordinating the disclosure! You guys are awesome ;)


---

## 2026-07-29 · Post · Ruby on Railsに深刻な脆弱性を報告し、先程修正バージョンが公開されました。一般的な構成において、任意コード実行に繋がるものです。


### Post — @ryotkak — 2026-07-29 15:13 UTC (2026-07-29 16:13 WAT)

- URL: https://x.com/ryotkak/status/2082484740494684250
- Metrics (at fetch): bookmark 74, impression 99776, like 471, quote 4, reply 3, retweet 129

> Ruby on Railsに深刻な脆弱性を報告し、先程修正バージョンが公開されました。一般的な構成において、任意コード実行に繋がるものです。
>
> 7.2.3.2、8.0.5.1及び8.1.3.1において修正されているため、速やかな更新を推奨いたします。
>
> CVE IDはCVE-2026-66066となります。
>
> https://x.com/flatt_security/status/2082484516279775264?s=46 https://twitter.com/flatt_security/status/2082484516279775264

**Links in post:** https://x.com/flatt_security/status/2082484516279775264?s=46, https://twitter.com/flatt_security/status/2082484516279775264

**Quoted post (full text):**

    #### Quoted post — @1073849003618365440 — 2026-07-29 15:12 UTC (2026-07-29 16:12 WAT)
    
    - URL: https://x.com/1073849003618365440/status/2082484516279775264
    - Metrics (at fetch): bookmark 223, impression 476304, like 642, quote 41, reply 2, repost 297
    
    > Ruby on Rails の深刻度「緊急」脆弱性が先ほど開示されました。弊社研究者 RyotaK @ryotkak を含むチームにより発見されたもので、一般的な構成において、リモートからの任意コード実行が可能です。
    >
    > 緊急度が高く、速やかな更新を推奨いたします。
    >
    > ▼ ほか詳細
    > https://blog.flatt.tech/entry/kindarails2shell_rails
    
    **Links in post:** https://blog.flatt.tech/entry/kindarails2shell_rails
    


---

## 2026-07-17 · Thread · 【注意】WordPress本体において、未認証で任意コード実行に繋がる脆弱性が修正されています。


Tags (automatic): SQL injection


### Post — @ryotkak — 2026-07-17 23:17 UTC (2026-07-18 00:17 WAT)

- URL: https://x.com/ryotkak/status/2078257717983236594
- Metrics (at fetch): bookmark 76, impression 36742, like 225, quote 1, reply 3, retweet 62

> 【注意】WordPress本体において、未認証で任意コード実行に繋がる脆弱性が修正されています。
>
> 影響を受けるWordPressのバージョンは以下のとおりです。
> - 6.9.0-6.9.4
> - 7.0.0-7.0.1
>
> 未検証ながら、PoCの存在も確認しているため、パッチの適用を速やかに実施することを推奨いたします。


### Thread part 2 — @ryotkak — 2026-07-17 23:19 UTC (2026-07-18 00:19 WAT)

- URL: https://x.com/ryotkak/status/2078258325645603258
- Metrics (at fetch): bookmark 13, impression 7878, like 33, quote 0, reply 1, retweet 9

> なお、本脆弱性を成立させるために使用されたSQL Injectionは6.8.0-6.8.5にも存在するようです。
>
> 詳細な情報は、発見者による以下の投稿をご参照ください。
>
> https://t.co/rtUcB5xPKY


### Thread part 3 — @ryotkak — 2026-07-18 13:13 UTC (2026-07-18 14:13 WAT)

- URL: https://x.com/ryotkak/status/2078468092766859302
- Metrics (at fetch): bookmark 28, impression 19340, like 67, quote 1, reply 0, retweet 20

> WordPressの任意コード実行について、概要をまとめた記事を公開しました。
>
> 社内において、完全にデフォルトの設定を用いて未認証の第三者が管理者権限を奪取可能であることを確認しているため、依然としてアップデートしていない方は即座の更新を推奨いたします。 https://t.co/SVh1F0iHKl

**Quoted post** 2078466304571543859: not readable via the API (deleted, private, or withheld).


---

## 2026-07-18 · Reply · @adnanthekhan Thank you for the info! Will validate them once I get back home


### Post — @ryotkak — 2026-07-18 00:07 UTC (2026-07-18 01:07 WAT)

- URL: https://x.com/ryotkak/status/2078270504939454752
- Metrics (at fetch): bookmark 1, impression 1085, like 1, quote 0, reply 0, retweet 0

> @adnanthekhan Thank you for the info! Will validate them once I get back home


---

## 2026-06-03 · Reply · @seanyeoh Thank you! Yeah, the architecture of GitHub Actions has been problematic since its launch.


### Post — @ryotkak — 2026-06-03 03:08 UTC (2026-06-03 04:08 WAT)

- URL: https://x.com/ryotkak/status/2062008384870813843
- Metrics (at fetch): bookmark 1, impression 562, like 1, quote 0, reply 0, retweet 0

> @seanyeoh Thank you! Yeah, the architecture of GitHub Actions has been problematic since its launch...


---

## 2026-06-02 · Reply · @0xLupin Thank you for reading it ;)


Tags (automatic): AI-assisted hunting


### Post — @ryotkak — 2026-06-02 09:10 UTC (2026-06-02 10:10 WAT)

- URL: https://x.com/ryotkak/status/2061737097107824994
- Metrics (at fetch): bookmark 0, impression 812, like 5, quote 0, reply 1, retweet 0

> @0xLupin Thank you for reading it ;)
>
> I believe we need something like an IBB but for SSC attacks, to reward good-faith researchers. However, given how bug bounties are currently being affected by AI, I'm not sure this is even feasible...


---

## 2026-06-01 · Post · Claude Codeに対してサプライチェーン攻撃を行うことが可能だった脆弱性についての記事を公開しました！ https://twitter.com/flatt_security/status/206


Tags (automatic): AI-assisted hunting


### Post — @ryotkak — 2026-06-01 13:09 UTC (2026-06-01 14:09 WAT)

- URL: https://x.com/ryotkak/status/2061434879309664575
- Metrics (at fetch): bookmark 71, impression 42174, like 240, quote 2, reply 10, retweet 24

> Claude Codeに対してサプライチェーン攻撃を行うことが可能だった脆弱性についての記事を公開しました！ https://twitter.com/flatt_security/status/2061434446390468913

**Links in post:** https://twitter.com/flatt_security/status/2061434446390468913

**Quoted post (full text):**

    #### Quoted post — @1073849003618365440 — 2026-06-01 13:07 UTC (2026-06-01 14:07 WAT)
    
    - URL: https://x.com/1073849003618365440/status/2061434446390468913
    - Metrics (at fetch): bookmark 73, impression 49895, like 109, quote 4, reply 0, repost 32
    
    > セキュリティリサーチャー RyotaK @ryotkak の技術ブログを公開しました。
    >
    > 今回、Claude Code GitHub Actions の権限制御を外部の GitHub Issue 経由でバイパスし、ワークフロー権限を悪用できる脆弱性、並びにそれに付随する設定ミスを発見・報告しました。
    >
    > 当該の脆弱性は v1.0.94 で修正済みですが、設定ミスについては各リポジトリにて対応が必要であるため、当該製品を利用されている場合は設定の見直しと実行ログの確認を推奨します。
    >
    > https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/
    
    **Links in post:** https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/
    


---

## 2026-06-01 · Post · I've published an article on how an attacker could break into the Claude Code supply chain! https://


Tags (automatic): Dependency confusion / supply chain, AI-assisted hunting


### Post — @ryotkak — 2026-06-01 13:04 UTC (2026-06-01 14:04 WAT)

- URL: https://x.com/ryotkak/status/2061433680443396273
- Metrics (at fetch): bookmark 13, impression 15917, like 53, quote 0, reply 4, retweet 7

> I've published an article on how an attacker could break into the Claude Code supply chain! https://t.co/cNkqnkq357

**Quoted post** 2061433196563386537: not readable via the API (deleted, private, or withheld).


---

## 2026-05-08 · Thread · Does anyone have a direct contact at @thezdi? I've been trying to register my Pwn2Own entries for th


Tags (automatic): Memory corruption / native


### Post — @ryotkak — 2026-05-08 22:41 UTC (2026-05-08 23:41 WAT)

- URL: https://x.com/ryotkak/status/2052881664909660521
- Metrics (at fetch): bookmark 16, impression 37810, like 124, quote 3, reply 8, retweet 5

> Does anyone have a direct contact at @thezdi? I've been trying to register my Pwn2Own entries for the past 3 weeks but still haven't received a clear response. I'll have to cancel my flight and hotel by May 10th if my entries aren't confirmed.


### Thread part 2 — @ryotkak — 2026-05-10 01:36 UTC (2026-05-10 02:36 WAT)

- URL: https://x.com/ryotkak/status/2053288150756450485
- Metrics (at fetch): bookmark 0, impression 4726, like 12, quote 0, reply 1, retweet 0

> I haven't received a response yet. Could someone from ZDI please reach out to me? Even an unofficial confirmation of whether I can participate would help me decide whether to cancel my bookings.


### Thread part 3 — @ryotkak — 2026-05-10 14:29 UTC (2026-05-10 15:29 WAT)

- URL: https://x.com/ryotkak/status/2053482472453849456
- Metrics (at fetch): bookmark 3, impression 10273, like 40, quote 2, reply 5, retweet 3

> Update: ZDI told me that they are at maximum capacity and can't add extra contest days.
>
> For other Pwn2Own contestants, I believe that if you haven't received confirmation yet, you won't be able to participate. Therefore, I recommend reporting the vulnerability directly.


### Thread part 4 — @ryotkak — 2026-05-10 14:29 UTC (2026-05-10 15:29 WAT)

- URL: https://x.com/ryotkak/status/2053482513293828375
- Metrics (at fetch): bookmark 0, impression 7784, like 12, quote 0, reply 1, retweet 0

> If you've successfully received confirmation from ZDI and are participating in Pwn2Own, I expect you'll see many collisions with the rejected contestants. Therefore, I'd recommend demonstrating the most unique exploit chain if you have multiple candidate vulnerabilities.


### Thread part 5 — @ryotkak — 2026-05-10 14:30 UTC (2026-05-10 15:30 WAT)

- URL: https://x.com/ryotkak/status/2053482857671303564
- Metrics (at fetch): bookmark 0, impression 6740, like 9, quote 0, reply 0, retweet 0

> Thank you so much to everyone who tried to reach out to ZDI. At the very least, I was able to save some of the cancellation fee!


---

## 2026-05-09 · Reply · @Chackal__ @eeyitemi i had to plan it as it would be 15+ hours flight for me sadly :/ i'm packing my


### Post — @ryotkak — 2026-05-09 22:02 UTC (2026-05-09 23:02 WAT)

- URL: https://x.com/ryotkak/status/2053234085158617318
- Metrics (at fetch): bookmark 0, impression 716, like 3, quote 0, reply 1, retweet 0

> @Chackal__ @eeyitemi i had to plan it as it would be 15+ hours flight for me sadly :/ i'm packing my suitcase currently in case they decide to allow my entries


---

## 2026-05-09 · Reply · @eeyitemi did you receive a response from them recently? I really need to confirm whether I should c


### Post — @ryotkak — 2026-05-09 21:23 UTC (2026-05-09 22:23 WAT)

- URL: https://x.com/ryotkak/status/2053224398220615944
- Metrics (at fetch): bookmark 1, impression 3407, like 5, quote 0, reply 1, retweet 0

> @eeyitemi did you receive a response from them recently? I really need to confirm whether I should cancel my booking to Berlin...


---

## 2026-05-09 · Reply · @TWO_XIE I sent an initial registration proposal to their email three weeks ago, but they had receiv


### Post — @ryotkak — 2026-05-09 21:17 UTC (2026-05-09 22:17 WAT)

- URL: https://x.com/ryotkak/status/2053222760974020690
- Metrics (at fetch): bookmark 0, impression 1187, like 0, quote 0, reply 1, retweet 0

> @TWO_XIE I sent an initial registration proposal to their email three weeks ago, but they had received a high volume of submissions, which caused a delay in communication, so unfortunately we couldn't move forward :/


---

## 2026-05-09 · Reply · @vectors2final @TheGrandPew @S1r1u5_ @thezdi thank you so much! please let me know once you've sent 


### Post — @ryotkak — 2026-05-09 11:35 UTC (2026-05-09 12:35 WAT)

- URL: https://x.com/ryotkak/status/2053076281470960025
- Metrics (at fetch): bookmark 0, impression 337, like 0, quote 0, reply 0, retweet 0

> @vectors2final @TheGrandPew @S1r1u5_ @thezdi thank you so much! please let me know once you've sent the message ;)


---

## 2026-05-08 · Reply · @v_metnew @thezdi we need at least a clear rejection...


### Post — @ryotkak — 2026-05-08 23:08 UTC (2026-05-09 00:08 WAT)

- URL: https://x.com/ryotkak/status/2052888321060397203
- Metrics (at fetch): bookmark 0, impression 2902, like 5, quote 0, reply 1, retweet 0

> @v_metnew @thezdi we need at least a clear rejection...


---

## 2026-03-24 · Reply · @Akhmad_Yudha @flatt_sec_en Thank you! I'll fix it!


### Post — @ryotkak — 2026-03-24 00:37 UTC (2026-03-24 01:37 WAT)

- URL: https://x.com/ryotkak/status/2036240906681200820
- Metrics (at fetch): bookmark 0, impression 170, like 1, quote 0, reply 0, retweet 0

> @Akhmad_Yudha @flatt_sec_en Thank you! I'll fix it!


---

## 2026-03-24 · Reply · @TWO_XIE thanks!


### Post — @ryotkak — 2026-03-24 00:36 UTC (2026-03-24 01:36 WAT)

- URL: https://x.com/ryotkak/status/2036240625687994490
- Metrics (at fetch): bookmark 0, impression 322, like 0, quote 0, reply 0, retweet 0

> @TWO_XIE thanks!


---

## 2026-03-24 · Reply · @sudhanshur705 Thank you for reading 🔥


### Post — @ryotkak — 2026-03-24 00:36 UTC (2026-03-24 01:36 WAT)

- URL: https://x.com/ryotkak/status/2036240582390194532
- Metrics (at fetch): bookmark 0, impression 450, like 1, quote 0, reply 0, retweet 0

> @sudhanshur705 Thank you for reading 🔥


---

## 2026-03-24 · Reply · @0xAsm0d3us thank you!


### Post — @ryotkak — 2026-03-24 00:35 UTC (2026-03-24 01:35 WAT)

- URL: https://x.com/ryotkak/status/2036240515012895157
- Metrics (at fetch): bookmark 0, impression 421, like 1, quote 0, reply 0, retweet 0

> @0xAsm0d3us thank you!


---

## 2026-03-23 · Post · I've published a writeup on a vulnerability I found in Google Cloud Looker: a single directory delet


Tags (automatic): RCE


### Post — @ryotkak — 2026-03-23 14:31 UTC (2026-03-23 15:31 WAT)

- URL: https://x.com/ryotkak/status/2036088432121065574
- Metrics (at fetch): bookmark 102, impression 34876, like 229, quote 0, reply 6, retweet 37

> I've published a writeup on a vulnerability I found in Google Cloud Looker: a single directory deletion bug that led to RCE and cross-instance privilege escalation in k8s. https://twitter.com/flatt_sec_en/status/2036087956898021411

**Links in post:** https://twitter.com/flatt_sec_en/status/2036087956898021411

**Quoted post** 2036087956898021411: not readable via the API (deleted, private, or withheld).


---

## 2026-01-26 · Post · Another vulnerability in React Server Components (CVE-2026-23864) that I reported was disclosed toda


### Post — @ryotkak — 2026-01-26 23:25 UTC (2026-01-27 00:25 WAT)

- URL: https://x.com/ryotkak/status/2015929125631099284
- Metrics (at fetch): bookmark 512, impression 346365, like 1783, quote 125, reply 75, retweet 229

> Another vulnerability in React Server Components (CVE-2026-23864) that I reported was disclosed today.
>
> This is separate from the one disclosed in December, so you'll need to update again.
>
> https://vercel.com/changelog/summary-of-cve-2026-23864

**Links in post:** https://vercel.com/changelog/summary-of-cve-2026-23864


---

## 2026-01-26 · Post · React Server Componentsに報告していた別の脆弱性 (CVE-2026-23864) が修正されました。


### Post — @ryotkak — 2026-01-26 23:24 UTC (2026-01-27 00:24 WAT)

- URL: https://x.com/ryotkak/status/2015928771644395699
- Metrics (at fetch): bookmark 99, impression 48221, like 380, quote 2, reply 1, retweet 96

> React Server Componentsに報告していた別の脆弱性 (CVE-2026-23864) が修正されました。
>
> 昨年12月に修正された脆弱性とは別の脆弱性であるため、再度アップデートを実施してください。
>
> https://vercel.com/changelog/summary-of-cve-2026-23864

**Links in post:** https://vercel.com/changelog/summary-of-cve-2026-23864


---

## 2026-01-14 · Thread · 本日公開されたNode.js側のセキュリティリリースはReact / Next.js等、特定の条件を満たすフレームワークにデフォルトで影響するDoSの脆弱性修正を含みます。


### Post — @ryotkak — 2026-01-14 01:00 UTC (2026-01-14 02:00 WAT)

- URL: https://x.com/ryotkak/status/2011242089133273575
- Metrics (at fetch): bookmark 16, impression 21165, like 70, quote 0, reply 1, retweet 9

> 本日公開されたNode.js側のセキュリティリリースはReact / Next.js等、特定の条件を満たすフレームワークにデフォルトで影響するDoSの脆弱性修正を含みます。
> React2Shell対応の際にフレームワーク更新している場合でも、Node.jsランタイムの更新が必要となりますので、影響範囲を再度ご確認ください。 https://t.co/X4RNDjQusa

**Quoted post** 2011137343323865196: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @ryotkak — 2026-01-14 01:03 UTC (2026-01-14 02:03 WAT)

- URL: https://x.com/ryotkak/status/2011242634568950108
- Metrics (at fetch): bookmark 1, impression 6087, like 4, quote 0, reply 0, retweet 0

> 詳細についてはNode.js公式のセキュリティアドバイザリをご確認ください。
> (なお、本件について報告をしたのは私ではなく、別の方となります。)
> https://t.co/JGSSzEQ0Nb


---

## 2026-01-12 · Post · I wrote an article about 8 vulnerabilities in Claude Code that allowed me to bypass the permission m


Tags (automatic): AI-assisted hunting


### Post — @ryotkak — 2026-01-12 17:10 UTC (2026-01-12 18:10 WAT)

- URL: https://x.com/ryotkak/status/2010761406002627018
- Metrics (at fetch): bookmark 78, impression 28954, like 251, quote 0, reply 7, retweet 32

> I wrote an article about 8 vulnerabilities in Claude Code that allowed me to bypass the permission model and execute arbitrary commands! https://t.co/xi9EqlrMZT

**Quoted post** 2010715968188862629: not readable via the API (deleted, private, or withheld).


---

## 2025-12-12 · Thread · Note: this vulnerability affects Next.js 13.x or 14.x, which CVE-2025-55182 (React2Shell) didn't aff


### Post — @ryotkak — 2025-12-12 04:18 UTC (2025-12-12 05:18 WAT)

- URL: https://x.com/ryotkak/status/1999332971447484593
- Metrics (at fetch): bookmark 24, impression 20398, like 95, quote 1, reply 4, retweet 12

> Note: this vulnerability affects Next.js 13.x or 14.x, which CVE-2025-55182 (React2Shell) didn't affect, so I recommend to re-investigate the impacted assets again. https://t.co/WeiL6NkXwA

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2025-12-11 22:18 UTC (2025-12-11 23:18 WAT)
    
    - URL: https://x.com/ryotkak/status/1999242366776164450
    - Metrics (at fetch): bookmark 53, impression 88027, like 412, quote 5, reply 11, retweet 35
    
    > I reported another vulnerability to React Server Components.
    >
    > Please note that while it still requires you to update, this one doesn't allow remote code execution. https://t.co/h5ZVqrWtK3
    
    **Quoted post (full text):**
    
        #### Quoted post — @1566463268 — 2025-12-11 20:38 UTC (2025-12-11 21:38 WAT)
        
        - URL: https://x.com/1566463268/status/1999217365628903739
        - Metrics (at fetch): bookmark 1460, impression 3260807, like 6241, quote 1446, reply 384, retweet 1170
        
        > Researchers have found two new vulnerabilities in React Server Components while attempting to exploit the patches last week.
        >
        > These are new issues, separate from the critical CVE last week. The patch for React2Shell remains effective for the Remote Code Execution exploit.
        
    


### Thread part 2 — @ryotkak — 2025-12-12 07:49 UTC (2025-12-12 08:49 WAT)

- URL: https://x.com/ryotkak/status/1999386202533929399
- Metrics (at fetch): bookmark 4, impression 5706, like 12, quote 0, reply 1, retweet 0

> Please refer to Vercel's advisory for more details on which Next.js versions are affected:
> https://t.co/89qjR3yp3e


---

## 2025-12-12 · Thread · なお、本脆弱性は CVE-2025-55182 (React2Shell) において影響を受けなかったNext.js 13.xや14.x等も影響を受けるため、再度影響範囲の評価を実施することを推奨いた


### Post — @ryotkak — 2025-12-12 04:15 UTC (2025-12-12 05:15 WAT)

- URL: https://x.com/ryotkak/status/1999332319908524236
- Metrics (at fetch): bookmark 62, impression 63289, like 322, quote 8, reply 1, retweet 92

> なお、本脆弱性は CVE-2025-55182 (React2Shell) において影響を受けなかったNext.js 13.xや14.x等も影響を受けるため、再度影響範囲の評価を実施することを推奨いたします。
>
> https://t.co/UaBLBCAWMZ

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2025-12-11 22:20 UTC (2025-12-11 23:20 WAT)
    
    - URL: https://x.com/ryotkak/status/1999242821640094115
    - Metrics (at fetch): bookmark 79, impression 143527, like 509, quote 3, reply 1, retweet 111
    
    > React Server Componentsに別の脆弱性を報告しました。
    >
    > 依然として影響を受ける依存関係をアップデートする必要はありますが、今回の脆弱性は任意コード実行には繋がらないことに留意してください。 https://t.co/h5ZVqrWtK3
    
    **Quoted post (full text):**
    
        #### Quoted post — @1566463268 — 2025-12-11 20:38 UTC (2025-12-11 21:38 WAT)
        
        - URL: https://x.com/1566463268/status/1999217365628903739
        - Metrics (at fetch): bookmark 1460, impression 3260807, like 6241, quote 1446, reply 384, retweet 1170
        
        > Researchers have found two new vulnerabilities in React Server Components while attempting to exploit the patches last week.
        >
        > These are new issues, separate from the critical CVE last week. The patch for React2Shell remains effective for the Remote Code Execution exploit.
        
    


### Thread part 2 — @ryotkak — 2025-12-12 07:49 UTC (2025-12-12 08:49 WAT)

- URL: https://x.com/ryotkak/status/1999386043980873881
- Metrics (at fetch): bookmark 3, impression 5143, like 5, quote 0, reply 0, retweet 0

> 影響を受けるNext.jsバージョンの詳細については、Vercelの公式アドバイザリをご確認ください。
> https://t.co/89qjR3yp3e


---

## 2025-12-11 · Thread · React Server Componentsに別の脆弱性を報告しました。


### Post — @ryotkak — 2025-12-11 22:20 UTC (2025-12-11 23:20 WAT)

- URL: https://x.com/ryotkak/status/1999242821640094115
- Metrics (at fetch): bookmark 79, impression 143527, like 509, quote 3, reply 1, retweet 111

> React Server Componentsに別の脆弱性を報告しました。
>
> 依然として影響を受ける依存関係をアップデートする必要はありますが、今回の脆弱性は任意コード実行には繋がらないことに留意してください。 https://t.co/h5ZVqrWtK3

**Quoted post (full text):**

    #### Quoted post — @1566463268 — 2025-12-11 20:38 UTC (2025-12-11 21:38 WAT)
    
    - URL: https://x.com/1566463268/status/1999217365628903739
    - Metrics (at fetch): bookmark 1460, impression 3260807, like 6241, quote 1446, reply 384, retweet 1170
    
    > Researchers have found two new vulnerabilities in React Server Components while attempting to exploit the patches last week.
    >
    > These are new issues, separate from the critical CVE last week. The patch for React2Shell remains effective for the Remote Code Execution exploit.
    


### Thread part 2 — @ryotkak — 2025-12-11 22:20 UTC (2025-12-11 23:20 WAT)

- URL: https://x.com/ryotkak/status/1999242963839566103
- Metrics (at fetch): bookmark 7, impression 9698, like 33, quote 0, reply 0, retweet 9

> 脆弱性の詳細情報については公式ブログをご覧ください:
>
> https://t.co/4VCxwpIAyp


---

## 2025-12-11 · Thread · I reported another vulnerability to React Server Components.


Tags (automatic): RCE


### Post — @ryotkak — 2025-12-11 22:18 UTC (2025-12-11 23:18 WAT)

- URL: https://x.com/ryotkak/status/1999242366776164450
- Metrics (at fetch): bookmark 53, impression 88027, like 412, quote 5, reply 11, retweet 35

> I reported another vulnerability to React Server Components.
>
> Please note that while it still requires you to update, this one doesn't allow remote code execution. https://t.co/h5ZVqrWtK3

**Quoted post (full text):**

    #### Quoted post — @1566463268 — 2025-12-11 20:38 UTC (2025-12-11 21:38 WAT)
    
    - URL: https://x.com/1566463268/status/1999217365628903739
    - Metrics (at fetch): bookmark 1460, impression 3260807, like 6241, quote 1446, reply 384, retweet 1170
    
    > Researchers have found two new vulnerabilities in React Server Components while attempting to exploit the patches last week.
    >
    > These are new issues, separate from the critical CVE last week. The patch for React2Shell remains effective for the Remote Code Execution exploit.
    


### Thread part 2 — @ryotkak — 2025-12-11 22:19 UTC (2025-12-11 23:19 WAT)

- URL: https://x.com/ryotkak/status/1999242547416433006
- Metrics (at fetch): bookmark 9, impression 7350, like 19, quote 0, reply 0, retweet 1

> Please refer to the official information for the details of this vulnerability:
>
> https://t.co/4VCxwpIAyp


---

## 2025-11-27 · Post · JPCERTコーディネーションセンター様より、脆弱性報告部門においてベストレポーター賞をいただきました！ https://twitter.com/jpcert/status/1993933857788


### Post — @ryotkak — 2025-11-27 13:05 UTC (2025-11-27 14:05 WAT)

- URL: https://x.com/ryotkak/status/1994029912236401141
- Metrics (at fetch): bookmark 4, impression 15956, like 129, quote 2, reply 2, retweet 5

> JPCERTコーディネーションセンター様より、脆弱性報告部門においてベストレポーター賞をいただきました！ https://twitter.com/jpcert/status/1993933857788514341

**Links in post:** https://twitter.com/jpcert/status/1993933857788514341

**Quoted post** 1993933857788514341: not readable via the API (deleted, private, or withheld).


---

## 2025-10-03 · Thread · I reported an arbitrary code execution in Unity Runtime, which affects all versions starting from Un


Tags (automatic): RCE


### Post — @ryotkak — 2025-10-03 04:20 UTC (2025-10-03 05:20 WAT)

- URL: https://x.com/ryotkak/status/1973966245298163796
- Metrics (at fetch): bookmark 103, impression 216412, like 432, quote 19, reply 15, retweet 117

> I reported an arbitrary code execution in Unity Runtime, which affects all versions starting from Unity 2017.1. 
>
> As the vulnerability can be exploited without specific usage, I strongly encourage developers to patch.
>
> Technical details below:
> https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/

**Links in post:** https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/


### Thread part 2 — @ryotkak — 2025-10-03 13:14 UTC (2025-10-03 14:14 WAT)

- URL: https://x.com/ryotkak/status/1974100695193411713
- Metrics (at fetch): bookmark 3, impression 10329, like 21, quote 0, reply 0, retweet 0

> Note: The vulnerability exists in the runtime and isn't expected to affect projects with artifacts that don't use the runtime (e.g., VRChat avatars).
>
> I didn't investigate specific cases, so please use this information only as a reference when assessing the impact on your project


---

## 2025-10-03 · Thread · Unityのランタイムに任意コード実行の脆弱性を報告しました。


### Post — @ryotkak — 2025-10-03 04:22 UTC (2025-10-03 05:22 WAT)

- URL: https://x.com/ryotkak/status/1973966902709141997
- Metrics (at fetch): bookmark 145, impression 173287, like 782, quote 26, reply 6, retweet 340

> Unityのランタイムに任意コード実行の脆弱性を報告しました。
> Unity 2017.1以降の全てのバージョンに影響し、プラットフォームによってはデフォルトの構成で影響を受けるため、即座の更新を推奨いたします。
>
> https://x.com/ryotkak/status/1973966245298163796

**Links in post:** https://x.com/ryotkak/status/1973966245298163796

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2025-10-03 04:20 UTC (2025-10-03 05:20 WAT)
    
    - URL: https://x.com/ryotkak/status/1973966245298163796
    - Metrics (at fetch): bookmark 103, impression 216412, like 432, quote 19, reply 15, retweet 117
    
    > I reported an arbitrary code execution in Unity Runtime, which affects all versions starting from Unity 2017.1. 
    >
    > As the vulnerability can be exploited without specific usage, I strongly encourage developers to patch.
    >
    > Technical details below:
    > https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/
    
    **Links in post:** https://flatt.tech/research/posts/arbitrary-code-execution-in-unity-runtime/
    


### Thread part 2 — @ryotkak — 2025-10-03 13:08 UTC (2025-10-03 14:08 WAT)

- URL: https://x.com/ryotkak/status/1974099262544990503
- Metrics (at fetch): bookmark 1, impression 14087, like 62, quote 3, reply 0, retweet 35

> 補足: 本脆弱性はUnityのランタイムに存在するものであり、成果物がUnityのランタイムを使用しないプロジェクト (例: VRChatのアバターなど) については影響を受けないものと考えられます。
>
> (個別事例について確認したわけではございませんので、あくまで影響調査の際の参考情報としてご利用ください)


---

## 2025-08-27 · Post · Metaのバグバウンティイベントで優勝しました！


### Post — @ryotkak — 2025-08-27 03:24 UTC (2025-08-27 04:24 WAT)

- URL: https://x.com/ryotkak/status/1960544017525170262
- Metrics (at fetch): bookmark 11, impression 33618, like 271, quote 2, reply 2, retweet 30

> Metaのバグバウンティイベントで優勝しました！
> https://x.com/flatt_security/status/1960542482510569738

**Links in post:** https://x.com/flatt_security/status/1960542482510569738

**Quoted post** 1960542482510569738: not readable via the API (deleted, private, or withheld).


---

## 2025-05-18 · Post · Got the Most Impact award at the Meta's Bug Bounty Researcher Conference in Tokyo!


### Post — @ryotkak — 2025-05-18 14:08 UTC (2025-05-18 15:08 WAT)

- URL: https://x.com/ryotkak/status/1924104690150891590
- Metrics (at fetch): bookmark 13, impression 29051, like 219, quote 2, reply 10, retweet 13

> Got the Most Impact award at the Meta's Bug Bounty Researcher Conference in Tokyo!
>
> Thank you so much @metabugbounty team and everyone who attended the event!
> #MBBRC2025 [pic.x.com/OsG9iXl8Wv]

**Media:**
- photo: https://pbs.twimg.com/media/GrPLBOpXsAAhqa9.jpg — no alt text provided by author


---

## 2025-03-05 · Thread · 🔔Challenge time!🔔


### Post — @ryotkak — 2025-03-05 14:53 UTC (2025-03-05 15:53 WAT)

- URL: https://x.com/ryotkak/status/1897299540598006249
- Metrics (at fetch): bookmark 34, impression 13151, like 73, quote 1, reply 1, retweet 15

> 🔔Challenge time!🔔
>
> I published one of my challenges from the SECCON CTF 13 Finals with a fix for the unintended solution! The goal for this challenge is to access the admin dashboard and get the flag.
>
> Can you solve it?
>
> https://not-that-short.pages.dev/ [pic.x.com/RqM6YUUc0o]

**Media:**
- photo: https://pbs.twimg.com/media/GlSPyNcb0AEN1gb.jpg — no alt text provided by author

**Links in post:** https://not-that-short.pages.dev/


### Thread part 2 — @ryotkak — 2025-03-22 05:08 UTC (2025-03-22 06:08 WAT)

- URL: https://x.com/ryotkak/status/1903312716263284871
- Metrics (at fetch): bookmark 1, impression 5775, like 11, quote 0, reply 1, retweet 2

> .@frevadiscor89 has solved the challenge!
>
> As a hint, I've included the diff from the SECCON CTF 13 Finals version, which should give you an idea of where to start looking.
>
> I'm currently working on the author write-up for my challenges and plan to release it in a few weeks!


### Thread part 3 — @ryotkak — 2025-04-14 15:08 UTC (2025-04-14 16:08 WAT)

- URL: https://x.com/ryotkak/status/1911798665204940932
- Metrics (at fetch): bookmark 1, impression 5047, like 3, quote 0, reply 0, retweet 0

> @frevadiscor89 I've published the author's writeup. While the article is written in Japanese, I've tweaked the layout a bit to make it translator-friendly, so you should be able to read it without hassle.
> https://x.com/ryotkak/status/1911798191143747636

**Links in post:** https://x.com/ryotkak/status/1911798191143747636

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2025-04-14 15:06 UTC (2025-04-14 16:06 WAT)
    
    - URL: https://x.com/ryotkak/status/1911798191143747636
    - Metrics (at fetch): bookmark 22, impression 12334, like 101, quote 1, reply 0, retweet 18
    
    > SECCON CTF 13 Finalsで出題した「super-fastcgi」と「not-that-short」に関しての作問者Writeupを公開しました。
    > https://blog.ryotak.net/post/seccon-13-ctf-final-author-writeup/
    
    **Links in post:** https://blog.ryotak.net/post/seccon-13-ctf-final-author-writeup/
    


---

## 2025-04-14 · Post · SECCON CTF 13 Finalsで出題した「super-fastcgi」と「not-that-short」に関しての作問者Writeupを公開しました。


### Post — @ryotkak — 2025-04-14 15:06 UTC (2025-04-14 16:06 WAT)

- URL: https://x.com/ryotkak/status/1911798191143747636
- Metrics (at fetch): bookmark 22, impression 12334, like 101, quote 1, reply 0, retweet 18

> SECCON CTF 13 Finalsで出題した「super-fastcgi」と「not-that-short」に関しての作問者Writeupを公開しました。
> https://blog.ryotak.net/post/seccon-13-ctf-final-author-writeup/

**Links in post:** https://blog.ryotak.net/post/seccon-13-ctf-final-author-writeup/


---

## 2025-04-03 · Thread · I recently reported a vulnerability to Next.js, which is a partial bypass of the middleware authenti


Tags (automatic): Auth bypass, AI-assisted hunting


### Post — @ryotkak — 2025-04-03 02:25 UTC (2025-04-03 03:25 WAT)

- URL: https://x.com/ryotkak/status/1907620383597146616
- Metrics (at fetch): bookmark 36, impression 10554, like 125, quote 0, reply 1, retweet 12

> I recently reported a vulnerability to Next.js, which is a partial bypass of the middleware authentication bypass vulnerability (CVE-2025-29927) with Takumi (http://takumi-san.ai), an AI security engineer.

**Links in post:** http://takumi-san.ai


### Thread part 2 — @ryotkak — 2025-04-03 02:25 UTC (2025-04-03 03:25 WAT)

- URL: https://x.com/ryotkak/status/1907620385245507930
- Metrics (at fetch): bookmark 1, impression 4216, like 11, quote 0, reply 0, retweet 2

> However, the requirement for this vulnerability to be exploitable is unlikely, which fairly reduces its impact. If your Next.js application fetches a third-party website server-side, I recommend upgrading to the latest version!  https://github.com/vercel/next.js/security/advisories/GHSA-223j-4rm8-mrmf

**Links in post:** https://github.com/vercel/next.js/security/advisories/GHSA-223j-4rm8-mrmf


---

## 2025-03-15 · Post · P3NFEST 2025 Winterにて「コードから探す脆弱性」というテーマの発表をさせていただきました！


### Post — @ryotkak — 2025-03-15 10:19 UTC (2025-03-15 11:19 WAT)

- URL: https://x.com/ryotkak/status/1900854355244576982
- Metrics (at fetch): bookmark 43, impression 12190, like 137, quote 1, reply 1, retweet 31

> P3NFEST 2025 Winterにて「コードから探す脆弱性」というテーマの発表をさせていただきました！
> ご聴講いただいた皆様、ありがとうございました！
>
> 発表に使用したスライドは以下のページで公開しています
> https://ryotak.net/slides/?id=1
>
> #P3NFEST

**Links in post:** https://ryotak.net/slides/?id=1


---

## 2025-03-02 · Post · SECCON CTF 13 Finalsにご参加頂いた皆様、ありがとうございました！Webカテゴリのsuper-fastcgiとnot-that-shortを作問していました。


### Post — @ryotkak — 2025-03-02 14:01 UTC (2025-03-02 15:01 WAT)

- URL: https://x.com/ryotkak/status/1896199116998447269
- Metrics (at fetch): bookmark 0, impression 6372, like 70, quote 0, reply 0, retweet 3

> SECCON CTF 13 Finalsにご参加頂いた皆様、ありがとうございました！Webカテゴリのsuper-fastcgiとnot-that-shortを作問していました。
> not-that-shortについて、競技中に難易度が低下するミスを発見したため、リベンジとして来週中に修正版を公開する予定です。ぜひ奮ってご参加ください！ #SECCON


---

## 2025-02-10 · Post · 【お知らせ】


### Post — @ryotkak — 2025-02-10 12:44 UTC (2025-02-10 13:44 WAT)

- URL: https://x.com/ryotkak/status/1888931980064292896
- Metrics (at fetch): bookmark 6, impression 9206, like 78, quote 1, reply 0, retweet 7

> 【お知らせ】
>
> 3月15日に渋谷で開催されるP3NFESTにおいて、基調講演を行う並びとなりました！
> ホワイトボックスによる脆弱性調査に必須である、コードの歩き方を解説します！
>
> https://x.com/kazzyokomizo/status/1888747412321395150

**Links in post:** https://x.com/kazzyokomizo/status/1888747412321395150

**Quoted post** 1888747412321395150: not readable via the API (deleted, private, or withheld).


---

## 2025-01-27 · Post · Git/GitHubに対して、認証情報の漏洩に繋がる複数の脆弱性を報告しました。


### Post — @ryotkak — 2025-01-27 01:32 UTC (2025-01-27 02:32 WAT)

- URL: https://x.com/ryotkak/status/1883689421750583600
- Metrics (at fetch): bookmark 134, impression 123668, like 723, quote 3, reply 1, retweet 161

> Git/GitHubに対して、認証情報の漏洩に繋がる複数の脆弱性を報告しました。
> 既に修正版がリリースされているため、更新を推奨いたします！ https://twitter.com/flatt_security/status/1883682348727976314

**Links in post:** https://twitter.com/flatt_security/status/1883682348727976314

**Quoted post** 1883682348727976314: not readable via the API (deleted, private, or withheld).


---

## 2025-01-26 · Post · I published a blog post about six vulnerabilities in Git/GitHub-related projects. They all result in


### Post — @ryotkak — 2025-01-26 15:01 UTC (2025-01-26 16:01 WAT)

- URL: https://x.com/ryotkak/status/1883530673061003672
- Metrics (at fetch): bookmark 45, impression 23316, like 173, quote 0, reply 1, retweet 30

> I published a blog post about six vulnerabilities in Git/GitHub-related projects. They all result in credential leakage when cloning a malicious repository, so be sure to update the Git installation! https://twitter.com/flatt_sec_en/status/1883530053843292288

**Links in post:** https://twitter.com/flatt_sec_en/status/1883530053843292288

**Quoted post** 1883530053843292288: not readable via the API (deleted, private, or withheld).


---

## 2024-12-31 · Post · 皆様本年は大変お世話になりました。2025年も引き続き脆弱性調査等のセキュリティに関連した活動を行っていきますので、何卒よろしくお願いいたします。


### Post — @ryotkak — 2024-12-31 14:50 UTC (2024-12-31 15:50 WAT)

- URL: https://x.com/ryotkak/status/1874105732099895604
- Metrics (at fetch): bookmark 0, impression 5311, like 68, quote 0, reply 0, retweet 0

> 皆様本年は大変お世話になりました。2025年も引き続き脆弱性調査等のセキュリティに関連した活動を行っていきますので、何卒よろしくお願いいたします。
> 良いお年をお迎えください！


---

## 2024-12-07 · Thread · OpenWrtのビルド用サーバーに脆弱性を報告しました。


### Post — @ryotkak — 2024-12-07 09:40 UTC (2024-12-07 10:40 WAT)

- URL: https://x.com/ryotkak/status/1865330507082518561
- Metrics (at fetch): bookmark 5, impression 9242, like 64, quote 1, reply 1, retweet 21

> OpenWrtのビルド用サーバーに脆弱性を報告しました。
>
> Attended sysupgrade、firmware-selector.openwrt[.]orgあるいはCLIからのアップグレードを過去に実施した場合、改ざんされたファームウェアが配信された可能性が完全には否定できないため、ファームウェアの再更新を推奨します。 (1/2)


### Thread part 2 — @ryotkak — 2024-12-07 09:40 UTC (2024-12-07 10:40 WAT)

- URL: https://x.com/ryotkak/status/1865330549440827668
- Metrics (at fetch): bookmark 7, impression 4654, like 32, quote 0, reply 0, retweet 15

> 技術的解説についてはこちらの記事をご確認ください。 https://flatt.tech/research/posts/compromising-openwrt-supply-chain-sha256-collision/
>
> 公式からの発表はこちらをご覧ください。 http://lists.openwrt.org/pipermail/openwrt-announce/2024-December/000061.html (2/2)

**Links in post:** https://flatt.tech/research/posts/compromising-openwrt-supply-chain-sha256-collision/, http://lists.openwrt.org/pipermail/openwrt-announce/2024-December/000061.html


---

## 2024-12-07 · Thread · PSA


Tags (automatic): Path normalization


### Post — @ryotkak — 2024-12-07 09:32 UTC (2024-12-07 10:32 WAT)

- URL: https://x.com/ryotkak/status/1865328560342524196
- Metrics (at fetch): bookmark 17, impression 7722, like 60, quote 0, reply 2, retweet 10

> PSA
> If you're using OpenWrt router and have used the Attended sysupgrade, firmware-selector.openwrt[.]org or CLI upgrade previously, I recommend you to re-flash your firmware
>
> Due to a security issue, it was possible to pollute the firmware images delivered to these tools (1/2)


### Thread part 2 — @ryotkak — 2024-12-07 09:32 UTC (2024-12-07 10:32 WAT)

- URL: https://x.com/ryotkak/status/1865328600024809938
- Metrics (at fetch): bookmark 139, impression 32376, like 225, quote 5, reply 1, retweet 74

> If you're interested in the technical details, I wrote the blog post here: https://flatt.tech/research/posts/compromising-openwrt-supply-chain-sha256-collision/
>
> For the further details, please check out the announcement from the OpenWrt team: http://lists.openwrt.org/pipermail/openwrt-announce/2024-December/000061.html (2/2)

**Links in post:** https://flatt.tech/research/posts/compromising-openwrt-supply-chain-sha256-collision/, http://lists.openwrt.org/pipermail/openwrt-announce/2024-December/000061.html


---

## 2024-11-29 · Post · NECの法人向けルーターに脆弱性を報告しました。CVE-2024-11013についてはユーザーに悪意がなくてもコマンドインジェクションが成立するためご注意ください。


### Post — @ryotkak — 2024-11-29 11:02 UTC (2024-11-29 12:02 WAT)

- URL: https://x.com/ryotkak/status/1862451969304273020
- Metrics (at fetch): bookmark 52, impression 36601, like 246, quote 7, reply 2, retweet 121

> NECの法人向けルーターに脆弱性を報告しました。CVE-2024-11013についてはユーザーに悪意がなくてもコマンドインジェクションが成立するためご注意ください。
>
> また、一部EOL製品については更新が行われておりませんので、回避策の実施か後継製品への置換を推奨いたします！
>
> https://jpn.nec.com/security-info/secinfo/nv24-009.html

**Links in post:** https://jpn.nec.com/security-info/secinfo/nv24-009.html


---

## 2024-08-29 · Post · 安売りされてた時に買ったAPに脆弱性を報告しました。公式ファームウェアを利用されている方は更新を推奨します！ https://twitter.com/elecom_pr/status/18289739


### Post — @ryotkak — 2024-08-29 08:28 UTC (2024-08-29 09:28 WAT)

- URL: https://x.com/ryotkak/status/1829073590085730739
- Metrics (at fetch): bookmark 39, impression 52016, like 309, quote 3, reply 1, retweet 105

> 安売りされてた時に買ったAPに脆弱性を報告しました。公式ファームウェアを利用されている方は更新を推奨します！ https://twitter.com/elecom_pr/status/1828973917131981199

**Links in post:** https://twitter.com/elecom_pr/status/1828973917131981199

**Quoted post** 1828973917131981199: not readable via the API (deleted, private, or withheld).


---

## 2024-08-02 · Thread · I recently developed and posted about a technique called "First sequence sync", expanding @albinowax


Tags (automatic): Race condition


### Post — @ryotkak — 2024-08-02 15:00 UTC (2024-08-02 16:00 WAT)

- URL: https://x.com/ryotkak/status/1819387926247362961
- Metrics (at fetch): bookmark 495, impression 123216, like 792, quote 17, reply 15, retweet 243

> I recently developed and posted about a technique called "First sequence sync", expanding @albinowax's single packet attack.
>
> This technique allowed me to send 10,000 requests in 166ms, which breaks the packet size limitation of the single packet attack.
>
> https://flatt.tech/research/posts/beyond-the-limit-expanding-single-packet-race-condition-with-first-sequence-sync/

**Links in post:** https://flatt.tech/research/posts/beyond-the-limit-expanding-single-packet-race-condition-with-first-sequence-sync/


### Thread part 2 — @ryotkak — 2024-08-03 11:33 UTC (2024-08-03 12:33 WAT)

- URL: https://x.com/ryotkak/status/1819698076665192836
- Metrics (at fetch): bookmark 0, impression 253, like 1, quote 0, reply 1, retweet 0

> @sw33tLie @0xteknogeek @albinowax So, even if we find the server that allows parallel processing of requests, it's unlikely to be much powerful as the techniques for HTTP/2


---

## 2024-07-01 · Post · OpenSSHの任意コード実行、発見者によると


### Post — @ryotkak — 2024-07-01 12:37 UTC (2024-07-01 13:37 WAT)

- URL: https://x.com/ryotkak/status/1807755450383028439
- Metrics (at fetch): bookmark 314, impression 556901, like 1189, quote 41, reply 0, retweet 660

> OpenSSHの任意コード実行、発見者によると
>
> 1. デフォルト設定で攻撃が可能
> 2. 32bit環境においては任意コード実行が可能であることを確認済み
> 3. 64bit環境においても時間をかければ任意コード実行が可能であると思われる
>
> ということで、早急に更新をした方が良さそうです！
> https://www.qualys.com/2024/07/01/cve-2024-6387/regresshion.txt

**Links in post:** https://www.qualys.com/2024/07/01/cve-2024-6387/regresshion.txt


---

## 2024-07-01 · Post · まだ手元では検証できていないんですが、OpenSSHにおけるRCEが見つかっているので各位ご確認を～


### Post — @ryotkak — 2024-07-01 10:32 UTC (2024-07-01 11:32 WAT)

- URL: https://x.com/ryotkak/status/1807723926107373603
- Metrics (at fetch): bookmark 13, impression 16660, like 64, quote 0, reply 0, retweet 13

> まだ手元では検証できていないんですが、OpenSSHにおけるRCEが見つかっているので各位ご確認を～
> https://x.com/qualys/status/1807693619161133539

**Links in post:** https://x.com/qualys/status/1807693619161133539

**Quoted post** 1807693619161133539: not readable via the API (deleted, private, or withheld).


---

## 2024-06-24 · Post · 英語で投稿した記事を社内で日本語訳していただきました！ https://twitter.com/flatt_security/status/1805045005498962307


### Post — @ryotkak — 2024-06-24 01:08 UTC (2024-06-24 02:08 WAT)

- URL: https://x.com/ryotkak/status/1805045257257779532
- Metrics (at fetch): bookmark 7, impression 9080, like 32, quote 0, reply 0, retweet 1

> 英語で投稿した記事を社内で日本語訳していただきました！ https://twitter.com/flatt_security/status/1805045005498962307

**Links in post:** https://twitter.com/flatt_security/status/1805045005498962307

**Quoted post** 1805045005498962307: not readable via the API (deleted, private, or withheld).


---

## 2024-04-28 · Post · Reproduced DOMPurify 3.1.0 bypass, but my payload requires two mutations. Has anyone managed to trig


### Post — @ryotkak — 2024-04-28 10:14 UTC (2024-04-28 11:14 WAT)

- URL: https://x.com/ryotkak/status/1784526620033974765
- Metrics (at fetch): bookmark 34, impression 16880, like 114, quote 0, reply 9, retweet 2

> Reproduced DOMPurify 3.1.0 bypass, but my payload requires two mutations. Has anyone managed to trigger it with a single mutation? [pic.x.com/QIy4C5OqtE]

**Media:**
- photo: https://pbs.twimg.com/media/GMPpgJCbgAAt977.jpg — no alt text provided by author


---

## 2024-04-10 · Post · I posted a blog regarding the vulnerabilities in the runtime of programming languages, including the


### Post — @ryotkak — 2024-04-10 00:32 UTC (2024-04-10 01:32 WAT)

- URL: https://x.com/ryotkak/status/1777857038170866133
- Metrics (at fetch): bookmark 33, impression 54679, like 181, quote 4, reply 4, retweet 31

> I posted a blog regarding the vulnerabilities in the runtime of programming languages, including the recent Rust's critical vulnerability. https://twitter.com/flatt_sec_en/status/1777853903054553441

**Links in post:** https://twitter.com/flatt_sec_en/status/1777853903054553441

**Quoted post** 1777853903054553441: not readable via the API (deleted, private, or withheld).


---

## 2024-04-02 · Post · HackerOneアンバサダークラブの日本部門アンバサダーになりました。


Tags (automatic): Platform: HackerOne


### Post — @ryotkak — 2024-04-02 10:01 UTC (2024-04-02 11:01 WAT)

- URL: https://x.com/ryotkak/status/1775101176666861779
- Metrics (at fetch): bookmark 13, impression 15459, like 116, quote 0, reply 4, retweet 10

> HackerOneアンバサダークラブの日本部門アンバサダーになりました。
> 日本におけるバグバウンティコミュニティはまだまだ小さいのが現状ですが、これから更に盛り上げていけるよう尽力します。
>
> また、日本在住のバグハンターの方でアンバサダークラブの会員になりたいという方はDM等でご一報ください。 https://twitter.com/Hacker0x01/status/1774912251561930775

**Links in post:** https://twitter.com/Hacker0x01/status/1774912251561930775

**Quoted post** 1774912251561930775: not readable via the API (deleted, private, or withheld).


---

## 2024-04-01 · Post · I posted about a bypass of a recent DOMPurify patch, which allowed DOMPurify bypass in certain cases


### Post — @ryotkak — 2024-04-01 15:04 UTC (2024-04-01 16:04 WAT)

- URL: https://x.com/ryotkak/status/1774814984306065788
- Metrics (at fetch): bookmark 19, impression 12148, like 98, quote 0, reply 2, retweet 13

> I posted about a bypass of a recent DOMPurify patch, which allowed DOMPurify bypass in certain cases.
>
> https://x.com/flatt_sec_en/status/1774814606852301138

**Links in post:** https://x.com/flatt_sec_en/status/1774814606852301138

**Quoted post** 1774814606852301138: not readable via the API (deleted, private, or withheld).


---

## 2024-03-21 · Post · 特定条件下で刺さるDOMPurifyのバイパスを報告しました。後日軽い解説記事を書くかもしれません https://twitter.com/cure53berlin/status/1770787676


### Post — @ryotkak — 2024-03-21 12:44 UTC (2024-03-21 13:44 WAT)

- URL: https://x.com/ryotkak/status/1770793606980260200
- Metrics (at fetch): bookmark 5, impression 6662, like 59, quote 0, reply 1, retweet 1

> 特定条件下で刺さるDOMPurifyのバイパスを報告しました。後日軽い解説記事を書くかもしれません https://twitter.com/cure53berlin/status/1770787676561535349

**Links in post:** https://twitter.com/cure53berlin/status/1770787676561535349

**Quoted post** 1770787676561535349: not readable via the API (deleted, private, or withheld).


---

## 2024-03-12 · Thread · Is anyone able to execute arbitrary JavaScript with the following snippets?


### Post — @ryotkak — 2024-03-12 13:54 UTC (2024-03-12 14:54 WAT)

- URL: https://x.com/ryotkak/status/1767549660431089813
- Metrics (at fetch): bookmark 45, impression 15944, like 64, quote 0, reply 7, retweet 10

> Is anyone able to execute arbitrary JavaScript with the following snippets?
> This is a real-world problem that I encountered while hunting on the bug bounty program, so I'm happy to split the bounty if anyone finds the solution!
>
> Details: https://gist.github.com/Ry0taK/5ce7be0db9ef520a032698eda5e9fd65 [pic.x.com/PPAxhKvtMj]

**Media:**
- photo: https://pbs.twimg.com/media/GIeWvhda0AEK29k.jpg — no alt text provided by author

**Links in post:** https://gist.github.com/Ry0taK/5ce7be0db9ef520a032698eda5e9fd65


### Thread part 2 — @ryotkak — 2024-03-13 00:46 UTC (2024-03-13 01:46 WAT)

- URL: https://x.com/ryotkak/status/1767713698674597938
- Metrics (at fetch): bookmark 0, impression 2732, like 1, quote 0, reply 1, retweet 0

> I've updated the code snippet to include mode contexts, and added some more FAQs:
> 1. The run function is used as a listener of the message event, so this function can be reached multiple times, and it'll discard the return value.
> 2. obj will always be empty. [pic.x.com/SGWiwCCcLv]

**Media:**
- photo: https://pbs.twimg.com/media/GIgtRBraUAA6mCS.jpg — no alt text provided by author


---

## 2024-02-18 · Post · 確定申告が終わったことを記念して、確定申告をやる際に使用したワールドを公開しました(?)


### Post — @ryotkak — 2024-02-18 08:12 UTC (2024-02-18 09:12 WAT)

- URL: https://x.com/ryotkak/status/1759128841480736987
- Metrics (at fetch): bookmark 3, impression 5532, like 39, quote 0, reply 1, retweet 10

> 確定申告が終わったことを記念して、確定申告をやる際に使用したワールドを公開しました(?)
>
> https://vrchat.com/home/world/wrld_0f0930f8-c5ac-4aaf-9f20-976243aec438
>
> 公開にあたってワールドデータを手直ししていただいた@ri4zn氏に改めて感謝申し上げます

**Links in post:** https://vrchat.com/home/world/wrld_0f0930f8-c5ac-4aaf-9f20-976243aec438


---

## 2023-12-23 · Post · @joaxcar @cure53berlin @htmx_org Just to be clear, I believe it's not the responsibility of htmx or 


### Post — @ryotkak — 2023-12-23 03:46 UTC (2023-12-23 04:46 WAT)

- URL: https://x.com/ryotkak/status/1738405634540998702
- Metrics (at fetch): bookmark 0, impression 386, like 2, quote 0, reply 1, retweet 0

> @joaxcar @cure53berlin @htmx_org Just to be clear, I believe it's not the responsibility of htmx or DOMPurify to handle such cases, rather the responsibility of the user who combines these libraries


---

## 2023-12-23 · Post · Cloudflare Pages上の任意のページを改竄したり、Pagesで使用されているFunctionsのコードを読み取ったりすることが可能だった脆弱性についての話を公開しました


### Post — @ryotkak — 2023-12-23 00:29 UTC (2023-12-23 01:29 WAT)

- URL: https://x.com/ryotkak/status/1738356007515140395
- Metrics (at fetch): bookmark 104, impression 52151, like 393, quote 4, reply 4, retweet 109

> Cloudflare Pages上の任意のページを改竄したり、Pagesで使用されているFunctionsのコードを読み取ったりすることが可能だった脆弱性についての話を公開しました
>
> https://blog.ryotak.net/post/cloudflare-pages-privesc-and-page-tampering/

**Links in post:** https://blog.ryotak.net/post/cloudflare-pages-privesc-and-page-tampering/


---

## 2023-10-06 · Thread · I made a small XSS Challenge!


Tags (automatic): XSS, Memory corruption / native


### Post — @ryotkak — 2023-10-06 13:50 UTC (2023-10-06 14:50 WAT)

- URL: https://x.com/ryotkak/status/1710291366654181749
- Metrics (at fetch): bookmark 111, impression 61542, like 235, quote 0, reply 8, retweet 39

> I made a small XSS Challenge!
>
> Can you pop an alert on this page? (The intended solution should be hard!)
>
> Rules are included on the challenge page: https://ryotak-xss-challenge.pages.dev/ [pic.x.com/Xfdbij0iPC]

**Media:**
- photo: https://pbs.twimg.com/media/F7ws25vXQAArAhq.jpg — no alt text provided by author

**Links in post:** https://ryotak-xss-challenge.pages.dev/


### Thread part 2 — @ryotkak — 2023-10-07 00:04 UTC (2023-10-07 01:04 WAT)

- URL: https://x.com/ryotkak/status/1710445886017515744
- Metrics (at fetch): bookmark 0, impression 18586, like 17, quote 0, reply 1, retweet 2

> Two solves so far!
> Congratulations to @LiveOverflow and @stueotue for solving it!
> There's no solves with the intended solution at this point, so I added notes about the intended solution


### Thread part 3 — @ryotkak — 2023-10-08 13:35 UTC (2023-10-08 14:35 WAT)

- URL: https://x.com/ryotkak/status/1711012407689245148
- Metrics (at fetch): bookmark 0, impression 4700, like 1, quote 0, reply 2, retweet 0

> I've made a change to the challenge page to reduce the difficulty.
>
> This challenge is now on https://ryotak-challenges.github.io/xss-chall-1/ and the URL of AngularJS script is changed.
>
> The reason for this change is to drop the HTTP/3 support. Nothing else including the contents of the script is changed

**Links in post:** https://ryotak-challenges.github.io/xss-chall-1/


### Thread part 4 — @ryotkak — 2023-10-29 03:08 UTC (2023-10-29 04:08 WAT)

- URL: https://x.com/ryotkak/status/1718464730430619664
- Metrics (at fetch): bookmark 2, impression 3553, like 5, quote 0, reply 0, retweet 0

> The challenge is now over! The writeup is published here:
> https://x.com/ryotkak/status/1718463660853801027

**Links in post:** https://x.com/ryotkak/status/1718463660853801027

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2023-10-29 03:03 UTC (2023-10-29 04:03 WAT)
    
    - URL: https://x.com/ryotkak/status/1718463660853801027
    - Metrics (at fetch): bookmark 152, impression 66386, like 421, quote 5, reply 4, retweet 100
    
    > I published an article about the DOM-based race condition, which was the solution for the challenge that I posted 3 weeks ago.
    > https://blog.ryotak.net/post/dom-based-race-condition/
    
    **Links in post:** https://blog.ryotak.net/post/dom-based-race-condition/
    


---

## 2023-10-29 · Post · I published an article about the DOM-based race condition, which was the solution for the challenge 


Tags (automatic): Race condition


### Post — @ryotkak — 2023-10-29 03:03 UTC (2023-10-29 04:03 WAT)

- URL: https://x.com/ryotkak/status/1718463660853801027
- Metrics (at fetch): bookmark 152, impression 66386, like 421, quote 5, reply 4, retweet 100

> I published an article about the DOM-based race condition, which was the solution for the challenge that I posted 3 weeks ago.
> https://blog.ryotak.net/post/dom-based-race-condition/

**Links in post:** https://blog.ryotak.net/post/dom-based-race-condition/


---

## 2023-07-31 · Post · 書きました。GitHubに報告したSSRFの話です。 https://twitter.com/flatt_security/status/1685824554034421760


### Post — @ryotkak — 2023-07-31 03:19 UTC (2023-07-31 04:19 WAT)

- URL: https://x.com/ryotkak/status/1685852543308730368
- Metrics (at fetch): bookmark 13, impression 32395, like 138, quote 0, reply 2, retweet 25

> 書きました。GitHubに報告したSSRFの話です。 https://twitter.com/flatt_security/status/1685824554034421760

**Links in post:** https://twitter.com/flatt_security/status/1685824554034421760

**Quoted post** 1685824554034421760: not readable via the API (deleted, private, or withheld).


---

## 2023-07-18 · Thread · 弊社(株式会社Flatt Security)と弊グループ(Japan HackerOne Club)が協賛するイベントを9月に開催します。ご参加お待ちしております！ https://twitter.c


Tags (automatic): Platform: HackerOne


### Post — @ryotkak — 2023-07-18 06:00 UTC (2023-07-18 07:00 WAT)

- URL: https://x.com/ryotkak/status/1681182135842131968
- Metrics (at fetch): bookmark 3, impression 12730, like 21, quote 0, reply 1, retweet 4

> 弊社(株式会社Flatt Security)と弊グループ(Japan HackerOne Club)が協賛するイベントを9月に開催します。ご参加お待ちしております！ https://twitter.com/flatt_security/status/1681137830926618625

**Links in post:** https://twitter.com/flatt_security/status/1681137830926618625

**Quoted post** 1681137830926618625: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @ryotkak — 2023-07-18 12:44 UTC (2023-07-18 13:44 WAT)

- URL: https://x.com/ryotkak/status/1681283899224363008
- Metrics (at fetch): bookmark 0, impression 231, like 0, quote 0, reply 0, retweet 0

> @Rhynorater あー、残念


---

## 2023-07-07 · Post · やるらしいです https://twitter.com/flatt_security/status/1677125738359848960


### Post — @ryotkak — 2023-07-07 01:29 UTC (2023-07-07 02:29 WAT)

- URL: https://x.com/ryotkak/status/1677127620956401665
- Metrics (at fetch): bookmark 5, impression 18684, like 59, quote 0, reply 1, retweet 7

> やるらしいです https://twitter.com/flatt_security/status/1677125738359848960

**Links in post:** https://twitter.com/flatt_security/status/1677125738359848960

**Quoted post** 1677125738359848960: not readable via the API (deleted, private, or withheld).


---

## 2023-07-06 · Post · 試しにThreads始めてみました


### Post — @ryotkak — 2023-07-06 00:23 UTC (2023-07-06 01:23 WAT)

- URL: https://x.com/ryotkak/status/1676748558425526273
- Metrics (at fetch): bookmark 0, impression 3071, like 4, quote 0, reply 0, retweet 1

> 試しにThreads始めてみました
> https://www.threads.net/@ryotkak

**Links in post:** https://www.threads.net/@ryotkak


---

## 2023-06-29 · Post · 各位: 大腸炎になったので活動ペースをしばらく落とします。溜まっている連絡は順次返していきますが、急ぎであればTwitterのDMかDiscordで投げてください。


### Post — @ryotkak — 2023-06-29 01:50 UTC (2023-06-29 02:50 WAT)

- URL: https://x.com/ryotkak/status/1674233949177139205
- Metrics (at fetch): bookmark 0, impression 5463, like 21, quote 0, reply 6, retweet 0

> 各位: 大腸炎になったので活動ペースをしばらく落とします。溜まっている連絡は順次返していきますが、急ぎであればTwitterのDMかDiscordで投げてください。


---

## 2023-05-30 · Thread · Minecraftに報告していた脆弱性 (CVE-2023-33245) が最新のバージョンで修正されました。


### Post — @ryotkak — 2023-05-30 08:32 UTC (2023-05-30 09:32 WAT)

- URL: https://x.com/ryotkak/status/1663463319695683584
- Metrics (at fetch): bookmark 6, impression 20922, like 99, quote 0, reply 1, retweet 17

> Minecraftに報告していた脆弱性 (CVE-2023-33245) が最新のバージョンで修正されました。
> シンボリックリンクを含むワールドデータを読み込んだ際に、任意のファイルに対して部分的にコントロール可能な内容を書き込むことが出来るというものです。 https://twitter.com/CVEnew/status/1663425110030598145

**Links in post:** https://twitter.com/CVEnew/status/1663425110030598145

**Quoted post** 1663425110030598145: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @ryotkak — 2023-05-30 08:33 UTC (2023-05-30 09:33 WAT)

- URL: https://x.com/ryotkak/status/1663463644389322753
- Metrics (at fetch): bookmark 1, impression 3092, like 7, quote 0, reply 0, retweet 0

> 修正のバックポートはされなさそうなので、古いバージョンで信頼できないワールド (インターネット上からダウンロードし、解凍したものなど) を読み込む際はシンボリックリンクが含まれていないことを確認することを推奨します。
> 公式サイトのヘルプページもご確認ください。
> https://help.minecraft.net/hc/en-us/articles/16165590199181

**Links in post:** https://help.minecraft.net/hc/en-us/articles/16165590199181


---

## 2023-04-22 · Thread · GitHubスタッフのアクセストークンを漏洩させることができた脆弱性に関して解説した記事を公開しました


### Post — @ryotkak — 2023-04-22 06:49 UTC (2023-04-22 07:49 WAT)

- URL: https://x.com/ryotkak/status/1649666796717506567
- Metrics (at fetch): bookmark 84, impression 68490, like 380, quote 2, reply 4, retweet 86

> GitHubスタッフのアクセストークンを漏洩させることができた脆弱性に関して解説した記事を公開しました
>
> https://blog.ryotak.net/post/github-actions-staff-access-token/

**Links in post:** https://blog.ryotak.net/post/github-actions-staff-access-token/


### Thread part 2 — @ryotkak — 2023-04-22 06:49 UTC (2023-04-22 07:49 WAT)

- URL: https://x.com/ryotkak/status/1649666837406429185
- Metrics (at fetch): bookmark 26, impression 10834, like 91, quote 1, reply 3, retweet 25

> Published a write-up about the vulnerability which could expose the access token of GitHub Staff.
>
> https://blog.ryotak.net/post/github-actions-staff-access-token-en/

**Links in post:** https://blog.ryotak.net/post/github-actions-staff-access-token-en/


---

## 2023-02-23 · Post · Security․Tokyoにご参加くださった方、ありがとうございました！ 


### Post — @ryotkak — 2023-02-23 05:12 UTC (2023-02-23 06:12 WAT)

- URL: https://x.com/ryotkak/status/1628623868209532929
- Metrics (at fetch): bookmark 0, impression 5011, like 21, quote 0, reply 0, retweet 0

> Security․Tokyoにご参加くださった方、ありがとうございました！ 
> オフラインイベントに参加するのは2回目だったのですが、様々な方々と交流できて非常に楽しかったです


---

## 2023-02-07 · Post · ということで2月22日に六本木で勉強会イベントがあります！ 奮ってご参加ください(?)


### Post — @ryotkak — 2023-02-07 01:14 UTC (2023-02-07 02:14 WAT)

- URL: https://x.com/ryotkak/status/1622765810623324160
- Metrics (at fetch): bookmark 3, impression 11012, like 35, quote 0, reply 0, retweet 9

> ということで2月22日に六本木で勉強会イベントがあります！ 奮ってご参加ください(?)
> https://x.com/flatt_security/status/1622520908907958272

**Links in post:** https://x.com/flatt_security/status/1622520908907958272

**Quoted post** 1622520908907958272: not readable via the API (deleted, private, or withheld).


---

## 2022-12-09 · Post · 非公開アカウント( @RyotaK_Private )を作りました。 今後重要ではないツイートに関してはこちらのアカウントでつぶやきます。


### Post — @ryotkak — 2022-12-09 00:57 UTC (2022-12-09 01:57 WAT)

- URL: https://x.com/ryotkak/status/1601018259825778689
- Metrics (at fetch): bookmark 0, impression 0, like 14, quote 1, reply 0, retweet 0

> 非公開アカウント( @RyotaK_Private )を作りました。 今後重要ではないツイートに関してはこちらのアカウントでつぶやきます。


---

## 2022-11-18 · Post · BitBucketにRCEを報告しました。 (より正確には、BitBucketが使用しているライブラリに脆弱性を報告する際に提供した情報により、BitBucketに脆弱性が発見されました。)


### Post — @ryotkak — 2022-11-18 00:48 UTC (2022-11-18 01:48 WAT)

- URL: https://x.com/ryotkak/status/1593405814747766785
- Metrics (at fetch): bookmark 6, impression 0, like 102, quote 1, reply 3, retweet 11

> BitBucketにRCEを報告しました。 (より正確には、BitBucketが使用しているライブラリに脆弱性を報告する際に提供した情報により、BitBucketに脆弱性が発見されました。)
> 対象のバージョンを使用している方は更新してください。 (技術的詳細はしばらくの間公開しません。)
> https://confluence.atlassian.com/bitbucketserver/bitbucket-server-and-data-center-security-advisory-2022-11-16-1180141667.html

**Links in post:** https://confluence.atlassian.com/bitbucketserver/bitbucket-server-and-data-center-security-advisory-2022-11-16-1180141667.html


---

## 2022-11-02 · Post · ところでOpenSSLとは全く関係ないんですが、Goに報告していた脆弱性が修正されました。Windowsにおいて環境変数の値が制御できる場合、別の環境変数を挿入できるという脆弱性です。 https:/


### Post — @ryotkak — 2022-11-02 01:44 UTC (2022-11-02 02:44 WAT)

- URL: https://x.com/ryotkak/status/1587621596180905984
- Metrics (at fetch): bookmark 4, impression 0, like 107, quote 0, reply 2, retweet 17

> ところでOpenSSLとは全く関係ないんですが、Goに報告していた脆弱性が修正されました。Windowsにおいて環境変数の値が制御できる場合、別の環境変数を挿入できるという脆弱性です。 https://twitter.com/golang/status/1587490110152773632

**Links in post:** https://twitter.com/golang/status/1587490110152773632

**Quoted post** 1587490110152773632: not readable via the API (deleted, private, or withheld).


---

## 2022-11-02 · Post · Datadogが出したOpenSSLの脆弱性に関する解説記事でPoCに使われてるPunycode、デコードすると「3年B組金八先生」になる... (なぜ？)


### Post — @ryotkak — 2022-11-02 00:50 UTC (2022-11-02 01:50 WAT)

- URL: https://x.com/ryotkak/status/1587608072952115200
- Metrics (at fetch): bookmark 18, impression 0, like 376, quote 5, reply 2, retweet 124

> Datadogが出したOpenSSLの脆弱性に関する解説記事でPoCに使われてるPunycode、デコードすると「3年B組金八先生」になる... (なぜ？)


---

## 2022-09-24 · Post · はい、ということでHackerOneのイベントであるH1-3493にオンラインで参加し(スペイン行きたかった...！)、Exterminator賞をいただきました。


Tags (automatic): Platform: HackerOne


### Post — @ryotkak — 2022-09-24 02:48 UTC (2022-09-24 03:48 WAT)

- URL: https://x.com/ryotkak/status/1573504617362903040
- Metrics (at fetch): bookmark 2, impression 0, like 104, quote 0, reply 13, retweet 2

> はい、ということでHackerOneのイベントであるH1-3493にオンラインで参加し(スペイン行きたかった...！)、Exterminator賞をいただきました。
> イベントの締めを見るために朝5時まで起きていたため、非常に眠いです... https://twitter.com/Hacker0x01/status/1573401562050953217

**Links in post:** https://twitter.com/Hacker0x01/status/1573401562050953217

**Quoted post** 1573401562050953217: not readable via the API (deleted, private, or withheld).


---

## 2022-08-09 · Post · Googleが落ちているため、後ろがGoogleのYahoo Japan!も落ちている


### Post — @ryotkak — 2022-08-09 01:39 UTC (2022-08-09 02:39 WAT)

- URL: https://x.com/ryotkak/status/1556817475257282560
- Metrics (at fetch): bookmark 2, impression 0, like 59, quote 1, reply 1, retweet 4

> Googleが落ちているため、後ろがGoogleのYahoo Japan!も落ちている


---

## 2022-08-08 · Post · できるだけ色んな種類の機内食を食べるため、行きと帰りで航空会社を別にしているんですが、エコノミーで提供される食事は個人的にJALが一番好みだった


### Post — @ryotkak — 2022-08-08 10:21 UTC (2022-08-08 11:21 WAT)

- URL: https://x.com/ryotkak/status/1556586509653790721
- Metrics (at fetch): bookmark 0, impression 0, like 12, quote 0, reply 0, retweet 0

> できるだけ色んな種類の機内食を食べるため、行きと帰りで航空会社を別にしているんですが、エコノミーで提供される食事は個人的にJALが一番好みだった


---

## 2022-08-08 · Post · というわけで、8月2日〜8月8日の間、HackerOneのイベント(H1-702)に参加するためにラスベガスに行っていました。


Tags (automatic): Platform: HackerOne


### Post — @ryotkak — 2022-08-08 10:21 UTC (2022-08-08 11:21 WAT)

- URL: https://x.com/ryotkak/status/1556586322969497606
- Metrics (at fetch): bookmark 1, impression 0, like 112, quote 0, reply 0, retweet 9

> というわけで、8月2日〜8月8日の間、HackerOneのイベント(H1-702)に参加するためにラスベガスに行っていました。
> 2ヶ月ぶり2度目のライブハッキングイベントだったんですが、対象企業のうちの一つで一位を取った他、Most Valuable Hackerに選んでいただけました 🎉 https://twitter.com/Hacker0x01/status/1556151101027762176

**Links in post:** https://twitter.com/Hacker0x01/status/1556151101027762176

**Quoted post** 1556151101027762176: not readable via the API (deleted, private, or withheld).


---

## 2022-08-08 · Post · ただいま日本


### Post — @ryotkak — 2022-08-08 10:20 UTC (2022-08-08 11:20 WAT)

- URL: https://x.com/ryotkak/status/1556586027258482688
- Metrics (at fetch): bookmark 0, impression 0, like 17, quote 0, reply 1, retweet 0

> ただいま日本


---

## 2022-08-07 · Thread · Most Valuable Hacker！


Tags (automatic): Platform: HackerOne


### Post — @ryotkak — 2022-08-07 05:14 UTC (2022-08-07 06:14 WAT)

- URL: https://x.com/ryotkak/status/1556146692184895488
- Metrics (at fetch): bookmark 13, impression 0, like 724, quote 2, reply 47, retweet 26

> Most Valuable Hacker！
> #h1702 [pic.x.com/oMulCDNEf6]

**Media:**
- photo: https://pbs.twimg.com/media/FZiLK2MUEAEO3aj.jpg — no alt text provided by author


### Thread part 2 — @ryotkak — 2022-08-07 05:37 UTC (2022-08-07 06:37 WAT)

- URL: https://x.com/ryotkak/status/1556152578303410176
- Metrics (at fetch): bookmark 0, impression 0, like 34, quote 1, reply 3, retweet 0

> HackerOneのイベント (h-702)でMost Valuable Hackerに選ばれました！


### Thread part 3 — @ryotkak — 2022-08-07 05:44 UTC (2022-08-07 06:44 WAT)

- URL: https://x.com/ryotkak/status/1556154251742613504
- Metrics (at fetch): bookmark 1, impression 0, like 2, quote 1, reply 0, retweet 0

> *h1-702です...


---

## 2022-08-05 · Post · 海外でこのレベルの怪我してるの、普通に考えて良くない気がしてきた


### Post — @ryotkak — 2022-08-05 19:11 UTC (2022-08-05 20:11 WAT)

- URL: https://x.com/ryotkak/status/1555632702245654528
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 1, retweet 0

> 海外でこのレベルの怪我してるの、普通に考えて良くない気がしてきた


---

## 2022-08-05 · Thread · 腰を痛めた


### Post — @ryotkak — 2022-08-05 18:40 UTC (2022-08-05 19:40 WAT)

- URL: https://x.com/ryotkak/status/1555624921501315072
- Metrics (at fetch): bookmark 0, impression 0, like 2, quote 0, reply 1, retweet 0

> 腰を痛めた


### Thread part 2 — @ryotkak — 2022-08-05 18:42 UTC (2022-08-05 19:42 WAT)

- URL: https://x.com/ryotkak/status/1555625360686870528
- Metrics (at fetch): bookmark 0, impression 0, like 9, quote 0, reply 0, retweet 0

> イベント会場のステージからジャンプで降りたら着地に失敗して腰と左半身を痛めました... (寝ても治らず)


---

## 2022-08-03 · Post · ラスベガスなう


### Post — @ryotkak — 2022-08-03 06:41 UTC (2022-08-03 07:41 WAT)

- URL: https://x.com/ryotkak/status/1554719021114675201
- Metrics (at fetch): bookmark 0, impression 0, like 33, quote 1, reply 1, retweet 0

> ラスベガスなう


---

## 2022-08-02 · Thread · さらば日本


### Post — @ryotkak — 2022-08-02 12:48 UTC (2022-08-02 13:48 WAT)

- URL: https://x.com/ryotkak/status/1554449023922122752
- Metrics (at fetch): bookmark 0, impression 0, like 22, quote 0, reply 3, retweet 0

> さらば日本


### Thread part 2 — @ryotkak — 2022-08-02 12:55 UTC (2022-08-02 13:55 WAT)

- URL: https://x.com/ryotkak/status/1554450849551634433
- Metrics (at fetch): bookmark 0, impression 0, like 0, quote 0, reply 0, retweet 0

> 当然機内は暇


---

## 2022-06-23 · Post · あ、よく考えたら初出しの情報なんですが、株式会社Flatt Securityで働いています。対戦よろしくお願いします(?)


### Post — @ryotkak — 2022-06-23 02:03 UTC (2022-06-23 03:03 WAT)

- URL: https://x.com/ryotkak/status/1539791335225688065
- Metrics (at fetch): bookmark 3, impression 0, like 170, quote 0, reply 0, retweet 15

> あ、よく考えたら初出しの情報なんですが、株式会社Flatt Securityで働いています。対戦よろしくお願いします(?)


---

## 2022-06-23 · Post · RT &gt; 


### Post — @ryotkak — 2022-06-23 02:02 UTC (2022-06-23 03:02 WAT)

- URL: https://x.com/ryotkak/status/1539791078584643585
- Metrics (at fetch): bookmark 0, impression 0, like 13, quote 0, reply 0, retweet 1

> RT &gt; 
> ということでオースティンに行ったときに食べたご飯の情報です (イベント期間中、出勤している扱いにしてもらった関係で会社のブログに書きました)


---

## 2022-06-18 · Thread · というわけで、HackerOneに招待されてH1-512に参加するためにテキサス州オースティンに行っていました


Tags (automatic): Platform: HackerOne


### Post — @ryotkak — 2022-06-18 20:37 UTC (2022-06-18 21:37 WAT)

- URL: https://x.com/ryotkak/status/1538259710922502147
- Metrics (at fetch): bookmark 1, impression 0, like 69, quote 0, reply 1, retweet 0

> というわけで、HackerOneに招待されてH1-512に参加するためにテキサス州オースティンに行っていました


### Thread part 2 — @ryotkak — 2022-06-18 20:39 UTC (2022-06-18 21:39 WAT)

- URL: https://x.com/ryotkak/status/1538260128675209217
- Metrics (at fetch): bookmark 0, impression 0, like 6, quote 0, reply 1, retweet 0

> 現地参加するかどうかを迷い続け、結局参加することを決断してから出発まで5日しかなかったので、かなり忙しかった...


---

## 2022-02-19 · Post · メルカリのセキュリティチームから、脆弱性報告のお礼としてハンガーとパーカーとTシャツをいただきました！


### Post — @ryotkak — 2022-02-19 05:22 UTC (2022-02-19 06:22 WAT)

- URL: https://x.com/ryotkak/status/1494905306153091076
- Metrics (at fetch): bookmark 11, impression 0, like 203, quote 0, reply 1, retweet 25

> メルカリのセキュリティチームから、脆弱性報告のお礼としてハンガーとパーカーとTシャツをいただきました！
> https://t.co/u8qrXtXd9Z https://t.co/2Q38WPM6sv https://t.co/zPkIspMfjT

**Media:**
- photo: https://pbs.twimg.com/media/FL719C5aAAQ_YCL.jpg — alt text: "ハンガー"
- photo: https://pbs.twimg.com/media/FL719D9aIAELIAc.jpg — alt text: "MERCARI BUG HUNTERパーカー"
- photo: https://pbs.twimg.com/media/FL71QfFaAAEHXVc.jpg — alt text: "MERCARI BUG HUNTER Tシャツ"

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2021-09-16 03:26 UTC (2021-09-16 04:26 WAT)
    
    - URL: https://x.com/ryotkak/status/1438343415087788036
    - Metrics (at fetch): not returned
    
    > バグバウンティで記念品として貰えるTシャツ、貰えるのは嬉しいんだけどハンガーが足りなくなるのでハンガーも一緒に送って欲しくなってきた
    


---

## 2022-02-12 · Post · Zshに脆弱性を報告しました。 (CVE-2021-45444)


### Post — @ryotkak — 2022-02-12 23:57 UTC (2022-02-13 00:57 WAT)

- URL: https://x.com/ryotkak/status/1492649060540760064
- Metrics (at fetch): bookmark 31, impression 0, like 512, quote 9, reply 0, retweet 125

> Zshに脆弱性を報告しました。 (CVE-2021-45444)
> 5.8.1より前のバージョンのZshは特定のプロンプト設定を使用している場合、プロンプト内のコマンドの出力結果を再帰的に解析します。
> これにより、悪意ある文字列を出力した際に、任意のコマンドを実行させる事が可能です。
> https://t.co/LE2P8nY5u0


---

## 2021-12-28 · Thread · Log4jの新しい脆弱性に関して、公式のセキュリティアドバイザリではRCEとなっていますが、細工された設定ファイルを読み込むことが攻撃の条件となっているため、設定ファイルを外部から読み込んでいるか、動


### Post — @ryotkak — 2021-12-28 23:49 UTC (2021-12-29 00:49 WAT)

- URL: https://x.com/ryotkak/status/1475977251338752002
- Metrics (at fetch): bookmark 14, impression 0, like 225, quote 3, reply 1, retweet 100

> Log4jの新しい脆弱性に関して、公式のセキュリティアドバイザリではRCEとなっていますが、細工された設定ファイルを読み込むことが攻撃の条件となっているため、設定ファイルを外部から読み込んでいるか、動的に設定を行っているケース等でないとRCEにはなりません。
> https://t.co/fyfUbMvYBs


### Thread part 2 — @ryotkak — 2021-12-29 02:29 UTC (2021-12-29 03:29 WAT)

- URL: https://x.com/ryotkak/status/1476017544335364096
- Metrics (at fetch): bookmark 4, impression 0, like 78, quote 2, reply 1, retweet 35

> Log4jの開発チームに確認したのですが、設定ファイルからのコード実行自体はセキュリティ上の問題としては扱っておらず、JNDIを使用して、LDAPからパスワードを取得している場合に当該のLDAPサーバーが侵害されると任意のコードが実行できる、という点をセキュリティ上の問題と見なしたそうです。


### Thread part 3 — @ryotkak — 2021-12-29 02:35 UTC (2021-12-29 03:35 WAT)

- URL: https://x.com/ryotkak/status/1476018925620318208
- Metrics (at fetch): bookmark 2, impression 0, like 41, quote 1, reply 0, retweet 21

> ちなみに、2.17.1においても細工された設定ファイルから任意のコードを実行することはできますが、Log4jの開発チームはこれを認識しており、かつ脆弱性ではないと考えているようです (念の為報告して、脆弱性ではないという旨の回答を受け取っています)


---

## 2021-12-22 · Post · 報告しました。現在も更新されていないアプリケーションが多数存在するため、Yappliを使用している企業の方はご確認ください。 https://t.co/TpiL5idPjg


### Post — @ryotkak — 2021-12-22 05:09 UTC (2021-12-22 06:09 WAT)

- URL: https://x.com/ryotkak/status/1473520980308148225
- Metrics (at fetch): bookmark 5, impression 0, like 60, quote 1, reply 0, retweet 18

> 報告しました。現在も更新されていないアプリケーションが多数存在するため、Yappliを使用している企業の方はご確認ください。 https://t.co/TpiL5idPjg

**Quoted post** 1473488720322248707: not readable via the API (deleted, private, or withheld).


---

## 2021-12-18 · Thread · はい、Log4jの3つ目の脆弱性が出ました。終わらない...


### Post — @ryotkak — 2021-12-18 12:08 UTC (2021-12-18 13:08 WAT)

- URL: https://x.com/ryotkak/status/1472176979961323522
- Metrics (at fetch): bookmark 57, impression 0, like 1483, quote 32, reply 5, retweet 558

> はい、Log4jの3つ目の脆弱性が出ました。終わらない...


### Thread part 2 — @ryotkak — 2021-12-18 12:12 UTC (2021-12-18 13:12 WAT)

- URL: https://x.com/ryotkak/status/1472177946073133056
- Metrics (at fetch): bookmark 2, impression 0, like 155, quote 1, reply 1, retweet 50

> 2.16.0でJNDIがかなり制限されているため、RCEには繋がらないと思っていますが、調査する気力がもうないので後日見てみます。
> ちなみに報告したのはAkamai TechnologiesのHideki Okamoto氏です。


### Thread part 3 — @ryotkak — 2021-12-18 12:19 UTC (2021-12-18 13:19 WAT)

- URL: https://x.com/ryotkak/status/1472179663904841729
- Metrics (at fetch): bookmark 3, impression 0, like 151, quote 1, reply 1, retweet 80

> 言い忘れてたので補足です。今回の脆弱性はLog4j 2.16.0において一部の設定で成立するDenial of Service(サービス妨害攻撃)です。影響を受ける方は2.17.0へ更新しましょう。


### Thread part 4 — @ryotkak — 2021-12-18 12:19 UTC (2021-12-18 13:19 WAT)

- URL: https://x.com/ryotkak/status/1472179828996833281
- Metrics (at fetch): bookmark 5, impression 0, like 124, quote 5, reply 0, retweet 79

> https://t.co/fyfUbMvYBs
>
> CVE-2021-45105: Apache Log4j2 does not always protect from infinite recursion in lookup evaluation


---

## 2021-12-17 · Thread · 補足しておくと、このツイートはCVE-2021-45046に付随する脆弱性に関しての言及です。


### Post — @ryotkak — 2021-12-17 07:33 UTC (2021-12-17 08:33 WAT)

- URL: https://x.com/ryotkak/status/1471745288159510531
- Metrics (at fetch): bookmark 7, impression 0, like 135, quote 3, reply 1, retweet 47

> 補足しておくと、このツイートはCVE-2021-45046に付随する脆弱性に関しての言及です。
> このツイートをした時点では機微な情報が抽出できるだけだと思っていたんですが、CVE-2021-45046を見て再度調査したところRCEまで行けそう、という事に気が付きました...。 https://t.co/LlqKWhrT89

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2021-12-12 23:44 UTC (2021-12-13 00:44 WAT)
    
    - URL: https://x.com/ryotkak/status/1470177786891767810
    - Metrics (at fetch): bookmark 18, impression 0, like 206, quote 2, reply 1, retweet 120
    
    > 詳細は言えないんですが、Log4j 2.15.0を使用している場合でもlookupsオプションは絶対に指定しないでください。
    > 次のバージョンである2.15.1において、lookupsオプションが指定されていても問題がないように変更される予定です。
    


### Thread part 2 — @ryotkak — 2021-12-17 08:12 UTC (2021-12-17 09:12 WAT)

- URL: https://x.com/ryotkak/status/1471755082274570240
- Metrics (at fetch): bookmark 1, impression 0, like 42, quote 1, reply 0, retweet 14

> あ、もう一個補足しておくと、このツイートをする3日前(12/10時点)にはLog4jチームに報告していました。
> CVE-2021-45046が当初DoSとして評価されてしまったのは、時間が取れずPoCを作れていなかったためというのと、情報の紐付けがうまく行っていなかったというのが原因だと思います。


---

## 2021-12-16 · Thread · 情報が出てしまったので言及しておきますが、Log4j 2.15.0を使用している場合でも、一部の設定でRCEが可能です。


### Post — @ryotkak — 2021-12-16 13:50 UTC (2021-12-16 14:50 WAT)

- URL: https://x.com/ryotkak/status/1471477923182170117
- Metrics (at fetch): bookmark 16, impression 0, like 196, quote 1, reply 2, retweet 96

> 情報が出てしまったので言及しておきますが、Log4j 2.15.0を使用している場合でも、一部の設定でRCEが可能です。
> おそらく明日中にはLog4jチームがアドバイザリを更新すると思うので、詳しくはそちらを参照してください。 https://t.co/vmaD0Q5AXo

**Quoted post** 1471465662975561734: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @ryotkak — 2021-12-16 14:22 UTC (2021-12-16 15:22 WAT)

- URL: https://x.com/ryotkak/status/1471485869685374984
- Metrics (at fetch): bookmark 1, impression 0, like 28, quote 1, reply 1, retweet 21

> @tsukkkkkun 一応補足しておくと、完全にデフォルトの設定では刺さりません。
> %m{lookups}を指定するか、CVE-2021-45046等の方法でLookupを発生させる必要があります


### Thread part 3 — @ryotkak — 2021-12-17 05:36 UTC (2021-12-17 06:36 WAT)

- URL: https://x.com/ryotkak/status/1471715844367745024
- Metrics (at fetch): bookmark 0, impression 0, like 30, quote 2, reply 0, retweet 10

> 実はこれ、僕も報告してました &amp; 詳細出ました。Log4j 2.15.0を使用している方で、影響を受ける方は2.16.0へ更新しましょう。
> https://t.co/fyfUbMvYBs
>
> &gt; Additional vulnerability details discovered independently by Ash Fox of Google, Anthony Weems of Praetorian, and RyotaK


---

## 2021-12-12 · Thread · 詳細は言えないんですが、Log4j 2.15.0を使用している場合でもlookupsオプションは絶対に指定しないでください。


### Post — @ryotkak — 2021-12-12 23:44 UTC (2021-12-13 00:44 WAT)

- URL: https://x.com/ryotkak/status/1470177786891767810
- Metrics (at fetch): bookmark 18, impression 0, like 206, quote 2, reply 1, retweet 120

> 詳細は言えないんですが、Log4j 2.15.0を使用している場合でもlookupsオプションは絶対に指定しないでください。
> 次のバージョンである2.15.1において、lookupsオプションが指定されていても問題がないように変更される予定です。


### Thread part 2 — @ryotkak — 2021-12-13 23:02 UTC (2021-12-14 00:02 WAT)

- URL: https://x.com/ryotkak/status/1470529629392109570
- Metrics (at fetch): bookmark 0, impression 0, like 16, quote 0, reply 0, retweet 2

> こちらの件、2.16.0において対応されたようです。


---

## 2021-12-12 · Thread · 昨日の時点で広く知れ渡っていましたが、WAFによる防御はほとんどのケースにおいて回避可能です。昨日の時点で、複数の研究者により回避方法が公開されているため、一時的な回避策を使用する場合はLog4j側の


### Post — @ryotkak — 2021-12-12 23:15 UTC (2021-12-13 00:15 WAT)

- URL: https://x.com/ryotkak/status/1470170475339091968
- Metrics (at fetch): bookmark 12, impression 0, like 163, quote 2, reply 1, retweet 52

> 昨日の時点で広く知れ渡っていましたが、WAFによる防御はほとんどのケースにおいて回避可能です。昨日の時点で、複数の研究者により回避方法が公開されているため、一時的な回避策を使用する場合はLog4j側の設定を変更するなどの方法を推奨します。


### Thread part 2 — @ryotkak — 2021-12-12 23:18 UTC (2021-12-13 00:18 WAT)

- URL: https://x.com/ryotkak/status/1470171340791758849
- Metrics (at fetch): bookmark 5, impression 0, like 82, quote 1, reply 0, retweet 32

> また、攻撃用のペイロードは複数の方法により難読化可能であるため、ログを確認する際は${と言った文字列を検索したほうが良いと思います。なお、攻撃が成功した場合、${といった文字列がログに出力されない場合があるため、可能であればLog4j以外の方法により取得したログを確認すると良さそうです。


---

## 2021-12-10 · Thread · Log4jの脆弱性、Javaのランタイムバージョンが最新で、デシリアライズ用のガジェットが無かったとしても悪用可能なので、絶対に更新してください...。


### Post — @ryotkak — 2021-12-10 14:44 UTC (2021-12-10 15:44 WAT)

- URL: https://x.com/ryotkak/status/1469317119733268483
- Metrics (at fetch): bookmark 24, impression 0, like 400, quote 8, reply 1, retweet 132

> Log4jの脆弱性、Javaのランタイムバージョンが最新で、デシリアライズ用のガジェットが無かったとしても悪用可能なので、絶対に更新してください...。


### Thread part 2 — @ryotkak — 2021-12-10 14:51 UTC (2021-12-10 15:51 WAT)

- URL: https://x.com/ryotkak/status/1469318765334917120
- Metrics (at fetch): bookmark 0, impression 0, like 46, quote 1, reply 2, retweet 4

> 技術的な解説はしません(するとしても一連の騒動が収まった後)が、どうせそのうち誰か気がつくと思います...。僕は疲れ果てたので寝ます


### Thread part 3 — @ryotkak — 2021-12-11 01:48 UTC (2021-12-11 02:48 WAT)

- URL: https://x.com/ryotkak/status/1469484243311271936
- Metrics (at fetch): bookmark 0, impression 0, like 39, quote 1, reply 0, retweet 9

> このツイート、ガジェット無しでRCEできるという意味合いではなく、十分に致命的な影響を他の攻撃方法により発生させられるので更新するべき、という意味合いのツイートです...！


---

## 2021-12-11 · Post · Log4j 2.15.0はJava 8が必須なので、Java 7を使用している環境はJavaのバージョンも上げなければ行けないらしく、かなり辛そうな感じになってるな


### Post — @ryotkak — 2021-12-11 00:34 UTC (2021-12-11 01:34 WAT)

- URL: https://x.com/ryotkak/status/1469465570152443905
- Metrics (at fetch): bookmark 36, impression 0, like 900, quote 45, reply 2, retweet 429

> Log4j 2.15.0はJava 8が必須なので、Java 7を使用している環境はJavaのバージョンも上げなければ行けないらしく、かなり辛そうな感じになってるな


---

## 2021-12-10 · Thread · Log4jの脆弱性、Log4Shellって名前がつきそう


### Post — @ryotkak — 2021-12-10 10:53 UTC (2021-12-10 11:53 WAT)

- URL: https://x.com/ryotkak/status/1469258854542491654
- Metrics (at fetch): bookmark 4, impression 0, like 162, quote 2, reply 1, retweet 21

> Log4jの脆弱性、Log4Shellって名前がつきそう


### Thread part 2 — @ryotkak — 2021-12-10 10:53 UTC (2021-12-10 11:53 WAT)

- URL: https://x.com/ryotkak/status/1469258947031080964
- Metrics (at fetch): bookmark 0, impression 0, like 18, quote 0, reply 1, retweet 3

> 付きそうというか付いてるな


---

## 2021-12-09 · Thread · ちょっと移動中で詳しく確認できてないんですが、log4j2に任意コード実行の脆弱性があり、Minecraftサーバー等で任意のコードが実行できるらしいので、サーバー管理者各位は今すぐlog4j2を使用


### Post — @ryotkak — 2021-12-09 23:13 UTC (2021-12-10 00:13 WAT)

- URL: https://x.com/ryotkak/status/1469082760363274240
- Metrics (at fetch): bookmark 43, impression 0, like 783, quote 14, reply 3, retweet 546

> ちょっと移動中で詳しく確認できてないんですが、log4j2に任意コード実行の脆弱性があり、Minecraftサーバー等で任意のコードが実行できるらしいので、サーバー管理者各位は今すぐlog4j2を使用しているソフトウェアを更新しましょう


### Thread part 2 — @ryotkak — 2021-12-09 23:14 UTC (2021-12-10 00:14 WAT)

- URL: https://x.com/ryotkak/status/1469083025816580096
- Metrics (at fetch): bookmark 3, impression 0, like 97, quote 0, reply 1, retweet 49

> 既に攻撃が始まってるらしく、かなり最悪な感じになってる


### Thread part 3 — @ryotkak — 2021-12-10 00:45 UTC (2021-12-10 01:45 WAT)

- URL: https://x.com/ryotkak/status/1469106025584537601
- Metrics (at fetch): bookmark 5, impression 0, like 99, quote 1, reply 1, retweet 85

> Minecraftサーバー 1.18、Minecraftクライアント 1.18で脆弱な挙動をすることを確認しました。(バニラ)
>
> 攻撃条件が細工されたログを出力することなので、サーバーであればサーバーに接続可能な任意のユーザー、クライアントであれば悪意あるチャットメッセージ等から任意コード実行ができそうです。


### Thread part 4 — @ryotkak — 2021-12-10 01:01 UTC (2021-12-10 02:01 WAT)

- URL: https://x.com/ryotkak/status/1469110011234500613
- Metrics (at fetch): bookmark 3, impression 0, like 64, quote 0, reply 1, retweet 41

> -Dlog4j2.formatMsgNoLookups=trueを起動時のパラメータに渡すと暫定的な対策になることも確認できました。(ただ、コードをしっかり読んだわけではないので間違いなく攻撃が成立しないとは言い切れません...)


### Thread part 5 — @ryotkak — 2021-12-10 01:05 UTC (2021-12-10 02:05 WAT)

- URL: https://x.com/ryotkak/status/1469110952096595971
- Metrics (at fetch): bookmark 2, impression 0, like 94, quote 4, reply 1, retweet 81

> サーバー側で対策が行われていたとしても、クライアント側への攻撃が行えることを確認しました。
> (つまり、最新のSpigotを使用しているサーバーに脆弱なクライアントで接続した場合、悪意あるプレイヤーが細工したチャットメッセージを送信することで任意コード実行を行うことができるかもしれません)


### Thread part 6 — @ryotkak — 2021-12-10 01:11 UTC (2021-12-10 02:11 WAT)

- URL: https://x.com/ryotkak/status/1469112478454157312
- Metrics (at fetch): bookmark 0, impression 0, like 43, quote 1, reply 1, retweet 16

> 最新版のSpigotにおいて脆弱性の修正が適切にバックポートされていることを確認しました


### Thread part 7 — @ryotkak — 2021-12-10 01:20 UTC (2021-12-10 02:20 WAT)

- URL: https://x.com/ryotkak/status/1469114682506358785
- Metrics (at fetch): bookmark 1, impression 0, like 34, quote 0, reply 1, retweet 17

> 最新版のFabric Loaderにおいて対策が行われていることを確認しました (なお、Minecraft Forgeに関しては現時点で対策版の公開が行われていません。)


### Thread part 8 — @ryotkak — 2021-12-10 01:21 UTC (2021-12-10 02:21 WAT)

- URL: https://x.com/ryotkak/status/1469114981988048896
- Metrics (at fetch): bookmark 2, impression 0, like 78, quote 1, reply 1, retweet 64

> 現時点でのまとめ
> - Spigotの最新ビルド: 対策済み
> - Fabric Loaderの最新版: 対策済み
> - Minecraft Forge: 未対策
> - Minecraft 1.18 (バニラ): 未対策


### Thread part 9 — @ryotkak — 2021-12-10 01:30 UTC (2021-12-10 02:30 WAT)

- URL: https://x.com/ryotkak/status/1469117199646617602
- Metrics (at fetch): bookmark 1, impression 0, like 49, quote 0, reply 1, retweet 20

> Paper(Spigotのフォーク)の最新ビルドにおいて、log4j2に対して行われた修正と同様の修正が行われていることを確認しました。なお、この修正は外部のLDAPサーバーとの通信を禁止するものであるため、依然としてローカルネットワーク内のLDAPサーバーへの通信を強制することが可能です。


### Thread part 10 — @ryotkak — 2021-12-10 06:02 UTC (2021-12-10 07:02 WAT)

- URL: https://x.com/ryotkak/status/1469185811237474304
- Metrics (at fetch): bookmark 2, impression 0, like 26, quote 0, reply 1, retweet 13

> -Dlog4j2.formatMsgNoLookups=true は古いバージョンのLog4j2には存在しないため、当該のバージョンを使用しているMinecraftにおいては対策として使用できません
> また、Minecraft(バニラ)に対して一時的な対策を施すパッチがMojangより配信されているようです。
> (仕事中なので検証ができていません...)


### Thread part 11 — @ryotkak — 2021-12-10 06:04 UTC (2021-12-10 07:04 WAT)

- URL: https://x.com/ryotkak/status/1469186194915622915
- Metrics (at fetch): bookmark 0, impression 0, like 13, quote 0, reply 0, retweet 3

> (当該のバージョンを使用しているMinecraftバージョンにおいては、が正しいです)


---

## 2021-12-09 · Post · 報告者？曰くApache Struts2などにも刺さるらしく、一週間ぐらいの間大変なことになりそう... https://t.co/FyIK7cOPTu


### Post — @ryotkak — 2021-12-09 23:23 UTC (2021-12-10 00:23 WAT)

- URL: https://x.com/ryotkak/status/1469085388837101569
- Metrics (at fetch): bookmark 4, impression 0, like 106, quote 2, reply 1, retweet 55

> 報告者？曰くApache Struts2などにも刺さるらしく、一週間ぐらいの間大変なことになりそう... https://t.co/FyIK7cOPTu

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2021-12-09 23:13 UTC (2021-12-10 00:13 WAT)
    
    - URL: https://x.com/ryotkak/status/1469082760363274240
    - Metrics (at fetch): bookmark 43, impression 0, like 783, quote 14, reply 3, retweet 546
    
    > ちょっと移動中で詳しく確認できてないんですが、log4j2に任意コード実行の脆弱性があり、Minecraftサーバー等で任意のコードが実行できるらしいので、サーバー管理者各位は今すぐlog4j2を使用しているソフトウェアを更新しましょう
    


---

## 2021-12-08 · Post · Microsoftから色々貰いました！


### Post — @ryotkak — 2021-12-08 09:19 UTC (2021-12-08 10:19 WAT)

- URL: https://x.com/ryotkak/status/1468510611525222404
- Metrics (at fetch): bookmark 1, impression 0, like 109, quote 1, reply 0, retweet 1

> Microsoftから色々貰いました！
> Thank you @msftsecresponse ;) https://t.co/tucB2WJMyy

**Media:**
- photo: https://pbs.twimg.com/media/FGEynkfVkAEbHBB.jpg — no alt text provided by author


---

## 2021-11-30 · Post · I published an article about vulnerability in Deno's registry that could allow tampering of Deno mod


### Post — @ryotkak — 2021-11-30 13:14 UTC (2021-11-30 14:14 WAT)

- URL: https://x.com/ryotkak/status/1465670531429003269
- Metrics (at fetch): bookmark 16, impression 0, like 79, quote 1, reply 0, retweet 19

> I published an article about vulnerability in Deno's registry that could allow tampering of Deno modules including Deno's install scripts.
>
> https://t.co/ak6TTBwf3z


---

## 2021-01-05 · Thread · Twitterのフリートにあった脆弱性の話です


### Post — @ryotkak — 2021-01-05 00:24 UTC (2021-01-05 01:24 WAT)

- URL: https://x.com/ryotkak/status/1346251211817713664
- Metrics (at fetch): not returned

> Twitterのフリートにあった脆弱性の話です
> https://blog.ryotak.me/post/twitter-privesc/

**Links in post:** https://blog.ryotak.me/post/twitter-privesc/


### Thread part 2 — @ryotkak — 2021-01-12 12:50 UTC (2021-01-12 13:50 WAT)

- URL: https://x.com/ryotkak/status/1348975587088482307
- Metrics (at fetch): not returned

> VSCodeのGitHubリポジトリに対して第三者が書き込み権限を奪えてしまった脆弱性の話です
> https://blog.ryotak.me/post/vscode-write-access/

**Links in post:** https://blog.ryotak.me/post/vscode-write-access/


### Thread part 3 — @ryotkak — 2021-02-25 03:33 UTC (2021-02-25 04:33 WAT)

- URL: https://x.com/ryotkak/status/1364780442121949184
- Metrics (at fetch): not returned

> GitHub Actionsにおけるサプライチェーン攻撃を通したリポジトリ侵害の影響範囲とその軽減策についてです
> https://blog.ryotak.me/post/github-actions-supplychain/

**Links in post:** https://blog.ryotak.me/post/github-actions-supplychain/


### Thread part 4 — @ryotkak — 2021-04-21 11:11 UTC (2021-04-21 12:11 WAT)

- URL: https://x.com/ryotkak/status/1384827136368775169
- Metrics (at fetch): not returned

> HomebrewのCaskリポジトリを侵害し、Homebrewを利用しているユーザーのコンピューター上で任意のコードを実行できた脆弱性の話です。
> 公式インシデント報告: https://brew.sh/2021/04/21/security-incident-disclosure/
> Blog (English): https://blog.ryotak.me/post/homebrew-security-incident-en/
> ブログ (日本語): https://blog.ryotak.me/post/homebrew-security-incident/

**Links in post:** https://brew.sh/2021/04/21/security-incident-disclosure/, https://blog.ryotak.me/post/homebrew-security-incident-en/, https://blog.ryotak.me/post/homebrew-security-incident/


### Thread part 5 — @ryotkak — 2021-07-16 00:00 UTC (2021-07-16 01:00 WAT)

- URL: https://x.com/ryotkak/status/1415823497398345731
- Metrics (at fetch): not returned

> cdnjsにおける任意コード実行が可能な脆弱性により、インターネット上のウェブサイトの12.7%を改ざんできた話です。
> https://blog.ryotak.me/post/cdnjs-remote-code-execution/

**Links in post:** https://blog.ryotak.me/post/cdnjs-remote-code-execution/


### Thread part 6 — @ryotkak — 2021-07-30 12:00 UTC (2021-07-30 13:00 WAT)

- URL: https://x.com/ryotkak/status/1421078156060938241
- Metrics (at fetch): not returned

> PyPI(Pythonのパッケージレジストリ)における潜在的な任意コード実行により、Pythonのエコシステムを侵害することができた脆弱性の話です。
>
> https://blog.ryotak.me/post/pypi-potential-remote-code-execution/

**Links in post:** https://blog.ryotak.me/post/pypi-potential-remote-code-execution/


### Thread part 7 — @ryotkak — 2021-08-08 00:02 UTC (2021-08-08 01:02 WAT)

- URL: https://x.com/ryotkak/status/1424158990758342656
- Metrics (at fetch): not returned

> TypeScriptのエコシステムを侵害し、VSCodeやAngular、TypeScript本体などを含む多数のプロジェクトに影響を及ぼすことが出来たDefinitely Typedの脆弱性の話です。
> https://blog.ryotak.me/post/definitelytyped-tamper-with-arbitrary-packages/

**Links in post:** https://blog.ryotak.me/post/definitelytyped-tamper-with-arbitrary-packages/


### Thread part 8 — @ryotkak — 2021-11-30 13:13 UTC (2021-11-30 14:13 WAT)

- URL: https://x.com/ryotkak/status/1465670240751087625
- Metrics (at fetch): bookmark 8, impression 0, like 63, quote 1, reply 0, retweet 20

> Denoのレジストリを侵害し、インストールスクリプトを含むDenoのモジュールを改竄できた脆弱性の話です。
> https://t.co/G7lJdKn7R8


---

## 2021-10-29 · Thread · 報告しました https://t.co/h9JLcc1S3y


### Post — @ryotkak — 2021-10-29 06:23 UTC (2021-10-29 07:23 WAT)

- URL: https://x.com/ryotkak/status/1453970848679804929
- Metrics (at fetch): bookmark 13, impression 0, like 175, quote 0, reply 2, retweet 23

> 報告しました https://t.co/h9JLcc1S3y

**Quoted post** 1453919776565198861: not readable via the API (deleted, private, or withheld).


### Thread part 2 — @ryotkak — 2021-11-05 00:38 UTC (2021-11-05 01:38 WAT)

- URL: https://x.com/ryotkak/status/1456420717243682816
- Metrics (at fetch): bookmark 3, impression 0, like 22, quote 0, reply 1, retweet 1

> 報告しました v2
>
> https://t.co/X6WzQwtwgo
> https://t.co/Dt3zTt5I1H

**Quoted post** 1456325640899137537: not readable via the API (deleted, private, or withheld).


### Thread part 3 — @ryotkak — 2021-11-12 12:38 UTC (2021-11-12 13:38 WAT)

- URL: https://x.com/ryotkak/status/1459138463345770496
- Metrics (at fetch): bookmark 1, impression 0, like 10, quote 0, reply 0, retweet 0

> 報告しました v3
> https://t.co/C2lGfnMu38


---

## 2021-10-20 · Thread · Minecraft speedrun Any% ACE (Arbitrary Code Execution) 00:00:37.130 https://youtu.be/1SE_fDXvTZ8 @Yo


Tags (automatic): RCE


### Post — @ryotkak — 2021-10-20 10:07 UTC (2021-10-20 11:07 WAT)

- URL: https://x.com/ryotkak/status/1450765590604312584
- Metrics (at fetch): not returned

> Minecraft speedrun Any% ACE (Arbitrary Code Execution) 00:00:37.130 https://youtu.be/1SE_fDXvTZ8 @YouTubeより

**Links in post:** https://youtu.be/1SE_fDXvTZ8


### Thread part 2 — @ryotkak — 2021-10-20 10:07 UTC (2021-10-20 11:07 WAT)

- URL: https://x.com/ryotkak/status/1450765665829212166
- Metrics (at fetch): bookmark 0, impression 0, like 4, quote 0, reply 0, retweet 0

> よくわからないことを昨日の夜やっていました


---

## 2021-10-19 · Post · これ、多分情報出してなかったと思うんですが、実は高校生です


### Post — @ryotkak — 2021-10-19 04:15 UTC (2021-10-19 05:15 WAT)

- URL: https://x.com/ryotkak/status/1450314661790838785
- Metrics (at fetch): not returned

> これ、多分情報出してなかったと思うんですが、実は高校生です


---

## 2021-10-06 · Post · CODE BLUE、ちょっとだけ出ます (初めてのインタビューだったのでレビューはお手柔らかにお願いします...)


### Post — @ryotkak — 2021-10-06 05:52 UTC (2021-10-06 06:52 WAT)

- URL: https://x.com/ryotkak/status/1445628001689817090
- Metrics (at fetch): not returned

> CODE BLUE、ちょっとだけ出ます (初めてのインタビューだったのでレビューはお手柔らかにお願いします...)


---

## 2021-09-16 · Post · バグバウンティで記念品として貰えるTシャツ、貰えるのは嬉しいんだけどハンガーが足りなくなるのでハンガーも一緒に送って欲しくなってきた


### Post — @ryotkak — 2021-09-16 03:26 UTC (2021-09-16 04:26 WAT)

- URL: https://x.com/ryotkak/status/1438343415087788036
- Metrics (at fetch): not returned

> バグバウンティで記念品として貰えるTシャツ、貰えるのは嬉しいんだけどハンガーが足りなくなるのでハンガーも一緒に送って欲しくなってきた


---

## 2021-09-10 · Post · Hello from OAuth2.0!


Tags (automatic): OAuth


### Post — @ryotkak — 2021-09-10 04:12 UTC (2021-09-10 05:12 WAT)

- URL: https://x.com/ryotkak/status/1436180741432307726
- Metrics (at fetch): not returned

> Hello from OAuth2.0!


---

## 2021-09-10 · Post · 読み/書き/DMとかいう大雑把すぎる権限管理からようやく抜け出せる


### Post — @ryotkak — 2021-09-10 03:59 UTC (2021-09-10 04:59 WAT)

- URL: https://x.com/ryotkak/status/1436177417077284868
- Metrics (at fetch): not returned

> 読み/書き/DMとかいう大雑把すぎる権限管理からようやく抜け出せる


---

## 2021-08-08 · Post · I published an article about a vulnerability in Definitely Typed that could be used to compromise th


### Post — @ryotkak — 2021-08-08 00:02 UTC (2021-08-08 01:02 WAT)

- URL: https://x.com/ryotkak/status/1424159111394959363
- Metrics (at fetch): not returned

> I published an article about a vulnerability in Definitely Typed that could be used to compromise the TypeScript ecosystem, potentially affecting many projects such as VSCode, Angular, or TypeScript itself.
> https://blog.ryotak.me/post/definitelytyped-tamper-with-arbitrary-packages-en/

**Links in post:** https://blog.ryotak.me/post/definitelytyped-tamper-with-arbitrary-packages-en/


---

## 2021-08-04 · Post · MSRC 2021 Most Valuable Security Researcherの一人に選ばれました https://twitter.com/msftsecresponse/status/142


### Post — @ryotkak — 2021-08-04 23:56 UTC (2021-08-05 00:56 WAT)

- URL: https://x.com/ryotkak/status/1423070349848039426
- Metrics (at fetch): not returned

> MSRC 2021 Most Valuable Security Researcherの一人に選ばれました https://twitter.com/msftsecresponse/status/1422958166258569218

**Links in post:** https://twitter.com/msftsecresponse/status/1422958166258569218

**Quoted post (full text):**

    #### Quoted post — @116285769 — 2021-08-04 16:30 UTC (2021-08-04 17:30 WAT)
    
    - URL: https://x.com/116285769/status/1422958166258569218
    - Metrics (at fetch): not returned
    
    > Congratulations to our MSRC 2021 Most Valuable Security Researchers! Thank you to all the researchers who have helped secure our customers. Check out our blog for the full list: https://msrc-blog.microsoft.com/2021/08/04/congratulations-to-the-msrc-2021-most-valuable-security-researchers/
    
    **Links in post:** https://msrc-blog.microsoft.com/2021/08/04/congratulations-to-the-msrc-2021-most-valuable-security-researchers/
    


---

## 2021-07-30 · Post · I published an article about a potential remote code execution in PyPI (Python's Package Registry) t


Tags (automatic): RCE


### Post — @ryotkak — 2021-07-30 12:00 UTC (2021-07-30 13:00 WAT)

- URL: https://x.com/ryotkak/status/1421078179226087428
- Metrics (at fetch): not returned

> I published an article about a potential remote code execution in PyPI (Python's Package Registry) that could allow an attacker to compromise the ecosystem of Python.
>
> https://blog.ryotak.me/post/pypi-potential-remote-code-execution-en/

**Links in post:** https://blog.ryotak.me/post/pypi-potential-remote-code-execution-en/


---

## 2021-07-21 · Thread · この脆弱性(CVE-2021-35054)に関して、色々と誤解を生みそうなので訂正しておくと、攻撃を成立させるにはサーバーが"online-mode=false"で実行されており、かつBungeeCo


### Post — @ryotkak — 2021-07-21 13:37 UTC (2021-07-21 14:37 WAT)

- URL: https://x.com/ryotkak/status/1417841274464313348
- Metrics (at fetch): not returned

> この脆弱性(CVE-2021-35054)に関して、色々と誤解を生みそうなので訂正しておくと、攻撃を成立させるにはサーバーが"online-mode=false"で実行されており、かつBungeeCord等のプロキシ等でセッションの有効性を確認していない等の条件を満たす必要があります。 https://twitter.com/madonomori/status/1417780096593661954

**Links in post:** https://twitter.com/madonomori/status/1417780096593661954

**Quoted post (full text):**

    #### Quoted post — @45548519 — 2021-07-21 09:34 UTC (2021-07-21 10:34 WAT)
    
    - URL: https://x.com/45548519/status/1417780096593661954
    - Metrics (at fetch): not returned
    
    > 「Minecraft」のJava版にディレクトリトラバーサルの脆弱性 ～JVNが注意喚起／正式版では未修正。「Spigot」「Minecraft Forge」の最新版で回避可能 https://forest.watch.impress.co.jp/docs/news/1339792.html [pic.x.com/EzEhuXOYoV]
    
    **Media:**
    - media `3_1417780090717442051` (details not returned by the API)
    
    **Links in post:** https://forest.watch.impress.co.jp/docs/news/1339792.html
    


### Thread part 2 — @ryotkak — 2021-07-21 13:40 UTC (2021-07-21 14:40 WAT)

- URL: https://x.com/ryotkak/status/1417841934807101442
- Metrics (at fetch): not returned

> 現状一番詳しく情報がまとまってるのは僕が個人的に運用しているアドバイザリ公開用のサイト
> https://vuln.ryotak.me/advisories/55
> (微熱があるので文章が少しおかしいのは許してください...)

**Links in post:** https://vuln.ryotak.me/advisories/55


---

## 2021-07-16 · Post · I published an article about remote code execution in cdnjs that could allow tampering of 12.7% of a


Tags (automatic): RCE


### Post — @ryotkak — 2021-07-16 00:00 UTC (2021-07-16 01:00 WAT)

- URL: https://x.com/ryotkak/status/1415823546870165505
- Metrics (at fetch): not returned

> I published an article about remote code execution in cdnjs that could allow tampering of 12.7% of all websites on the internet.
> https://blog.ryotak.me/post/cdnjs-remote-code-execution-en/

**Links in post:** https://blog.ryotak.me/post/cdnjs-remote-code-execution-en/


---

## 2021-05-24 · Post · Terrariaの脆弱性報告しました(？) https://t.co/hNzSSqMKN7


### Post — @ryotkak — 2021-05-24 23:47 UTC (2021-05-25 00:47 WAT)

- URL: https://x.com/ryotkak/status/1396976226355474433
- Metrics (at fetch): not returned

> Terrariaの脆弱性報告しました(？) https://t.co/hNzSSqMKN7

**Quoted post (full text):**

    #### Quoted post — @CVEnew — 2021-05-24 13:45 UTC (2021-05-24 14:45 WAT)
    
    - URL: https://x.com/CVEnew/status/1396824669991448585
    - Metrics (at fetch): not returned
    
    > CVE-2021-32075 Re-Logic Terraria before 1.4.2.3 performs Insecure Deserialization. https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32075
    
    **Links in post:** https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-32075
    


---

## 2021-05-11 · Post · Microsoftに報告してたVSCodeのRCEが更に2個修正されてた


### Post — @ryotkak — 2021-05-11 23:43 UTC (2021-05-12 00:43 WAT)

- URL: https://x.com/ryotkak/status/1392264023618379779
- Metrics (at fetch): not returned

> Microsoftに報告してたVSCodeのRCEが更に2個修正されてた
> CVE-2021-31211
> CVE-2021-31214


---

## 2021-04-29 · Post · Git for CygwinのCloneした時に刺さる任意コード実行です。


### Post — @ryotkak — 2021-04-29 23:07 UTC (2021-04-30 00:07 WAT)

- URL: https://x.com/ryotkak/status/1387906383056568320
- Metrics (at fetch): not returned

> Git for CygwinのCloneした時に刺さる任意コード実行です。
> アップストリーム(git/git)には修正が入っていないのでCygwin上でgitのセルフビルドをするのはやめたほうがいいです。 https://twitter.com/CVEnew/status/1387885772506861569

**Links in post:** https://twitter.com/CVEnew/status/1387885772506861569

**Quoted post (full text):**

    #### Quoted post — @CVEnew — 2021-04-29 21:45 UTC (2021-04-29 22:45 WAT)
    
    - URL: https://x.com/CVEnew/status/1387885772506861569
    - Metrics (at fetch): not returned
    
    > CVE-2021-29468 Cygwin Git is a patch set for the git command line tool for the cygwin environment. A specially crafted repository that contains symbolic links as well as files with backslash characters in the file name may cause just-checked out code to... https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29468
    
    **Links in post:** https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-29468
    


---

## 2021-04-21 · Post · ここ数日間Homebrewの他にもう一個インシデント対応してたからめちゃくちゃ忙しかった...


### Post — @ryotkak — 2021-04-21 11:53 UTC (2021-04-21 12:53 WAT)

- URL: https://x.com/ryotkak/status/1384837760561913856
- Metrics (at fetch): not returned

> ここ数日間Homebrewの他にもう一個インシデント対応してたからめちゃくちゃ忙しかった...


---

## 2021-04-21 · Post · I wrote an article about a recent security incident on Homebrew which allowed me to execute arbitrar


### Post — @ryotkak — 2021-04-21 11:11 UTC (2021-04-21 12:11 WAT)

- URL: https://x.com/ryotkak/status/1384827217876750338
- Metrics (at fetch): not returned

> I wrote an article about a recent security incident on Homebrew which allowed me to execute arbitrary codes on the users' machine. https://twitter.com/ryotkak/status/1384827136368775169

**Links in post:** https://twitter.com/ryotkak/status/1384827136368775169

**Quoted post (full text):**

    #### Quoted post — @ryotkak — 2021-04-21 11:11 UTC (2021-04-21 12:11 WAT)
    
    - URL: https://x.com/ryotkak/status/1384827136368775169
    - Metrics (at fetch): not returned
    
    > HomebrewのCaskリポジトリを侵害し、Homebrewを利用しているユーザーのコンピューター上で任意のコードを実行できた脆弱性の話です。
    > 公式インシデント報告: https://brew.sh/2021/04/21/security-incident-disclosure/
    > Blog (English): https://blog.ryotak.me/post/homebrew-security-incident-en/
    > ブログ (日本語): https://blog.ryotak.me/post/homebrew-security-incident/
    
    **Links in post:** https://brew.sh/2021/04/21/security-incident-disclosure/, https://blog.ryotak.me/post/homebrew-security-incident-en/, https://blog.ryotak.me/post/homebrew-security-incident/
    


---

## 2021-04-16 · Post · Microsoftの2021年第1四半期リーダーボード、トップ10入りしてた


### Post — @ryotkak — 2021-04-16 08:45 UTC (2021-04-16 09:45 WAT)

- URL: https://x.com/ryotkak/status/1382978481034723329
- Metrics (at fetch): not returned

> Microsoftの2021年第1四半期リーダーボード、トップ10入りしてた
> https://msrc-blog.microsoft.com/2021/04/15/congratulating-our-top-msrc-2021-q1-security-researchers/

**Links in post:** https://msrc-blog.microsoft.com/2021/04/15/congratulating-our-top-msrc-2021-q1-security-researchers/


---

## 2021-04-14 · Post · VSCode 1.55.2、変更点が全部僕が報告した脆弱性を修正するためのもので、ちょっと嬉しくなった


### Post — @ryotkak — 2021-04-14 00:21 UTC (2021-04-14 01:21 WAT)

- URL: https://x.com/ryotkak/status/1382126825011236869
- Metrics (at fetch): not returned

> VSCode 1.55.2、変更点が全部僕が報告した脆弱性を修正するためのもので、ちょっと嬉しくなった


---

## 2021-04-14 · Thread · 今日開示されたやつ、VSCodeのRCEが5個だった


### Post — @ryotkak — 2021-04-14 00:11 UTC (2021-04-14 01:11 WAT)

- URL: https://x.com/ryotkak/status/1382124429350608897
- Metrics (at fetch): not returned

> 今日開示されたやつ、VSCodeのRCEが5個だった
> 1. CVE-2021-28477
> 2. CVE-2021-28457
> 3. CVE-2021-28475
> 4. CVE-2021-28473
> 5. CVE-2021-28469


### Thread part 2 — @ryotkak — 2021-04-14 00:12 UTC (2021-04-14 01:12 WAT)

- URL: https://x.com/ryotkak/status/1382124565862633473
- Metrics (at fetch): not returned

> ついでにVSCodeの拡張機能のRCEも2個報告してた
> 1. CVE-2021-28470
> 2. CVE-2021-28471


---

## 2021-03-18 · Post · QiitaにXSS報告しました https://twitter.com/CVEnew/status/1372590038324813833


### Post — @ryotkak — 2021-03-18 23:55 UTC (2021-03-19 00:55 WAT)

- URL: https://x.com/ryotkak/status/1372698286373576704
- Metrics (at fetch): not returned

> QiitaにXSS報告しました https://twitter.com/CVEnew/status/1372590038324813833

**Links in post:** https://twitter.com/CVEnew/status/1372590038324813833

**Quoted post (full text):**

    #### Quoted post — @CVEnew — 2021-03-18 16:45 UTC (2021-03-18 17:45 WAT)
    
    - URL: https://x.com/CVEnew/status/1372590038324813833
    - Metrics (at fetch): not returned
    
    > CVE-2021-28796 Increments Qiita::Markdown before 0.33.0 allows XSS in transformers. https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28796
    
    **Links in post:** https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-28796
    


---

## 2021-03-16 · Post · MarkdownからGoogle Slidesに変換するやつ、Googleが作ってくれてるの知らなかった


### Post — @ryotkak — 2021-03-16 13:50 UTC (2021-03-16 14:50 WAT)

- URL: https://x.com/ryotkak/status/1371821248175435779
- Metrics (at fetch): not returned

> MarkdownからGoogle Slidesに変換するやつ、Googleが作ってくれてるの知らなかった
> https://github.com/googleworkspace/md2googleslides

**Links in post:** https://github.com/googleworkspace/md2googleslides


---

## 2021-02-27 · Post · メルカリに脆弱性報告して色々もらった


### Post — @ryotkak — 2021-02-27 05:18 UTC (2021-02-27 06:18 WAT)

- URL: https://x.com/ryotkak/status/1365531806330544129
- Metrics (at fetch): not returned

> メルカリに脆弱性報告して色々もらった
> https://about.mercari.com/security/vulnerability/ [pic.x.com/7xdebsbZ9e]

**Media:**
- photo: https://pbs.twimg.com/media/EvNX6etVgAQ6jTw.jpg — no alt text provided by author

**Links in post:** https://about.mercari.com/security/vulnerability/


---

## 2021-01-20 · Thread · 報告してたGoの脆弱性が修正されてました。


### Post — @ryotkak — 2021-01-20 01:11 UTC (2021-01-20 02:11 WAT)

- URL: https://x.com/ryotkak/status/1351698751098818560
- Metrics (at fetch): not returned

> 報告してたGoの脆弱性が修正されてました。
> CVE-2020-27955の概要読んで絶対Go自体も影響受けるなと思ってコード読んでる時に見つけたやつです。 https://twitter.com/golang/status/1351673649850421249

**Links in post:** https://twitter.com/golang/status/1351673649850421249

**Quoted post (full text):**

    #### Quoted post — @113419064 — 2021-01-19 23:31 UTC (2021-01-20 00:31 WAT)
    
    - URL: https://x.com/113419064/status/1351673649850421249
    - Metrics (at fetch): not returned
    
    > Go 1.15.7 and 1.14.14 have been released!
    >
    > A security fix for cmd/go (CVE-2021-3115),
    > and crypto/elliptic (CVE-2021-3114)
    >
    > Announcement: https://groups.google.com/g/golang-announce/c/mperVMGa98w
    >
    > Download: https://golang.org/dl/#go1.15.7
    >
    > #golang
    
    **Links in post:** https://groups.google.com/g/golang-announce/c/mperVMGa98w, https://golang.org/dl/#go1.15.7
    


### Thread part 2 — @ryotkak — 2021-01-20 01:26 UTC (2021-01-20 02:26 WAT)

- URL: https://x.com/ryotkak/status/1351702516610654212
- Metrics (at fetch): not returned

> ちなみになんですが、明示的にドキュメントに書かれていないだけで同じような実行可能ファイルの検索をする言語は結構あります


---

## 2021-01-14 · Post · 公開されてました。Git LFSのRCEです:


### Post — @ryotkak — 2021-01-14 10:58 UTC (2021-01-14 11:58 WAT)

- URL: https://x.com/ryotkak/status/1349672283325964291
- Metrics (at fetch): not returned

> 公開されてました。Git LFSのRCEです:
> https://github.com/git-lfs/git-lfs/security/advisories/GHSA-cx3w-xqmc-84g5

**Links in post:** https://github.com/git-lfs/git-lfs/security/advisories/GHSA-cx3w-xqmc-84g5


---

## 2020-10-09 · Post · 書きました


### Post — @ryotkak — 2020-10-09 09:17 UTC (2020-10-09 10:17 WAT)

- URL: https://x.com/ryotkak/status/1314495176665038849
- Metrics (at fetch): not returned

> 書きました
> https://blog.ryotak.me/post/twitter-list-chain/

**Links in post:** https://blog.ryotak.me/post/twitter-list-chain/


---

## 2019-12-10 · Post · 報告してたやつ


### Post — @ryotkak — 2019-12-10 05:04 UTC (2019-12-10 06:04 WAT)

- URL: https://x.com/ryotkak/status/1204265665290391553
- Metrics (at fetch): not returned

> 報告してたやつ
> Kinza におけるクロスサイトスクリプティングの脆弱性
> https://jvn.jp/jp/JVN63047298/

**Links in post:** https://jvn.jp/jp/JVN63047298/


---

## 2019-11-30 · Post · .@V_Melville さんにアイコンを描いていただきました！ありがとうございます！


### Post — @ryotkak — 2019-11-30 00:56 UTC (2019-11-30 01:56 WAT)

- URL: https://x.com/ryotkak/status/1200579220717502464
- Metrics (at fetch): not returned

> .@V_Melville さんにアイコンを描いていただきました！ありがとうございます！
> #新しいプロフィール画像 [pic.x.com/8DJGKHH5z3]

**Media:**
- photo: https://pbs.twimg.com/media/EKlQb2-U8AAKt0w.jpg — no alt text provided by author


---

## 2019-05-29 · Post · CVE取得した


### Post — @ryotkak — 2019-05-29 00:49 UTC (2019-05-29 01:49 WAT)

- URL: https://x.com/ryotkak/status/1133535728468578304
- Metrics (at fetch): not returned

> CVE取得した
