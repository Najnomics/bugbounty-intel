# IDOR Allowing to Place Other Students in Exam Sessions

- **Source URL:** https://medium.com/@mr_payload_injector/idor-allowing-to-place-other-students-in-exam-sessions-1bbefd14ac8d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219225508/https://medium.com/@mr_payload_injector/idor-allowing-to-place-other-students-in-exam-sessions-1bbefd14ac8d
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5105 (id 5105)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR Vulnerability Allowing to Place Other Students in Exam Sessions

--

# Introduction

Hello ethical hackers, hope you are doing well!

On a university portal, an IDOR vulnerability was found allowing you to place other students in an exam session.

# What is an IDOR?

IDOR stands for Insecure Direct Object Reference, and it refers to a type of security vulnerability that occurs when an application provides direct access to objects based on user-supplied input. In simpler terms, it occurs when an attacker can manipulate input to access, modify, or delete objects (such as files, database records, or user accounts) that they are not authorized to access.

# Vulnerability Explanation

The portal has a feature where you can register for an exam session. The registration URL ends with the student application number. When seeing a number in a URL, you should start playing with it! The URL ends with:

`?applicationno=XXXXXXX`
The application number is a 7 digits incremental integer number. For example, if your number is 2189324, changing the application number to 2189325 will let you place another student in an exam session and so on for all application numbers.

# Vulnerability Proof of Concept

1. Choose the option of registering for an exam session.
2. Before registering, change the application number in the opened URL to be equal to another application number.
3. The registration page will now display name and student ID of the other student you entered his/her application number in the URL.
4. Now, you can register an exam session for this student.

# Impact

Privacy Violation: A user should be able only to register him/her self in an exam session, not other students.

Thanks for reading this simple article. Happy ethical hacking!
