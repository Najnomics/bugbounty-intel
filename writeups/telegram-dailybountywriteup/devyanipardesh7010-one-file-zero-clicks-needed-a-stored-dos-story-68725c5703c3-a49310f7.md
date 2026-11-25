# One File, Zero Clicks Needed

- **Source URL:** https://medium.com/@devyanipardesh7010/one-file-zero-clicks-needed-a-stored-dos-story-68725c5703c3
- **Fetched from:** https://medium.com/@devyanipardesh7010/one-file-zero-clicks-needed-a-stored-dos-story-68725c5703c3?source=rss-d191fcb32625------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14947 (id 14947)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Devyani Pardeshi / Wed, 14 Oct 2026 06:17:30 GMT

Hi everyone, I’m Devyani — and this is the story of my first bug.

I used to look at other researchers’ reports and wonder, *how do people even find this stuff?* I’d tried like so many times , and all i used to got was ? A “Informative” , a “Duplicate.” and rest “NA” That’s it. It was frustrating enough that I took a break from bug hunting altogether — I was tired of staring at requests until they blurred together in my sleep.

Eventually I came back, no expectations, nothing to lose.

I found a diagramming tool that let users upload custom shape libraries as SVG files. Harmless enough, right? Except SVGs are secretly just XML wearing a trench coat, and XML has a party trick called entity expansion — nicknamed the “Billion Laughs” attack. (Yes, that’s really the name.)

So I uploaded one. Saved the diagram. And then:

The screen just… kept loading.

1 minute — still loading.

5 minutes — still loading.

1 hour — *still loading.*

That’s when it clicked: oh. This is interesting.

The file wasn’t malicious in the “steals your password” sense — it was malicious in the “asks the server to do an impossible amount of work and never stops” sense. A few hundred bytes of XML that the parser dutifully tried to expand into something enormous, forever. Nothing was hacked. The backend was just exhausted.

I set up two accounts: a low-privilege collaborator with basic edit access, and a high-privilege owner. The collaborator uploaded the SVG into the diagram’s custom library and dragged it onto the canvas. Diagram wouldn’t load — expected.

Then I logged back in as the owner, who’d never touched the malicious file, and opened the same diagram.

Also stuck. Also spinning.

That’s when I realized this wasn’t a “break my own session” bug — it was *stored*. One low-privilege collaborator had planted something that would hang the diagram for anyone who opened it, indefinitely, with zero further effort. One file. Zero clicks. Maximum chaos.

Imagine a team that relies on these diagrams for architecture docs. One day the page won’t load. People blame their wifi, then their laptop, then eventually file a ticket — and IT spends an afternoon confused, because nothing looks “broken.” The backend is just stuck, forever, resolving a file that looks like a boring little icon.

I reported it. It got triaged. I followed up once, and fix is now in progress, and I walked away with my first paid bounty — $300 — for a file that’s basically angry XML throwing a tantrum.

If your app lets people upload SVGs and the parser doesn’t explicitly disable external entity resolution, you don’t have an image upload feature — you have a Trojan horse delivery service with extra steps.

And if you’ve tried bug hunting a few times and all you’ve gotten back is “Informative” and “Duplicate” — don’t quit. Sometimes all it takes is one oddly-named XML bomb and a lot of stubbornness.

❤
