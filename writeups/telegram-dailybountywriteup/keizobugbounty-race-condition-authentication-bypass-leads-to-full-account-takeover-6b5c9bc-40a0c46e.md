# Race Condition Authentication Bypass Leads to Full Account Takeover

- **Source URL:** https://medium.com/@keizobugbounty/race-condition-authentication-bypass-leads-to-full-account-takeover-6b5c9bc0a54d?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@keizobugbounty
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5764)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Race Condition Authentication Bypass leads to Full Account Takeover

Bug bounty research was conducted to an large cap company with an eCommerce web application that facilitates purchasing and ordering of various products. The scope of this adventure focused on login functions. The login mechanism to this particular website utilizes One-Time Passwords (OTPs) delivered via email or SMS. The login process itself comprises a multi-step flow utilizing a unique identifier (flowId) to specify the account for which the OTP token is being validated. Specifically, the multi-step flow itself raises concerns regarding potential vulnerabilities to flow manipulation etc. because of it’s complex structure.

In more detail, the request flow unfolds as follows:

• **POST /init-email**: Initiates the login process with the user’s email and associates it with the specified flowId.

• **POST /send-email**: Sends the OTP to the designated email linked to the flowId.

• **POST /check-otp**: Validates the OTP provided by the user.

Each request includes the flowId parameter that points the request actions to the specific user attached to the flowId.

Notably, these requests can be sent in a different orders, such as initiating the email step before but also after sending the OTP. This could in theory create weird situations. However, attempts to initialize an email for one user, send the OTP, and then initialize an email for another user to log in with the first user’s OTP were unsuccessful.

Prior to [James Kettle](https://portswigger.net/research/james-kettle)’s publication of “[Smashing the State Machine](https://portswigger.net/research/smashing-the-state-machine)” the research encountered a hurdle due to the absence of applicable methods to bypass the authentication used in this website. However, following Kettle’s [publication](https://portswigger.net/research/smashing-the-state-machine) and the subsequent [enhancements](https://portswigger.net/blog/new-techniques-and-tools-for-web-race-conditions) of the Burp Suite’s turbo-intruder tool, the research resumed with a focus on exploiting a race condition vulnerability.

#### Race Conditions

Race condition attacks, are typically associated with limit-overrun scenarios like redeeming gift cards multiple times, involve exploiting simultaneous backend processes. This is achieved by submitting multiple redemption requests in rapid succession within a brief timeframe. This timing exploits the backend’s concurrent processing of multiple threads: one responsible for verifying the status of the gift card and another for marking it as utilized. As a result, the gift card can be applied multiple times, leading to a ”free money glitch.”

#### Race condition in login

In our login scenario, the race condition could be utilized by simultaneously changing the email attached to the specified flow in conjunction with verifying the OTP that was received to the original email. This would deceive the backend threads into authenticating the attacker as the victim by utilizing the OTP received by the attacker.

Main cause to this vulnerability is the fact that it is possible to update the email attached to the flow and verify the OTP code for the same flow simultaneously since these processes are done simultaneously by different threads.

The technical process of the attack unfolds as follows:

1\. The attacker initiates the email and sends the OTP request as usual.

2\. Upon receiving the OTP, the attacker configures Burp Suite repeater to send parallel init-email (with the victim’s email) and check-otp (with the received OTP) requests.

3\. By sending these requests simultaneously, the attacker successfully logs in as the victim.

The ”parallel” requests method, also referred to as a single packet attack, entails sending multiple HTTP/2 packets within a single TCP packet. This technique enables the possibility of sending multiple requests to the server that all arrive simultaneously. I highly recommend reading James Kettle’s [research](https://portswigger.net/research/smashing-the-state-machine) on this topic, as it provides invaluable insights.

This attack was possible due to the ability to change the email associated with the flow even after the OTP was generated for another email, thereby violating business logic rules. Additionally, the backend’s use of multiple threads for email initialization and OTP validation contributed to the exploit.

In the backend, the processes during this race condition attack would unfold as follows:

1. \[Thread A\]: Initiates the email initialization for the victim’s email associated with the prior initialized flowId for the attacker – resulting in success.
2. \[Thread B\]: Concurrently checks the validity of the OTP for the specified flowId – also resulting in success, as the first thread has not yet changed the flowId email to match the victim’s email.
3. \[Thread B\]: Subsequently, upon confirming the validity of the OTP, proceeds to retrieve the token for the user specified in the flowId. Since the first thread has now updated the email value, the token retrieved belongs to the victim user.

As a result of this vulnerability, it was possible to authenticate as any user on the website solely by knowing their email address. The issue was reported to the company, receiving a critical severity status and a substantial bounty reward.

#### Behind the scenes jargon

Of course when telling the findings in reader friendly style it seems like it is straightforward and easy to find this type of vulnerabilities. However what wasn’t told was that it always takes several iterations and trial and error until the vulnerabilities are found.. more often nothing is found. If it would be easy, it would have already been discovered by someone else ;)

Diagrams by: [https://sequencediagram.org/](https://sequencediagram.org/)
