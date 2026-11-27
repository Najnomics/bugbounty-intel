# Utilizing Log Poisoning

- **Source URL:** https://medium.com/@YNS21/utilizing-log-poisoning-elevating-from-lfi-to-rce-5dca90d0a2ac?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@YNS21
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5542)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*What is Log Poisining?*

Log Poisoning is a technique used in cybersecurity to exploit vulnerabilities within web applications, particularly in the context of escalating privileges from Local File Inclusion (LFI) to Remote Code Execution (RCE). By manipulating log files, attackers can inject malicious code or commands, enabling them to gain unauthorized access, execute arbitrary commands, or take control of the target system. This introduction serves as a primer for understanding the potential risks associated with log poisoning and the importance of implementing robust security measures to mitigate such threats.

Explore the nuances of cybersecurity techniques, with a particular emphasis on File Inclusion vulnerabilities, in an immersive setting provided by the Hack The Box lab. This educational opportunity offers aspiring cyber security students a hands-on platform to deepen their understanding of LFI (Local File Inclusion) and its broader implications, all at no cost.

1-*Before delving deeper, let’s first define our vulnerability by thoroughly exploring the web application interface.*

?page="value"

→ Notice how the parameter changes each time we click HOME, ABOUT US, INDUSTRIES, or CONTACT buttons.

We’ve identified an LFI vulnerability in our web application. Our next step is to fuzz the parameter for any exploitable information. We can utilize a word list for this purpose : [Auto\_Wordlists/wordlists/file\_inclusion\_linux.txt at main · carlospolop/Auto\_Wordlists · GitHub](https://github.com/carlospolop/Auto_Wordlists/blob/main/wordlists/file_inclusion_linux.txt)

**But nothing intresting !!**

*2- Upon discovering that our application employs PHP, we can leverage cURL to utilize PHP wrappers for potential exploitation.*

Following the utilization of a PHP wrapper, we ascertain that the application filters the source code but allows base64-encoded formats.

*→ Here are some useful PHP wrappers that can be utilized in exploiting the identified vulnerability:*

http://example.com/index.php?page=php://filter/read=string.rot13/resource=index.php

http://example.com/index.php?page=php://filter/convert.iconv.utf-8.utf-16/resource=index.php

http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php

http://example.com/index.php?page=pHp://FilTer/convert.base64-encode/resource=index.php

*3- Let’s read the source code of the index page using the PHP wrapper and check for any useful information that could aid in further exploitation:*

*Result:*

Let’s decode this encoded format from base64 and examine its contents for potential insights:

echo "base64 text format" | base64 -d > index.php

*We decode this encoded format and add it to a file index.php*

*After we examine the source code of index.php we found an admin page:*

Upon accessing the page and clicking on the Service Log, we’re presented with a parameter named “log”. This provides us with an opportunity to attempt LFI payloads once again. Given that we’re aware of the Nginx web server configuration, let’s attempt to access the log files for potential poisoning exploits.

http://94.237.56.188:50883/ilf\_admin/index.php?log=../../../../../../../../var/log/nginx/access.log

Let’s initiate Burp Suite and attempt to poison the user agent with a PHP system code to execute commands on the server.

After successfully injecting the PHP system code into the user agent, we proceed by removing the user agent from the HTTP headers. Following this, we append the “cmd” parameter with our desired command for execution on the server.

*After the injection of user agent:*

*Let’s execute our command and observe the results to ascertain the success of our injection attempt.*

As evident, we have achieved Remote Code Execution successfully. Now, we can proceed to retrieve the flag by executing the “cat” command.

In summary, we’ve demonstrated how to identify and exploit vulnerabilities leading to Remote Code Execution. Your engagement has been invaluable. For more insights, follow me on Medium. Thank you for joining!
