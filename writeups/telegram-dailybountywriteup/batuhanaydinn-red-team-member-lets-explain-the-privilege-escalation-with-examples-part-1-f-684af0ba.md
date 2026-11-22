# Red Team Member — Let’s explain the Privilege Escalation with examples / Part 1

- **Source URL:** https://medium.com/@batuhanaydinn/red-team-member-lets-explain-the-privilege-escalation-with-examples-part-1-f109b4ce49b2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251224083849/https://medium.com/@batuhanaydinn/red-team-member-lets-explain-the-privilege-escalation-with-examples-part-1-f109b4ce49b2
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3553 (id 3553)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Red Team Member — Let’s explain the Privilege Escalation with examples / Part 1

Hello folks, I hope your week is going well. I’m getting hot and I got my drink again and I wanted to sit in front of the computer and tell you about one of the most fun steps of a red team member this week, privilege escalation. By the way, if you’re not following me on Medium, you might miss a lot. By subscribing to my newsletter [https://medium.com/@batuhanaydinn/subscribe](/@batuhanaydinn/subscribe), you can be informed about the articles quickly and read my educational articles in the field of cyber security. Again, let’s understand what privilege escalation is before we examine it in depth and move on to simulations.

## Part 1: Hackers Are Privileged People

It is not possible for you to come across any article that I did not mention technical definitions here, but first of all, I would like to start this by giving examples from daily life so that everyone can visualize it in their minds. Understanding how a hacker’s head works and being able to put what we have learned theoretically into real-life examples increases the pleasure we get from the job, but also takes us one step ahead.

An APT group wants to join veryverybig company. It is extremely difficult for them to get into the company’s network because they are aware that real life is not like hack the box machines and the company’s emails are very well protected, but also because of the superior cyber security awareness skills of the people working in the company. That’s why they think that privileged people need credentials and access cards. In the shopping mall opposite the company, they produce a copy of the company personnel’s card, through which they can enter the company using the cards they use to pass through the door.


Real life really isn’t like the machines we solve on the internet. The event I described above is one of the methods used by red team members or APT teams. Here, if the technology used on NFC is old, things can get a lot easier. I’m not going to tell you about this today, but you will be amazed when you learn how they work and how easily they can be hacked.

Now that we can only imagine what Privilege Escalation is, let’s give some technical and theoretical information that won’t bore you, and see how this can happen on simulation.

### What is Privilege Escalation?

Privilege Escalation is a cyber attack method in which malicious people or attackers try to gain access to a higher level of authority by raising their low level of authority on the target system. This often involves users or processes with limited privileges gaining undesirable greater access to the system. Privilege Escalation attacks can enable attackers to access sensitive data, change system configurations, or perform other malicious activities.

### Privilege Escalation Types

1. **Horizontal Privilege Escalation**: An attacker gains access to the target account by obtaining the credentials of another user with the same authorization level or by stealing a session.
2. **Vertical Privilege Escalation**: The attacker tries to reach a higher level of authorization by raising the privileges of a low-authority account. For example, it might try to switch from a user account to an administrator (“root”) account.
3. **Retrieving Credentials**: An attacker attempts to access accounts with higher privileges by hijacking passwords stored in a vulnerable application or system.

## Part 2: Let’s develop a simulation

Now let’s come to the funniest and, in my opinion, the most educational part of the job. Those who have read my previous articles know that I love to develop simulations and provide information about how an error occurs. I think the way to understand any subject is to understand the basis of that subject. When we adapt this to cyber security, if you can basically figure out why such errors occur in a project and if you can create such errors, you understand the issue. What we do is look through the eyes of the developers and discover the mistakes they can make. The source code is not available during any pentest or red team activity. What will provide you with the ability to observe every data returning from the area you are testing is knowing how that software was developed. Now that I’ve been babbling a lot, we can now start developing our simulation and understanding the privilege escalation in the simulation we developed.

Instead of telling you the code step by step, I will give you the github repo in the link. My request from you is to first read the code and answer the fields containing Privilege Escalation on the code by highlighting these lines and test yourself. You can write your sample codes or thoughts on how to close these security vulnerabilities in the comments or as an issue.

Although there are many security vulnerabilities in the code, I will only tell you about one. Those who look carefully must have seen the error in the register field immediately.

The input field added as hidden takes the value of 0 by default. You may think that this is a simulation and that you are unlikely to encounter such a thing in reality, but I have encountered such an IDOR vulnerability before. the IDOR? yes, even if we do http parameter pollition here, when we actually examine the security vulnerability by going down to the basics, we realize that an admin user can be added by changing the user\_type object in an undesirable way.

The request we send by changing the user\_type value should produce values such as 404 under normal conditions. Here, however, we encounter something very different.

Since the request sent is not filtered and the user\_type value is left open in the register field, a normal person changes the user\_type value while registering and gains admin access on the web app. As for why I explained it with such a simple example, I think the most important thing is to understand what the underlying problem is. To read what this type of vulnerability looks like in a more advanced area:

I think I can explain simply and simply what this type of vulnerability looks like and that our main purpose is to gain unauthorized access. If you have any questions, please don’t forget to ask.

In the next week, I will show a much more detailed Privilege Escalation example on the CTF machine that I am still writing. Don’t forget to follow me on [Medium](/@batuhanaydinn) to be informed about the machine quickly next week. Plus, I publish a lot of information about the articles on my [LinkedIn](https://www.linkedin.com/in/batuhan-aydinn/) and [Twitter](https://twitter.com/telumak) accounts, don’t forget to follow me there and report your comments. Take care of yourself, until the next article, I wish you a healthy, happy and profitable time. ❤️❤️❤️
