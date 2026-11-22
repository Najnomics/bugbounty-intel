# Linux Privilege Escalation | TryHackMe — Part 2

- **Source URL:** https://medium.com/@NoOne./linux-privilege-escalation-tryhackme-part-2-9a4cddba01ab?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603221306/https://medium.com/@NoOne./linux-privilege-escalation-tryhackme-part-2-9a4cddba01ab
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6090 (id 6090)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Linux Privilege Escalation | TryHackMe — Part 2

Hi! Let’s continue with TryHackMe’s **Linux Privilege Escalation** room. Here is the link to Part 1: [https://medium.com/@NoOne./linux-privilege-escalation-tryhackme-part-1-f0ae442e6864](/@NoOne./linux-privilege-escalation-tryhackme-part-1-f0ae442e6864).

# Task 8 — Privilege Escalation: Capabilities

## Q: How many binaries have set capabilities?

Let’s check out the guide on how we can list binaries that have set capabilities.

As we are starting with an unprivileged user `karen`, we will redirect the error messages to `/dev/null` as suggested.

We have a list of six binaries with set capabilities.

**Answer:** `6`

## Q: What other binary can be used through its capabilities?

The guide shows us the exploit for the `vim` binary, so the other binary listed here that can be used through its capabilities is `view` (`/home/ubuntu/view`).

**Answer:** `view`

## Q: What is the content of the flag4.txt file?

First, let’s locate the `flag4.txt` file.

The `flag4.txt` file is readable by all users. So, we don’t even need to run any exploits to grab the flag. We can simply print the file contents to the terminal and obtain the answer. First, let’s do it that way.

We have the flag. It is quite unexpected that we didn’t even need to run any exploits for it. However, for the sake of learning and keeping up with the guide, we will tag along with exploiting binaries with set capabilities.

We identified the `vim` and `view` binaries using the `getcap` command earlier. We will try to spawn a root shell using each binary with the help of GTFOBins. Let’s begin with `vim`.

As we don’t have sudo rights, we will just run the final command. However, we need to check the version of Python installed on the system and alter the command accordingly.

We can see that the target system has Python3 installed, so we will use the Python3 version of the exploit:

`./vim -c ‘:py3 import os; os.setuid(0); os.execl(“/bin/sh”, “sh”, “-c”, “reset; exec sh”)’`

Let’s give it a try.

Running the exploit spawns a blank root shell, so we simply print the contents of the `flag4.txt` file.

Now, let’s try the other binary — `view`. First, we will check out GTFOBins for the correct command.

Again, we will replace `:py` with `:py3` in the command for the exploit to work correctly. We need to either make sure we are in the correct directory where the `view` binary is located or provide the complete path to the binary.

And we have the flag once again.

**Answer:** `THM-9349843`

# Task 9 — Cron Jobs

## Q: How many user-defined cron jobs can you see on the target system?

The walkthrough guides us on how to check the list of user-defined cron jobs.

Let’s run the command and count the number of user-defined cron jobs.

We can see four user-defined cron jobs at the bottom.

**Answer:** `4`

## Q: What is the content of the flag5.txt file?

First, let’s locate the `flag5.txt` file.

We have located the file, but unlike the previous task, we cannot access the file directly. Let’s check out what the cron jobs can do for us.

Let’s begin with the `backup.sh` file as suggested in the guide. First, we will modify the file to create a reverse shell and set up a listener on our local machine. We will hopefully receive a reverse connection from the target system within a minute, as the `backup.sh` file is scheduled to run every minute.

After a few minutes of waiting, we did not receive any connection from the target machine. So, the first point of action is to check the file permissions. Turns out, nobody has the right to execute the file. So, we will just push a nice little `chmod +x` in there to make the file executable. That should hopefully fix the issue.

Finally, we have a reverse shell. Let’s quickly grab the flag from `flag5.txt`.

Nice and easy!

**Answer:** `THM-383000283`

## Q: What is Matt’s password?

We have a reverse shell with root privileges, so we can simply print the shadow file, grab `Matt`’s password hash, and crack the hash to obtain the password. Let’s do it.

There we go. We have cracked the password.

We could repeat the same steps with the `/tmp/test.py` binary. It appears that the file does not exist on the target system, so we can simply create one with the same name and take the same steps to spawn a root shell.

Additionally, in some cases, we can abuse a given script instead of modifying it entirely, as suggested below.

**Answer:** `123456`

# Task 10 — Privilege Escalation: PATH

## Q: What is the odd folder you have write access for?

We can obtain a list of folders we have write access for using the `find` command with the appropriate permission flags. Let’s take a look at the complete command.

We have a `-writable` flag that can be set for ease of use. Let’s try it out on the target system to find the odd folder required to answer this question.

The command produces a ton of results, and the only seemingly odd result is `/home/murdoch`. We are using `tail` for the sake of a compact screenshot. It would otherwise hinder your progress.

**Answer:** `/home/murdoch`

## Q: Exploit the $PATH vulnerability to read the content of the flag6.txt file.

First, let’s print the `PATH` variable and locate the `flag6.txt` file.

Now, let’s check out the guide.

So, we need to find a script/application that will run a command (`thm`in this case) in the context of a different user or `root` itself. If the script does not specify the absolute path of the command, the OS will search for the command in the folders listed under the `PATH` variable. If `$PATH` is modifiable, we will add a writable folder to `$PATH`, create a file with the name of the command (`thm`), and specify what the command should do.

That’s a lot to take in. Let’s get right into it.

A few quick searches in the `/home` folder later, we find a `test` file owned by `root` and with the SUID bit set. It is executable by all users, so if we execute it, it will run with the privileges of the `root` user. Let’s check out what it does.

It appears the file is trying to run the command `thm` but the OS is unable to find it in `$PATH`. We know that `/home/murdoch` is a writable folder, so we will create a binary named `thm` in that folder and make the binary spawn a shell. However, we will need to add the folder to `$PATH` first.

The example shows us how to add `/tmp` to `$PATH` , but we will replace `/tmp` with `/home/murdoch`. Note that it would be better to perform the exploit through `/tmp` as interfering with a user’s home directory is not the best idea, but we are not working on a real engagement, so we might as well.

Now, we will create an executable named `thm` in the `/tmp/murdoch` directory and make it spawn a shell.

Let’s carry out the same steps.

There we go. Now, if we run the `test` script, it should hopefully try to run the `thm` binary within `/home/murdoch`, which will give us a `root` shell. Let’s see how that works out.

And we have `root`. Clean and simple.

Now, let’s read the contents of `flag6.txt`.

There we go. That was fun.

## Q: What is the content of the flag6.txt file?

Let’s submit the flag as we have already read the contents of the `flag6.txt` file.

**Answer:** `THM-736628929`

# Task 11 — Privilege Escalation: NFS

## Q: How many mountable shares can you identify on the target system?

Let’s begin with the official guide.

We need to run the command shown above on our local machine. Let’s do it.

We can see that the target system has three mountable shares.

**Answer:** `3`

## Q: How many shares have the “no\_root\_squash” option enabled?

Let’s check out the official guide again.

Let’s check out the `/etc/exports` file on the target system.

We can see the three mounts listed at the bottom, and they all have the `no_root_squash` option enabled.

**Answer:** `3`

## Q: Gain a root shell on the target system

The guide tells us how we can exploit the `no_root_squash` option on a mountable share.

Let’s continue following the guide on how to leverage this vulnerability to gain a `root` shell on the target system.

As suggested, we will first create a temp folder and mount one of the `no_root_squash` shares to our local machine. Then, we will create a simple executable that will spawn a shell.

We have mounted `/home/backup` folder to `/tmp/test` and created `exploit.c` containing a simple shell-spawning script. Note that we need `sudo` privileges to mount the folder, and we will need them to perform any actions on that folder. The `-o` flag of the `mount` command is used to specify additional options or parameters. We are using the parameters `rw`, which stands for `read-write`, specifying read and write permissions to the mounted folder.

Now, let’s compile the code and set the SUID bit.

Let’s check whether the files reflect in the folder that we have mounted — `/home/backup` on the target system.

Well, although most of the information is not provided for some reason, we have confirmed that the files exist on the target system. Let’s try executing `exploit` and hopefully pop a root shell.

Turns out, we do not have `execute` permissions on the `/home/backup` folder. A lot of time seemingly wasted but something to learn nonetheless.

Let’s try the whole thing again, but this time with the `/tmp` folder.

Now, let’s check the situation of the target machine’s mounted folder — `/tmp`.

Perfect! We have got it working. Let’s execute `exploit` to finally pop a root shell.

Not so fast, I guess!

At this point, I realised I wouldn’t be able to pop a `root` shell anyway because I created the exploit on my local machine through a standard user account — kali — as can be seen in the screenshots above. Accordingly, on the target machine, the owner of the exploit is ‘ubuntu’, not the root user. So, even if the exploit were to be executed, I would pop a standard shell, not a root shell. So, I had to redo the entire process through the root user account. Moving on . . .


After some google-fu, I found three seemingly workable bypasses: using a helper script called `XenSpawn`, which can be found [here](https://github.com/X0RW3LL/XenSpawn); adding the `-static` option to the compiler command for static linking; and dependency bundling using `LD_LIBRARY_PATH`.

Let’s try the easy and obvious static flag.

We can also confirm that the executable `exploit` is owned by `root` this time around. Let’s run it.

And we finally have a `root` shell. This part took a lot of going back and forth and more time than expected, but it was a worthy learning experience.

## Q: What is the content of the flag7.txt file?

We have a root shell on the machine, so we will simply locate the flag7.txt file and print its contents to the terminal.

Finally, ending on a high.

**Answer:** `THM-89384012`

We are all done with the guided tasks in the Linux Privilege Escalation room. We will go through the final task — Capstone Challenge — soon Insha’Allah. Until then, take care!
