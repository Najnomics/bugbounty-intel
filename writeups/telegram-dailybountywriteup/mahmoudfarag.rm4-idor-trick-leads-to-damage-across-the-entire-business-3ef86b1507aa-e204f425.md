# IDOR Trick Leads to Damage Across the Entire Business

- **Source URL:** https://medium.com/@mahmoudfarag.rm4/idor-trick-leads-to-damage-across-the-entire-business-3ef86b1507aa
- **Fetched from:** https://medium.com/@mahmoudfarag.rm4/idor-trick-leads-to-damage-across-the-entire-business-3ef86b1507aa?source=rss-435542f7a180------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14937)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mahmoud Farag / Wed, 07 Oct 2026 01:28:46 GMT

الحمد لله، والصلاة والسلام على رسول الله

I’d like to share a security finding I discovered during my research.

A books platform let you delete a review through two different endpoints. One of them checks that the review is yours. The other one doesn’t — it just deletes whatever ID you hand it.

The catch is that you can’t get somebody else’s review ID from the website. Reviews are written in the mobile app.

I started on the web application, doing what any user would do: I opened a book and went to leave a review.

There was no way to.

The site shows you the reviews other people wrote, their star ratings, the whole listing — but nowhere to write one yourself. To post a review, you need the mobile app. That’s the only place the feature exists.

That’s an interesting shape for an application to have. A whole write path that lives in one client and not the other, on a platform whose entire purpose is reviews. Two clients, one feature, and only one of them was built to handle it — which usually means only one of them was tested for it.

So I downloaded the mobile app.

Then I wrote a review from the phone and watched the request go out:

`POST /api/books/{book_id}/reviews`
And the response came back carrying the "review\_id" of the review I had just written.

That’s the value the browser never sees. The web front-end never creates a review, so it never handles a fresh "review\_id", so that identifier had never once appeared in my browser traffic.

I had it now. And the only question left was whether the web API would take an identifier that came off the phone.

I copied the ID out of the mobile request, pasted it into the equivalent request on the web side, and sent it.

It took it.

I wrote a review from the app as "User B", kept the "review\_id", then logged into the website as "User A" — a completely separate account, no relationship to User B, no special role.

Then, with User A’s session:

```
DELETE /api/books/{book_id}/reviews/{review_id} HTTP/2
Host: target.com
Cookie: <User A session>
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
```
HTTP/2 204 No Content

No error. No ownership complaint.

I checked the review:

`GET /api/reviews/{review_id}`
HTTP/2 404 Not Found

User B’s review was gone. Deleted by an account that had nothing to do with it, using an ID that came out of a different client entirely.

Worth being precise here, because it’s the thing that makes this finding what it is.

The app isn’t a bypass. It’s just the only place in the product where a "review\_id" is put in front of a user.

The server treats that identifier as a global object reference. It doesn’t care that it was minted by the mobile backend, it doesn’t care which client is presenting it, and on the nested route it doesn’t care who’s asking. A value that the mobile API hands to its author is a live delete handle on the web API in anyone’s hands.

Which means the boundary the platform was relying on — *you only ever see your own review IDs* — is a UI boundary, not an authorization one.

Any authenticated user can permanently delete another user’s review by supplying its review\_id.

Because reviews directly affect the books’ ratings and visible feedback, an attacker can repeatedly delete legitimate reviews and manipulate the platform’s review content and ratings.

Thank you for taking the time to read my write-up.

LinkedIn: [https://www.linkedin.com/in/mahmoud-farag4](https://www.linkedin.com/in/mahmoud-farag4)
