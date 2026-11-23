# 0-click Account Takeover (ATO) via Google Authentication

- **Source URL:** https://medium.com/@elcapitano7x/0-click-account-takeover-ato-via-google-authentication-b63a01a80a03?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261024065651/https://medium.com/@elcapitano7x/0-click-account-takeover-ato-via-google-authentication-b63a01a80a03
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6542 (id 6542)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 0-click Account Takeover (ATO) via Google Authentication

## **Description:**

A critical vulnerability has been identified in the Google Authentication mechanism of the application. By manipulating the ID and email parameters in the authentication request, an attacker can obtain an access token for any user. This allows the attacker to take over any account without any user interaction, leading to a complete compromise of the victim’s account.


### **what is the Single Sign-On (SSO):**

Implementing Single Sign-On (SSO) with Google Cloud is a strategic move for organizations looking to enhance their security posture while simplifying the user authentication process. SSO centralizes authentication through a trusted Identity Provider (IdP), reducing the risks associated with password fatigue and credential theft. This approach also streamlines administrative tasks, providing IT teams with a more efficient way to manage user access and enforce security policies, including multi-factor authentication (MFA).

By following a structured implementation process — selecting a compatible IdP, configuring the necessary settings, and thoroughly testing the setup — organizations can ensure a smooth transition to SSO. The benefits of SSO are manifold: improved security, enhanced user experience, simplified administration, and better compliance with regulatory standards.

[click here](https://cloud.google.com/architecture/identity/single-sign-on) to read more about the SSO with google


## Proof of Concept (PoC):

1-Login with Google:

**2-Intercept the OAuth Request:**

## Get Elcapitano’s stories in your inbox

Join Medium for free to get updates from this writer.

3-**Modify the Request:**

- Change the `id` field to any ID.
- **NOTE** In changing the ID, you can try any number because it does not verify whether this number is correct or not, but it verifies whether the ID existed before or not, so you can enter anything, for example
- “id”:”1" or “id”:”123456”…. etc
- Change the `email` field to the victim's email address.

4- **now Gain Access to Victim’s Account:**

## **Conclusion**

This scenario highlights the severity of the vulnerability, demonstrating how an attacker can exploit the improper handling of OAuth tokens to perform a zero-click account takeover. The potential consequences include data breaches, loss of user trust, and significant reputational damage to Example.com. The recommended fixes must be implemented urgently to secure the application and protect user accounts from unauthorized access.

That’s all for today. I hope you all enjoyed it and learned something new

*Please don’t hesitate to reach out to me anytime on X Elcapitano*

I trust that this write-up proves helpful to you in any way.
