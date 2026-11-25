# Telegram Asked Us to Stay Silent About an XSS. We Published It Anyway.

- **Source URL:** https://medium.com/@expatch/telegram-asked-us-to-stay-silent-about-an-xss-we-published-it-anyway-7bee8d2027a1
- **Fetched from:** https://medium.com/@expatch/telegram-asked-us-to-stay-silent-about-an-xss-we-published-it-anyway-7bee8d2027a1?source=rss-febdd385b95a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14911)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** ExPatch Security / Tue, 15 Sep 2026 03:26:51 GMT

*Denis Rostilov & Aleksander Rostilov, ExPatch Vulnerability Research*

*We told the vendor first and stayed quiet until the fix shipped. Everything was tested on our own accounts. This is a post-fix disclosure.*

**We found a stored XSS in Telegram Desktop and reported it on June 3, 2026. On July 1, Telegram told us it could not approve public disclosure, citing risks even from disclosing already addressed issues. The first patched beta shipped on July 3, followed by a stable release on July 14. We waited for the fix to ship before publishing. We declined the bounty and asked for the money to go to charity. We also asked for a coordinated publication date. This is that publication. There is no exploit code here, and we attacked no live systems.**

Let me paint the scene.

9:47 a.m. A fintech company has to hand its engineering chat to compliance. It happens twice a year. The lead developer opens Telegram Desktop, clicks “Export chat history,” picks HTML, and opens the resulting file in Chrome.

The page loads: messages, timestamps, names, code snippets, the thread where someone pasted AWS keys “just for a second.”

He doesn’t see the script tag that has already fired inside a button. In the four hundred milliseconds it took the page to render, every message on it was packed into JSON and sent to a server in another country.

He sees a normal export. The attacker sees everything.

The message with the payload arrived seven months earlier. A new colleague forwarded it, thinking it was a link to the company blog. The bot behind it was never in the group. It didn’t need to be.

*This scene is a composite. The attack chain in it — forwarding, export, opening, and exfiltration — was demonstrated in our tests.*

Telegram Desktop can export a chat to an HTML file, and that file opens in a browser. We found that a bot could put invisible JavaScript inside an inline button — and that JavaScript would run the moment someone opened an export containing the button. No second click. No warning.

From the open page, the script could read every message, send them to an attacker’s server, and rewrite the page itself.

The bot never joins the chat. One forwarded message is enough.

Fixed in Beta v6.9.4 / Stable v7.0.1. No Telegram advisory, no CVE assigned. The full technical writeup: expatch.com/writeups/telegram-html-export-xss.html.

The export code lives in a file called export\_output\_html.cpp. Message text gets cleaned before it lands in the page: a helper called SerializeString() turns \<, >, &, ", ' into safe HTML entities, converts line breaks and Unicode separators to \<br>, and hex-encodes ASCII control characters. The same helper is used for sender names and other fields.

Button text didn’t get that treatment. Line 1752 simply wrote it into the page:

button.text.toUtf8()

So any HTML inside a button’s text field became live markup in the exported page — script tags included.

That line came from commit 52c779bf in early 2024 and shipped in stable v4.15.1 on March 8, 2024. It stayed in production for about two years and four months.

An XSS is when data on a page starts running as code. “Stored” means the malicious data is saved somewhere and fires later. Normally an attacker needs access to the target to plant it. Not here:

The attacker creates a bot. The bot sends one message: the text says “check out our new blog post,” the button’s text is thirty invisible U+3164 characters followed by a script tag, and the button's URL points to a real-looking blog.

In Telegram, the button looks empty or almost empty. It still works as a link, so nothing seems wrong.

Someone forwards that message into the target group. Telegram keeps the button, because it’s a URL button. The bot was never a member of the group. It has zero access to the group through the API.

*The forwarded message in the test group. The Forwarded from label and the message’s appearance are preserved; the chat content is not blurred.*

Seven months later, someone exports the chat.

The video below was recorded before the fix. It shows the whole chain: the page turns into a fake Telegram verification form while every message on it is quietly copied to the attacker’s server.

