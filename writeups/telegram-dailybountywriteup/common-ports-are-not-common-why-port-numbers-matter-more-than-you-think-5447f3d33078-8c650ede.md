# Common Ports Are Not Common

- **Source URL:** https://sukhveersingh97997.medium.com/common-ports-are-not-common-why-port-numbers-matter-more-than-you-think-5447f3d33078
- **Fetched from:** https://sukhveersingh97997.medium.com/common-ports-are-not-common-why-port-numbers-matter-more-than-you-think-5447f3d33078?source=rss-8b2cfce9f882------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14928 (id 14928)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sukhveer Singh / Wed, 30 Sep 2026 04:16:52 GMT

*You see port 22 open. You think SSH.*

*You see port 80 open. You think HTTP.*

*You see port 3306 open. You think MySQL.*

But what if I told you that this simple assumption can sometimes lead you in the wrong direction?

One of the first things cybersecurity students learn is a list of common ports:

**21 → FTP**

**22 → SSH**

**23 → Telnet**

**25 → SMTP**

**53 → DNS**

**80 → HTTP**

**443 → HTTPS**

**445 → SMB**

**3306 → MySQL**

**3389 → RDP**

It looks simple.

Almost too simple.

And that’s where the problem begins.

A port number is not a guarantee of what is running behind it.

It is a **clue**.

And for anyone learning penetration testing, vulnerability assessment, network security, or bug hunting, understanding that difference can completely change the way you approach reconnaissance.

Imagine you’re performing reconnaissance on a server.

You run a basic scan and receive something like:

PORT     STATE    SERVICE

22/tcp open ssh

80/tcp open http

443/tcp open https

3306/tcp open mysql

At first glance, everything looks familiar.

You might immediately think:

*“Okay, SSH is on 22, HTTP is on 80, HTTPS is on 443, and MySQL is on 3306.”*

But a more experienced security tester asks a different question:

***“What is actually listening on these ports?”***

That single question is incredibly important.

Port numbers are assigned to services and protocols through registries, and many well-known services have conventional ports. For example, IANA lists FTP control on port 21 and SSH on port 22, while HTTP is registered on port 80.

But a service does not have to live on its traditional port.

Nmap’s own documentation explicitly warns that services can run on unusual or non-standard ports.

That’s why **port scanning is only the beginning of reconnaissance — not the conclusion.**

Before we talk about security, let’s make the concept simple.

Think of an IP address as the **address of a building**.

The port is the **door number**.

The IP address tells you:

*“Which machine?”*

The port tells you:

*“Which network endpoint on that machine?”*

For example:

192.168.1.10:22

can be thought of as:

Machine → 192.168.1.10

Port → 22

A server can have many ports available at the same time.

22     → Remote administration

80 → Web application

443 → Secure web application

3306 → Database

Each service can listen for network connections on a particular port.

IANA divides port numbers into three major ranges:

These ranges help organize port assignments, but the number itself should not be treated as proof of the application behind it.

This is probably the most important lesson in this entire article.

If you see:

22/tcp open

you can reasonably suspect SSH.

But you should not automatically conclude:

*“This is definitely SSH.”*

Why?

Because administrators can configure applications to listen on different ports.

HTTP → 8080

SSH → 2222

MySQL → 3307

There is nothing magical about port 22 that forces SSH to exist there.

Likewise, something unexpected could be listening on port 22.

Nmap documentation gives exactly this warning: its service database can make educated guesses based on well-known ports, but real services can run on unusual ports. That’s why Nmap provides service/version detection.

This leads to a fundamental penetration-testing principle:

***Don’t trust the port. Identify the service.***

If ports are not absolute, why bother learning them?

Because common ports are still extremely useful.

They give you a **starting point**.

Imagine receiving this scan:

21/tcp   open

22/tcp open

80/tcp open

443/tcp open

445/tcp open

3306/tcp open

3389/tcp open

Even before identifying the exact applications, you already have useful information.

You can start forming hypotheses.

Likely FTP.

Possible investigation areas include:

Likely SSH.

Likely HTTP.

Now you may have a web application to investigate.

That opens a completely different security-testing path:

Likely HTTPS.

Now you can investigate:

Likely MySQL.

This immediately tells you:

*“There may be a database service exposed here.”*

That’s potentially significant because databases are normally expected to have carefully controlled network access.

Likely RDP.

That suggests a Windows remote desktop service may be present.

The point isn’t that every open port is vulnerable.

The point is that **every open port expands your understanding of the attack surface.**

