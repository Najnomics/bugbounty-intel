# How I escalated default credentials to Remote Code Execution

- **Source URL:** https://pawanchhabria.medium.com/how-i-escalated-default-credentials-to-remote-code-execution-1c34504be7a5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230329173044/https://pawanchhabria.medium.com/how-i-escalated-default-credentials-to-remote-code-execution-1c34504be7a5
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2141 (id 2141)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I escalated default credentials to Remote Code Execution

Hello All, We all know [Recon](https://www.bugcrowd.com/resources/levelup/doing-recon-like-a-boss/) is very important to get P1 bugs. [Shodan](https://www.shodan.io/) and [Censys](https://censys.io/) are probably the best search engines. I have been testing a lot of application logic issues so thought of learning some recon as well.

**Please note:** The domain and other details have been masked for Confidentiality Purpose.

Recently, I came across an application which was using [Tomcat](https://tomcat.apache.org/). Lets take the domain as [www.example.com](http://www.example.com). The first thing I did was brute forcing tomcat directories, but unfortunately, it did not work. I tried a couple of more things but it didn’t work, that’s where I decided to visit shodan.

I took the domain name and pasted it on Shodan. I filtered out the results on the basis of port. That’s where I noticed something strange. I saw some application running on port 8082 and it was using tomcat. The IP address was x.x.x.x (Just an example).

I tried accessing [http://x.x.x.x:8082/manager](http://x.x.x.x/manager) and guess what, it was prompting me to enter username and password. I got some hope there.

Boooommmm!!!!!, The username=**tomcat** and password=**s3cret** worked and the Tomcat Application Manager Console was accessible.

Technically, I should have stopped but I knew, I can get a remote code execution by uploading malicious war file. I needed a malicious .JSP file to make the war file. I took the JSP file from [here](https://github.com/tennc/webshell/blob/master/fuzzdb-webshell/jsp/cmd.jsp), saved it with name index.jsp on desktop. Then, I created the war file using the commands in the below screenshot.

Once the war file was generated, I navigated to “Select WAR file to upload” section and uploaded it.

After refreshing the page, I could see an application named “webshell” was added in the list of application.

I quickly opened it on a new tab. The webshell was successfully uploaded and I was able to run a few commands on it.

**Golden Tip:** Always think the other way round while hunting. Old vulnerabilities never die, we have to be creative enough to find them.

That’s it for this writeup.

Happy Testing!

Make sure you say a “Hi” to me if I could be of some help!

Twitter: [@heybenchmarkkk](https://twitter.com/heybenchmarkkk)

LinkedIn: [Pawan Chhabria](https://www.linkedin.com/in/pawanchhabria/)
