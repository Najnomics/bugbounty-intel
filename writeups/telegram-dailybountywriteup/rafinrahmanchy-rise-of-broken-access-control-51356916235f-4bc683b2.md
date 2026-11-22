# Rise of Broken Access Control

- **Source URL:** https://medium.com/@rafinrahmanchy/rise-of-broken-access-control-51356916235f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105131326/https://medium.com/@rafinrahmanchy/rise-of-broken-access-control-51356916235f
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4583 (id 4583)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Rise of Broken Access Control

## Why authorization flaws are trendy and easier to discover

--

The latest OWASP Top 10 project was published two years ago. We saw broken access control (BAC) at the top, which was fifth in the previous list. Whenever we open social media, we observe people regularly receiving bounties for bugs like IDOR, Privilege Escalation, CSRF, etc. Here we will see the evolution of broken access control, exploring why it is prevalent and easier to discover. Finally, we will discuss how various professionals should address these issues. I wrote this article after researching broken access control for a long time. Hope you can take full advantage of my experience! Read till the end with patience.

# Evolution

The table above illustrates the evolution of broken access control over the years. The latest OWASP Top 10 merged 34 Common Weakness Enumerations (CWEs) into the broken access control category due to their similarity, elevating it to the top position. I assume the audience here knows these flaws as it’s a technical write-up. Broken access controls typically fall under the ‘Authorization Testing’ section of OWASP Web Security Testing Guide (WSTG). While testing these weaknesses, you’ll find their impact pretty close. Which is unauthorized access, modification, and/or disruption by insufficient/malformed permission requests. We will try to understand this by discussing some notable security bugs in the group. For that, we’ve chosen IDOR, Path Traversal, and CORS Misconfiguration.

“The best way to understand is a few good examples.”

— Isaac Newton


## IDOR

IDOR or Insecure Direct Object Reference is a common access control vulnerability. It allows attackers to orchestrate user-supplied input to infiltrate others’ objects. This input could be a session token, user ID, directory, file name, etc. IDOR occurs when attackers can steal/guess these unique identifiers to violate authorization. More specifically, the substitution of claim fools the server as if it’s the legitimate user’s action. Platform misconfiguration and mass assignment can also cause IDOR. IDOR leads to unauthorized view, modification, or disruption of users’ property. You’ve to set the URL, HTTP header, cookie, or POST data accordingly. IDOR is basically horizontal privilege escalation. Threat actors can do anything with IDORs. Such as PII extraction, account take-over, posting on another’s behalf, deleting others’ data, and so on. Primarily there are four types of IDOR.

**Basic IDOR:** Editing HTTP request to directly retrieve the result. The attacker can see the changes made by him instantly. We all are aware of this kind of IDOR.

**Blind IDOR:** Opposite of Basic IDOR. Here the output is shown indirectly via another channel e.g. page or media. It means you won’t see any indication of success or result in the immediate response.

**Second Order IDOR:** As per my study, there are two occurrences of 2nd order IDOR. In the first, the HTTP response message is contradictory. One part (typically the header portion) will show a negative or error sign, and the other part (typically the response body) will show the desired result! The second one is a bit complex. Here the attacker needs to modify a request from the sequence. The attacker forges that request with the victim’s identity to compromise his session. Detailed writeup [here](https://ozguralp.medium.com/a-less-known-attack-vector-second-order-idor-attacks-14468009781a).

**File-based IDOR:** Explicitly/massively being able to download people’s files. Using target-specific dork, predictable file name/location, and brute-forcing with sequential file name/extensions are usual methods for it.

## CORS Misconfiguration

CORS defines who, what and how can access cross-origin resources from a web server. Here ‘who’ refers to authorized subdomains and third-party sites. ‘What’ refers to the ability to view credentials. And ‘how’ refers to the allowed request methods. Browsers determine these by observing the ‘ACAO’ ‘ACAC’ and ‘ACAM’ headers respectively. Although there are many more CORS headers out there, I’ve mentioned the relevant ones. CORS essentially provides API access to origins outside of SOP through browsers. If these headers are poorly configured, an attacker can impersonate a victim. The workflow of CORS misconfiguration is described below. Assume the target website is siteofvictim.com and siteofhacker.com is the origin controlled by the attacker.

1) The user is logged into both sites at the same time.

2) siteofhacker.com hosts a malicious script that is rendered by the browser.

3) The script sends a privileged request to siteofvictim.com on behalf of the user. 

4) siteofvictim.com sends requested data and CORS headers to the browser.

5) The browser then attaches the required data to siteofhacker.com’s response.

