# Directory Traversal and LFI worth $400

- **Source URL:** https://medium.com/@hritkmjth/directory-traversal-and-lfi-worth-400-c4422785d3bd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250224102523/https://medium.com/@hritkmjth/directory-traversal-and-lfi-worth-400-c4422785d3bd
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2040 (id 2040)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Directory Traversal and LFI worth $400

--

**A Directory Traversal and Local File Inclusion bug couldn’t be simpler than this, which eventually led to a bounty worth $400.**

Hi! I am Hritik and this write-up is mainly for the beginners in the field of bug bounty. By reading this, I can assure you that you’ll have a new hope of finding a good bug just by paying attention to the URL, even if you are a complete beginner. So, let’s start.

*If you already know about directory traversal and LFI, you can skip to Vulnerability section.*

**What is Directory Traversal?**

Directory Traversal is a vulnerability that allows an attacker to navigate through directories on the server, potentially accessing files that they should not have access to. This can be particularly dangerous if the attacker is able to navigate to sensitive directories, such as those containing configuration files or databases. In my assessment, I discovered that the website was vulnerable to Directory Traversal through an input parameter.

**What is Local File Inclusion (LFI)?**

Local File Inclusion (LFI) is a type of vulnerability that allows an attacker to access sensitive information stored on the web server by including local files into a page being served to the user. Essentially, this means that an attacker can access files on the server that they should not have access to, such as configuration files or even passwords. In my assessment, I discovered that the website was vulnerable to LFI through the same parameter that was vulnerable to directory traversal.

**Vulnerability**

While doing recon for *redacted.com* (A private VDP and as per their privacy policies, I cannot disclose their name), I found an endpoint in the web app, say “*redacted.com/media?fp=../content/”.*

You know already 😉.

So without a do, I tried for directory traversal hitting “*redacted.com/media?fp=../../../../../”* and with no surprise the directories in the server were listed.

However, listing the directory names is of little or no impact unless you can list a sensitive information with the help of this. So, now I had to list the files which could potentially contain sensitive information.

I tried a couple of ways to list the files such as:

*redacted.com/media.html?fp=../../../../../*

*redacted.com/media.php?fp=../../../../../*

*redacted.com/media.txt?fp=../../../../../*

*redacted.com/media/index.html?fp=../../../../../*

etc..

But at last, one particular endpoint worked to my surprise and that was:

*redacted.com/html?fp=../../../../../*

I then traversed through the directories using directory traversal to find the sensitive directories and found a directory named **database-dump**. Upon looking at the contents of the directory, I was able to find database dumps, which contained username and passwords along with that of the admin account. I cracked the password (hashed with SHA1) of the admin account and was able to successfully take over the web application.

**Learning**:

Surf through the web application before you blindly start throwing payloads and performing automated scan checks because you never know how low the fruit might be hanging there.

**Disclosure:**

Reported to redacted.com on 04 March 2022.

Got reply from redacted.com on 06 March 2022 and was asked to confirm my identity.

Replied back with identity confirmation on 09 March 2022.

redacted.com confirmed the identity and awarded bounty worth NRs. 50,000 (\~$400) on 17 March 2022.

Thanks and regards!

Hritik T.

Signing out…
