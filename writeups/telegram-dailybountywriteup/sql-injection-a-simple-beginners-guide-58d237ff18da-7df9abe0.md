# SQL Injection

- **Source URL:** https://ishengoma.medium.com/sql-injection-a-simple-beginners-guide-58d237ff18da?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240604221054/https://ishengoma.medium.com/sql-injection-a-simple-beginners-guide-58d237ff18da
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5811 (id 5811)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Introduction**

Hi everyone! I’m ***Ishengoma***, and I’ve got something cool to share with you. Ever heard of SQL injection? It’s like a secret code that can break into computer systems. Imagine your computer system as a vault holding precious information. Just like a real vault, it needs strong locks. But what if there’s a sneaky way for intruders to trick the lock and get inside? That’s where SQL injection comes in.

Now, picture our brother, [@cyb4x](http://twitter.com/cyb4x), as a mastermind who creates challenge to test our computer’s security skills. He’s built something called a lab where we can learn about SQL injection. It’s like a playground, but instead of swings and slides, you’ll find codes and databases.🤓

In this write-up, we’ll explore what SQL injection is and how it works. So, let’s dive in and discover the secrets of SQL injection together!

Now, let’s start with a short description of the challenge and its link.

So, I clicked the link, and it directed me to the login form.

I began by viewing the page source code, but nothing interesting was there. Then I moved forward to inject the login form for about 15 minutes without any good outcome. So, I went back to the challenge description hint. It state “Enumeration is the Key”🤔. Wow, I got an idea! Let’s enumerate to find the hidden directories of the site first if can see any.

I fired up a gobuster to scan hidden directories, also narrowing down the search scope to focus only on certain file types like html, js, and php.

`Command: gobuster dir -u https://#############/iaactf/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .html,.js,.php`
Wooow😱😱, I got one more directory named “register.php” with the status code of 200 means (OK). Now let’s open it on our browser tab. Before the site opened up, it displayed the message.

Now let’s open it (Press OK).

I started to look for the source code, down below I found a js file. Once I opened it, booom💥💥💥 I found the hardcoded username and password for the login page.

Now, let’s go back to the login page and try login using the credentials founded.

Finally, I’m in! While navigating on the pages on the site, on the top right corner, I found a hyperlink named profile. It seems interesting to me because there is a place where I can send something to the server through the profile updates. I tried to write there “*Hacker Ishengoma was here!*”🤓

Then the update status appeared on the left corner “*Profile updated successfully.*” see below picture!

So, I tried to write malicious input on it like ==, =, and ‘. And the one that worked is (single quote). In SQL injection attacks, attackers often exploit vulnerabilities by injecting malicious input containing a “single quote” to manipulate the SQL query structure. For example, if an application constructs a SQL query without properly sanitizing input and simply concatenates user input directly into the query string.

[LEARN MORE SQL Injection TRICKS HERE.](https://book.hacktricks.xyz/pentesting-web/login-bypass/sql-login-bypass)

And I found the error message indicating a SQL syntax issue found in the “profile.php” file on line 25 of the code.

What came to my mind first is to use SQLMap “because using SQLmap can provide a more efficient and comprehensive approach to finding and exploiting SQL injection vulnerabilities ultimately it’s help achieve better results within the given time frame.”

NB: Remember to use your cookies as your in login session.

`Command: sqlmap -u "https://#############/iaactf/profile.php?bio=1" --cookie "PHPSESSID=vuh2gp6daic4i7pv3a1ff5meg9" --dump-all`
I got several databases, but the one interested in is “u797547124\_iaactf1”, now let’s follow it to see what tables are in that DB.

`Command: sqlmap -u "https://#############/iaactf/profile.php?bio=1" --cookie "PHPSESSID=vuh2gp6daic4i7pv3a1ff5meg9" -D u797547124_iaactf1 --tables`
We got three tables, but the one that is interested in is “flag” table. Perhaps we can find our destination message/flag there. Now let’s go for the flag table and dump what is inside.

`Command: sqlmap -u "https://#############/iaactf/profile.php?bio=1" --cookie "PHPSESSID=vuh2gp6daic4i7pv3a1ff5meg9" -D u797547124_iaactf1 -T flag --dump`
**Conclusion**, In simple terms, we’ve learned that certain symbols like “=”, “‘“, and “==” and many many more can be used by hackers to mess with databases. We also see how important it is for programs to check the stuff people type in and to set things up in a smart way. Tools like SQLmap make finding and fixing these problems easier, helping to keep our online stuff safe from bad guys.

*Grateful for your presence! Feel free to ping me anytime!*
