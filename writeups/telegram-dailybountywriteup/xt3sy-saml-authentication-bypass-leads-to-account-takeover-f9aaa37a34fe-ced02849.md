# SAML authentication bypass leads to account takeover

- **Source URL:** https://medium.com/@Xt3sY/saml-authentication-bypass-leads-to-account-takeover-f9aaa37a34fe?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@Xt3sY
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 4500)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Greetings, hackers!** I am [Pushkar](https://www.linkedin.com/in/pushkar-bhagat-03349a194/) a Security researcher from India, and I am excited to share my recent discovery of an account takeover vulnerability that allowed me to access a victim’s account without any credentials or interaction from the victim. In this write-up, I will explain the details of the vulnerability, and the steps I took to reproduce it.

During the sign-up process, I noticed that they were using [Single sign-on SAML](https://learn.microsoft.com/en-us/entra/identity-platform/single-sign-on-saml-protocol), which prompted me to investigate further.

Step 1 : Create account and Login

Here 324435 is my username.

Step 2 : Intercept the request in burpsuite.

Here we can see we have SAML Response, too read it add Burp-extention “SAML Raider Cert” and click on SAML Raider.

Step 3: It is an XML based markup language used to facilitate identity checks on larger-scale applications. So now we should able to read it.

Remember our username 324435 ?

Created one more user with 345530 and replace it with that intercepted request

Step 4: SAML usually uses a signature (and sometimes encryption) to ensure data integrity. Signature-based security is not always well implemented.

**Signature is only verified when it exists**

After struggling so much i got to know you could try removing the signature value from the SAML response. Sometimes, this is the only action required to bypass security checks. There are two ways that you can do this: empty out the signature field or remove the field entirely.

So i removed that base-64 signature.

Step 5: Forward the request anddd…

**YOU KNOW, I AM SOMETHING OF A LEGITIMATE USER MYSELF**
