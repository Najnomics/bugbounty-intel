# How One Free Trial Became Unlimited Number Of Licenses | $$$$ Bounty

- **Source URL:** https://medium.com/@marwanmedhat0001/how-one-free-trial-became-unlimited-number-of-licenses-bounty-c98b8a4ee7e7
- **Fetched:** 2026-11-26
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14999)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Marwanmedhat / Tue, 24 Nov 2026 22:00:51 GMT

Hi, I’m ***Marwan Medhat (M4R0O0)***, a Security Researcher, Bug Hunter, and Ethical Hacker.

In this writeup, I want to share a business logic vulnerability I found while testing a private bug bounty program. The report was accepted, rewarded, and marked as resolved.

The target’s identity and sensitive information have been redacted .

The application offered a free 30-day trial with a clear restriction: **one trial license per company**.

What caught my attention was that getting a license and registering it were two separate operations. The initial operation checked whether a company had already used its trial. I wanted to know whether the same rule was enforced when a license was actually registered.

I started with a test company that had already received its free trial. **The normal trial-generation workflow enforced the restriction, *as expected.***

At this point, there was nothing unusual. The interesting question was whether that restriction applied to the *entire license lifecycle or only to the first operation.*

I examined how the application handled license registration using separate controlled company accounts. My focus was on the server-side relationship between a license, its issuing company, and the company registering it.

The result exposed a mismatch: **the registration workflow accepted an additional trial for a company that had already used its entitlement.** It also allowed a trial issued under a different controlled company to be associated with the receiving company.

The registration request used multipart form data. The two license-related fields identified the license being registered; the request also contained the authenticated session and form-verification data.

Below is redacted version of the request submitted with my report.

POST /\[REDACTED-REGISTRATION-PATH\] HTTP/2

Host: \[REDACTED\]

Cookie: \[REDACTED\]

User-Agent: \[REDACTED\]

Referer: \[REDACTED\]

Origin: \[REDACTED\]

Content-Type: multipart/form-data; boundary=REDACTED\_BOUNDARY

--REDACTED\_BOUNDARY

Content-Disposition: form-data; name="\[LICENSE\_NUMBER\_FIELD\]"

\[REDACTED\]

--REDACTED\_BOUNDARY

Content-Disposition: form-data; name="\[LICENSE\_IDENTIFIER\_FIELD\]"

\[REDACTED\]

--REDACTED\_BOUNDARY

\[Remaining form fields and verification tokens redacted\]

--REDACTED\_BOUNDARY--

What mattered was not a redirect or a successful HTTP status on its own, but the server-side change that followed: an additional license appeared in the receiving company’s records.

A successful response alone wasn’t enough for me. I wanted to see whether the license had actually been associated with the receiving company.

I checked the company’s license list to verify whether the additional trial licenses had been successfully registered.

The results confirmed my findings. I was able to register **11 trial licenses under a single company account**, despite the application’s stated limit of one free trial per company.

This demonstrated that the restriction was not consistently enforced throughout the licensing process.

After successfully reproducing the vulnerability manually, I wanted to determine whether the behavior was repeatable.

I developed a Python script to automate the testing workflow and verify the resulting license state.

Rather than relying solely on HTTP response codes, the script checked whether the additional licenses actually appeared in the company’s license list.

The results confirmed that the issue was not an isolated occurrence.

**The one-trial-per-company restriction was not consistently enforced throughout the licensing workflow.**

[***Automated POC Here***](https://gist.github.com/maro0o1/ef4c246ea8d0f71fc4d15ab7d1410fd4)

The complete automation script was provided to the security team as part of the original report to assist with reproduction and validation.

The issue was a **business logic flaw** in the way the application enforced its commercial policy. The initial trial workflow checked eligibility, but the final registration operation did not consistently enforce that same restriction or the expected relationship between the license and company.

The demonstrated impact was the registration of un limited number of =licenses under a single controlled company. Potential consequences included abuse of the trial model and lost sales opportunities. I did not establish actual revenue loss, unlimited active usage, or the ability to predict valid license identifiers.

The appropriate fix is to verify ownership and trial eligibility on the server at the final registration step, and enforce the rule consistently throughout the license lifecycle.

*Recommended controls for the license registration workflow.*

The security team initially requested additional reproduction details. After I supplied further evidence, the team reproduced the issue, accepted the report, awarded a bounty, and marked it as resolved.

**Bounty: $$$$ (amount undisclosed)**

The finding was classified as Low severity. The exact program details, report identifiers and sensitive request data are intentionally withheld.

The initial trial limit worked. That was what made this case interesting to me: a valid check in one part of an application can still fail to protect the overall business rule.

**A business rule should be enforced where the final state changes, not only where the workflow begins.**

Thanks for reading.

I’m **Marwan Medhat (M4R0O0)**, a Security Researcher, Bug Hunter, and Ethical Hacker. I share practical web security research and bug bounty writeups.

**X:** [M4R0O0](https://x.com/m4r0o0_m?s=11)

**LinkedIn:** [Marwan Medhat](https://www.linkedin.com/in/marwan-medhat-53b8822a6/)
