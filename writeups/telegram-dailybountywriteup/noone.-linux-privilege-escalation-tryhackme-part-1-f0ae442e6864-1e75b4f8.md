# Linux Privilege Escalation | TryHackMe — Part 1

- **Source URL:** https://medium.com/@NoOne./linux-privilege-escalation-tryhackme-part-1-f0ae442e6864?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240605153017/https://medium.com/@NoOne./linux-privilege-escalation-tryhackme-part-1-f0ae442e6864
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6075 (id 6075)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Linux Privilege Escalation | TryHackMe — Part 1

# Introduction

Hi! I am a Content Creator/Editor by profession and an infosec novice trying to step into the InfoSec industry. I will mainly cover TryHackMe rooms and modules in my write-ups. As a beginner in this field, I will mostly stick to following the official walkthroughs provided by TryHackMe and not reiterate the theoretical concepts here for the most part.

Let’s begin!

Today, I will be covering TryHackMe’s **Linux Privilege Escalation** room. You can read up on it and access the practice VMs [here](https://tryhackme.com/r/room/linprivesc).

The room begins with a basic introduction of what will be covered in this room and provides a fundamental understanding of privilege escalation. Let’s jump straight into Task 3!

# Task 3 — Enumeration

## **Q: What is the hostname of the target system?**

The task specifies how to identify the hostname of the target system.

Let’s give that a shot.

There we go! Nice and easy!

Also pay attention to the beginning of the prompt — `karen@wade7363`.

It specifies the current user and the hostname of the system separated by ‘@’.

**Answer:** `wade7363`

## **Q: What is the Linux kernel version of the target system?**

We are given two ways of identifying the Linux kernel version.

Let’s try both methods.

There we have it.

**Answer:** `3.13.0-24-generic`

## Q: What Linux is this?

Both commands used in the previous question specify that the Linux flavour in use is Ubuntu, but we are not given the version. In `/proc/version`, we have `Ubuntu 4.8.2-19ubuntu1` — although it appears to be the required answer, it is rather relevant to the gcc version in use.

Let’s check out what the guide has in store for us.

Let’s read the `/etc/issue` file to identify the OS and version running on the system.

That gives us the required answer.

**Answer:** `Ubuntu 14.04 LTS`

## Q: What version of the Python language is installed on the system?

We are not given a specific way of identifying the version of Python installed on the system. The only relevant information provided to us is as follows:

As suggested, we can run the `env` command and check whether it lists Python in the `PATH` variable. Let’s try it out.

We can see that the `PATH` variable does not print anything concerning Python. While that does not help us much, we can simply the run the commands `python --version`and `python3 --version`, where the former prints the version of Python2 and the latter prints the version of Python3, if any, running on the system. Let’s give them a shot.

The target system is running two versions of Python, but the answer field accepts only the Python2 version.

**Answer:** `Python 2.7.6`

## Q: What vulnerability seem to affect the kernel of the target system? (Enter a CVE number)

We identified the kernel version of the target system in one of the previous questions. It is `3.13.0–24-generic`. Let’s perform a simple google search for the required CVE number.

The first few results clearly state the CVE number issued for the vulnerability affecting the kernel version of the target system.

**Answer:** `CVE-2015-1328`

# Task 5 — Privilege Escalation: Kernel Exploits

## Q: find and use the appropriate kernel exploit to gain root privileges on the target system.

In the previous task, we identified that the target system is vulnerable to CVE-2015-1328. Let’s try the first result from exploit-db.

We can confirm that the kernel version falls in the range `3.13.0 < 3.19`. This exploit is also EDB Verified, as suggested by the check-mark, so we can run it safely against the target system. Let’s download the exploit into the `/tmp` directory and run it as per the following instructions:

Here is the result:

And we are in!

## Q: What is the content of the flag1.txt file?

We have root access on the system. Let’s first locate the `flag1.txt` file.

Now, let’s print the file contents to grab the flag.

There it is. Nice and easy!

**Answer:** `THM-28392872729920`

# Task 6 — Privilege Escalation: Sudo

## Q: How many programs can the user “karen” run on the target system with sudo rights?

The task mentions the command `sudo -l` for checking root privileges available to the current user.

Let’s run the said command to identify the programs the `karen` can run with sudo rights.

Thus, `karen` can run three commands with sudo rights — `find`, `less`, and `nano`.

**Answer:** `3`

## Q: What is the content of the flag2.txt file?

First, let’s locate the `flag2.txt` file.

The `locate` command does not work, so we will use the `find` command.

Let’s break down the command.

`find` Initiating the command for finding the required file

`/` The directory in which we want to look for the file — here, we are looking into the entire file system

`-type f` Specifying the type of file or object we want to look for — 'f' stands for regular file

`-name flag2.txt` Specifying the name of the file

We have found the location of the file. Let’s now print its contents to grab the flag.

We have access to the file, so we can read it without any hassles. Nice and easy!

**Answer:** `THM-402028394`

## Q: How would you use Nmap to spawn a root shell if your user had sudo rights on nmap?

The tasks provides the following hint in this regard:

Let us check out the [given link](https://gtfobins.github.io/) and see how we can use Nmap with sudo rights to spawn a root shell.

As shown in the second method, we can simply run the interactive mode to spawn a root shell.

**Answer:** `sudo nmap --interactive`

## Q: What is the hash of frank’s password?

Password hashes are generally stored in the `/etc/shadow` file. Let’s check out whether we can access it with our current privileges.

As expected, a standard user cannot access the file. We need to leverage the three commands we identified that we can run with sudo rights.

Let’s try them all.

First, we will try the `find` command.

Let’s look into GTFOBins and get the command for spawning a root shell using `find` with sudo rights.

Let’s spawn a root shell to access the shadow file and search for `frank`’s password hash.

There it is.

Now, let’s try the `less` command.

As the less command is used to print the contents of a file, we can simply run it with sudo rights to read the shadow file directly. While GTFOBins provides a command to spawn a shell, we do not need it in this case.

There we go. Two commands down!

Finally, let’s try the `nano` command.

We will go back to GTFOBins for this one.

Looks alright. Let’s give it a shot.

Typing `sudo nano` spawned a nano window. Then, we hit CTRL+R followed by CTRL+X, which brought the input cursor to the `Command to execute:` field shown in the lower portion of the image. Now, we will run `reset; sh 1>&0 2>&0` in that prompt to spawn a root shell. Then, we will again access the shadow file and grab the required password hash.

And we have got the hash once again. Easy enough.

**Answer:** `$6$2.sUUDsOLIpXKxcr$eImtgFExyr2ls4jsghdD3DHLHHP9X50Iv.jNmwo/BJpphrPRJWjelWEz2HH.joV14aDEwW1c3CahzB1uaqeLR1`

# Task 7 — Privilege Escalation: SUID

## Q: Which user shares the name of a great comic book writer?

Let’s check the `/etc/passwd` file to identify the user who shares the name of a great comic book writer.

The user `gerryconway` appears to be the required username. (A quick google search confirms it is indeed the name of a famous comic book writer.)

**Answer:** `gerryconway`

## Q: What is the password of user2?

The task suggests searching for files with the SUID bit set. We will then leverage those files to access the shadow file and grab the password hash of `user2`. We will (potentially) crack the hash to obtain the required password.

Among the resulting files, only `/usr/bin/base64` has an entry on GTFOBins with the SUID flag set. Let’s try it out to print the shadow file.

As suggested in the image, we will skip the first command (and perhaps even the second one).

We have the password hashes of `gerryconway`and `user2`. Let us use `john` — a Kali built-in hash-cracking tool — to obtain the password of `user2` from the hash. We will use the following command:

`john --wordlist=/path/to/wordlist /path/to/hashfile`

And we have the password of `user2`.

Let’s try cracking the password of `gerryconway` just for the fun of it.

And we have cracked that too. Although not necessary, we can try cracking the password hashes of other users if we are unable to escalate our privileges vertically. The other users could potentially have different permissions or files that could be leveraged to get root access on the target system.

**Answer:** `Password1`

## Q: What is the content of the flag3.txt file?

First, let’s locate `flag3.txt`.

Now that we have the location, we will use the `base64` command to read the contents of `flag3.txt`just as we did with the shadow file.

We have the flag!

**Answer:** `THM-3847834`

A lengthy write. We will go through the remaining tasks in Part 2 Insha’Allah.
