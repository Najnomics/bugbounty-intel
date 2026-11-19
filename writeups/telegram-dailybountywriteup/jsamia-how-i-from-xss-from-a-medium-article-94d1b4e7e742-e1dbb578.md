# How I found XSS from a medium article

- **Source URL:** https://medium.com/@jsamia/how-i-from-xss-from-a-medium-article-94d1b4e7e742?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251020233146/https://medium.com/@jsamia/how-i-from-xss-from-a-medium-article-94d1b4e7e742
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6179 (id 6179)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found XSS from a medium article

Heres a simple story how I got a simple XSS after reading a medium article. For full context I recommend reading the original finders article by Prince Roy found [here](/@royzsec/bypassed-the-amazon-cloudfront-logic-and-got-xss-at-the-national-weather-agency-of-the-u-s-100af330430a)

Assuming you know the basics of how this XSS works, we will get into my side of the story

## Discovery

This wasn’t my normal discovery, I was reading through different articles and stumbled upon a story by the talented hacker Prince Roy (who you should follow if you don’t already). I noticed in his article that he posted links, and I love seeing stuff for myself so I clicked on them. This is where I noticed it was still giving the same response as he had originally got

I then tried his payload and noticed it didn’t work, I tried a few others and nothing either, but it still seemed vulnerable to me so I fired up dalfox to test for me. I unfortunately do not have the screenshots of dalfox running as this was found over a month ago.

`dalfox url https://training.weather.gov/pds/climate/index.php?unit=7`
It didn’t take long before it gave a hit! I then tested the payload and sure enough we got an XSS:

The payload in this case was:

`7%22%3E%3Csvg%2FOnLoad%3D%22%60%24%7Bprompt%60%60%7D%60%22%3E` I submitted this vulnerability to them, got a quick response saying it was valid and they would let me know when it was fixed. After not hearing anything for a few weeks I decided up to follow up and check in on the status and it was fixed!

I appreciate you guys reading and will hopefully be able to share a few more bugs soon!
