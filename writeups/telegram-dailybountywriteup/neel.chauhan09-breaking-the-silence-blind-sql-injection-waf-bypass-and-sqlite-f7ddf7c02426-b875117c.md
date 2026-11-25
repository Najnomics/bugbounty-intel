# Breaking the Silence

- **Source URL:** https://medium.com/@neel.chauhan09/breaking-the-silence-blind-sql-injection-waf-bypass-and-sqlite-f7ddf7c02426
- **Fetched from:** https://medium.com/@neel.chauhan09/breaking-the-silence-blind-sql-injection-waf-bypass-and-sqlite-f7ddf7c02426?source=rss-dc15ab41b8c5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14925)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Neel Chauhan / Sat, 26 Sep 2026 19:00:35 GMT

*How a simple analytics filter became a Boolean oracle for database extraction*

Hello guys, so you know there is a particular kind of satisfaction in a challenge that refuses to give you anything for free. No stack traces, no verbose errors, no helpful 500 pages. Just a single page that says either *"Records found."* or *"No records match."* and dares you to make sense of it.

That was **Insight**, an “analytics dashboard with a filterable report.” The objective was blunt: obtain config.admin\_api\_key and recover the flag. And there was a hint that turned out to be the whole puzzle in disguise, though I didn't realise it at the time: *"the report may answer more than it appears to, if you ask indirectly."*

This is the story of how a text box that only knew two sentences ended up spelling out a secret it was built to protect. The techniques matter, but what I really want to walk you through is the **reasoning**: how I got from “a filter box” to “arbitrary database read” by listening carefully to what the application was telling me.

The page was almost aggressively simple. One input, category, submitted over GET, reflected back into a server-rendered form. No JavaScript, no API calls, no tokens riding along in headers. Just this:

category=sales   → Records found.

category=test → No records match.

category= → Enter a category.

Most people glance at this and see a boring filter. But that middle line kept nagging at me. *“No records match”* is the application answering a **yes/no question about its own data**. Did a row exist, or didn’t it? That’s a **boolean oracle**, and a boolean oracle is a foothold. My working hypothesis became: if I can make that yes/no depend on a secret instead of a category, the app will leak that secret one bit at a time, whether it wants to or not.

I didn’t know how yet. But I knew what to listen for.

Before I could find the bug, I spent real effort proving what it *wasn’t*, because a wrong theory you never disprove will waste more time than the right one takes to find.

Template injection? I threw {{7\*7}}, \<%= 7\*7 %>, and ${7\*7} at it, and they all came back reflected verbatim and HTML-escaped. Reflection isn't evaluation. Dead.

NoSQL operators? I tried category\[$ne\]=x, and it got parsed into a JavaScript object, rendering as the telltale \[object Object\]. That quietly told me the backend was Node, which was worth filing away. But the operator itself never matched anything. Paused.

Prototype pollution, JWT forgery, I gave each a fair test, and each one failed to *prove execution*. That word, **prove**, is the discipline I kept coming back to. An accepted payload isn’t a working one. I kept demanding evidence that my input actually *ran*, and none of these gave it.

Classic SQL injection looked dead too, at first. I tried the textbook probes:

sales' AND '1'='1   → No records match

sales' AND '1'='2 → No records match

By the book, if injection worked, the '1'='1' version should have stayed true and found records. Both failing looked like the query was safely parameterized. It wasn't, and the payload that proved it is still my favourite request of the whole engagement:

sal'||'es   → Records found.

Sit with that for a second, because it took me a moment too. 'sal' concatenated with 'es' using ||, which is SQL's string-join operator, equals 'sales'. If the input were parameterized, the database would go looking for a category literally named sal'||'es, find nothing, and say so. Instead it said **Records found**. The only way that happens is if my quote broke out of the string and || got executed *as SQL*, stitching sales back together.

Injection was live. And the negative control sealed it: I sent sal'||'ex, which builds salex, and it returned "No records." So the oracle was honest, tracking the real query result rather than blindly agreeing with me.

So why had AND '1'='1' failed? Not safety. A **firewall**. Which was the next thing I needed to understand.

A WAF sits in front of the app and blocks requests matching certain patterns. When it blocked me, it returned a distinctive red *“Request blocked by WAF.”* page instead of the normal response, and that visible difference was a gift. It let me interrogate the thing directly. I fed it single tokens and watched which ones tripped it:

select   → blocked

SeLecT → blocked (so: case-insensitive)

union, from, where, and, or, || → all allowed

aselecta, 1select1 → allowed (embedded 'select' is fine)

