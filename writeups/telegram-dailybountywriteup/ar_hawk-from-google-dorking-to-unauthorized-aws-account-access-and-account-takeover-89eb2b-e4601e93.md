# From Google Dorking to Unauthorized AWS Account Access and Account Takeover

- **Source URL:** https://medium.com/@ar_hawk/from-google-dorking-to-unauthorized-aws-account-access-and-account-takeover-89eb2b9d284f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240104200902/https://medium.com/@ar_hawk/from-google-dorking-to-unauthorized-aws-account-access-and-account-takeover-89eb2b9d284f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4858 (id 4858)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Google Dorking to Unauthorized AWS Account Access and Account Takeover

--

*Ending 2023 with good note, I came up with another misconfiguration due to a parameter that leads to exposure of AWS credentials and access to their S3 buckets and cloud infrastructure. Let’s not talk more, understand the approach to recon and exploit the potential threat.*

# TL;DR

Another week another target, As I already mentioned in my [previous blogs](/@ar_hawk/how-a-misconfigured-lotus-domino-server-can-lead-to-disclosure-of-pii-data-of-employees-badad691dad) I use automation for my reconnaissance of which snippet I have released in earlier blogs. While my automation doing its job, I perform some manual recon via ***Google Dorking, Shodan, GitHub, etc***. This time I was focused more on Google Dorking for finding out ***more subdomains, urls and endpoints***.

I found an endpoint which is generating the pdf, it clicked me about **SSRF \[Server Side Request Forgery\]** and after some checks and validation I found its vulnerable to SSRF and I know that the host is deployed on AWS and I was able to find out the ***secret id and secret key of AWS*** which led to Unauthorized access to their AWS Infrastructure.

# Recon Automation Script Snippet

# \[1\] Let’s start with Reconnaissance — Understanding the target

- As said automation is working in background, I was doing some google dorking to gather some subdomains. Let’s call our target as `redacted.com`.
- The following google dork I was using to gather subdomains: **site:*.redacted.com**
**Level 1 subdomains**, but you want to gather **X Level of subdomains** (*I mean if you want to gather subdomains like* [*www.admin.redacted.com,*](http://www.admin.redacted.com,) [*www.stag.admin.redacted.com,*](http://www.stag.admin.redacted.com,) *etc.*) use the dork **site:*.*.*.redacted.com**
*****
- I found a subdomain `int.redacted.com` which has the following endpoint and parameter **/pdf.axd?url=redacted.com**

# \[2\] Subdomain Analysis — Hacking the Endpoint

- Its time to analyze the endpoint and parameter. When I visited that subdomain, I found a ***pdf generation error*** which states that the developer is using the endpoint to generate the PDF and the current generated pdf is just the errors came across while development. *So Its like developer has created the pdf of the errors to test the PDF Generation Feature.*

- Now I started analyzing the `url=` endpoint, I inputted a domain [https://evil.com](https://evil.com)
**BoomMMMMM 💥**, Its time to exploit it.
- At this point the web application is not validating the user input. This means application is vulnerable to **Improper User Input Validation**.
- What I did, I simply added my interactsh URL, which is basically a free alternative to Burp Collaborator.

- In the response, I found the request is generating from an IP address which belongs to **Amazon AWS**. While tech stack discovery of the organization, I already found that most of the applications are hosted AWS Cloud Infrastructure.

- Now, the impact of the improper user input validation increases as we have a successful Blind SSRF. Though its not critical but let’s exploit it to gather the AWS credentials which make this a critical severity threat for the organization.

# \[3\] Exploiting Blind SSRF — Gathering AWS Credentials

- Whenever I came across such misconfiguration, I use the following payload to gather AWS meta-data: [url=169.254.169.254/latest/meta-data](http://169.254.169.254/latest/meta-data.)

- **BooOMM 💥**, the payload gets accepted, its time to gather the IAM credentials. Note that currently AWS has deployed a authentication mechanism that require ***AWS token with aws ID and aws secret key.*** This token is valid for very less time.
- Now I have used the payload to get the Identity credentials: `url=169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance` and here we go, we got the credentials.

- Now, I have imported these credentials and tokens in my terminal and access their S3 buckets associated with this account. The following commands were used to export the credentials. After that use the command `aws s3 ls` which will list all the S3 buckets.

```
export AWS_ACCESS_KEY_ID="REDACTED"
export AWS_SECRET_ACCESS_KEY="REDACTED"
export AWS_SESSION_TOKEN="REDACTED"
```
# Conclusion

- Let’s understand the impact and remediations. The above sections already explained the criticality of the threat but its important to mention the impact and remediation to improve the quality of your reports.

# It’s time to Say Good Bye 🙋♂

**Happy New Year Everyone😃**

*Thanks for reading, hope you enjoyed and learned something from this blog.*

*If you have any questions, DM at* [https://twitter.com/0xfa1c0n](https://twitter.com/0xfa1c0n).