[https://www.youtube.com/watch?v=RXMavDmTXQk](https://www.youtube.com/watch?v=RXMavDmTXQk)

This is the part we find most interesting.

Telegram has a privacy mode for bots. By default, a bot in a group doesn’t get ordinary messages or history — only commands, replies, messages sent through the bot, and service messages. Admins see a label on the bot: “has no access to messages.” That’s why adding utility bots feels safe: weather, polls, reminders.

HTML export breaks that boundary. When you export a chat, Telegram writes the bot’s own messages into the file — including its buttons. So the bot’s script ends up on the page, and from there it can read every message shown in the document. The API never gave the bot that data. The export file did.

A weather bot with privacy mode on can’t read your messages. Until someone opens an export with its button in it — and then it can, from inside that person’s browser.

[https://www.youtube.com/watch?v=abfv3qM7FaI](https://www.youtube.com/watch?v=abfv3qM7FaI)

This is what CVSS calls Scope Changed: the flaw is in Telegram Desktop’s local export code, but the damage happens in the browser, in a different security context.

The script runs as soon as the file opens:

Our PoC also showed how the page can be replaced entirely — with a fake “Verification required” Telegram form. In the demo, the password fields were read-only and only a test email went to 127.0.0.1. That was our safety rail, not a limit of the technique; the same control over the page can be used for phishing.

There is a quieter problem, too. The script can edit what you see: change timestamps, sender names, message text; hide, reorder, or insert messages; change their surrounding context. The history on Telegram’s servers and the file on disk stay untouched. But if an exported chat is used as evidence in a review or a legal case, what’s on screen is no longer trustworthy.

Forwarding is what makes this scale. In groups where content protection is off, any member can carry the message along: a 10,000-member public group, an engineering chat of 2,400 people, a 200,000-member trading supergroup — every copy carries its own payload. Channels are different: posting there takes admin rights or an insider, so that’s a targeted vector, not free mass distribution. And every poisoned export page fires on its own; a page without the payload does nothing.

The payload stays until the message is deleted. People who join later can get it too, if the prior history is visible to them and the message is inside the range they export. (About the panel above: one record shows 14 messages from four senders. The counter on top includes a repeat collection of the same set — it doesn’t mean 28 unique messages or several victims.)

[https://www.youtube.com/watch?v=yeCiDChMtvs](https://www.youtube.com/watch?v=yeCiDChMtvs)

And unlike an attachment, you can’t scan this. It’s just text inside Telegram’s own database. You can block the script’s URL; you can’t scan the message itself. It only turns into code when an unrelated, legitimate action happens — exporting a chat. The gap can be months or years. The attacker plants it and waits.

The fix is one call, and it shipped in commit 8457d13a, "Fix escaping in HTML export of keyboards" (John Preston; authored June 30, committed July 2, 2026):

\- block.append(button.text.toUtf8());

+ block.append(SerializeString(button.text.toUtf8()));

- ? ("return ShowTextCopied('" + content + "');").toUtf8()

+ ? ("return ShowTextCopied('"

+ + QString(content)

+ .replace('\\', u"\\\\"\_q)

+ .replace('\'', u"\\'"\_q)

+ + "');").toUtf8()

The same commit also closes a bonus vector: a JavaScript injection into the onclick="return ShowTextCopied('…')" attribute of copy-callback buttons. Now content escapes backslashes and single quotes before it becomes part of a JS string.

Why did nobody notice for two years? Because Telegram’s own apps don’t run a browser. They show button text as plain characters — the script tag is just text there, and with the invisible filler the button looked empty anyway. The export code is where text becomes HTML, and it trusted that text. The app looked fine. The file didn't.

How serious is it? CVSS 3.1 gives it **8.2 (High)**: CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N. We deliberately chose Attack Vector Local, not Network: the vulnerable part is the local export code, and the network path that delivers the payload handles data correctly. Changing that one metric would give 9.3, but we'd rather have a score we can defend. The impact doesn't change: sensitive content leaves the opened document, and the record can be rewritten.

**If you use Telegram Desktop:** update. The first release with the fix is Beta **v6.9.4** (July 3, 2026), then stable **v7.0.1** (July 14, 2026). The update does not rewrite old files. If you exported chats to HTML before that, re-export them after updating — or open old exports with JavaScript disabled. Treat any export made before the fix as untrusted active content.

A Telegram security representative also joined our demonstration group as TS Sec. They wrote that they had tried the export feature in another group and asked whether we had received anything. We discussed the demonstration directly in the chat, before the later exchange about publication.

Here is the key part of their reply:

*“We also have considered the possibility of a public disclosure but we cannot approve it as disclosing even the already addressed issues could put more Telegram users at risk in the future. For instance, if information about a vulnerability is made public, malicious actors may attempt to exploit it thereby causing financial harm to Telegram users.”*

Their public bounty policy says something narrower: reports disclosed to the public before they are fixed are not eligible for a bounty. “Vulnerabilities that are disclosed to the public or to third parties before they are addressed are not eligible for our bug bounty program.” Nothing there says that publishing after a fix needs Telegram’s approval. We didn’t sign an NDA.

Read their answer again: “even the already addressed issues.” This wasn’t “please wait for the release.” The fix was already written the day before. It was a refusal to approve publication after the fix.

Three reasons.

**People.** Old export files are still dangerous, and a silent patch never tells anyone to re-export or to open old files carefully. An advisory is how users find out.

**Unpatched clients.** The fix only helps people who update, and it doesn’t rewrite files that are already on disk.

**The norm.** Advisories and CVE records let defenders check whether they’re affected, help incident responders know what to look for, and make outside review possible. The fix commit is public; the explanation around it is not.

For comparison: Signal keeps a public page of security acknowledgments with reported issues and researcher names. Chrome publishes release notes with CVE numbers and researcher credit. Apple adds CVE numbers when it can. There is still no Telegram advisory and no public CVE record for this issue — while the fix commit sits in a public repository for anyone to read without context.

Security isn’t the absence of bugs. Everyone has bugs. It’s what the vendor does next: publish an advisory, assign a CVE, let researchers publish. When a company that markets security says no to documenting a bug it has already fixed, it’s fair to ask: is this protecting users, or the brand?

We reported the bug through Telegram’s official bug bounty program at security@telegram.org. Everything was tested on our own accounts and our own test groups. The PoC kept its network traffic on 127.0.0.1 — apart from standard Bot API calls, we didn't touch Telegram's production. We declined the $500 bounty and asked for it to go to charity. We published after the fix shipped and after we verified it in released builds. There is no working exploit against live systems in this post.

The screenshots come from three separate controlled demonstrations, not one continuous run. All accounts and groups were ours. The bug is fixed.

Full technical writeup, with the CVSS rationale and the complete disclosure timeline: [https://expatch.com/writeups/telegram-html-export-xss.html](https://expatch.com/writeups/telegram-html-export-xss.html)

*Denis Rostilov & Aleksander Rostilov, ExPatch Vulnerability Research*

*security@expatch.llc · expatch.com*
