# PHP2Shell

- **Source URL:** https://medium.com/@rj_crypt/php2shell-dissecting-the-memory-overloads-behind-phps-critical-9-2-rce-vulnerabilities-cfcd5b1115ab
- **Fetched from:** https://medium.com/@rj_crypt/php2shell-dissecting-the-memory-overloads-behind-phps-critical-9-2-rce-vulnerabilities-cfcd5b1115ab?source=rss-1374b7e6d496------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14955)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Rahul Singh Choudhary / Wed, 21 Oct 2026 22:10:07 GMT

As security researchers and developers, we’ve often been told to trust core web frameworks and runtime environments. After all, they’ve survived decades in the wild. But on October 21, 2026, the global security landscape felt an abrupt jolt. Two critical remote code execution (RCE) vulnerabilities — collectively dubbed **PHP2Shell** (**CVE-2026–109618** and **CVE-2026–109619**) with a CVSS score of **9.2** — were publicly disclosed.

These flaws aren’t just highly dangerous; they are actively being exploited in the wild, bypass authentication, and allow remote attackers to compromise servers through PHP’s error-handling mechanisms. If you run almost any version of PHP (5.4 through 8.5) in its default configuration, your environment is likely vulnerable.

Let’s break down how this exploit works — first, in simple layman terms, followed by a deeper dive into the engineering flaw, concluding with how you can hunt, patch, and defend against this threat.

To understand why PHP2Shell is so devastating, forget about memory heaps and pointers for a minute. Imagine your PHP server is a busy restaurant kitchen.

Customers (web users) send in dinner orders (HTTP requests). Your kitchen staff (PHP-FPM worker processes) prepares those orders at dedicated prep stations. To prevent a single crazy order from bankrupting the restaurant or stalling the kitchen all night, the manager enforces a strict rule:

“If any single order uses up more than $100 worth of ingredients or counter space, hit the emergency stop buzzer, abandon the ticket immediately, and move on to the next customer.”

Usually, this rule saves the day. Now, an attacker walks in. They don’t want dinner; they want to hijack the kitchen.

In technical terms, PHP panicked because it ran out of memory, jumped out of the current execution flow to stay alive, and forgot to wipe the slate clean for the next request.

In cyber terms, this “kitchen chaos” translates directly into arbitrary code execution — the attacker commands the server (gets a shell) without ever having to log in.

Now, let’s peek under the hood of **Zend Engine**, the C-based core of PHP, and look at the actual vulnerability chain.

To prevent a runaway script from consuming all system resources, PHP enforces a per-request memory\_limit (e.g., 128M).

Historically, PHP utilizes standard C-level setjmp() and longjmp() functions for high-level "abnormal termination" (errors or Out of Memory events). Normally, if PHP hits the memory limit while processing raw multipart/form-data upload headers, session variables, or heavy serialization, it generates a fatal OOM (Out of Memory) error.

To escape this crisis without crashing the entire web-server process, PHP triggers a longjmp().

longjmp() is essentially an abrupt "teleportation" of the CPU's execution state back to an earlier checkpoint. It bypasses the standard stack unwinding and memory cleanup code that would normally happen during a graceful return.

When an OOM happens during multipart POST parsing or upload progress tracking (such as when session upload progress mechanisms or heavily parsed custom HTTP payloads are on the stack), variables, arrays, and objects are only partially initialized. Crucial internal pointers, which should point to active request objects, are left dangling in memory.

The attacker forces this OOM, causing PHP’s memory allocator (Zend MM) to skip cleaning the allocated request memory. The metadata for those objects continues to exist, while the system thinks the memory is freed—a classic **Use-After-Free (UAF) or memory-corruption condition**.

If the heap can be groomed or a subsequent request’s payload can be strategically loaded into the memory slots where those dangling pointers reside, the attacker can overlay a new payload onto the corrupt state.

By sending a secondary request back-to-back, the attacker fills the now ”abandoned” memory block with shellcode or function pointers (hijacking zend\_executor or zval types). Because the PHP environment is now operating in a compromised state, calling standard built-in functions can trigger pointer dereferences of the attacker’s data, handing over remote code execution.

During your assessment of your enterprise or target, there are a few primary methods to determine if systems are exposed.

Query your PHP configurations immediately.

Any release under the newly patched security versions (e.g., before critical security fixes deployed in Late October 2026, such as PHP 8.1.31, 8.2.25, 8.3.13, 8.4.1, etc.) is highly suspected of being vulnerable.

Check your web server logs (Apache error.log, Nginx error.log, or php-fpm.log). Look for abrupt crash dumps, Segfaults, or recurrent out-of-memory errors occurring within short intervals—often a footprint of exploit attempts or failed tuning:

Look for heavy requests targeting upload\_progress or utilizing high-volume multipart uploads (especially with thousands of file inputs or extremely long field names designed to blow out chunk memory parsing).

Because this flaw resides at the language runtime layer, fixing the application code won’t solve it. The primary line of defense is upgrading PHP.

Update your PHP installation directly from your distribution package manager or compile the latest security release.

**Ubuntu / Debian:**

**RHEL / AlmaLinux:**

Ensure that php-fpm, mod\_php, and CLI environments are restarted.

If legacy infrastructure prevents an immediate upgrade, you should heavily constrain inputs to mitigate the OOM triggers.

The “PHP2Shell” incident reminds us that even decades-old parsing handlers and core cleanup strategies (like longjmp) are susceptible to the demands of modern web inputs. Upgrade your PHP servers today to ensure you don’t let your digital "kitchen" get messy enough to give attackers a back door! Let me know if you run into any specific edge cases with FPM or older builds!

**Interested in a hands-on lab walkthrough?**

I wanted to keep this write-up accessible without drowning you in memory hex dumps and raw packet captures. However, if you’d like a **Part 2** where we spin up a vulnerable lab, trace the raw HTTP payloads in Burp Suite, and watch the dangling pointers corrupt the Zend Heap in real time, **drop a comment below or leave some claps!** If there’s enough interest, I’ll publish the full hands-on technical breakdown next.
