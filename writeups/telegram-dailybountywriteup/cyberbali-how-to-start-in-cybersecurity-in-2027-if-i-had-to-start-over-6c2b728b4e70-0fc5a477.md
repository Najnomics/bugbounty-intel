# How to Start in Cybersecurity in 2027 (If I Had to Start Over)

- **Source URL:** https://medium.com/@cyberbali/how-to-start-in-cybersecurity-in-2027-if-i-had-to-start-over-6c2b728b4e70
- **Fetched from:** https://medium.com/feed/@cyberbali
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14985 (id 14985)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
#### Cybersecurity is a skill you cannot buy your way into, it has to be built. It’s the alpha of software engineering — the part that decides whether everything else survives. This guide helps you through each step you need to take to crack the code — without breaking the bank !

A while ago I interviewed a few candidates from a well-known postgraduate cybersecurity program as a favor to a friend. They were smart, polite and clearly hardworking. They had also paid a lot of money and spent a lot of months on that program.

Then I asked a practical question: “I am a business owner who runs a coffee shop. I am hiring you to probe my application’s weaknesses. How would you approach this assignment — detail me the steps”. Most of them went quiet.

I want to be clear that this wasn’t their fault. They did what they were told. They studied the syllabus, passed the exams and collected the certificate. Nobody told them the one thing that matters most in this field: **security is a craft, and a craft is learned with your hands.**

This article is for the people who are where those candidates were: smart, motivated, a little anxious, and about to spend money and months on a path that may not get them where they want to go.

It’s my honest attempt to show a cheaper, faster and more fun way.

### First, what this article is (and isn’t)

Cybersecurity is huge. There are SOC analysts, threat hunters, forensics people, GRC consultants, malware analysts, cloud security architects, and many more. I have not worked in all of them, and I won’t pretend I have.

I’m writing from what I’ve actually done: **application and API security, offensive testing, and secure software engineering.** That’s the lane I know. If you’re curious about SOC, GRC or forensics, talk to people who live there. They’ll give you better advice than I can, and I’ll gladly send you to them.

But if you are starting a fresh, then all those specialization would be futile — what I am about to tell you is the bedrock that will eventually take you there.

### The idea: the builder’s eye and the breaker’s hands

Security has two hands:

- **The builder’s hand** designs and ships software that holds up under pressure. This is security engineering: requirements, design, secure coding, testing, monitoring.
- **The breaker’s hand** proves, with evidence, where software fails. This is offensive security: finding weaknesses and showing how they’re exploited.

You don’t pick a side forever. You pick where to start, and you end up using both.

Security engineering principles are the core of all security around us: least privilege, defense in depth, validating input, separating trust boundaries, failing safely.

Offensive security is what happens when someone misses those principles, and someone else gets to exploit the gap.

If you only break things, you’ll learn tricks. If you only build, you’ll never know whether your defenses work. Do both and each hand teaches the other.

### Before you commit to jumping in !

This isn’t a listicle you can skim for the “top 10 tools” and leave. Every section leans on the one before it. The path in the first half only makes sense once you’ve seen the two-hands idea, and the lessons on certifications and community near the end explain why the path is built the way it is.

If you jump straight to the resource list, you’ll walk away with a list of links. If you read to the end, you’ll get the reasoning behind them, and that’s the part that lets you adapt this plan to your own laptop, budget and timeline.

So please stay till the last section. Keep a notebook or a text file open, maybe a cup of chai, and treat this as a conversation, not a lecture.

Now, let’s start from Step 0.

### Step 0: Learn to write code (gently)

Many people who come into security aren’t developers, and that’s fine. But I want to be honest about one thing: **learning to write code first is the biggest difference-maker I’ve seen.**

You don’t need to become a software engineer. You need to read the thing you’re attacking or defending. When you can read code, a vulnerability stops being a magic trick and becomes an obvious consequence of a decision someone made.

If you already work as a developer, you’re ahead. You understand how software gets built and where shortcuts hide. Use that.

If you don’t code yet, start small:

- Learn Python basics: variables, loops, functions, files, HTTP requests, JSON.
- Learn the Linux command line well enough to live in it.
- Build one tiny web API with a login (Flask or FastAPI is plenty), run it locally, and keep it. You’ll attack and defend it later, and it’ll teach you more than a month of lectures.

Don’t worry about writing beautiful code. Write code that runs and that you understand.

### Step 1: Knowledge before tools

