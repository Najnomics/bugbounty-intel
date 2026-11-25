# I Didn’t Even Open Burp Suite — One URL Change Exposed Hidden WordPress Content

- **Source URL:** https://medium.com/@The_Knower/i-didnt-even-open-burp-suite-one-url-change-exposed-hidden-wordpress-content-04c2a56125d2
- **Fetched from:** https://bugbountywizard.app/i-didnt-even-open-burp-suite-one-url-change-exposed-hidden-wordpress-content-04c2a56125d2?source=rss-871c67c0afac------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14962 (id 14962)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** The Knower / Tue, 27 Oct 2026 22:01:58 GMT

Hello, friend! 👋

I’m **TheKnower**, a Bug Bounty Hunter passionate about discovering vulnerabilities and making the digital world more secure.

In this article, I’ll share my findings and walk you through my research.

*How a simple browser test uncovered a potential access-control vulnerability in a WordPress print feature.*

When people think about web application security testing, they often imagine complicated payloads, proxy tools, and hours spent analyzing HTTP requests.

But sometimes, the most interesting discoveries start with something much simpler.

**I didn’t even need to open Burp Suite for this test.**

*During reconnaissance, I identified the website as running WordPress and discovered a print-related endpoint. I then modified its URL parameters directly in the browser to investigate whether the endpoint enforced proper access controls.*

Instead of immediately launching my usual testing tools, I decided to try something simple: modify the URL directly in the browser and see how the application responded.

I changed a few parameters, pressed Enter, and looked at the result.

What I found suggested that content intended to remain unpublished could be retrieved without logging in.

Here’s how I investigated it.

The website exposed a print URL similar to:

/archives/\[POST\_ID\]/?print=pdf

At first, it looked like a normal feature designed to generate a printable version of an article.

But URLs often reveal more than their intended purpose. WordPress uses query parameters to control how content is retrieved, so I wondered whether this endpoint accepted additional parameters that could influence the results.

Rather than starting with a complex payload, I began by modifying the URL directly in my browser.

My first test was to see whether the endpoint would return private posts.

I modified the URL to include these parameters:

?print=print-custom&post\_status=private&posts\_per\_page=10

Then I loaded the URL in the browser.

The response appeared to contain private posts without requiring authentication.

That was the moment the test became interesting. A feature intended to generate a printable document appeared to be doing more than changing the output format: it was potentially allowing a visitor to influence which content WordPress retrieved.

A single result wasn’t enough to understand the scope, so I continued testing.

Next, I changed the requested post status from private to draft:

?print=print-custom&post\_status=draft&posts\_per\_page=10

Again, the response appeared to return non-public content.

I then tested other content states, including pending-review posts and private pages. My observations suggested that the behavior was not limited to one specific post or status. The custom print functionality also appeared to support PDF output.

The key concern was now clear: **if an unauthenticated visitor could retrieve these records, the endpoint could expose content that WordPress was supposed to keep restricted.**

The browser test helped demonstrate the behavior, but understanding the underlying cause required examining the relevant implementation.

The code pattern I investigated parsed query parameters from the request and passed them into WordPress’s content retrieval function:

parse\_str($url\_data\['query'\], $args);

unset($args\['print'\]);

```
if (!empty($args)) {
    $posts = query_posts($args);
}
```
The important detail is that request parameters appear to be passed into query\_posts() after removing only the print parameter.

WordPress query arguments can influence which content is retrieved, including its post status and type. If the endpoint does not separately enforce authorization, an unauthenticated user may be able to request content they should not see.

To be precise, query\_posts() is not inherently a vulnerability. The security issue would be the absence of adequate authorization and input restrictions in the endpoint's actual implementation.

$doc\_type = explode( '-', $print );

/\* for search or archives \*/

if ( isset( $doc\_type\[1\] ) ) {

switch ( $doc\_type\[1\] ) {

case 'custom':

$url\_data = isset( $\_SERVER\['REQUEST\_URI'\] )

? wp\_parse\_url( sanitize\_text\_field( wp\_unslash( urldecode( $\_SERVER\['REQUEST\_URI'\] ) ) ) )

: array();

parse\_str( $url\_data\['query'\], $args );

unset( $args\['print'\] );

if ( ! empty( $args ) ) {

$posts = query\_posts( $args ); // attacker-controlled WP\_Query args

}

break;

...

*The relevant code pattern suggests that user-controlled query parameters can influence content retrieval.*

The practical impact depends on what the exposed records contain. A harmless test draft has a different impact from a private page containing confidential information.

This is why the finding should be assessed based on the actual data exposed, not simply the number of records returned.

The tests described here used read-only requests and did not intentionally modify content.

Finally

This vulnerability was reported to the program and triaged as **High severity**, but it was marked as a duplicate of a previously reported issue.

Even though it was a duplicate, the research was a valuable learning experience.

[I Didn’t Even Open Burp Suite — One URL Change Exposed Hidden WordPress Content](https://bugbountywizard.app/i-didnt-even-open-burp-suite-one-url-change-exposed-hidden-wordpress-content-04c2a56125d2) was originally published in [BugBountywizard](https://bugbountywizard.app) on Medium, where people are continuing the conversation by highlighting and responding to this story.
