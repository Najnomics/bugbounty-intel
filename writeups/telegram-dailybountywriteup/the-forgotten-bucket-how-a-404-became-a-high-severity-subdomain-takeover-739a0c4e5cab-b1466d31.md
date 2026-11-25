# The Forgotten Bucket

- **Source URL:** https://0xkrishn.medium.com/the-forgotten-bucket-how-a-404-became-a-high-severity-subdomain-takeover-739a0c4e5cab
- **Fetched from:** https://0xkrishn.medium.com/the-forgotten-bucket-how-a-404-became-a-high-severity-subdomain-takeover-739a0c4e5cab?source=rss-df86adc1019f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14924 (id 14924)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Krishn Babariya / Fri, 25 Sep 2026 11:41:15 GMT

There is a particular kind of bug-hunting moment that looks completely uninteresting at first.

No SQL error.

No exposed admin panel.

No mysterious API response.

Just a **404**.

Most of the time, a 404 is exactly what it says it is.

But while testing a bug bounty program recently, I found an authentication-related subdomain that failed in a way that made me stop and look twice.

For this write-up, I will call it: https://auth.target.tld

The host was alive. HTTPS worked. Traffic was going through Cloudflare.

But instead of an application, the response contained this:

\<Error>

\<Code>NoSuchBucket\</Code>

\<Message>The specified bucket does not exist\</Message>

\<BucketName>auth.target.tld\</BucketName>

\</Error>

That changed the question immediately.

I was no longer asking:

*Why is this page returning 404?*

I was asking:

*Why is a trusted auth. subdomain still pointing to a cloud resource that no longer exists?*

That small difference turned a boring error page into a **High-severity subdomain takeover finding**.

I sent a simple request to the hostname through Burp Suite Repeater:

GET / HTTP/2

Host: auth.target.tld

The response came back as:

HTTP/2 404 Not Found

Server: cloudflare

X-Amz-Request-Id: \<redacted>

And inside the body:

Code: NoSuchBucket

Message: The specified bucket does not exist

BucketName: auth.target.tld

Three things immediately stood out:

1\. The hostname was still active.

2. The request was reaching infrastructure backed by Amazon S3.

3. S3 was saying that the expected bucket did not exist.

A missing page and a missing cloud resource are not the same thing.

If a bucket exists but is private, you will commonly see an authorization-style response such as 403 AccessDenied.

Here, the provider was telling me:

NoSuchBucket

The hostname existed. The resource it depended on did not.

That is exactly the kind of broken ownership relationship that can lead to a subdomain takeover.

At a high level, the infrastructure looked like this:

User

|

v

auth.target.tld

|

v

Cloudflare

|

v

Amazon S3

|

v

Expected bucket: auth.target.tld

|

v

404 NoSuchBucket

At some point, the company had apparently configured the hostname to use an S3-backed origin.

Later, the bucket disappeared. The public hostname did not.

That leaves a **dangling cloud resource**:

Company still controls the hostname

|

v

Cloud configuration expects a resource

|

v

That resource no longer exists

If the missing cloud resource can be claimed by another account, the hostname may begin serving content controlled by whoever owns that resource.

That is the core idea behind this class of subdomain takeover. But I did not want to report a vulnerability based on one error message alone.

So I started verifying each part independently.

A recognizable cloud-provider error is a clue.

It is not the entire proof.

I wanted to answer a more specific question:

*Does the expected S3 bucket actually exist?*

So instead of only requesting the company hostname, I queried Amazon’s S3 endpoints directly using the expected bucket name.

The checks were equivalent to:

curl.exe -I "https://s3.amazonaws.com/auth.target.tld/"

and:

curl.exe -I "https://s3.us-east-1.amazonaws.com/auth.target.tld/"

Both returned:

HTTP/1.1 404 Not Found

Server: AmazonS3

x-amz-request-id: \<redacted>

Now I had two separate sources telling me the same thing.

Live trusted hostname

|

+----> S3: NoSuchBucket

Direct S3 verification

|

+----> 404 Not Found

This was much stronger evidence than simply saying:

*“The page looks like an S3 error.”*

The bucket itself appeared to be absent.

At this point, I knew which conditions I wanted to verify, so I put them into a small Python script.

The verifier checked:

1\. Does the hostname still resolve?

2. Does the live host return the S3 NoSuchBucket condition?

3. Do direct S3 endpoint checks show the bucket as missing?

4. Is the real parent domain present on the Public Suffix List?

The interesting part was not the script itself.

It was that each check tested a different assumption.

The final chain looked like this:

Hostname is alive

+

S3 origin behavior is visible

+

Expected bucket is missing

+

The condition is reproducible independently

=

Credible takeover condition

The script eventually reached:

VERDICT: VULNERABLE

(bucket unclaimed, takeover possible)

A dangling bucket is already a meaningful infrastructure issue.

But the hostname made this particular case more interesting.

This was not something like:

old-images.target.tld

or:

unused-assets.target.tld

It was an authentication-themed hostname:

auth.target.tld

Think about how that looks to an ordinary user:

https://auth.target.tld/login

