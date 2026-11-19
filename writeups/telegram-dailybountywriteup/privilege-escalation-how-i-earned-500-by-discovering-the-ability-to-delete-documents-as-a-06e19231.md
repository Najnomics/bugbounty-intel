# Privilege Escalation

- **Source URL:** https://infosecwriteups.com/privilege-escalation-how-i-earned-500-by-discovering-the-ability-to-delete-documents-as-a-student-8cdf9eab1375?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012135942/https://infosecwriteups.com/privilege-escalation-how-i-earned-500-by-discovering-the-ability-to-delete-documents-as-a-student-8cdf9eab1375
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3853 (id 3853)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation: How I Earned $500 by Discovering the Ability to Delete Documents as a Student

--

I recently stumbled upon a fascinating issue while testing Examosis, an educational platform. This issue allowed low privilege users,students, to delete documents and items they weren’t supposed to delete only administrators should have the privilege to delete content.

**Understanding Target (Examosis)**


Examosis\[virtual name to prevent the identity of private name\], it’s an online learning platform widely used in educational institutions, particularly in the healthcare field. Examosis provides students and educators with a comprehensive set of tools and resources to enhance the learning experience.

**What’s Privilege Escalation?**


Think of privilege like keys to different rooms in a building. Imagine you have a key to your room, and your teacher has a key to the classroom. But one day, you somehow get a key that can open all the rooms, even the ones you’re not supposed to go into. That’s what we call “privilege escalation” in the computer world — it’s like getting extra keys you shouldn’t have.

**Discovering the Bug**


I was surfing, Examosis I had two accounts open at the same time — one as a regular student and the other as an administrator.

I noticed something interesting. The administrator account had a special feature that allowed it to delete files and content that regular students weren’t supposed to touch.

Curiosity got the best of me I wondered, “What if I could use the student account to delete files too?”


I tried it out, clicked the delete button, captured the request , and deleted the file with the administrator account first.

But here’s where it got exciting. I used that same request with the student account, the one that wasn’t supposed to have this power. And guess what? It worked again!

## Steps To Reproduce

- To reproduce this issue you require the two accounts one for admin and other for student/user
- Then open student account and go to course/workshop as we know we are only allowed to download the document.
- Select the document you wanna delete get the Document ID.
- So use the below request through student account and Document Id to id.

```
DELETE /v0/link/`ID` HTTP/2
Host: www.examosis.org
Cookie: _--------student/user cookie-----------
Content-Length: 37
...
```
- Send the request and the document get deleted.

**The Bounty**


Now, let’s talk about the cool part — the reward I got for finding this bug.Its time to get some money. I go to the program report submission page, submit the report As a way to say “thank you,” they gave me $500!

T**akeaway**


When you’re on a website, explore and compare permissions between different types of accounts. This means trying to do things you’re not supposed to, starting as a regular user and seeing if you can perform tasks meant for admins.

*Leave a clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting content.*


*Find me on Twitter: @a13h1\_*


# Thank you everyone

Keep Supporting, Keep Clapping, Keep Commenting.
