# The Art of Persistence

- **Source URL:** https://medium.com/@ziadabdo1255/the-art-of-persistence-scaling-recon-to-a-high-severity-stored-xss-on-ifixit-community-dbf1a822b4af
- **Fetched from:** https://medium.com/@ziadabdo1255/the-art-of-persistence-scaling-recon-to-a-high-severity-stored-xss-on-ifixit-community-dbf1a822b4af?source=rss-09e7e8318a71------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14909)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ziad  Abdo / Sat, 12 Sep 2026 12:50:47 GMT

We’ve all been there: staring blankly at Burp Suite while every single payload gets chewed up and spat out by rigid sanitization filters. That was exactly my reality while hunting on iFixit.

The main application was a fortified fortress. Inputs were encoded with surgical precision, WAF rules were tight, and standard XSS vectors died before they even reached the DOM. After hours of cycling through parameters, fuzzing endpoints, and watching payload after payload fail, mental fatigue started setting in. Frustration was creeping in fast, and I was seconds away from closing my laptop, calling it a night, and writing off iFixit as a total dead end.

Then came that familiar inner voice every bug hunter knows: “Just one last recon run. Just map the edge cases.”

I went back to raw subdomain discovery, pulling passive datasets and certificate logs to see if anything had slipped through the cracks. And there it was, sitting quietly among the list of modern endpoints: community.ifixit.com.

The moment I loaded that subdomain, I couldn’t help but chuckle. The UI looked so wildly out of place compared to the sleek main domain that I honestly couldn’t tell if I’d stumbled upon a forgotten digital artifact from 2005 or a random experimental build someone forgot to decommission. It practically radiated an aura of "Please test me, no security engineer has looked at this in years." That vintage, out-of-place aesthetic was the green light I needed. Burnout instantly turned back into adrenaline.

I immediately registered an account and began mapping features that persisted user data. **The Group Creation module** immediately caught my eye—a place where dynamic text wasn’t just stored, but displayed publicly to anyone browsing the directory.

Instead of dropping a basic, noisy alert(1) that any basic filter might block or a user might notice, I went straight for a weaponized, silent out-of-band payload:

I pasted it into the Group Name field and hit save. I checked the HTTP request in Burp Suite: 200 OK. The backend didn’t strip the dangerous \<svg> tag, nor did it HTML-entity encode the event handler. It accepted the raw payload and saved it directly into the persistent database.

Now came the moment of truth. I injected my payload directly into the Group Name field and hit save. I checked the HTTP request in Burp Suite: 200 OK. The backend didn’t strip the tags, nor did it HTML-entity encode the input. It accepted the raw payload and saved it directly into the persistent database.

Now came the moment of truth.

I injected my payload directly into the Group Name field and hit save. I checked the HTTP request in Burp Suite: 200 OK. The backend didn’t strip the tags, nor did it HTML-entity encode the input. It accepted the raw payload and saved it directly into the persistent database.

Now came the moment of truth.

I navigated back to the group directory and clicked on the newly created group page to open its details. The moment the page loaded, BOOM! An alert box popped up right on the screen, popping up my active document.cookie values.

The application was fetching the stored group name from the database and echoing it raw straight into the DOM context. The browser parsed the payload, executed the script natively within the community.ifixit.com origin context, and triggered the alert instantly upon page load—all with zero extra interaction required. Any user or administrator simply viewing that public group profile would instantly trigger the payload, exposing their active session data.

What started as a frustrating session on the verge of total burnout turned into a confirmed High-severity finding, all thanks to one rule every bug hunter should live by: When the front door is locked tight, look for the vintage side door that everyone forgot existed.

What started as a frustrating session on the verge of total burnout turned into a confirmed High-severity finding, all thanks to one rule every bug hunter should live by: When the front door is locked tight, look for the vintage side door that everyone forgot existed. GET request arrived, carrying the full document.cookie string—including the sensitive XSRF-TOKEN and session identifiers.

The application was fetching the stored group name from the database and echoing it raw into the DOM context. The victim’s browser rendered the unescaped \<svg> tag, executed the onload event handler natively within the community.ifixit.com origin context, and silently dispatched the session metadata straight to my server—all with zero user interaction required. Any user or administrator simply viewing that public group profile was instantly, silently compromised.

What started as a frustrating session on the verge of total burnout turned into a High-severity finding, all thanks to one rule every bug hunter should live by: When the front door is locked tight, look for the vintage side door that everyone forgot existed.
