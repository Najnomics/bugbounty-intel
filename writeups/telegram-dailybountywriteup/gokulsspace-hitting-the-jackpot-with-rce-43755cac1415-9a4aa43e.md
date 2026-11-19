# Hitting the jackpot with RCE!

- **Source URL:** https://medium.com/@gokulsspace/hitting-the-jackpot-with-rce-43755cac1415?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241117082514/https://medium.com/@gokulsspace/hitting-the-jackpot-with-rce-43755cac1415
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7078 (id 7078)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hitting the jackpot with RCE!

Hey, so everyone was pushing me to write another write-up after the acceptance of my first ever bug bounty write up. So if you haven’t already read it please have a look at it here: [https://medium.com/@gokulsspace/the-30000-bounty-affair-3f025ee6b834](/@gokulsspace/the-30000-bounty-affair-3f025ee6b834)

I am a very lazy person and writing such reports and write-ups are very hectic to me. So excuse my time gap for writing them.

So here I am with another RCE story, my second RCE in the year 2023. So, as I was digging up some hosts of a company, let’s call it redacted.com as always, I came across few interesting subdomains. Whatever we are doing here, the major part of it is recon and be a legend in finding those hidden assets of a company. I don’t care about what tools you use. Subfinder, Amass, knockpy, securitytrails whatever. But, make sure that you have found that one treasury of bugs. It may be a single subdomain or multiple subdomains or may be an IP which isn’t that interesting for you.

So, when we do the subdomain enumeration we will come across a huge list of them especially when it is giant of a company. The most interesting subdomains or IPs you come across includes default pages of Ngnix, Apache, Redhat whatever. So be on the lookout of such pages especially Ngnix.

When I come across one such page, I decided to FUZZ it with my wordlist to enumerate if there is any hidden paths or files are available. Interestingly, I wasn’t wrong and found a path called test. More like [http://redacted.com/test/](http://redacted.com/test/)

It was a messy endpoint and developer did some nasty works inside it for testing purpose. So there was few options to upload files also.

You may have come across on such instances but uploading a file other than the image or doc file might be hectic and you try to bypass the upload restrictions with various ideas and will end up failing to do so. But here it was simple because it was a developer’s playground. He hangs out there on his free time and no restrictions to upload any kind of files.

Yeah, you guessed it write. PHP files for the rescue!!! I tried uploading a random php file called ***test.php*** on this endpoint and succeeded. Later, I checked where this file is gonna stored. So again Fuzzed the endpoint [http://redacted.com/test/](http://redacted.com/test/) and found an index of uploaded files on this path: [http://redacted.com/test/plain/uploads](http://redacted.com/test/plain/uploads) . There I saw my boy test.php.

Now, I got excited and wasted no time to finish this dirty job. I created another php file called ***rce.php*** with one of the dangerous payload that is available **\<?php system($\_GET\[“cmd”\]);?>**

The code snippet `<?php system($_GET["cmd"]);?>` is a simple PHP script that can be very dangerous if deployed on a live web server. It takes a command from the URL (via the `cmd` GET parameter) and executes it on the server.

So, I uploaded it and went to [http://redacted.com/test/plain/uploads](http://redacted.com/test/plain/uploads) to see the file *rce.php.* Now, the job is almost done. I Just executed those magical commands to verify the RCE by adding cmd parameter. Like this:

[http://redacted.com/test/plain/uploads/rce.php?cmd=whoami](http://redacted.com/test/plain/uploads/rce.php?cmd=whoami)

[http://redacted.com/test/plain/uploads/rce.php?cmd=ls%20-la](http://redacted.com/test/plain/uploads/rce.php?cmd=ls+-la)

So that’s it. The target was not a main scope of the program. So they adjusted the bounty to be a little low.

Hope you guys learned something from this and if you liked it please share it on your social medias and give me a follow here. Thank you!

My linkedin: [https://www.linkedin.com/in/gokul-sudhakar-72a93923a/](https://www.linkedin.com/in/gokul-sudhakar-72a93923a/)
