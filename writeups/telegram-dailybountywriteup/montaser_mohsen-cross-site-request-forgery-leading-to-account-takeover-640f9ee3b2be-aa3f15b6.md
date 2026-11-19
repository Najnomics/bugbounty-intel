# Cross-Site Request Forgery Leading to Account Takeover

- **Source URL:** https://medium.com/@montaser_mohsen/cross-site-request-forgery-leading-to-account-takeover-640f9ee3b2be?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260301115728/https://medium.com/@montaser_mohsen/cross-site-request-forgery-leading-to-account-takeover-640f9ee3b2be
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12850 (id 12850)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Cross-Site Request Forgery Leading to Account Takeover

My name is Montaser Mohsen.I am a security researcher focused on web application vulnerabilities and account takeover scenarios.I pay close attention to business logic flaws that appear simple but create high impact.This write-up explains a Cross-Site Request Forgery vulnerability that led to full Account Takeover.For privacy and security reasons, the affected organization will be referred to as **Example.com**.

## Vulnerability Overview

The application allowed authenticated users to change their email address.

This functionality lacked proper CSRF protection.

An attacker could force a logged-in victim to submit a forged request that changed the account email address to one controlled by the attacker.

No password was required.

No 2FA was required.

No confirmation was sent to the original email.

Once the email was changed, the attacker could trigger a password reset and gain full control of the account.

This resulted in complete Account Takeover.

## Root Cause

The email change endpoint:

- Did not validate a proper CSRF token
- Did not verify Origin or Referer headers
- Did not require re-authentication
- Did not send a confirmation link to the original email address

The application trusted the authenticated session cookie without verifying the legitimacy of the request source.

## Proof of Concept

A malicious HTML file hosted by the attacker:

```
<html>
<body>
<form method="POST" action="https://example.com/security/changeEmail">
<input type="hidden" name="email" value="attacker@example.com"/>
<input type="hidden" name="confirmEmail" value="attacker@example.com"/>
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>
```
Attack scenario:

- Victim logs into Example Government
- Victim visits attacker-controlled webpage
- The form auto-submits silently
- Email address changes instantly
- No warning is displayed
- The victim remains unaware.

## Steps to Reproduce

1. Log in as a normal user.
2. While authenticated, visit an attacker-controlled webpage containing the malicious form.
3. The request is automatically submitted.
4. The email address is changed to attacker@example.com.
5. The attacker initiates a password reset.
6. The reset link is sent to the attacker’s email.
7. The attacker sets a new password.
8. The account is fully compromised.

## Impact

This vulnerability allowed:

- Full Account Takeover
- Unauthorized email modification
- Unauthorized password reset
- Loss of confidentiality
- Loss of data integrity

If the account contained regulated or sensitive data, the risk would increase significantly.

I expected the issue to be classified at least as P2 because it led directly to Account Takeover.

However, the bugcrowd classified p4.

The likely reasoning involved required user interaction.

From a practical exploitation perspective, any vulnerability that enables silent email change followed by password reset should be treated as a direct ATO vector.

## Remediation

The issue was fixed after responsible disclosure.

The remediation included:

- Proper server-side CSRF token validation
- Re-authentication requirement before email changes
- Additional verification controls
- Stronger request validation mechanisms

These changes effectively eliminated the exploitation path.

## Security Recommendations

For developers and security teams:

- Implement per-session CSRF tokens
- Validate tokens server-side
- Verify Origin and Referer headers
- Require password or 2FA re-authentication for email changes
- Send confirmation emails to both old and new addresses
- Use SameSite=Strict cookies
- Log and alert users on email changes

🔗 Connect With Me

If you found this article helpful or have questions about vulnerabilities and bug bounty hunting, feel free to connect with me:

Facebook: [https://facebook.com/montasermohsen98](https://facebook.com/montasermohsen98)

Twitter (X): [https://x.com/Montaser\_M98](https://x.com/Montaser_M98)

LinkedIn: [https://linkedin.com/in/montasermohsen98](https://linkedin.com/in/montasermohsen98)
