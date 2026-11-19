# How I found +100 Reflected Cross Site Scripting & SQL Injection on an Private Hackerone Bug bounty…

- **Source URL:** https://medium.com/@jooelsaka/how-i-found-100-reflected-cross-site-scripting-sql-injection-on-an-private-hackerone-bug-bounty-26eef05c9b63?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260622042821/https://medium.com/@jooelsaka/how-i-found-100-reflected-cross-site-scripting-sql-injection-on-an-private-hackerone-bug-bounty-26eef05c9b63
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2557 (id 2557)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found +100 Reflected Cross Site Scripting & SQL Injection on an Private Hackerone Bug bounty Program

## Hi Readers hope you all are doing great In this article I’m going to talk about one of my findings in an private bug bounty program

### As an 18-year-old engineering student with a passion for technology, I have found a unique way to apply my skills by working as a bug hunter freelancer. Through my freelance work, I have gained valuable experience in identifying and reporting software bugs, while also earning some extra income. I am excited to continue exploring this field and honing my skills as I pursue my education in engineering.

Tools that I used :-


- Subfinder: [https://github.com/projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder)
- Assetfinder: [https://github.com/tomnomnom/assetfinder](https://github.com/tomnomnom/assetfinder)
- Httpx: [https://github.com/projectdiscovery/httpx](https://github.com/projectdiscovery/httpx)
- Paramspider: [https://github.com/devanshbatham/ParamSpider](https://github.com/devanshbatham/ParamSpider)
- Kxss or GF: [https://github.com/Emoe/kxss](https://github.com/Emoe/kxss) // [https://github.com/tomnomnom/gf](https://github.com/tomnomnom/gf)

The idea came into my mind when i first saw ParamSpider tool and it Grapping all the parameters for a domain

I have worked on an wide scope program ( +2000 Subdomains ) and as we all know that Paramspider is only crawling for an single subdomain so we got a problem here that it’s impossible to run Paramspider on every single subdomain that will take a lot of efforts and time so Bash scripting just came into my mind !!! I asked ChatGPT for an bash script to crawl all the subdomains but it didn’t work properly in that way so I had to write it by myself and I wrote an simple one

\*\*bash script :-

```
for URL in $(</root/recon/target/httpx); do (python3 paramspider.py -d "${URL}");
done;
```
Steps :-

1. collecting all the domains that on scope
2. running Subfinder using the following command

`subfinder -dL domains.txt -o subfider-subdomains.txt`
3\. running assetfinder using the following command

`cat domain_list.txt | assetfinder --subs-only > assetfinder-subdomains.txt`
4\. combine the following subdomains in one list and remove duplicates

`cat subfinder-subdomains.txt assetfinder-subdomains.txt > subdomains.txt``sort -u subdomains.txt > sort.txt`
5\. we need to use Httpx to quickly and efficiently identify URLs that return a status code of 200 for a given domain list.

`cat sort.txt | httpx -mc 200 > 200_urls.txt`
6\. Running Paramspider for crawling all the Parameters,URLS

```
for URL in $(</root/recon/target/200_urls.txt); do (python3 paramspider.py -d "${URL}");
done
```
7\. after getting all the output we need to combine them into one file again and remove duplicates if found using the same previous commands

8\. running KXSS for identifying the filtered , unfiltered Sympols note that Kxss scan could take several minutes or longer. Be patient and wait for the scan to complete

`cat filtered_urls.txt | kxss`
then we will move to the last part we need to get unfiltered \<> URLs like the following result to be able to inject/execute javascript commands

It has come to our attention that the current parameter filtering process does not include the {\<>} symbols. As a result, this creates a vulnerability in which an attacker may be able to execute JavaScript commands either manually or using tools such as Dalfox.

here is it’s the end of our story However, it is important to remember that security is an ongoing process and requires **constant vigilance**. As new threats emerge and technology evolves, it is essential to stay up to date with the latest security best practices and continually assess and improve the security of the system.

If you require any further assistance or have any questions, please do not hesitate to reach out to me via Twitter or Instagram. I am always available to provide support and address any concerns you may have. Thank you for your time and consideration.

[***Instagram***](http://instagram.com/dnelsaka): @dnelsaka

[Twitter](http://twitter.com/joo_elsaka) : @@joo\_elsaka
