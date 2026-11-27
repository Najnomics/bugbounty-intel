# What is server-side template injection?

- **Source URL:** https://cyberw1ng.medium.com/what-is-server-side-template-injection-77b7e4d0cad2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241210083025/https://cyberw1ng.medium.com/what-is-server-side-template-injection-77b7e4d0cad2
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5910 (id 5910)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# What is server-side template injection?

## Server-side template injection is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side. Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, rather than passed in as data | Karthikeyan Nagaraj

8 min readApr 21, 2024

# What is server-side template injection?

Server-side template injection is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed server-side.

Template engines are designed to generate web pages by combining fixed templates with volatile data. Server-side template injection attacks can occur when user input is concatenated directly into a template, rather than passed in as data. This allows attackers to inject arbitrary template directives in order to manipulate the template engine, often enabling them to take complete control…
