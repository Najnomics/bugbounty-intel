# Host Header Injection in Password Reset Function Leading to Account Takeover and Blind SSRF

- **Source URL:** https://medium.com/@mhmodgm54/host-header-injection-in-password-reset-function-leading-to-account-takeover-and-blind-ssrf-b63ed248b93a?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@mhmodgm54
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12266)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Introduction

In this write-up, I describe a **Host Header Injection vulnerability** in a password reset functionality that leads to a **1-click Account Takeover (ATO)** through **Password Reset Poisoning**.

Additionally, the same vulnerability resulted in **Blind Server-Side Request Forgery (SSRF)** due to server-side interactions with an attacker-controlled domain.

The part of reset password is similar to [portswigger](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-basic-password-reset-poisoning).

### Discovery Steps

### password reset poisoning

While testing the **password reset** functionality I first sent a normal reset request and intercepted it using **Burp Suite**.

I forwarded the request to **Repeater** and started modifying different parameters.

After several tests, I attempted **Host Header Injection** by modifying the Host header to an attacker-controlled domain.

The application accepted the injected Host header without validation.

As a result, the password reset email contained a reset link pointing to my malicious domain instead of the legitimate one.

i received this email

**now if the victim click on this account the attacker get it’s token and can reset victim password and takeover it’s account**

### Account Takeover (ATO)

When the victim clicks the poisoned password reset link:

- The reset token is sent to the attacker-controlled server
- The attacker captures the token
- The attacker uses the token to reset the victim’s password
- Full account takeover is achieved

This attack requires only **one click by the victim**, making it highly impact.

### Blind SSRF

To safely record interactions, I used [**Beeceptor**](https://app.beeceptor.com/) as an attacker-controlled domain (similar to Burp Collaborator) but free.

After completing the ATO proof of concept, I noticed **multiple HTTP requests** hitting my [**Beeceptor**](https://app.beeceptor.com/) endpoint.

Interestingly:

- More requests were received than expected
- Some requests occurred **even when the reset link was not clicked**

This behavior strongly suggests **Blind SSRF**, where the backend server makes HTTP requests to the injected host.

A possible explanation is that the back-end:

- Fetches resources email images.
- Performs internal checks on URLs included in outgoing emails

These requests occur server-side and are invisible to the user, which explains the **blind nature** of the SSRF.

### **End**

I hope this write-up helps others understand the real-world impact of Host Header Injection vulnerabilities.

*أن رجلا جاء إلى رسول الله صلى الله عليه وسلم فقال : ( يا رسول الله ! أيُّ الناس أحبُّ إلى الله ؟ فقال : أحبُّ الناس إلى الله أنفعهم للناس…)*
