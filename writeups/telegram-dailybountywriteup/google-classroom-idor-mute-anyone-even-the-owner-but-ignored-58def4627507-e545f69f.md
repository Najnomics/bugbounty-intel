# Google Classroom IDOR

- **Source URL:** https://v0ltex.medium.com/google-classroom-idor-mute-anyone-even-the-owner-but-ignored-58def4627507?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250405171650/https://v0ltex.medium.com/google-classroom-idor-mute-anyone-even-the-owner-but-ignored-58def4627507
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9265 (id 9265)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Google Classroom IDOR: Mute Anyone, Even the Owner… But Ignored 😔

— — — — — — — — — — — — بسم الله الرحمن الرحيم — — — — — — — — — — — —

اللهم انصر إخواننا في غزة، وكن لهم عونًا ونصيرًا، وفرّج كربهم، واحفظهم بحفظك، وانصرهم نصرًا عزيزًا مؤزّرًا (#FreePalestine).

Hi Hackers,

I’m currently hunting on Google VRP and have found a few cool bugs. But this one? It’s kind of special ,it got marked as “Won’t Fix (Infeasible).”

I started by checking out Google VRP’s scope, looking for a domain with lots of functionality and permission logic. Why? Because I enjoy manual testing and digging into auth bugs. That’s why I picked **Google Classroom** as my first target.

Let’s dive into how I stumbled upon this IDOR. If you’ve ever hunted bugs on Google, you know their requests can look a bit… wild 😅 \[You start guessing what each parameter is doing\]. While comparing requests across multiple accounts, I noticed something interesting: there’s an ID for each user role — Owner, Teacher, and Student.

Then, I spotted another ID in the mute functionality, but this one was specifically tied to students.

Wait… IDs? Time to test for IDOR! I started swapping the student ID with a teacher’s ID, refreshed the page… and boom! The teacher was muted. Tried the same with the Owner ID, And the owner was muted too.

**Quick Note:** The mute functionality in Google Classroom is actually meant for teachers or owners to mute students — not the other way around. Here’s what happens when a user gets muted:

They can still submit work, but other students won’t see it.

They can’t reply to classmates’ work.

They can’t comment or post.


This bug was interesting because it let a teacher (attacker) mute **everyone** — Owners, other Teachers, and Students. This disabled the comment function for those users, It was a huge oversight since teachers aren’t supposed to have that kind of control over other teachers or the owner!

**Summary:**

An IDOR bug allowed an attacker with teacher privileges to mute other teachers and even the Owner by swapping a student ID with the Owner/Teacher ID (IDs are exposed in the request, requiring no victim interaction). This caused a privilege downgrade, violating the intended permission model where only students should be muteable by teachers. Even Owners, the highest-privileged users, were affected, posing a significant security risk.

**Steps To Reproduce:**

1. Create three accounts at `https://classroom.google.com/`, \[[Owner@google.com](mailto:Owner@google.com) , [attacker-teacher@google.com](mailto:attacker-teacher@google.com) , [student@google.com](mailto:student@google.com)\]
2. From the Attacker-Teacher account, go to the “People” tab and refresh. Then, search through the browser history (Burp history) for the user names. You’ll find the IDs next to them
3. From the Attacker account, mute the student while intercepting the request in a proxy like Burp Suite. Send the intercepted request to the repeater and drop it.
4. In the repeater, replace the **Student ID** with the **Owner ID** or another **Teacher ID** and click **Send**.
5. NNavigate to the Owner account and observe that they’ve been muted. They’ll no longer be able to announce, comment, or reply to comments — essentially, your permissions are downgraded.

**Impact:**

Critical Roles Affected: Owners/teachers are the backbone of a class. Silencing them breaks everything.

Real-World Harm: Education disrupted, trust lost, and workflows destroyed.

Privilege Escalation \[IDOR\]:Teachers gain unauthorized control over peers and owners.

DoS: Owners can be muted, blocking class management.

Workflow disrupt :Teachers can disrupt collaborative environments by silencing peers.


Despite the potential impact, Google marked this as “Infeasible” and they won’t fix it 😭.

This mean it could still exist at the time you’re reading this write-up 😂.

I hope you enjoyed the write-up, See you in the next one.
