# How IDOR could jeopardize digital business

- **Source URL:** https://medium.com/@mmaulanaabdullah/how-idor-could-jeopardize-digital-business-2e0fc8f056aa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251128100736/https://medium.com/@mmaulanaabdullah/how-idor-could-jeopardize-digital-business-2e0fc8f056aa
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3654 (id 3654)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How IDOR could jeopardize digital business

E-commerce business grows significantly in the past few years, there must be some well-known companies in a nation which have a huge amount of transactions across regions, customers and sellers (usually with >100M downloaders). Somehow, same business rises at narrower district which targets the lower class within the area, it can be seen from google play store, it’s developing rapidly as well.

Unfortunately maturity level of API development gap is far from those two players since a lot of factors come in, mainly maybe about investment cost to ensure the development is really appropriate. Of course this could not be a justification to let users’ data is at risk. No matter what, their data has to be as safe as possible. That is the background while writing this article, just to encourage starting up a business digital must concern about customer data safety.

Okay let’s finish the chit chat. IDOR (Insecure Direct Object References) is one of top finding vulnerabilities found. System is not capable enough to identify who can retrieve what resource through API. Let’s dig dive into the actual case at redacted.net on how just because an IDOR issue could lead to impersonate admin user who is possible to do all things such as managing products, price, orders, so on and so forth.

## Reproduce the Issue

1. **Iterating user\_id to find out admin user information**

Pretty straightforward indication IDOR might happen is once login API response does not contain any token, or session as user identifier. Even it has, there is still chance user identifier could be modified or it is not being used by the backend as input for access matrix for futher validation.

To make it clearer, modify the user\_id to be another number e.g 4000. In case it’s firmed, all users’ profile can be collected very easily which contain sensitive information such as name, email, phone number, gender, address, date of birth just by a iterating user\_id in range 1 to 10K number. If according to you, this is not dangerous, it is totally wrong as this is a beginning that might potentially cause account take over. More problematic one if there is a way to find out admin user profile and impersonate admin account.

Boom, with user\_id 1 it can be seen that admin email is well collected.

**2. Performing admin password reset**

Please find out one of the following written articles on how system is mistakenly implement wrong OTP during password reset.

In summary, with the following API reset (forgot password feature) at redacted.net, it’s allowed to modify any users’ email and new password without any further validation from account owner.

**3. Finding the admin login page**

It’s quite easy to identify what kind of framework this system is using by reading http header which is wordpress and it’s well known login panel would be [https://redacted.net/wp-login.php](https://redacted.net/wp-login.php)

Give it a try to login with admin user email found out at step 1 and new password at step 2. Boom !!! it’s successful to impersonate admin user account.

## How to improve to avoid such case occurs

1. To introduce non-modifiable user identifier token (recommended to use JWT token which has strong secret information)
2. To have API resource matrix by validating whether user identifier token is eligible to collect requested information or not
3. To have proper OTP implementation in login, update password and reset password process. Furthermore, on important occasional activities such as purchase

Hope it helps. Please kindly comment if you have any more inputs/feedback in terms of usual finding related with IDOR and how to fix it. Thank you