Here’s the mental cheat sheet every beginner should know.

PortCommon ServiceWhat It Usually Indicates**21**FTPFile transfer**22**SSHSecure remote administration**23**TelnetLegacy remote access**25**SMTPEmail transfer**53**DNSDomain-name resolution**80**HTTPWeb traffic**443**HTTPSEncrypted web traffic**445**SMBWindows file/printer sharing**3306**MySQLMySQL database**3389**RDPWindows Remote Desktop

These are **conventional associations**, not guarantees.

That distinction is what separates memorization from actual understanding.

FTP stands for **File Transfer Protocol**.

Port 21 is traditionally associated with FTP control traffic. IANA registers FTP control on port 21.

From a security perspective, seeing FTP should make you ask:

*“Why is file transfer exposed here, and how is it configured?”*

Questions worth investigating in an authorized assessment include:

The interesting part isn’t simply:

21 = FTP

It’s:

21

↓

FTP?

↓

Which FTP implementation?

↓

Which version?

↓

Which configuration?

↓

What exposure does that create?

That’s reconnaissance thinking.

Port 22 is registered for the **Secure Shell protocol**.

SSH is widely used for secure remote administration.

For a penetration tester, an open SSH port can reveal several useful pieces of information.

22/tcp open ssh OpenSSH

is much more informative than simply:

You might want to determine:

But remember:

***An open SSH port is not automatically a vulnerability.***

Remote administration is often supposed to be exposed.

The security question is whether it is **appropriately configured and protected**.

Port 23 is traditionally associated with Telnet.

Telnet is historically important, but it is also an excellent example of why understanding a service matters more than memorizing a port.

Telnet provides remote terminal access without the protections expected from modern encrypted remote administration.

If you encounter it during an authorized assessment, its presence deserves attention.

You should ask:

*“Why is this legacy service still exposed?”*

A port number becomes interesting when you connect it to **security context**.

Port 25 is commonly associated with **SMTP**, the Simple Mail Transfer Protocol.

SMTP is part of the email ecosystem.

Seeing port 25 may tell you that the host is potentially involved in email delivery.

But don’t stop at:

25 = SMTP

Ask:

Again, the port gives you the starting point.

DNS is one of the most important services on the Internet.

It translates human-friendly names such as:

example.com

into network addresses and supports many other functions.

Port 53 is associated with DNS, but DNS commonly involves **both TCP and UDP**, depending on the operation.

During reconnaissance, DNS can become extremely valuable because it can reveal information about the infrastructure you’re authorized to assess.

example.com

api.example.com

mail.example.com

dev.example.com

vpn.example.com

The interesting discovery isn’t simply:

*“Port 53 is open.”*

It is:

*“What does this DNS service tell me about the environment?”*

Now we reach one of the most interesting ports for web security professionals.

**Port 80 → HTTP**

HTTP is traditionally associated with unencrypted web traffic, and IANA registers HTTP on port 80.

If you’re interested in:

then port 80 is extremely important.

But don’t simply open the website and stop.

Think about the application.

Look for:

/

├── login

├── admin

├── api

├── dashboard

├── upload

├── user

├── account

└── internal

A web port can lead to an enormous application attack surface.

And here’s another important lesson:

***The web doesn’t belong exclusively to port 80.***

Web applications can run on many other ports.

8080

8000

8008

3000

5000

8443

9000

So if your reconnaissance only checks port 80 and 443, you may miss web applications.

Port 443 is commonly associated with HTTPS.

But HTTPS is not simply:

*“HTTP + port 443.”*

It involves HTTP carried over TLS.

That distinction matters because encryption protects communication in transit, but it doesn’t automatically make the application secure.

You can have:

HTTPS

+

Broken authorization

or:

HTTPS

+

SQL injection

HTTPS

+

IDOR

HTTPS

+

XSS

TLS can protect the connection while the application itself contains serious security weaknesses.

That’s why:

***Encryption ≠ Application Security***

Port 445 is commonly associated with **SMB**, especially in Windows environments.

SMB is used for functions such as file and printer sharing.

If you encounter SMB during an authorized internal assessment, it can provide valuable information about the Windows environment.

Questions might include:

The important concept is that a network service represents functionality.

And functionality creates attack surface.

Port 3306 is commonly associated with MySQL.

Now imagine you scan an Internet-facing server and see:

3306/tcp open mysql

Your first thought should not be:

*“I found a database, let’s attack it.”*

Instead:

