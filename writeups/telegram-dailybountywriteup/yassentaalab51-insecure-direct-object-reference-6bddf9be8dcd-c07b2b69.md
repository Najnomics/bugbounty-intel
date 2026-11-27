# Insecure Direct Object Reference

- **Source URL:** https://medium.com/@yassentaalab51/insecure-direct-object-reference-6bddf9be8dcd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240816072930/https://medium.com/@yassentaalab51/insecure-direct-object-reference-6bddf9be8dcd
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6967 (id 6967)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Insecure Direct Object Reference (IDOR)

ا**للهم علمنا ما ينفعنا، وانفعنا بما علمتنا، وزدنا علما**

**“سُبْحَانَكَ لا عِلْمَ لَنَا إِلَّا مَا عَلَّمْتَنَا إِنَّكَ أَنْتَ الْعَلِيمُ الْحَكِيمُ**

Alright, so let’s start with a simple example to get what an IDOR (Insecure Direct Object Reference) is.

Imagine you and your friend work at the same company, and each of you has your own office. In those offices, you keep some pretty sensitive stuff, so naturally, you’ve each got a unique key to make sure only you can get in.

But here’s the thing: What if your friend somehow gets hold of your key? Now they can stroll right into your office and check out all your sensitive info.

The problem here is that while you each have a unique key, there’s no system in place to double-check that the person using the key is actually supposed to be there.

This is basically what happens with an IDOR vulnerability in a digital context.

Now, let’s get into the tech side of things.

Picture this: You’re shopping online, adding all sorts of goodies to your cart.

The app you’re using creates a endpoint like this:

`/cart?user=YOUR_USERNAME`
This URL is your personal space where only you should see what’s inside your cart.

But what happens if you change the \`YOUR\_USERNAME\` part to someone else’s username, like:

`/cart?user=FRIEND_USERNAME`
If the app doesn’t check whether you’re allowed to see your friend’s cart, boom — you’ve got access to their stuff.

That’s a serious security problem.

In this case, the app is dropping the ball by not verifying that you’re authorized to see that specific cart. This lack of proper checks is what makes it an IDOR vulnerability.

But wait, there’s more!

IDORs aren’t just about sneaking a peek at someone else’s info; they can also let you mess with someone else’s data. Imagine you can change your password by going to a endpoint like this:

`/change_password?user_id=1`
If the app isn’t careful, you could change someone else’s password just by swapping out \`1\` with their user ID.

Now that’s a serious problem — especially for things like password resets or account recovery.

## **Finding IDORs**

IDOR vulnerabilities can be found in various parts of a web application:

1.User Profiles

— Endpoint: \`/user/profile?user\_id=1234\`

Allows users to view their own profile information. If changing \`user\_id\` to another user’s ID grants access to that user’s profile, it indicates an IDOR vulnerability.

2\. Order History

— Endpoint:\`/orders/history?order\_id=5678\`

Shows the order history for a given order ID. If modifying \`order\_id\` allows access to other users’ orders, it’s a sign of IDOR.

3\. Messages or Notifications

— Endpoint: \`/messages/inbox?message\_id=9876\`

Retrieves a specific message based on its ID.

Changing \`message\_id\` to another value might let you access someone else’s messages.

4\. User Management APIs

— Endpoint: \`/api/users/{user\_id}\`

Retrieves or updates information for a specific user.

If you can change \`{user\_id}\` to another user’s ID and access or modify their data, it’s an IDOR vulnerability.

## So, how do you hunt these down? Here’s the game plan:

## Test Access Controls:

Start by creating two accounts

one for you and one for your “victim.”

Browse the site normally with one account, while running Burp Suite or another tool in the background.

Look for any endpoints with unique identifiers, like \`user\_id\` or \`order\_id\`.

Try swapping your ID with your victim’s ID. If it works and you get a 200 OK, bingo! You’ve got yourself an IDOR.

\- Handle Encoded or Hashed IDs:

Sometimes the ID is encoded or hashed.

If that’s the case, try decoding it with common schemes.

For hashed IDs, see if they’re predictable. If the algorithm isn’t super complex, you might be able to guess other users’ IDs by analyzing patterns.

-Offer Extra IDs:

If you don’t see any IDs in the requests, try adding them yourself. For example, if you’re fetching messages:

```
GET /api_v1/messages?user_id=YOUR_USER_ID
 
```
What if you add another user’s ID to the URL?


GET /api_v1/messages?user_id=FRIEND_USER_ID
Does it give you access to their messages? If so, you’ve hit the jackpot.


Try HTTP Parameter Pollution (HPP):

Sometimes you can exploit IDORs by passing multiple values for the same parameter. It’s rare, but worth a shot:


GET /api_v1/messages?user_id=YOUR_USER_ID&user_id=FRIEND_USER_ID


Change the Request Method:

If GET requests aren’t working, try POST, PUT, DELETE, PATCH — mix it up and see what happens.

References

\- Videos:

— [insiderPhD](https://youtu.be/cV0uoZTLVVY?si=5uGB07u1e3WxE-Os)

— [rs0n\_live](https://youtu.be/BfbS8uRjeAg?si=-0jzeQgZ3KGQpTRx)
