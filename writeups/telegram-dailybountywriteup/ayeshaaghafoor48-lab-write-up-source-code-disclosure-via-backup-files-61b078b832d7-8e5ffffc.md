# Lab Write-up

- **Source URL:** https://medium.com/@ayeshaaghafoor48/lab-write-up-source-code-disclosure-via-backup-files-61b078b832d7?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/@ayeshaaghafoor48/lab-write-up-source-code-disclosure-via-backup-files-61b078b832d7?source=rss-1036fb23e306------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14814 (id 14814)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ayeshaaghafoor / Tue, 25 Aug 2026 09:51:14 GMT

The objective of this lab is to find a hidden backup directory via reconnaissance, analyze a leaked Java source file backup, extract a hard-coded database password, and submit it to solve the lab.

Step-by-Step Exploitation

Step 1: Discover the Hidden Directory

Access the home page of the lab.

In your browser’s address bar, append /robots.txt to the lab's main domain to check for any directories explicitly hidden from search engine crawlers.

Observe the robots.txt rule: Disallow: /backup. This leaks the existence of an unindexed /backup directory.

Figure 1: Viewing the robots.txt file to identify the restricted /backup directory path.

Step 2: Access the Backup Index

Change the URL endpoint in your browser to navigate directly to the /backup directory.

Because directory browsing is improperly configured, the server displays an open index page showing a backup file named ProductTemplate.java.bak.

Figure 2: Viewing the open directory listing on the /backup endpoint containing a Java source backup file.

Step 3: Extract the Database Password

Click on the link for ProductTemplate.java.bak or navigate directly to /backup/ProductTemplate.java.bak to read its contents.

Review the Java source code structure. Within the database connection block (ConnectionBuilder.from(...)), locate the hard-coded parameters for the PostgreSQL driver connection.

Identify and copy the long string parameter value representing the database password (e.g., nyrg4gmcxnz9wwhd4a6dfvkflun5c3zx).

Figure 3: Reviewing the leaked Java source code to extract the hard-coded database credential string.

Step 4: Submit Solution

Copy the extracted password string.

Return to the main lab interface banner, click Submit solution, paste the password text, and click OK to solve the lab.

Remediation

Leaving source code or backup artifacts in a web-accessible directory allows attackers to reconstruct database logic and steal secrets. Fix this vulnerability with the following controls:

Remove Non-Production Files: Never store editor backup files (\*.bak, \*.swp), old versions, or raw source text code inside the public web document root (public\_html, www).

Disable Directory Browsing: Configure the web server (Apache, Nginx, IIS) to disable directory listings globally so users cannot view structural file lists if an index file is absent.

Externalize Sensitive Credentials: Avoid hard-coding application secrets or infrastructure passwords into code files. Use environmental variables or a dedicated key-management system instead.