***“Why is this database network-accessible?”***

That is a much better security mindset.

Databases frequently contain valuable application data.

A production architecture may intentionally restrict database access so that only application servers or specific internal systems can reach it.

Therefore, an exposed database service can be an important architectural finding — even when the database software itself is fully patched.

Port 3389 is commonly associated with **Remote Desktop Protocol (RDP)**.

RDP is widely used for remote Windows administration.

From a defensive perspective, Internet exposure of administrative interfaces deserves careful review.

From a penetration-testing perspective, you might investigate:

Again:

3389 open

doesn’t automatically mean:

3389 vulnerable

It means:

***There is a remote service that deserves identification and contextual analysis.***

Let’s return to our original scan.

21/tcp    open

22/tcp open

80/tcp open

443/tcp open

3306/tcp open

A beginner may create a table:

21  → FTP

22 → SSH

80 → HTTP

443 → HTTPS

3306 → MySQL

An experienced tester creates hypotheses:

21  → Probably FTP → Identify service/version

22 → Probably SSH → Identify implementation/config

80 → Probably HTTP → Enumerate application

443 → Probably HTTPS → Enumerate TLS + application

3306 → Probably MySQL → Identify exposure/configuration

That small difference represents a huge change in methodology.

This is where tools such as Nmap become useful.

A basic port scan can tell you:

80/tcp open

Service/version detection can attempt to determine what is actually running.

nmap -sV 192.168.1.10

Nmap’s -sV functionality interrogates open ports and attempts to identify the protocol, application, version, and sometimes additional information such as hostname, device type, operating-system family, or CPE data.

You might get something like:

PORT    STATE SERVICE VERSION

22/tcp  open  ssh     OpenSSH

80/tcp open http Apache httpd

443/tcp open ssl/http Apache httpd

Now your reconnaissance has become much more useful.

Instead of asking:

*“Which ports are open?”*

you’re asking:

***“Which services are exposed, what software implements them, and what does that exposure mean?”***

This is one of the biggest mistakes beginners make.

Imagine you’re scanning an authorized target and discover:

8080/tcp open

You think:

*“Nothing important. It’s not 80.”*

Wrong assumption.

8080 is frequently used for web applications, proxies, development environments, and management interfaces.

Or you discover:

2222/tcp open

Don’t assume it’s irrelevant just because SSH isn’t on 22.

It could be SSH.

It could be something else.

The correct approach is identification.

Nmap’s documentation specifically notes that services may be configured on unusual ports and explains why version detection is useful for identifying what is actually running.

Here’s a simple methodology you can remember.

Example:

What protocol is speaking here?

Apache

Nginx

OpenSSH

Microsoft IIS

MySQL

PostgreSQL

Apache httpd 2.x

This is where things become interesting.

Only now should you begin asking:

*“Is there a security issue?”*

This prevents a common beginner mistake:

**seeing a service and immediately assuming vulnerability.**

Here’s another mental model.

Imagine a house.

The house has:

Front door

Back door

Garage

Windows

Basement

Roof access

Every accessible entry point increases the number of ways someone might interact with the building.

A server is similar.

22  → SSH

80 → Web

443 → HTTPS

445 → SMB

3306 → Database

3389 → RDP

Each exposed service represents a **network-facing interface**.

But exposure doesn’t automatically mean vulnerability.

The risk depends on things such as:

**Service + Version + Configuration + Authentication + Authorization + Network Exposure + Application Logic**

That’s why security professionals don’t simply count open ports.

They interpret them.

Let’s look at several mistakes beginners frequently make.

Not necessarily.

It’s a strong clue, but service detection provides stronger evidence.

A web application could be running on another port.

No.

An open service is not automatically a vulnerable service.

HTTPS protects communication in transit. Application vulnerabilities can still exist.

Definitely not.

Common ports are useful for quick reconnaissance, but unusual ports can expose important services.

Nmap supports targeted and broader port-scanning approaches, including scanning top ports and specific port ranges.

Imagine a company tells you:

*“Our website is secure.”*

You test:

You find:

80

443

You perform a web assessment.

But suppose the same server also exposes:

22

8080

8443

3306

Now your understanding of the environment changes.

Maybe:

80  → Main website

443 → Main website

8080 → Development application

8443 → Admin interface

3306 → Database

22 → SSH

The web application might be perfectly secure.

But the overall server exposure may still deserve investigation.

This is why **attack-surface discovery comes before vulnerability hunting.**

You don’t need to memorize hundreds of port numbers immediately.

