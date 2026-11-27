# Instagram and Meta 2FA Bypass by Unprotected Backup Code Retrieval in Accounts Center

- **Source URL:** https://medium.com/@scriptshuva/instagram-and-meta-2fa-bypass-by-unprotected-backup-code-retrieval-in-accounts-center-c735ff650f10?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241001234708/https://medium.com/@scriptshuva/instagram-and-meta-2fa-bypass-by-unprotected-backup-code-retrieval-in-accounts-center-c735ff650f10
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7045 (id 7045)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Instagram and Meta 2FA Bypass by Unprotected Backup Code Retrieval in Accounts Center

Hello, I'm Shuva Saha (scriptshuva). Today, I will be discussing a vulnerability I discovered: bypass of two-factor authentication (2FA) mechanisms in Meta and Instagram.

**Bounty**: $10,000 Awarded for bypassing two-factor authentication (2FA) mechanisms in Meta and Instagram

## Meta 2FA Bypass

A hacker who gains access to a victim Facebook or Instagram account can retrieve Meta 2FA backup codes from the account center, bypassing Meta two-factor authentication (2FA) and gaining full access to the victim Meta account.

## Step 1: Login Initiation

1. Go to [Meta Auth](https://auth.meta.com/).
2. Log in using the compromised Facebook or Instagram accounts.

## Step 2: 2FA Handling

1. If 2FA is enabled on the Meta account, select the recovery code option when prompted for 2FA.

## Step 3: Exploitation Process

1. Open a new tab in the browser and go to [Facebook Accounts Center Two-factor authentication Settings](https://accountscenter.facebook.com/password_and_security/two_factor).

2\. Click Additional methods and then Click Recovery codes

3\. Use a proxy tool, such as Burp Suite, to intercept **FXAccountsCenterTwoFactorRecoveryCodesDialogQuery** graphql request.

## Step 4: Request Modification

1. Modify the intercepted request by changing the variables and doc\_id as shown below:

`variables={"account_id":"victim_meta_account_id","account_type":"FRL","interface":"FB_WEB"}&doc_id=6358505927544740`
**Note**: The flaw here is the missing meta account password protection.

## Step 5: Recovery Code Retrieval

1. Send the modified request.
2. Extract the recovery code from the response.

## Step 6: Account Takeover

1. Use the retrieved 2FA backup code to log in to the victim meta account, effectively bypassing the 2FA.

## Instagram 2FA Protection Bypass

A hacker who gains access to a victim Facebook account can retrieve Instagram 2FA backup codes from the account center, bypassing Instagram two-factor authentication (2FA) and gaining full access to the victim Instagram account.

## Step 1: Login Initiation

1. Go to [Instagram](https://instagram.com/).
2. Log in using the compromised Facebook account.

## Step 2: 2FA Handling

1. If 2FA is enabled on the Instagram account, select the recovery code option when prompted for 2FA.

## Step 3: Exploitation Process

1. Open a new tab in the browser and go to [Facebook Accounts Center Two-factor authentication Settings](https://accountscenter.facebook.com/password_and_security/two_factor).

2\. Click Additional methods and then Click Recovery codes

3\. Use a proxy tool, such as Burp Suite, to intercept **FXAccountsCenterTwoFactorRecoveryCodesDialogQuery** graphql request.

## Step 4: Request Modification

1. Modify the intercepted request by changing the variables and doc\_id as shown below:

`variables={"account_id":"victim_instagram_account_id","account_type":"INSTAGRAM","interface":"FB_WEB"}&doc_id=6358505927544740`
**Note**: The flaw here is the missing Instagram account password protection.

## Step 5: Recovery Code Retrieval

1. Send the modified request.
2. Extract the recovery code from the response.

## Step 6: Account Takeover

1. Use the retrieved 2FA backup code to log in to the victim Instagram account, effectively bypassing the 2FA.

## Outcome

By following these steps, the attacker successfully logs into the victim Instagram and Meta accounts by bypassing the two-factor authentication, exploiting the missing password protection for accessing backup codes.

## Technical Details

The vulnerability exists because Instagram and Meta backup code retrieval process in the Facebook Accounts Center does not require the Instagram and Meta account password. This lack of password protection allows anyone with access to the victim Facebook account to obtain Instagram and Meta backup codes and bypass 2FA.

## Remediation

Now, accessing Instagram and meta backup codes for requires verifying login to the Instagram and meta accounts, ensuring that backup codes are protected by an additional layer of security.

**Timeline:**

Report Created : Monday, June 26, 2023

Bounty Awarded : July 8, 2023 ( $5000 for Meta 2FA bypass )

Bounty Awarded : July 27, 2023 ( $5000 for Instagram 2FA bypass )

Publicly Disclose Approved: August 21, 2024
