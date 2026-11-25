# Command Injection

- **Source URL:** https://medium.com/@raksharoot/command-injection-when-the-shell-runs-your-input-a99ba1b8bfb5
- **Fetched from:** https://medium.com/@raksharoot/command-injection-when-the-shell-runs-your-input-a99ba1b8bfb5?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14953)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Mon, 19 Oct 2026 16:55:32 GMT

From *;id* to JVM diagnostics, every way an OS command sneaks in.

Disclaimer: Educational content only. Only test systems you own or have written permission to test. Use legal labs and disposable VMs. Never test command injection on production systems without explicit authorization.

Command injection is the bug that ends the engagement.

Not because it’s clever. Because it’s total. The moment your input hits a shell, you’re not a pentester anymore, you’re the server. Read files, write files, pivot to the internal network, install a rootkit, exfiltrate the database. Game over.

And yet, it keeps showing up. In 2026. In modern apps. In Synology Photos, in PaperCut, in NetScaler, in Cisco Smart Software Manager.

So let’s talk about how it actually works, and why “we escape the input” is not the defense people think it is.

A command injection happens when user input ends up in a string that gets passed to a shell — *sh* , *bash* , *cmd.exe* , PowerShell, whatever.

The shell parses that string the same way it parses anything else. Semicolons separate commands. Pipes chain output. Backticks and *$()* run subshells. Ampersands fork. Newlines start a new line.

So if your input is *127.0.0.1* and the app runs *ping -c 1 127.0.0.1*, you type *127.0.0.1; id* and the shell runs both.

That’s it. That’s the whole bug.

The complexity comes from all the ways apps try to defend against this and fail.

Before you inject a command, you need to get out of whatever quote or context your input is in.

*If the app does:*

*exec(“ping -c 1 “ . $\_GET\[‘ip’\]);*

You’re unquoted. *; id* works.

*If it does:*

*exec(“ping -c 1 ‘“ . $\_GET\[‘ip’\] . “‘“);*

You’re single-quoted. You need to close the quote first: *‘ ; id ; ‘* .

*exec(‘ping -c 1 “‘ . $\_GET\[‘ip’\] . ‘“‘);*

You need *“ ; id ; “* .

Always look at the surrounding syntax. If you see *‘ or “* in the error message or response, you know the context you need to break.

These work on both Unix and Windows:

Unix only:

Two more that don’t execute but matter:

The newline ( *%0A* ) is my default. It works on both platforms, survives most naive filters, and doesn’t require closing any specific quote. If a filter blocks *;* and *|* and *&* , they usually forget *%0A* .

If you see any of these in a URL, request body, or JSON, you’re probably looking at a command execution sink:

Also look at anything that takes an IP, a hostname, a filename, a password, a domain, a URL. Those are the inputs that get passed to shell commands.

Some apps implement admin “rule engines” that execute PHP. If runkit is enabled, you can redefine functions at runtime.

If rules are stored and re-evaluated later, this becomes persistent RCE. Look for *runkit* or *runkit7* in *phpinfo()* or check *extension\_loaded(‘runkit’)* .

Here’s a subtle one from Infoblox *NetMRI*.

The *saml\_id* parameter only had to *start* with an integer. The rest of the string was passed to Ruby’s *IO.popen* without further validation.

Payload:

The *1* satisfies the numeric check. The *%26* (encoded *&* ) and *$(whoami)* execute.

***The lesson:*** validating the first character of a field is not validating the field. If a numeric-looking input reaches a shell, it’s a shell injection, not a numeric field.

This one is genuinely clever.

RewriteMap helpers written in bash sometimes push query params into globals and compare them in arithmetic contexts: *\[\[ $a -gt $b \]\] , $((…)) , let .*

Arithmetic expansion re-tokenizes the content. Variable names and array references get expanded twice.

The Ivanti EPMM pattern: *st* maps to *gStartTime*, *h* maps to *theValue* . Later:

Send *st=theValue* so *gStartTime* becomes the literal string *theValue*. Then *h=gPath\[‘sleep 5’\]* so *theValue* contains an array index.

During the arithmetic check, the shell evaluates *sleep 5*.

Probe (\~5 second delay, then a 404):

If you see the delay, you’ve got code execution, no shell metacharacters required. Just variable names in an arithmetic context.

If you’re auditing a JavaScript or TypeScript backend, you will see *child\_process*. The vulnerable pattern is always the same:

*exec()* spawns a shell. Backticks, *;* , *&&* , *|* , *$()* all get parsed as shell syntax.

The fix is boring:

*execFile()* doesn’t spawn a shell. Arguments go straight to *execve* as an array. No metacharacters get parsed.

**A real-world example:** Synology Photos ≤ 1.7.0–0794 was RCE through an unauthenticated WebSocket event that put attacker data into *id\_user*, which was later interpolated into *exec()*. Pwn2Own Ireland 2024.

Not all command injection is direct.

Sometimes the attacker’s request is just a log-poisoning step. The exploit fires later, when a privileged job parses that log and puts the extracted text into a shell command.

*The NetScaler example:*

2\. A Perl monitoring script runs *grep | tail | sed | awk* over the log and builds

