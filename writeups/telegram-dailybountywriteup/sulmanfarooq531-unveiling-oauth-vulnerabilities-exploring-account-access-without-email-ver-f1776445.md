# Unveiling OAuth Vulnerabilities

- **Source URL:** https://medium.com/@sulmanfarooq531/unveiling-oauth-vulnerabilities-exploring-account-access-without-email-verification-d36762361df7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240717125746/https://medium.com/@sulmanfarooq531/unveiling-oauth-vulnerabilities-exploring-account-access-without-email-verification-d36762361df7
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6516 (id 6516)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Unveiling OAuth Vulnerabilities: Exploring Account Access Without Email Verification

# Introduction

In the realm of online security, OAuth vulnerabilities pose significant risks, especially when it comes to the account verification process. Today, we’ll explore two scenarios demonstrating how improper handling of email verification in OAuth implementations can lead to potential security flaws. These scenarios highlight how users can gain access to accounts without verifying their email, creating opportunities for unauthorized access. Let’s delve into the details and understand the implications of these vulnerabilities.

# What is OAuth?

OAuth, or Open Authorization, is an open standard for access delegation commonly used as a way to grant websites or applications limited access to a user’s information without exposing their credentials. It is widely employed by internet giants such as Google, Facebook, and Twitter to permit users to share information about their accounts with third-party apps or websites.

OAuth operates by allowing an application to obtain access tokens which are used to authorize access to resources on behalf of the user. This process enhances security by not exposing user credentials to third-party services, instead relying on a secure token that grants the necessary permissions.

# The Impact of OAuth Vulnerabilities

While OAuth streamlines the process of access delegation and increases security, improper implementation can lead to serious vulnerabilities. These vulnerabilities can range from allowing unauthorized access to user accounts to escalating privileges within an application. The consequences of such vulnerabilities can include:

- Unauthorized access to sensitive user data.
- Compromise of user accounts and credentials.
- Potential misuse of user privileges within applications.
- Exposure to phishing or social engineering attacks.

Given the widespread use of OAuth in modern web applications, ensuring its secure implementation is crucial. Let’s examine two scenarios that expose vulnerabilities in the email verification process of OAuth.

# How I Discovered These Scenarios

During a routine security assessment of an OAuth-based authentication system, I encountered some peculiar behaviors related to email verification. The exploration began with a curiosity about what happens if the email verification process is bypassed or handled incorrectly. Here’s a step-by-step recount of how I found these issues:

- **Created an Account**: I signed up using my Gmail address and chose to verify the email later.
- **Logged In Without Verification**: I filled out the details and was able to log in without verifying the email.
- **Tested Gmail Authentication**: Logged out and logged back in using Gmail’s OAuth authentication, which granted access without needing to verify the email.
- **Logged In Directly**: Logged out again and successfully logged in using the Gmail ID and password I created, even though the email wasn’t verified.
- **Verified Email and Retested**: I then verified the email, logged out, and logged back in with the same ID and password. Post-verification, access was still allowed without additional security checks.

# Scenario 1: Logging In Without Email Verification

**Step 1: Create an Account Using a Gmail Address:** When you sign up for an account, you usually provide your Gmail address and set a password. The typical expectation is that you’ll need to verify your email before fully accessing the account.


**Step 2: Choose to Verify Email Later:** During the sign-up process, you are given two options: verify your email now or verify later. For this scenario, choose to verify later.


**Step 3: Fill Out the Required Details:** Enter your account name, first and last name, and password. Click to create the account.


**Step 4: Log In Without Email Verification:** Surprisingly, you can log in to the account even though you haven’t verified your email. This indicates that the system allows access without completing the verification process.


**Step 5: Log Out and Use Gmail Authentication to Log Back In:** Log out from the account. Then, log back in using Gmail authentication. You will notice that this method also grants you access.


**Step 6: Log Out from Gmail Authentication and Log In Directly:** Log out again and try logging in using the Gmail ID and the password you initially created. You’ll find that you can successfully access the account without having verified your email.


# **Implications of Scenario 1**

This scenario reveals a vulnerability where the account system allows access without email verification. While this might seem convenient, it opens the door to unauthorized access and potential misuse of accounts. However, the impact might be considered low since unverified accounts typically have limited functionality.

# Scenario 2: Logging In After Email Verification

**Step 1: Verify the Email:** Go back to your registered Gmail account and complete the email verification process.


**Step 2: Confirm Account Verification:** Upon verifying the email, the account is fully activated.


**Step 3: Log Out and Use the Created ID and Password:** Log out from the account. Then, log back in using the created email ID and password.


**Step 4: Successful Login After Verification:** You can successfully log in to the account with the created email ID and password after verification.


# **Implications of Scenario 2**

In this scenario, even after the email is verified, the account remains accessible with the initially created password. This might seem normal, but if the system doesn’t enforce additional security measures after verification, it becomes a high-risk vulnerability. Attackers could exploit this to gain unauthorized access to verified accounts.

# Conclusion

These two scenarios highlight significant OAuth vulnerabilities related to the email verification process. In Scenario 1, the ability to log in without verifying the email can lead to unauthorized access, albeit with limited impact. In Scenario 2, the post-verification access without enhanced security checks presents a higher risk, as verified accounts are more valuable targets for attackers.

To mitigate these risks, developers should ensure that systems enforce strict email verification before granting access and implement additional security measures for verified accounts. Addressing these vulnerabilities is crucial in maintaining the integrity and security of user accounts.

# Key Takeaways

1. **Always Enforce Email Verification**: Systems should not allow access to unverified accounts.
2. **Enhance Security Post-Verification**: Implement robust security measures for verified accounts to prevent unauthorized access.
3. **Regular Security Audits**: Conduct frequent security assessments to identify and patch potential vulnerabilities in OAuth implementations.

By understanding and addressing these vulnerabilities, we can build more secure systems and protect user data effectively.

# About the Author

[**Sulman Farooq S**](https://www.linkedin.com/in/sulman-farooq-s-369013181/) is a passionate cybersecurity enthusiast with over two years of experience in penetration testing. He specializes in network, web application, mobile application, and API penetration testing. Follow me on Medium for more insights into cybersecurity and vulnerability assessments.

Stay vigilant and keep your applications secure! Happy (ethical) hacking! 😊😊😊
