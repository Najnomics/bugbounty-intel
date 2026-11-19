# How a simple Directory Listing leads to PII Data Leakage, Remote Code Execution and many more…

- **Source URL:** https://medium.com/@ar_hawk/how-a-simple-directory-listing-leads-to-pii-data-leakage-remote-code-execution-and-many-more-104b09e644f4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251118130248/https://medium.com/@ar_hawk/how-a-simple-directory-listing-leads-to-pii-data-leakage-remote-code-execution-and-many-more-104b09e644f4
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2598 (id 2598)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How a simple Directory Listing leads to PII Data Leakage, Remote Code Execution and many more vulnerabilities on a HR management subdomain

## TL;DR

While performing a pentest for a client, I found a subdomain with a **Directory listing** enabled on a endpoint leaking some images of its employees and nothing more. The subdomain on other endpoint leaking the PII data such as *professional email IDs, personal phone numbers,* etc. While visiting the subdomain, there is endpoint which allows me to change the information about the employee where I found multiple inputs which were misconfigured with **Stored Cross-site scripting** and one endpoint to upload an image that leads to **Remote Code Execution**.

*Let’s start with the complete exploitation of the misconfiguration.*

## Recon — Getting Started

- Let’s take the target domain as *redacted.com.*
- I started with basic subdomain enumeration using tools such as *Subfinder, Amass, Assetfinder and Alterx.*

```
$ subfinder -d redacted.com -o subfinder.txt
$ amass enum -d --passive redacted.com -o amass.txt
$ echo redacted.com | assetfinder --subs-only | tee assetfinder.txt
$ cat subfinder.txt amass.txt assetfinder.txt | sort -u | anew subdomains.txt
$ cat subdomains.txt | alterx | anew subd.txt
```
- After gathering all the subdomains, I saved them in a file say *subd.txt.*
- Now, its time to resolve the subdomains and check how many of them are alive or having status code 200. I used *httpx* and then saved the output in a file say *live.txt.*

`$ cat subd.txt | httpx -mc 200 | tee live.txt`
- From the above live subdomains, I again use the tool *httpx* to find out the title and tech stack of each of the subdomain.

`$ cat live.txt | httpx -td -title`
- While analysing the result of the above command, I found one interesting title “ **Index of /** ” of a subdomain say *hr.redacted.com.*

***Quick Tip:*** To find Directory listing with zero efforts, Gather all the subdomains using all the techniques and then run httpx with above flags \[-title -sc\] and see if you get some title as “ Index of / “ or “ Index of “, etc.


- Now, I have data to work on . I started *nuclei* on all the live subdomains at the backend and started manually looking the directory listing misconfiguration and the HR management subdomain.

## \[1\] Time to Hack — Working with the Directory Listing

- From the Directory Listing enabled on `/uploads`endpoint, I found only the images of the employees of the company. That sounds like a simple Directory Listing enabled because its not leaking anything sensitive or internal data.

- So, I started looking at the subdomain by removing the endpoint and found that subdomain’s endpoint `/teamlevel`is hosting the information of all its employees in a hierarchy format. I can view the details of any employee by just clicking on their name.

- I found that the subdomain itself leaking the PII data of its employees such as ***professional email IDs, personal phone numbers, first name, last name, their hobbies/interests***, etc.

- Now, I found something interesting that I can report but while looking at the subdomain, I got some instinct that something more is available on this subdomain. So, I started digging more into it.

## \[2\] Time to Hack — Working with the Subdomain

- I started fuzzing the subdomain and found an interesting endpoint `/hrms` which is asking for the employee’s email address to login/authorize. I already have the email IDs of each of the employees from the subdomain.

- I entered an email ID and without any password or OTP, I logged into their dashboard and was allowed to change the data available on it. So, the data present on the dashboard was the same data that was being displayed on the subdomain as the details of the employees.

- Now, I have the input boxes to play with and a file upload functionality as well.

## \[3\] Time to Hack — Working with the Input Boxes

- I started playing with input boxes and first thing I tried inputting a XSS payload `<img src=x onerror=prompt()>`in all of the four boxes and clicked on the submit button.

- Nothing, got reflected, I visited the subdomain again and clicked on the employees profile whose email ID I have used to login to the dashboard.
- ***BooooMMM*** I got alert boxes for all of the four payload I have entered. This got me *4 Stored XSS vulnerability due to improper access control and PII data leak*.

## \[4\] Time to Hack — Working with the File Upload Functionality

- Again, I logged into the dashboard and this time I uploaded an image with an extension `png` and intercepted my request using Burp-Suite.
- I sent the intercepted request to Repeater and changed the extension of the image to check what all extensions are allowed by the web application. I found majorly all the image extensions are allowed and there was no size limit as well.
- So, instead of uploading a image, I have tried to upload a php file and was successfully able to upload it.

- But the catch was I don’t know the path where it get stored. Because I can’t execute the commands without knowing the storage endpoint.
- I started checking the JS files, each Burp request to get anything, but It was no luck. Then suddenly I checked that directory listing that was present on the same subdomain and what I found the php file that I have uploaded was also there.

- I clicked on that php file, ***BooOOMMM*** I am now able to execute the system commands which means I found *Remote Code Execution via Improper File Upload Checking, Improper Access Control and Directory Listing*.

***Quick Tip:*** Always fuzz on the subdomains to find critical/sensitive information that leads to PII Data leak or unauthorised access.


## Conclusion

From the analysis, I can say that the above subdomain have the following misconfiguration and vulnerabilities:

1. Web Server Misconfiguration \[ ***Directory Listing Enabled*.** \]
2. PII Data Leak of the Employees.
3. Improper Access Control \[ ***No password required to access the Employee’s Dashboard.*** \]
4. Improper Input Validation and Improper File Upload Validation \[ ***XSS payload and PHP File Upload was allowed.*** \]
5. Stored Cross-Site Scripting and Remote Code Execution.

*Thanks for reading, hope you enjoyed and learned something from this blog.*

*If you have any questions, dm at https://twitter.com/AayushVishnoi10.*