Threat actors can achieve CORS misconfiguration in many ways. Such as hosting a fake website, exploiting existing domain’s vulnerability (e.g. XSS, subdomain take-over), broken parsers and so on.

## Directory Traversal

Directory/path traversal allows us to abuse user-controlled input to access files outside the web root. The attacker achieves this by inserting a directory/file name with a combination of slashes and dots at potential entry points. Examples are shown below.

[https://redacted.com/page?file=/etc/passwd](https://redacted.com/page?file=%2Fetc%2Fpasswd)

[https://redacted.com/page/../../etc/passwd](https://redacted.com/page/../../etc/passwd)

[https://redacted.com/page/file=content.ini..%2F..%2F..%2F..%2Fetc%2Fpasswd](https://redacted.com/page/file=content.ini..%2F..%2F..%2F..%2Fetc%2Fpasswd)

The crafting of a payload depends on various criteria, such as the web server used, current path, and filters. You have to try valid and invalid inputs in different parts of the endpoint until you observe any symptoms. Verbose errors are the best way to weaponize payloads. LFI and path traversal are similar, the only difference is in read and execute. Improper input handling and the usage of risky programming features can cause this vulnerability. Path traversal can be leveraged for RCE. From reading system files, perpetrators are also able to take-over the backend server.

Apart from these, there are many other weaknesses. These include Privilege Escalation, CSRF, Open Redirects, etc. I will discuss the above and others in the future.

# Why is it So Common?

After reading till now, you might’ve realized that access control bugs are quite available nowadays. There are different reasons for the abundance of authorization issues.

- Attack surface is huge
- Easy to learn and find
- Harder to remediate

## Never-ending Attack Surface

Broken access control consists of a large set of security glitches. Each issue also has categories and subcategories mentioned above. Making its attack surface comparatively broader than other vulnerability sections. Other vulnerabilities typically have limited risk factors. Like, Injections occur only when input fields are not validated against dangerous data. XXE takes place in XML-based applications. The sign-in form typically contains authentication vulnerabilities only. But Authorization flaws can arise in any feature or type of application, irrespective of design and technologies used. When the developer creates a functionality, he directly or indirectly assigns some permission there. A malicious user tries to use it in an alternative way. As organizations adopt an array of applications, cloud services, and interconnected platforms, the permutations of potential vulnerabilities multiply exponentially. Each misstep in access control configuration widens the surface area available for exploitation, offering adversaries a vast playground to probe and compromise.

## Simplicity

If you study access control vulnerabilities, you’ll realize how easy they are to learn and identify in web applications. You don’t need any in-depth technical knowledge. I’d say almost any level of learner can learn to discover broken access controls by following some tutorials on the internet. For now, just knowing the fundamentals of HTTP, HTML and web technologies will be enough. I also found a couple of authorization flaws at the very beginning of my learning! Finding access control vulnerabilities doesn’t require any heavy setup. Even you can spot them by using browser or its Developer tools. Especially simple IDORs, Privilege Escalation, GET CSRF and information disclosure via Google Hacking. Learning any interception proxy (e.g. Burp Suite, OWASP ZAP or Fiddler) will enable you to find numerous access control bugs. You can find all types of IDOR, parameter pollution, CORS misconfiguration, Path traversal and CSRF this way. I’d suggest going with Burp Suite for its rich collection of [extensions](https://portswigger.net/bappstore). There are also many asset discovery tools for attack surface expansion. Such as gau, GauPlus, waybackurls, ParamSpider, Arjun, Ffuf, Gobuster and DirBuster. These tools can find hidden endpoints where access controls are broken.

## Challenging Remediation

As mentioned earlier, the attack surface of authorization hardly has limits. So we can’t protect all endpoints despite desire. Especially for applications with diverse user roles, intricate permission structures, and dynamic nature. Then it becomes difficult, time-consuming and expensive to resolve access control-related problems. As an application grows, it becomes more difficult to close authorization gaps. Sometimes series of patches are circumvented by attackers. That’s why broken access control is a nightmare for many developers.

# Statistics

Now let’s see the numbers which will make our statements more solid. Although we’ve discussed the OWASP Top 10 project, now we will go through other stats. Let’s observe both organizational and individual data.

As you can see above, the ranking and bounties for access control issues have been increased. Which clearly means that broken access controls are extensively available. According to [HackerOne](https://www.hackerone.com/top-ten-vulnerabilities), *“Awards for Improper Access Control increased 134% year over year to just over US$4 million”*.

Talking about stats, SANS/CWE Top 25 Software Errors can’t be ignored. It has highlighted five broken access controls in the last [edition](https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html). Where two major issues (CWE-862: Missing Authorization and CWE-863: Incorrect Authorization) have been moved to more upper position.

Enough of the official dataset. It’s time to look what our community folks are doing.

It seems that most offensive security professionals are overwhelmed with access control flaws! And now we know the reasons behind that.

# What Should You Do?

By ‘you’ I mean anyone who is reading the article. He/she can be a developer, administrator, DevOps engineer, security analyst, security architect, penetration tester, auditor, bug bounty hunter or anyone who is working with a web-based client or organization. So as a whole, I wrote about two generic groups. Because some tasks can overlap between each roles from the particular group. I hope you’re vigilant enough to understand it.

## For Testers

- Read documentations to understand access management, technical specifications and test cases. Especially from user documentations, QA and RFCs.
- Create multiple account with different user and roles. For instance, userA, userB, adminC and moderatorD. It will enable you to test all kinds of privilege escalation.
- Utilise all functionality with different permissions (public, private, custom, person with link/invitation) to expand the attack surface.
- Setup the tools (e.g. proxy, browser, wordlist, scripts) accordingly for assessment purpose. Customize your own checklists for testing.
- In black box testing, inspect and modifying traffics, match/replace, macro, extensions for testing authorization are required. Burp Suite and OWASP ZAP have all these feature.
- In white box testing, use a static analysis tool by following code review guide. The methodology must comply with the application’s context to avoid invalid results. Semgrep is comparatively effective here.
- Find sensitive/hidden endpoints from source code, JavaScript enumeration, crawling, parameter discovery, APIs, Github, Google hacking, Wayback Machine, fuzzing etc. This way you can obtain unprotected functionality, secret IDs, tokens, confidential files etc. Pleanty of technique/toolings are available to simplify these.
- Test the application thoroughly instead of basic strategy. Like most people try IDOR by changing numbers in URL. But forget about HTTP verbs, alphanumeric ID, API version, special characters and POST data.
- Try different attack techniques. Such as parameter pollution, stripping token header/parameter, tampering/replaying with metadata (cookie, JWT, access token, hidden field), mass assignment, race condition, forced browsing, 4xx bypass etc.
- Test premium services whether they can be used without paying. You might need to purchase them.
- Review the system and application logs for unauthorized access attempts. From there you can extract the payload of the exploit.
- Retest the patches as sometimes they’re poorly implemented. This [report](https://bugreader.com/drix17@csrf-bypass-in-use-data-to-view-photos-and-videos-75) is an example that even strong security teams can make such mistakes.
- For crowdsource testers, chain vulnerabilities from/to BAC or try less-known attack vectors. This is just an advice to overcome duplicate or burnouts.

## For Developers

- Implement access control matrix to map roles to dedicated resource or functions.
- Ensure that the language/framework you use follows effective security practices against authorization vulnerabilities.
- Never rely on security by obscurity.
- Assign secure session IDs which must be unique, unguessable, secret and dynamic.
- Do authorization check on each request.
- Enforce re-authentication on sensitive actions.
- Avoid client-side control enforcement.
- Implement access control model based on compliance reqirement and business needs.
- There are several methods to prevent IDOR. Such as, avoiding direct object references using GUIDs, authN/authZ checks and input sanitization.
- The security of modern apps is aligned with business rules. Such as, nobody can edit a shopping cart after payment, locked contents shouldn’t be used without unlocking, and functions should be restricted after policy violation/access revocation. So developers should apply access control on each layer or step.
- Limit CORS to block requests from malicious origins.
- Rate limit API endpoints to prevent automated attacks.
- Some action is limited to a certain time frame or a certain number of attempts. Like 30 day restriction, promo code with 90 enrollments, voucher with 1 month subscription, 5 downloads/day, etc. Proper server-side validation and session management can eliminate TOCTOU/business logic flaws related to them.
- Enforce the principle of least privilege.
- Deny by default everything except public contents.
- Disable web server directory listing and ensure the root directory doesn’t contain sensitive files.
- Enforce logging and monitoring of access control failures.
- Disable client-side caching of sensitive data.
- Use a central application-wide interface to regulate access controls.
- Regularly audit and test access controls to check their effectiveness.

# Conclusion

So that’s all for today. This article provides a comprehensive guide and motivation for identifying access control bugs. These can be discovered and exploited in many ways. Some test cases are simple and some are complicated. I promise to discuss all of them in the future. Stay tuned for more insightful articles.
