# Insecure Direct Object References (IDOR) — PortSwigger Lab Walkthrough

- **Source URL:** https://vivek0x.medium.com/insecure-direct-object-references-idor-portswigger-lab-walkthrough-e1c61dba9090
- **Fetched from:** https://web.archive.org/web/20260831093142/https://vivek0x.medium.com/insecure-direct-object-references-idor-portswigger-lab-walkthrough-e1c61dba9090
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14890 (id 14890)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Insecure Direct Object References (IDOR) — PortSwigger Lab Walkthrough

Access Control section of PortSwigger’s Web Security Academy, and this one’s a classic — the kind of vulnerability that gets its own well-known name in the security world: **IDOR**, short for Insecure Direct Object Reference. If you’ve ever heard someone say “just change the file name in the URL and see what happens,” this lab is basically that idea in its purest form.

### What this lab asks for:

This lab stores user chat logs directly on the server’s file system, and retrieves them using static URLs. Solve the lab by finding the password for the user `carlos`, and logging into their account.


No credentials handed to us this time — we’re working entirely off what the app exposes on its own.

### Step 1: Poking Around the App

I clicked **Access the lab** and landed on the homepage, which had three simple links in the nav bar: **Home**, **My account**, and **Live chat**. Nothing unusual yet, so I went straight for the one that sounded most interesting — **Live chat**.

The chat page showed a short conversation log (something like “Now chatting with Hal Pline… Disconnected”) and two buttons underneath the message box: **Send** and **View transcript**.

### Step 2: Grabbing the Transcript Request

`View transcript` immediately caught my attention — "transcript" usually means the app is pulling some kind of saved file, and saved files often live at predictable URLs. I turned on Burp Suite's intercept and clicked the button.

The captured request pointed to:

`https://<lab-id>.web-security-academy.net/download-transcript`
I forwarded the request and it downloaded a file called **2.txt**

### Step 3: The IDOR

A file called `2.txt`, served from a static-looking URL, immediately raises one question: what happens if I ask for `1.txt`?

I edited the URL directly in the browser:

`https://<lab-id>.web-security-academy.net/download-transcript/1.txt`
And just like that, it downloaded a completely different file — `1.txt` — no authentication check, no ownership check, nothing stopping me from just requesting a different number.

### Step 4: Reading the Leaked File

I opened `1.txt` and read through it. Buried in that transcript was a password for the user `carlos`, in plain text — sitting in a file that had nothing to do with my session or account.

```
CONNECTED: -- Now chatting with Hal Pline --
You: Hi Hal, I think I've forgotten my password and need confirmation that I've got the right one
Hal Pline: Sure, no problem, you seem like a nice guy. Just tell me your password and I'll confirm whether it's correct or not.
You: Wow you're so nice, thanks. I've heard from other people that you can be a right ****
Hal Pline: Takes one to know one
You: Ok so my password is p7oxlsyfhqkk92de63n9. Is that right?
Hal Pline: Yes it is!
You: Ok thanks, bye!
Hal Pline: Do one!te
```
### Step 5: Logging In as Carlos

I went back to the login page and logged in with:

- **Username:** `carlos`
- **Password:** `p7oxlsyfhqkk92de63n9`

It worked immediately. Lab solved.

### Root Cause

This is IDOR in its most textbook form. The application stores chat transcripts as flat files on the server (`1.txt`, `2.txt`, and so on) and serves them from a predictable, sequential, static URL — with **zero access control** tying a transcript to the user who's actually allowed to view it. There's no session check, no ownership validation, nothing. If you know the naming pattern, you can just walk through the numbers and pull whatever file you want.

This is exactly the kind of vulnerability that shows up in the real world constantly — invoice IDs, order numbers, document links, profile pictures — anything referenced by a sequential or guessable identifier in a URL, with no server-side check that the requester actually owns that resource.

### Key Takeaway

Never assume an object reference is safe just because it’s “hidden” behind a download link or a button click. If a resource is reachable by predictable IDs — numeric, sequential, or otherwise guessable — and the server isn’t verifying that the current user actually has permission to access that specific object, you’ve got an IDOR. The fix isn’t obscurity, it’s an actual authorization check on every single request, every single time, regardless of whether the reference “looks” hard to guess.

This lab is a great reminder that sometimes the simplest test — just change a number in the URL — is still one of the most effective things you can do during a security review.

GoodByeee….