(select → blocked

A picture formed. The WAF only truly cared about one word, select, and only when it stood alone as a token. Everything else I'd need was permitted. The entire challenge had quietly narrowed down to a single question: **how do you hand SQLite an intact select keyword that the firewall won't recognise as one?**

My first instinct was to split the word: sel/\*\*/ect, or a newline jammed in the middle. And these *do* fool the firewall's regex. The problem is they also fool the database. SQLite reads sel, then a comment, then ect, which is three separate tokens and a syntax error, not the keyword select. A bypass that breaks the word breaks it for *everyone*. That's the trap with keyword filters, and it's exactly why those attempts silently returned "No records."

Then it clicked. Keep the keyword whole, and wrap it *from the outside*:

/\*\*/select/\*\*/

SQLite treats /\*\*/ as ignorable whitespace and sees a clean, contiguous select. The firewall sees select fused to comment characters on both sides, so it's not a standalone token, exactly like the harmless aselecta from earlier. Both are satisfied, for opposite reasons. Here's the proof:

sal'||(/\*\*/select/\*\*/'')||'es   → Records found.

That request ran a real subquery. From this point on I had **arbitrary blind read**: any query I wanted, its answer delivered back through that two-sentence oracle.

Now I went straight for the prize: select admin\_api\_key from config. Null. I tried again. Null. Every single variation came back empty, and for a while I genuinely thought my bypass had broken somewhere. It hadn't. The bypass was fine. My *assumption* was the problem, and untangling that assumption is the most satisfying part of this whole box.

Here’s what I had been taking for granted. When the objective said config.admin\_api\_key, my brain read it the way you'd read it in most databases: a **table** called config, with a **column** called admin\_api\_key. So I kept writing select admin\_api\_key from config, asking for a column that, as it turned out, simply did not exist. The database wasn't hiding the value from me. It was honestly telling me *"there is nothing here by that name,"* and I kept mishearing it as *"access denied."* Those are very different messages, and confusing them cost me a dozen requests.

So I stopped guessing and did the thing I should have done sooner: I asked the database to describe *itself*. Every SQLite database carries a built-in catalogue table called sqlite\_master, and it holds the CREATE TABLE statement for every table in the schema. If I could read sqlite\_master through my oracle, the database would hand me its own blueprint. So I did, pulling it out character by character, and it gave up this:

CREATE TABLE events (id, category, visible)

CREATE TABLE config (id, name, value)

And the moment I saw that second line, the hint detonated in my head.

config was never a table with an admin\_api\_key column. Look at its shape: id, name, value. It's a **key-value store**. Instead of one column per setting, every setting is its own *row*, a name paired with a value. So the real database might literally contain a row that reads name = 'admin\_api\_key', value = '\<the secret>', sitting quietly among other config rows. The dotted notation config.admin\_api\_key was never SQL at all. It was a human way of saying *"the admin\_api\_key setting inside config,"* which in this schema translates to *the value of the row whose name is admin\_api\_key*.

*That* is what *“ask indirectly”* meant, and it’s such a clean piece of challenge design. A direct question, “give me the admin\_api\_key column," gets you nothing, because there is no such column. You have to ask *around* the secret instead of *at* it: request the generic value, and narrow down with a where clause on name.

select value from config where name='admin\_api\_key'

Same data the challenge promised. Completely different question. And suddenly the earlier hints read like a map I’d been holding upside down. The events table, with its visible flag, is what the report was actually built to filter and display. config was sitting right next to it in the same database, holding secrets the report was never designed to touch. *"The analytics report should never reveal it"* wasn't flavour text. It was a precise description of the boundary the developers intended, and my injection had simply reached across it. The report *could* answer more than it appeared to. I just had to ask the question it wasn't expecting.

I still only had *yes* and *no* to work with. The page never prints the value. So I turned each character of the secret into a question the oracle could answer, using this gadget:

sales'||(/\*\*/select/\*\*/case when (CONDITION) then '' else 'X' end)||'

The logic is neat once you see it. When CONDITION is true, the CASE returns an empty string, the visible category stays sales, and the page says *Records found*. When it's false, it appends an X, turning the value into salesX, which matches nothing, so the page says *No records match*. Any true/false test I could phrase in SQL suddenly became visible on the page.

Then I asked, position by position, “is this character’s code greater than *N*?”, halving the range each time until it converged on a single value. substr() picked out the character I wanted, unicode() turned it into a number, and a binary search pinned each one down in about seven requests:

sales'||(/\*\*/select/\*\*/case when (

unicode(substr((/\*\*/select/\*\*/value from config

where name='admin\_api\_key' limit 1),POS,1)) = CODE

) then '' else 'X' end)||'

Thirty-four characters later, every one of them reconstructed purely from the shape of *Records found* and *No records match*, the page had told me exactly what it was built to hide:

`FLAG{I01_c7b73fd425c256c810fcb47b}`
Nothing was ever printed. The flag was the pattern of the answers, decoded.

A boolean oracle in the filter, then SQL injection proven by string concatenation, then SQLite fingerprinted, then a select-blocking WAF slipped with comment-wrapped keywords, then the schema dumped to reveal a key-value config table, then the secret read as a *row* rather than a column, and finally exfiltrated bit by bit through a database that was made to answer questions it never knew it was answering.

The single real fix is **parameterized queries**. Bind category as a value and none of this exists, because a quote can never become code. Everything downstream of that was a second line of defence doing a first line's job. The WAF was a speed bump, not a wall, and keeping secrets in the same queryable database as report data meant one injection reached all of it. Keep secrets out of the app's reach and give the database only the access it actually needs, so that even a mistake can't read the config table.

Two things stuck with me from this box. First, a boolean oracle is far more powerful than it looks. It’s a complete read primitive wearing the costume of a filter, and slowness is its only real limit. Second, never accept that a bug is dead just because the *obvious* payload failed. AND '1'='1' collapsing looked like safety. sal'||'es succeeding revealed the truth. The difference between those two requests is the difference between walking away and walking out with the flag.

The Application Was Talking. I Just Had to Listen, which turned out to be two sentences long.