Even security-aware users are trained to look at the domain before trusting a login page.

In a successful takeover scenario, the attacker would not need to convince the victim to trust a random domain.

The content would appear under the organization’s own trusted namespace.

That creates an obvious phishing and impersonation risk.

The vulnerability was not simply:

*“There is a deleted S3 bucket.”*

The more useful way to describe it was:

***A trusted authentication-related hostname remained attached to an apparently unclaimed cloud resource.***

That is a much more meaningful security boundary.

There was one more detail I wanted to understand.

Could control of this subdomain potentially interact with cookies scoped to the parent domain?

To answer that question, I checked the **real parent domain** against the Public Suffix List.

The actual domain used during testing was **not present on the Public Suffix List**.

That means a configuration such as:

Domain=.target.tld

is technically possible.

But this is where it is important not to exaggerate impact.

I did **not** demonstrate:

cookie theft

session theft

cookie injection

account takeover

The Public Suffix List check only established that parent-domain cookie scope was technically possible.

Whether that could become exploitable would depend on the application’s actual cookie configuration.

I kept that distinction very clear in the report.

A useful rule I follow is:

Confirmed evidence != maximum theoretical impact

For this finding:

NoSuchBucket response           CONFIRMED

Expected S3 bucket missing CONFIRMED

Trusted auth hostname CONFIRMED

Dangling takeover condition CONFIRMED

Cookie/session compromise       NOT DEMONSTRATED

That makes a report much easier for a triager to trust.

There was an obvious next step.

Create the missing bucket. Upload a harmless HTML page. Show that it appears on the target’s subdomain. That would produce a spectacular proof-of-concept screenshot. I chose not to do it. All of my testing remained read-only.

I did not:

create or claim the S3 bucket

upload content

modify the target

set cookies

access customer data

attempt session compromise

By this point, I already had enough evidence to establish the security problem.

Bug bounty testing is not about seeing how far you can push a vulnerable system.

It is about proving the issue with the **minimum necessary impact**.

Sometimes stopping at the right point is part of the skill.

The bug can be understood as two pieces of infrastructure having different lifecycles.

Originally:

auth.target.tld

|

v

CDN / proxy

|

v

S3 bucket exists

|

v

Everything works

Then the cloud resource gets deleted:

auth.target.tld

|

v

CDN / proxy

|

v

S3 bucket: gone

The hostname configuration survives.

The resource it references does not.

And that leaves a dangling trust relationship behind.

The fix is straightforward:

If the hostname is no longer required:

Remove the DNS/CDN configuration.

If the hostname is still required:

Recreate and retain the expected resource,

then make sure its ownership cannot be lost.

The difficult part is usually not remediation.

It is noticing that the infrastructure has entered this state at all.

I kept the bounty report simple.

The core evidence was:

1\. The hostname was still active.

2\. Requests reached an S3-backed origin.

3\. S3 returned NoSuchBucket for the expected resource.

4\. Independent S3 checks also returned 404.

5\. The affected hostname was authentication-related.

6\. I performed no destructive takeover or customer-impact testing.

The report was accepted as **High severity**.

And I think that is one of the more useful lessons from this hunt:

The vulnerability was not technically complicated. There was no exotic payload. No race condition. No multi-stage exploit chain.

The interesting part was understanding what a seemingly boring error message meant about the infrastructure behind it.

The first lesson was to treat error messages as infrastructure clues.

There is a huge difference between:

404 Not Found

NoSuchBucket

BucketName: ...

x-amz-request-id: ...

The second response tells you something about the architecture.

The second lesson was to independently verify takeover conditions.

I try to move from:

"This looks vulnerable."

to:

"The live hostname behaves like this."

"The cloud provider expects this resource."

"The resource independently appears absent."

"These observations all agree."

The third lesson was that **context matters**.

A takeover condition on:

archive-static.target.tld

and one on:

may be technically similar. But the trust users place in those hostnames is very different.

Finally, I was reminded that proving a bug does not always mean exploiting it to its maximum possible impact.

Good research also means knowing when you already have enough evidence.

This is roughly what I now ask whenever I encounter a suspicious abandoned hostname:

Does the hostname still resolve?

Who is actually generating the error?

Is a third-party cloud service involved?

Does the response reveal the expected resource name?

Does that resource still exist?

Can I verify the missing-resource condition independently?

What would an existing-but-private resource return instead?

Does the hostname have a security-sensitive purpose?

Can the issue be demonstrated without claiming anything?

Not every dead hostname is vulnerable. Not every cloud error means takeover.

But if several independent checks point toward the same dangling resource, a boring error page can become a very interesting finding.

This entire investigation started with a 404.

The important part was noticing that the failure did not belong to the web application.

It belonged to the infrastructure underneath it.

The hostname still existed.

The cloud resource behind it did not.

That gap was enough to turn an abandoned authentication-related subdomain into a **High-severity security finding**.

Bug hunting often rewards complicated technical knowledge.

But it also rewards curiosity.

Sometimes the best question is simply:

\> **Why is it failing like that?**

Because every once in a while, the error page is the vulnerability.
