# How I Could Have Shut Down Every Restaurant in Europe With One Click

- **Source URL:** https://medium.com/@TionoX/how-i-could-have-shut-down-every-restaurant-in-europe-with-one-click-0125387c1628
- **Fetched from:** https://medium.com/@TionoX/how-i-could-have-shut-down-every-restaurant-in-europe-with-one-click-0125387c1628?source=rss-e583088d7258------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14903 (id 14903)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohammed Ashraf / Tue, 08 Sep 2026 14:44:03 GMT

Sometimes a bug starts with a complicated attack chain.

Sometimes it starts with:

*“Hmm… what happens if I change this ID?”*

This one started exactly like that.

While testing part of its authorized bug bounty program, I came across an API responsible for managing restaurant delivery areas.

At first glance, it looked pretty normal.

Then I changed a restaurant ID.

And the API basically said:

*“Sure, why not?”*

That was the moment things got interesting.

The Partner Hub frontend uses an API similar to:

`GET /v2/deliveryarea/lists/shorts/{restaurantId}`
The frontend normally sends the authenticated restaurant’s own ID.

Something like:

GET /v2/deliveryarea/lists/shorts/12345678

The interesting question was:

**What happens if I replace that ID with another restaurant’s ID?**

So I changed it to a different, unrelated restaurant.

For this article, all identifiers below have been replaced with fictional values.

GET /v2/deliveryarea/lists/shorts/87654321

And I got:

HTTP/1.1 200 OK

With delivery-area information containing objects similar to:

```
{
  "id": 1876543210,
  "available": 1,
  "boundary": "POLYGON((24.3512 42.6901,23.3524 52.6917,24.3541 52.6912,...))"
}
```
Wait.

I wasn’t supposed to have access to this restaurant.

But the API returned its delivery areas anyway.

The important part wasn’t simply that the API returned an object.

It returned **another restaurant’s delivery configuration**.

The application was effectively trusting:

restaurantId from URL

instead of enforcing:

authenticated\_user → authorized\_restaurants → requested\_restaurant

In other words:

My account

|

v

My restaurant

|

X

|

v

Someone else's restaurant

The backend wasn’t properly checking that relationship.

Reading another restaurant’s delivery areas was already interesting.

Then I noticed something else in the JavaScript bundle.

The frontend contained mappings for the delivery-area API.

Conceptually, it looked like:

deliveryAreas:

restaurantId =>

smartGateway +

"/v1/delivery-area/list/short/" +

restaurantId

deliveryAreaEnable:

areaId =>

smartGateway +

"/v1/delivery-area/" +

areaId +

"/enable"

deliveryAreaDisable:

areaId =>

smartGateway +

"/v1/delivery-area/" +

areaId +

"/disable"

That immediately raised another question:

**If I can obtain another restaurant’s area ID, can I modify it too?**

I took one of the area IDs returned by the unauthorized read.

Again, the values shown here are fictionalized.

Before the test:

available = 1

Then I sent:

PUT /v2/deliveryarea/1876543210/disable

The response:

HTTP/1.1 204 No Content

A 204 by itself doesn't prove much.

So I queried the delivery area again.

Before:

After:

available = 0

The backend had actually changed the state.

Not a UI trick.

Not a cached response.

Not a fake success message.

An actual backend-side state transition.

I then restored the state:

PUT /v2/deliveryarea/1876543210/enable

And verified:

So the complete transition was:

1 → 0 → 1

Everything was restored immediately after testing.

At this point, the issue was no longer simply:

*“I can read another restaurant’s data.”*

It was:

*“I can modify another restaurant’s delivery configuration.”*

That changes the impact considerably.

A delivery area determines where a restaurant can deliver.

If an unauthorized user can disable that area, the restaurant could potentially stop accepting deliveries from an entire geographic zone.

Imagine a restaurant operating normally.

Then someone changes:

Delivery Area A

available = true

to:

Delivery Area A

available = false

Customers inside that area could potentially lose delivery coverage.

And the attacker doesn’t need access to the restaurant’s dashboard.

They don’t need to log into the victim restaurant.

They don’t need the victim’s credentials.

They only need an authenticated partner account.

The core issue appeared to be that the gateway was resolving the requested resource primarily from the identifier supplied in the request.

The application had contextual information such as the authenticated account and restaurant identity.

But the authorization layer wasn’t properly enforcing:

Does this user actually control restaurant X?

Instead, the effective logic looked much closer to:

Authenticated?

|

+-- Yes

|

+-- Take restaurantId from URL

|

+-- Return / modify object

The secure model should be:

Authenticated user

|

v

Authorized restaurants

|

v

Requested restaurant

|

