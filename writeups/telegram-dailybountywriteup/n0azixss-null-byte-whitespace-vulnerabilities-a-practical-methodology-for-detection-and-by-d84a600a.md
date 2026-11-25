# Null Byte & Whitespace Vulnerabilities

- **Source URL:** https://medium.com/@N0aziXss/null-byte-whitespace-vulnerabilities-a-practical-methodology-for-detection-and-bypass-c88886444a87
- **Fetched from:** https://medium.com/@N0aziXss/null-byte-whitespace-vulnerabilities-a-practical-methodology-for-detection-and-bypass-c88886444a87?source=rss-ef3c608c2595------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14932 (id 14932)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** N0aziXss / Sun, 04 Oct 2026 03:45:34 GMT

Understanding Legacy Parsing Quirks and Their Modern Security Implications

By N0aziXss | Security Researcher | HackerOne & BugCrowd Validated

When developers validate user input, they often focus on the visible characters: letters, numbers, symbols. But two categories of characters frequently slip through the cracks: null bytes and whitespace.

Null bytes (0x00) and various whitespace characters (spaces, tabs, newlines) have caused some of the most subtle and dangerous vulnerabilities in web application history. While some issues are mitigated in modern languages, the core problem persists: applications often mishandle these characters when parsing, truncating, or filtering input.

✓ Null bytes can terminate strings in C-based systems

✓ Whitespace can bypass keyword filters and regex patterns

✓ File extension checks can be tricked

✓ Path traversal protections can be circumvented

✓ SQL and command injection filters can be evaded

✓ Understanding null byte and whitespace behavior

✓ Vulnerability map: where these issues appear

✓ Systematic testing methodology

✓ Conceptual bypass techniques

✓ Remediation and prevention

**Disclaimer:** This article is for educational and authorized security testing only. Always obtain proper permission before testing any system.

Definition:

A control character with the value zero. In many programming languages

and system calls, it marks the end of a string.

Representations:

- %00 (URL encoding)

- \0 (C/PHP string escape)

- 0x00 (hex)

- \x00 (hex escape)

Historical Behavior:

- C functions like strcmp(), fopen() stop at null byte

- PHP versions before 5.3.4 were vulnerable to null byte injection

- Java's file I/O also treats null byte as terminator

Definition:

Characters that represent horizontal or vertical space in typography.

Common Whitespace:

- Space (0x20, %20)

- Tab (0x09, %09)

- Newline (0x0A, %0A)

- Carriage Return (0x0D, %0D)

- Vertical Tab (0x0B, %0B)

- Form Feed (0x0C, %0C)

Unicode Whitespace:

- Non-breaking space (U+00A0)

- En space, em space, thin space

- Zero-width space (U+200B)

1\. String Truncation:

Null byte truncates strings in C-based functions.

2. Parsing Differences:

Different components (browser, server, database) interpret

whitespace differently.

3. Filter Evasion:

Regex patterns often miss variations in whitespace.

4. Encoding Confusion:

Double encoding can bypass simple decoders.

┌─────────────────────────────────────────────────────────────────────┐

│ NULL BYTE VULNERABILITY MAP │

└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────┐

│ Null Byte (0x00) │

└──────────┬──────────┘

│

┌──────────────────────┼──────────────────────┐

│ │ │

▼ ▼ ▼

┌───────────────┐ ┌───────────────┐ ┌───────────────┐

│ File Upload │ │ Path Traversal│ │ Input │

│ Extension │ │ / LFI │ │ Validation │

│ Bypass │ │ │ │ Bypass │

└───────┬───────┘ └───────┬───────┘ └───────┬───────┘

│ │ │

▼ ▼ ▼

┌───────────────┐ ┌───────────────┐ ┌───────────────┐

│ Upload │ │ Read Sensitive│ │ Truncate │

│ Malicious │ │ Files │ │ Input to │

│ File │ │ │ │ Bypass Check │

└───────────────┘ └───────────────┘ └───────────────┘

┌─────────────────────────────────────────────────────────────────────┐

│ WHITESPACE VULNERABILITY MAP │

└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────┐

│ Whitespace │

│ Variations │

└──────────┬──────────┘

│

┌──────────────────────┼──────────────────────┐

│ │ │

▼ ▼ ▼

┌───────────────┐ ┌───────────────┐ ┌───────────────┐

│ SQL Injection │ │ Command │ │ Filter │

│ Keyword │ │ Injection │ │ Evasion │

│ Bypass │ │ Bypass │ │ │

└───────┬───────┘ └───────┬───────┘ └───────┬───────┘

│ │ │

▼ ▼ ▼

┌───────────────┐ ┌───────────────┐ ┌───────────────┐

│ Bypass WAF │ │ Execute │ │ Access │

│ or Input │ │ Commands │ │ Restricted │

│ Filter │ │ │ │ Content │

└───────────────┘ └───────────────┘ └───────────────┘

\# Identify Input Points

1. File Upload Endpoints:

- Check file extension validation

- Test filename handling

- Observe error messages

2. File Inclusion Parameters:

- Look for ?page=, ?file=, ?template=

- Test path traversal attempts

- Note how paths are appended

3. SQL Query Inputs:

- Identify parameters used in queries

- Test simple SQL injection

- Observe error messages

4. Command Execution Points:

- Any feature that runs system commands

- Test with simple input

- Note filtering behavior

\# Non-Intrusive Observation

1. Identify a parameter that validates file extensions:

- Example: ?file=report.pdf

- Server checks if extension is .pdf

