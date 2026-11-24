# IDOR to read all user’s private route comments

- **Source URL:** https://medium.com/@youssifm.raghib/idor-to-read-all-users-private-route-comments-e97120d43262?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240607012044/https://medium.com/@youssifm.raghib/idor-to-read-all-users-private-route-comments-e97120d43262
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5599 (id 5599)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## **IDOR to read all user’s private route comments**

hello Hackers, this is my first writeup i will shows you how i can read all user’s private route comments.

| **Understanding target**

This target is for sports and exercises, its a public program. It allows the user to create his own exercise and share it with friends. You can share the result of your exercise as a post. There are two types of exercises, routes and workout, and there are three types of post privacy: public post, private post and friend only post.

You can infer each type of privacy from its name, but for clarification

Public post: Any user can see it, interact with it, and see its comments

private post: No one can see it except you

friends only post: Only people on your friends list can see it.

| **the bug**

while i am testing this target, after creating the route i noticed that if I write more than five comments, a new function appears that caught my attention called read all comments.

Immediately, I turned on the interceptor and clicked on read all comments

I found the request like this.

The parent\_story\_id parameter caught my attention

I thought to myself: What if I changed this ID to the victim’s private post ID?

So I actually changed the ID to the victim’s ID and boom.

In the response there are all the comments of the private post and information about who made the comments.

**i reported this bug and get accepted as a valid issue.**

my linkedin: [Youssif Mohamed](https://www.linkedin.com/in/youssif-mohamed-08b5032a7/)

i hope you enjoy this writeup don’t forget to like :).
