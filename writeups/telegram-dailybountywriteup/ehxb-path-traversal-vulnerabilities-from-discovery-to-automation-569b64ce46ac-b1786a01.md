# Ehxb | Path Traversal Vulnerabilities

- **Source URL:** https://ehxb.medium.com/ehxb-path-traversal-vulnerabilities-from-discovery-to-automation-569b64ce46ac?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251012175235/https://ehxb.medium.com/ehxb-path-traversal-vulnerabilities-from-discovery-to-automation-569b64ce46ac
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11216 (id 11216)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Ehxb | Path Traversal Vulnerabilities

When I first started learning about web security, **path traversal** was one of those vulnerabilities that seemed almost too simple to be real. How could something as basic as manipulating a filename cause such serious damage? But after spending hours in the lab and testing real applications, I realized that simplicity is often what makes it so dangerous. Developers overlook it, filters fail to catch it, and before you know it, an attacker is reading your server’s most sensitive files.

In this post, I’ll walk you through what path traversal is, where to find it, how to test it with five different bypass techniques, and finally, how to automate your testing using Python. Let’s dive in.

### What is Path Traversal?

Path traversal, also known as directory traversal, is a vulnerability that allows attackers to access files and directories stored outside the web root folder. By manipulating file path references, an attacker can navigate through the server’s directory structure and read arbitrary files.

The most common target? The **/etc/passwd** file on **Linux** systems. It’s a standard file that contains user account information, and it’s the perfect proof of concept because it’s readable by any user and confirms you’ve successfully traversed the directory structure.

The impact can range from information disclosure (**source code**, **configuration files**, **credentials**) to complete server compromise if the attacker can write files or access sensitive application logic.

### Where Do We Find Path Traversal?

**Path traversal** vulnerabilities typically appear in features that handle file operations. Here are the most common places to look:

**Image loaders**: Applications that display images based on a filename parameter (like product images, avatars, or gallery viewers).

**File download features**: Any endpoint that lets users download files by specifying a filename or path.

**Document viewers**: PDF viewers, report generators, or any feature that loads documents dynamically.

**Template engines**: Systems that load templates based on user input.

**File upload handlers**: Sometimes the filename itself can be manipulated during upload.

**Include/require statements**: Especially in older PHP applications where user input is passed to include() or require().


The key is to look for any parameter that seems to reference a file: filename, file, path, template, page, document, or even custom parameter names like img, doc, or resource.

## Testing Path Traversal: 5 Real-World Scenarios

Now let’s get practical. I’m going to show you five different scenarios I encountered while practicing in **PortSwigger’s** Web Security Academy labs. Each one represents a different defense mechanism and how to bypass it.

### Scenario 1: The Simple Case

The first scenario is the most straightforward. The application takes a filename parameter and directly uses it to load an image. No filters, no validation, just pure trust in user input.

The vulnerable request looks like this:

`GET /image?filename=product.jpg`
To exploit it, I simply replaced the filename with a path traversal sequence:

`GET /image?filename=../../../etc/passwd`
The ../ tells the server to go up one directory. By chaining three of them together, I navigated from the images directory, through the web root, and into the system’s /etc directory.

How I found it: I intercepted the image request in Burp Suite, noticed the filename parameter, and immediately tested it with the classic traversal payload. The response came back with the full contents of /etc/passwd. No resistance at all.

### Scenario 2: Absolute Path Bypass

The second scenario was trickier. The application blocked traversal sequences like ../ entirely. Any attempt to use them resulted in an error or the request being rejected.

But here’s the thing: if the application blocks relative paths, what about absolute paths?

Instead of trying to navigate up directories, I just told the server exactly where to go:

`GET /image?filename=/etc/passwd`
And it worked. The application was so focused on blocking ../ that it forgot to validate absolute paths.

How I found it: After my initial ../ payload was blocked, I tried different variations. When I used the absolute path /etc/passwd, the application happily served the file. This taught me that filters are often incomplete they block one thing but forget about another.

### Scenario 3: Non-Recursive Stripping

The third scenario had a filter that stripped out ../ sequences from the input. At first glance, this seems like a solid defense. But the filter had a fatal flaw: it only ran once.

Here’s what I mean. If I sent ../../../etc/passwd, the filter would remove the ../ sequences, leaving me with etc/passwd, which wouldn’t work.

But what if I nested the sequences? What if I sent ….// instead of ../?

When the filter removes ../ from …./, it leaves behind ../ again. So my payload became:

`GET /image?filename=….//….//….//etc/passwd`
The filter stripped out the middle characters, but the remaining characters formed valid traversal sequences.

How I found it: After realizing the filter was removing ../, I experimented with different patterns. The nested approach worked because the filter wasn’t recursive it only scanned the input once and didn’t check what remained after the removal.

### Scenario 4: Double URL Encoding

The fourth scenario was even more sophisticated. The application blocked path traversal sequences and then performed URL decoding on the input before using it.

This is actually a common pattern in web applications: decode the input, validate it, and then use it. But the order matters.

If the application decodes after validation, I can bypass the filter by double encoding my payload. Here’s how:

Normal: ../

URL encoded once: %2e%2e%2f

URL encoded twice: %252e%252e%252f


When I send the double-encoded version, the validation sees **%252e%252e%252f**, which doesn’t look like a traversal sequence. It passes validation. Then the application decodes it once, turning it into **%2e%2e%2f**. Finally, when the application uses it, the web server decodes it again, turning it into ../.

My payload:

`GET /image?filename=..%252f..%252f..%252fetc/passwd`
How I found it: I noticed that my normal traversal sequences were blocked, but when I tried URL encoding, the behavior changed slightly. That told me the application was doing some kind of decoding. I then tried double encoding, and it bypassed the filter completely.

### Scenario 5: Path Validation Bypass

The fifth scenario was the most realistic. The application validated that the supplied path started with the expected directory: /var/www/images/.

This is actually a good security practice, but it was implemented incorrectly. The application checked the prefix but didn’t canonicalize the path afterward.

So I could satisfy the validation by including the expected prefix, and then traverse out of it:

`GET /image?filename=/var/www/images/../../../etc/passwd`
The application saw /var/www/images/ at the start and approved it. But when the path was resolved, the ../ sequences navigated back out of that directory and into /etc.

How I found it: I noticed the application was rejecting paths that didn’t start with /var/www/images/. So I included that prefix in my payload and then added traversal sequences after it. The validation passed, and the traversal worked.

### Bonus Scenario: Null Byte Bypass (Legacy Systems)

There’s one more technique worth mentioning, though it only works on older systems. Some applications validate that the filename ends with a specific extension, like .png or .jpg.

On legacy systems (particularly older PHP versions), you can bypass this using a null byte (%00). The null byte terminates the string in the underlying C functions, so everything after it is ignored.

Payload:

`GET /image?filename=../../../etc/passwd%00.png`
The application sees .png at the end and approves it. But when the file is actually read, the null byte cuts off the string at /etc/passwd.

Note: This doesn’t work on modern systems anymore, but it’s still worth knowing for older applications.

### How to Fix Path Traversal

Now that we’ve seen how to exploit path traversal, let’s talk about how to fix it.

The best solution: Don’t use user input in file paths at all. Instead, use an ID or index that maps to a filename on the server side. For example:

**GET /image?id=123**

The server looks up ID 123 in a database and retrieves the corresponding filename. The user never controls the actual path.

If you must use user input:

1\. Validate against a whitelist of allowed files.

2. Canonicalize the path (resolve all ../ and symbolic links).

3. Verify the canonical path is still within the expected directory.

4. Use a secure file API that prevents traversal.


**Here’s an example in Java:**

```
File file = new File(BASE_DIRECTORY, userInput);
String canonicalPath = file.getCanonicalPath();
if (!canonicalPath.startsWith(BASE_DIRECTORY)) {
 throw new SecurityException("Invalid file path");
}
```
This ensures that no matter what tricks the attacker uses, the final path must be within the base directory.

## Final Thoughts

Path traversal is one of those vulnerabilities that seems simple on the surface but has endless variations in the real world. Every application implements its own filters and validation, which means you need to be creative and persistent.

And most importantly: always test ethically. Only test applications you have permission to test, whether that’s through bug bounty programs, penetration testing engagements, or practice labs like PortSwigger’s Web Security Academy.

If you have any questions or require further clarification, don’t hesitate to reach out. Additionally, you can stay connected for more advanced cybersecurity insights and updates:

🔹 GitHub: @0xEhab

🔹 X (Twitter): @[0xEhab](https://x.com/0xEhab)

🔹 Instagram: @[pjo\_](https://www.instagram.com/pjo_/)

Stay tuned for more comprehensive write-ups and tutorials to deepen your cybersecurity expertise. 🚀
