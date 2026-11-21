# How I Chained Recon and IDOR to Access 100's of Credit Cards

- **Source URL:** https://medium.com/@XCriminal/how-i-chained-recon-and-idor-to-access-100s-of-credit-cards-0ca50eb82a74?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260520133601/https://medium.com/@XCriminal/how-i-chained-recon-and-idor-to-access-100s-of-credit-cards-0ca50eb82a74
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9935 (id 9935)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Featured

# How I Chained Recon and IDOR to Access 100's of Credit Cards

*I recently found a bug in a bug bounty program where a small mistake in access control allowed me to access sensitive user data through an Insecure Direct Object Reference (IDOR) vulnerability.*

### Background

While casually reviewing a private program, I noticed that the target had recently rolled out ***some new features around user account management***.

The application allowed users to register accounts, manage their profiles, and store payment information. Despite the limited attack surface, I decided to invest some time in manually inspecting how the application handled identifiers and access control. I added some fake credit card info to the victim account to test the vulnerability.

### **Discovery**

During pentest, I observed that the application was setting a cookie named `cam=`, which seemed to contain a ID. A closer look revealed that this value was being used as the `external_customer_id` in backend API requests.

To validate whether the application enforced proper access controls, I created two accounts:

- **victim** (who was just chilling, minding their business)
- **attacker** (me)

I added fake credit card details to the victim’s account, I intercepted a request made by the attacker account to the following endpoint:

Replacing the attacker’s `external_customer_id` with the victim’s `id` allowed me to retrieve credit card information from the victim’s account. The server responded with the following details:

- Exposed whole card number via card token
- Expiry date
- Default card status

The endpoint confirmed that the application was vulnerable to an IDOR, allowing unauthorized access to sensitive user data.

IDOR occurs when an application exposes a reference to an internal implementation object, such as a file, database record, or user ID, and fails to verify whether the user is authorized to access it.


### What Went Wrong

There were no authorization checks in place to verify that the object or data could be accessed by the authorized user.

In my case, to **escalate the impact** of the vulnerability, I aimed to retrieve UUIDs belonging to other users.

Always test for UUID or ID’s leakage in password reset flows, referral links, and email tracking URLs. These often bypass access control checks but contain identifiers that can later be reused in direct object access attempts.


### Increasing the Impact via Recon

To elevate the severity of the IDOR vulnerability, I gathered archived URLs of the application and found that **"forgot password" and some endpoints were publicly indexed**. These URLs often contained JWT tokens or query parameters that included IDs such as `external_customer_id`.

I used two primary tools for this purpose:

- [waybackurls](https://github.com/tomnomnom/waybackurls)
- [gau](https://github.com/lc/gau)

Attaching the script that I used to collect all URL’s from the target domain.

```
#!/bin/bash
# Check if domain is provided
if [ -z "$1" ]; then
  echo "Usage: $0 domain.com"
  exit 1
fi
DOMAIN=$1
OUTPUT_DIR="target"
OUTPUT_FILE="$OUTPUT_DIR/$DOMAIN-urls.txt"
# Create the target directory if it doesn't exist
mkdir -p $OUTPUT_DIR
# Run waybackurls and gau, combine and dedupe
echo "[*] Gathering URLs for $DOMAIN..."
(waybackurls $DOMAIN; gau --blacklist png,jpg,gif $DOMAIN) | sort -u > $OUTPUT_FILE
echo "[+] URLs saved to $OUTPUT_FILE"
```
R*econ is boring. Until it’s not.*


Most of us skip it because it feels like playing hide-and-seek with someone who doesn’t want to play. But trust me, recon is the stage where apps accidentally leak secrets like they’re trying to get hacked.

Few endpoints like `reset-password` which has the JWT token

After collecting archived reset-password URLs containing JWT-like tokens, I used Burp Suite Decoder to analyze them. Upon decoding, I identified parameters such as `externalCustomerId` and other unique identifiers that mapped directly to user accounts.

Although the JWT tokens extracted from the archived URLs were expired and could not be used for authentication, they could still be decoded to reveal their payload.


These extracted IDs were later used to exploit the IDOR vulnerability and retrieve credit card information.

Now I tried fetching card data with the stolen ID’s, guess what??

This confirmed that the (IDOR) was not isolated — it **affected a large set of users**, significantly increasing the severity of the vulnerability.

Realizing the critical impact, I immediately reported the findings to the program.

*The security team acted quickly, triaged the vulnerability, and patched it within hours of my report.*


### Attack Path:\

### **Why severity was changed?**

Its severity was the fact that it exposed live credit card data belonging to real customers still stored in the system. The credit card numbers, expiry dates, and default card statuses were actual, sensitive financial details that could be exploited for fraud or identity theft.

### How they fixed it?

I’ve confirmed that the issue has been fixed, the development team quickly addressed the vulnerability by implementing strict authorization checks on the backend APIs handling user-specific data. Specifically, they ensured that every request to access sensitive information, such as credit card details, verifies that the requesting user is indeed the owner of the data.

If you come across any other techniques, please let me know in the comments. Until next time!

Happy Hacking!!
