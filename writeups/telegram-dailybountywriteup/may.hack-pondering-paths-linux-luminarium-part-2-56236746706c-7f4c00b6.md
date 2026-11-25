# Pondering Paths — Linux Luminarium Part 2

- **Source URL:** https://medium.com/@may.hack/pondering-paths-linux-luminarium-part-2-56236746706c
- **Fetched from:** https://medium.com/@may.hack/pondering-paths-linux-luminarium-part-2-56236746706c?source=rss-a57e9aee68a9------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14885 (id 14885)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** mayhack / Thu, 27 Aug 2026 15:57:17 GMT

***Part 1 is already available on my profile. Check my profile if you haven’t read it yet.***

Welcome back to the **Linux Luminarium** series! 👋

In Part 1, we covered the basic idea of commands, arguments, and command history.

Now we are moving to the next module: **Pondering Paths**.

This module is all about **Linux paths** — how the filesystem is structured, how to move between directories, and how to use absolute and relative paths.

We will solve every challenge step by step and focus on **understanding why the command works**, not just copying it.

The Linux filesystem starts at /, which is called the **root directory**.

Under /, we have directories, files, programs, configuration files, and many other things.

For this challenge, a program called pwn has been placed directly inside /.

Our task is to execute it using its **absolute path**.

Since the program is located directly inside /, its absolute path is:

/pwn

We run:

hacker@paths\~the-root:\~$ /pwn

BOOM!!!

Here is your flag:

pwn.college{YPpx1o9eu3zeLicdPyZdq0pBdnl.QX4cTO0wiM2QDO1EzW}

An **absolute path** starts from the root directory /.

For example:

/pwn

/challenge/run

/home/hacker

/usr/bin

The important thing is the starting /.

So:

means:

/ → root

└── pwn

**Absolute path = path starting from /.**

It does not matter where our terminal currently is. /pwn always refers to the same location.

In PWN College, challenge programs are usually stored inside the /challenge directory.

This challenge has a program named run inside /challenge.

Therefore, its absolute path is:

/challenge/run

Our task is to execute it using that absolute path.

We can first look at our current directory:

hacker@paths\~program-and-absolute-paths:\~$ ls

COLLEGE PWN instructions mkdir myflag not-the-flag output.txt pwn the-flag x

The challenge program is not something we need to find manually.

We already know its location from the description.

So we execute:

Output:

Correct!!!

/challenge/run is an absolute path! Here is your flag:

pwn.college{ItUiWVeGxEof5rxpxcEYswD47Qg.QX1QTN0wiM2QDO1EzW}

Here we combine two ideas:

/           → root

challenge → directory

run → program

is an absolute path because it starts from /.

Linux contains a huge number of directories and files.

We can move between directories using the cd command:

cd /some/new/directory

Changing directories changes our **current working directory (cwd)**.

The challenge asks us to execute /challenge/run while our current directory is /home.

At first, we made a few mistakes.

We tried:

cd /challenge/run

but got:

bash: cd: /challenge/run: Not a directory

This makes sense because run is a **program**, not a directory.

We also tried:

cd /home/hacker /challenge/run

which resulted in:

bash: cd: too many arguments

cd expects one destination at a time.

We used:

pwd

and got:

/home/hacker

pwd means **Print Working Directory**.

It tells us exactly where our terminal currently is.

From:

we can use:

cd ..

Here .. means **the parent directory**.

/home/hacker

↑

..

moves us to:

/home

We can confirm it with:

After moving to /home, we execute:

The challenge responds:

Correct!!!

/challenge/run is an absolute path, invoked from the right directory!

Here is your flag:

pwn.college{c50FNc90EcGnmLN47rXuorMJFFw.QX2QTN0wiM2QDO1EzW}

Three commands are important here:

→ Shows where we are.

→ Moves to the parent directory.

cd /home

→ Directly moves to /home.

This challenge is similar to the previous one, but instead of changing to one directory, we have to do it **five times**.

