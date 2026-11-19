# How to Find SSRF Bugs That Pay

- **Source URL:** https://masimshahzad.medium.com/how-to-find-ssrf-bugs-that-pay-hunting-server-side-request-forgery-in-url-fetch-and-image-import-63e5c93ab433
- **Fetched from:** https://web.archive.org/web/20261106110833/https://masimshahzad.medium.com/how-to-find-ssrf-bugs-that-pay-hunting-server-side-request-forgery-in-url-fetch-and-image-import-63e5c93ab433
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14963 (id 14963)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How to Find SSRF Bugs That Pay: Hunting Server Side Request Forgery in URL Fetch and Image Import Features

The server will fetch any URL you give it. The whole game is choosing a URL the server should never visit.

*Cover image: AI generated illustration made in Canva.*

Every modern app fetches URLs for you. It imports a profile photo from a link. It builds a preview of a page you shared. It calls a webhook when an invoice is paid. Each of those helpful features hands the server a destination chosen by a user, and that is exactly where this bug lives.

Disclosure: This article was researched and written with AI assistance, and it was checked for accuracy and originality before publishing.

By the end of this article you will understand what server side request forgery really is, why cloud metadata makes it so valuable, how hunters prove it safely with their own callback servers, and how developers can shut it down properly. No live target is needed to learn any of this. The method is taught for authorised testing only.

## The bug class, explained simply

Server side request forgery, usually shortened to SSRF, happens when an application takes a URL from a user and fetches it from the server without properly controlling where that request may go.

The difference between your browser fetching a URL and a server fetching it is position. Your browser sits outside the company network. The server sits inside it. The server can often reach internal admin panels, internal APIs and cloud services that the public internet can never touch. When you choose the URL, you borrow the server position, its network trust and sometimes its cloud identity.

The most famous internal destination is the cloud instance metadata address, a link local address that cloud servers use to learn about themselves. On some cloud setups that address can hand out temporary credentials for the cloud account itself. That is why a small URL field can become a critical finding. The bug is not the fetch. The bug is the missing control over the destination.

HackerOne published a useful spotlight on this class, collecting disclosed cases where curiosity about a fetch feature uncovered much deeper access. You can read it at [https://cybernoz.com/spotlight-on-the-server-side-hackerone/](https://cybernoz.com/spotlight-on-the-server-side-hackerone/) and a second copy of that spotlight at [https://hackernoon.com/spotlight-on-the-server-side-a-guide-to-ssrf-vulnerabilities-7o3d3466](https://hackernoon.com/spotlight-on-the-server-side-a-guide-to-ssrf-vulnerabilities-7o3d3466)

In one disclosed case in that spotlight, work that began around a PDF generation feature led to a server side request issue with serious internal reach, and the programme awarded a 4000 dollar bounty after a careful fix. In another disclosed case discussed there, a researcher showed that a fetch path could have reached cloud metadata keys and internal files. The lesson repeats across cases. The first signal is usually small. The impact depends on what the server can reach next.

## How the bug was found

Good SSRF hunting starts by listing every feature that makes the server fetch something.

1\. Image import by URL, avatar upload by link and product image fetch.

2\. Link preview, bookmark import and website screenshot features.

3\. Webhooks, integration callbacks and payment notification testers.

4\. PDF builders, feed readers, file import from a remote URL and video or audio transcription by link.

5\. Any API parameter named like a URL, a host, a callback or a redirect target.

For each feature, the hunter first supplies a URL on a server the hunter controls. If the application server connects to that callback, the fetch is confirmed and the request headers often reveal the server software and its cloud environment. This is safe proof. The callback belongs to the hunter, and no internal system has been touched yet.

Next, the hunter studies how the application validates the destination. Does it block plain words, or does it resolve the address and check the real destination? Weak validation is the heart of most SSRF findings. A filter that checks the text of a URL can be confused by redirects, by address formats the filter did not expect, or by a public name that resolves to an internal address at fetch time. Hunters describe these classes in general terms in reports, prove the smallest possible reach, and stop.

## Get Muhammad Asim Shahzad’s stories in your inbox

Join Medium for free to get updates from this writer.

The strongest reports then answer one question with evidence. What can this server reach that an outsider should never reach? A blind callback proves the fetch. A response from an internal health endpoint proves internal reach. Cloud metadata access, proved with the minimum necessary evidence and reported at once, proves critical impact. Hunters must never keep cloud credentials, never use them to move deeper, and never pull real data beyond the smallest proof a triage team needs.

*Where SSRF Hides: image import, link preview, webhooks, PDF builders and feed readers are the features where a user chosen URL most often reaches the server. This image is an AI generated illustration made in Canva.*

## Impact, in plain words

A basic SSRF that only fetches public pages is low value. It wastes server resources and little more.

An SSRF that reaches internal services is serious. Internal admin tools often trust requests that come from inside the network, so a forged request can read internal data or trigger internal actions that were never meant to be public.

An SSRF that reaches cloud metadata can be critical. Temporary cloud credentials can open storage, databases and whole cloud accounts. That is why programmes pay far more for demonstrated internal or metadata reach than for a simple callback. Your report should explain the reach in business language. State what the server could touch, what data or control that would give an attacker, and where you stopped.

## How to find it and how to fix it

Hunt with a callback first, always. Confirm the server fetches your URL, record timing and headers, then test validation classes one at a time and document each result. Slow responses can also hint at internal destinations, but timing alone is weak proof, so pair it with a controlled callback whenever you can.

*The Safe Fetch Checklist: allowlist hosts, check the resolved IP, validate redirects, and give the fetcher no cloud credentials. This image is an AI generated illustration made in Canva.*

For defenders, the fix is an allowlist, not a longer blocklist.

1\. Allow only the hosts or host patterns the feature truly needs, and only the http and https schemes.

2\. Resolve the name before fetching, check the resolved address against private, loopback and link local ranges, and fetch the checked address so a second resolution cannot swap it.

3\. Block redirects to new destinations, or validate every redirect hop with the same rules.

4\. Give the fetching service no cloud credentials by default, and require the stronger metadata mode that needs a session token where your cloud offers it.

5\. Put the fetcher in a restricted network segment with no route to internal admin services.

6\. Log every outbound fetch destination and alert on attempts to reach metadata or internal ranges.

Verify the fix by repeating the original tests. Your controlled callback for an allowed public URL should still work if the feature needs it. Callbacks and fetches toward internal ranges, metadata addresses and redirect tricks should all fail, and the failures should appear in the logs.

## Closing takeaways

SSRF rewards hunters who think about position. Ask what the server can see from where it sits, not only what the page shows you.

Proof grows in steps. A callback proves the fetch. Internal reach proves the risk. Minimum metadata evidence proves critical impact, and then you stop and report.

The lasting fix is positive control. An allowlist, checked resolved addresses and a fetcher with no cloud identity will beat any blocklist that tries to guess every bad destination.

Sources credited in this article: the HackerOne SSRF spotlight linked in the body above, which collects publicly disclosed reports, and the public OWASP guidance on server side request forgery prevention. All research is based on publicly disclosed material only.

Tags: Bug Bounty, Cybersecurity, SSRF, Web Security, HackerOne

Written by Muhammad Asim Shahzad, SVP Head Application Security and VAPT at UBL, with thirteen plus years in offensive security, HackerOne Top 100 history, Synack Red Team experience and CVE 2021 31521 to his name. More writing and services at protector47.com. Connect with Asim on LinkedIn at [https://www.linkedin.com/in/protector47](https://www.linkedin.com/in/protector47) and find his public researcher history through HackerOne under the name protector47.
