# i HACKED nasa in just 4 days

- **Source URL:** https://medium.com/@choudharyyash127/i-hacked-nasa-in-just-4-days-1fb93bed2fd7
- **Fetched from:** https://medium.com/@choudharyyash127/i-hacked-nasa-in-just-4-days-1fb93bed2fd7?source=rss-7e72ac271915------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14955 (id 14955)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** yash  / Wed, 21 Oct 2026 22:34:59 GMT

*4 days of persistence, multiple rejections, and one lesson I will never forget.*

Let me tell you a story about my first week of bug hunting on NASA’s Vulnerability Disclosure Program.

I started with excitement, motivation, and the confidence of someone who had watched a few bug bounty videos and thought:

**“How hard can it be? Find a bug, write a report, get rewarded. Easy!”**

Narrator: *It was not easy.* 💀

I started hunting on NASA’s VDP, exploring the target and looking for security issues.

And guess what?

Within just **two hours, I found my first bug!**

I was excited. My brain had already started celebrating.

*“That’s it! My bug bounty journey with NASA has officially begun!”*

Then came the verdict.

**P5.**

My happiness went from 🚀 to 🪦 in approximately three seconds.

I stared at the screen like NASA had personally rejected my career.

But I told myself, “Okay, Yash. First attempt. Learn and move on.”

I came back the next day with fresh motivation.

This time, I found an issue that allowed me to manipulate the view counter on a post through repeated HTTP requests.

I thought, “Interesting! Let’s document this properly and see what happens.”

I submitted the report.

And then…

**P5. AGAIN.**

At this point, I started wondering whether P5 was NASA’s way of saying, “Thanks for participating.” 😂

Still, I wasn’t ready to quit.

The next day, I discovered what appeared to be an email ID and password exposed on a NASA page’s error response.

Now, I thought this could be more serious.

I documented the finding and submitted another report.

The response?

**P5 — and Duplicate.**

BRO. 😭

Not only was the severity low, but someone had apparently found the same issue before me.

My brain started running its own incident response:

I was frustrated, but I kept going.

I decided to investigate another domain connected to NASA.

During my research, I discovered a potential stored XSS vulnerability on a website associated with NASA.

I carefully reported it, hoping this would finally be the one.

Then came the verdict:

**Out of Scope.**

At that moment, my bug-hunting journey felt like a relationship.

I kept putting in the effort, but the target kept telling me we weren’t compatible. 💀😂

Four days of hunting, multiple reports, and no result I was hoping for.

I was genuinely disappointed.

I started thinking, “Maybe I should stop wasting time on this target and move on.”

But then I had one more thought.

**What if I haven’t failed? What if I just haven’t found the right vulnerability yet?**

That thought changed everything.

Instead of blindly searching for more vulnerabilities, I decided to change my approach.

I spent around three hours studying the Vulnerability Rating Taxonomy (VRT) and thinking more carefully about what makes a security finding meaningful.

I started focusing on the difference between simply discovering something unusual and demonstrating a genuine security impact.

Then I went back to my reconnaissance.

This time, I tried to be more methodical, looking more deeply at the target’s exposed resources and configuration.

And then I found something interesting.

**Sensitive data exposure and an insecure directory exposure.**

I investigated the finding, collected evidence, and prepared a report explaining what I had discovered.

I submitted it.

Then began the hardest part of bug hunting:

**Waiting.**

Five hours passed.

I checked the submission.

Refreshed the page.

Checked again.

Refreshed again.

At this point, I was probably generating more requests to the dashboard than I had during my actual testing. 😂

The status changed.

**Triaged. P4.**

I finally had a valid P4 report on NASA’s VDP!

\<figure> \<img src=”” alt=””/> \</figure>

After all those P5s, the duplicate, and the out-of-scope finding, seeing that valid report felt incredible.

Just when I thought getting a valid P4 was the highlight of my journey, something else made the experience even more special.

**I also got recognized in NASA’s Hall of Fame!** 🤯🔥

Let that sink in for a moment.

A few days earlier, I was sitting there collecting P5s, dealing with duplicates, and getting out-of-scope verdicts. I was literally questioning my approach.

And now? I had a valid P4 report and Hall of Fame recognition associated with NASA.

From *“Maybe bug hunting isn’t for me”* to *“WAIT… I’M IN NASA’S HALL OF FAME?”* 😂

Looking back, I learned some important lessons.

**1. A P5 doesn’t mean you’re a bad hacker.**

A report can be technically correct but have limited security impact. Learn how to demonstrate impact instead of focusing only on finding something unusual.

**2. Duplicates are part of the game.**

Someone else finding the same issue first doesn’t mean your research was useless. It means you need to keep exploring and develop your own methodology.

**3. Out of scope means out of scope.**

A vulnerability on a related domain isn’t automatically eligible for a program. Always check the exact scope and rules before testing.

**4. Read the VRT before chasing severity.**

Understanding how vulnerabilities are classified helps you write stronger reports, assess realistic impact, and prioritize meaningful findings.

**5. Persistence matters, but so does working smarter.**

Repeating the same approach isn’t always the answer. Sometimes you need to stop, study, rethink your methodology, and return with a better plan.

**6. Don’t measure your progress only by severity.**

A P4 feels great, but every properly investigated finding can teach you something. Focus on improving your technical skills and report quality.

My first week with NASA looked something like this:

If bug hunting were a video game, I would have spent four days fighting the tutorial boss before unlocking the actual mission.

But I learned something more valuable than a status label.

**The difference between giving up and getting better is often what you do after your first few failures.**

To anyone starting their bug bounty journey, especially beginners like me, don’t expect every report to be a critical vulnerability.

You will find low-severity issues. You will encounter duplicates. Some findings will be out of scope. Sometimes, you will spend hours researching something that doesn’t become a valid report.

That’s part of the process.

Read the program policy. Understand the scope. Learn the VRT. Document your findings carefully. Prove impact responsibly. And never forget that persistence works best when combined with knowledge.

I’m still learning, still improving, and still hunting.

This is only the beginning.

**One valid report won’t make you an expert, and a few rejected reports won’t make you a failure.**

Keep learning. Keep improving. Keep believing in yourself.

And remember:

*The bug might be P5, the report might be a duplicate, and the next target might be out of scope.*

*But your learning journey? That should never be out of scope.* 😂🚀

#BugBounty #CyberSecurity #NASA #EthicalHacking #VulnerabilityResearch #InfoSec #BugHunting
