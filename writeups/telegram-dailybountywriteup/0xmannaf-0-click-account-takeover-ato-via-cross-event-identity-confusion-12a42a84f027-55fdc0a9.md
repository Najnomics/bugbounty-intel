# 0 click Account Takeover (ATO) via Cross-Event Identity Confusion

- **Source URL:** https://medium.com/@0xmannaf/0-click-account-takeover-ato-via-cross-event-identity-confusion-12a42a84f027?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260326013456/https://medium.com/@0xmannaf/0-click-account-takeover-ato-via-cross-event-identity-confusion-12a42a84f027
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13019 (id 13019)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 0 click Account Takeover (ATO) via Cross-Event Identity Confusion

بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ | In the name of God, the most gracious, the most merciful

Hey amazing hackers, my name is **Momen Samir (0xmannaf)**. Today I’ll be discussing a bug that I recently found on a target on Bugcrowd. We will refer to it as **target.com**.

This ATO was very tricky, and I reported it twice to finally get it triaged.So happy reading

First, after fuzzing, I found a subdomain named **create.target.com**, but this subdomain responded with no content.

So I went to the Wayback Machine and found some URLs, and I noticed a **create account** URL:

[https://create.target.com/flow/target/create26/register-interest/createaccount](https://create.target.com/flow/target/create26/register-interest/createaccount)

After registering, it redirected me to the home page and it didn’t ask for verification. I tried many things here, but none of them worked.

So I stuck with the subdomain for a few days, testing the functions and trying to understand what it does. I found that this subdomain is for company events and has two user options:

1- **Interest**: Can see the event online for free

2- **In-person**: Can go to the event offline for **$400**


I also tried to make a **privilege escalation** from Interest to In-person for free, but I came up with nothing.

I was almost giveing up on this subdomain, but I looked at the URL and said, **“What if I changed create26 to create25?”**

It opened a **2025 event registration portal** (which is an ended event). So I tried to register with the same account that I had registered with in the **2026 event**, and it registered normally.

To explain it more, imagine that we have two sessions:

1- **victim@gmail.com** → registered with:

https://create.target.com/flow/target/create**"26"**/register-interest/createaccount

And the attacker, in another session, uses **victim@gmail.com** to register in:

https://create.target.com/flow/target/create**"25"**/register-interest/createaccount


Now, from the **attacker session**, I tried to navigate to **create26** (which is a valid and working event), hoping that it would open the victim’s account. But I found that every time I tried to navigate to **26** from **25**, it logged me out.

I kept digging and found that when I register the email, it takes an **invalid session**.

Because of that, it logs me out, but once I log in with **OTP**, it verifies the account and gives me access to navigate to **26** from the **25 account**.

But here is the problem: as an attacker, I can’t log in using OTP because I don’t have access to the victim’s email account. So I tried to change the account email to one I control to be able to log in with OTP and verify the account, then navigate to the **2026 victim account**.

To understand it more, the attacker will do the Next:

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

1- Create an account with the **victim’s email address** in the **create25 portal** (for example: victim@gmail.com)

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —-

2- Change the victim account email to **attacker@gmail.com** to be able to verify the account using OTP login

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

3- Navigate to **Create26**, and **boom**, the victim account is there.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -


So the subdomain logic does the following:

The backend links attendee identities across events for the **same email**, but at the same time allows registering with the **same email in the 2025 event** without saying **“Email already exists”** or asking for authorization.

It also does **not enforce ownership verification** when the email address is modified in the **CREATE25 profile**,

Allowing an attacker to **rebind the identity to a different email address**, which allows them to navigate to the **2026 event** and see the connected email there (**the victim’s email**).

But unfortanly it was a third-party vendor platform which is VDP and give no bounty !

in the end i can’t stop saying:

**Thank god | الْحَمْدُ لِلَّهِ**
