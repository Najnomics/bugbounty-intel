# Race Condition leads to Cache Poisoning ?!

- **Source URL:** https://ltidi.medium.com/race-condition-leads-to-cache-poisoning-77bdfb9483fd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241008051047/https://ltidi.medium.com/race-condition-leads-to-cache-poisoning-77bdfb9483fd?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7497 (id 7497)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I have been researching about cache poisoning attack these days. While hoping to learn as much as possible and catch up with others top cache poisoning hunters / researchers as fast as I can, I discovered an edge use case of race condition which could potentially leads to Cache Poisoning DoS.

## The Stories

While doing “this and that” with my automation in order to build up methodologies to test for Cache Poisoning among a wide-scope targets which should be stable, accurate and without as much false positive as possible, I accidentally observed a weird behavior of some targets while responding to my test cases with high rate of requests combining of the valid — original and the poison requests which results to a status of response would be cached successfully. I tried to send each requests one by one to see what happens and was fail to replicate that behavior. I wondered if this is the result of the “collision” while the targets processing the concurrent requests combining both the valid and the poison …

For whom not familiar with Race Condition or Cache Poisoning, there would be lots of articles relevant to this read:

- [https://portswigger.net/research/smashing-the-state-machine](https://web.archive.org/web/20241008051047/https://portswigger.net/research/smashing-the-state-machine)
- [https://portswigger.net/research/gotta-cache-em-all](https://web.archive.org/web/20241008051047/https://portswigger.net/research/gotta-cache-em-all)
- etc

## Try to replicate the behavior

At first, I checked the requests that reach to the status which could poison the target’s cache response. I sent all those requests again and observed that I could not reach the targeting status of response. The responses kept sending back an error of detecting the poison payloads in my request.

I thought that it might be false positive when running the poison requests noisily to the targets. In order to confirm, I tried to continuously sending those poison requests concurrently with high rate limit. However, I still have not reach the targeting status of response even once. This behavior pushed me back to think that “It should be not false positive now”.

Back to the beginning, I would run all my automations again and carefully look its running. And yes, I reached to the status which could poison the target’s cache response again. But this time, I figured out that there was a mix between the original / valid request with the requests containing the poison payloads before having successfully poison the target’s cache response. Somehow, in the mix connection, the requests with poison payloads had been processed by the server without sending back the error of detecting poison payloads or invalid requests as before. As soon as the poison payloads had been processed by the server, it would reach the state that poison the target’s cache response. Weird and interesting, but it was quite clear then.

## Race condition + Cache Poisoning = 🔥

At this time, I knew that abusing the “collision” affect of doing race condition a mix of original / valid request with the requests containing the poison payloads, we could bypass the malformed requests detection of proxy or middleware processors, force the server the process our poison payloads and finally create magic !

In order to make a good explanation in the report, I managed to find an easy “STEP TO REPRODUCE” via Burp Suite.

Normally, sending the poison requests manually would be considered as bad and being responded by a “400 Bad Request” response which would not reach the cacheable / vulnerable status of the server.

After having played with Burp Suite & the idea of mixing original / valid request by doing race condition for a while, I discovered that we could take advantage of the Group feature of Burp Suite Repeater and the Send Group Requests feature to reproduce the idea in an easy and stable way.

**Here is how:**

- Create Repeater Group with the valid request & the poison request (the valid request would be the first request in the group)

- Choose Send group (single connection) and found the poison request would reach the status that is vulnerable / cacheable 🔥

## Summary

The case I showed in this read is just one sample of exploiting cache poisoning with race condition help. I hope that you guys could take the idea to combine with your skillsets / poison payloads to make more interesting cases because I could confirm that this behavior is not so rare out there.

As a Bug Bounty Hunter, you should find a way to mass-scan the issue in wide targets as well!

Happy reading and hunting!
