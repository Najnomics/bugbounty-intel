# Unauthenticated DaData Relay

- **Source URL:** https://medium.com/@abdoalkaser53/unauthenticated-dadata-relay-leaking-fns-registry-records-and-burning-a-paid-api-quota-122cef28e8a4
- **Fetched from:** https://medium.com/@abdoalkaser53/unauthenticated-dadata-relay-leaking-fns-registry-records-and-burning-a-paid-api-quota-122cef28e8a4?source=rss-f83275467ea4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14964 (id 14964)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Abdo Alkaser / Fri, 30 Oct 2026 05:45:34 GMT

*Missing authentication on a backend proxy*

dadata-client-\*\*.\*\*.ru is a backend service that relays requests to DaData, a paid Russian registry-lookup API. Its /suggestions/party endpoint accepted anonymous POST requests with no token, cookie, or API key, and returned full FNS (Federal Tax Service) registry records for any search term. A sibling service on the company’s own backend correctly returns 401 Unauthorized for the equivalent lookup, which makes this a one-instance misconfiguration, not an intentional public API. I reported it as Standoff365 report #37253 (CWE-306, rated Medium by me). It was closed as a duplicate of #37076.

DaData is a commercial service that returns structured data about Russian legal entities and individual entrepreneurs: names, tax IDs, addresses, directors, and more. Companies usually pay per request or per plan, and they put a small proxy service in front of it so the API key stays on the server.

A proxy like that is only safe if it checks who is calling it. If it doesn’t, anyone on the internet can spend the owner’s paid quota. The key stays hidden, but the service is effectively public.

The target matched the program’s published wildcard scope, so it was in scope.

One request, no credentials:

curl -sk -i -H "X-Bug-Bounty: alkaser" -H "Content-Type: application/json" \

-d "@body.json" "https://dadata-client-\*\*.\*\*.ru/suggestions/party"

`{"query":"Sberbank","count":3}`
The response was 200 OK, returning full registry records for every match: legal name, INN, OGRN, KPP, OKPO, director name and title, registration and actuality dates, full registered address with FIAS id, GPS coordinates, and nearest metro stations.

To see whether there was any cap on how much data one request can pull, I tested the count parameter.

So input validation works, and the only limit I saw is 20 rows per request. I found no sign of a per-client limit. I did not run volume tests, to stay within safe testing practice.

Is this endpoint meant to be public? I checked the company’s own backend:

curl -sk -i -H "X-Bug-Bounty: alkaser" \

"https://\*\*-sellplus-backend.\*\*.ru/api/Suggestion/fio/?query=test"

The response was 401 Unauthorized with WWW-Authenticate: Bearer.

The same company protects the same kind of lookup everywhere else, and only this instance is open. That is the difference between “public API by design” and “broken access control”.

What it is **not**: no customer data was exposed, and the findById-style routes returned 404. This is broken access control plus third-party quota abuse, not a breach of the company’s own application data. I state that clearly because it keeps the severity honest.

**Fix:** require authentication on the relay (the same Bearer scheme already used on the main backend), restrict it at the network or mesh level so only internal services can reach it, and add per-client rate limiting.