Before you touch a hacking tool, get the fundamentals in your head. My go-to recommendation is Professor Messer’s free [Network+](https://www.youtube.com/watch?v=k7IOn3TiUc8&list=PLG49S3nxzAnl_tQe3kvnmeMid0mjF8Le8) and [Security+](https://www.youtube.com/watch?v=KiEptGbnEBc&list=PLG49S3nxzAnl4QDVqK-hOnoqcSKEIDDuv) video playlists. Find a lite weight Linux distro and have a go at it.

Notice what I said: *the knowledge, not the cert.* Those playlists are some of the clearest explanations of networking and security basics anywhere, and they’re free. Use them as a curriculum. Whether you ever sit the exam is a separate decision, and we’ll get to that.

Then check yourself. Before you move on to hacking platforms, you should be able to do these without notes:

- Explain, step by step, what happens when you type a URL and press Enter: DNS, TCP, TLS, HTTP.
- Read a raw HTTP request and explain every header.
- Explain the difference between authentication and authorization, and between a 401 and a 403.
- Work out how many hosts a /26 subnet holds.
- Move around a Linux system, read file permissions, and explain what a process is.

If you can’t do a few of these yet, you haven’t failed. You’ve found your next week’s homework.

### Step 2: Learn the craft with guided platforms

Once the basics are comfortable, move to a guided hands-on platform. They will cost you a little bit money — but trust me, the amount of time and burnout they will save you from would be worth it.

I usually point people to **TryHackMe** or **TCM Security**. Both have curated learning paths that teach the basics of hacking in a structured way, so you’re not lost in a sea of random tutorials.

Pick one and stay with it for a while. Don’t hop between five platforms in a month. Skips the certification offerings for now, just take the lessons.

TryHackMe — Do the PreSecurity, CyberSecurity 101, Jr Pentester, Security Engineer and Web Application pentesting paths.

The Cyber mentor — Go with the pen testing learning path.

### Step 3: Burning down Lanka — probing the weakness.

When you’ve finished a guided path and you’re drawn to the breaking side, it’s time to go off the rails (safely).

1. **Web Security Academy (PortSwigger).** It’s free and excellent. Work through the labs on injection, authentication, access control and SSRF.
2. **CTFs.** They’re fun, they build speed and they teach you to be stuck productively.
3. **Home labs.** Install vulnerable apps like OWASP Juice Shop or crAPI locally and attack them on your own machine.
4. **Look at how others do it.** Watch walkthroughs, read other people’s writeups, join discussions. You’ll learn techniques you’d never discover alone.

One rule: **try the challenge first.** Struggle with it, even for hours. Fire up your LLM and discuss the challenge with it (explicitly instruct it to only help you think and not answer). Then look into how others have solved it (read write-ups).

And when you finish, write it up. A write up forces you to understand what you did, not just that it worked. It also becomes proof of skill that no certificate can offer. Try for about ten CTFs or labs with a writeup for each, and then do one entirely on your own, with no walkthrough. All of these goes into your portfolio.

Make notes of all the tools and techniques you learn — end of this exercise should give you a “playbook” of your own. Which tools to use, when, what should be the parameters to pass and so on.

A note on ethics, because it matters: only test systems you own or have written permission to test — do not break into other’s homes howsoever cool it might sound — that’s a crime. Your lab is your playground. The internet isn’t.

### Step 4: Project Vishwakarma — Building the defenses

In Indian tradition, Vishwakarma is the divine architect, the builder behind the fortresses of the gods. I’ve borrowed his name for this step because designing defenses is the most fundamental responsibility of a security professional, and the one beginners skip most often. This is a must needed skill for a true master.

Offensive skills show you how things break. Engineering is how you stop them from breaking, and it’s the foundation everything else rests on. Building security into a product from the very first design decision is slow, demanding work, which is why we’ll learn it by building something real.

The best way I know to learn it is a project that walks through the entire secure software development lifecycle (SSDLC) from start to finish. Take a small application, maybe an API for a coffee shop, a notes app or a booking system, and take it through these stages:

- **Requirements.** Write down what the app must do, and also what it must never allow. Pull security requirements from a standard like OWASP ASVS. Think about abuse cases, not just use cases.
- **Design.** Draw a data flow diagram. Mark the trust boundaries. Do a simple threat model (STRIDE works fine for a first attempt). OWASP Threat Dragon could be a good tool to use.
- **Implementation.** Build it with secure defaults: proper authentication, authorization checks on every request, input validation, safe handling of secrets, and sensible dependencies. OWASP cheat-sheet is your friend here. You can use AI for this step.
- **Verification.** For every security requirement, write a test case. Add automated checks like SAST, dependency scanning and DAST. Then try to break it manually. OWASP WSTG will come handy.
- **Release and operations.** Add logging that would help you investigate an incident. Think about how you’d patch and how you’d notice an attack.

The end result I want you to have is a **list of implemented security requirements, each with test cases that prove it works.**

Here’s what one entry looks like:

- *Requirement:* a user can only view their own orders.
- *Design control:* the order service checks that the order belongs to the authenticated user on every request.
- *Test case:* log in as user A, request an order that belongs to user B, and expect a rejection. Do the same by changing the ID in different parts of the request.

If you can write fifty of these and show they pass, you’ve learned more about real security engineering than most courses teach.

### Do both, and cross-test

The best learning happens when the two hands meet. Build your secure app. Then swap with a friend. They attack yours, you attack theirs, and you each write a report.

You’ll find bugs in your own code that you were certain weren’t there. That moment is humbling, useful and surprisingly addictive.

### Why I say: start with web, or mobile

I’d encourage you to spend a good part of your first year on **web security or mobile security.** Here’s why:

- They are time-tested. The problems have been studied for years.
- There are a lot of resources to learn from and a lot of safe targets to practice on.
- The principles you learn there apply everywhere: trust boundaries, authentication and authorization, input handling, session management, secrets.

If you have to choose, web and API security is the easier starting point because it needs less setup and has more free labs. Mobile is a great second step or a strong choice if you have a particular interest, though it takes more effort to set up.

Whatever you pick, go deep. Strong principles first. You can apply them to other stacks later.

### Where you’ll meet the specializations anyway

When you start reading about cybersecurity, you’ll hear about cloud security, AI security, GRC and more. It’s easy to feel behind. Here’s the good news: you’ll meet these in the initial years anyway, inside the learning framework you’re already following.

- **Cloud security.** Your app has to run somewhere. Once you deploy your project, you’ll bump into identity and access management, network rules and misconfiguration. IAM is, in the end, authorization at scale.
- **AI security.** Most of the time it’s API security in disguise. An application takes untrusted input, passes it across a trust boundary to something that can take actions, and hopes for the best. That’s the same pattern behind injection and SSRF. If you understand web and API fundamentals, you’ll pick up the new details quickly.
- **GRC (governance, risk and compliance).** Remember your list of security requirements, mapped to test cases and evidence? An auditor would call that a control framework. You’ll already know how to build the evidence.

So here’s my honest advice: **don’t chase these yet.**

Pace yourself. Hold the fancy for the time when you’ve reached some milestones, say the ten write ups, the solo challenge and the SSDLC project. Even then, plan to spend a couple of years in your first career stage building depth before specializing.

Chasing every hot topic means you’ll be a beginner in five things instead of competent in one. Competence in one makes every other field easier.

### A fair word on certifications

This is the part I was most nervous to write, so let me be clear and fair.

**Certifications aren’t bad.** Some are thoughtfully designed, and some even have practical exams that test whether you can do the work. Some employers use them as a filter. If a particular job requires one, getting it can be a sensible, practical decision.

But in India especially, I see a pattern that worries me. A lot of young people believe a certificate is what makes you a hacker. It’s understandable. We come from a culture where an exam, a rank or a degree is the path to a good life. In security, though, it doesn’t work that way.

### The scam radar

Because there’s a lot of money in this space, there are also a lot of predatory programs. Before you pay for a course, especially an expensive one, check for these signs:

- Guaranteed placements or “job in 90 days” promises.
- “Become an ethical hacker” with no live labs.
- No public portfolios from past students: no write-ups, no GitHub, no blog posts.
- Assessments that are only multiple-choice questions.
- Pressure to pay now, offers that expire tonight, EMI schemes that make a large fee feel small.
- Trainers who can’t show their own practical work.

And here’s a simple test: **ask the program to show you three of its graduates’ public projects or write-ups.** A good program will be proud to. A weak one will change the subject.

You don’t need an expensive program to learn this. Everything in this article can be done with free or low-cost material and a laptop.

### Don’t walk alone

There’s one more thing that matters as much as any technical skill, and almost nobody talks about it: **people burn out fast in this field.**

The common traps are:

- Learning in isolation, with no one to ask.
- Comparing yourself to people who post only their wins.
- Grinding fourteen-hour days for a month and then collapsing.
- Feeling like an impostor because the field is endless and you can never know everything.
- Hoarding tutorials instead of building something.

The antidote isn’t a magic trick. It’s other humans.

- **Find a study partner or a small group.** Cross-test each other’s projects. Explain concepts out loud.
- **Show up to a community.** Local meetups like Null chapters and OWASP chapters are full of people who remember being beginners. Online, you’ll find communities like the Black Hills Information Security Discord, and places like r/AskNetsec where you can ask and answer questions.
- **Learn in public.** Share a write-up once a month. It doesn’t have to be perfect.
- **Ask good questions.** Say what you tried, what you expected and what happened. People love helping someone who has done the thinking.
- **Give back.** Answer one beginner’s question a week. Teaching is one of the fastest ways to learn.

There’s an old saying: if you want to go fast, go alone; if you want to go far, go together. Security is a long road, so take the second option.

### Closing

I’m not against certificates, courses or degrees. I’m against the belief that they can replace doing the work. Hands-on practice is the king of this field, and you can start today, for free, on your own laptop.

Build something. Break something. Write down what you learned. Share it with someone. Then do it again.

If you’re a beginner reading this, I’d love to hear where you’re starting from. And if you have a different path that worked for you, share it in the comments. We all learn faster that way.

### Let me pitch Cyberbali to you !

This is “The Cyberbali Brief” — A goldmine of knowledge on how to design secure software.

We write good stuff here. Knowledge that is acquired by building large scale enterprise solutions, stuff that could mean a world of difference to your cybersecurity wisdom.

**Do Subscribe. Find more about my work —** 

[https://cyberbali.in/](https://cyberbali.in/)

**Join us at the Cyberbali Exchange**— Our cybersecurity discord community with Indian tadka —

[https://discord.gg/TA7gBKZbUM](https://discord.gg/TA7gBKZbUM)
