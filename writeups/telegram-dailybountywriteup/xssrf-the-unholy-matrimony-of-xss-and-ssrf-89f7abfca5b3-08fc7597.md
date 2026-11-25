# XSSRF

- **Source URL:** https://naumankh4n.medium.com/xssrf-the-unholy-matrimony-of-xss-and-ssrf-89f7abfca5b3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105163324/https://naumankh4n.medium.com/xssrf-the-unholy-matrimony-of-xss-and-ssrf-89f7abfca5b3?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4742 (id 4742)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **XSSRF : The Matrimony of XSS and SSRF.**

3 min readDec 17, 2023

--

بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ

In the Name of Allah (SWT) the Merciful, the Compassionate


Hey folks, [Nauman Khan](https://web.archive.org/web/20240105163324/https://www.linkedin.com/in/naumankh4n/) back in action! 🚀 Today, we’re diving into the depth of **XSSRF** — where Server-Side Request Forgery (SSRF) meets Cross-Site Scripting (XSS).

Lets Learn How I was able to turn an Informative(P5) SSRF to an High(P2) Severity Vulnerability And Got $$$ for it.

## **Vulnerable Functionality:**

- The web app provides users with an intuitive page creation wizard for marketing campaigns.
- A standout feature allows users to seamlessly integrate external pages into their marketing content.
- Users submit an external URL through the web app, indicating the source of the external page.
- Upon submission, the web app triggers a backend process to fetch the content from the provided URL.
- So Basically its an SSRF.
- But The backend Uses AWS Lambda functions And also there is proper checkings on the endpoint so, no metadeta retrieveal and no further Server Side attacks .
- Tried Many things to bypass the check but Failed .
- But there is something which we can make use of.
- The fetched content is stored within the web app.
- To facilitate user preview, a dedicated endpoint serves the stored response, displaying the external page within the app.
- However, a critical vulnerability emerges as the web app neglects to adequately sanitize the fetched content, potentially exposing the system to security risks.

## **Vulnerability:**

- Imagine an attacker submitting a seemingly innocent external URL.
- Due to the absence of content sanitization, the web app fetches and stores the entire content from the malicious URL without scrutinizing it for potential threats.
- The content retrieved contains a crafted XSS payload that, when previewed by unsuspecting users, it triggers the execution of malicious scripts within the web app.
- Woohoo !!

## Impact:

- Okay , the XSS triggers but Whats the Impact ??? Because I am the one who can create marketing pages And only I can view the preview …
- The WebApp Has feature to invite multiple marketeers to work on a campaign together.
- So if you have another guy who is working on same campaigns , You just need to tell them to visit preview endpoint which hosts our malicious scripts.
- And Wallaaah ! They got xssed!

The Initial Response from the team was like “*Its Not A bug Its A feature”*


And After explaining the Impact they assigned as an P2(High).


Thank You For reading :

Jai Hind / Intifada Inquilab
