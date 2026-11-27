# DOS attack possible on Reset 2FA feature of #Hackerone

- **Source URL:** https://medium.com/@lokesh.leads13/disallow-any-hackerone-user-permanent-access-to-his-her-own-hackerone-account-using-vulnerability-147ce9957692?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230627015852/https://medium.com/@lokesh.leads13/disallow-any-hackerone-user-permanent-access-to-his-her-own-hackerone-account-using-vulnerability-147ce9957692
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3150 (id 3150)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **DOS attack possible on Reset** 2FA feature of #Hackerone

--

*Severity: Medium (5.0) Weakness: Insecure Design & No Rate Limiting in place*

**Summary:**

I have found a vulnerability in “reset 2FA” feature of hackerone using which any malcious user on hackerone can permanently deny access to H1 site to all the users. This will Disallow any #Hackerone user permanent access to his/her own Hackerone account using vulnerability in

Only requirement is Attacker need to have the Victim’s email.

**Description:** 

There is no rate limiting in place on “Reset Two factor authentiction” graphql endpoint and this bug can be leveraged by malicious hacker to deny access to the user’s hackerone account permanently.

# Steps To Reproduce

Proof Of Concept-

Victim — [victim1@gmail.com](mailto:coolranjan.saxena@gmail.com) 

Attacker- [hackerone\_user@gmail.com](mailto:lranjan0713@gmail.com)

1. Two Factor Authentication is enabled on both Victim and Attacker.
2. Attacker will login into hackerone site using his/her valid “email address” and “Password” on the sign in page — [https://hackerone.com/users/sign\_in](https://hackerone.com/users/sign_in).
3. Application redirects to the “Two-factor Authentication” page.
4. Click on “Reset Two-factor Authentication” and intercept the request using burp suite.
5. Attacker sends the intercepted request to “intruder” and replaces the Email with “Victim’s email” and sets a bruteforce payload on “password” field.
6. Run the brute force attack using intruder.
7. Brute force attack will lockout the Victim account and since there is no Rate Limiting in place Brute Force attack will successfully run(infinite times) locking out the Victim thus denying the co-hacker to access or unlock his/her hacekrone account.
8. Simultaneous brute force attack can be run on 10’s or 100’s of users. Since, no rate limiting/IP restriction/authorization check implemented on reset 2FA functionality it can be easily exploited.

Note: “account unlock instruction” will be on use since brute force can be run infinitely and Victim’s account will keep getting locked.

There is a violation of security design principle, as once user have passed the intial password based login flow, on two factor authentication they must not be able to use any other user email on “Reset Two-factor authenticatoin” graphql endpoint.

Hackerone team closed this vulnerability as **“informative”.  However a live demo was done with the H1 team as well and show cased that WAF didn’t blocked the bruteforce attack and account got locked permanently with no user access. Also, many H1 users email addressess are publicly available on H1 site, so not much effort required to scrape the emails.**

Simple mitigation would have been to either implement API rate limiting and Block the IP trying brute force or not allow any hacker to user their “Reset two factor authentication” flow to send the request for any other user’s email id. Request should result in “unauthorized” HTTP request.

After reporting this issue under responsible disclosure program and repeated follow up no action was taken. It have closed as “Informational”. But i think security community must be aware of this flaw.
