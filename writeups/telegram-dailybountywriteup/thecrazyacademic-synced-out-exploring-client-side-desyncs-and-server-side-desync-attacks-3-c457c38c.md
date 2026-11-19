# Synced Out

- **Source URL:** https://medium.com/@TheCrazyAcademic/synced-out-exploring-client-side-desyncs-and-server-side-desync-attacks-39911f1b4076?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230712072735/https://medium.com/@TheCrazyAcademic/synced-out-exploring-client-side-desyncs-and-server-side-desync-attacks-39911f1b4076
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3301 (id 3301)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
--

*Synced Out: Exploring Client Side Desyncs and Server Side Desync Attacks*

So some people probably heard about these in Albinowaxs last talk on HTTP Request Smuggling attacks but what he didn’t tell people is there applicable generally pretty much everywhere we even see them in video games. So anyways I’m gonna show some quick examples and explain what they are because I don’t want this post to be that long.

So basically a Client side desynchronization refers to situations where the client-side loses or has inconsistent network connectivity. This can occur due to factors such as a weak Wi-Fi signal, intermittent network disruptions, or device-specific issues. When the client loses connection or experiences delays in data transmission, it can result in transactional inconsistencies. For example, if a client sends a request to update data but fails to receive a response due to a dropped connection, the client’s local state may differ from the server’s state. This state could be an objects state and that can have a lot of security implications.

A Server desynchronization is basically the same thing but it’s the servers network connection that drops typically from power outages, overloads, random drops etc. If the server gets confused during a state transition again you get an inconsistent state.

So now that you know the basic definitions I’m gonna provide some examples.

Example 1. Item Duping in Animal Crossing via Client Side Desync Attack

https://www.youtube.com/watch?v=n4ermA\_2CFQ

It could be considered an exploit with security implications because video game virtual item economics typically involve real world money and people buy bells on eBay for newer animal crossings like new horizons. In this example I’m covering an old entry in the series which is animal crossing city folk.

The way it basically worked is you put items in your inventory you wanted to dupe, saved the game went to a friend’s town via Nintendo WFC, dropped the items in their town, leave to go back to your town but by timing it right and turning the Wii off on the right frame you would cause a client side desync which confused the game into thinking you never went to the friend town. This happened because progress is only saved between towns via the gate system and also locally in your own town which creates a integrity gap.

Whenever you save the game before you leave town the game saves the objects state as an array of items and the array of objects never gets nulled out until you go to the friend’s town drop items then leave back to your town which syncs up your client inventory data with the server that handles the town system. By desyncing before the sync up occurs you get to keep your items and the items you dropped stay causing a dupe.

Example 2. Item Duping in RuneScape via Server Side Desync Attack

https://www.youtube.com/watch?v=jvKdZ1c6AfI it’s around 8 minutes in when the Server Desync is discussed.

The way it basically worked is hackers would log into thousand of accounts and spam chat and skill functionality until the server crashed. To save on computational resources the server only stores inventory object states or the server save state during normal logout. When the server crashed it never does the save state hence all the accounts items were duped that were dropped on the ground back into their inventory. It’s as if they never dropped the item. Inconsistent object states in relation to items always lead to dupe bugs. When it comes to games like RuneScape which have a bigger virtual economy then animal crossing it creates financial implications.

Example 3. Auth Bypass in Multi Step Recovery Flow Web Apps via Client/Server Side Desyncs

While not a specific example both types of desyncs can lead to auth bypasses but usually server desyncs tend to lead it more frequently. For example if you complete step 1 which might be answering a security question and your wifi cuts out it might confuse the transactional state to get confused and skip remaining steps allowing any pass to be set for an account things like this have been found in the wild before.

Hope you enjoyed this surface quick level overview of what client and server desync attacks are and their security implications. There’s much more examples I’m sure I just couldn’t think of anything other then item dupes and auth bypasses.
