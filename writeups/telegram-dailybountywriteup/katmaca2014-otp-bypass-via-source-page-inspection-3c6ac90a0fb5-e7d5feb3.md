# OTP Bypass via Source Page Inspection

- **Source URL:** https://medium.com/@katmaca2014/otp-bypass-via-source-page-inspection-3c6ac90a0fb5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127063756/https://medium.com/@katmaca2014/otp-bypass-via-source-page-inspection-3c6ac90a0fb5
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3899 (id 3899)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OTP Bypass via Source Page Inspection

Hello guys today I will explain an OTP (One-Time-Password) Bypass I found during a website penetration test. Lets get into it…

My initial step was to explore the website and understanding the functions used on it. After registering with my credentials, I returned to the login page for further analysis.

Upon entering my login credentials, I was directed to a second page where a text message containing an OTP was sent to my phone. This showed that the system had implemented Two-Factor Authentication (2FA), which is a good security measure.

However, while inspecting the requests sent and received via Burp Suite, I noticed something unusual there was no request being sent to validate the OTP code I entered. SO the OTP validation had to be performed on the frontend side of the application.

To delve deeper, I decided to inspect the frontend code. It didn’t take long for me to find the flaw: the OTP code sent to my device was embedded within the HTML code, hidden in an input element. When I used my browser’s inspection tool, I could expose the OTP code. And just like that, I had gained unauthorized access to the system, effectively bypassing the OTP.

In summary, the developers of this system left a security hole. The OTP bypass should have been validated on the backend server, where it could be better protected. In our case, the validation was unfortunately done on the frontend, leading to an easily exploited vulnerability.
