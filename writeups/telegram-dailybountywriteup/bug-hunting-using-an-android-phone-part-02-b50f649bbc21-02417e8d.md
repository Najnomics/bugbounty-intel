# Bug Hunting Using an Android phone -Part 02

- **Source URL:** https://cybrox.medium.com/bug-hunting-using-an-android-phone-part-02-b50f649bbc21
- **Fetched from:** https://cybrox.medium.com/bug-hunting-using-an-android-phone-part-02-b50f649bbc21?source=rss-199c59d958d5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14940 (id 14940)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** None / Fri, 09 Oct 2026 05:42:18 GMT

If you don’t read my first article yet, about “How to start Bug Hunting Using an Android phone -Part 01. Then read the first article, before you read this article. My First article link:

[https://medium.com/@shawon22re/how-to-start-bug-hunting-using-an-android-phone-part-1-7c010740b0cc](https://medium.com/@shawon22re/how-to-start-bug-hunting-using-an-android-phone-part-1-7c010740b0cc)

Modern web applications often communicate with APIs.

While testing an authorized application, you may discover endpoints such as:

/api/login

/api/profile

/api/orders

/api/users

/api/products

/api/password-reset

Don't immediately assume that an endpoint is vulnerable.

1\. What does the endpoint do?

2. Who can access it?

3. What parameters does it accept?

4. Does it require authentication?

5. Does the server properly validate input?

6. Does changing an identifier expose another user's data?

This mindset is much more valuable than simply running automated scanners.

Vulnerabilities You Can Learn on Android

A phone-based setup is suitable for learning many web vulnerabilities, including:

Check whether a normal user can access functionality or information intended for another user.

Look for sensitive information exposed through:

\- Error messages

- Debug pages

- API responses

- Public files

- Misconfigured endpoints

Study problems involving:

\- Login

- Logout

- Password reset

- Email verification

- Session management

If an application uses identifiers such as:

/account?id=100

you can study whether changing the identifier causes unauthorized access.

Only perform this type of testing on accounts and systems where you have permission.

You can learn how browsers enforce cross-origin policies and investigate whether an application's CORS configuration improperly trusts untrusted origins.

Input Validation

Test how applications handle unexpected but harmless input and observe whether the application properly validates and sanitizes it.

One of the best ways to practice web security legally is through intentionally vulnerable training environments such as PortSwigger Web Security Academy.

Instead of testing random websites, you can reproduce vulnerabilities in a controlled environment.

For example, you can study:

\- SQL injection

- Authentication vulnerabilities

- Access control

- SSRF

- CORS

- XXE

- Command injection

- WebSockets

- File upload vulnerabilities

- Business logic vulnerabilities

This is especially useful for Android users because you can combine the browser, Termux, and an HTTP inspection application while following the lab instructions.

Bug hunting from Android is possible, but it has limitations.

A phone may make it harder to:

\- Manage many requests simultaneously

- Use advanced interception features

- Work with large wordlists

- Run heavy scanners

- Analyze large amounts of data

- Use complex browser developer tools

- Maintain multiple applications side-by-side

You may therefore need to adapt your workflow.

Instead of trying to reproduce a desktop setup exactly, focus on understanding the vulnerability and finding a practical mobile workflow.

A Simple Android Bug-Hunting Workflow

A beginner can follow this process:

1\. Choose an authorized target

↓

2. Read the program's scope

↓

3. Perform passive reconnaissance

↓

4. Explore the application manually

↓

5. Identify interesting endpoints

↓

6. Understand requests and responses

↓

7. Create a testing hypothesis

↓

8. Test safely

↓

9. Reproduce the issue

↓

10. Document the impact

↓

11. Submit a clear report

The most important step is reproduction.

Finding something strange is not enough. You need to demonstrate that the behavior is actually a security issue and explain its impact clearly.

Final Thoughts

You don't need an expensive laptop to begin learning cybersecurity.

An Android phone with Termux, a browser, an HTTP inspection tool, and access to legal training labs can provide a surprisingly capable learning environment.

However, remember that tools don't make the hacker — understanding does.

Learn HTTP. Understand authentication. Study how applications process data. Read documentation. Practice in legal labs. Take detailed notes. Then gradually move toward real bug bounty programs that explicitly allow your testing.

Your phone may be limited compared with a full desktop setup, but it is more than enough to start building the skills required for web security research.

Start small. Understand deeply. Test responsibly.
