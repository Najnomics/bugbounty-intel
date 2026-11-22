# How I Found My First RCE !

- **Source URL:** https://mchklt.medium.com/how-i-found-my-first-rce-f80073626fff?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251108013043/https://mchklt.medium.com/how-i-found-my-first-rce-f80073626fff
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6115 (id 6115)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found My First RCE

**.السلام عليكم ورحمه الله وبركاته والصلاه والسلام على رسول الله سيدنا محمد**

As-salamu alaykum everyone! In this article, I’ll talk about my first RCE experience. It happened with a [CVE-2023–46604](https://nvd.nist.gov/vuln/detail/CVE-2023-46604) in Apache ActiveMQ. I’ll focus more on how I found it rather than bringing new stuff to the table for expert bug hunters.

In my recon process, i made sure to update my list of subdomains every week and scan for open ports every three days (though, it’s better to do it every day). For subdomains enumeration, I used tools like [Subfinder](https://github.com/projectdiscovery/subfinder) and [Amass](https://github.com/owasp-amass/amass).

```
subfinder -dL domains.txt -o subdomains.txt
#then subdomains of subdomains 
subfinder -dL subdomains.txt -o more-subdomains.txt
#using amass
amass enum -passive -norecursive -noalts -df domains.txt -o subs.txt
#then subdomains of subdomains
amass enum -passive -norecursive -noalts -df subs.txt -o more-subs.txt
```
Then:

`cat more-subdomains.txt subdomains.txt subs.txt more-subs.txt | sort -u > targets.txt`
after that i start port scanning in some cases i got a lot of subdomains somtimes +5k, I made a simple script to check subdomains using [DNSx](https://github.com/projectdiscovery/dnsx) and divided them into groups of 15. Then, I ran [Naabu](https://github.com/projectdiscovery/naabu) with nohup to keep it running in the background.

script that i use

```
#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi
cat $1 | dnsx -o $1_ok.txt
split -l 15 $1_ok.txt 15_file_
for file in 15_file_*; do
    nohup naabu -list "$file" -p - -o "${file}.out"&
done
```
then

`cat 15*out | sort -u > ports.out` Many times, I manually checked that list. I filtered out hosts that might be honeypots, and sometimes Naabu gave unreliable results.

btw, after that, I manually checked for hosts with open ports between 3 and 10. When I noticed a strange open port, I used Nmap to find out which services were running on it.

In this instance, there was a host named bamboo.target.com, and I noticed that it had an open port, 54663.

When I used Nmap with the -sSCV flag, I discovered that it was running Apache ActiveMQ, which was present in its latest versions [CVE-2023–46604](https://github.com/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ) .

Then, I simply applied the exploit, and it worked right away. I reported it in a detailed report, which turned out to be a smart move. Providing all the necessary information for the triager and the security team often leads to a good bonus for your efforts.

as well as for that result

That’s all, folks! Thanks for your time. Feel free to check out my [LinkedIn](https://www.linkedin.com/in/mchklt/) or [Twitter](https://twitter.com/mchklt) — I’m looking for homies there!
