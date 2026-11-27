# OTP Bypass through Session Manipulation

- **Source URL:** https://medium.com/@n4if/otp-bypass-through-session-manipulation-d73deceaa42f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260923021342/https://medium.com/@n4if/otp-bypass-through-session-manipulation-d73deceaa42f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6497 (id 6497)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OTP Bypass through Session Manipulation

## Introduction

I’m excited to share my journey into the world of OTP bypass vulnerabilities. Recently, I discovered a subtle but impactful flaw in a web login system that allows attackers to bypass OTP verification through session manipulation. This article will walk you through the discovery process, detailed steps, and the ingenious use of session cookies to exploit the vulnerability.

## Summary

During my recent bug-hunting adventure, I encountered a critical vulnerability in the OTP page of a web login component. This issue arises from improper handling of certain request parameters, enabling unauthorized access via response manipulation. The core of this exploit involves crafting session cookies using PIDM and WEBID parameters.

## The Discovery

In my investigation, I noticed something peculiar with the OTP page’s handling of user authentication. By analyzing the traffic between the client and server, I discovered that the PIDM and WEBID parameters in the POST request were used to create a session cookie. This insight came from using a valid OTP code and observing how the server responded.

## Key Observations

- Parameters Involved: PIDM and WEBID
- Exploit Technique: Response manipulation
- Impact: Unauthorized access through OTP bypass

## Understanding the Valid Response

Note: This vulnerability was discovered in a major organization; details are withheld for confidentiality.


To understand how the server crafts session cookies, I used a valid OTP code during testing. Here’s how the process unfolded:

- Using Valid Credentials and OTP:

After entering valid credentials and a valid OTP code, I observed the server’s response. The response included a session cookie crafted using PIDM and WEBID values from the POST request. For example:

valid OTP code in “VerC”

The server’s response was:

`Set-Cookie: SESSID=QlZOWEY3MTIzNDcyNA==`
- Decoding the Session Cookie:

Decoding this Base64 encoded cookie (QlZOWEY3MTIzNDcyNA==) revealed:

`BVNXF71234724`
This confirmed that the PIDM and WEBID were used to create the session cookie.

- Crafting a Session Cookie:

With this knowledge, it was clear that by crafting a session cookie using PIDM and WEBID, an attacker could bypass the OTP. Here’s how:

- Invalid OTP and Manual Crafting:

Even if an invalid OTP code is used, the attacker can craft a session cookie manually by combining PIDM and WEBID, encoding them using Base64, and manipulating the response to include this session cookie. This bypasses the need for a valid OTP.

## Get Naif Al-anazi’s stories in your inbox

Join Medium for free to get updates from this writer.

Here’s the crafted session cookie process:

```
PIDM=1234724
WEBID=BVNXF7
Combined: BVNXF71234724
Base64: QlZOWEY3MTIzNDcyNA==
```
The crafted cookie can be used to manipulate the server response.

- Observing Redirection to Dashboard:

After entering a valid OTP code, I noticed the server response contained:

```
<HTML>
<HEAD>
<meta http-equiv="refresh" content="0;url=/app/dashboard?welcome=true">
</HEAD>
</HTML>
```
## Proof of Concept (PoC)

Here are the detailed steps to exploit the vulnerability:

- Log in with Valid Credentials:

Enter valid credentials on the login page to be redirected to the OTP page.

- Submit Any OTP:

Enter a random number in the OTP input field and capture the POST request:

Random number in VerC

- Crafting the Session Cookie:

Combine PIDM and WEBID values:

```
BVNXF71234724
Base64: QlZOWEY3MTIzNDcyNA==
```
Use this Base64 encoded string as the session cookie.

- Manipulating the Response:

Intercept the server’s response and modify it to include the crafted session cookie:

When you send the Post request, intercept the response and add the cookie you craft

- Access the Dashboard:

The manipulated response, containing the crafted session cookie, will redirect you to the dashboard, effectively bypassing the OTP verification.

## The Intricacy of the Bug

*The breakthrough in this discovery was realizing that session cookies could be crafted using PIDM and WEBID. By analyzing the server’s response to a valid OTP and understanding how the session was managed, I deduced that these parameters could be combined and encoded to create valid session cookies.*


## Steps to Discovery:

1. Parameter Analysis: Used a valid OTP and observed that the server crafted a session cookie using PIDM and WEBID.
2. Session Behavior Investigation: Confirmed that the session cookie could be replicated manually by combining and encoding PIDM and WEBID.
3. Parameter Manipulation: Crafted session cookies manually to test the bypass mechanism.
4. Response Manipulation: Used the crafted session cookie in the response to bypass OTP verification.

This finding was intriguing because it showed that the system’s session management mechanism inadvertently exposed a path to bypass critical security measures. The ability to craft a session cookie using PIDM and WEBID revealed a hidden vulnerability that could be exploited by understanding and manipulating session behavior.

## Impact

This vulnerability allows attackers to bypass OTP verification, posing significant risks to the confidentiality, integrity, and availability of the affected system. By understanding and exploiting session management flaws, attackers can gain unauthorized access without requiring valid OTPs.

## Conclusion

The journey to uncovering this OTP bypass vulnerability was both challenging and rewarding. It highlights the importance of meticulous analysis and a deep understanding of session management in web applications. Ensuring secure setups and prompt response to potential vulnerabilities is crucial for maintaining robust security.

For further insights or discussions on this topic, feel free to connect or comment below.

Stay secure,

Naif Al-anazi

Follow me in LinkedIn for more: [https://www.linkedin.com/in/n4if](https://www.linkedin.com/in/n4if)