Each time we run /challenge/run, it tells us which directory we need to move to next.

We start at:

We move to:

The challenge tells us to go to:

/etc

cd /etc

Then:

gives:

Correct!!!

Moving on to level 2

Please use the cd utility to change directory to /usr/share/build-essential

Now we move to:

cd /usr/share/build-essential

Then run:

The challenge tells us:

Moving on to level 3

Please use the cd utility to change directory to /sys

Move to:

cd /sys

The next location is:

/var/log

cd /var/log

The challenge asks us to move to:

/usr/bin

Finally:

cd /usr/bin

We get:

Correct!!!

/challenge/run is an absolute path, invoked from the right directory!

Here is your flag:

pwn.college{MIGFXFr4eLZ7Fwa1Ktyb86hQIIE.QX3QTN0wiM2QDO1EzW}

The five locations were:

/etc

↓

/usr/share/build-essential

↓

/sys

↓

/var/log

↓

/usr/bin

This challenge teaches an important habit:

**Always read the output of the program.**

The challenge itself tells us where we need to go next.

Also remember:

helps us verify our current location.

Now we move from **absolute paths** to **relative paths**.

A relative path does not start with /.

absolute: /challenge/run

relative: challenge/run

A relative path is interpreted based on our **current working directory**.

If we are currently in /:

challenge/run

points to:

The challenge asks us to first move to / and then execute the program using a relative path beginning with c.

First:

cd /

Now our current directory is:

/

We initially tried:

but the challenge rejected it:

Incorrect...

You invoked this challenge with an absolute path.

This challenge needs a relative path!

That makes sense because /challenge/run starts with /.

We need a relative path.

Since we are currently in /, we can use:

Run:

Correct!!!

challenge/run is a relative path, invoked from the right directory!

Here is your flag:

pwn.college{YD\_Qqb1s1CWKppbeCYpEaGWSU-9.QX5QTN0wiM2QDO1EzW}

The difference is simple:

starts with /, so it is **absolute**.

does not start with /, so it is **relative**.

Because our current directory is /:

current directory: /

relative path: challenge/run

actual location: /challenge/run

A relative path depends on **where you currently are**.

That’s why pwd is such a useful command when working with paths.

Linux directories contain two special entries:

.

..

The . represents the **current directory**.

So if we are inside /, these are equivalent:

challenge

./challenge

././challenge

The challenge specifically requires us to use a relative path that **starts with .**.

We first check where we are:

We need to move to /.

Now we can execute:

./challenge/run

The challenge accepts it:

Correct!!!

./challenge/run is a relative path, invoked from the right directory!

Here is your flag:

pwn.college{o5L79Pwc-z2UXhUObfEi1Ng-EL4.QXwUTN0wiM2QDO1EzW}

Suppose we are in:

.

Therefore:

current directory

↓

./challenge/run

↓

/challenge/run

The important difference is that we explicitly tell Linux:

**“Start from my current directory.”**

This challenge takes the idea of . one step further.

We need to run the challenge from:

/challenge

Normally, typing:

run

will **not** execute /challenge/run.

Linux does not automatically search the current directory when we type a naked command like run.

This is intentional because automatically searching the current directory could cause accidental execution of a malicious program with the same name as a normal system command.

Instead, we explicitly tell Linux to use the current directory with:

./

First we move to /challenge:

cd /challenge

Now:

returns:

bash: run: command not found

This is the important part of the challenge.

Even though run exists in the current directory, Linux does not automatically execute it.

We then tried:

but the challenge rejected it because that is an **absolute path**.

which failed because we were already inside /challenge.

Since we are already in:

the run program is in our current directory.

So we use:

./run

Correct!!!

./run is a relative path, invoked from the right directory!

Here is your flag:

pwn.college{YY\_aTqWfLhDK0hZfC6cPQ4V98tZ.QXxUTN0wiM2QDO1EzW}