2. Test null byte truncation:

- Send value that includes null byte before extension

- Observe if server accepts a different extension

3. Document behavior:

- Does the server reject null byte?

- Does it truncate the string?

- Is the response different?

Note: Do not attempt to upload malicious files.

Just observe how the server handles the null byte.

\# Testing Filter Evasion

1. Identify an input that filters keywords:

- Example: SQL injection attempt blocked

- Filter blocks "SELECT" or "UNION"

2. Test whitespace alternatives:

- Replace spaces with tabs, newlines, comments

- Observe if the filter is bypassed

3. Document which variations work:

- URL-encoded whitespace

- Inline comments (/\*\*/)

- Plus signs (+)

Note: This is conceptual. Do not attempt to exploit.

Use only on systems you own or have permission to test.

\# Conceptual Testing

1. Identify a file inclusion point:

- Example: ?page=home.php

- Server appends .php extension

2. Test null byte truncation:

- Send value that truncates before .php

- Attempt to include arbitrary file

3. Observe:

- Does the server stop at null byte?

- Can you read /etc/passwd? (in a test environment)

Note: Only test in a controlled lab environment.

\# Reporting Findings

For each finding, document:

- Endpoint and parameter

- Input sent (conceptual, not exploit code)

- Server response

- Expected vs actual behavior

- Security impact

- Remediation recommendation

\- %00 (URL encoded)

- %2500 (double encoded)

- \0 (string escape)

- \x00 (hex escape)

-%00%00 (multiple null bytes)

Note: Modern languages (PHP 5.3.4+, Java, Python) reject null bytes

in most file operations. This is primarily a legacy issue.

\- %20 (space)

- %09 (tab)

- %0A (newline)

- %0D (carriage return)

- %0B (vertical tab)

- %0C (form feed)

- + (plus sign, in URL encoding)

- /\*\*/ (inline comment in SQL)

- () (parentheses, sometimes)

- Unicode whitespace: %C2%A0, %E2%80%8B

Use Case: Bypassing keyword filters in SQL injection.

\- Double URL encoding: %2500 → %00

- Unicode encoding: %u0000

- Overlong UTF-8: %C0%80 for null byte

Note: Most modern parsers reject overlong encodings.

In PHP versions before 5.3.4, null bytes could truncate strings

in file functions. Attackers could bypass extension checks:

Example concept: shell.php%00.jpg would be treated as shell.php

because the null byte terminated the string before the extension.

This was patched in PHP 5.3.4 (2011).

Web Application Firewalls (WAFs) often use regex to block attacks.

Attackers have bypassed WAFs by using unusual whitespace characters

that the regex did not account for.

Example: SQL keywords separated by newlines instead of spaces.

Java's file I/O has historically been vulnerable to null byte

injection in some contexts, but modern Java versions reject

null bytes in file paths by throwing exceptions.

✅ DO:

• Use modern language versions (PHP 5.3.4+, Java 7+)

• Validate input against a whitelist

• Sanitize filenames before use

• Use built-in functions for path handling

• Reject input containing null bytes

• Normalize whitespace before validation

• Use parameterized queries (for SQL)

❌ DON'T:

• Rely on blacklists (they always miss variants)

• Trust client-side validation

• Use string concatenation for file paths

• Assume whitespace is always a space

✅ DO:

• Test null byte in file upload parameters

• Test whitespace variations in injection attempts

• Document behavior, not just presence

• Use a controlled lab environment

• Report findings responsibly

❌ DON'T:

• Use null byte or whitespace to exploit production systems

• Share actual exploit payloads

• Test without authorization

\- Content-Security-Policy: helps mitigate injection impacts

- X-Content-Type-Options: nosniff

- Proper file upload validation on server side

- WAF rules updated for whitespace variations

□ Identify file upload endpoints

□ Test null byte in filename (conceptual)

□ Identify file inclusion parameters

□ Test null byte in path traversal

□ Identify SQL injection points

□ Test whitespace bypass for keyword filters

□ Identify command injection points

□ Test whitespace alternatives for commands

□ Document all findings with evidence

□ Verify fixes with regression testing

┌─────────────────────────────────────────────────────┐

│ PHASE 1: RECON │

│ • Map input points │

│ • Identify validation mechanisms │

│ • Note error messages │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│ PHASE 2: NULL BYTE │

│ • Test file extension validation │

│ • Test path traversal truncation │

│ • Observe server behavior │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│ PHASE 3: WHITESPACE │

│ • Test SQL keyword filters │

│ • Test command injection filters │

│ • Document bypass variations │

└─────────────────────────────────────────────────────┘

│

▼

┌─────────────────────────────────────────────────────┐

│ PHASE 4: DOCUMENTATION │

│ • Clear findings │

│ • Risk assessment │

│ • Remediation guidance │

└─────────────────────────────────────────────────────┘

1\. Null bytes and whitespace are often overlooked

2. Legacy systems may still be vulnerable

3. Test both in file operations and injection contexts

4. Document behavior, not just presence

5. Always test ethically and with authorization

1\. Use modern language versions

2. Whitelist validation is essential

3. Reject null bytes in file paths

4. Normalize whitespace before filtering

5. Test your own applications against these vectors

**The smallest characters can cause the largest breaches.**

**A null byte is invisible. A whitespace variation is easy to miss. Together, they have bypassed countless security controls.**

**Validate everything. Trust nothing.**

N0aziXss is an experienced security researcher specializing in web application security and bug bounty hunting, with multiple validated discoveries across various platforms.
