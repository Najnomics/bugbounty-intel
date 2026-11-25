# How I hacked into police and ivoted attack to RCE

- **Source URL:** https://medium.com/@Cybervenom/how-i-hacked-into-police-and-ivoted-attack-to-rce-83e5c7e5dfd6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221229073429/https://medium.com/@Cybervenom/how-i-hacked-into-police-and-ivoted-attack-to-rce-83e5c7e5dfd6?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1165 (id 1165)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I hacked into Police and Pivoted attack to RCE

Let’s breach in guys,So there was Section for the appreciation letters on site which has public appreciation letters of police.wich has following fields “Subject”,“Date From” and “Date To”.

I selected date range and entered random words in subject and intercepted request in burp suite.Sent request to repeater as i was interested in parameters related to dates functions.

I started charging parameters with different payloads to break query strings it showed minor difference in content-length.My hope raised more but it was not clear if it’s vulnerable.So here i decided to make sleep database and confirm the sql injection.

I chose the subject parameter and entered sleep payload for db to sleep 20 seconds and it delayed response to verify increased delay to 50 seconds and boom it delayed nearly minute.I performed same test with date parameters and they were also vulnerable to sql injection.Site was vulnerable to “time based blind” sql injection.It’s Time to raid boys.

So i copied request and created text file with parameters marked and loaded into sqlmap.But as i said it was time-based blind sql injection it was taking too long to retrieve data.Till now i was able to retrieve some data which may be enough to report issue but i was not satisfied.

As it was “Microsoft SQL Server”. I thought other way round then retrieving more data.I checked if current user is dba and to my surprise it was true.So now it was not just a sql injection.

It was time to pivot attack to RCE.

I used “ — os-shell” command to open interactive shell.Then i tried basic command like“whoami” for poc.And boom it responded with username.I can execute commands on Police server.

This is how i hacked into police.I Pivoted sql injection to RCE and executed commands on police servers.I was waiting so long for this to be patched.So i can publish this write up and that’s why it took so long for other write up.

Thank You fellas peace out.
