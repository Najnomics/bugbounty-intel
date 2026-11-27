# How I Found Dom Xss on School Website.

- **Source URL:** https://medium.com/@debug0xa/how-i-found-dom-xss-on-school-website-defcaa2a4455?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@debug0xa
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 9727)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## How I Found Dom Xss on a School Website.

Good evening everyone, I’m debug a bug bounty Hacker, so I was bored and I wanted to do something fun, I decided to check a school in my country.

I started by gathering sub-domains, using subfinder and assetfinder

#### subfinder -d target.com > subdomains.txt

#### assetfinder target.com > subdomains.txt

After gathering subdomains, I decided to know which one were alive or with 200,301,404 etc status codes, it’s very important to always know, so you won’t be wasting your time, you can use a tool called httpx for that 👇

#### cat subdomains.txt | httpx-toolkit -sc -tech-detect -title -silent

After doing this, I decided to check for parameters using the katana tool👇

#### cat subdomain.txt | katana > endpoints.txt

Then One url or subdomain got my attention target.com/?id=, so I thought I should test for xss first, then a GitHub tool came into my mind, xsstrike you can get it on GitHub , you might ask why not Burpsuite, I’ll just say I didn’t need the stress, so I used the tool, and I found a dom xss vulnerability on it 👇

### There you Go😉…it was a quick and easy Findings…. And I wanted to try and make this write up so Short.

Thanks for Reading till The End.

More crafts about my methodology will be published soon again.😮💨

Thank You🫡