Think of:

as:

**“where I am right now.”**

current directory + run

Since our current directory is /challenge:

./run

↓

/challenge/run

This is an extremely useful Linux concept.

When a program is in your current directory, use:

./program

instead of:

program

Every Linux user has a **home directory**.

For the hacker user in PWN College, it is:

The shell commonly starts there.

That is why we often see:

hacker@dojo:\~$

The \~ is shorthand for the user's home directory.

For hacker:

\~ = /home/hacker

Bash expands \~ when it appears at the beginning of a path-like argument.

echo \~

can produce:

This challenge adds three conditions:

The program /challenge/run will write a copy of the flag to the file path we provide.

/challenge/run \~

The shell expands:

\~

into:

So the program tried to write the flag to:

But /home/hacker is a **directory**, not a file.

Therefore, it failed:

Writing the file to /home/hacker!

/challenge/run: line 29: /home/hacker: Is a directory

So we need to specify a **file inside our home directory**.

We can use:

/challenge/run \~/f

Before expansion:

\~/f

is only a few characters long.

After Bash expands \~:

/home/hacker/f

So the program writes the flag to that file.

Terminal:

hacker@paths\~home-sweet-home:\~$ /challenge/run \~/f

Writing the file to /home/hacker/f!

... and reading it back to you:

pwn.college{IZZjIzDSAvpyQct0hmr5PSglHVd.QXzMDO0wiM2QDO1EzW}

This challenge is mainly about **shell expansion**.

We type:

but Bash expands it before the program receives the argument:

\~/f

↓

/home/hacker/f

This lets us satisfy both requirements:

Before expansion → short argument

After expansion → absolute path inside home

We could use another filename too:

/challenge/run \~/x

or:

/challenge/run \~/a

The important thing is that the final expanded path is inside:

and the original argument satisfies the length requirement.

The most important concept here is:

\~ = home directory

For our user:

Also remember that **Bash expands \~ before the command receives the argument**.

The **Pondering Paths** module introduced several important Linux concepts.

An absolute path starts from /.

/challenge/run

/home/hacker

/usr/bin

A relative path depends on our current directory.

If our current directory is /, it refers to:

means the current directory.

Example:

..

means the directory one level above the current directory.

For our hacker user:

Shows our current working directory:

Changes our current directory:

cd /tmp

cd ..

cd \~

When a program exists in the current directory, explicitly execute it using:

instead of simply:

TypeExampleMeaningAbsolute/challenge/runStarts from /Relativechallenge/runStarts from current directoryCurrent directory./runRun run from current directoryParent directory../fileGo one directory upHome\~/fileFile inside user's home

The easiest way to remember it:

/   → Root

. → Here

.. → One level up

\~ → Home

The **Pondering Paths** module taught us how Linux understands locations.

We started with the root directory /, learned how to use **absolute paths**, and then moved into **relative paths**.

The most useful things to remember are:

/   → root

. → current directory

.. → parent directory

\~ → home directory

We also learned how pwd helps us understand where we are and how cd changes our location.

Most importantly, we saw that **the same path can behave differently depending on our current working directory**.

These concepts will become extremely important in the upcoming Linux modules because we’ll start using paths with commands to access, create, move, and manipulate files.

**This is Part 2 of the Linux Luminarium series. Check my profile for Part 1 and the other upcoming parts.** 🚀

If you found this helpful and want to learn more about **web security, hands-on labs**, feel free to follow me for upcoming posts.

✍️ Follow me for more cybersecurity write-ups

🔗 **LinkedIn** — [codermayank](https://www.linkedin.com/in/codermayank/)

📸 **Instagram** — [@mayhack\_](http://instagram.com/mayhack_)

Tags: #BugBounty #EthicalHacking #CyberSecurity #Linux #PwnCollege #CTF #CaptureTheFlag #LinuxSecurity #PenetrationTesting #WebSecurity #InfoSec
