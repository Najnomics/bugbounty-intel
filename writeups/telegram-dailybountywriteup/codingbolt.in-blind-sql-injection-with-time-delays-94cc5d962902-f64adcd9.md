# Blind SQL injection with time delays

- **Source URL:** https://medium.com/@codingbolt.in/blind-sql-injection-with-time-delays-94cc5d962902?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501131526/https://medium.com/@codingbolt.in/blind-sql-injection-with-time-delays-94cc5d962902
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7448 (id 7448)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# **Blind SQL injection with time delays**

*Blind SQL Injection with Time Delays: A Stealthy Attack Unveiled*

In the world of cybersecurity, few vulnerabilities are as silent and sneaky as Blind SQL Injection. Unlike traditional SQL injection attacks where attackers receive immediate, visible feedback from the database, Blind SQL Injection operates in the dark, providing no visible clues to the attacker. Instead, it relies on subtle changes in application behavior, such as time delays — a technique that allows attackers to extract data bit by bit, even without any visible response.


*This article delves into Blind SQL Injection with Time Delays, revealing how it works, why it’s dangerous, and how it can be prevented.*

# What is Blind SQL Injection?

Blind SQL Injection occurs when a web application is vulnerable to SQL injection but doesn’t return any visible output or error messages. Instead of directly revealing sensitive data, the application might behave differently depending on the attacker’s input — such as taking longer to load or redirecting to another page.

Because of the absence of visible feedback, attackers need to infer the results of their queries. They do this by sending a series of true/false conditions to the database, and then analyzing the time it takes for the application to respond. Over…
