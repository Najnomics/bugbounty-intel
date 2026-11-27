# From alert(origin) to ATO, an XSS Story

- **Source URL:** https://medium.com/@remmy9/from-alert-origin-to-ato-an-xss-story-d6bd2684bdca?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@remmy9
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 8689)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey everyone, it’s Remmy. In this writeup, I’ll explain how I recently escalated an XSS vulnerability to an Account Takeover. I won’t be covering my recon process since it’s quite similar to what other hunters do. So, please forgive me for that.

### First Part — The XSS Discovery?

I was working on a program recently and decided to try out some new techniques I read about in "JavaScript For Hackers" and incorporate them into my methodology. While exploring one of the subdomains discovered during the DNS Bruteforce, I encountered a register page where I could register an account within the application.I registered as a regular user, logged in, and began doing some manual work to familiarize myself with the web application. Upon checking the technologies by the web application using Wappalyzer, I realized that it employs React and its ecosystem for front-end development. I felt a bit disappointed, not only because XSS in React is impossible but also because I couldn't leverage the knowledge I gained from JS for Hackers. What a disaster!

But then I remembered one thing: just because a web application uses a library like React or a framework like Vue.js doesn’t mean all features are built with them. Developers often use vanilla (pure) JavaScript to implement functionalities. So, I gave myself some hope — actually, it was the only thing I could do at that moment. 😆

I started testing every functionality — any feature that processed user input — and guess what? As expected, there was no XSS or even a reflection.

After a few days of frustration, I came back to the web application and started testing the features again — this time completely from scratch. I carefully observed everything and realized that I had missed something early in my hunting: the **nickname editing feature**. This feature allowed users to set a fancy nickname, which was displayed as a badge on top of their profile picture. The idea was that when others viewed your profile, they’d form a positive impression of you. (Honestly, who even judges people based on their nickname? Except me, I guess.)

When I clicked on the “Edit Nickname” button, I could enter my nickname, but there was another interesting functionality. There was an **expand/fullscreen icon** (or whatever you want to call it) that opened the nickname editor in a separate page. In that expanded view, I wasn’t just able to set a nickname — I could also upload a profile picture and customize other fancy details.

After entering a dummy nickname (I called myself **CuttieBatman**), I clicked the **Save** button, then pressed **Save and Exit**. If you’re expecting an XSS here — well, unfortunately, it didn’t happen.

Instead, the web application redirected me to a new page where I could view my fancy new public profile. But what caught my attention was the **URL**, which contained a parameter like this:

someSubdomain.redacted.com/usersview/profiles/someFancyParameters&v=true&nickname=CuttieBatman

I wasn’t sure what **“v”** meant in the URL, but I was certain that the nickname parameter was referencing me. So, I viewed the source code of the page, and as expected, my nickname was present in the parameter.

I went back to the nickname editor and entered **“\<”** as a simple test payload, then saved, clicked **Save and Exit**, and returned to the profile page. Sure enough, the **“\<”** was reflected on the page.

Encouraged by this, I repeated the process — this time entering **“\<i”** as my input. I saved, exited, blah blah blah… and once again, it was reflected. So I understood that the web application doesn’t have any problem with \< and string. It was a good starting.

I repeated the steps again, this time entering **“\<img src=x”**, but the web application blocked me. So, I removed the src=x and tried again, only to be blocked once more! It was clear that the protection was triggered by a valid tag.

With no other option, I decided to fuzz the inputs. I used **PortSwigger** and tested several tags, but every attempt resulted in the same error: **Blocked by the protection**.

At this point, I realized it was time to change my approach. What would happen if I fuzzed like this:

\<i\[FUZZ\]m\[FUZZ\]f\[FUZZ\]>

I fuzzed various characters using different encodings — space, tab, null, and enter — applying URL encoding, Unicode, HEX, and more. After testing several payloads, one payload turned out to be successful: the tab character. Yes, I literally inserted the HTML-encoded tab character, and the application rendered it as a valid tag. As a result, the \<img tag was reflected in the input. The application was removing any spaces between the input and then rendered it. I continued with approached and I had the final payload of this:

\<	i	m	g	 	s	r	c	x	=	 	o	n	e	r	r	o	r	=	a	l	e	r	t	(	o	r	i	g	i	n	)	>

from what I understand, the web application’s protection was primarily focused on detecting complete, unencoded HTML tags. By submitting HTML-encoded characters, I was able to bypass the protection regex. The application didn’t recognize the encoded characters as part of a complete tag, so the filter didn’t block it. However, when the browser rendered the page, it decoded the HTML entities back into their original form, allowing the tag to be executed and bypassing the security

There was one problem, though: the application didn’t accept my payload at first because the maximum allowed characters for a nickname were 32, and my payload was 161 characters long.

### Second Part: Response Manipulation to bypass char limit

When we entered our payload, Requests and Responses happened like this:

HTTP/1.1 200 OK

Host: target.com

Content-Type: application/json

Content-Length: 68

{

"status": "failed",

"message": "maximum character exceeded.",

"code": 400

}

I had to manipulate the response to determine if there was any way to bypass the character limitations. First, I modified the "status": "failed" to "status": "success" in the JSON response, but nothing happened. Turns out, the issue wasn't just with the status field.

The real problem lay with the application’s handling of the response codes. A 400-status code was used for failed responses, but for successful ones, the response included a code: 1 and an additional parameter "set": "vbspmd".

After bypassing the character limitations, I successfully set my payload and navigated to the next page. To my surprise, the XSS was triggered, and it worked perfectly! (There was a catch — users had to be logged in for the payload to execute, as the page wasn’t displayed to unauthenticated users.)

### Third Part — Account Takeover

Getting an XSS was great, but it wasn’t enough for me — I wanted an Account Takeover (ATO). Escalating the impact was my next goal. To achieve that, I needed to steal authenticated cookies, replace them with my own, and log in as the victim.

So, what was the plan? Simple:

1. Write a payload to exfiltrate the victim’s session.
2. Package it into a working Proof of Concept (PoC).
3. Deliver it to the target.
4. Profit. 😈

I wrote the exploit, set up a listener on my VPS, and tested the exploit on myself. It worked perfectly. I had successfully escalated the XSS to an Account Takeover (ATO). With the exploit functioning as expected, I crafted a detailed report, attached all the proof of concepts (POCs), and submitted it.

However, after 4–5 days, I received the dreaded notification: my report was closed as a duplicate of the findings from their external penetration testing team.

**And that’s how the report ended — with a bit of pain in my heart.** :)

Hope you enjoyed reading through my writeup!

You can follow me on X (formerly Twitter): [Remmy (@NineRemmy) / X](https://x.com/NineRemmy)
