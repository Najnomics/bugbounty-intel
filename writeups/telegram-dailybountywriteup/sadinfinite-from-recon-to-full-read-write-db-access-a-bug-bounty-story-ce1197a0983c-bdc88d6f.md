# From Recon to Full Read/Write DB Access — A Bug Bounty Story

- **Source URL:** https://medium.com/@sadinfinite/from-recon-to-full-read-write-db-access-a-bug-bounty-story-ce1197a0983c
- **Fetched from:** https://medium.com/@sadinfinite/from-recon-to-full-read-write-db-access-a-bug-bounty-story-ce1197a0983c?source=rss-6ebfbfd68929------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14943 (id 14943)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** SadInfinite / Sun, 11 Oct 2026 22:30:25 GMT

Here is how I gained a critical access over one their main infrastructure easily !

Hello there !

I am SadInfinite a Security Researcher / BugBounty Hunter. I was hunting on an HackerOne scope of a dutch company.

This was wildcard so I first enumerated domains and found which one of these was alive. Then I started a light fuzz on every single domain. On one of their main APIs domain I got a hit on a : /adminer

This normally refer to “Adminer” tool, a database management system requiring authentication (login+password), but…

Requesting this endpoint does not present a login form. Instead, the server responds with a 302 redirect that already contains valid connection parameters, and following it lands directly in an **authenticated Adminer session** connected to a production database (real-estate-api) hosted on internal infrastructure. From here, an anonymous, unauthenticated attacker can browse the full table list, inspect schema, and access table contents, including a table holding user credentials. It's also possible to edit data.

This is CRITICAL (only limited by the max. severity of the scope) because I had access over really sensitive informations like credentials and PIIs including for other systems about company. I had all about every employees. Moreover I was able to edit this data or delete it.

This was really quickly triaged (around 6 hours) and resolved in less than 48 hours :

I especially love this finding because it’s a good example of how we can go from recon to critical vulns with just a bit of automation and ideas.

Next time, think about adding such content discovery steps in your recon workflow so you will be able to find such vulns.

Thanks for reading that writeup !

Hoping we will meet again,

SadInfinite.

You can contact me by :

Mail : sadinfinite@outlook.com

Discord : sadinfinite
