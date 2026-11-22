# Broken access control (username or email enumeration)

- **Source URL:** https://medium.com/@ahany8591/broken-access-control-username-or-email-enumeration-a6e9493fffb5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142204/https://medium.com/@ahany8591/broken-access-control-username-or-email-enumeration-a6e9493fffb5
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3938 (id 3938)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken access control (username or email enumeration)

In this writup i will share with you a vulnerability that some companies accept it and some not according to the situation case.

in this login page:

proof of concept is very simple in the following two photos i will enter on correct username and one wrong one and see for the existing one redirect me to enter the password:

while wrong ones keep saying {The username you entered is not valid.}

and didn’t redirect me to enter the password:

The right form to response to invalid username is **Login failed; Invalid user ID or password,**This does not inform the attacker on which credential is wrong and makes enumeration more difficult.

## Impact:

1. **BRUTE FORCING PASSWORDS**
Once an attacker has a list of valid usernames, they can then easily target those users for common passwords. On a large platform, how many users have a password of Password@123?
2. **CREDENTIAL STUFFING**
An attacker can use the usernames identified to search existing compromised databases for passwords. Chances are your users have identical usernames on other platforms, and may have used identical passwords as well.

3\. **SOCIAL ENGINEERING**

After learning usernames, an attacker can likely identify the names of those users and attempt to contact them directly with social engineering campaigns.

Unfortunately, the program says its **Dublicate**

Always keep trying to reach your goal, **Happy Hacking**
