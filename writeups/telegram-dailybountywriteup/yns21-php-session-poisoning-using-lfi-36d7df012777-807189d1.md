# PHP Session Poisoning using LFI.

- **Source URL:** https://medium.com/@YNS21/php-session-poisoning-using-lfi-36d7df012777?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250330083932/https://medium.com/@YNS21/php-session-poisoning-using-lfi-36d7df012777
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5461 (id 5461)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# PHP Session Poisoning using LFI.

# PHP Session Poisoning:

*1- introduction:*

PHP session poisoning is a type of security vulnerability that occurs when an attacker manipulates or exploits the session management mechanisms in PHP applications to gain unauthorized access or perform malicious actions. Sessions are used in web applications to maintain user-specific information across multiple requests or pages, such as login credentials or user preferences.

**2-*Retrive the session cookie:***

The first thing we need to do in a PHP Session Poisoning attack is to examine our PHPSESSID session file and see if it contains any data we can control and poison. So, let’s first check if we have a `PHPSESSID` cookie set to our session:

*→ CURL:*

→ DevTool: (Ctrl + Shift + c)

As we can see our cookie session is : j3ocuu7vju30kona78drbdpjsr and should be stored with a prefix of **sess\_**.the final file should be like this **sess\_j3ocuu7vju30kona78drbdpjsr.**


**3*-Conduct the attack:***

Typically, on Linux servers, these session files are housed within the directory path: **/var/lib/php/sessions/**. Conversely, on Windows systems, they tend to reside in ***C:\Windows\Temp***. In this specific scenario, we can ascertain the hosting environment of the PHP web application, deducing it to be a Linux server. This inference is drawn from the server’s response, which can be obtained through the use of tools such as curl or other utilities capable of system enumeration.

In the case the web application is vulnerable to LFI attack and we can read the data from our path: **/var/lib/php/sessions/** with the help of our ***language function***:

Let’s found if our session cookie file is present on the path:

→We fired up BurpSuite:

Let’s try setting the value of `page` a custom value (e.g. `language parameter`) and see if it changes in the session file. We can do so by simply visiting the page with `?language=hello_world` specified, as follows

Now we will search the path with our php session cookie:

This time, the response contains our previous text `hello_world`, so let’s try to run a **php webshell.** with the encoded format: *\<?php system($\_GET\[‘cmd’\]); ?>:*

Finally, we can include the session file and use the `&cmd=id` to execute a commands:

Note: To execute another command, the session file has to be poisoned with the web shell again, as it gets overwritten with `/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd` after our last inclusion. Ideally, we would use the poisoned web shell to write a permanent web shell to the web directory, or send a reverse shell for easier interaction.
