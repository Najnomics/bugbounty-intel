# LFI Prevention

- **Source URL:** https://meetcyber.net/lfi-prevention-how-to-actually-fix-file-inclusion-vulnerabilities-9cda530d6c3f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13487 (id 13487)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# LFI Prevention: How to Actually Fix File Inclusion Vulnerabilities

## From input validation to server hardening — what developers should be doing to prevent LFI from the ground up. Part 7 of the File Inclusion series.

## LFI Prevention: How to Actually Fix File Inclusion Vulnerabilities

*Part 7 and the final part of the File Inclusion series. The previous parts were all about finding and exploiting these vulnerabilities. This one flips the perspective — if you’re a developer, or you’re doing a pentest and need to write recommendations, here’s what actually fixing this looks like.*

After spending six parts breaking file inclusion vulnerabilities in every way imaginable, it’s worth stepping back and asking — how do you actually stop this? The answer has a few layers, and none of them alone is enough. You need to think about it at the code level, the server level, and the infrastructure level.

## Layer 1 — Don’t Let User Input Near Include Functions

This is the root fix and honestly the only one that fully solves the problem. If user input never touches `include()`, `require()`, or any file reading function, there's nothing to exploit.

The ideal approach is to have the application load files based on internal logic only. Instead of doing this:

`include($_GET['language']);`
You do this:

```
$allowed = ['en' => 'english.php', 'es' => 'spanish.php'];
$lang = $_GET['language'];
include($allowed[$lang] ?? 'english.php');
```
The user passes `en` or `es`. The application maps that to an actual file internally. The user never controls what gets included — they just pick from a menu of options you defined. Even if they try to inject a path, it just won't match anything in your whitelist and falls back to the default.

This is the cleanest fix and should be the first recommendation in any pentest report about LFI.

## Layer 2 — Prevent Directory Traversal

If for some reason user input does need to influence file paths, at minimum you need to strip out traversal sequences. PHP has a built-in function for this:

`$filename = basename($_GET['file']);`
`basename()` strips everything except the actual filename. So `../../../../etc/passwd` becomes just `passwd` — which hopefully doesn't exist in your web directory.

If you want to go further, you can recursively strip `../` from the input:

```
while(substr_count($input, '../', 0)) {
    $input = str_replace('../', '', $input);
}
```
This is better than a single `str_replace` because it handles nested patterns like `....//` that survive a single pass — exactly the bypass we covered in part 1.

The caveat is that rolling your own sanitization is risky. You might miss edge cases. For example, bash wildcards like `?` and `*` can sometimes behave like `..` in shell commands. If your PHP code ever calls `system()` and the attacker controls the input, they might bypass your PHP-level sanitization through shell behavior. Using framework-native functions is always safer than writing your own.

## Layer 3 — Server Configuration

Even if the code has a flaw, the server can limit the damage significantly.

**Disable remote file inclusion** — if your app doesn’t need to include remote URLs, turn it off completely in `php.ini`:

```
allow_url_fopen = Off
allow_url_include = Off
```
This kills RFI entirely and also blocks the `data://` and `input://` wrapper attacks from part 2.

**Lock the app to its own directory** — add this to `php.ini`:

`open_basedir = /var/www`
Now even if an attacker finds an LFI, they can’t read `/etc/passwd` or any file outside the web root. The damage is contained.

**Disable dangerous functions** — if your app doesn’t need `system()`, `exec()`, or similar functions, disable them:

`disable_functions = system, exec, shell_exec, passthru`
if `system()` is gone the attacker can't get code execution through it.

**Run in Docker** — the modern standard. If the app runs in a container, even a full compromise is isolated. The attacker gets the container, not the host.

## Layer 4 — Web Application Firewall

A WAF like ModSecurity sits in front of your application and inspects every request. It can detect and block common LFI patterns — things like `../`, `%2e%2e`, `php://filter`, `data://` in parameter values.

The important thing about WAFs is they’re not a replacement for fixing the code. They’re a safety net. An attacker who understands encoding bypasses and custom payload crafting can often get around WAF rules — we demonstrated several of those techniques in part 1. But a WAF in permissive mode at minimum gives you visibility. It logs the attempts, alerts your security team, and buys time to respond.

The real value of a WAF isn’t making you unhackable — it’s making attacks noisier and more detectable.

None of these alone is enough. The whitelist fixes the vulnerability. Everything else reduces the damage if someone misses a whitelist somewhere. Defense in depth — multiple layers, each one catching what the previous missed.

*That’s the full File Inclusion series. From basic LFI on DVWA all the way to automated scanning and prevention. Hope it was useful.*
