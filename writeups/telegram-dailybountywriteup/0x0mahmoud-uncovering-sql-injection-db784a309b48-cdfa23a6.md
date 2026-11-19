# Uncovering SQL Injection

- **Source URL:** https://medium.com/@0x0mahmoud/uncovering-sql-injection-db784a309b48?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250914072848/https://medium.com/@0x0mahmoud/uncovering-sql-injection-db784a309b48
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10418 (id 10418)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Uncovering SQL Injection

**Hello everyone!**

I hope you’re doing great. its my first writup for critical bug i found in The last month of last year

## Introduction

### What is SQL Injection?

**SQL Injection (SQLi)** is a serious **web security vulnerability** that allows an attacker to manipulate how a website interacts with its **database**. It happens when a web application **does not properly validate user input**, allowing malicious users to inject harmful SQL (Structured Query Language) commands into the system.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## The Reconnaissance Phase: Finding the Attack Surface

When I pick a new program to test, my first step, after understanding its scope and policies, is always to search for its “attack surface.” This means looking for all the places where I might be able to interact with the application and potentially find weaknesses.

**A quick note on P1 vulnerabilities and scope:** If you’re specifically hunting for Critical (P1) vulnerabilities, sometimes the “scope” itself becomes less restrictive. In my experience, if a domain clearly belongs to the company you’re testing, a high-impact vulnerability discovered on it is often accepted, even if it wasn’t explicitly listed in the initial in-scope assets. This has certainly been the case for me!

### Back to the hunt!

The first thing I do when starting reconnaissance is to leverage Google Dorking for wide-reaching target discovery.

This powerful technique allows me to leverage Google’s search capabilities to find specific files, directories, or even related subdomains that might not be immediately obvious.

In this particular assessment of `[Redacted Application]`, I focused on finding related hosts. I used various search queries, including variations similar to `"site:example-*.*.*"`. These dorks helped me uncover a number of interesting related domains and, crucially, several login portals. Each of these findings represented a potential new entry point or attack surface for further investigation.

As I gathered these results, I needed an efficient way to save them. For this, I leveraged a helpful script available for **Tampermonkey**, a popular open-source browser extension. This particular script enabled me to quickly save all the discovered links to a downloadable file with a simple keyboard shortcut. This ensured I wouldn’t miss any valuable leads and could easily refer back to my findings.

### In an upcoming section — or possibly a dedicated follow-up article — I’ll be sharing some of the most effective search queries I use during reconnaissance

## Step 2: Diving Deeper

With my list of reconnaissance targets ready, I transitioned into the active testing phase. I began by targeting **login portals**, which are often high-value areas for uncovering security weaknesses.

### Manual Testing Focus:

- **Authentication Bypass** — Attempted to access accounts without valid credentials.
- **Logic Flaws** — Investigated potential design or input-handling weaknesses within the login process.

The login interface resisted all my attempts — no security issues were discovered.

I then expanded testing to other input vectors across the application. I looked specifically for **injection vulnerabilities**, including SQLi, XSS, and others.

To support my manual work, I initiated **automated crawling and fuzzing** using tailored wordlists. This step aimed to uncover:

- Hidden or unlinked pages
- Uncommon directories

Even after this intensive round of probing, the application remained secure, with no critical vulnerabilities uncovered during this stage.

## The Turning Point: Discovering Hints From The Web Archive

Since live testing hadn’t exposed any vulnerabilities, I shifted my focus to historical data. While reviewing archived versions of the application through the Wayback Machine, I identified **two previously available input points** — parameters that suggested interaction with the backend database, even though they were no longer present in the current live version.

To assess their security, I tested both using a simple yet effective method: injecting a **single quote (')**, a classic way to check for SQL injection. One of the inputs responded normally, with no indication of vulnerability. However, the **second entry point** returned a clear SQL syntax error—an immediate red flag that indicated the input was being processed directly by the database without proper sanitization.

Sure enough, when I submitted the input, the application returned a clear and revealing error message:

You have an error in your SQL syntax; check the manual that corresponds to your PostgreSQL server version for the right syntax to use near ‘…’ at line24


This was the breakthrough I had been looking for.

The message confirmed two key things:

- The application was using **PostgreSQL** as its backend database.
- The input I submitted was being directly processed by the SQL engine without proper sanitization or validation.

The inclusion of *line 35* in the error gave an extra clue — it indicated exactly where my input disrupted the underlying query. This strongly suggested a classic **SQL Injection flaw**, and validated that the parameter I tested was unsafely connected to the database logic.

## Phase 3: Exploitation — Confirming the SQL Injection

After confirming the SQL syntax error with the single quote, it was time to move to the exploitation phase. This is where you figure out exactly what kind of SQL Injection you have and what information or control it allows.

To do this efficiently, I used an automated SQL Injection tool (like **Ghauri**, as shown in the image). These tools are designed to automatically test for different SQL Injection types and help pull data from the database.

The tool quickly confirmed two types of SQL Injection vulnerabilities:

*Boolean-based Blind SQL Injection*

*Stacked Queries SQL Injection*


The automated tool also successfully identified the backend database system and its version: **PostgreSQL version 12.20 (64-bit)**.

This confirmation of both Boolean-based blind and, especially, Stacked Queries SQL Injection on a PostgreSQL database pointed to a severe security flaw. This bug could potentially lead to full data theft or even allow an attacker to run their own code on the database server.

Thank you.