+-- Match? --> Continue

|

+-- No -----> 403 Forbidden

That authorization boundary was missing.

Another interesting detail was that the delivery-area identifiers were numeric and appeared to be discoverable through the unauthorized read functionality.

That creates a potentially dangerous chain:

Restaurant ID

↓

Unauthorized delivery-area lookup

↓

Area ID

↓

Unauthorized enable/disable

The attacker doesn’t necessarily have to guess the area ID.

The vulnerable read endpoint can provide it.

This makes the write primitive considerably easier to automate.

Technically, yes.

And this is where things get a little scary.

I did **not** perform mass exploitation.

There was no reason to start randomly disabling real restaurants just to make a screenshot for a report.

The vulnerability itself, however, creates an automation opportunity.

Conceptually, an attacker could build a script that performs:

for each restaurant:

retrieve delivery areas

extract area IDs

disable selected areas

Which means the attack isn’t necessarily limited to one restaurant.

It could potentially be scaled.

In the worst-case scenario, an attacker could automate the process to affect a large number of restaurants.

Basically:

One vulnerable authorization check

+

Enumerable identifiers

+

Write operation

=

Very bad Tuesday

😅

For the actual bug bounty submission, I intentionally kept the impact demonstration controlled.

I verified the state transition on a test operation and immediately restored it.

I did **not** attempt to disrupt multiple restaurants.

I also provided the security team with reproduction steps so they could independently validate the behavior.

This is an important part of bug bounty testing:

**You don’t need to burn down the house to prove that the gasoline is flammable.**

Once you have demonstrated the unauthorized write and verified the backend state change, continuing to cause damage adds very little security value.

The final issue combined multiple security problems:

An authenticated partner account could access delivery areas belonging to another restaurant.

The response exposed delivery-area boundaries, including polygon/multipolygon coordinates.

The attacker could disable and enable delivery areas belonging to another restaurant.

Disabling delivery areas can affect where a restaurant is able to accept deliveries.

Because restaurant and area identifiers could be obtained and processed programmatically, the write primitive could potentially be automated across multiple targets.

That’s a pretty nasty combination for what initially looked like a simple IDOR.

The frontend was actually doing the right thing from a normal user-flow perspective.

It normally sent the logged-in restaurant’s ID.

But security cannot depend on:

*“The frontend wouldn’t normally send that.”*

Because an attacker doesn’t have to behave like the frontend.

If the browser sends:

GET /deliveryarea/lists/shorts/12345678

an attacker can send:

GET /deliveryarea/lists/shorts/87654321

The backend has to decide whether that request is authorized.

Not the JavaScript.

Not the UI.

Not the user.

**The server.**

The obvious remediation is to enforce object-level authorization before performing the lookup or modification.

For example:

Authenticated user

↓

Resolve user's authorized restaurants

↓

Check requested restaurant

↓

Allow / deny

For write operations, the server should additionally verify that the requested areaId belongs to a restaurant the authenticated user is authorized to manage.

Something equivalent to:

areaId

↓

Find owning restaurant

↓

Is caller authorized for this restaurant?

↓

YES → modify

NO → 403

Headers such as X-Stands-As should never be treated as a security boundary by themselves.

They can be useful for application context, but authorization must ultimately be derived from trusted server-side identity and access-control rules.

IDOR/BOLA vulnerabilities are often underestimated because the initial test can look ridiculously simple.

You change:

/user/123

/user/124

and suddenly everyone thinks:

*“It’s just an IDOR.”*

But the real question isn’t:

**“Can I change the ID?”**

The real questions are:

That’s where a simple IDOR can turn into a serious BOLA.

I didn’t actually go and shut down restaurants.

That would have been a terrible idea.

But from an attacker’s perspective, once you have:

Restaurant ID

↓

Delivery Area IDs

↓

Unauthorized disable endpoint

automation becomes the interesting part.

With a properly authorized test environment and a safe target set, the same logic could be wrapped into a script capable of processing many restaurants automatically.

So, in the most dramatic possible summary:

***One authorization bug + a little automation = a hypothetical “close everything” button.***

Please don’t make that button. 😂

The important lesson isn’t that I *could* disrupt the platform.

It’s that the backend should make sure **nobody without authorization can disable even one other restaurant’s delivery area in the first place.**

And that’s exactly why object-level authorization matters.

Never assume an ID in a URL is protected just because the UI only exposes your own ID.

Always test the authorization boundary:

Can I access another tenant's object?

Can I modify it?

Can I chain the two?

Can I automate it?

Because sometimes the difference between a low-impact IDOR and a P1 isn’t the IDOR itself.

It’s what happens **after you change the ID.**

Happy hunting. 🐛
