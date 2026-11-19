# OpenAI’s CHATGPT ATO Writeup

- **Source URL:** https://medium.com/@rohanroy_66407/openais-chatgpt-ato-writeup-ce5d5284aa5c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142208/https://medium.com/@rohanroy_66407/openais-chatgpt-ato-writeup-ce5d5284aa5c
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2153 (id 2153)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OpenAI’s CHATGPT ATO Writeup

Hello InfoSec Community, this is my first writeup and I am here with a technical breakdown of the vulnerability which was found in OpenAI’s ChatGPT. The vulnerability was Web Cache Deception. Basically it was possible to takeover someone’s account, view their chat history, and access their billing information without them ever realizing it.

Web Cache Deception: It allows attackers to easily expose the private information in a web application or in some cases takeover a victim account.

Caching:

1. helps to reduce latency from the server
2. serve the users with the content faster.

There are different types of caching mechanism -

1. CDN
2. Load Balancer
3. Reverse Proxy

How Caching Works:

Client sends request ([https://www.example.com/anything.css](https://www.example.com/anything.css)). First the request arrives at the caching mechanism and because the caching mechanism is not familiar with the file it asks the same to the web server. Web server sends the file to the caching mechanism and the caching mechanism decides whether the file should be cached or not (check which file it is so it looks at the end of the URL and it sees that it has .css extension (stylesheet) and if it is configured to cache static files then the file gets cached in the caching mechanism). And the caching mechanism sends the file to the user. Also next time when user asks for the same file the caching mechanism serves the file back to the user without asking from the web server as the file is cached.

Attack Scenario:

Lets suppose a user wants to access (hxxps://[www.example.com/account.php/anything.css](http://www.example.com/account.php/anything.css)). What happens in some cases is server sometimes returns 200 and URL does not change and instead the user is served with the content of /account.php (private information).

So a malicious user B sends the link (hxxps://[www.example.com/account.php/anything.css](http://www.example.com/account.php/anything.css)) to user A and when user A clicks on the link, the server sends the content of /account.php to user A with the response cached in the caching mechanism. And later when user B sends the same request he is also served with the /account.php page of user A. Also this happens only when user A is authenticated when he clicked the link at first.

If the content of the html has CSRF tokens or JWT the attack could be chained to direct ATO.

The same vulnerability was found in OpenAI’s ChatGPT. Basically it was possible to takeover someone’s account, view their chat history, and access their billing information without them ever realising it.

1. Nagli a renowned security researcher was exploring the requests that handle ChatGPT’s authentication flow and was looking for any anomaly that might expose user information. The following GET request caught his attention: (hxxps://chat.openai.com/api/auth/session). Basically whenever a user logs in to his/her ChatGPT instance, the application will fetch his/her account context, as in the email, name, image and accessToken from the server.
2. He had to force the load balancer into caching his request on a specific crafted path, so that he would be able to read victim’s sensitive data from the cached response. So in order to make the exploit work, he had to make the CF-Cache-Status response to acknowledge a cached “HIT”, which means that it cached the data, and it will be served to the next request across the same region. (A “DYNAMIC” response is received if the data is not cached)
3. Now as per caching, when a web server is deployed, the main goal of “Caching” is the ability to serve heavy resources faster to the end-user, mostly JS/CSS/Static files. In ChatGPT’s case it was Cloudflare. Goal was to find a way to load the same endpoint with one of the specified file extensions, while forcing the endpoint to keep the sensitive JSON data, so that the data gets cached.
4. First thing what Nagli did was that he tried to fetch the resource with a file extension appended to the endpoint, and see whether it would throw an error or display the original resource.

chat.openai\[.\]com/api/auth/session.css → 400

chat.openai\[.\]com/api/auth/session/anything.css → 200

It was shocking as OpenAI would still return the sensitive JSON with CSS file extension, it might have been due to fail regex or just OpenAI’s team not taking this attack vector into context. Now there was only one thing to be checked, whether he could pull a “HIT” from the cache server which he managed to get.

Full Attack Flow:

A) Attacker crafts a dedicated .css path of the /api/auth/session endpoint.

B) Attacker distributes the link (either directly to a victim or publicly).

C) Victim visits the legitimate link.

D) Response is cached.

E) Attacker harvests JWT credentials.

Remediation:

1. Manually instruct the caching server to not catch the endpoint through a regex. (Fix which OpenAI chose)
2. Don’t return the sensitive JSON response unless you directly request the desired endpoint.

(chat.openai\[.\]com/api/auth/session != chat.openai\[.\]com/api/auth/session/anything.css)

Interesting part is even this fix was bypassed by another security researcher using CRLF injection. Lets see how

1. Cache deception was fixed but a bypass attempt that failed on the Auth API worked on another API, giving access to all conversations’ titles of a user. By adding (%0A%0D) between anything and .css in the URL, the researcher was able to get a “HIT” cache status of an API request (not a static file).
2. This meant that an “API” request was cached since Cloudflare thought that it was a static file request that needed to be cached. Request looked like — GET /backend-api/conversations%0A%0D.css?offset=0&limit=20
3. Upon sending this request to the victim and him/her accessing it — his/her own “API” response will be cached, and if you recheck the same URL (fetching the cached response of the victim), it was possible to see the victim’s HTTP response which had the conversation titles.
4. The researcher thought the %0A%0D would also work on the Auth API but it was not possible. He thought CRLF chars were being escaped against the Auth session API but he suspected they would be able to catch other chars. (Regex is terrible at catching encoded whitespace characters, especially when it gets forwarded between different hops).
5. So he appended the URL-encoded representation of tabulation (\t) — %09, and the Payload (%0A%0D%09) worked. He managed to get Cf-Cache-Status as “HIT” hence bypassing OpenAI’s fix of the original ATO issue with a new payload. Also he figured out that all of the chat.openai\[.\]com APIs were vulnerable to the same bypass payload.
