# Find XSS Vulnerabilities in Minutes

- **Source URL:** https://medium.com/@phirojshah20/find-xss-vulnerabilities-in-minutes-912d02d2b848?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502051435/https://medium.com/@phirojshah20/find-xss-vulnerabilities-in-minutes-912d02d2b848
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8381 (id 8381)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Find XSS Vulnerabilities in Minutes

Cross-Site Scripting (XSS) remains one of the most prevalent vulnerabilities in web applications. As a red teamer or a bug bounty hunter, identifying XSS vulnerabilities quickly and efficiently is crucial. In this article, I will walk you through a simple yet powerful process to find XSS vulnerabilities in just a few minutes using a streamlined one-liner command. Let’s get started!

# Step 1: Setting Up the Command

The first step is to copy the target website’s URL. Once you have the target URL, you can use the following one-liner command to initiate the XSS hunting process:

`echo example.com | gau | gf xss | uro | Gxss | kxss | tee xss_output.txt`
Now, let’s break down what each tool in this command does:

# Tool Breakdown

**GAU (Get All URLs)**:

GAU fetches old URLs from various passive sources like Wayback Machine, AlienVault, Common Crawl, and URLscan. These archived URLs are valuable for discovering hidden endpoints.

**GF Pattern (grep patterns)**:

The GF tool filters URLs to find those with parameters that are often vulnerable to XSS attacks. It uses predefined patterns to identify potential targets.

**URO (Unique URL Remover)**:

URO cleans up the results by removing duplicate URLs, ensuring you only have unique entries to test.

**Gxss (Get XSS)**:

Gxss checks URLs for parameters that reflect user input in the HTTP response, which is a common sign of XSS vulnerability.

**Kxss (Killer XSS)**:

Kxss further analyzes the URLs to identify unfiltered special characters that can be exploited for XSS attacks.

**tee**:

The `tee` command saves the output of the entire process into a file named `xss_output.txt`, so you can review and refine the results later.

# Step 2: Reviewing the Output

Once you run the command, you’ll get a list of URLs with reflected parameters that could be susceptible to XSS. The next step is to refine and validate the results to reduce noise and focus on real vulnerabilities.

# Refining the Results

To clean up the output and show only URLs with potentially vulnerable parameters, use the following command:

`cat xss_output.txt | grep -oP '^URL: \K\S+' | sed 's/=.*/=/' | sort -u > final.txt`
This command will:

- Extract only the URLs from the output.
- Remove everything after the `=` sign to focus on the parameters.
- Sort the results to ensure they are unique.

# Step 3: Exploiting with Loxs Tool

After refining the list, it’s time to exploit the potential XSS vulnerabilities using the **Loxs** tool.

# How to Use the Loxs Tool

1. Navigate to your Loxs tool folder.
2. Run the tool and select option **4** for XSS testing.
3. Enter the path to your `final.txt` file containing the filtered URLs.
4. Provide the path to your XSS payload file.
5. Hit Enter and let the tool perform the exploitation.

# Example Payloads

Make sure your payload file contains various XSS payloads to test different contexts and bypass filters.

# Conclusion

By following this streamlined process, you can efficiently identify and exploit XSS vulnerabilities in minutes. The one-liner command simplifies the initial reconnaissance, while tools like Gxss, Kxss, and Loxs help you refine and automate the exploitation phase. Stay safe, and happy hunting!
