# Linux Privilege Escalation — Capstone Challenge | TryHackMe

- **Source URL:** https://medium.com/@NoOne./linux-privilege-escalation-capstone-challenge-tryhackme-e69c798204bc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240604132706/https://medium.com/@NoOne./linux-privilege-escalation-capstone-challenge-tryhackme-e69c798204bc
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6098 (id 6098)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Linux Privilege Escalation — Capstone Challenge | TryHackMe

Hi! We previously covered all guided tasks of the Linux Privilege Escalation room. You can find them at the following links:

Part 1: [https://medium.com/@NoOne./linux-privilege-escalation-tryhackme-part-1-f0ae442e6864](/@NoOne./linux-privilege-escalation-tryhackme-part-1-f0ae442e6864)

Part 2: [https://medium.com/@NoOne./linux-privilege-escalation-tryhackme-part-2-9a4cddba01ab](/@NoOne./linux-privilege-escalation-tryhackme-part-2-9a4cddba01ab)

It is now time to put all that we have learned about Linux privilege escalation into practice. Let’s get started with the final task — Capstone Challenge. As this challenge does not have a guide, I will be going through it from a complete black-box POV. There may be quite a few unnecessary tangents and headbutts, but we will eventually get there.

# Objective

Let’s take a look at the challenge.

Right, then. Our main objective is to read the contents of `flag1.txt` and `flag2.txt`. We are given ssh credentials for an unprivileged user `leonard`, and we need to escalate our privileges until we are `root`. Let’s get started.

We will begin by checking whether we have any `sudo` privileges.

We cannot run `sudo`. Let’s check the command history of the user. There could be some hints or even passwords left behind.

We don’t have much to go on with, but we can at least gather that `flag2.txt` is located in the `/home/rootflag` directory. We also might need to compromise the `missy` user in order to get `root` on the system, but we will focus on the current user first.

We have an empty directory named `perl5` that is world-executable. I’m not sure where that would come into play. Also, we get a `permission denied` error when we try to access `/home/missy` or `/home/rootflag`. Let’s try cron jobs. Maybe there is something worth exploiting in there.

Nope, not quite. Let’s try finding files with the SUID bit set. It was a fairly successful path in the guided tasks.

That looks promising! We exploited the `base64` binary with the SUID bit set in Task 7. Let’s try it out again. This could be a case of getting ahead of ourselves, but there’s no harm in trying to read the contents of the flag files directly using `base64`. We are not sure where the two files might be located, so we will just try `/home/missy/flag1.txt` and `/home/rootflag/flag2.txt` based on the information we gathered from the `history` command. We won’t waste time guessing the correct locations.

Well that was easier than I expected it to be. We have found the `root` flag without any effort, and it appears that `flag1.txt` is located somewhere else. Let’s try another route.

As we can use the `base64` binary with `root` privileges, we might as well grab the `root` user’s password hash from the `/etc/shadow` file and try cracking it. Let’s see how that works out for us.

We now have the `root` user’s password hash. We also went ahead with grabbing `missy`’s password hash, just in case. Let’s try cracking both hashes using `john`and the default `rockyou.txt`.

`john` ran for a while but couldn’t crack the `root` hash. The process had to be stopped before completion because the hash cracking was not expected to take so long unless the hash was meant to be uncrackable. So, we shall now move on to `missy`’s hash.

No longer than a single sole second later, we have cracked `missy`’s hash. It took longer to type the command than for `john` to crack the hash. Nice and easy.

Let’s log in as `missy` and read the `flag1.txt` file to get the answer to the final question (as we already have the `root` flag).

There’s the flag.

Although we will have technically completed the challenge by obtaining both flags, we will try to escalate our privileges until we have compromised the `root` user. Let’s begin by checking whether `missy` has any `sudo` privileges.

And we have a new vector. We can run the `find` command with `sudo` privileges. Let’s quickly jump on to GTFOBins and find out how we can make our way to `root`.

Perfect! We can simply run the command `find . -exec /bin/sh -p \; -quit` to escalate our privileges to `root`. Let’s do it!

There it is! We finally have a root shell.

## Q: What is the content of the flag1.txt file?

**Answer:** `THM-42828719920544`

## Q: What is the content of the flag2.txt file?

**Answer:** `THM-168824782390238`

# Recap

We began with the user `leonard`, who had no `sudo` privileges. After some information gathering, we identified that the binary `base64` has the SUID bit set. We then used this binary to read the contents of the `/etc/shadow` file and grabbed the password hashes of `missy` and `root`. While we couldn’t crack the password hash of `root`, we cracked the hash of `missy` and identified the password of that account — `Password1`. Then, we logged into the `missy` account and found that we can run the `find` command with `sudo` privileges. We then turned to GTFOBins and found the command `find . -exec /bin/sh -p \; -quit`, which spawned a nice little `root` shell for us.

Easier than expected but a fun challenge nonetheless for beginners. Loved it. Insha’Allah we will crack open another room or maybe even a similar challenge soon. Until then, take care!