Start with the important ones.

21 → FTP

22 → SSH

23 → Telnet

3389 → RDP

80 → HTTP

443 → HTTPS

8080 → Common alternate HTTP

8443 → Common alternate HTTPS

25 → SMTP

53 → DNS

445 → SMB

3306 → MySQL

Then expand your knowledge gradually.

The goal isn’t:

*“I memorized 100 port numbers.”*

The goal is:

***“I can look at a network service and understand what it might mean.”***

If you’re learning ethical hacking or penetration testing, think about your workflow like this:

Target

↓

Port Discovery

↓

Open Ports

↓

Service Identification

↓

Version Detection

↓

Technology Enumeration

↓

Configuration Analysis

↓

Attack Surface Mapping

↓

Vulnerability Testing

↓

Validation

↓

Reporting

Notice something important.

**Vulnerability testing comes relatively late.**

A common beginner mistake is jumping directly from:

Port 80

to:

SQL Injection!!!

Good security testing is more methodical.

First understand the environment.

Then identify the technology.

Then understand how it works.

Then test the relevant security assumptions.

This is perhaps my favorite way to think about reconnaissance.

Imagine you scan a server and find:

22

80

443

3306

That’s not just four numbers.

It’s a story.

Maybe the server is:

Linux server

+

SSH administration

+

Web application

+

HTTPS

+

Database

Now imagine:

80

443

8080

8443

That’s a different story.

Maybe you’re looking at:

Public web application

+

HTTPS

+

Development server

+

Administrative web interface

And:

445

3389

might suggest a Windows-oriented environment.

The port numbers don’t give you the complete story.

But they give you **chapters**.

Your job during reconnaissance is to read the rest.

There are two ways to approach a port scan.

*“Port 22 is SSH.”*

*“Port 22 is commonly associated with SSH. Let’s verify what’s actually listening and understand its exposure.”*

*“3306 means MySQL.*

*“3306 commonly indicates MySQL. Why is a database service exposed, what implementation is running, and is this exposure intended?”*

*“443 means secure.”*

*“HTTPS provides encrypted transport, but I still need to assess the application and its security controls.”*

*“Only common ports matter.”*

*“Common ports are useful starting points, but non-standard ports can host important services too.”*

That mindset shift is what turns a list of port numbers into a reconnaissance skill.

If you’re learning this in a legal lab environment, create a small virtual network with systems you own or are authorized to test.

Run a basic scan:

nmap \<LAB-IP>

Then try service detection:

nmap -sV \<LAB-IP>

Compare the results.

Ask yourself:

You are no longer just scanning ports.

You’re building a **network attack-surface map**.

Always perform scans only against systems you own or have explicit permission to test.

Don’t remember ports as isolated numbers.

Remember them as questions.

PortCommon AssociationSecurity Question**21**FTPWhy is file transfer exposed?**22**SSHHow is remote administration protected?**23**TelnetWhy is this legacy remote-access service present?**25**SMTPWhat mail service and configuration are exposed?**53**DNSWhat infrastructure information does DNS reveal?**80**HTTPWhat web application is exposed?**443**HTTPSWhat TLS and application controls are present?**445**SMBWhat Windows resources are exposed?**3306**MySQLWhy is the database network-accessible?**3389**RDPHow is remote desktop access protected?

That’s a much more useful cheat sheet than simply memorizing:

21 = FTP

22 = SSH

23 = Telnet

...

The biggest lesson isn’t that you should memorize port numbers.

It’s that **you should stop treating port numbers as answers.**

A port number is a clue.

A service is evidence.

A version gives you context.

A configuration gives you more context.

And the actual security risk depends on the entire environment.

So the next time you see:

don’t immediately think:

*“SSH.”*

Think:

***“SSH is likely. Now let’s verify it.”***

When you see:

3306/tcp open

*“MySQL vulnerability.”*

***“A database service may be exposed. Why? What is it? How is it configured?”***

And when you see:

443/tcp open

don’t think:

*“Secure website.”*

***“Encrypted transport. Now what application is behind it?”***

That is the difference between **memorizing cybersecurity** and **thinking like a security professional**.

The port is only the door.

Your job is to understand **what is behind it**.

Remember this five-line methodology:

PORT

↓

SERVICE

↓

VERSION

↓

CONFIGURATION

↓

RISK

**Don’t just ask what port is open.**

***What is actually running there, why is it exposed, and what does that exposure mean?***

That’s where real reconnaissance begins.
