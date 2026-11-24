# Unveiling IDOR

- **Source URL:** https://medium.com/@a13h1/unveiling-idor-how-i-accessed-users-post-images-without-authentication-a-mischievous-adventure-80387cdd5994?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260221194850/https://medium.com/@a13h1/unveiling-idor-how-i-accessed-users-post-images-without-authentication-a-mischievous-adventure-80387cdd5994
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3432 (id 3432)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR: How I Accessed Users’ Post Images Without Authentication

I recently discovered a critical Insecure Direct Object Reference (IDOR) vulnerability in a prominent automobile advertising website. In this post Apart from the moose name of the website where I found this bug, I’m using example.com as a reference. This vulnerability allowed attackers to manipulate and replace vehicle images on any user’s post without accessing their account or requiring any authentication. In this blog post, I will share the details of my discovery, the potential risks, and the responsible disclosure process that followed.

**Understanding Example.com**

Example is a popular platform that enables users to advertise their vehicles for sale. It offers a user-friendly interface, allowing individuals to showcase their cars with images and relevant details to attract potential buyers.

**Discovery of the IDOR Vulnerability**

Like a curious cyber explorer, I stumbled upon a peculiar URL pattern while traversing example’s virtual terrains: `https://www.example.com/annoncer-son-vehicule/vehicule_edit_photos?id=%60victimspostid%60`. There it was—the enigmatic `id` parameter, beckoning me to playfully probe further.

With a glint in my eye and a dash of excitement, I engaged in playful mischief by manipulating the `id` parameter. Swapping post IDs with the glee of a child unraveling a puzzle, I wondered what the virtual world had in store for me.

As I clicked the virtual “Go” button, a magical gateway opened before me. Like a mischievous magician, I found myself transported into the realm of other users’ vehicle posts. Without any authentication barriers, I was a cyber-genie, able to access and edit images with ease. Each click was an enchanting revelation — a new door to an unsuspecting user’s automobile adventure.


But even in the midst of my playful escapades, the voice of ethical responsibility guided me to tread lightly and preserve the integrity of the platform.

**The Balance of Power and Responsibility**

While the allure of digital pranks tempted me, I couldn’t ignore the gravity of the situation. The mischievous charm of IDOR carried potential risks — defacing legitimate advertisements, replacing images with whimsical visuals, and sowing seeds of distrust among users.

In the spirit of ethical hacking, I realized that great power demanded even greater responsibility.


It was time to transform my playful capers into a quest for solutions.

**Reporting**

Embracing the mantle of an ethical knight, I galloped towards the Example security team with valuable insights in hand. My journey was not just a mischievous escapade, but a mission to protect and preserve trust in the digital realm. With the vulnerability reported and a swift response from the Example crew, the wheels of change were set in motion. A patch was swiftly applied, closing the gateways to misadventure and restoring the platform’s security.

Connect with me on Twitter [@a13h1\_](https://twitter.com/a13h1_) or find me on LinkedIn [https://www.linkedin.com/in/a13h1/](https://www.linkedin.com/in/a13h1/). And to all the readers, I extend my heartfelt gratitude for joining me on this journey. May this tale of IDOR entertain and enlighten you.
