# Race Condition - Eating Rate Limits for Account Takeover

- **Source URL:** https://shahjerry33.medium.com/race-condition-eating-rate-limits-for-account-takeover-ff44b6dc8798?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250404130641/https://shahjerry33.medium.com/race-condition-eating-rate-limits-for-account-takeover-ff44b6dc8798?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9263 (id 9263)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Race Condition - Eating Rate Limits for Account Takeover

**Summary**

Race condition vulnerability occurs when websites process requests concurrently. Race conditions typically occurs in multi-threaded or multi-process environments where multiple threads or processes are competing for shared resources. A race condition attack depends on the relative timing of events and an attacker can manipulate this timing to cause unintended behavior in the application to perform some malicious tasks.

**Description**

I have found a race condition using which I was able to bypass the implemented rate limit on the login panel and was able to take over the account. On a website’s login panel, rate limit was implemented and I was not able to perform a brute force attack as the rate limit was blocking me but using the modified script for race condition I was able to bypass that rate limiting mechanism which led me to successful authentication bypass and get into an account.

**Anatomy of Race Condition Vulnerability**

Race conditions are often sensitive to timing and the success of an attack depends on precise timing manipulations. The period of time during which a collision is possible is known as the “race window”.

*What is Race Window ?*

**Race Window** refers to a time-frame during which a vulnerability can be exploited due to the concurrent execution of multiple threads or processes. It is the period in which the outcome of the program or system depends on the order and timing of events, leading to unexpected and insecure behavior.

**Example for easy understanding**

*Scenario: Help Desk Login Portal with Rate Limit*

Imagine a company has a help desk login portal where employees enter their credentials. To prevent brute force attacks, the system has a rate limit that allows only 5 login attempts per minute from a single IP address.

**Normal Behavior (Rate Limit Working Correctly)**

- You enter a wrong password
- You try again
- After 5 failed attempts, the system blocks further login attempts for 1 minute

Now normally, this prevents attackers from trying thousands of passwords quickly.

**How the Race Condition Bypasses the Rate Limit**

Instead of sending one login request at a time, you use a crafted script that:

1. Queues 100 login requests at once behind a “gate”
2. Sends all 100 requests simultaneously when the gate opens

*The flaw in the server’s logic:*

- The rate limit counter updates after processing each login request
- Since all 100 requests arrive at the same time, the server doesn’t block them immediately
- The server validates passwords first, then increments the rate limit counter

*Result:*

- Even though only 5 attempts per minute are allowed, you successfully send 100 password guesses before the counter updates (for demo I have only shown 6 attempts in above image instead of 100)
- If one of those passwords is correct, you gain access to the account before the rate limit blocks you.

**NOTE:** In above diagram I have shown 6th attempt because the rate limit that is being triggered after 5th invalid attempt will not be triggered here as the requests are queued and once all the 6 requests are launched the rate limit will be incremented by 1 only as all the requests reached the login panel at almost same time.

**How I found this vulnerability ?**

1. I went on the target website’s login panel, intercepted the login request > right click > Extensions > Turbo Intruder > Send to turbo intruder

2\. In Turbo Intruder, I loaded the modified script and from the notepad I just selected all the passwords, right clicked and copied it (a clipboard copy) and clicked on Attack

3\. After the completion of 100 requests in parellel, I got the valid credentials

**Modified Script**

**NOTE:** You will find the similar script **HERE** but it didn’t work for me, so I modified it a bit. For using the above script you can visit here [**Github**](https://web.archive.org/web/20250404130641/https://github.com/JerryShah3/Scripts-and-Payloads/issues/1).

**Why this happened ?**

In my opinion,

The bypass happened because the server checked the login credentials first and updated the rate limit counter afterwards, creating a timing gap (race window). When I flooded it with multiple login attempts in parallel, the server processed all the guesses before it could count them as separate attempts. This let me identify the correct password without triggering the rate limit, as the server only counted the attack as “1 try” instead of “100 tries”. The flawed order of operations and poor synchronization allowed me to “race ahead” of the rate limit.

**Impact**

The vulnerability allows attackers to bypass rate limits and identify the credentials of any user which ca lead to credential compromise and account takeover.

**CVSS Score & Explained**

***Vector String:*** CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N

***Score:*** 3.7 Low

*Explanation:*

Attack Vector (Network): The attacker can access the project over the network, as it’s a web application.

Attack Complexity (High): The race condition attack needs precise timing for a succession

Privileges Required (None): The attacker does not need any privilege to perform this attack

User Interaction (None): No additional user interaction is needed for the attacker to exploit the vulnerability.

Scope (Unchanged): The affected application is maintained by the same security authority.

Confidentiality (Low): There is an exposure valid credentials on succession

Integrity (None): The attacker is not able to modify any data here

Availability (None): The overall website remains accessible

**Mitigation**

To mitigate this issue it is recommended to implement below fixes

1. **Atomic Rate Limiting**: Increment the rate limit counter before validating credentials, not after.
2. **Lock Shared Resources**: Use locks/mutexes to prevent parallel processing of login attempts for the same account.
3. **Reject Overloaded Packets**: Treat HTTP/2 multiplexed requests as multiple individual attempts, not one.
4. **Add Server-Side Delays**: Introduce throttling (e.g., 2-second delay) after failed logins to slow brute-force attacks.

**NOTE:** Sorry for the delay in blogs as I was busy in certifications. I recently completed **OSCP+, OSCP, CRTP,** [**CRTSv2**](https://web.archive.org/web/20250404130641/https://www.credential.net/f68f4e4a-0cc7-4c24-9209-11af21751d3f#acc.P1Qo3Mjt) and [**CRTA**](https://web.archive.org/web/20250404130641/https://www.credential.net/d39516c6-c353-42a3-bfe0-d98023b2f661#acc.uzxpU2la) for red teaming.