3\. That value gets interpolated into a separate backtick find :

4\. The *;* ends *find .* The injected *id>/tmp/proof* runs. The trailing malformed command fails harmlessly.

The pipeline treated the metacharacters as data. The shell sink gave them meaning.

When testing, trace the full path from the unauthenticated log writer to the scheduled reader to the shell sink. An immediate HTTP 200 is not proof. Wait for the scheduled job. Check for the output file.

This is a class of bug that scanners miss entirely, because the exploit is not in the request. It’s in the infrastructure.

RFC 7468 allows explanatory text before a PEM BEGIN line. Some parsers accept it; some don’t.

Cisco Smart Software Manager had a chain where Ruby’s *OpenSSL::X509::Certificate.new* accepted a *$(…)* preamble in an intermediate certificate, and a Node.js configurator later ran:

Double quotes don’t prevent command substitution. The *$(…)* executes before OpenSSL sees the bundle.

***The constraint:*** only the intermediate cert retained the raw preamble. The leaf was reserialized with *to\_pem*, which stripped it. So the payload had to go in the intermediate.

***The lesson:*** parsing boundaries are where bugs live. The X.509 parser accepted a PEM object. The later shell command used the original raw text. Two parsers, two interpretations, one execution.

Not every injection requires shell metacharacters.

If an app passes untrusted strings as arguments to a system utility, even via *execve* or *execFile* , with no shell, programs still parse any argument starting with *-* or - - as an option.

*Common places:*

If the program supports - - (end-of-options), naive mitigations that prepend - - in the wrong place can be bypassed. Test - - placement carefully.

This is my favorite trick for turning an IPC bug into RCE.

Any primitive that lets you inject JVM command-line arguments — *\_JAVA\_OPTIONS* , launcher config files, *AdditionalJavaArguments* fields in desktop agents, can become reliable code execution without touching application bytecode.

Force a deterministic crash by shrinking metaspace:

*-XX:MaxMetaspaceSize=16m*

Attach an error hook:

The JVM parses these itself. No shell metacharacters required. The command runs with the same integrity level as the launcher.

Any desktop IPC bug that forwards user-supplied JVM flags, like a local WebSocket handler that doesn’t validate Origin, becomes OS command execution.

Sometimes the injection is in the **program name**, not the arguments.

PaperCut’s Scan to Fax job builds an executable path from *providerConnector : getAbsoluteBinaryPath(providerConnector)*

It accepts the path if *Files.isExecutable* succeeds, retries with *.exe* on Windows, then passes the path and a separate argument array to *ProcessUtils.execAndGetOutput*.

Neither the executable check nor the *.exe* fallback verifies the path stays inside the connector directory.

That resolves to *cmd.exe* outside the connector directory. Combine with *system.scan.fax.send.command-args* set to */c whoami* and the service runs *cmd.exe /c whoami*.

This is executable-selection injection, not shell injection. The arguments go through an array. Metacharacters don’t matter. The attacker-controlled program is the payload.

A separate PaperCut chain: */app?service=page/SetupCompleted* returns a valid *JSESSIONID* without credentials. From there:

4\. Click Apply. The code runs.

No print job needed. The payload executes during form submission because it’s placed outside the *printJobHook* function.

Horizon3’s *CVE-2023–27350.py* automates the whole chain.

You have command execution. Now you need the output.

Character by character, using shell conditionals:

Slow, but it works when there’s no other channel. Automate it.

If outbound DNS is allowed, use a service like dnsbin.zhack.ca or pingb.in.

Every subdomain query is a piece of data. Watch the DNS logs.

If outbound HTTP is allowed:

Fastest when it works, which is often.

Some filters are dumb. Some are less dumb. All of them can usually be defeated.

*Windows wildcards:*

? matches one character. \* matches any. \*\* searches recursively. Combining them lets you spell *notepad* without ever typing “notepad”.

*Linux:*

There’s a whole world of bypasses. Environment variables, *IFS* , wildcards, base64 encoding, *rev* , *xxd* , *${LS\_COLORS:10:1}* to get a space. The dedicated Linux restriction-bypass guide is worth reading.

**The golden rule:**

If a filter blocks *;* , *|* , *&* , and *$()* , try *%0A* (newline). If it blocks *%0A* , try tabs. If it blocks tabs, try IFS. If it blocks everything, try argument injection.

Not exhaustive, but this is the order I go in:

Command injection isn’t about shell metacharacters. It’s about trust boundaries that were never enforced.

The bug isn’t *;* . The bug is that user input reached a shell, and the shell did what shells do.

The defenses that actually work:

Everything else is theater.

***And when you’re hunting, remember:*** not every command injection is a *;* in a URL. It could be a JVM flag, a path in a config file, a log line, a PEM preamble, or the name of the executable itself.

The shell is wherever the OS reads a string and interprets it as an instruction.

***Test in legal labs.*** Never on production. And if you find one, report it fast, because command injection is RCE, and RCE is the end of the world.

That’s Part-9. Read the whole series in order: [Web Pentesting: A Complete Guide](https://medium.com/@raksharoot/list/web-pentesting-a-complete-guide-ad31d529002a)
