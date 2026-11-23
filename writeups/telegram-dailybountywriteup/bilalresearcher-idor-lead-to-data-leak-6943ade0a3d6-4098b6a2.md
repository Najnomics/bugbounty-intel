# IDOR Lead to Data Leak

- **Source URL:** https://medium.com/@bilalresearcher/idor-lead-to-data-leak-6943ade0a3d6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240829062506/https://medium.com/@bilalresearcher/idor-lead-to-data-leak-6943ade0a3d6
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7070 (id 7070)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR Lead to Data Leak

Hello, hackers. My name is Bilal. Today, I’ll be discussing a bug I recently discovered with my friend while hunting a few days ago.

First, we began by analyzing and understanding the functionality of the application. We discovered that it is an online gaming platform.

While starting the testing process, I visited the /profile page and then searched through the Burp History for any hidden requests.

We came across a request using the HTTP method OPTIONS.

The request contains two parameters: `player_id_or_name`, which accepts either the user's ID or their name, and `event`, which specifies the game name.

By sending the request to Repeater and changing the request method from `OPTIONS` to `GET`, I was able to retrieve a list of all the games the user has played.

I discovered that by changing the username from my own to another user’s, I was able to retrieve their data as well.

Data we found was :

- player id(private)
- match time
- result(win or lose)
- his handle at his game
- game name

The program accepts this as a P3 issue.

*Find me on Twitter: @bilalresearcher*
