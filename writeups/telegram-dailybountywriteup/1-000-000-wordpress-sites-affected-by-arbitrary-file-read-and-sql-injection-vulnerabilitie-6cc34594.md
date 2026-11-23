# 1,000,000 WordPress Sites Affected by Arbitrary File Read and SQL Injection Vulnerabilities in…

- **Source URL:** https://wordfence.medium.com/1-000-000-wordpress-sites-affected-by-arbitrary-file-read-and-sql-injection-vulnerabilities-in-9e93f9767569?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260517104920/https://wordfence.medium.com/1-000-000-wordpress-sites-affected-by-arbitrary-file-read-and-sql-injection-vulnerabilities-in-9e93f9767569
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13557 (id 13557)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 1,000,000 WordPress Sites Affected by Arbitrary File Read and SQL Injection Vulnerabilities in Avada Builder WordPress Plugin

On March 21, 2026, the Wordfence Intelligence Vulnerability Database received submissions for two vulnerabilities in Avada Builder, a widely used WordPress plugin with an estimated 1,000,000 active installations.

The vulnerabilities, an authenticated arbitrary file read and an unauthenticated SQL injection, were discovered and responsibly reported by researcher Rafie Muhammad through the Wordfence Bug Bounty Program.

Rafie earned a combined $4,453.00 in bounties for these discoveries ($3,386.00 for the arbitrary file read and $1,067.00 for the SQL injection).

Avada Builder is a popular page builder plugin used alongside the Avada theme, one of the best-selling WordPress themes available. Given the plugin’s wide adoption, these vulnerabilities represent a notable disclosure that WordPress site owners should be aware of.

This article provides an overview of both vulnerabilities, their impact, patch status, and the protection available through the Wordfence firewall.

## Vulnerability Details

## CVE-2026–4782: Authenticated (Subscriber+) Arbitrary File Read

- **CVSS Score:** 6.5 (Medium)
- **Affected Versions:** Avada Builder \<= 3.15.2
- **Patched Version:** 3.15.3

The Avada Builder plugin is vulnerable to arbitrary file read in all versions up to, and including, 3.15.2 via the \`fusion\_get\_svg\_from\_file\` function with the \`custom\_svg\` parameter of the \`fusion\_section\_separator\` shortcode.

The function does not include file type or file source checks, which means that not only SVG files can be loaded, but PHP files can be as well.

Authenticated attackers with subscriber-level access and above can exploit this to read the contents of arbitrary files on the server. This could include the site’s \`wp-config.php\` file, which contains database credentials as well as cryptographic keys and salts.

Although the function is nonce-protected, the nonce can be obtained by authenticated users in the vulnerable version, and there is no capability check on the associated AJAX function.

The vulnerability was partially patched in version 3.15.2 and fully patched in version 3.15.3.

## CVE-2026–4798: Unauthenticated SQL Injection

- **CVSS Score:** 7.5 (High)
- **Affected Versions:** Avada Builder \<= 3.15.1
- **Patched Version:** 3.15.2

The Avada Builder plugin is vulnerable to time-based SQL injection via the \`product\_order\` parameter in all versions up to, and including, 3.15.1. The vulnerability exists because the \`ORDER BY\` statement is added to the query without using the WordPress \`wpdb::prepare()\` function. While the \`sanitize\_text\_field()\` function is applied to the input, it does not protect against SQL injection.

Unauthenticated attackers can append additional SQL queries into already existing queries to extract sensitive information from the database, such as password hashes.

Because union-based SQL injection is not possible due to the query structure, exploitation requires a time-based blind approach using SQL CASE statements and the SLEEP() command.

It is important to note that this vulnerability only critically affects sites where WooCommerce was previously used and then deactivated. The relevant database tables from WooCommerce must exist for the vulnerable code path to be reached.

This vulnerability was patched in version 3.15.2, released on April 13, 2026.

## Impact

Avada Builder has an estimated 1,000,000 active installations. The arbitrary file read vulnerability could allow attackers to obtain database credentials and cryptographic security keys from \`wp-config.php\`.

The SQL injection vulnerability could allow extraction of password hashes and other sensitive data from the database.

Together, these vulnerabilities could provide attackers with the information needed to further compromise an affected site.

## Patch Status

The Avada team was notified through the Wordfence Vulnerability Management Portal on March 24 and 25, 2026, and acknowledged the reports promptly.

The first patch, version 3.15.2, was released on April 13, 2026, addressing the SQL injection vulnerability and partially addressing the arbitrary file read vulnerability. The fully patched version, 3.15.3, was released on May 12, 2026.

Site owners running Avada Builder should update to version 3.15.3 to ensure both vulnerabilities are fully addressed.

## Protection

Wordfence Premium, Wordfence Care, and Wordfence Response users received a firewall rule to protect against exploits targeting the arbitrary file read vulnerability on March 25, 2026.

Sites using the free version of Wordfence received the same protection 30 days later, on April 24, 2026.

All Wordfence users, including those on the free version, are protected against the SQL injection vulnerability by the Wordfence firewall’s built-in SQL injection protection.

## Conclusion

Two vulnerabilities in the Avada Builder plugin have been responsibly disclosed, patched, and documented.

Rafie Muhammad’s contributions through the Wordfence Bug Bounty Program led to the identification and resolution of both issues.

Site owners using Avada Builder should verify that their installations are updated to version 3.15.3. Review the report to ensure your site is not affected.

*Originally published on the \[Wordfence Blog\](https://www.wordfence.com/blog/2026/05/1000000-wordpress-sites-affected-by-arbitrary-file-read-and-sql-injection-vulnerabilities-in-avada-builder-wordpress-plugin/).*
