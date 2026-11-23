# IDOR

- **Source URL:** https://medium.com/@tanyago/idor-deleting-comments-like-a-boss-0413a375024f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240901190023/https://medium.com/@tanyago/idor-deleting-comments-like-a-boss-0413a375024f
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7110 (id 7110)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR : Deleting Comments Like a Boss!

Hello everyone, it’s been a while since I last posted some blogs. In this post, I’m going to share how I found IDOR (Insecure Direct Object Reference) vulnerabilities on two websites. Unfortunately, I didn’t get any response from one of the websites, and on the other, my report was marked as a duplicate. So without further delay, let’s discuss the bugs.

# First Website

While exploring the website’s functionality, I came across the comment section, which often feels like a treasure trove for vulnerabilities. I posted a comment on the site and then checked the request and response in Burp Suite. Everything seemed normal at first. Next, I deleted my comment and observed the request and response again. This time, the request included two parameters: `Token` and `reply id`.

I wondered if I could change this `reply id` to another user's reply id. But the main challenge was: How would I get another user's reply id? To figure this out, I liked another user’s comment and intercepted the request. In that request, I found the user’s reply id.

I copied the other user’s reply id and replaced it in the delete comment request. And WOW! The comment was deleted.

STEPS :

1. Like the comment of the victim and intercept the request
2. Copy the reply id and drop the request
3. Post any comment on the website
4. Delete the comment and intercept the request
5. Change the reply id to victim reply id and forward the request
6. Victim’s comment is deleted

With this method I was able to delete the post of the other user’s also. But sadly, I never received any response for this bug.

# Second Website

On the second website, I again found a comment section, so I posted a comment and then deleted it. In the delete comment request, I noticed two parameters once more.

Again, I thought about changing the comment id to the victim’s comment id, but I wasn’t sure how to obtain the comment id. In this case, there was no option to like comments. So, I searched through my Burp Suite history, and guess what? I found a request where all the comment ids were leaking in the response. I simply copied the other user’s comment id and replaced it in the delete comment request, and boom — the comment was deleted. Sadly, this report was marked as a duplicate, but no worries — I got some content for my blog from this finding.

I hope you enjoyed this blog . Let’s meet in the next post. Keep spreading knowledge.
