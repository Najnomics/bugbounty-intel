# A bug that permitted bypassing of Facebook’s two-factor authentication (2FA) was discovered by a…

- **Source URL:** https://medium.com/@dkjhaj2ee/a-bug-that-permitted-bypassing-of-facebooks-two-factor-authentication-2fa-was-discovered-by-a-8ba35eca70e9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230201054833/https://medium.com/@dkjhaj2ee/a-bug-that-permitted-bypassing-of-facebooks-two-factor-authentication-2fa-was-discovered-by-a-8ba35eca70e9
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1576 (id 1576)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A bug that permitted bypassing of Facebook’s two-factor authentication (2FA) was discovered by a hacker.

A flaw in a new, centralized system that Meta developed for users to manage their Facebook and Instagram logins could have made it possible for nefarious hackers to disable two-factor safeguards on an account simply by knowing the phone number of the account holder.

When a user entered the two-factor code used to log into their accounts on the new Meta Accounts Center, which enables users to link all of their Meta accounts, including Facebook and Instagram, a security researcher from Nepal, realized that Meta had not set up a limit on the number of attempts.

An attacker might use the victim’s phone number to access the centralized accounts centre, link the victim’s number to their own Facebook account, and then brute force the two-factor SMS code. Since there was no cap on how many attempts a person might make, this was the crucial phase.

Once the attacker cracked the code, his Facebook account was connected to the victim’s phone number. After a successful attack, Meta would still notify the victim that their two-factor authentication had been blocked because their phone number had been connected to another account.

According to that, cancelling anyone’s SMS-based 2FA just by knowing their phone number has the greatest impact.

Given that the target no longer had two-factor enabled, an attacker might attempt to access the victim’s Facebook account at this time by phishing for the password.

Last year, a hacker discovered the bug in the Meta Accounts Center, and he notified the business by mid-September. A few days later, Meta repaired the flaw and gave the hacker $27,200 in exchange for disclosing it.

# Conclusion

The security is a major concern for all web platforms. So the regular testing is required for this and the platform should respect if anything found like above.

Securing your online presence is crucial for protecting your personal and sensitive information from cyber threats.
