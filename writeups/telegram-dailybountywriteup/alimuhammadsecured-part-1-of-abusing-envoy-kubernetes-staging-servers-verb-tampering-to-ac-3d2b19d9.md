# Part 1 of Abusing Envoy+Kubernetes Staging Servers & Verb Tampering to achieve XSS, IDORs, and…

- **Source URL:** https://medium.com/@alimuhammadsecured/part-1-of-abusing-envoy-kubernetes-staging-servers-verb-tampering-to-achieve-xss-idors-and-8f4620c035b2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251029125225/https://medium.com/@alimuhammadsecured/part-1-of-abusing-envoy-kubernetes-staging-servers-verb-tampering-to-achieve-xss-idors-and-8f4620c035b2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11539 (id 11539)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Part 1 of Hacking into a Fortune 500 Finance Company

There are 2 parts to this writeup to keep it from getting too long. When part 2 is released it will be here at the top.


When hunting on a site I tend to just poke around, gauge the functionality and see logically what can be broken before I fuzz.

The target was a large finance holding company. Almost all their domains were heavily locked down and required employee SSO credentials to use.

However, one of their sites let verified authors worldwide publish verified documentations and how-tos on the company’s own software, but publishing an article required strict approval by the site admins to prevent inappropriate content from being published.

I decided to finally perform some basic recon following these steps:

Critical Side Note in automated Fuzzing:

Always include a `User-Agent` header when fuzzing at the very least. I nearly missed a `P1` vulnerability by not doing this.

While using HTTPX to verify which subdomains were live, a few subdomains consistently returned as being unreachable. However, when I stumbled upon one of the supposedly unreachable subdomains when google dorking they were reachable-a whole asset I almost missed.

Turns out there was a reverse proxy in front of the domain silently dropping any request packets without a proper User-Agent header, adding to the detection difficulty, the Windows server behind the proxy had ICMP replies disabled making it truly appear as a non-live domain.

Even after adding proper headers, I still got inconsistent results with HTTPX. To this day, I haven’t found a reliable solution. Rate limiting was not the issue either, it loaded fine in the browser (even after 1000+ refreshes), but failed in HTTPX.


1. Fuzz subdomain VHOSTS via`FFUF`
2. `PureDNS` for direct DNS enumeration.
3. I also went through passive collection of subdomains by using tools such as `subfinder` and google dorking (`site:REDACTED.com` ).
4. Looked for related sister sites via:

- `FOFA`
- `SHODAN` (Via Favicon hash search)
- Fuzzing `TLD` via PureDNS (ex: REDACTED`.FUZZ` )

5\. Scanning ports via `Masscan` & `RustScan`

- I stopped over-relying on one tool and lowered the maximum packet rate as it typically leads to inconsistent results.

6\. Scrape endpoints from `GAU` , `WayBackURLS` , `Dorking`

- When dorking I use the [URL Extractor](https://chromewebstore.google.com/detail/ggiihlkbikggfknjgbocmogobagckdpc?utm_source=item-share-cb) extension to parse all the URLs from google searches as I dork.

7\. Exposed secrets by searching target-specific keywords on `Github` , `PostMan` , etc.

After cleaning up and collecting the list I realized there weren’t many subdomains this company offered, however there were two that stuck out to me the most:

- `staging.REDACTED.com`
- `testing-ignore.REDACTED.com`

The `testing-ignore` subdomain was inaccessible and had no digital footprint as to what it’s purpose was or what it was used for.

I shifted my focus to the staging server, I realized account takeover (ATO) may be possible if I registered an account using an email that existed in prod but not in staging. This would only work if both servers were using the same JWT signing keys.

Unfortunately, when registering a new account there’s an email verification sent-I could not bypass this. But then I caught myself falling into autopilot. I was just following the same checklist everyone runs through.

Why was I even trying to register with someone else’s email on staging in the first place? My goal was to obtain a JWT from staging and replay it against prod. But I was getting ahead of myself, I didn’t even examine the decoded JWT, what if there wasn’t even an email field at all?

I decoded a JWT from an authenticated login on staging and it looked like this:

But what if the server wasn’t even using the `email` claim in the JWT to query and identify users, but instead was using the `id` claim? I thought about this because it was an incrementing number instead of a `UUID`.

I confirmed this by registering multiple accounts on prod and noticed it go from `536`to `537`, `538`, etc. For further verification, I logged in, changed my email and noticed my JWT still had my old email address in it even though account settings displayed my new updated email.

Okay-that confirms my suspicions, the server isn’t even querying the email claim in the JWT anyway, it’s querying the id claim.

Furthermore, when I did attempt to use the staging JWT on prod it was denied complaining about an invalid signature. Turns out prod and staging used separate signing keys.

I was pretty much trying to replicate the same attack that  talks about in his youtube video [here](https://www.youtube.com/watch?v=0R3xHx7fPUM).

Before I gave up I clicked around on the staging domain and everything pretty much looked the same-until I went to profile settings and realized it displayed someone else’s email !

So we have ATO? No-if I tried to reset my password it would not show someone else’s email it would instead show `Hey Muhammad, please reset your password by clicking the link below:` . So what is going on?!

I decided to poke at the tech stack being used by this company, a few good techniques are I employ is by leveraging the `Wappalyzer` chrome extension, reading response headers sent back from the web server, and skimming any specfic keywords in the JavaScript files.

Turns out this service was using `Kubernetes`, `Nginx`, and `Envoy` proxies!

Why is this important you may be asking...? Well Kubernetes can get very complex and if you’re not careful with isolating the workflows for prod and staging there can be hidden mixups.

I think this company’s staging servers had separate envoy proxy configurations for different routes.

For example, in the staging server when I sent the password reset it may have internally routed my request to an internal endpoint within the correct staging cluster.

However, in the staging server, when I tried to view my user information the envoy proxy handling my request may have routed the request internally to a prod cluster instead of a staging cluster.

I suspect the developers had automated deployment pipelines that spun up staging environments whenever the production code changed, but failed to update all the Envoy routing configurations for certain endpoints. Because of this my staging userID was being mapped to a prod userID due to poor isolation between the two environments.

### Who Cares?

We now have leakage of mass PII of all accounts, we can create a script to register accounts on the staging subdomain, and then scrape the account information associated with it.

Turns out if you’re an admin your articles get auto-approved. I tested this by making a test article and it got auto approved on the staging server. Unfortunately, they also did not have isolation for their articles envoy configurations and it pushed it to the prod domain and I was able to over-write articles as the staging postId was lower than that of the prod (just like the userIds).

Not just this, but now we could perform authenticated fuzzing with an admin-privileged JWT on the staging server and uncover more hidden endpoints.
